# pipeline

Stages, run in order and resumable per source via `data/manifest.csv`:

1. **collect**: add candidate URLs from seed lists and RSS feeds to the manifest.
2. **fetch**: save source text to `data/raw/` (private).
3. **classify**: assign primary and secondary category buckets.
4. **extract**: split each source into decision records and fill fields against `schema/decision_record.schema.json`, with an evidence pointer per field.
5. **link**: resolve `builds_on` / `superseded_by`, normalize company and author names.
6. **validate**: hand-review a sample; record field-level accuracy in `evals/`.

Not built yet: the pilot comes first.
