# Interaction contracts

Use the sections corresponding to the designed experience. Keep the contract in the project's design/spec or a concise working note, not a new universal architecture.

## Objects and navigation

For each visible object, define its identity, human-readable title, primary fields, related evidence, and allowed actions. Preserve qualified identity across categories; equal short IDs in different collections do not imply the same object. Supplementary data extends a main object through an explicit relationship, not a silent overwrite.

For the main path, define entry, decision/action, result, recovery, and return. Returning from detail should restore the relevant search/filter/selection/position; a shareable URL should identify its promised state. Preserve independent state scopes instead of allowing an unrelated prior selection to filter the next task invisibly.

## State transitions

For each consequential transition record:

| Starting state | Trigger | Result and visible feedback | Persistence | Recovery/focus |
|---|---|---|---|---|
| <actual state> | <user/system event> | <new state and its evidence> | <what survives close/back/reload> | <where the user resumes> |

Cover applicable loading, empty, error, success, validation, unavailable, and permission states. Also model interrupted editing, draft versus saved content, modal close, return, refresh, and keyboard focus where present. Explain what is stored locally, exported, or synchronized; these are different outcomes. A target date becomes a confirmed commitment only under the supplied domain rule.

## Inputs and results

For each control identify the object, metric/unit, time window, default, affected results, recalculation trigger, and pending/error feedback. Put the result's current scope beside the result. Multiple scopes can coexist, but labels and layout must prevent a user from reading one as the other. Changing an input must either update its promised outputs or make their stale state explicit.

## Comparison

Choose dimensions that support the user's decision. Keep dimensions comparable, object identity visible, and differences/conditions explicit. Narrow screens may use dimension-by-dimension groups, focused pairs, or another justified approach; avoid requiring memory of an entire preceding document. Removing or changing a candidate must update the comparison without mixing identities.

## Search and reading

Provide recognizable results with relevant context; take the user to the matching object or passage when the task requires evidence reading. Preserve the route back. Offer a clear empty-result recovery and useful handling of a missing source. Keep primary content, full text, related evidence, and internal production notes in distinct roles.

## Multiple audiences

Only when the brief defines different audiences, map audience → permitted content/objects → actions → search/detail/source/download paths. Produce the right content for each audience from the authoritative facts. Hidden controls or client filters alone do not establish access isolation. Keep the domain's disclosure and permission decisions in project input; escalate only an actual unresolved boundary.

## Compound and interrupted actions

When an action includes several outcomes, define each separately: what is committed, what is still pending, and what the user can recover if a later step fails. Saving input, generating a result, downloading and sending are distinct states. Match feedback, busy controls, persisted data and the next action to the actual completed step.

For reachable interruption, duplicate action, changed access/status, old tabs and delayed responses, define whether the pending operation may still take effect. A cancelled or archived item must not be reactivated by a late result; retain recoverable input and explain the available continuation. Choose relevant cases from this workflow, not every theoretical race. UX owns the outcome contract; engineering owns transactions, request identifiers and enforcement.

Completion: each partial outcome and reachable interruption has an observable state and recovery; a generic success toast cannot stand for all steps.

## Search, filters and ranking

When present, define searchable scope/fields and meaningful aliases; AND/OR behavior within and across facets; sorting/ties; result counts; reset and zero-result recovery. Derive displayed results, counts and any narrative from the same selected scope. Keep object identity and selection stable across detail/return. A promoted or pinned result must still satisfy declared filters and make its commercial role understandable; do not describe that ordering as unconditional relevance. Algorithm and commercial policy decisions belong to their actual owners.

## Data grain and interpretation

Name the counted object, grouping level, unit and time/scope beside a data result. Categories with identical labels must not secretly represent different underlying objects. Keep a chart, detail list and explanatory prose aligned with their respective documented grain. Credentials, visits, events and people are not interchangeable. Missing business formulas remain a domain/data question; UX does not invent a calculation to make the display look complete.
