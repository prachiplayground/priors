"""Fetch source texts for extraction.

Reads data/manifest.csv, downloads every source with status `found`, extracts
readable text, and saves it under data/raw/ (git-ignored, never published).
Updates each row's status to `fetched`, or records the error in `notes`.

Usage:
    python pipeline/fetch.py                 # fetch everything still at `found`
    python pipeline/fetch.py --only ID [ID]  # fetch specific source_ids
    python pipeline/fetch.py --force         # re-fetch even if already fetched
    python pipeline/fetch.py --dry-run       # show what would be fetched

Podcasts and books are skipped: podcasts go to the staging dataset
(decision 0006) and books are noted by hand.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import time
import urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
import trafilatura
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "manifest.csv"
RAW = ROOT / "data" / "raw"

USER_AGENT = "priors-research-bot/0.1 (+https://github.com/prachiplayground/priors)"
SKIP_TYPES = {"podcast", "book"}
DELAY_SECONDS = 2.0  # be polite between requests
MIN_CHARS = 1500  # below this, extraction probably failed (paywall, JS page, abstract only)

_robots_cache: dict[str, urllib.robotparser.RobotFileParser | None] = {}


def allowed_by_robots(url: str) -> bool:
    """Respect robots.txt. If it can't be read, assume allowed."""
    parts = urlparse(url)
    base = f"{parts.scheme}://{parts.netloc}"
    if base not in _robots_cache:
        rp = urllib.robotparser.RobotFileParser()
        try:
            resp = requests.get(f"{base}/robots.txt", headers={"User-Agent": USER_AGENT}, timeout=15)
            if resp.status_code >= 400:
                _robots_cache[base] = None
            else:
                rp.parse(resp.text.splitlines())
                _robots_cache[base] = rp
        except requests.RequestException:
            _robots_cache[base] = None
    rp = _robots_cache[base]
    return True if rp is None else rp.can_fetch(USER_AGENT, url)


def pdf_to_text(data: bytes) -> str:
    reader = PdfReader(io.BytesIO(data))
    return "\n\n".join((page.extract_text() or "") for page in reader.pages)


def html_to_text(html: str, url: str) -> str:
    text = trafilatura.extract(
        html, url=url, include_comments=False, include_tables=True, favor_recall=True
    )
    return text or ""


def fetch_one(row: dict) -> tuple[str, str]:
    """Return (status, note). Writes data/raw/<id>.txt and <id>.meta.json on success."""
    source_id = row["source_id"]
    url = (row.get("fetch_url") or "").strip() or row["url"]

    if urlparse(url).path in ("", "/"):
        return "found", f"URL is a site homepage, not a specific page: {url}"

    if not allowed_by_robots(url):
        return "found", f"blocked by robots.txt: {url}"

    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=60)
    if resp.status_code >= 400:
        return "found", f"HTTP {resp.status_code} for {url}"

    content_type = resp.headers.get("content-type", "").lower()
    is_pdf = "pdf" in content_type or url.lower().endswith(".pdf") or resp.content[:5] == b"%PDF-"
    text = pdf_to_text(resp.content) if is_pdf else html_to_text(resp.text, url)

    if len(text) < MIN_CHARS:
        return "found", f"only {len(text)} chars extracted from {url}; check for paywall, JS rendering or abstract-only page"

    RAW.mkdir(parents=True, exist_ok=True)
    (RAW / f"{source_id}.txt").write_text(text, encoding="utf-8")
    meta = {
        "source_id": source_id,
        "fetched_from": url,
        "canonical_url": row["url"],
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "format": "pdf" if is_pdf else "html",
        "chars": len(text),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }
    (RAW / f"{source_id}.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return "fetched", f"{len(text):,} chars ({meta['format']})"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", nargs="+", metavar="ID", help="source_ids to fetch")
    parser.add_argument("--force", action="store_true", help="re-fetch sources already fetched")
    parser.add_argument("--dry-run", action="store_true", help="list what would be fetched, change nothing")
    args = parser.parse_args(argv)

    with MANIFEST.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    todo = [
        r for r in rows
        if r["source_type"] not in SKIP_TYPES
        and (args.force or r["status"] == "found")
        and (not args.only or r["source_id"] in args.only)
    ]
    print(f"{len(todo)} source(s) to fetch")

    ok = 0
    for i, row in enumerate(todo, 1):
        label = f"[{i}/{len(todo)}] {row['source_id']}"
        if args.dry_run:
            print(f"{label}: would fetch {(row.get('fetch_url') or '').strip() or row['url']}")
            continue
        try:
            status, note = fetch_one(row)
        except Exception as exc:  # keep going; record the failure in the manifest
            status, note = "found", f"error: {type(exc).__name__}: {exc}"
        row["status"], row["notes"] = status, note
        ok += status == "fetched"
        print(f"{label}: {status} - {note}")
        time.sleep(DELAY_SECONDS)

    if not args.dry_run:
        with MANIFEST.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nDone: {ok}/{len(todo)} fetched. Failures are noted in data/manifest.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
