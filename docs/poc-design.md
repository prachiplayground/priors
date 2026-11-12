# Proof-of-concept design

The POC is the smallest working version of priors that can answer the research question in the [study](study/). It's built **skill-shaped** (as instruction files and records that a coding agent such as Claude Code loads) but is **not distributed** until the study supports a "go" decision ([decision 0014](decisions/0014-skill-shaped-poc-not-distributed.md)). During the study, the researcher runs it and shares the screen.

## Structure

```
skills/priors/
  SKILL.md                # rules: modes, "evidence, not decisions", output format
  references/
    think.md              # the sparring conversation: look up, spar, persuade
    audit.md              # the PRD check
    verifier.md           # how every claim is verified before it's shown
  corpus/
    index.md              # one line per decision: company, problem shape, tags
    decisions/*.yaml      # 10–15 hand-structured decision records
```

At this scale there's no database or vector search. The agent reads `index.md`, picks the relevant records by problem shape and opens them. Retrieval is revisited only if the corpus grows.

## `priors think`: the sparring partner

Covers three of the four modes in one conversation:

- **Look up:** answers direct questions ("How did Airbnb handle cold start?") with the relevant decision records, cited.
- **Spar:** given the PM's plan, surfaces 3–5 comparable decisions (framing, alternatives, tradeoffs, what failed) and pushes back with questions, never answers. Example: *"Two of these teams needed a supply-side guardrail metric. What's yours?"*
- **Persuade:** on request, assembles the precedent behind a position the PM has chosen, including counter-examples, for a review or stakeholder conversation.

It ends, on request, with a short cited **brief** of what the PM concluded and why. The PM writes the conclusions; priors supplies the evidence.

## `priors audit prd.md`: the check

Reads an existing PRD and returns findings, each with the gap, why it matters, the precedent behind it, and a verification status. It never rewrites the PRD.

## The verifier

Every precedent claim is checked before it's shown, by a separate agent with fresh context that sees only the claim and the record:

1. **Supported:** does the source actually say this?
2. **Comparable:** is the situation genuinely similar (scale, business model, sidedness, constraints)? This guards against the classic precedent-study errors: romanticizing past decisions and ignoring context.
3. **Contested:** is there counter-evidence in the corpus?

Verdicts: **confirmed** (shown), **needs check** (shown, flagged) or **rejected** (never shown). Verification roughly doubles the model calls per claim; cost and latency are measured in the study.

## Session log

Each session writes a local log: the precedents shown, the verifier's verdicts, and (for audits) which findings the PM accepted or rejected. These logs supply the system-quality measures in the study. They stay on the researcher's machine and are anonymized before any analysis is published.

## Rules in SKILL.md

- Never say "you should." Present what comparable teams did, what they optimized for, what they gave up, and where evidence is thin.
- Surface at least one counter-example or limitation whenever precedent points one way.
- Say so when no comparable precedent exists, rather than stretching a weak match.
- Distinguish what a source reports from what it implies.
- Cite every claim with its decision record and source.
