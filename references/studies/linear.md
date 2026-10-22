# Linear — make the product preview carry the detail

- Source: [Linear homepage](https://linear.app/)
- Reviewed: 2026-10-22 (America/Los_Angeles)
- Evidence status: **visual-reviewed**
- Inspected: live desktop opening at approximately 1264 × 712 pixels; homepage text and navigation labels.
- Limits: mobile, navigation disclosures, keyboard operation, motion preferences, and performance were not tested. Product claims were not independently verified.

## Observed

The opening is almost black, with a slim navigation row, a large left-aligned white heading, and a substantial empty interval between navigation and headline. Support copy is smaller and gray. A small announcement link sits toward the opposite edge. A wide, detailed dark product interface enters the bottom of the viewport; its sidebar, issue title, and activity content provide a different density from the spacious introduction.

The homepage text continues through intake, planning, and delivery workflows with concrete interface examples. This is evidence of content organization, not a visual review of every lower section.

## Interpretation

The contrast between a quiet proposition and a dense preview suggests a deliberate product: the introduction establishes priority, while the interface supplies specificity. That is a design judgment, not evidence of better comprehension or conversion. A black palette alone does not reproduce this relationship.

## Transferable recipe

For an original team research tool, write one short proposition and show a plausible research task immediately afterward. Define a shared content container, restrained neutral palette, and two clear type roles before adding decoration. Build the preview from your own sample data: project navigation, one selected finding, supporting notes, and a next action.

Use CSS Grid for the preview's internal columns as a proposed implementation. Choose the collapse point by content fit. At narrow widths, prioritize the selected finding and use a labeled navigation control; avoid shrinking a desktop screenshot into illegibility. Keep an explanatory caption outside the preview.

**Original exercise:** create a landing page for “Fieldnote,” a fictional research organizer. Include one hero, one preview, and three workflow summaries. Acceptance checks:

- At 390 and 1280 CSS pixels, heading, support copy, and main action remain readable without horizontal page scrolling.
- A reviewer can name the preview's task from its caption without reading miniature UI labels.
- Sample navigation either works or is clearly presented as a noninteractive illustration; no decorative buttons masquerade as controls.
- Removing the preview leaves a complete product explanation and usable next step.

## Accessible and lightweight adaptation

Use semantic headings and real links, visible focus, and sufficient contrast for subdued text and boundaries. If using an image preview, provide a concise description and explicit dimensions. Load later previews lazily. Optional animation should stop under reduced motion and never delay essential content. Measure the finished page before asserting speed.

## When to avoid it

Avoid this sparse opening when visitors need urgent information, a dense directory, or a transaction form immediately. A large interface mockup also adds little when the product's value is better demonstrated by a short outcome or physical object.
