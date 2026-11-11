# 0003. Add a Responsible AI, Ethics & Governance bucket plus cross-cutting ethics fields

- **Date:** 2026-11-11
- **Status:** Accepted

## Options considered
Fold into Trust & Safety; bucket only; bucket plus `ethics_considerations` and `source_perspective` on every record

## Decision and reasoning
Ethics concerns the effects of the company's own systems, a different question from protecting users against bad actors. Assessing every decision makes nulls informative, and `source_perspective` counters the PR bias of self-reported sources.

## Revisit if
The bucket stays thin even with independent sources.
