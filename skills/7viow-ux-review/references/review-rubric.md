# Design review lenses

Read the relevant section when the task needs a deeper design check. Principles explain findings; the task and artifact determine whether a change is needed.

## Information architecture and hierarchy

Group by recognizable user objects, tasks, decisions, or states. Check naming, completeness, overlap, category rationale, and entry/return paths. Distinguish primary objects from supporting calculations, references, or metadata. Deep classification is a cue to compare simpler navigation, filters, search, or progressive disclosure; depth alone does not prove failure.

Identify the primary judgment and action. Map decision-critical information, task support, background, and optional detail to visible emphasis and order. Low-frequency metadata must not displace the main task. Different object types need enough structure to explain whether they can be compared or combined.

Check heading units against the brief's presentation-depth limit. Look for a redundant eyebrow/title/description stack, an object title missing the current task, and counts that merely restate a few visible cards. Respect a supplied threshold rather than treating one client's threshold as a universal standard. Distinguish remaining availability from pagination. Check whether independent rules could be scanned separately without losing their conditions, and whether a footer supplies a real declaration/attribution instead of repeating the site identity.

## Visual craft

- Composition: a useful focal point, stable alignment, and clear reading/interaction order; symmetry is not more important than the user's decision.
- Spacing/density: coherent outer/section/group spacing, object-action proximity, and density appropriate to the content and work.
- Typography: legible long text, distinguishable headings/body/metadata, appropriate line width/height, aligned numbers and units, wrapping that preserves meaning.
- Color: stable semantic roles and readable contrast; status remains understandable without color alone. Measure contrast when claiming a ratio.
- Surfaces: containers express objects, grouping, selection, or elevation; avoid fragmentation from unnecessary nesting, borders, or shadows.
- Components: consistent anatomy and variants for equivalent roles; forms have persistent labels, useful validation, and visible focus.
- Icons/illustration: coherent style and recognizable meaning; imagery explains content or brand without hiding the task.
- Motion: feedback and orientation are understandable; motion neither delays the task nor conceals state changes, and relevant reduced-motion behavior is covered.
- Responsive: redistribute priority and controls, not just scale/stack. A large desktop can also fail if sidebars squeeze a long document. A short viewport can hide modal actions without any horizontal overflow.

A visual emphasis needs an information, state, interaction, or brand reason. Context can justify richness and atmosphere; avoid treating every expressive design as decoration to remove.

Use actual long names beside adjacent controls to test fit, including collapsed navigation. Verify that differentiated destination cards remain identifiable and readable. Inspect footer/content bounding boxes when overlap is alleged; an annotation outline is not proof of a product border. Report the observed spacing rather than claiming an unreproduced collision.

## Interaction and accessibility

Evaluate discoverability, action/target proximity, feedback, recovery, and the weight of the interaction. A small clarification rarely needs a modal; consequential branching may need explicit choices. Check keyboard/focus, labels, text alternatives, readable status, and reachable targets where the artifact permits. Cite a specific standard and tested condition for a compliance claim; static inspection is not full accessibility certification.

Exercise success, warning, rejection, failure, loading, empty, expired, and revoked states that exist in the product. Tone, icon, wording and recovery must agree; color alone is insufficient. For copy/claim actions, observe a noticeable in-viewport result and the lasting item state, including clipboard failure. Check toast dismissal and focus/hover timing, full-width row confirmations, cancel/Escape focus recovery, and short-choice controls with keyboard and narrow-screen input. Verify requested new-page behavior by observing both the new destination and the retained source page. After a revoke/expiry, check that old validity text and success badges no longer promise active access.

Leave the original entry view open while changing permission from another authorized view. Check its visible state and its next resource request separately; a correctly blocked resource does not prove that an old access-granted message was updated.

## Content and trust

Verify representative names, IDs, relationships, numbers, units, dates, and statuses against the available facts. Keep unknowns honest and meaningful sample data identifiable. Copy should say what happened, what can be done, and what follows. Preserve necessary conditions while checking any declared rewrite limit; a necessary overrun requires an itemized meaning-based exception, not an unreported waiver. Technical terms belong when the target user needs them to make a decision.

## Design System

Map applicable tokens, typography, layout, components, states, motion, and voice to the supplied source. Check repeated patterns per component type. A gap in the system is not a documented violation: identify the uncovered need and whether the smallest supplement follows the existing system. Project supplements do not silently become shared tokens.

## Reader and maintenance boundaries

Check whether labels, version/status metadata, and absent-field notices help this reader's current task. Source completeness does not require displaying every field. The owner's full version is not automatically a maintenance screen. For repeated unwanted content, trace the common source and generated search/full-text/export surfaces that actually exist; a hidden label or isolated page fix cannot prove a shared generation issue is resolved. Keep the repair scoped to demonstrated affected paths.


When reviewing a rewrite contract, inspect its declared numerical copy limit/budget and itemized exceptions as well as meaning. Check the reported counts with available tools, preserve required objects/actions/conditions/units/timing, and distinguish a numerical overrun from a task failure. A baseline with no rewrite contract is not automatically defective for exceeding a compression ratio.

## Draft decisions, delivery feedback, and exit

Distinguish locked requirements from draft suggestions. Flag a repeated heading or short-page navigation item for its effect on the reader, even when it originated in a draft request; propose a change that preserves the underlying intent. Verify attribution against the confirmed business producer and the actual link destination, separately from source-code copyright.

Observe verification delivery beside its input at a narrow width: message and action must remain distinguishable, with the right success/failure treatment. Check active entry and reader exit paths, cancel/focus recovery, consequences, resource access after exit, and visible failure. A screenshot of an exit button alone does not establish the flow.

## Visual meaning and expansion readiness

Inspect the difficult representative page at its intended use scale before endorsing the same pattern for a batch. Does a visual preserve the real relationship, such as a cycle or conditional dependency? Are necessary conditions readable alongside the decision? Do grouping, proximity and whitespace reduce the reader's memory burden? No universal item count, font size or absence of overflow proves this. A diagram with all named nodes can still explain the wrong relationship. A declared visual reference needs a visible organizing contribution, not just matching colors.
