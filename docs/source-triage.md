# Source triage

Not every case study is about a decision. Some are mostly engineering ("how we built it"), some teach a method, and some are opinion or frameworks. Turning all of them into decision records would present engineering write-ups as product choices and weaken the whole premise. So every source is triaged **before** it's structured.

The test isn't "product or engineering?" Engineering under constraints is often a real decision, and a valuable one for PMs: trading feature freshness for serving cost, or latency for quality. The test is:

> **Is there a real choice here, with a reason and a consequence?**

## The rubric

Score each source 0–2 on five questions. It takes 10–15 minutes per source.

| # | Question | 0 | 1 | 2 |
| --- | --- | --- | --- | --- |
| 1 | **Choice:** is there an explicit decision among alternatives, with the reasoning? | No decision; describes a system | A decision is implied, reasoning thin | Alternatives named and the choice explained |
| 2 | **Context:** are the problem, constraints (team, budget, latency, scale, timeline) and goal stated? | Missing | Partly | Problem, constraints and goal all clear |
| 3 | **Outcome:** is a result reported? | None | Qualitative ("it worked well") | Measured result, or a clear account of what failed |
| 4 | **PM relevance:** would a PM learn something they could apply? | Implementation detail only | Some transferable lesson | Clear, transferable product lesson |
| 5 | **Candor:** does it admit tradeoffs, costs or failures? | Pure success story | Mentions a tradeoff in passing | Discusses costs, failures or what they'd do differently |

## Roles

| Role | Rule | How it's used |
| --- | --- | --- |
| **Decision source** | Total ≥ 6 **and** Choice = 2 | Structured into one or more decision records. Cited as precedent. |
| **Technique source** | Choice ≤ 1, PM relevance ≥ 1 | Not a decision record. Kept as supporting context the tool can explain when a decision mentions it (e.g. what "interleaving" or "contextual bandits" means). Never cited as precedent. |
| **Background** | Frameworks, opinion, overviews, books | Frames the conversation (e.g. aggregation theory, experimentation principles). Never cited as precedent. |
| **Excluded** | Total ≤ 3 and no technique value | Left in the manifest with its score, not used. |

Borderline cases (total of 5, or Choice = 1 with a strong outcome) are decided by hand and noted in the manifest.

## Decision types

Every decision record also records what kind of decision it was (`decision_type`):

- **`product`**: what to build or optimize for (e.g. shifting a feed from engagement to retention).
- **`technical_with_product_impact`**: an engineering choice made under constraints that changed what users get (e.g. accepting higher serving cost for real-time personalization).
- **`process`**: how the team decides or works (e.g. experiment guardrails, interleaving to speed up testing).

## Where it's recorded

In `data/manifest.csv`:

- `triage_score`: total 0–10, plus the five sub-scores as `choice/context/outcome/relevance/candor`, e.g. `8 (2/2/2/1/1)`
- `role`: `decision`, `technique`, `background` or `excluded`
- `constraints_note`: the key constraints in a few words (e.g. "batch features lagged 24h; serving cost")

`role_guess` holds an unconfirmed first-pass guess made before reading. It is replaced by `role` once the source is triaged.

## Validating the rubric

The study checks whether the rubric works: do precedents from higher-scoring sources get rated more useful by PMs in sessions? If not, the rubric is measuring the wrong things and gets revised.
