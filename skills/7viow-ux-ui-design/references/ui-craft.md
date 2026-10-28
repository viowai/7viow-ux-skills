# UI craft

Use before producing or materially changing high-fidelity screens. Make choices for the actual content and task; keep existing choices in a local repair unless they cause the problem.

## Composition and hierarchy

Choose a focal object/judgment/action, a reading path, and a grid appropriate to the content. Put actions near their targets and feedback near the decision. Balance whitespace and density for the user's work; prioritize meaning over equal-sized tiles. Give explanatory visuals enough room to explain something, without displacing the main task.

Treat supplied draft labels and navigation suggestions as proposals unless explicitly locked. When one creates repetition or obscures the task, state the concrete drawback and apply a clearer alternative within the authorized repair. Preserve the intended outcome; a short page needs an extra section jump only when it meaningfully reduces finding effort.

Audit each page, section, and card heading as one presentation unit. Prefer its title plus only necessary supporting information; do not automatically stack an eyebrow, title, and explanation. Remove a label already supplied by the site, selected navigation, or title. Where needed, combine the current object and task into one meaningful title. Honor an explicit two-level presentation cap; this is not a reason to delete required source content or silently flatten document structure.

Do not repeat a small, immediately visible collection as a total. Follow any supplied threshold, such as showing a count only above five items. A remaining quantity supports a different decision: show “8 remaining” when availability matters, rather than a decorative “8 / 10” or page-like fraction without pagination. Keep footer declarations or confirmed copyright separate from the content in normal document flow; do not fill the footer with a repeated product name and audience label.

## Typography and spacing

Define a small coherent hierarchy for titles, object names, body, status, metadata, and actions, using supplied tokens when present. Check real long titles, multiline labels, numbers, units, and empty states. Use comfortable paragraph width and line height; large windows should not squeeze a document behind sidebars. Coordinate page/section/group spacing and control density rather than assigning arbitrary values per element.

## Color and surfaces

Use stable roles for action, selection, warning, success, disabled, text, background, and borders. Preserve readable contrast including muted text, focus, and charts; color alone must not convey essential status. Cards represent an object/task/state or useful grouping. Use elevation/borders/radius consistently and avoid redundant nested surfaces that fragment the reading path. Expressive style is valid when supported by the brief and brand.

When adjacent cards represent materially different destinations or audiences, give them recognizable accents and readable surfaces while retaining text/imagery as identifiers. Keep these identity accents separate from state semantics. A denied application, expiring access, successful copy, and failed operation must not all use the same calm informational treatment. Bind tone, icon, label, and recovery action to the actual state.

Keep long-lived entry screens synchronized with authoritative state, including changes made elsewhere. Verify the visible transition after revocation or expiry as well as resource enforcement; blocking the next resource request does not correct a stale “access granted” screen.

## Components and details

Define reusable anatomy, density, variants, states, and copy for buttons, forms, lists, tables, tags, navigation, dialogs, and relevant specialist components. Inputs have explicit labels and recoverable errors; dialogs have clear exits and focus return. Table and chart labels preserve unit/time meaning. Icons need understandable semantics and consistent visual weight. Images need a purpose, appropriate alternatives, and honest provenance.

For a deliberate action such as copy/claim/save, provide a noticeable result in the active viewport. Use a brief accessible toast for transient success and keep recoverable errors beside their target; retain a useful row state after the toast closes without repeating the same message in several blocks. Do not move focus to a toast; allow dismissal and pause its timeout while hovered or focused. A grid-row confirmation must span a readable row, not inherit a narrow cell. Verify its destructive consequence, cancel/Escape recovery, and focus return.

Place a delivery result beside the relevant verification control. Give its next action a distinct button or link row with spacing that survives narrow widths; keep status text and clickable text distinguishable. Verify success and failure treatments.

Make session exit discoverable from both the active entry and reader. Explain material consequences before ending access: ending a browser session and revoking a grant can require different recovery. Reuse the actual mechanism, keep cancel/focus recovery usable, and leave a visible error when exit fails.

Choose one primary feedback channel per event. If a visible field, form, or confirmation already gives an actionable error, do not repeat that error in a simultaneous toast or announce it twice. A request for noticeable copy feedback does not justify adding error toasts to every form.

With a few mutually exclusive choices, consider directly visible radio options instead of hiding them in a select. Use native semantics and verify labels, selected/disabled/focus states, keyboard selection, and narrow-screen sizing. When the brief requires a separate page for an independent reader or destination, keep the originating task open, implement that behavior for links and asynchronous entry, and provide a usable fallback if a new window is blocked. Do not apply it blindly to in-place filters and task steps.

## Motion and responsiveness

Motion should explain a transition, feedback, or orientation without blocking work. Account for relevant reduced-motion preferences. Reorder priority at narrower widths, keeping decision-critical content and controls reachable. Inspect short heights when fixed bars or dialogs exist. Long tables may scroll in their own container; important text should not shrink or truncate until its meaning disappears. Use actual target dimensions, not a universal breakpoint list.

## Design System mapping

Map decisions to applicable tokens, components, patterns, and states. Document only real gaps or justified deviations; derive small supplements from the nearest existing rules. A missing rule is not permission to silently import another visual system. Repeated equivalent components should keep the same meaning and anatomy.

## Meaningful grouping and theme changes

Chunk content around a recognizable task or relationship. Use headings, proximity and contrast to make boundaries visible; a fixed number of cards or items is not a cognitive limit. Preserve reading and action continuity across groups.

For a theme change, distinguish identity accents from semantic success/warning/error and content imagery. Trace shared text, surfaces, controls and relevant output variants to their actual token/component source; changing a sidebar alone does not establish a coherent theme. Inspect real rendered variants and states, including computed styles when they explain a mismatch. Keep the project-specific palette in project sources.
