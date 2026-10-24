# Repair the maintained source

Use when changing an existing artifact that is generated, rendered from data/components, or distributed in several views. Identify the maintained source before deciding where to edit.

## Follow the change to its owner

Trace the affected element to the smallest relevant chain: source content/data → template, component, or renderer → generated file → visible view. Inspect the existing build/export instructions and one concrete affected element; do not inventory the entire project without a reason.

- For directly maintained HTML, a native design object, or a source document with no generation step, edit that source directly. Do not invent a build pipeline.
- For generated HTML, copied exports, role/audience projections, or values rendered from data, change the owning data, template, CSS, component, or generator. Editing a screenshot, rendered DOM, or an exported file alone does not repair its maintained source.
- Keep facts, units, periods, object identity, permissions, and unknown states intact. A visual or wording repair does not authorize changing the data meaning. If a necessary repair changes a previously visible value, explain the reason and source.
- An authorized one-off export can be edited directly. Label its scope and the overwrite risk; do not report that future builds inherit the change.

If the source is unavailable, state exactly what can be repaired in the supplied artifact and what cannot survive regeneration. Continue independent work. Request the missing source only when a durable repair depends on it; do not fabricate a generator or claim one was updated.

## Rebuild and test persistence

Run the project's existing generation/export path in the authorized copy. Generate the affected outputs from the changed source without relying on previously patched output files; a separate output directory or a disposable copy is usually enough. Do not delete user work to make this test possible.

Inspect the regenerated version, then exercise the repaired task and its relevant adjacent states. Check affected audience views, search/full-text/download representations when they share the changed source. For data-driven behavior, also exercise a second representative record or a changed input to expose a hardcoded first example. Preserve the original business input; probe changes stay in a disposable test copy.

A successful build alone is not acceptance. Record the source changed, generation command/path, regenerated artifact, actual task result, and untested dependencies. Hand this evidence to Review. If rebuilding or inspecting the result is unavailable, distinguish a source patch from a verified durable repair.

## Useful counterexamples

- A selected-item bar works only because generated HTML was patched; the normal build removes it. Fix the renderer and recheck the rebuilt page.
- One role's exported page has the new label but the next export restores the old label. Fix the shared label/template while preserving each role's actual data scope.
- A live value is pasted into markup to make a screenshot look right. Repair formatting or binding and check another value; do not freeze the data.
- A standalone HTML file is itself the maintained source. Editing and reloading it is valid; demanding a generator would add unrelated work.
