---
name: 7viow-ux-review
description: Review product UX/UI, task flows, prototypes, screenshots, or shipped interfaces. Diagnose usability, information hierarchy, interaction, content, visual craft, and design-system issues with evidence and testable repairs. Use for an assessment or a post-repair recheck; use a design skill when the main request is to create or redesign the artifact.
license: MIT
metadata:
  author: Viow
  version: "0.3.2"
---

# 7viow UX Review

Evaluate whether the intended user can understand, decide, act, and recover in the supplied experience. Deliver a prioritized assessment with evidence and a repair contract. The requested review is the primary deliverable; modifying the reviewed artifact requires a repair request.

## 1. Establish the review target

Identify the audience and task, artifact/version, stage, relevant devices, requested scope, source facts, and any locked decisions. Reuse known context; ask only when a missing answer would change the assessment. Keep the user's chosen creative method separate from the Design System's production constraints.

Choose the evidence available:
- **Running interface:** execute representative tasks in the supplied environment; preserve the user's data and restore temporary test state.
- **Mockup or screenshot:** assess visible structure/craft and specified behavior; mark runtime behavior untested.
- **Specification:** assess decisions, coverage, and handoff clarity; do not imply a rendered experience was checked.

Read existing same-scope findings first. Maintain one problem list, adding evidence or uncovered issues rather than duplicate audits. Completion: the actual review object and the limits of observable evidence are identified.

## 2. Walk the user's tasks

For a running artifact, use available browser or design tools to follow entry → decision/action → outcome → recovery/return. Check a meaningful result, not just whether a button reacts. Use [task-walkthrough.md](references/task-walkthrough.md) when the experience contains search, comparison, data controls, editing, navigation, or multiple audiences.

Record starting state, actions, expected result, observed result, and the evidence location. Inspect the code or data only where it explains a reachable problem or verifies an important factual relationship. Note when a cause remains a hypothesis.

For a narrow change, follow its affected task and plausible regressions. For a broad review, cover learnability, efficiency, memorability, error recovery, and confidence/satisfaction through specific observations. Expert judgments are not measured user satisfaction or usability-study results.

Completion: each covered task has an observed outcome or a specific evidence gap; a static screenshot cannot close an interaction test.

## 3. Inspect the relevant design layers

Use [review-rubric.md](references/review-rubric.md) for information architecture, visual craft, accessibility, content integrity, or Design System review. Apply the sections that can affect the task; avoid mechanically emitting every heading.

When a Design System is specified, locate it from the explicit source or current project declaration and read the applicable rules, tokens, components, states, and linked resources before claiming compliance. Cite the exact constraint for a violation. Distinguish a documented violation from an undefined area that needs a proportionate supplement. If no usable source is found after checking user, project and available registered references, explicitly tell the user and ask whether to supply/import one or authorize a project-local specification; reuse an existing answer. Continue assessment areas that do not depend on it, without claiming Design System compliance.

Judge dynamic information in context: identity, status evidence, unit, time range, selection, and audience must agree with what the interface promises. If a malformed relationship causes misleading content, describe the UX impact and hand the engineering repair to its owner.

Completion: findings connect to an actual task, artifact detail, or cited constraint; preference alone is not a defect.

## 4. Prioritize and hand off

Use only **High / Medium / Low** as defined in [severity-guide.md](references/severity-guide.md). Keep severity separate from confidence, implementation effort, and business priority. A quick first impression is a diagnostic cue, not a timed user study or automatic High rating.

Use [review-repair-template.md](assets/review-repair-template.md) for structured reviews or repair handoffs. Keep problem ID, target/version, task, reproduction, expected/actual, evidence type/location, impact/severity, smallest useful repair, and observable acceptance. DS and audience references are conditional.

Lead with the most consequential findings; acknowledge sound behavior when it matters. Recommend structural repair before cosmetic polish when structure causes task failure. Preserve the chosen product/method and request scope; a full redesign needs a demonstrated reason and authorization.

Completion: another designer or engineer can execute the repair and tell whether it worked without guessing your intent.

## 5. Recheck and deliver

When asked to recheck, rerun each repaired task plus directly affected regressions against the identified new version. For generated or data-driven artifacts, use the source-and-regeneration branch in [task-walkthrough.md](references/task-walkthrough.md): identify the maintained source and examine the regenerated result before closing a durable-repair claim. Keep unresolved and untested items distinct. Close a finding with observed acceptance evidence, not a patch description. New findings need new evidence; do not invent defects to fill a round count.

Deliver the assessment, the actual artifact entrance when available, tested conditions, remaining gaps, and the next concrete action. Explain how the reader should review and respond in a short companion note. Keep internal test logs and implementation details out of product copy. Do not claim user validation, full accessibility conformance, or cross-host compatibility beyond the evidence.

`7viow-ux-ui-design` may consume the repair contract if installed and modification is requested. This review skill works independently; a missing companion is not a reason to stop a review.
