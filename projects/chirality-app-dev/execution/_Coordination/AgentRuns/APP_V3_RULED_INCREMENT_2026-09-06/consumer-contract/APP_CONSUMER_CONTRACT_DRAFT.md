# App consumer acceptance draft — ruled design directions

Status: CANDIDATE CONSUMER CONTRACT for Runtime fan-in. The owner selected the five design directions; concrete cross-owner parameters below are recommendations awaiting Runtime finalization and the required acceptance instruments. No wire enum, new endpoint, credential policy, lifecycle act, or implementation is created here. Fixture IDs refer to FIXTURE_SPECIFICATIONS.json, all unexecuted.

## Presentation decisions within the accepted intent

Use the Walkthrough's dialogue-centred shell: preserve the primary conversation and composer; put account controls in the left account row/popover and full Settings in the right view. Show request review inline with the relevant activity/conversation and open provenance/details in the right panel without replacing the primary chat. Do not auto-switch the user to another chat for a background request; show its chat/root identity and a review affordance. Final component loci remain the owning package's implementation brief.

Expose a short readable title first, with exact identity and evidence available in details. UI copy below is presentation text, not protocol vocabulary. Never infer a role from child origin, supplier text, labels, timestamps or a currently selected conversation. Global identity does not imply active-root execution readiness. Retain D122's one local-model-server indicator and no OpenAI/API status dots. Unknown or stale status has neutral treatment, not a green success badge.

## Child approval action/state matrix

| Observed state | Visible presentation | Permitted action / required result |
|---|---|---|
| Origin or current authority unavailable | “Checking who requested this” or “Request unavailable”; no actionable prompt until authoritative join | Inspect available context; no Allow/Deny/session grant. Runtime decides join expiry; App cannot make association authoritative. F01/F02 |
| Current attributed request | Requesting child, parent conversation, active root, destination/protocol, permission scope; disclose broker in details separately | Render only advertised, supported, qualified decisions. Acting human identity comes from authenticated contract, never editable arbitrary actor text. Before response refresh/revalidate exact request/revision. F01/F03 |
| Different current chat/root | Identify the originating chat/root on the request | Reviewing cannot rebind it to selected chat. Return action targets the originating identity only; missing permission gives unavailable. F04 |
| User closes view | Prompt is dismissed locally; pending request remains visibly discoverable where still valid | No grant, denial or stop implied. No automatic default decision. F05 |
| Human intent durably recorded, transport not confirmed | “Decision recorded”; then “Sending decision” if actually sending | Lock duplicate submissions. Do not report granted/applied. Identical redelivery follows Runtime's idempotency contract; App does not retry uncertain delivery. F06 |
| Transport confirmed, application unconfirmed | “Decision sent; application unconfirmed” | Inspect evidence; no automatic Retry, no green applied claim. F07 |
| Provider resolution with no attributable decision | “Request no longer available”; details explain resolved without known decision | Controls disabled. Do not synthesize approval, denial, child completion or supplier application. F02/F08 |
| Stale/replaced/retired request | “Request expired” or “Work stopped” only when the cause proves it | Disable decisions, refresh current state; keep historical intent/origin. Old generation never reactivates. F08/F09 |
| Delivery uncertain / reconciliation required | “Delivery uncertain” / “Recovery required”; explain work may have acted | Inspect/recover through accepted Runtime flow; no silent replay or unsafe Retry. Preserve draft/history. F07/F09 |

Deny appears only when actually advertised and qualified. Session-wide grant is a separate explicit action and explanatory scope; if its exact scope/grouping evidence is unavailable it is not offered. Unsupported protocol is labelled accurately or unavailable, never relabelled HTTPS. The old v2 client must not receive a downgraded primary-looking child prompt. Negotiation failure renders the feature unavailable while preserving other supported work. F03/F10.

### Separate Stop action

Label **Stop current work**. Before the action, show persistent explanatory text: “Stops this conversation's current turn and its active child work. This does not deny only this request.” The affected conversation is named even if it is in the background. Do not claim a per-child stop. This meaning applies only after Runtime confirms the proposed whole-turn scope in its final contract.

An intentional Stop click invokes the existing/accepted stop operation once. Display “Stopping…” until outcome evidence arrives; “Stopped” requires the corresponding observed terminal/lifecycle evidence. A failure or uncertain result remains visible. Closing the approval view is not Stop. Preserve the primary conversation, unsent draft and historical evidence. No additional confirmation dialog is required by this draft: the action's explicit label, target and nearby consequence text make the choice concrete. F11/F12. Missing per-request denial remains a distinct unmet acceptance obligation; this escape never waives it.

## Account and isolated-context matrix

| Situation | Presentation / action | Must not imply |
|---|---|---|
| Global account available; root needs consent/sign-in/readiness | Show global identity in left row; active-root Settings says the exact missing step and root name | Global signed-in status grants root readiness or consent. F13 |
| Account/root/epoch/policy switches during read | Loading/unknown for the newly selected root; ignore late previous-root response | Previously granted root repainting the new root as granted. F14 |
| Logout/account switch requested | Show exact offered scope and pending/confirmed result returned by accepted brokerage contract | Credential copying, all-root revocation, selected-root-only logout or token deletion before those semantics are accepted. F15 |
| No folder, design not implemented | Truthful existing restricted composer; retain draft and choose-folder path | Sending already supported by an invented home/default root. F16 |
| Future accepted isolated context ready | Composer shows **Isolated chat**; details explain no project folder access and only actual permitted capabilities | No filesystem exists, universal sandbox strength, or authority over known folders. Context path need not dominate UI; identity remains inspectable. F16 |
| Attach a project to an existing isolated chat | Recommend explicit **Start a new chat in this folder** after draft preservation; retain old history separately | Silent migration/rebinding, inherited approval/consent, or old acceptance applied to a new root. Final transition contract remains Runtime/Root-owned. F17 |
| Isolated context unavailable/removed | History display follows accepted read entitlement; execution unavailable with reason | Recreate missing context or replay old work automatically. F18 |

Shared-login brokerage remains design-only. Runtime must return typed readiness, identity and continuity semantics; App maps them without receiving tokens. Keep root consent separate from account credential custody. No-folder design also needs lifetime/history/delete/export and allowed attachment semantics before UI actions can be implemented. Deleting a chat remains local hide under the recorded shell decision; do not silently equate it with deleting an isolated context or stored evidence.

## Workflow proposal and currency matrix

| Proposal/workflow situation | User-facing action | Acceptance rule |
|---|---|---|
| Current proposal with exact contents and authority context | Show proposed change, scope/root, source/currency, and Accept / Adjust / Not now | Accept binds to the exact reviewed content and authoritative prior basis; an event or valid DTO is not evidence a human accepted it. F19 |
| Content or authoritative basis changes during review | Mark changed/stale; disable the stale Accept and offer refreshed review | Never apply latest unseen content using the old click. Runtime/domain exact expected-content identity must reject races. F20 |
| Adjust | Open editable proposed content while preserving original provenance | Editing is not acceptance; the revised candidate must be reviewed explicitly. No prior approval carries forward. F19 |
| Not now | Dismiss/record the appropriate chat trigger according to accepted contract | Does not deny unrelated proposals, change deliverable lifecycle, or create permanent global suppression. F21 |
| Concurrent advancement or cross-folder Bind | Show conflict or new binding requiring fresh validation | A copied acceptedAt/event/hash alone cannot authorize a new root; current prior-hash comparison is required. F22 |
| Instruction/source drift | Show stale source and affected action unavailable pending accepted current basis | No silent repin, latest-instruction substitution, roadmap status promotion or replay. F20 |

Root owns instruction/role semantics, Runtime execution contracts, and the domain/project instrument human gate meaning. App preserves file-native authority and marks derived progress. Four existing terminal identifiers remain intact; proposal-view states are not new terminal events. D117 optional managed-attempt replay remains separate from native approvals.

## Cross-owner parameters to resolve in Runtime fan-in

1. **Representation and identity:** recommend explicit negotiated closed child-approval projection; unknown version unavailable. Runtime must name exact version negotiation, request digest/canonical serialization, identity/read entitlement and authenticated responder policy. App needs display-safe actor labels plus inspectable stable opaque identity, not raw supplier payload. Without this, no actionable child prompt.
2. **Stop scope and uncertainty:** recommend whole current conversation turn with its active child work, preserving history; return distinct in-progress/observed outcome/unknown evidence. Runtime must confirm generation impact and whether other work is affected. Broader impact returns to owner; App cannot promise smaller scope. No per-request denial waiver.
3. **History and limits:** recommend read-only origin/intent/settlement after shutdown with existing project authorization, never live authority. Runtime finalizes retention/read entitlement and bounds/depth/lifetime coverage; App exposes unavailable/limit cause without inventing native fan-out policy. Evidence absent means no historical-attribution completion claim.
4. **Brokerage:** recommend global identity plus separate active-root readiness/consent. Runtime/Root must settle logout-all versus root-specific operations, account switch/revocation/epoch and custody. App offers only accepted operations with exact scope labels. A1 aggregation cannot satisfy accepted A2 brokerage.
5. **Isolated context:** recommend one distinct context per chat and project attachment as a new session, to avoid cross-chat/project authority ambiguity; these are contract recommendations, not selected backend/storage parameters. Runtime/Root decide lifetime/deletion/export, registration, instructions/account and tools/attachments. Ordinary chat hide must not destroy execution records. Unresolved parameters keep sending held.
6. **Workflow:** recommend exact reviewed content plus expected prior basis bound to authenticated human decision; conflict returns to refreshed review, never auto-merge/retry. Runtime/Root/domain owners settle versioned events, actor/approval provenance, persistence and write authorization. App cannot choose canonical schema or create a human gate through presentation.

Any rejected recommendation must return its concrete App capability/copy/fixture consequence. These are exact consumer asks to the owning finalization increment, not a second Runtime architecture design.
