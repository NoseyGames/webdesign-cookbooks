# Signal

An original, fictional research product landing page. The page pairs a quiet editorial introduction with a detailed, readable product preview, then explains a method and offers working Python/JavaScript examples. All copy, sample data, layout, CSS artwork, and inline SVG are original. No reference-site assets, source, testimonials, or customer claims are included.

## Run

Open `index.html` directly, or from the repository root run:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web
```

Visit [http://127.0.0.1:8000/signal/](http://127.0.0.1:8000/signal/). Stop with Ctrl+C. No build, dependencies, external assets, accounts, or network requests are needed. Serving the parent directory also enables the footer's gallery link.

## Source-to-code map

| Study or recipe | Applied principle | Where to read |
| --- | --- | --- |
| [Linear](../../../references/studies/linear.md) | A spacious introduction followed by a specific, denser product preview | `index.html`: `.hero`, `.workspace`; `styles.css`: `.workspace-body` |
| [Resend](../../../references/studies/resend.md) | Editorial serif contrast, practical developer examples, a clear language selection path | `.hero-grid`, `.code-section`, and `script.js` |
| [Responsive composition](../../../recipes/web/03-responsive-composition.md) | Recompose content instead of shrinking a desktop screenshot | The three-column workspace becomes a two-column layout, then a single reading column |
| [Progressive UI](../../../recipes/web/05-accessible-progressive-ui.md) | Semantic controls, explicit state, useful HTML when JS fails | Hidden enhancement toolbar, `aria-pressed` language buttons, selectable code, polite feedback |

These are interpretations of the studies, not reproductions of the referenced sites. The system font stack avoids a font download: Georgia has the display role, Arial carries UI and prose, and Consolas/monospace carries code.

## Interaction contract

- Header and hero links navigate to actual page sections. The footer returns to the examples gallery. Navigation remains visible at all sizes; there is no menu to initialize.
- The workspace is a labeled illustration made from HTML. Its navigation-looking labels are plain list items, not fake interactive controls. All research material is explicitly sample content.
- Python and JavaScript buttons are a normal button group, not ARIA tabs. Tab reaches each button; Enter/Space selects. `aria-pressed` and the underline identify the selection. Focus stays on the selected button and a polite region announces the choice.
- Both samples describe the same local transformation: filter three notes down to two open items, then project their ID and title. The page **never runs the displayed snippets**. Copy them into Python 3 or a JavaScript console to execute them. Input is deliberately trusted sample data; the page calls out the validation boundary for real external inputs.
- Copy writes only the selected snippet, and announces success only after the clipboard promise resolves. Missing clipboard access and rejected permission have distinct manual-copy instructions. Controls are temporarily disabled while a copy is pending, preserving the association between selected code and reported result.
- Without JS, both labeled code examples and all content are visible; the nonfunctional enhancement controls stay hidden. Code blocks scroll internally and can be keyboard-focused.
- Motion is limited to optional smooth fragment scrolling and subtle color transitions, enabled only when reduced motion is not requested. There is no autoplay or animation-delayed content.

## What to change

Start with the tokens at the top of `styles.css`, then change the proposition and fictional research question together. Keep the preview caption and sample disclosure truthful. Change both language snippets, their expected result, and the data contract as one unit. If introducing a real service, replace the local example intentionally; do not imply a live backend where none exists.

The preview's compact labels serve its illustrative role. The main explanation, interaction labels, and code remain independent content. If adapting the preview into an actual application, increase its text sizes and design its own complete interaction model.

## Verification

On 2026-10-23, JavaScript syntax passed `node --check script.js`. The two displayed code snippets were extracted from HTML, executed with Python and Node, and their parsed JSON outputs compared with the documented two open notes; both matched.

Actual desktop, narrow-screen, keyboard, and no-script browser results are recorded in [shared verification](../VERIFICATION.md), including the clipboard test's limits. No accessibility conformance or performance score is claimed.

Before shipping a derivative, repeat those checks and add screen-reader review, zoom and text-spacing overrides, forced colors, and actual OS reduced-motion settings. Inspect expanded code, long translated labels, and fallback fonts rather than assuming the default view covers them.
