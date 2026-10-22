# From cookbook feedback to a reviewed dataset

This repository does **not** train a model, submit jobs, spend API credits, or supply a production training dataset. It improves task context and makes evaluation repeatable. A dataset and a supported training system are separate work.

## Start with evidence

1. Establish a baseline using `evals/tasks.json` and `evals/rubric.md`. Keep prompts and tools fixed between baseline and candidate trials.
2. Improve the brief, reference selection, recipe, or verification loop. Keep only corrections that help beyond one screenshot or one test case.
3. For recurring failures, collect an input, the defective output, the reviewed corrected output, tests/screenshots, and a short explanation of the correction. Prefer complete, executable examples with verified outcomes.
4. Record provenance and rights for every included artifact. Publicly viewable websites are reference material, not automatically licensed training data. Do not scrape these studies' linked sites into a dataset by default.
5. Review correctness and remove secrets, personal data, fabricated claims, and unverified code. An agent's self-rating is not sufficient approval.
6. Split by project or design family before augmentation. Keep closely related pages and variants together so evaluation is not contaminated by near-duplicates. Maintain a private holdout that is never included in context bundles or training.
7. Compare cookbook-only performance against any proposed trained candidate on that holdout. Log critical failures, reviewer agreement, cost, and latency as well as scores.

## Suggested provider-neutral record

```json
{
  "id": "original-project-001",
  "project_group": "original-project",
  "track": "web",
  "brief": "Exact user task and constraints",
  "input_artifacts": ["relative/path/to/input"],
  "corrected_artifacts": ["relative/path/to/reviewed/output"],
  "correction_summary": "Specific observed defect and validated correction",
  "evidence": ["test output or screenshot reference"],
  "provenance": "Original author and source history",
  "rights": "Documented permission/license covering intended use",
  "review_status": "pending",
  "split": "unassigned"
}
```

This is a collection convention, **not** a provider upload schema. Do not upload pending records. Export only after choosing a supported method and validating its current format. Start with a small reviewed collection; there is no universal example count that guarantees design quality.

## Provider availability

Checked 2026-10-21: OpenAI's [model optimization guide](https://developers.openai.com/api/docs/guides/model-optimization) states that its fine-tuning platform is winding down and is unavailable to new users; existing users have a limited continuation period. Consult the current [deprecations documentation](https://developers.openai.com/api/docs/deprecations) before planning a job. This cookbook deliberately avoids a hard-coded model ID or a training script that implies general availability.

The portable route is useful now: relevant instructions, original examples, human review, and repeatable evaluation. A provider-supported training route can be added later when access, rights, quality, costs, and actual evaluation gains justify it.
