# 04 · Make motion earn its place

**Use when:** a reference has dramatic movement or a page feels unresponsive to interaction.

**Inputs:** an interaction purpose and a static layout that already works. **Output:** small, explicit state transitions with a reduced-motion alternative.

## Method

1. Name the job: confirm a button interaction, connect a disclosure to its content, or direct attention to a changed result. Decoration can be valid, but cannot obstruct reading or navigation.
2. Define states before animation: closed/open, selected/unselected, idle/loading/success/error. Make the interface understandable with all transition durations set to zero.
3. Prefer short transitions on a few elements. For this example, 160–240ms is a design starting point, not a standard or a universal optimum.
4. Prefer `transform` and `opacity` where appropriate. Avoid repeatedly changing layout properties. Measure actual rendering costs; a composited animation can still be expensive. [web.dev animation guide](https://web.dev/articles/animations-guide).
5. Make motion opt-in through `prefers-reduced-motion: no-preference`. Keep content visible in base styles. Never make a failed animation or observer leave an entire page transparent.
6. Do not replace native scrolling, trap the pointer, or require hover. Use native buttons, anchors, and disclosures.
7. If movement runs automatically for more than five seconds alongside other content, review the applicable pause/stop/hide requirement. Reduced-motion support alone is not that control. [W3C pause, stop, hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html).

```css
.project-art { transform: none; }
@media (prefers-reduced-motion: no-preference) {
  .project-art { transition: transform 200ms ease; }
  .project:hover .project-art { transform: scale(1.025); }
  .project:focus-within .project-art { transform: scale(1.025); }
  html { scroll-behavior: smooth; }
}
```

Use [MDN reduced-motion guidance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) when implementing preference-aware CSS or JavaScript. JavaScript animation systems must also react if the preference changes during the session.

## Acceptance checks

- Enable reduced motion before loading and while the page is open. Essential content and controls remain identical in meaning.
- Navigate without a mouse. Focus is visible; revealing content does not unexpectedly move focus.
- Interrupt transitions repeatedly. The final state stays correct.
- Disable JavaScript. The reading experience and native links remain useful.
- Record a performance trace before adding permanent `will-change` declarations or complex scroll effects.

**Common repair:** if motion is the only interesting part of the page, fix the typography, content, or art direction first. If a button animates but does nothing, implement the action before polishing the animation.
