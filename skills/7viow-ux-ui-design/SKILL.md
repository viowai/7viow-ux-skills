---
name: 7viow-ux-ui-design
description: >-
  Create or revise product UX/UI: task flows, information architecture, screen designs, interaction states, interface copy, prototypes, and implementation-ready specifications. Use for design generation or an authorized design repair; use a review skill when the requested deliverable is only an assessment.
license: MIT
metadata:
  author: Viow
  version: "0.3.2"
---

# 7viow UX/UI Design

Turn a product intent into a coherent experience people can understand and use. Deliver the requested design artifact and the decisions needed to maintain it. The user may be a product manager, designer, builder, or team using AI; adapt the explanation to their design fluency without weakening the quality bar.

## 1. Bind the task and choose the design mode

Read the brief, source materials, current artifact, and relevant project rules. Identify audience/task, expected outcome, fidelity, format/tool, existing decisions, data, and constraints. Honor an explicit creative method. Treat the Design System as a separate production constraint, not as implied permission to replace that method.

- **Explore:** for an undecided core page/keyframe, substantial layout redesign or IA reorganization, read [direction-selection.md](references/direction-selection.md). Derive 2–3 substantive strategies from the user task, IA and information priorities; show inspectable keyframes with real content and important interactions, compare tradeoffs, and obtain a choice before detailed production unless selection is explicitly delegated. This is a core stage, not optional decorative variants.
- **Develop:** build the selected direction to the requested fidelity. Keep decisions already made; do not repeat option selection.
- **Repair:** change the authorized part of the existing artifact, preserve its data, working flows, and visual language, and verify affected tasks. A small correction does not restart the whole design process.

A larger revision can mix modes: preserve the selected product/frame, apply Explore to a module whose purpose, structure or main interaction remains undecided, and use Repair for settled local defects. Calling the whole request a repair does not bypass substantive direction selection for an unresolved part.

Resolve source questions from the workspace first. Ask only when a missing answer materially changes a product decision, factual meaning, or permitted action. Otherwise state a reasonable assumption and continue the authorized work. Completion: scope, mode, actual deliverable, and any decision that truly blocks it are clear.

## 2. Design the information and task structure

For a new or materially changed screen/flow, identify its user decision, content objects, relationships, key actions, and completion/recovery paths. Group using recognizable user categories; distinguish primary objects from supporting data, evidence, and internal metadata. Explain deeper navigation by a useful finding path rather than forcing an arbitrary layer count.

Map information to decision-critical, task-supporting, background, and optional roles. Use that map to determine order, emphasis, grouping, progressive disclosure, and narrow-screen behavior. A vivid visual needs a task, state, interaction, or brand reason.

Use representative real content and meaningful long/empty cases. Preserve source identity, units, status, uncertainty, and relationships. If a project fact is missing, leave an honest state instead of fabricating precise data. Project-specific business rules remain in the brief/spec, not in the reusable method.

For a handoff or substantial flow, use [ui-spec-template.md](assets/ui-spec-template.md). For complex state, comparison, data controls, search, or multi-audience work, read [interaction-contracts.md](references/interaction-contracts.md). Completion: the screen supports a named task with enough actual content to evaluate it; a layout shell alone is insufficient.

## 3. Shape the UI with the chosen design language

Read [design-system-discovery.md](references/design-system-discovery.md): locate the user/project/registered source, then read its relevant tokens, components, patterns, states and linked resources. If none is found, explicitly tell the user and ask whether to supply/import one or authorize a project-local specification; reuse an earlier answer. Continue independent task/IA work while the dependent choice is pending. Preserve an existing creative method and authorized repair style without calling them a discovered Design System.

Before high fidelity, read [ui-craft.md](references/ui-craft.md) and decide composition, typography, spacing, color, surfaces, components, imagery, motion, and responsive behavior as they apply. Work from the information priority, then refine the aesthetic—not a grid of interchangeable cards.

Reuse documented tokens and component variants. Record uncovered requirements and a minimal project-level supplement based on existing rules. A global Design System extension needs its own scope. For interface copy, read [ux-writing.md](references/ux-writing.md): explicit outcomes, clear recovery, consistent naming, necessary conditions and mandatory per-item numeric checks. Existing-copy rewrites default to ≤80% of original non-whitespace characters, with documented necessary-meaning exceptions; new copy has a declared numeric length budget.

Completion: visual hierarchy expresses the user's decision; repeated patterns are coherent; relevant controls, text, states, and layouts have concrete definitions.

## 4. Produce the requested artifact

Match the format and fidelity to the request. Specifications, low-fidelity designs, native design files, interactive prototypes, and changes to an existing app are different deliverables. A local HTML prototype is useful when requested or needed to judge an interaction; it is not mandatory for every design task.

When producing an interactive artifact, implement the required main path, navigation, state transitions, empty/error recovery, and realistic sample content. Preserve existing sources when the task requests a separate candidate. Use the available project/tool conventions; keep a standalone deliverable self-contained when required. The output must include all resources needed to open or run it.

For a repair, keep a direct before/after relationship to the supplied artifact. Maintain original data and unaffected behavior. Take a real baseline if visual evidence is needed; do not fabricate a before image for a new design. For generated, data-driven, or multi-view artifacts, read [source-repair.md](references/source-repair.md): trace the element to its maintained source, repair that source, regenerate the affected outputs without relying on patched exports, and verify the rebuilt task. Directly maintained artifacts need no invented generator; an output-only patch with missing source cannot establish a durable repair.

Completion: the artifact exists in the requested format and can be opened or run; unimplemented interactions are clearly labeled and cannot satisfy an interactive request.

## 5. Verify the user's result and hand off

Use [acceptance.md](references/acceptance.md) to test the tasks affected by this work. A runnable artifact needs actual behavior and visual inspection with the available browser/design tools. Report tool limitations and unverified scope accurately. A source-only check does not verify what the user sees.

Fix demonstrated defects within the authorized scope, then rerun their tasks and directly affected regressions. For a final interactive/high-fidelity candidate or design-review workflow, read [design-review-handoff.md](references/design-review-handoff.md), discover and apply the available Review method, and close actionable findings before claiming that cycle complete. Reuse an existing same-scope assessment and preserve its IDs. When Review is unavailable, deliver the authorized artifact with Design self-check and the explicit unperformed Review gap. Distinguish same-execution self-review from independent evaluation.

Deliver the actual version/entrance with concise guidance: intended user and task, meaningful design choices, how to review/use it, tested conditions, remaining limitations, and next action. Place source history and internal implementation records in companion material, not product copy. Follow the user's language and existing project voice.

Completion: the requested artifact and task results are inspectable; claims name what was actually tested. No fixed round count, numerical quality score, or author assertion replaces acceptance evidence.
