# 06 · Ship a measured, reviewable result

**Use when:** a page looks complete and needs an honest quality decision.

**Inputs:** a working page, target audience/devices, and agreed constraints. **Output:** a short evidence report and prioritized fixes.

## Method

1. Establish a representative environment: viewport, browser, device/CPU assumptions, and network conditions. Record those details with results.
2. Inspect the initial request path. Avoid shipping a framework or animation library for work a few semantic elements and CSS rules can do. Added dependencies must have a clear benefit.
3. Size and compress media. Reserve layout space, lazy-load appropriate below-the-fold images, and keep the likely LCP image available early. Do not apply lazy loading indiscriminately to the hero.
4. Test the entire page, not just the first viewport. Inspect footer, expanded disclosures, filter results, and the narrow layout.
5. Run functional checks separately from visual review. Confirm real navigation destinations, form behavior, error recovery, and absence of console errors.
6. Compare the result against the brief and direction sheet. Find the three highest-impact changes, implement them, and repeat the affected checks.
7. Document what remains untested. A localhost screenshot does not establish real-user loading performance, conversion improvement, or accessibility conformance.

## Performance targets

[Google's Core Web Vitals guidance](https://web.dev/articles/vitals) defines “good” thresholds as LCP ≤2.5 seconds, INP ≤200 milliseconds, and CLS ≤0.1, evaluated at the 75th percentile of visits, with mobile and desktop considered separately. These are field experience thresholds, not a guarantee from one Lighthouse run. A lab run helps diagnose causes; it cannot supply a representative production INP percentile.

For a small static page, **illustrative project budgets** might be: no required third-party scripts, ≤50 KiB compressed application JavaScript, and ≤500 KiB initial transferred assets. Choose budgets based on actual audience needs and document exceptions. These values are not web standards and do not guarantee good Core Web Vitals.

## Review report template

```text
Brief and primary journey:
Build/revision:
Browser, viewport, device and network conditions:
Functional checks performed and results:
Desktop and narrow visual review:
Keyboard, reduced motion, no-JS checks:
Automated findings and manual follow-up:
Measured performance (lab or field, sample/method):
Three fixes, ordered by user impact:
Known limitations and untested conditions:
```

## Acceptance checks

- No unexplained failed requests or uncaught JavaScript errors.
- Main content is available without waiting for decorative animation.
- Static asset dimensions prevent unexpected content movement.
- Links and buttons perform their stated actions.
- Claims in the handoff distinguish measured results, visual judgments, and assumptions.

**Common repair:** remove an expensive decorative dependency before obsessing over tiny source-code savings. A high automated score is useful evidence, not a complete design review.
