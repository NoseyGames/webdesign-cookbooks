# 03 · Recompose for the available space

**Use when:** a desktop design must become a usable narrow-screen experience.

**Inputs:** content priorities and a working source order. **Output:** layouts that adapt without hiding essential content.

## Method

1. Start with a meaningful HTML reading order. Do not use CSS reordering to make keyboard focus jump around the visual page.
2. Add `width=device-width, initial-scale=1` to the viewport meta tag. Do not disable user zoom.
3. Let text and media determine height. Prefer `minmax(0, 1fr)` grid tracks, wrapping flex rows, and bounded fluid sizes over fixed pixel widths.
4. Resize slowly. Add a breakpoint where the actual composition fails: a nav begins to collide, a project caption becomes too narrow, or a paired layout loses balance. Device names are not evidence for a breakpoint.
5. Recompose deliberately. A two-column hero can become copy followed by a smaller illustration. Preserve the proposition and action; decorative artwork can shrink or simplify.
6. Check long words, translated labels, longer names, and empty results. Apply `overflow-wrap: anywhere` selectively to user-provided long strings, not indiscriminately to display text.
7. For images, reserve dimensions or aspect ratio. Use `srcset`/`sizes` when different source sizes exist, and use `<picture>` when the composition itself must change.

```css
.hero { display: grid; grid-template-columns: 1.15fr 1fr; gap: 3rem; }
.hero > * { min-width: 0; }
.art { width: 100%; aspect-ratio: 1; }
.filters { display: flex; flex-wrap: wrap; gap: .5rem; }
@media (max-width: 52rem) {
  .hero { grid-template-columns: 1fr; }
  .art { max-width: 34rem; justify-self: center; }
}
```

See [MDN responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) and [MDN responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images).

## Acceptance matrix

| Condition | Inspect |
| --- | --- |
| 320 CSS px | No page-level horizontal scrolling; actions and text remain usable |
| 390 and 768 CSS px | Nav wrapping, artwork scale, card captions |
| 1440 CSS px | Line length, whitespace balance, maximum width |
| 200% text zoom | No clipped labels or overlapping content |
| 400% browser zoom at a 1280px viewport | Reflow equivalent to a 320 CSS px viewport |
| Touch and keyboard | Hover is never the only way to reveal essential information |

The widths are this cookbook's test samples. WCAG 2.2 reflow has specific 320 CSS px / 256 CSS px criteria and exceptions for content requiring two-dimensional layout; read the [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) rather than equating any one screenshot with conformance.

**Common repair:** remove fixed widths and intrinsic-size constraints before applying `overflow-x: hidden`. Hiding overflow can conceal the defect and clip focus rings.
