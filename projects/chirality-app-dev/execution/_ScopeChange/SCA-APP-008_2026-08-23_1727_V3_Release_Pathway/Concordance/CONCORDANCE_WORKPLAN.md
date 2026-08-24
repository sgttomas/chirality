# Root/App Contract Concordance Workplan — SCA-APP-008

**State:** `CANDIDATE — AWAITING_OWNER_APPROVAL`
**ReadyForNextPhase:** `NO`
**Basis:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Scope:** decision preparation only; this file does not activate or execute a concordance run.

## Purpose and boundary

Before any SCA-APP-008 contract candidate can be accepted as App truth, a later owner-authorized Root/App concordance act must resolve the three questions below against committed, live Root and App authority. HELP_HUMAN may assemble and byte-verify the decision inputs, but every acceptance, cross-loop disposition, and routing authorization remains Ryan Tufts's act under K-AUTH-1.

The accepted Gate-1/Gate-2 assessment remains frozen. Its contract text remains `CONCORDANCE_GATED_CANDIDATE`; this workplan neither selects final wording nor supplies the missing Root value.

## Frozen inputs

| Input | Identity / role |
| --- | --- |
| A2 owner ruling | `plans/steers/chirality_app_v3_app_ruling_record_a2_2026-08-23.md`, SHA-256 `37e6b6d60874ded0727cf65f25aea09cc961bd35b135b5b8eb33c0d20c1f6158`; accepts Gate-1/Gate-2 and authorizes drafting only. |
| Contract candidate | `../Contract_Amendments.proposed.md`, SHA-256 `8a6a799912eb9f610c8e1f6635d7eaf3f90e08614823ab3f715c3006bc0d1485`; proposed rows remain non-binding. |
| App carrier context | `../Carrier_Map.md`, SHA-256 `72a1b55b5307b6df5131011e30581e323737e95f3bcf85471121481ded25b619`; accepted assessment context, not applied carrier truth. |
| Root notice draft | `../DRAFT_NOTICE_TO_ROOT.md`, SHA-256 `8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72`; frozen and unrouted. |
| Current App contract | `projects/chirality-app-dev/docs/CONTRACT.md`; live App truth to be hashed at the future concordance basis. |
| Root truth | The then-live, owner-accepted Root contract, session-store/schema surfaces, invariant inventory, and applied SCA records; exact committed paths and hashes must be frozen by the future activation record rather than inferred from this App candidate. |

## Decision input C-01 — K-EVENT-4 exact live Root session path

**Open question:** What exact committed, versioned Root session-store path is the canonical runtime audit record that K-EVENT-4 must name? This workplan deliberately records no answer.

Required evidence for an owner decision:

1. the exact Root file or contract row that defines the canonical path, with commit, blob SHA-256, and line citation;
2. the literal path bytes, including variable/version notation and whether the subject is a directory, JSON file, or JSONL file;
3. the accepted schema/version identity and the Root writer/ownership invariant that makes the path canonical;
4. evidence that Root's current applied state, not a plan, draft, historical record, or App compatibility path, owns the value;
5. an App-side comparison against the legacy `.chirality/sessions/<id>/events.jsonl` compatibility source so the final text preserves one active writer and non-destructive migration; and
6. an exact proposed K-EVENT-4 post-image regenerated from the owner-selected value, followed by fresh Root/App review.

**Decision owner:** Ryan Tufts, after HELP_HUMAN presents a byte-bound Root/App comparison and each loop confirms the provenance of its own truth.

**PASS output:** an owner-selected exact path identity, bound to its Root source bytes, plus an exact regenerated App K-EVENT-4 candidate that preserves Root ownership, one-writer semantics, projection-only App streaming/replay, and non-destructive legacy migration.

**HOLD output:** `K_EVENT_4_PATH_UNRESOLVED` if no single accepted Root value exists, source identity cannot be reproduced, candidate wording would create dual writers, or Root/App sources disagree. The contract candidate remains unaccepted; no placeholder or inferred path is permitted.

## Decision input C-02 — cross-loop invariant-ID collision

**Open question:** Do any proposed App invariant IDs collide with a live Root or App invariant ID in ownership or meaning?

The comparison set must include existing-row candidates `K-CONTROL-1`, `K-ROLE-2`, `K-NET-1`, `K-KEY-1`, `K-EVENT-3`, `K-EVENT-4`, and `K-EVENT-6`; new-row candidates `K-CONSENT-1` and `K-UNTYPED-1`; and every consequential enforcement-map reference, including `K-SUBAGENT-1/2/3`. Inclusion in this inventory is not acceptance of an ID or its wording.

Required evidence for an owner decision:

1. complete, deterministically extracted invariant-ID inventories from the live Root and App contracts and their accepted coverage/enforcement maps, each bound to commit and file SHA-256;
2. for every duplicate ID, the exact Root and App row bytes, ownership, verification/enforcement mapping, and classification as byte/semantic parity, permitted App specialization, incompatible collision, or stale reference;
3. proof that proposed new IDs are unused in both loops and that existing IDs retain stable meaning rather than being silently repurposed;
4. a reference-integrity scan over the exact proposed Gate-3 carrier and contract package; and
5. an explicit identity map or renaming proposal for every non-parity collision, with affected references and rollback consequences.

**Decision owner:** Ryan Tufts. HELP_HUMAN prepares the cross-loop comparison; the Root and App loops each retain authority over their own contract application.

**PASS output:** a complete collision matrix with no unexplained duplicate and an owner-approved identity disposition for every duplicate: shared parity, allowed App specialization, or exact rename/reference rewrite.

**HOLD output:** `INVARIANT_ID_CONCORDANCE_UNRESOLVED` if either inventory is incomplete, a candidate ID has incompatible live meanings, a proposed new ID is already occupied, or a required reference rewrite is not exact. All affected contract candidates remain unaccepted; no automatic renumbering or semantic merge occurs.

## Decision input C-03 — routing moment for the reciprocal Root notice

**Open question:** At what exact owner-gated moment may the frozen `DRAFT_NOTICE_TO_ROOT.md` be copied into a Root coordination surface, and does the owner authorize that routing in the same act or a separate act? The draft remains unrouted now.

Required evidence for an owner decision:

1. the exact accepted Gate-3/Gate-4 candidate identities and the later Gate-5 application identity, if Gate 5 has occurred;
2. proof of the concordance outcomes for C-01 and C-02 and the final contract-candidate identities they bind;
3. the then-current App `_ScopeChange/_LATEST.md` state and evidence that any pointer move occurred only in a separately authorized Gate-5 act;
4. a byte-exact routed-notice candidate derived from the frozen draft, including the accepted/applied App identities and no stale `assessed, but not yet accepted or applied` claim;
5. the exact proposed Root destination, receiving-loop ownership, and confirmation that the notice is coordination rather than Root authority; and
6. a verbatim owner instruction naming whether routing occurs after Gate-3/Gate-4 approval, after Gate-5 application, or under another explicit sequence, plus the exact bytes and destination authorized.

**Decision owner:** Ryan Tufts. HELP_HUMAN verifies both-loop byte identities and presents the routing alternatives and their sequencing effects; neither loop may infer authorization from acceptance alone.

**PASS output:** an explicit owner routing decision bound to one exact notice candidate, one destination, and one application state. The receiving Root loop may then adopt, amend, or decline under its own instruments.

**HOLD output:** `ROOT_NOTICE_ROUTING_UNAUTHORIZED` if Gate state, concordance state, notice bytes, destination, or owner authorization is ambiguous. `DRAFT_NOTICE_TO_ROOT.md` remains inside the SCA folder and no Root path is written.

## Authorized sequence for a future concordance act

1. Obtain a separate owner activation for the bounded concordance act; this workplan is not activation.
2. Freeze the exact Root and App commits, authority surfaces, invariant inventories, and overlapping work. Material source movement produces `STALE_INPUT` and requires a fresh basis.
3. Extract C-01 and C-02 evidence read-only. Preserve every unknown, mismatch, and ownership distinction; implementation and tests are evidence, not contract authority.
4. Produce one byte-bound decision packet for C-01 and C-02, including exact candidate post-images and HOLD alternatives. Do not edit either loop's contract.
5. Present the packet to Ryan Tufts. Record only the owner's actual path and invariant-ID dispositions; unresolved items keep affected candidates on HOLD.
6. Regenerate the exact Gate-3 contract candidate and its downstream hash plan from the ruled values, then obtain fresh independent Root/App review. Any byte change invalidates prior post-image hashes.
7. Return the concordance result for owner approval. Contract acceptance and later Gate-5 application remain separate acts.
8. Present C-03 at the owner-selected gate. Route only the exact authorized notice bytes to the exact authorized Root destination; otherwise preserve the draft unrouted.

## Explicit non-effects

- No concordance activation record, R0 calibration, corpus inventory, discovery wave, claim ledger, repair tranche, or backcheck is created or run.
- No Root value, invariant disposition, contract wording, or notice timing is accepted by this workplan.
- No existing SCA-APP-008 assessment byte is modified.
- No App or Root contract, invariant register, coverage/enforcement map, SOW, decomposition, dependency, lifecycle, status, pointer, code, docs, frontend, runtime, plan, or foreign-loop surface is modified.
- No notice is routed, and no Root action is requested in this phase.
- No implementation, activation, release, signing, notarization, deployment, distribution, publication, readiness, reliance, or acceptance claim is made.

## Candidate handoff

| State | Value |
| --- | --- |
| `ConcordanceWorkplanState` | `COMPLETE_CANDIDATE_AWAITING_OWNER_APPROVAL` |
| `ActivationState` | `NOT_AUTHORIZED` |
| `ContractCandidateState` | `CONCORDANCE_GATED_CANDIDATE` |
| `NoticeState` | `DRAFT_UNROUTED` |
| `ReadyForNextPhase` | `NO` |
| `NextOwner` | `Ryan Tufts` |
| `NextAction` | Approve, amend, or reject this future concordance workplan; no execution follows without a separate activation act. |
