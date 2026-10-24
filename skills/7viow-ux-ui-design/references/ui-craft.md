# UI craft

Use before producing or materially changing high-fidelity screens. Make choices for the actual content and task; keep existing choices in a local repair unless they cause the problem.

## Composition and hierarchy

Choose a focal object/judgment/action, a reading path, and a grid appropriate to the content. Put actions near their targets and feedback near the decision. Balance whitespace and density for the user's work; prioritize meaning over equal-sized tiles. Give explanatory visuals enough room to explain something, without displacing the main task.

## Typography and spacing

Define a small coherent hierarchy for titles, object names, body, status, metadata, and actions, using supplied tokens when present. Check real long titles, multiline labels, numbers, units, and empty states. Use comfortable paragraph width and line height; large windows should not squeeze a document behind sidebars. Coordinate page/section/group spacing and control density rather than assigning arbitrary values per element.

## Color and surfaces

Use stable roles for action, selection, warning, success, disabled, text, background, and borders. Preserve readable contrast including muted text, focus, and charts; color alone must not convey essential status. Cards represent an object/task/state or useful grouping. Use elevation/borders/radius consistently and avoid redundant nested surfaces that fragment the reading path. Expressive style is valid when supported by the brief and brand.

## Components and details

Define reusable anatomy, density, variants, states, and copy for buttons, forms, lists, tables, tags, navigation, dialogs, and relevant specialist components. Inputs have explicit labels and recoverable errors; dialogs have clear exits and focus return. Table and chart labels preserve unit/time meaning. Icons need understandable semantics and consistent visual weight. Images need a purpose, appropriate alternatives, and honest provenance.

## Motion and responsiveness

Motion should explain a transition, feedback, or orientation without blocking work. Account for relevant reduced-motion preferences. Reorder priority at narrower widths, keeping decision-critical content and controls reachable. Inspect short heights when fixed bars or dialogs exist. Long tables may scroll in their own container; important text should not shrink or truncate until its meaning disappears. Use actual target dimensions, not a universal breakpoint list.

## Design System mapping

Map decisions to applicable tokens, components, patterns, and states. Document only real gaps or justified deviations; derive small supplements from the nearest existing rules. A missing rule is not permission to silently import another visual system. Repeated equivalent components should keep the same meaning and anatomy.
