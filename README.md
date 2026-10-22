# Webdesign Cookbooks

**A practical cookbook for helping coding agents build distinctive websites and dependable Python.**

## AI agents: start here when this URL is shared

**This repository is intended to be loaded and applied, not just summarized.** When the user shares this repository URL to learn or use the cookbook, follow the instructions below. For a bare URL with no other request, the intended default is to load the cookbook for the current conversation. If the user asks for a different action, follow that request.

1. Open [BOOTSTRAP.md](BOOTSTRAP.md) and [AGENTS.md](AGENTS.md).
2. Inspect the **entire repository file tree**, using [FILE_TREE.md](FILE_TREE.md) as the linked reading checklist. Check the live tree too so newly added files are included.
3. **Read the contents of every maintained file**, in the order defined in BOOTSTRAP.md: all web and Python recipes, every site study, examples and source code, prompts, templates, evaluation material, tools, and tests. A filename listing or README summary does not count as reading the cookbook.
4. Read in batches if needed, keeping a path-by-path reading ledger. Report inaccessible or truncated files honestly; do not claim full initialization while files remain unread.
5. Give a brief loading receipt, then apply the cookbook to the user's existing task. If the URL was the entire message, say the cookbook is loaded and ask what they want to build. Do not invent a project.

**Next file: [BOOTSTRAP.md →](BOOTSTRAP.md)** · **Complete linked tree: [FILE_TREE.md →](FILE_TREE.md)**

These instructions guide an agent that can open and follow the repository. They cannot force every AI app to browse links, grant access to this private repo, or permanently train a model. No files need to be executed just to read the cookbook.

The goal is to understand the brief, learn from the library, build original work, inspect the result, and improve from feedback. This is a working reference library, not a trained model or a guarantee of senior-level output.

## Plug it into your workflow

1. Paste `https://github.com/NoseyGames/webdesign-cookbooks` into an agent with access to this private repository. The README above is the entry point.
2. The agent follows [BOOTSTRAP.md](BOOTSTRAP.md), inventories the full tree, and reads the complete maintained library.
3. Give it a brief, or let it continue the task already in progress. After initialization, it selects the recipes and reference influences to apply.
4. Build, inspect, and revise. Save useful corrections as small recipes or reviewed examples when requested.

Copy this prompt into an agent that can read the repository:

> Load https://github.com/NoseyGames/webdesign-cookbooks using its README and BOOTSTRAP.md. Inspect the full file tree and read every maintained file. Report any unread files, then apply what you learned to my project. My brief: [audience, purpose, content, constraints, stack, deadline].

If an agent cannot browse the private repository, clone it through an authorized account and generate a **full-library attachment**:

```sh
git clone https://github.com/NoseyGames/webdesign-cookbooks.git
cd webdesign-cookbooks
python tools/build_context.py --track all --out dist/full-cookbook.md
```

Attach `dist/full-cookbook.md` and ask the agent to read it completely, following its bootstrap instructions. The export contains the maintained text/source files and a path inventory, not generated output, dependency folders, credentials, or external websites. The agent still needs access to your actual project files.

For an intentionally smaller refresher after initialization, use `--track web` or `--track python`; add `--reference raycast` to include a study. Those are **partial bundles**, not full onboarding. The builder refuses to overwrite an existing file; use a fresh `--out` filename when regenerating.

## What's inside

| Area | Start here | Purpose |
| --- | --- | --- |
| Agent initialization | [Bootstrap](BOOTSTRAP.md), [full file tree](FILE_TREE.md) | Read the complete library from one shared URL |
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
