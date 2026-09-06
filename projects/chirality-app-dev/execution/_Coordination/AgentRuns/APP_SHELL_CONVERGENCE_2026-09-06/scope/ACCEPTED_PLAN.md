# Conversation evidence

The following is the full preceding plan as presented. It is preserved as conversation evidence, not a new standing queue. After this plan the user said, verbatim: **Implement the proposed plan.**

<proposed_plan>
# Agent 0 plan: deliver the shell redesign as a coherent experience

## 1. Objective and starting point

Make the running application recognizably match the approved shell mock in both appearance and interaction, while preserving the functional foundations already merged.

The next milestone is **a coherent shell that we can inspect together**. Subsequent milestones complete the richer workflows and document/chat interactions that motivated the redesign.

At execution start, CHANGE establishes a fresh branch from verified current main. WORKING_ITEMS reconciles the merged implementation with deliverable `Remaining` items and dependency evidence, including the runtime workspace migration. Completed state fields, workflow parsing, file containment, and document handling are reused.

The mock and accepted target specification define the design; live deliverables and owner rulings define executable scope. This conversational plan creates no additional standing work queue.

## 2. Ownership and decisions

I remain responsible for alignment, ordering, cross-package coordination, and rejecting results that pass technical checks but miss the intended experience.

| Owner | Responsibility |
|---|---|
| PKG-02 WORKING_ITEMS | Integrate the shell, navigation, composer, right panel, and activity experience |
| Other package WORKING_ITEMS managers | Deliver their bounded workflow, session, runtime-consumption, and packaging obligations when prerequisites permit |
| SCOPE_CHANGE | Process necessary scope amendments through existing instruments |
| Independent reviewers | Assess the frozen source and compare the actual UI against the approved design |
| CHANGE | Commit, push, and prepare the validated PR |

Assign **one integration owner for shared shell components and CSS**. Parallel work must have disjoint write targets; managers return coordination through Agent 0.

Resolve the existing decisions separately:

- **D120 presentation scope:** recommend A1, authorizing the omitted shell/activity integration files. This is required for the complete structural pass.
- **D120 no-folder behavior:** recommend B1, preserving the truthful current restriction while routing the missing contract design to Root.
- **D121 inline PDF:** pursue the bounded security amendment and native proof through its owning gate. External opening remains partial behavior until then.

These are recommendations, not recorded rulings. Pending runtime or PDF decisions do not hold independent presentation work.

## 3. Delivery sequence

### Milestone 1 — The recognizable shell

Integrate the authorized T2, T3 composition corrections, and T5 work in dependency-valid iterations:

- Remove the active shell header, duplicate headings, and legacy toolbar. Apply Stone tokens, restrained typography, plain labels, and the white/lightest centre.
- Make the left panel chat-focused, with one wordmark and reachable settings. Remove its duplicate file tree.
- Create the compact composer with attachments inside and the context line below. Preserve streaming guards and existing session ownership.
- Give the right panel one control row and the document viewer one clear title/control hierarchy.
- Replace the resizable activity shelf with the fixed **32px strip**. Open details in the right-panel Activity view once its host prerequisite is verified.
- Apply the specified pane defaults and bounds: left 240px, maximum 360px; centre minimum 420px; Files default 300px. Preserve compatible saved-state readers.

For the D120 integration, retain reconnect/settings state and handlers in ShellFrame and pass their controls through the proposed presentation slots. Keep the primary ChatPanel mounted once throughout navigation and panel changes.

**Checkpoint:** show actual application/mock comparisons before expanding into the next feature milestone.

### Milestone 2 — Complete the everyday interactions

After the relevant predecessor gates are satisfied:

- Add chat search, titles, pins, groups, archive, and folder-per-chat behavior.
- Complete account/popover/Settings presentation using the authorized integration state.
- Add document reference chips, Ask, Attach, and quote composition.
- Resolve the distinction between continuing an owned chat in the centre and viewing a child session as read-only replay on the right.

Do not silently treat partial T3 completion as satisfying every downstream gate. Assess each existing criterion; route an amendment where the recorded dependency genuinely prevents independent progress.

### Milestone 3 — Complete the workflow experience

Connect the already implemented workflow contract to the Workflows view, library, creation/binding forms, roadmap, specification/rung controls, and proposal cards.

Activate the owning packages for instruction, delegation, and live-event integration only against accepted contracts. Fixture-backed presentation and live execution receive separate completion claims.

Finish the approved icon and packaging work under their existing gates. Pop-out windows remain deferred.

## 4. Acceptance and visible progress

Use two distinct acceptance judgments: **design fidelity** and **functional correctness**. Neither substitutes for the other.

At each meaningful UI checkpoint:

- Compare populated chat, Files, document, expanded-panel, and replay states at 1440px and 960px in both themes; check narrower context-line wrapping.
- Inspect typography, spacing, hierarchy, duplicate controls, panel geometry, and the fixed activity strip against the approved reference.
- Exercise keyboard/focus behavior, reconnect, settings access, streaming, resize/restore, and persistence.
- Confirm that panel operations preserve the primary conversation, composer draft, and session identity.

After the source is frozen, require fresh independent review over the complete diff, registered tests/typecheck/build/premerge checks, browser evidence, and applicable native/security checks. Frontend changes carry the required login-proof restaging consequence.

Show the user concise comparisons and clearly distinguish **implemented**, **verified**, and **blocked** behavior.

## 5. Closeout and completion rule

Managers update the existing deliverable records and return evidence, remaining obligations, and dependency dispositions. I validate the combined experience and resolve contradictory claims before CHANGE publishes it.

Continue through lawful follow-on work rather than stopping at the first blocked feature. At the run’s permitted closeout, prepare a PR describing the actual resulting experience and explicit residuals.

The previous PR’s merge authorization applied to that PR; this plan assumes no automatic merge authority for a future PR.

The redesign is complete only when its accepted visual and interaction requirements are verified or explicitly deferred by the owner. A green CI run alone does not establish that outcome.
</proposed_plan>
