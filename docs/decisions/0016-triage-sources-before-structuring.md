# 0016. Triage every source before structuring it; only decision sources become precedent

- **Date:** 2026-11-12
- **Status:** Accepted

## Context
The corpus mixes very different kinds of sources. Some describe a product decision with its reasoning and outcome. Others are mostly engineering ("how we built it"), teach a method, or offer frameworks and opinion. Structuring all of them as decision records would present engineering write-ups as product choices, and weaken the premise that priors shows how teams *decided*.

At the same time, engineering under constraints is often a real decision that PMs need to understand (e.g. trading feature freshness for serving cost). Excluding all engineering content would throw away some of the most useful precedent.

## Options considered
1. Structure every source as decision records.
2. Keep only product-strategy sources; drop engineering content.
3. Triage each source with a short rubric (choice, context, outcome, PM relevance, candor) and assign a role: decision, technique, background or excluded.

## Decision and reasoning
Option 3. The test is whether a source contains *a real choice with a reason and a consequence*, not whether it's product or engineering. Decision sources become decision records and can be cited as precedent. Technique sources become supporting context the tool can explain but never cite as precedent. Background frames the conversation. Decision records gain a `decision_type` field (product, technical with product impact, process) so PMs can see what kind of choice a precedent was.

A first-pass guess at roles (`role_guess` in the manifest) puts about half the pilot corpus in the decision role. It's confirmed or corrected by reading each source.

## Revisit if
In the study, precedents from higher-scoring sources aren't rated more useful than those from lower-scoring ones. Then the rubric measures the wrong things and needs revising.
