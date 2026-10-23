# Working example verification

Checked on **2026-10-23**, served locally with Python's HTTP server and exercised in the Chromium-based in-app browser on Windows. This records observed results, not a claim of accessibility conformance, production readiness, or improved model weights.

## Scope and results

| Example | Exercised behavior | Result |
| --- | --- | --- |
| [Signal](signal/) | Keyboard language selection; visible sample, pressed state, focus, copy feedback | JavaScript selection exposed only its sample and retained button focus. Copy reported success after its promise resolved. Independent clipboard readback through the browser tool returned empty, so the clipboard payload was not independently verified. |
| [Forma](forma/) | All three finishes; repeated additions; removal; clearing; empty state focus | Two Chalk plus one Moss produced 3 items / $148; removing the last item produced 2 / $96; clearing produced 0 / $0 and moved focus to the bag heading. Umber displayed $52 and updated the illustration title. |
| [Common Ground](common-ground/) | Keyboard filters; selected state; result counts; native case disclosures | Identity, Digital, and Motion each exposed the correct three projects; All restored six. Exactly one filter stayed pressed, focus remained on the chosen button, and an open case note survived filtering. |
| [Orbit](orbit/) | Keyboard room selection; caption, link, pressed state; motion toggle; native field notes | Archive and Garden selected the corresponding scene, text, and real section link. Motion toggled on and off; field-note disclosures worked with Enter. |

Full desktop and 390px-page screenshots were inspected for all four new examples. Document width checks at 320px and 390px found no horizontal page overflow, including the tested interaction states. Long Signal code remained inside its own scrollable code block. The gallery was visually inspected at desktop and 390px and checked for overflow at 320px, 390px, and 768px. CSS pixel widths can exclude the browser scrollbar.

No-script baselines were checked using temporary copies with the script tag removed, leaving the original markup and stylesheet intact. Signal retained both code samples; Forma retained all products, prices, and native disclosures; Common Ground retained six projects and native disclosures; Orbit retained all room notes and native disclosures. Enhancement controls stayed hidden. The temporary copies are not part of the repository.

Captured browser warning/error logs were empty after the tested interactions. This is not a complete network audit; the local server logged a harmless missing favicon request.

## Source and repository checks

- All four new JavaScript files passed `node --check`.
- Both Signal snippets were extracted from HTML, executed with Python and Node, and compared with the documented two-record JSON result; both matched.
- A source audit of the gallery and four new HTML pages found no duplicate IDs; all 54 local `href`/`src` references and fragments resolved.
- Repository validation checks reference metadata, evaluation task metadata, and local Markdown file targets. The complete context export includes the new source files; the intentionally partial web export does not.
- Repository validation passed. The existing Python suite ran 51 tests: 49 passed and two Windows symlink tests skipped. The first attempt hit sandbox temporary-directory permissions; rerunning with a writable workspace temporary directory passed.

The existing [Fieldwork](fieldwork/) example was preserved. Its earlier verification belongs to that example's README; it was not subjected to a new full interaction pass in this addition.

## Remaining checks before shipping a derivative

Actual screen-reader output, OS reduced-motion changes, forced colors, zoom/text-spacing overrides, touch devices, other browser engines, performance measurements, clipboard-denial behavior, and Orbit's offscreen/tab-visibility motion pausing were not exhaustively exercised. Reduced-motion and pause paths were inspected in source. Clipboard fallback messages exist but their browser failure paths still need a separate test.

These examples have fictional content and local interaction state. Forma does not submit an order, Common Ground does not send an inquiry, Signal does not run code in the page, and Orbit does not depend on a 3D runtime. Adapt the behavior deliberately before connecting a real service.
