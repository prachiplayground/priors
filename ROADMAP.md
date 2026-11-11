# Roadmap

Eight phases take priors from scaffold to launch, roughly 12 weeks at 8–10 hours a week. Each phase ends at a gate that must pass before the next begins, and each leaves a public artifact. Decisions made along the way are logged in [docs/decisions](docs/decisions/).

| Phase | Gate to pass | Public artifact | Status |
| --- | --- | --- | --- |
| 0. Setup | Manifest complete; all sources fetched locally | Repo, schema, decision log, fetch script | 🟡 In progress |
| 1. Gold set | 5 sources hand-labeled into decision records; schema fits them | Gold set + labeling guide | ⚪ Not started |
| 2. Extraction v1 | ≥ 90% core-field accuracy against the gold set | Extraction eval report | ⚪ Not started |
| 3. Dataset v0.1 | 30 sources extracted and reviewed | Hugging Face dataset + datasheet | ⚪ Not started |
| 4. Co-writer prototype | Dogfood PRD written; "evidence, not decisions" pass rate measured | priors' own PRD + rubric results | ⚪ Not started |
| 5. Discovery (alongside 2–4) | 8–10 PM interviews synthesized | Discovery write-up | ⚪ Not started |
| 6. Scale to v1.0 | 300+ sources, ≥ 20 decisions per bucket, accuracy holds | Dataset v1.0 + retrieval eval | ⚪ Not started |
| 7. App + MCP server | A stranger can use it end to end | Live explorer, co-writer, structured-query MCP server | ⚪ Not started |
| 8. Launch and learn | Launched with first usage metrics | Case-study write-up | ⚪ Not started |

## Why this order

- **The gold set comes before automation.** Hand-labeled records are the answer key every eval is scored against, and labeling them is how schema problems surface early.
- **The co-writer is tested in a Claude Project before any app exists.** It's the cheapest test of the core idea.
- **Discovery runs alongside the build,** so what PMs say can still change how the dataset scales.
- **Scale comes after quality.** Volume is easy to add and hard to clean up.

## Running the pipeline

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python pipeline/fetch.py --dry-run   # preview
python pipeline/fetch.py             # fetch sources to data/raw/ (private)
```
