# Reference library

**26 website studies:** the original 14 user-supplied references plus 12 discovered examples. During [bootstrap](../BOOTSTRAP.md), read the full library. When building a project, select one or two complementary influences for specific decisions and translate them into original work.

The original studies were reviewed on **2026-10-21**. The additions were researched on **2026-10-22 (America/Los_Angeles)**; some retain desktop observations from October 21 alongside a fresh content check. Every study separates observations, interpretation, and proposed implementation. **Visual-reviewed means a desktop view was inspected; it does not mean the site passed a responsive, accessibility, motion, or performance audit.** Read the individual evidence scope. No third-party screenshots, source code, or site assets are included.

## New examples

| Study | Design lesson to practice |
| --- | --- |
| [Linear](studies/linear.md) | Use typography, spacing, and a detailed product preview to make a restrained interface specific. |
| [Stripe](studies/stripe.md) | Balance expressive color with a structured business proposition and product routes. |
| [Resend](studies/resend.md) | Combine editorial typography with useful developer examples and clear documentation paths. |
| [Studio Lenzing](studies/studio-lenzing.md) | Use asymmetric alignment, whitespace, and project imagery to establish studio character. |
| [Ordinary Folk](studies/ordinary-folk.md) | Turn conversational type and a reel entry point into a deliberate composition. |
| [Lusion](studies/lusion.md) | Give dimensional art a bounded stage while preserving straightforward navigation. |
| [Active Theory](studies/active-theory.md) | Build atmosphere around one sculptural centerpiece, with a usable fallback. |
| [Instrument](studies/instrument.md) | Contrast oversized identity with a strong media block and compact navigation. |
| [Bruno Simon](studies/bruno-simon.md) | Treat an interactive portfolio as a navigable world with explicit onboarding. |
| [teenage engineering](studies/teenage-engineering.md) | Give a physical product a strong visual presence and distinctive information hierarchy. |
| [Aesop](studies/aesop.md) | Connect editorial storytelling to calm, consistent product presentation. |
| [Pentagram](studies/pentagram.md) | Make varied project work the main attraction while keeping project context readable. |

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

## Choose a useful pairing

| Brief | Complementary influences | Constraint to preserve |
| --- | --- | --- |
| Developer product | Linear's product specificity + Resend's example-led education | Keep the example readable and actionable at narrow widths. |
| Creative studio | Ordinary Folk's typographic composition + Pentagram's project context | Make real work and contact routes easy to find. |
| Physical product | teenage engineering's object scale + Aesop's product information rhythm | Keep product names, details, and actions readable without media. |
| Experimental portfolio | Lusion's bounded visual stage + Bruno Simon's onboarding | Provide direct links and a lightweight alternative to the experience. |
| Technical service | Aethr's editorial composition + Aloud's workflow explanation | Explain the service before introducing decorative complexity. |

These are suggested exercises, not instructions to combine the source sites' branding or assets. Each new study includes its own original exercise and acceptance checks.

## Learn from working code

The [working examples](../examples/web/README.md) turn these principles into original, runnable HTML/CSS/JS: **Signal** (Linear + Resend), **Forma** (Aesop + teenage engineering), **Common Ground** (Ordinary Folk + Pentagram + Instrument), and **Orbit** (Lusion + Bruno Simon). Each source guide identifies the principle, implementation, interaction contract, and adaptation points. The earlier **Fieldwork** example remains available too.

## Use and expand the library

- Use the [catalog](catalog.json) for IDs and metadata. For a partial refresher after initialization: `python tools/build_context.py --track web --reference aesop --out dist/aesop-context.md`.
- Use the [discovery guide](discovery.md) to explore the expanded collection and choose what to investigate next.
- Add a reference using the [workflow](../docs/REFERENCE-WORKFLOW.md), [study template](../templates/site-study.md), and [analysis prompt](../prompts/analyze-reference.md). Update the full file tree too.

Revisit the live source before relying on a time-sensitive detail. Preserve attribution and rights; reuse principles, not another site's branding, copy, imagery, or unverified claims.
