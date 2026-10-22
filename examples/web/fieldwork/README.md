# Fieldwork

An original editorial studio landing page for **webdesign-cookbooks**. All studio and project names are fictional; the project descriptions are explicitly labelled as concepts. The illustration and project artwork are original inline SVG/CSS. No reference-site assets or source were copied.

## Run

Open `index.html` directly in a current browser, or run from the repository root:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web/fieldwork
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000). Stop the server with Ctrl+C. There is no package install or build step. The only runtime files are `index.html`, `styles.css`, `script.js`, and `project-brief.txt`.

## Design decisions to study

- **One strong opening:** a large proposition shares the page with a single geometric print. Warm paper, oxide red, and ink form a constrained palette.
- **Typography with roles:** system sans carries information; an italic system serif introduces a controlled contrast in display text.
- **Varied rhythm:** paired portfolio pieces lead to a wide third composition, a quieter method section, and a clear closing action.
- **Honest content:** fictional work is identified. No invented client logos, testimonials, or performance claims.
- **A real destination:** the final call to action links to a downloadable project brief. It does not pretend to submit a form or send a message.

## Interaction and implementation

At narrow widths, a native button controls a navigation disclosure. Enter/Space activate it; Escape closes it and returns focus. Activating a nav link moves focus to the destination section. Resizing keeps hidden controls from retaining focus.

Category buttons filter the three projects, update `aria-pressed`, and report the result count in a polite status region. The two categories intentionally overlap for a project that covers both identity and digital. Each project uses native `<details>` for its concept note.

Navigation and all projects are available in baseline HTML. JavaScript reveals only the controls it initializes, then collapses mobile navigation. The project brief and native disclosures work independently of JavaScript.

All decorative motion is inside `prefers-reduced-motion: no-preference`: small hover/focus transforms and smooth fragment scrolling. The default styles remain static and readable. There is no autoplay, scroll hijacking, pointer tracking, or animation-delayed content.

## Verification performed — 2026-10-21

The example was served locally and inspected in the Codex in-app browser. Its exposed browser version was not recorded. These are development checks, not a conformance certificate.

| Check | Result |
| --- | --- |
| JavaScript syntax via `node --check script.js` | Passed |
| Visual screenshots at 320, 390, 768, and 1440px viewport widths | Inspected; no visible text overlap in the reviewed states |
| Full-page desktop screenshot at 1440px | Inspected through the footer |
| Document horizontal overflow at 320, 390, 768, 1440px | None; measured scroll width equalled client width |
| Identity and Digital filters; reset to All | Correct projects and result counts; selected state updated |
| Keyboard Enter on a filter and native project disclosure | Worked |
| Mobile menu Enter open / Escape close | Worked; focus returned to the toggle |
| Mobile section link | Menu closed and destination section received focus |
| Baseline page with its script tag omitted in a temporary test copy | Navigation and all 3 projects available; filters/toggle hidden; native disclosure worked; no 390px overflow |
| Captured browser console errors/warnings during initial interaction review | None |
| Main solid-color text contrast calculations | Ink/paper 13.08:1; muted/paper 5.34:1; muted/studio 4.91:1; oxide/paper 5.86:1 |

The temporary no-script test copy was removed after review. The actual browser setting for JavaScript was not changed. Color calculations cover the listed flat-color pairs, not an exhaustive rendered contrast audit.

**Not verified:** screen-reader output, actual OS reduced-motion switching, forced-colors rendering, 200%/400% zoom and text-spacing overrides, all browser engines, touch hardware, and real-user performance. The download link and its local text file exist; the browser automation's download-completion event timed out, so successful download completion was not confirmed in that environment. A native browser check remains useful before reuse.

## Repeat before shipping a derivative

1. Walk the page with Tab and Shift+Tab, then activate navigation, filters, details, and download using the keyboard.
2. Inspect 320px and a wide desktop, including expanded details and filtered states.
3. Disable JavaScript in browser settings and reload. Confirm the baseline journey.
4. Enable reduced motion and forced colors; inspect focus and selected state.
5. Test text zoom, browser zoom, and text-spacing overrides from [the typography recipe](../../../recipes/web/02-layout-and-typography.md).
6. Check with a screen reader and an automated accessibility tool, then investigate findings manually.
7. Measure representative loading and interaction performance. This example has small local assets, but no Lighthouse score or Core Web Vitals result is claimed.

For changes, start with the tokens at the top of `styles.css`, then adapt copy and artwork to the new brief. Keep semantics and state handling intact while changing the visual language.
