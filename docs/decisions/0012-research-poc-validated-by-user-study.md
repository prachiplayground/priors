# 0012. Position priors as a research proof of concept validated by a user study

- **Date:** 2026-11-11
- **Status:** Accepted
- **Supersedes the sequencing (not the vision) of:** 0001, 0002

## Context
An outside review of the repository (by another AI assistant) scored the product thinking highly but flagged that the plan proved the *system* would work before proving anyone *needed* it: discovery came late, the 13-bucket schema would be built before knowing which fields PMs use, and the metrics measured system quality rather than user value.

## Options considered
1. Keep the build-first plan (gold set → extraction → scale → app), with interviews alongside.
2. Pause building and do discovery interviews only.
3. Reframe as a research proof of concept: build the smallest queryable system on a hand-structured slice of the corpus, test it in a recorded, round-based user study against a baseline, and scale only if the study shows value.

## Decision and reasoning
Option 3. It keeps the momentum of building (a working prototype in week 1) while making the user problem the center of the project. It's also the honest origin story: the corpus came first, and the open question was whether it helps PMs at the moment of decision.

- The first focus area is personalization and experimentation, where the corpus is densest. The 13 buckets remain the long-term design.
- 10–15 hand-structured decision records serve as both the prototype's knowledge base and the future gold set.
- The study runs in two rounds with documented changes between them, so the improvement loops are backed by before/after evidence.
- Metrics span three layers: system quality, product behavior and user value. The north star is the share of sessions that end in an evidence-supported improvement to the PM's initial framing.

## Revisit if
Round 1 shows PMs don't change their framing or don't trust the precedents. Then pivot the format (e.g. curated briefs instead of a co-thinker) or stop scaling, and publish the finding.
