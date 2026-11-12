# User study protocol

**Research question:** Does sparring with real product precedent help PMs think through decisions, or is it just interesting reading?

| File | What it covers |
| --- | --- |
| This page | Hypotheses, participants, tasks, measures, rounds, data handling |
| [interview-guide.md](interview-guide.md) | The session script, minute by minute |
| [consent-form.md](consent-form.md) | What participants agree to, including recording and publishing |
| [outreach.md](outreach.md) | The message used to recruit participants |
| `rounds/` | Findings per round (added as rounds complete) |

## Hypotheses

- **H1 (behavior):** With priors, PMs revise or sharpen their initial framing more often than with their usual research approach.
- **H2 (breadth):** With priors, PMs identify more alternatives and risks.
- **H3 (time):** priors gets PMs to a framing they're confident in faster than their usual approach.
- **H4 (trust):** PMs trust cited precedent more than uncited AI answers, and say so unprompted.
- **H5 (mode):** PMs reach for priors mostly while thinking (looking things up and sparring), not only when writing documents. This tests [decision 0013](../decisions/0013-sparring-partner-not-prd-collaborator.md).

Any of these can fail. Failed hypotheses are reported as findings.

## Participants

- **Who:** product managers (any level) who have written or reviewed a PRD in the last 6 months.
- **How many:** 3–4 per round, 2 rounds, 6–8 total. Different people each round.
- **Mix:** at least one PM each from a large company and a smaller one; at least one who works on personalization, search or experimentation (the focus area) and one who doesn't.

## Tasks

Each participant chooses one:

- **A. Bring your own decision:** a real decision you made or are making, described at whatever level of detail you're comfortable sharing.
- **B. Use a prepared scenario:** *"You're a PM at a mid-size online marketplace. Leadership wants a personalized homepage. You have a quarter. Frame the decision and the first version."*

- **C. Check a PRD:** bring an old or sanitized PRD (or use a provided sample) and run `priors audit` on it.

Tasks B and C exist so no one has to discuss confidential work on a recording.

## Session design (60 minutes)

1. **Warm-up (10 min):** how they last researched a hard decision: where they looked, how long it took, what they wish they'd known.
2. **Baseline (15 min):** they frame the decision using their usual tools (search, AI assistant, notes), thinking aloud.
3. **With priors (20 min):** they revisit the same decision with the priors prototype, thinking aloud, using it however they like: asking questions, sparring, or auditing (task C).
4. **Debrief (15 min):** what changed in their framing, what was useful, what they distrusted, what was missing.

Baseline always comes first, so priors can only add to an initial framing rather than shape it from the start.

## Measures

| Measure | How it's captured |
| --- | --- |
| Framing change | Researcher compares the framing written after the baseline with the one after priors, using a simple rubric (no change / reworded / meaningfully improved) |
| Alternatives and risks | Counted from each written framing |
| Time to confident framing | Timestamps from the recording, plus self-report |
| Usefulness and trust | 1–5 ratings in the debrief, plus open comments |
| Research cost today | Self-reported hours spent on precedent research for their last PRD |
| Mode of use | Which modes the PM uses unprompted (look up, spar, persuade, check), coded from the recording, plus their answer to "when would you reach for this?" |
| Audit findings (task C) | Share of findings the PM accepts, rejects or wants to check |
| Verifier | Confirmed / needs check / rejected counts per session; time and cost per session |
| System quality | Every citation in the session checked: was it accurate, and was it relevant? |

## Rounds and the improvement loop

After round 1, the top findings are turned into specific changes (prompt, retrieval, which fields are shown, interface), each logged with its reason. Round 2 measures whether the changes helped. The round-to-round comparison is the evidence for the improvement loops described in the main README.

## Data handling and ethics

- **Consent first:** written consent before any recording, with separate opt-ins for publishing (see [consent-form.md](consent-form.md)).
- **Anonymous by default:** participants are referred to as P1, P2, and so on. Company names are removed unless the participant opts in.
- **Recordings stay private:** stored outside this repository, never committed, deleted 12 months after the study ends unless the participant agreed to publication.
- **Review before publishing:** any clip or quote is shown to the participant before it's published, and they can withdraw it.
- **Withdrawal:** participants can withdraw at any time, and their data is deleted.
