# Instrument — balance identity scale with routes into the work

- Source: [instrument.com](https://www.instrument.com/)
- Reviewed: 2026-10-22 (America/Los_Angeles)
- Evidence status: **visual-reviewed**, with bounded scope.
- Views inspected: the verified desktop opening snapshot from 2026-10-21, approximately 1264 × 712 pixels, plus a fresh homepage text review on 2026-10-22.
- Limits: the opening was not visually rechecked on October 22. Reel playback, category-filter behavior, project pages, mobile layout, keyboard behavior, and performance were not tested.

## Observed

The recorded opening was initially blank, then displayed an enormous heavy uppercase wordmark on white. Compact gray pill navigation sat near an announcement. A large rounded orange media panel contained a black play control; a black cookie overlay partly covered it. Fresh [homepage](https://www.instrument.com/) text includes a skip-navigation link, work/services/contact routes, a recent-work section with brand, marketing, and product labels, and separate service and contact sections. The presence of those labels does not establish how filtering works. No loading duration or exact typography was measured.

## Interpretation

The wordmark and saturated media panel carry the opening's identity; smaller navigation provides a route into the work. Projects and service categories can reinforce each other instead of leaving visitors to infer what an agency offers.

The cookie overlay reminds us to test real interface layers. These interpretations do not establish user behavior or business outcomes.

## Transferable recipe

**Original exercise:** build the homepage for a fictional design cooperative called Field Assembly. Create its own typographic identity, one original film poster, six project summaries, and three clearly defined service categories. Let a visitor move directly from a service description to relevant work.

Proposed implementation: place the wordmark, navigation, and media in independent layout regions with a shared page gutter. Use fluid sizing with a maximum so the identity remains within the viewport. Treat the film poster as an explicit media component with reserved dimensions. Below it, create project links with persistent titles and service labels; optional filter buttons should enhance an already readable list. On narrow screens, put service navigation before decorative media.

Acceptance checks:

- At 360 and 1440 CSS pixels, the name, navigation, and media action do not collide.
- A keyboard user can skip to the main content, reach every project, and operate the optional filters with a visible selected state.
- With JavaScript unavailable, the complete project list and service links remain available.
- If consent UI is needed, inspect its open state at 200% zoom: every consent action is reachable, and it cannot silently trap focus or permanently hide the media control.
- Playing and dismissing the film stops audio and restores focus to the initiating button.

## Accessible and lightweight adaptation

Give the wordmark an appropriate accessible name. Load the film after activation, provide captions, and keep project descriptions outside images. Lazy-load lower project media while reserving its dimensions. Inspect consent and media states alongside the homepage.

## When to avoid it

Avoid giving the brand name most of the opening when visitors primarily need search, support, or transactions. Scale should follow the audience's need for recognition and exploration.
