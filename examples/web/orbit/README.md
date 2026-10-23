# Orbit — atmosphere without an entry barrier

A fictional exhibition implemented in original HTML, CSS, JavaScript, and inline SVG. Run by opening `index.html`, or serve the repository's examples directory:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/web
```

Visit `http://127.0.0.1:8000/orbit/`. No package installation, framework, fonts, imagery, audio, renderer, or backend is fetched.

## Learn from the implementation

| Reference principle | Working implementation |
| --- | --- |
| [Lusion](../../../references/studies/lusion.md): bound the visual centerpiece | `.scene` reserves a stage for an original SVG sculpture; navigation and captions remain normal HTML. |
| [Bruno Simon](../../../references/studies/bruno-simon.md): orient visitors to unfamiliar interaction | Three named buttons select rooms, with explicit state and concise announcements. All destinations also have direct links and field notes. |
| Atmosphere through hierarchy | A constrained green/ivory palette, oversized type, overlapping decorative orb, small annotations, then quieter editorial notes. |
| Progressive enhancement | `index.html` contains all three notes and native disclosures. JavaScript reveals controls only after handlers exist. |
| User-controlled motion | `updateMotion()` combines an explicit choice, media preference, page visibility, and scene visibility. CSS independently disallows animation under reduced motion. |

These are original interpretations of the studies, not reproductions of source sites. There is no simulated 3D engine: the legible SVG and CSS demonstrate the composition at a much smaller implementation cost.

## State contract

- A room selection updates the sculpture, caption, destination link, and exactly one pressed button. Focus remains on the trigger.
- Motion starts off. Users can turn it on and off; the OS reduced-motion preference disables it. A preference change resets the choice so movement does not silently resume later.
- Decorative movement pauses when the page or stage is hidden. No timer advances a visitor to another room.
- With JavaScript unavailable, the introductory scene, all field notes, navigation, and native disclosures remain usable. There are no invisible content gates.

## Read, then change

Read HTML landmarks and source order first, then the numbered CSS sections, then `selectRoom()` and `updateMotion()`. Change palette and typography tokens, replace the fictional content, and alter the original SVG geometry to fit a new brief. Adding a room requires both a readable article and an explicit entry in `rooms`; keep those two representations consistent.

Try replacing the artwork with an image that fails to load: the explanation and direct destinations must still make sense. Do not turn this into mandatory game navigation for a booking flow or information service.

## Verification

See the shared [verification record](../VERIFICATION.md) for checks actually performed and remaining limits. Before shipping a derivative, test 320px and desktop, keyboard room selection and disclosures, reduced-motion changes, JavaScript failure, zoom, screen-reader output, and target-device performance.
