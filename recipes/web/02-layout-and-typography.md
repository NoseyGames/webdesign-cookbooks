# 02 · Build hierarchy with type and space

**Use when:** everything looks like a card, text competes with itself, or desktop screenshots look attractive but the page is hard to read.

**Inputs:** approved copy, content hierarchy, direction sheet. **Output:** a small token system and a repeatable layout grammar.

## Method

1. Rank content before styling: page proposition, section titles, body copy, captions, metadata. Use heading levels for document structure, not visual size.
2. Choose one body face and optionally one expressive face. Start with system fonts; add a licensed web font only when it materially changes the direction. Font choice affects wrapping, so inspect the fallback too.
3. Give display text a bounded fluid scale and body copy a comfortable measure. A 55–70 character reading measure is a starting preference, not a WCAG requirement. Never force heading line breaks without checking narrow screens and zoom.
4. Establish a shared page gutter and maximum width. Use a grid to align sections; break the grid deliberately for artwork, not accidentally for text.
5. Use spacing to group related elements. A caption should be visibly closer to its project than to the next project. Increase separation between sections before adding dividers or boxes.
6. Remove redundant visual emphasis. If size and position already communicate importance, bold, color, a pill, and a shadow probably are not all necessary.

```css
:root {
  --paper: #f5f1e8;
  --ink: #262923;
  --accent: #a73523;
  --gutter: clamp(1.25rem, 5vw, 5rem);
  --section-gap: clamp(4rem, 8vw, 8rem);
}
.shell { width: min(100% - 2 * var(--gutter), 90rem); margin-inline: auto; }
.display { font-size: clamp(3rem, 1.4rem + 6vw, 8.25rem); line-height: .98; }
.prose { max-width: 62ch; line-height: 1.65; }
.pair { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem; }
@media (max-width: 45rem) { .pair { grid-template-columns: 1fr; } }
```

`clamp()` bounds a preferred value; combining relative font units with viewport units is useful, but does **not** automatically guarantee accessible zoom behavior. Test it. [MDN clamp reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp).

## Acceptance checks

- Read the page at 100% and 200% zoom; headings do not overlap or lose text.
- Test the WCAG text-spacing overrides: 1.5× line height, 2× paragraph spacing, .12em letter spacing, .16em word spacing. No content or function is lost. These are override test conditions, not mandatory default styling. [W3C text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).
- Long project names and real paragraphs fit. Do not validate with only short placeholder copy.
- No text block depends on a fixed height to fit.
- Disabling custom fonts preserves useful hierarchy.

**Common repair:** if a layout feels cramped, inspect line length and grouping before shrinking all text. If it feels empty, add useful content or improve composition rather than filling space with ornamental boxes.
