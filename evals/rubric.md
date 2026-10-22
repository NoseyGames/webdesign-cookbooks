# Evaluate the output, not the confidence of the answer

Use this rubric to compare **baseline** (same task without cookbook context) with **candidate** (same task plus selected cookbook context). Keep model/version, tools, brief, assets, time budget, and test environment constant. Run several trials, shuffle labels for reviewers, and retain failures. These are proposed project criteria, not evidence that the cookbook already improves model performance.

## Web scorecard: 0–4 per dimension

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Task clarity | Purpose/action unclear | Main action understandable | Content sequence and actions fit the audience with little friction |
| Composition and hierarchy | Competing focal points, arbitrary layout | Coherent but generic structure | Deliberate hierarchy and rhythm that fit this brief |
| Type and detail | Unreadable or inconsistent | Readable with some inconsistencies | Consistent roles, spacing, line lengths, and refined alignment |
| Responsive behavior | Broken or missing narrow layout | Main content fits, some awkwardness | Intentional reflow, usable navigation, robust long content |
| Accessibility and interaction | Core task unusable | Main flow works, gaps remain | Keyboard/focus/state checks pass; semantics, contrast, motion considered |
| Engineering and performance | Broken, unstable, or wasteful | Works with avoidable complexity | Clear code, real states, appropriate asset strategy, measured checks |

Scores 1 and 3 represent intermediate outcomes. Attach evidence to every score. A visual screenshot cannot prove semantic or keyboard behavior. Judge distinctiveness in context: novelty is not a requirement for a dense business interface.

## Python scorecard: 0–4 per dimension

Correctness; explicit contracts and input validation; error handling; maintainability; test quality; proportionate resource/security controls. A 0 means absent/broken, 2 means common cases work with meaningful gaps, and 4 means requirements and important edge cases are verified with clear evidence.

## Release gates

Do not average away a broken primary action, inaccessible core keyboard path, data loss, credential leak, or a failed required test. Record such failures as a blocked gate. Suggested internal target: no blocked gates, no dimension below 2, and at least 18/24. Calibrate with actual reviewers; the threshold is a convention, not a scientific metric.

For web checks, include narrow and wide screenshots, 200% zoom/reflow, keyboard-only primary flow, focus visibility, reduced-motion behavior, console errors, and content stress cases. Measure contrast and performance rather than guessing. Log browser/device/network and whether tests were manual or automated. A clean console is not proof of accessibility.

## Improvement log

Use `templates/evaluation-record.md`. Record baseline/candidate scores, defects, fixes, and unchanged variables. A candidate is an improvement only if it passes critical gates and the evidence supports better outcomes. Include regressions, review disagreements, time/cost, and uncertainty. Do not label a model “senior” from a single attractive screenshot.
