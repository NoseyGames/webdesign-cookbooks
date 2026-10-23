# Working web examples

**Five complete pages, five distinct directions.** Every example uses plain HTML, CSS, and JavaScript. All brands, projects, product data, and artwork are original or explicitly fictional. No external libraries, fonts, images, analytics, backend, package installation, or build step are required.

## Run the gallery

From the repository root:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000), then choose a page. Stop the server with Ctrl+C. You can also open [index.html](index.html) directly. Clipboard permissions vary by browser and origin; Signal reports a manual-copy fallback when copying is unavailable.

## Choose an example

| Example | Style and reference principles | Working behavior | Source files |
| --- | --- | --- | --- |
| [Signal](signal/README.md) | Dark developer product; [Linear](../../references/studies/linear.md) and [Resend](../../references/studies/resend.md) | Language selection, copy success/failure feedback, readable product preview | [HTML](signal/index.html) · [CSS](signal/styles.css) · [JS](signal/script.js) |
| [Forma](forma/README.md) | Warm editorial commerce; [Aesop](../../references/studies/aesop.md) and [teenage engineering](../../references/studies/teenage-engineering.md) | Finish selection, local sample bag, quantity/subtotal and removal | [HTML](forma/index.html) · [CSS](forma/styles.css) · [JS](forma/script.js) |
| [Common Ground](common-ground/README.md) | Expressive studio portfolio; [Ordinary Folk](../../references/studies/ordinary-folk.md), [Pentagram](../../references/studies/pentagram.md), and [Instrument](../../references/studies/instrument.md) | Discipline filters, result announcements, native project disclosures | [HTML](common-ground/index.html) · [CSS](common-ground/styles.css) · [JS](common-ground/script.js) |
| [Orbit](orbit/README.md) | Atmospheric installation; [Lusion](../../references/studies/lusion.md) and [Bruno Simon](../../references/studies/bruno-simon.md) | Room selection, explicit motion controls, offscreen pause, direct reading path | [HTML](orbit/index.html) · [CSS](orbit/styles.css) · [JS](orbit/script.js) |
| [Fieldwork](fieldwork/README.md) | Original editorial studio study; warm paper, oxide accents, geometric artwork | Mobile navigation disclosure, project filters, native details, project-brief download | [HTML](fieldwork/index.html) · [CSS](fieldwork/styles.css) · [JS](fieldwork/script.js) |

These implement transferable relationships from the reference studies. They do not reproduce the sites or claim to use their implementation techniques. The gallery's small illustrations are original previews, not source-site screenshots.

## Read the implementation, not just its screenshot

During [bootstrap](../../BOOTSTRAP.md), read **every file in this directory tree**, including all five examples and their READMEs. For each page:

1. **HTML:** trace landmarks, heading order, content, destinations, native controls, and the useful baseline when scripts are absent.
2. **CSS:** identify tokens, alignment, typography roles, the main composition, and the narrow-screen reflow. Explain why a rule exists before copying it.
3. **JavaScript:** name each state and transition. Trace which DOM text, attributes, and controls change together; check failure paths and focus behavior.
4. **README:** connect the reference principle to its actual code. Read the [verification record](VERIFICATION.md) and distinguish tested behavior from intended behavior.
5. **Apply:** borrow a small pattern that fits the current brief, then change the content, visual identity, and composition. Do not turn every new project into the same example.

Full-library exports include these source files automatically:

```sh
python tools/build_context.py --track all --out dist/cookbook-with-working-code.md
```

Use a fresh output filename. The intentionally partial `--track web` bundle contains recipes and selected studies; it does not include these working pages. Use the full export or read their source files directly when implementation examples are needed.

## Patterns worth comparing

- **State without a framework:** Signal changes a language, Forma changes a product choice, Common Ground changes a filter, and Orbit changes a scene. Each keeps the visible result and accessible state in sync.
- **Enhancement without a dependency:** baseline content and real destinations live in HTML. JavaScript makes a page more convenient; it does not create the only route to essential information.
- **Different responsive solutions:** a product preview simplifies, a shelf stacks, an editorial grid becomes linear, and a decorative scene yields space to copy. A breakpoint is a content decision.
- **Different visual systems:** serif contrast, strict sans-serif scale, object framing, and atmospheric SVG are demonstrated separately. Their differences matter as much as shared coding conventions.

## Practice with a changed brief

Replace Signal's examples with another pair of equivalent local transformations. Give Forma a fourth finish and verify its label, price, and bag line stay consistent. Give Common Ground a new discipline and check both the all-results view and an empty result. Add an Orbit room while preserving its ordinary HTML destination and reduced-motion behavior.

Before shipping a derivative, repeat keyboard, narrow-layout, script-failure, reduced-motion, zoom, screen-reader, and performance checks. This is teaching code with bounded verification, not a production commerce service or a conformance certificate.
