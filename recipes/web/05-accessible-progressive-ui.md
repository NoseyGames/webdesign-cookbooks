# 05 · Keep the interface usable through every state

**Use when:** adding navigation, filters, disclosures, or forms to a visual page.

**Inputs:** semantic HTML and a state inventory. **Output:** keyboard-usable enhancements with useful failure behavior.

## Method

1. Build the baseline with `<header>`, `<nav>`, `<main>`, headings, links, buttons, `<label>`, and `<details>` where they fit. Navigation links navigate; buttons change state. Do not simulate a button with a clickable `<div>`.
2. Add a skip link and visible focus styling. Keep outlines clear of clipping and sticky overlays.
3. Make mobile navigation a disclosure: a real button, accurate `aria-expanded`, and `aria-controls` pointing at the controlled navigation. Normal site links do not need the application-style ARIA `menu` role. [W3C disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/).
4. Hide the menu toggle until its handlers are installed. Leave navigation available when JavaScript fails. Only collapse the navigation after successful initialization.
5. Treat project filters as toggle buttons with `aria-pressed`. Keep focus on the activated filter and announce a concise result count through a polite status region. Do not announce every card's content.
6. For forms, show labels, instructions, field-level errors, and recovery actions. Do not rely on placeholder text or color alone. Preserve user input after failures.
7. Test contrast for the actual text/background pairs. WCAG AA generally requires 4.5:1 for normal text and 3:1 for large text; applicable UI boundaries and state indicators have separate 3:1 requirements. Exceptions and definitions matter. [W3C contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Required states to review

| Component | States / behavior |
| --- | --- |
| Navigation | Expanded, collapsed, Escape closes, resized to desktop, JavaScript disabled |
| Filter | All, one category, no matching items, visible selected state, spoken result count |
| Form | Empty, invalid, submitting, success, server/network error, retry |
| Disclosure | Closed, open, keyboard activation, understandable summary label |

Use a comfortable 44×44 CSS px target where practical as a project preference. WCAG 2.2 AA target size (minimum) is 24×24 CSS px with specified exceptions and spacing alternatives; 44×44 is the enhanced AAA criterion. [W3C target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## Acceptance checks

- Complete the main journey using Tab, Shift+Tab, Enter, Space, and Escape where applicable.
- Confirm no keyboard trap and no hidden element in the tab order.
- Check names, roles, states, and heading order with a screen reader; automated checks are insufficient.
- Test text spacing, zoom, reduced motion, and forced colors.
- Record the tool/browser and what was tested. Do not claim WCAG conformance from a short checklist or an automated score.

**Common repair:** choose a native control before adding more ARIA. ARIA cannot supply missing keyboard behavior.
