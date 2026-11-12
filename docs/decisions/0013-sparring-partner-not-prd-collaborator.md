# 0013. Make priors a sparring partner for decisions, with the PRD as one destination

- **Date:** 2026-11-12
- **Status:** Accepted
- **Refines:** 0008, 0011

## Context
The product had been framed as a PRD co-writer (0008), then as "co-think and co-write" (0011). The question was whether the corpus is most valuable for writing a document, or as something PMs consult throughout their work.

## Evidence
- **Mobbin**, the largest design reference library, analyzed 317,427 queries to its AI integration: none of the top 50 asked it to generate anything. People looked things up mid-work, grounded design conversations in evidence, and studied how other teams solved the same problem before committing.
- **Architecture precedent research**: studies of the design process find precedent is consulted in almost every phase, not for a single deliverable, and that it lends authority to a proposal. The field's known failure modes, romanticizing past decisions and neglecting context, map directly to priors' verifier checks.

## Options considered
1. PRD co-writer: the corpus serves one document at one moment.
2. Sparring partner: the corpus serves four modes (look up, spar, persuade, check) across the decision process; the PRD is one destination.

## Decision and reasoning
Option 2. It matches how comparable reference libraries are actually used, fits the "evidence, not decisions" principle, and covers the PRD moment anyway through the `audit` verb. The core experience becomes a conversation (`priors think`); `audit` remains a focused entry point because it's the easiest value to demonstrate.

The research question changes accordingly: *"Does sparring with real product precedent help PMs think through decisions, or is it just interesting reading?"*

## Revisit if
The study shows PMs reach for priors mainly when writing documents, not during thinking. Then the PRD-centered framing was right after all.
