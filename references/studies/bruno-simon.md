# Bruno Simon — make the portfolio demonstrate the skill

Source: [bruno-simon.com](https://bruno-simon.com/) · Reviewed: 2026-10-22 (America/Los_Angeles)

## Evidence and scope

**Visual-reviewed.** Inspected desktop screenshots at 1280 × 720 before and after activating the entry scene, plus homepage text and documented controls. The start interaction was verified; driving, map navigation, keyboard operation, narrow layouts, frame rate, and loading performance were not tested. The screenshots belong to this review session, not a reusable asset collection.

## Observed

The entry screen places a small vehicle, bench, lamp, and tree on a circular island against a purple floor grid. A bright perimeter and handwritten start cue concentrate attention around the vehicle. After activation, the scene expands into a warm orange and pink environment with paths, water, foliage, and large dimensional name lettering. Menu and map icons sit at the upper right.

The page's text explains driving as the way to explore the portfolio. It also documents movement controls, quality options, sound, and recovery from getting stuck. These are documented features; their operation was not comprehensively verified.

## Interpretation

For a creative developer, the interaction can serve as evidence of craft before a visitor opens a case study. The controlled introduction makes an unfamiliar interface less abrupt. The tradeoff is discovery cost: visitors have to understand the world before they can evaluate the work.

## Transferable recipe

**Original implementation proposal, not a reconstruction:** create a small illustrated workshop portfolio with three clearly marked project stations. Begin with semantic HTML containing the project list, contact route, and a short explanation. Add an optional interactive scene above that content only after the basic page works.

Keep the first camera view fixed, frame one obvious entry action, and introduce movement only after explicit activation. Use one shared project data source for both scene markers and ordinary links. On narrow screens, replace precision navigation with large station buttons; preserve the same project order and descriptions. Do not rely on understanding a spatial map to find contact details.

**Exercise:** build the three-station concept using original geometric illustrations before considering a 3D renderer. A visitor should be able to open any project directly from the text list, then return to the same place after trying the scene.

**Acceptance checks:** block the scene's script and confirm every project remains reachable; test entry, exit, and recovery with keyboard alone; ensure resizing never covers the exit control; ensure no audio starts before a deliberate choice.

## Accessible and lightweight adaptation

Offer a persistent plain-view route, visible focus, and named controls. Reduced-motion mode should use fixed views and instantaneous station changes. Load decorative scene assets on demand, cap rendering resolution, and stop rendering when hidden. Provide a useful poster and text while enhancement loads or fails.

## When to avoid it

Avoid game-like navigation for urgent tasks, routine purchasing, or portfolios whose content cannot support the extra interaction effort. A memorable scene is useful only when the visitor can still judge the work.
