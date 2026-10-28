# Interface writing

Use for authorized creation or rewriting of labels, instructions, statuses, errors, empty states, and consequential confirmations. Layout-only work preserves existing wording; the numeric rewrite rule does not grant permission to change it. Research prose and document bodies are not interface-copy compression targets.

Write for the user's current decision. Explain the event, available action, and consequence or recovery when relevant. Use the product's voice and consistent names. Prefer precise action labels over ambiguous confirmations, while keeping familiar conventional labels when their outcome is already clear.

Keep necessary scope, units, time ranges, eligibility, and unresolved facts. Meet the numeric requirements below while preserving meaning. Avoid fabricated certainty or decorative metadata. Technical terms are useful when the intended user needs them for choice, permissions, cost, privacy, or recovery; otherwise express the practical result.

Distinguish unknown from none, draft from saved, locally saved from synchronized, planned from confirmed, and attempted from completed according to the actual product rules. State what the user can do when the result is empty or unavailable. Treat sample content as sample, not a claim about real people or transactions.

Check a representative label by performing its action: does the resulting behavior match what the label promises? If the layout cannot hold a necessary condition, fix the information design instead of hiding the condition.

## Compact interface information

Use context already established by the product and selected navigation. A title can combine the current object and purpose; an extra category eyebrow that repeats either is unnecessary. Keep a heading unit to the user's agreed number of levels, commonly title plus necessary support. Do not add a third line merely to complete a template.

Split independently actionable rules into separate statements. Keep each condition with the rule it qualifies: validity duration, whether entry extends it, and replenishment are separate rules. Structure a notification preview as fields when that helps scanning, while preserving its actual copyable message. Do not turn every clause of continuous prose into a list.

Choose quantities by the reader's decision: remaining availability, current selection, and paginated position mean different things. Omit a redundant total for a small visible set; preserve an explicit project threshold. Footer text should carry an actual declaration, attribution, or confirmed copyright rather than repeat the page introduction. Never invent a rights holder.

After a state transition, remove stale promises: a revoked item must not still say its old deadline is an active validity promise, and an expired result must not retain a success badge that implies current access. Describe the event and next available action in the appropriate state treatment. A transient toast and persistent item status have different jobs; avoid an additional duplicate success paragraph.

## Mandatory numeric acceptance

For an existing UI copy rewrite, the default maximum is **80% of the original length per item**. Count plain visible Unicode characters excluding whitespace, including punctuation; use the same method before and after. Do not average multiple items or move text elsewhere merely to pass the ratio. Unchanged factual values are not rewrites; keep an explicit mapping when one message is split or combined.

Record `id | before | after | original characters | revised characters | ratio | result | required meaning/exception`. A ratio above 0.8 must be revised again or explicitly recorded as an exception with the exact information that cannot be removed and why it is necessary. Safety, consent, cost, eligibility, uncertainty, scope, units, timing or a short essential action label may justify an exception. Generic “sounds better” is insufficient. A justified exception is not a numerical pass; present it separately and verify its necessary meaning in review. Do not remove facts or make a result misleading to satisfy the metric.

New copy has no original: define a numeric character budget for each relevant control/message role before drafting, based on task, layout and necessary content. Measure the actual result. If the budget cannot preserve essential meaning, revise the design or document a specific exception/budget change; never invent a compression baseline.

Use [check_copy.py](../scripts/check_copy.py) for repeatable measurement when Python is available; otherwise compute the same counts with available tools. Input is a JSON list with `id`, `mode` (`rewrite`/`new`), `after`, and either `before` or positive integer `max_chars`. An optional `exception` contains `reason` and `required_meaning`. The script reports numerical results and exceptions; it cannot establish semantic completeness. Keep this record in delivery/review material, not product copy.

Completion: all affected copy is measured, each over-limit item is repaired or individually justified, and required meaning is checked against the source. Report counts of numerical passes, exceptions and unresolved items separately.

## Reader-facing information

Retain complete source facts in the underlying artifact/data, but choose visible fields for the reader's current task. Show a type label, version, production status, internal ID, or missing-field message only when it adds needed understanding or changes a decision. Empty optional metadata need not become a row of “not provided” labels. Keep missing decision-critical facts explicit. The author's complete reading version is still a reading experience, not automatically a maintenance console. Keep build/release/review administration in a separate maintenance entrance.

When the same unwanted content is generated in several places, fix its owning source/derivation and affected shared views, including full text/search/export where present. If the product has a build chain and a concrete forbidden field/path is confirmed, add a targeted failing fixture at that chain; CSS hiding or a one-page patch does not establish removal from the generated product.

## Draft intent and attribution

Honor locked names and factual requirements. Treat tentative labels as editable: preserve the task they describe, challenge wording that creates a concrete comprehension problem, and explain the useful replacement briefly. A section name should match its content, not the wording of a draft instruction.

Use the confirmed project producer for product attribution. Keep producer, copyright holder, and linked-site owner distinct; a developer identity or open-source license notice does not automatically determine a business site footer. Label a personal-site destination honestly when it represents a company founder.

## Labels, locale, voice and tone

For classification or search, use the concept's preferred label and meaningful aliases from the content model. A label should predict its destination or action; state labels should identify the evidence and available action. Keep the underlying identity stable when wording changes.

Use personality where it supports the relationship and task. In failure, consent or uncertainty, clarity and recovery take priority over jokes or emotional decoration. Voice can stay recognizable while tone responds to the situation. Broader brand voice and prose development belong to the appropriate writing method.

When localization is in scope, check actual labels, ambiguity, units/dates, culturally relevant meaning and rendered expansion with the target language/context. Translation preserves meaning; do not apply a cross-language 80% ratio. An authorized rewrite of existing copy in the same locale uses the rewrite rule; new localized copy uses a budget appropriate to that locale and layout. A machine translation or expert review is not participant validation.
