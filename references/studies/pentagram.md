# Pentagram — connect expressive work to a useful browsing system

Sources: [homepage](https://www.pentagram.com/) and [work index](https://www.pentagram.com/work) · Reviewed: 2026-10-22 (America/Los_Angeles)

## Evidence and scope

**Visual-reviewed.** Inspected desktop screenshots at approximately 1280 × 720 and homepage/work-index text. Selecting slide 2 changed the project to Isomorphic Labs. A cookie overlay was dismissed before the later capture. Filtering, keyboard controls, narrow layouts, loading, and performance were not audited.

## Observed

A compact white header separates site navigation from expansive project artwork. One captured slide is a vivid orange bilingual identity with a lower-left project explanation. A centered control presents design discipline and client sector as a sentence. Another captured slide uses pale green imagery for a different project, while the same browsing concept remains present. Below the carousel, a dark editorial section introduces another body of work.

The work index exposes both sector and discipline categories, short project descriptions, and a route to load more projects. This makes the collection available through more than a sequence of hero images.

## Interpretation

The interface leaves room for each project's own art direction while providing a stable way to browse. Separating what was designed from who it was designed for gives prospective clients two useful entry points. Large imagery creates an invitation; metadata turns that invitation into a searchable body of evidence.

## Transferable recipe

**Original implementation proposal:** build a portfolio for a fictional multidisciplinary studio with six original projects. Keep the header, project caption, and browsing controls consistent while letting each project image vary. Store title, short outcome description, discipline, sector, and URL as structured data. Do not encode these fields into a single promotional image.

Use one featured project initially and a normal grid underneath. Introduce a carousel only if sequencing contributes something useful. Give the discipline and sector selectors visible labels, even if their surrounding copy reads like a sentence. On narrow screens, stack selectors and move captions beneath images so artwork never determines text contrast. Use the same filters on the project index, with a clear reset action and an explicit empty state.

**Exercise:** create projects across three disciplines and sectors, including one belonging to multiple categories. Reach it by either appropriate route. Replace the featured image with light and dark images without changing the controls.

**Acceptance checks:** confirm captions remain readable for both image extremes; preserve selected filters when navigating back; verify every project has a direct link outside the carousel; announce updated result counts without moving focus; check an empty combination offers an obvious recovery action.

## Accessible and lightweight adaptation

Prefer native selects or well-tested disclosure controls over custom pointer-only menus. If slides advance automatically, include pause and disable that movement for reduced-motion preferences. Give slide buttons meaningful names and selected state. Load the first project image promptly, defer later media, and retain descriptive text when imagery fails.

## When to avoid it

Avoid elaborate filtering for a tiny portfolio. A handful of carefully ordered projects and clear descriptions will usually be easier to evaluate than a sparse taxonomy.
