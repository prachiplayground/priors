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

- **H1 (quality):** Framings produced with priors are rated higher, by blind raters, than framings produced with the participant's usual approach.
- **H2 (breadth):** With priors, PMs identify more alternatives and risks.
- **H3 (time):** within the same 20 minutes, PMs reach a framing they're more confident in with priors than with their usual approach.
- **H4 (trust):** PMs trust cited precedent more than uncited AI answers, and say so unprompted.
- **H5 (mode):** PMs reach for priors mostly while thinking (looking things up and sparring), not only when writing documents. This tests [decision 0013](../decisions/0013-sparring-partner-not-prd-collaborator.md).

Any of these can fail. Failed hypotheses are reported as findings.

## Participants

- **Core participants (at least 6 of 8):** PMs who work in or near the POC's focus area: personalization, recommendations, search, growth/engagement or experimentation, and who have written or reviewed a PRD in the last 6 months. The POC's corpus covers this area, so testing elsewhere would mostly measure missing coverage (a false negative), not whether precedent helps.
- **Exploratory participants (1–2):** PMs from other areas, to see how priors behaves at the edge of its coverage. Their results are reported separately and never pooled with the core results.
- **How many:** 3–4 per round, 2 rounds, 6–8 total. Different people each round.
- **Mix:** at least one PM from a large company and one from a smaller one.

## Tasks: two matched scenarios

Each participant works on **two comparable scenarios**, one with their usual tools and one with priors. Both are in the focus area and designed to be similar in difficulty:

- **Scenario 1:** *"You're a PM at a mid-size online marketplace. Leadership wants a personalized homepage to increase repeat purchases. You have a quarter. Frame the decision and the first version."*
- **Scenario 2:** *"You're a PM at a subscription content app. Leadership wants personalized recommendations on the home screen to improve 30-day retention. You have a quarter. Frame the decision and the first version."*

Using prepared scenarios also means no one has to discuss confidential work on a recording.

**Optional, if time allows (qualitative only, never scored):** a participant can bring their own decision, or run `priors audit` on an old or sanitized PRD. These show how priors handles real material but aren't part of the comparison.

## Session design (75 minutes)

1. **Warm-up (10 min):** how they last researched a hard decision: where they looked, how long it took, what they wish they'd known.
2. **Task 1 (20 min):** one scenario, with one condition (usual tools *or* priors), thinking aloud. Ends with the framing template.
3. **Task 2 (20 min):** the other scenario, with the other condition. Ends with the framing template.
4. **Debrief (15 min):** comparing the two experiences, what was useful, what they distrusted, what was missing, when they'd reach for priors.
5. **Buffer (10 min):** setup, consent check, optional extras.

**Counterbalancing.** Equal time per condition removes the "more time to think" advantage, and a fresh scenario per condition removes the learning effect of revisiting the same problem. Which scenario and which condition come first rotate across participants:

| Participant | Task 1 | Task 2 |
| --- | --- | --- |
| P1, P5 | Scenario 1, usual tools | Scenario 2, priors |
| P2, P6 | Scenario 2, usual tools | Scenario 1, priors |
| P3, P7 | Scenario 1, priors | Scenario 2, usual tools |
| P4, P8 | Scenario 2, priors | Scenario 1, usual tools |

One known limitation: when priors comes first, ideas from it can carry over into the usual-tools task. Rotating the order makes that visible in the data (compare the priors-first and priors-second groups) rather than hiding it.

## Measures

| Measure | How it's captured |
| --- | --- |
| Framing quality | **Blind rating** (see below) of both framings per participant |
| Alternatives and risks | Counted from each written framing, by the blind raters |
| Time to confident framing | Timestamps from the recording, plus self-reported confidence (1–5) at the end of each task |
| Usefulness and trust | 1–5 ratings in the debrief, plus open comments |
| Research cost today | Self-reported hours spent on precedent research for their last PRD |
| Mode of use | Which modes the PM uses unprompted (look up, spar, persuade, check), coded from the recording, plus their answer to "when would you reach for this?" |
| Verifier | Confirmed / needs check / rejected counts per session; time and cost per session |
| System quality | Every citation in the session checked: was it accurate, and was it relevant? |

### Blind rating of framings

The researcher built priors, so the researcher doesn't score the framings.

1. **Same format:** every framing is written in the same template, in the participant's own words.
2. **Anonymize and strip:** a helper (not the researcher) removes participant details and any visible traces of the condition: citations, record IDs and phrases like "priors showed".
3. **Shuffle:** framings from both conditions are mixed into one set, labeled only with a random code.
4. **Two independent raters:** two PMs uninvolved in the project score each framing 1–5 on five dimensions: problem clarity, alternatives considered, risks identified, success and guardrail metrics, and how well-supported the reasoning is. They don't know which condition produced which framing.
5. **Agreement:** report how closely the two raters agree. Where they differ by 2 or more points, they discuss and re-score, and the disagreement is reported.
6. **Optional third rater:** an LLM judge using the same rubric, reported alongside the humans and only trusted if it agrees with them.

### What the sample can and can't show

With 6–8 participants, results are **directional evidence, not statistical proof**. Each participant's paired result is reported individually (did their priors framing score higher than their usual-tools framing?), alongside averages, so readers can judge the pattern for themselves.

## Rounds and the improvement loop

After round 1, the top findings are turned into specific changes (prompt, retrieval, which fields are shown, interface), each logged with its reason. Round 2 measures whether the changes helped. The round-to-round comparison is the evidence for the improvement loops described in the main README.

## Data handling and ethics

- **Consent first:** written consent before any recording, with separate opt-ins for publishing (see [consent-form.md](consent-form.md)).
- **Anonymous by default:** participants are referred to as P1, P2, and so on. Company names are removed unless the participant opts in.
- **Recordings stay private:** stored outside this repository, never committed, deleted 12 months after the study ends unless the participant agreed to publication.
- **Review before publishing:** any clip or quote is shown to the participant before it's published, and they can withdraw it.
- **Withdrawal:** participants can withdraw at any time, and their data is deleted.
