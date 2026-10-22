# Webdesign Cookbooks

**A practical cookbook for helping coding agents build distinctive websites and dependable Python.**

The goal is better decisions, not a bigger prompt: understand the brief, study useful references, build original work, inspect the result, and learn from failures. This is an initial working library, not a trained model or a guarantee of senior-level output.

## Plug it into your workflow

1. Clone this repository and open it in your coding agent. Codex can load the root [AGENTS.md](AGENTS.md); other tools need their supported instruction mechanism or an explicit prompt.
2. Give the agent a real brief and ask it to read [START-HERE](docs/START-HERE.md).
3. Select the web or Python track, one or two relevant reference studies, and the acceptance checks.
4. Build, inspect, and revise. Save the useful correction as a small recipe or reviewed example.

Copy this prompt into an agent that can read the repository:

> Read AGENTS.md and docs/START-HERE.md in webdesign-cookbooks. Apply the relevant recipes to my project. For web work, choose two complementary reference studies, propose a specific visual direction, and implement an original design. Verify the responsive layouts and interactions. For Python, define the input/error contract and run behavioral tests. My brief: [audience, purpose, content, constraints, stack, deadline].

**A URL by itself is not an installation.** A private repository must be accessible to the agent. If your tool cannot read a repo, generate a self-contained Markdown bundle and attach it:

```sh
git clone https://github.com/NoseyGames/webdesign-cookbooks.git
cd webdesign-cookbooks
python tools/build_context.py --track web --out dist/web-context.md
python tools/build_context.py --track python --out dist/python-context.md
```

Use `--reference raycast` (or another catalog ID) to include a study. Bundles contain guidance and selected studies; the agent still needs access to your actual project files. The builder refuses to overwrite an existing file; use a fresh `--out` filename when regenerating.

## What's inside

| Area | Start here | Purpose |
| --- | --- | --- |
| Web design | [Web recipes](recipes/web/README.md) | Art direction, composition, typography, responsive behavior, motion, accessibility, performance |
| Visual references | [Reference library](references/README.md) | Original, evidence-labeled studies of the 14 supplied sites |
| More inspiration | [Discovery list](references/discovery.md) | Additional websites to explore, with review status |
| Working web example | [Example](examples/web/README.md) | Original HTML, CSS, and JavaScript with no build step |
| Python | [Example and recipes](examples/python/README.md) | Typed boundaries, predictable errors, safe I/O, meaningful tests |
| Agent prompts | [Kickoff](prompts/kickoff.md), [critique](prompts/critique.md), [new reference](prompts/analyze-reference.md) | Repeatable task workflows |
| Evaluation | [Rubric](evals/rubric.md), [task set](evals/tasks.json) | Compare output quality before and after cookbook changes |
| Future training | [Improvement workflow](training/README.md) | Build a reviewed, rights-aware dataset if a suitable training route is available |

## Try the examples and checks

Requires Python 3.11+. No API keys, model training, or package installation are needed.

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web/fieldwork
```

Open `http://127.0.0.1:8000` in your browser. Stop the server with Ctrl+C. The [Python example README](examples/python/README.md) lists its CLI commands.

```sh
python -m unittest discover -s tests -v
python tools/validate_repo.py
```

## Add more sites

Provide a URL and what you like about it. Use the [analysis prompt](prompts/analyze-reference.md), create a [study](templates/site-study.md), and add the catalog entry. A screenshot alone is not evidence of responsiveness, accessibility, conversion performance, or implementation technology. Keep those claims separate.

## Guidance versus fine-tuning

This repo supplies task context, recipes, examples, and evaluation criteria. It does not permanently improve ChatGPT or automatically train any model. Actual fine-tuning changes model parameters through a separate provider-supported process. Start with measurable improvements from the cookbook before investing in training. See [training/README.md](training/README.md) for scope and current provider caveats.

## Reuse

Original repository code and writing are under the [MIT license](LICENSE). Linked websites, brands, screenshots, fonts, and other third-party materials remain subject to their owners' terms. The repository includes original analysis rather than copies of those websites.
