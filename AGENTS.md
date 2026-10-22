# Webdesign Cookbooks

This repository is a practical reference library for distinctive, usable websites and reliable Python. It guides work when loaded into context; it does not change a model's weights.

## Load only what the task needs

- Start with `docs/START-HERE.md` and the user's actual brief.
- Web work: read `recipes/web/README.md`, then the relevant recipes and at most two complementary studies from `references/catalog.json`.
- Python work: read `examples/python/README.md` and the relevant files under `recipes/python/`.
- Review: use `evals/rubric.md`. When adding a reference, follow `docs/REFERENCE-WORKFLOW.md` and `templates/site-study.md`.
- In another project, use `prompts/kickoff.md` or generate a portable context bundle with `python tools/build_context.py --track web --out dist/web-context.md`. Do not replace that project's instructions blindly.

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
python tools/build_context.py --track web --out dist/web-context.md
python tools/build_context.py --track python --out dist/python-context.md
```

The tests check tools and examples, not whether a model has become a senior designer. Human visual judgment and task-specific evaluation are still required.
