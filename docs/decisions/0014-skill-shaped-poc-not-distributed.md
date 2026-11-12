# 0014. Build the POC skill-shaped, but don't distribute it until the study says go

- **Date:** 2026-11-12
- **Status:** Accepted

## Context
Popular agent skills (e.g. Hallmark, Cloudflare's security-audit-skill, ai-job-search) install with one command into tools people already use, ship their knowledge as files, and use patterns such as verbs and independent verification. The question was whether the POC should be a skill now or only after validation.

## Options considered
1. Claude Project prompt for the POC; skill later.
2. Skill-shaped POC (same files, skill structure), run by the researcher; publish and support it only after a "go".
3. Publish the skill immediately and recruit study participants through installs.

## Decision and reasoning
Option 2. The content (rules, verb instructions, decision records) is identical either way, so the skill structure costs nothing and avoids rework. The verifier needs a separate fresh-context agent, which a skill setup supports and a Claude Project doesn't do cleanly. Distribution (one-line install, cross-tool support, docs) answers "how do people get it?", which only matters once the study shows they want it. Running sessions on the researcher's machine also keeps the study fair, testing whether precedent helps rather than whether participants can install a tool.

## Signal to watch
If a participant asks to keep using it after a session, let them install it and record that as a finding: unprompted pull is strong evidence of value.

## Revisit if
The study gives a "go": then publish the install, support other agent tools, and document it.
