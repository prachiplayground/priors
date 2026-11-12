# 0015. Fix the study design: matched scenarios, counterbalancing, blind rating, focused recruiting

- **Date:** 2026-11-12
- **Status:** Accepted
- **Changes:** the study protocol from 0012

## Context
A second outside review (by another AI assistant) rated the plan highly but identified three methodology flaws that would have weakened any result:

1. **Learning effect:** participants framed a decision with their usual tools, then revisited the *same* decision with priors for longer. Any improvement could come from extra thinking time, not priors.
2. **Rater bias:** the researcher, who built priors, judged whether framings improved.
3. **Coverage mismatch:** participants from any domain would face a corpus focused on personalization and experimentation, so a poor result might only reflect missing coverage.

## Options considered
- For (1): add a time-matched control group; or use **two matched scenarios per participant, equal time per condition, with order counterbalanced** across participants.
- For (2): use an LLM judge; or use **two independent human raters, blind to condition**, with an optional LLM judge as a third rater.
- For (3): narrow the corpus to participants' domains; or **recruit mainly within the focus area**, with a few exploratory participants reported separately.

## Decision and reasoning
The bolded options. A within-subject, counterbalanced design is the most informative option for a 6–8 person study: each participant serves as their own comparison, and rotating scenario and condition order cancels out order and scenario effects while making carry-over visible. Blind rating removes the builder from judging their own product. Focused recruiting tests the question the POC can actually answer. Sessions grow from 60 to 75 minutes. Results are reported as directional evidence, with each participant's paired result shown individually.

## Revisit if
Blind raters disagree too often to produce reliable scores (then refine the rubric with examples), or the two scenarios turn out unequal in difficulty (then compare within scenario only).
