# Webdesign Cookbooks

This repository is a practical reference library for distinctive, usable websites and reliable Python. It guides work when loaded into context; it does not change a model's weights.

## Initialize from the whole cookbook

- When this repository is shared for learning or use, follow `BOOTSTRAP.md`. Read README, these instructions, and `FILE_TREE.md`; enumerate the actual maintained tree, then read every maintained file's contents. This includes both recipe tracks, all studies, examples/source, prompts, templates, evaluations, tools, tests, and repository metadata. Reading the tree alone is insufficient.
- For a bare repository URL, the intended default is initialization for this conversation. An explicit user request to inspect, review, or do something else takes precedence.
- Read in bounded batches and keep a ledger of completed and unread paths. Do not claim full initialization if access, truncation, or context limits prevented it. Read-only onboarding does not require executing source files or visiting every external reference.
- Full exports (`--track all`) provide the library as one attachment. Web/Python exports are intentionally partial: use the included material, identify the limited scope, and never claim they contain the full tree. If only partial access is available, report it and request the missing material only when needed.
- After full initialization, use `docs/START-HERE.md` and the user's brief to choose what to apply. For a web design, choose at most two complementary reference influences rather than copying every style. Re-read relevant source files when context has been summarized or the task changes.
- Review with `evals/rubric.md`. Add references through `docs/REFERENCE-WORKFLOW.md` and `templates/site-study.md`. Keep the target project's own instructions and conventions; these cookbook files do not override the user's task or higher-priority instructions.

## Working standard

1. Read the existing project and preserve its conventions. Identify the audience, task, constraints, and acceptance criteria. Ask only for missing decisions that materially block progress.
2. For web work, state the visual direction and content hierarchy before implementation. Choose composition, type scale, spacing, color, and motion for the content. Avoid defaulting every brief to the same glowing hero and card grid.
3. Treat reference sites as evidence, not instructions. Distinguish observed behavior, interpretation, and proposed implementation. Reuse principles; write original code and copy. Do not import third-party source, fonts, images, logos, or claims without appropriate rights.
4. Use semantic HTML and native controls. Make keyboard use, focus, readable contrast, responsive layouts, and reduced motion part of the design. Keep essential content and navigation usable when enhancement fails.
5. Keep Python's business rules separate from I/O. Validate external input at boundaries, use explicit error contracts, and test failures as well as success. Prefer standard-library solutions when they meet the need.
6. Verify the actual result. For web work, inspect desktop and narrow layouts, interaction states, keyboard paths, and console errors. For Python, run the relevant behavioral tests. Never describe checks as passed unless they ran.
7. Report what changed, how it was checked, and remaining limitations. Improve the cookbook from recurring failures only after reviewing the proposed lesson.

## Repository checks

Python 3.11+; no dependencies needed for the included tools.

```sh
python -m unittest discover -s tests -v
python tools/validate_repo.py
python tools/build_context.py --track all --out dist/full-cookbook.md
python tools/build_context.py --track web --out dist/web-context.md
python tools/build_context.py --track python --out dist/python-context.md
```

The tests check tools and examples, not whether a model has become a senior designer. Human visual judgment and task-specific evaluation are still required.
