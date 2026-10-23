# Common Ground — expressive studio portfolio

A complete original vanilla HTML/CSS/JavaScript page for a fictional multidisciplinary design practice. Six invented projects show how strong typography and varied artwork can coexist with useful project browsing. No dependencies, external fonts, images, network calls, or build step are required.

## Run and read

Open [index.html](index.html) directly, or from the repository root run:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web
```

Then visit `http://127.0.0.1:8000/common-ground/`. Read [styles.css](styles.css) for layout and responsive decisions, followed by [script.js](script.js) for the filter enhancement. Use the [example gallery](../index.html) to compare this direction with the other implementations.

## Design direction

The audience is a potential collaborator evaluating a studio's craft. The page's job is to make the practice understandable, let someone find relevant work, and explain what a useful inquiry contains. Oversized staggered type introduces the voice; the work occupies most of the page. A 12-column composition alternates wide and narrow artwork with staggered vertical rhythm. At narrow widths it becomes a clear single list. Coral, yellow, green, and blue belong to the invented projects rather than a system of decorative UI cards.

Primary influences are [Ordinary Folk](../../../references/studies/ordinary-folk.md), for a conversational typographic introduction, and [Pentagram](../../../references/studies/pentagram.md), for giving varied project artwork a consistent browsing structure. [Instrument](../../../references/studies/instrument.md) is a supporting comparison for connecting service categories with project evidence. These are transferable principles; no source markup, artwork, logos, copy, or exact site composition was reused.

## Learn from the implementation

| Principle | Find it in the source | Why it matters |
| --- | --- | --- |
| Expressive type with semantic order | `index.html`: the single `h1`; `styles.css`: `.line-two`, `.line-three`, and the 40rem breakpoint | Visual staggering never changes spoken or keyboard order; mobile offsets relax. |
| Original art independent of real content | `index.html`: six `.project-art` blocks and adjacent headings/descriptions | Inline SVG and CSS illustration are decorative; titles, disciplines, and case notes remain live text. |
| Asymmetry with a consistent caption system | `styles.css`: `.work-list`, `.project-wide`, `.project-narrow`, `.project-heading` | Project artwork can vary while metadata remains predictable. |
| Usable baseline | `index.html`: complete articles, native `details`, initially hidden `#work-filters` | Without JavaScript, every project and case note remains available. |
| Overlapping filters | `index.html`: `data-disciplines`; `script.js`: `Set`, `matches()`, `selectFilter()` | After Hours is reachable through Identity and Digital; Good Loop through Identity and Motion; Small Hours through Digital and Motion. |
| State and feedback | `script.js`: `aria-pressed`, `hidden`, status update; `styles.css`: selected filter | Selected state is explicit, hidden articles leave the focus order, and results are announced without moving focus. |
| Small purposeful motion | `styles.css`: `prefers-reduced-motion: no-preference` | Optional artwork feedback and smooth scrolling disappear for reduced motion; no content depends on animation. |

Each filter has three matches; All has six. Counts are computed from the actual HTML, not maintained separately in JavaScript. Filtering preserves open native disclosures and returns to the full editorial arrangement with All. Only one discipline is selected at a time, so the supplied categories cannot produce an empty combination. If you extend this to multiple criteria, add an explicit zero-results recovery state.

## Adapt it

1. Write your actual practice description and six case summaries before choosing artwork.
2. Replace each project's live title, description, discipline tokens, and case notes. Keep category IDs consistent with the buttons.
3. Change palette and geometry inside the inline SVGs, or use images you have rights to use with reserved dimensions and appropriate alternative text. The current artwork is decorative because nearby text provides each project's meaning.
4. Adjust the type scale and offsets with real copy at 320, 390, and 1440 CSS pixels. Do not hide page overflow to disguise an oversized heading.
5. Replace inquiry guidance with your real contact route when deploying. The current section deliberately explains a useful brief and does not pretend to submit information.

All projects are concepts. Case notes separate a challenge, design decision, and intended concept outcome from unmeasured commercial results. The illustrative Open Index artwork is not an interactive application preview.

## Meaningful verification

See [shared verification results](../VERIFICATION.md) for the checks actually performed. The following are acceptance checks to run after changing this example, not a claim of complete accessibility conformance:

- Test All → Identity → Digital → Motion → All. Expect 6 → 3 → 3 → 3 → 6 articles, one pressed filter, and matching status text. Confirm each overlapping project appears in both of its disciplines.
- Use Tab and Enter/Space to operate filter buttons and each “Read case notes” disclosure. Check focus remains on the filter after a result change, hidden projects cannot receive focus, and open disclosures remain usable on return.
- Disable JavaScript and reload. All six projects, native disclosures, skip link, navigation, and inquiry guidance must remain usable; unavailable filters must stay hidden.
- At 320, 390, and 1440 CSS pixels, inspect the entire page, including expanded notes and filtered arrangements, for overflow, collisions, and readable captions. Recheck browser zoom and text-spacing overrides.
- Enable reduced motion; artwork must remain static and all functionality must remain available. Test forced colors and a screen reader separately.
- Check the browser console and requests. No external resources are expected. A syntax check alone cannot establish visual or interactive correctness.

No field performance, conversion, or assistive-technology claims are made by this example.
