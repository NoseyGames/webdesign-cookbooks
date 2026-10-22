# Start with the job, then choose the recipe

First initialize with [BOOTSTRAP.md](../BOOTSTRAP.md): inspect the full tree and read all maintained files using [FILE_TREE.md](../FILE_TREE.md). The task selection below happens **after** that complete first pass. If only a partial bundle was supplied, identify that limitation rather than claiming full initialization.

## For a new web project

Write a six-line brief: audience; primary task; real content; brand character; technical constraints; completion checks. If the brief is incomplete, make reversible assumptions and state them. Do not invent customer counts, testimonials, certifications, or conversion claims.

Select a visual direction using `templates/design-brief.md`. Choose one reference for composition and another for a different concern, such as product explanation or typography. Read their studies rather than mixing every site's visual effects. Translate each influence into a decision: “use an oversized editorial headline with a narrow supporting column” is actionable; “make it premium” is not.

After the initial full read, revisit `recipes/web/README.md` and the recipes relevant to this task. Sketch the page's sequence in words, then implement the most important viewport and content hierarchy. Adapt narrow layouts intentionally; preserve the order that lets the user understand and act. Add interactions after the static page works.

Inspect the result at desktop and narrow widths. Test the actual primary action, navigation, focus, keyboard, overflow, long content, empty/error states, and reduced motion. Compare against `evals/rubric.md`; fix the highest-impact defect before adding decoration.

## For Python work

State the function or CLI contract: inputs, outputs, error behavior, side effects, dependencies, and scale. Revisit the applicable recipes under `recipes/python/` and the runnable example's README. Keep parsing and external I/O at the boundary; test the pure rules using concrete cases. Add concurrency, frameworks, or abstraction only when the requirement calls for them.

## Using this repo inside another project

Keep that project's existing instructions. Share this repository URL, place a checkout in an accessible reference directory, or attach a full export. Follow the README entry point and BOOTSTRAP.md; a nested clone does not guarantee automatic instruction loading in every agent. Give an honest loading receipt and summarize the relevant working rules before implementation so missed context is visible.

The official [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) describes Codex instruction discovery and limits. Other agents have different loaders. Do not assume a filename is universally recognized.

## The smallest useful loop

Brief → relevant context → original implementation → inspection/tests → specific correction → reviewed lesson. Record the model/version, cookbook commit, task, screenshots or test output, and outcome when comparing iterations. Never change the benchmark prompt while attributing gains only to the cookbook.
