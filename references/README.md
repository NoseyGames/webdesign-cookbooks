# Reference library

Choose a reference for a particular design decision, then translate that decision into original work. Start with one or two studies; importing every visual effect produces a weaker direction.

These 14 user-supplied sites were inspected on **2026-10-21 (America/Los_Angeles)**. Every study distinguishes what was observed, interpretation, and a proposed implementation. **Visual-reviewed means a desktop view was inspected, not that the site passed a complete responsive, accessibility, motion, or performance audit.** Each study states its narrower scope. No source code or site assets are included.

## Explain a product or workflow

| Study | Useful question |
| --- | --- |
| [Raycast](studies/raycast.md) | How can a broad product connect visual identity to concrete use cases? |
| [Ardor](studies/ardor.md) | How can a product-shaped demonstration explain an unfamiliar interaction? |
| [Aloud](studies/aloud.md) | How can a short promise lead into a clear, sequential workflow? |

## Build a distinct brand or personal portfolio

| Study | Useful question |
| --- | --- |
| [Drool](studies/drool.md) | How can expressive type and illustration form one coherent visual language? |
| [Studio Nelka](studies/studio-nelka.md) | How can one strong visual idea express the page's message? |
| [Nikola Radeski](studies/nikola-radeski.md) | How can a portrait, identity, and section navigation organize a personal portfolio? |
| [Odoo Web Design](studies/odoo-design.md) | How can repeated accent treatments connect a hero to a project gallery? |

## Present products and support buying decisions

| Study | Useful question |
| --- | --- |
| [Square](studies/square.md) | How can audience and capability routes organize a broad product range? |
| [Heist](studies/heist.md) | How can sensory product presentation coexist with a clear shopping action? |

## Give technical ideas a concrete form

| Study | Useful question |
| --- | --- |
| [Aethr](studies/aethr.md) | How can an editorial composition reinforce a network metaphor? |
| [Colmez](studies/colmez.md) | How can industry-specific language and imagery distinguish business software? |
| [Atalanta](studies/atalanta.md) | How can alignment, rules, and a restrained palette support a technical narrative? |
| [Biotic](studies/biotic.md) | How can an organic metaphor introduce a scientific mission? |

## Introduce a mission and invite participation

| Study | Useful question |
| --- | --- |
| [OnEarth](studies/onearth.md) | How can landscape imagery lead into projects and participation? |

OnEarth is a website template. Its example impact totals, donations, dates, and people are not verified organizational results. Across all studies, displayed testimonials and business claims remain claims of their source sites.

## Use and expand the library

- For a software landing page, pair **Aethr's composition** with **Aloud's workflow explanation**; make your own visual identity and content.
- For a creative service, pair **Drool's coherent illustration language** with **Odoo's transition into project evidence**.
- Use the [catalog](catalog.json) for IDs and metadata, or include a chosen study with `python tools/build_context.py --track web --reference aloud --out dist/aloud-context.md` from the repository root.
- Explore [additional discovery candidates](discovery.md). Their evidence labels matter; a discovery link is not automatically an inspected case study.
- Add a reference using the [workflow](../docs/REFERENCE-WORKFLOW.md), [study template](../templates/site-study.md), and [analysis prompt](../prompts/analyze-reference.md).

Revisit the live source before relying on a time-sensitive detail. Preserve attribution and rights; reuse principles, not another site's branding, copy, imagery, or unverified claims.
