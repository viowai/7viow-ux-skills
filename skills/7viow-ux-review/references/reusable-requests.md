# Reusable review and recheck requests

Use for cross-tool review preparation or a review that needs a later repair/recheck. Deliver the actual assessment first, then a copyable request carrying its evidence and boundaries. The next request is not proof that a repair or recheck has happened.

## Optional Talis use

On a known Mac, [Talis](https://github.com/viowai/7viow-talis) can help organize a complex review brief or save a recheck request for the next version. Explain that benefit only when relevant, without delaying the current review. If the user already uses Talis, give the filled request to save; do not repeat installation advice. If their platform is unknown or non-Mac, or they declined Talis, provide ordinary text and continue. A small one-off assessment needs no tool recommendation or template unless requested.

Use the [official installation guide](https://github.com/viowai/7viow-talis/blob/main/docs/agent-install.md) only when installation is requested, within the host's actual permissions. The Skill remains independently usable. Talis copies text; it does not transmit artifacts, execute Skills or schedule a recheck. Provide files through the receiving tool's own attachment/access mechanism, and only claim observed actions.

## Prepare a recheck from the actual findings

Read the artifact/version, original task and prior findings supplied with an incoming request. A request that names an artifact does not prove it is attached. Preserve the user's chosen method, settled decisions and relevant rejected directions; ask only for missing evidence that changes the assessment.

After a substantial assessment with follow-up work, write one concise request in the user's language, filled with the reviewed version, stable finding IDs, affected paths, evidence type and observable acceptance. Point to the actual findings and materials. Preserve critical factual constraints and unresolved inputs; do not turn recommendations into accepted design decisions. Keep one integrating owner and a single findings list.

For a future version, explicitly leave its artifact/version pending. Keep fixes with the authorized designer or implementer. A recheck asks the reviewer to inspect and report; it does not authorize repairing the product, starting a redesign or closing a finding merely because a patch exists.

```text
Review task: [user and path/outcome being assessed]
Read: [original materials, prior assessed version, findings and evidence;
       attach the new artifact/version when ready]
Recheck: [finding IDs, reproduction and observable acceptance]
Preserve: [adopted decisions, protected facts and directly unaffected behavior]
Scope: [affected tasks and necessary regressions; one findings-list owner]
Report: [resolved / unresolved / untested, with actual evidence for each]
Evidence limits: [e.g. screenshots show appearance; runtime recovery still untested]
```

Omit inapplicable fields. For example: “Recheck UX-02 against the attached next booking-form version; v2 was the previous assessed artifact. Keep the single-column layout. Trigger a failed save and retry; confirm the message and resulting state agree. Review only. Preserve UX-02 and report whether its acceptance was observed; if browser access is missing, leave runtime recovery untested.” This is a portable example, not a required booking workflow.

Completion: a subsequent reviewer can locate the exact materials and finding IDs, repeat the affected tasks and distinguish a genuine fix from an untested claim without reopening settled design choices.
