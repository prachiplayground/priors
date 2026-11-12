# pipeline

Stages, run in order and resumable per source via `data/manifest.csv`:

1. **collect**: add candidate URLs from seed lists and RSS feeds to the manifest.
2. **fetch** ✅ `fetch.py`: save source text to `data/raw/` (private). Respects robots.txt, waits between requests, flags pages that yield too little text (paywalls, JS pages, abstract-only pages).
2b. **triage**: score each source on the [triage rubric](../docs/source-triage.md) and assign its role. Only `decision` sources continue to extraction.
3. **classify**: assign primary and secondary category buckets.
4. **extract**: split each source into decision records and fill fields against `schema/decision_record.schema.json`, with an evidence pointer per field.
5. **link**: resolve `builds_on` / `superseded_by`, normalize company and author names.
6. **validate**: hand-review a sample; record field-level accuracy in `evals/`.

Stages 3–6 come next, after the gold set (see [ROADMAP.md](../ROADMAP.md)).
