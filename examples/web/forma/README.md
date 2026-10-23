# FORMA — a calm product storefront

An original, fictional ceramics collection implemented with vanilla HTML, CSS, and JavaScript. No third-party code, assets, fonts, packages, network calls, checkout, or payment service. All illustrations are original inline SVG. The prices and product specifications are demonstration content, not real offers.

## Run

Open `index.html` directly, or serve the web examples from the repository root:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web
```

Visit [http://127.0.0.1:8000/forma/](http://127.0.0.1:8000/forma/). The example consists of [HTML](index.html), [CSS](styles.css), and [JavaScript](script.js); there is no build step. The gallery link assumes the rest of this repository is present.

## From reference principle to working code

| Influence | Original interpretation | Where to study it |
| --- | --- | --- |
| [Aesop: calm product shelves](../../../references/studies/aesop.md) | Consistent image area, name, purpose, dimensions, and price across three ceramics | `.product-grid`, `.product-art`, and `.product-title` |
| [teenage engineering: object as poster](../../../references/studies/teenage-engineering.md) | One oversized, complete sculptural vessel leads the page | `.hero-art` and the original `.vessel` SVG |
| [Typography and layout](../../../recipes/web/02-layout-and-typography.md) | System serif expresses the collection; small system sans handles labels and practical information | Type tokens, `h1`, `h2`, and `.eyebrow` |
| [Progressive UI](../../../recipes/web/05-accessible-progressive-ui.md) | All product content in HTML; enhancement controls revealed after initialization | `hidden` attributes and the final lines of `script.js` |

These are transferable relationships, not reproductions of reference pages. The wide hero uses two unequal columns; the narrow layout places the proposition before the artwork. The shelf becomes a full vertical list, with no mandatory sideways scrolling. Decorative transitions run only when reduced motion is not requested.

## Interaction contracts

1. **Finish selection:** native select `#finish` switches Chalk ($48), Umber ($52), or Moss ($52). It changes the SVG's material via `data-finish`, visible finish and price, accessible SVG title, and a polite status. The baseline options carry the price data; the JavaScript does not maintain a second hidden product catalog.
2. **Add to sample bag:** the button copies the currently selected finish into an in-memory list. Existing items retain their own finish and price when the preview changes. Count, grouped rows, subtotal, and status update without moving focus away from the add button.
3. **Remove last item:** removes the last addition, even when repeated finishes are grouped visually. **Clear bag** removes all additions. Empty-state controls disable; if the active control becomes disabled, focus moves to the sample bag heading.
4. **Reload:** clears the sample bag. There is no persistence or transmitted data. Prices are whole-dollar USD demo values; adapt money handling before using a real catalog.
5. **Without JavaScript:** navigation, all three product descriptions, every finish price, SVG artwork, and native detail disclosures remain available. Preview/add controls stay hidden. Nothing pretends to place an order.

## Adaptation exercises

- Replace the vase with your own inline illustration, retaining the accessible title and finish hooks. Keep the complete object within its viewBox at every width.
- Add a fourth finish in HTML and a matching CSS `data-finish` rule. Confirm its name and price propagate without changes to the bag algorithm.
- Replace short product names with 60-character names, inspect the shelf at 320px, and fix the composition without clipping text or hiding overflow.
- Build a real catalog only after defining availability, currency, tax, errors, and the server-side source of truth. This local bag is an interaction lesson.

## Verification

`node --check examples/web/forma/script.js` passed on 2026-10-23. Actual browser results are recorded in [shared verification](../VERIFICATION.md). Do not infer accessibility conformance or performance scores from the implementation.

Repeat these checks before adapting or shipping:

- Inspect 320, 390, 768, and 1440 CSS pixel widths; compare document and viewport widths and inspect the complete page, including expanded product details.
- Use the keyboard to select every finish, add two Chalk and one Moss, confirm 3 items / $148, remove the Moss to get 2 / $96, then clear to 0 / $0. Confirm empty-state focus and visible focus styles.
- Confirm the preview changes without altering existing bag entries. Add and remove after resetting.
- Disable JavaScript and confirm the complete baseline content and navigation. Check console output after interactions.
- Check 200% text zoom, 400% browser zoom, text spacing overrides, reduced motion, forced colors, and a screen reader. These require their own evidence.
