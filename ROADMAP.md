# Roadmap

priors is a research proof of concept. The roadmap is built around one question:

> **Does sparring with real product precedent help PMs think through decisions, or is it just interesting reading?**

The plan is to answer it with the smallest working system first, and invest in automation and scale only if the answer is yes. Each phase ends at a gate and leaves a public artifact. Decisions are logged in [docs/decisions](docs/decisions/); the study design is in [docs/study](docs/study/).

| Phase | Weeks | Gate to pass | Public artifact | Status |
| --- | --- | --- | --- | --- |
| 0. Setup | 0 | Corpus collected, schema drafted, repo public | Repo, schema, decision log, fetch script | ✅ Done |
| 1. Build the POC | 1 | Pilot sources [triaged](docs/source-triage.md); 10–15 decisions hand-structured from decision sources; `think`, `audit` and the verifier run end to end ([design](docs/poc-design.md)) | Curated decision set + skill-shaped prototype | 🟡 Next |
| 2. Study round 1 | 2 | 3–4 PM sessions recorded and analyzed against the baseline | Round 1 findings | ⚪ |
| 3. Improve | 3 | Changes made for each top finding, each logged with its reason | Changelog: round 1 → round 2 | ⚪ |
| 4. Study round 2 | 4 | 3–4 new PM sessions; measures compared with round 1 | Round 2 findings + before/after | ⚪ |
| 5. Decide | 5 | Clear go / pivot / stop on scaling, based on study evidence | Decision log entry + case-study draft | ⚪ |
| 6. Scale (if go) | 6–9 | Automated extraction ≥ 90% accurate vs. the curated set; more areas added | Dataset on Hugging Face + extraction eval | ⚪ |
| 7. App + MCP server (if go) | 9–11 | A stranger can use it end to end | Live explorer, co-thinker, structured-query MCP server | ⚪ |
| 8. Publish the case study | 12 | Write-up with recorded evidence and the improvement loop | Case study | ⚪ |

## Why this order

- **Value before scale.** Hand-structured decisions are enough to test whether precedent helps. Automated extraction only matters once the answer is yes.
- **The curated set does double duty.** The 10–15 hand-written decision records are both the POC's knowledge base and the gold set that automated extraction will later be scored against.
- **Rounds make the improvement loop real.** Changes between study rounds are documented with before/after measures, so the system loops in the README are backed by evidence, not just a diagram.
- **A negative result is still a result.** If PMs don't benefit, that finding, and why, is published too.

## Measures

Three layers, from system to user:

| Layer | What it answers | Example measures |
| --- | --- | --- |
| System quality | Does the machine work? | Citation accuracy, relevant-precedent rate, unsupported-claim rate |
| Product behavior | Does it change how PMs think? | Share of sessions where the PM revises their framing, alternatives considered, risks identified |
| User value | Is it better than what they do today? | Time to a confident framing vs. baseline, perceived usefulness and trust, decision quality vs. baseline (rubric) |

**North star for the study:** the share of sessions that end in an evidence-supported improvement to the PM's initial framing.

## Running the pipeline (phase 6)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python pipeline/fetch.py --dry-run   # preview
python pipeline/fetch.py             # fetch sources to data/raw/ (private)
```
