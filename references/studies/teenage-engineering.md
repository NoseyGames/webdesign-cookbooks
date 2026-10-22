# teenage engineering — give an object the scale of a poster

Sources: [homepage](https://teenage.engineering/) and [store](https://teenage.engineering/store) · Reviewed: 2026-10-22 (America/Los_Angeles)

## Evidence and scope

**Visual-reviewed.** Inspected the desktop homepage at approximately 1280 × 720 and read homepage/store text. The browser showed a product campaign; text extraction showed a store-opening announcement. Visual observations therefore use the screenshot; catalog organization uses store text. Mobile, menus, product selection, checkout, animation, and performance were not tested.

## Observed

The captured homepage uses a black field and a very large gray device with small orange details. Its scale pushes part of the object below the viewport. Across the top, thin outlined illustrations accompany groups for products, store, updates, and finding information. The typography is compact relative to the product, and the visible chrome takes the character of an equipment diagram. A horizontal scrollbar is present in this captured viewport; this is a limitation to avoid inheriting, not a recommended effect.

The store text organizes a substantial inventory into product families and accessories, with repeated product links and purchase actions.

## Interpretation

The object itself carries the visual identity. Restrained surrounding color gives physical materials and controls room to communicate. Grouped utility navigation suggests an ecosystem around the product, including finding help after purchase. The dramatic crop creates curiosity, but it can delay explanation for unfamiliar visitors.

## Transferable recipe

**Original implementation proposal:** design a page for a fictional field recorder using an original photograph or illustration. Give the first section one large product image, a short product name, a plain-language purpose, and one primary action. Use a limited neutral palette with one accent drawn from the original object. Make utility groups visually related without turning every link into a card.

Keep essential copy outside the image. Use a constrained content wrapper and an image container with an intentional aspect ratio; do not use a fixed desktop width that creates horizontal scrolling. On narrow screens, move the product explanation above the image and turn the utility groups into a compact navigation disclosure. A complete object view should appear before technical details.

**Exercise:** prepare two versions of the hero, one with a full object and one with an expressive crop. Ask a reviewer to identify the product's purpose, the next action, and the route to support without scrolling.

**Acceptance checks:** verify there is no horizontal overflow at 360, 768, and 1280 CSS pixels; verify all utility routes remain available by keyboard; check that long translated labels do not collide with illustrations; confirm the purpose remains understandable with images disabled.

## Accessible and lightweight adaptation

Use real links and disclosure buttons, adequate target sizes, visible focus, and readable labels alongside icons. Supply responsive image sizes and dimensions; keep the important image eager and defer lower catalog media. Avoid decorative animation competing with product inspection.

## When to avoid it

Avoid a giant object-led opening when a service needs explanation or when customers primarily compare many specifications. In those cases, place the comparison or task closer to the top.
