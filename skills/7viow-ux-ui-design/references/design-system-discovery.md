# Design System discovery

Resolve the design source before making system-dependent visual decisions.

1. Read an explicit file, folder or named source supplied by the user, including its relevant linked tokens/components/states and usage rules.
2. If only a name or no source is given, inspect the current project's declared design references and the host's registered/shared sources that are actually available. Match the name and scope; do not assume a fixed home directory or search unrelated private projects.
3. If sources disagree, distinguish the product's creative method, formal Design System, existing implementation style and project supplements. Use the current explicit instruction to resolve precedence; ask if a consequential conflict remains.
4. If no usable Design System is found, explicitly tell the user and ask whether to supply a source, import one they choose, or authorize a project-local specification. Do not silently treat a chosen visual direction or existing CSS as an approved Design System. Reuse an earlier explicit answer instead of asking again.

Continue task/IA/content analysis that does not depend on the missing choice. Wait on dependent visual development when the choice changes it. If a repair is already explicitly authorized to preserve existing styles, retain those styles within that scope while reporting the missing formal source; the missing-system question still needs to be raised unless already answered.

Record the actual source/version and the rules used. A known system with an uncovered pattern is a specific gap, not absence of the entire system: derive the smallest project supplement from adjacent tokens/patterns and document it. Do not extend a global system without that scope.
