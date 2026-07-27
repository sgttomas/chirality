# Decision Log

| Date | Gate | Actor | Decision | State |
|---|---:|---|---|---|
| 2026-07-26 | Intake | Ryan Tufts | Human-initiated OD-5 App boundary correction after adoption of OD-2 Option A. | `RECORDED` |
| 2026-07-26 | 1 | SCOPE_CHANGE | Parsed five direct MODIFY actions, one conditional trace MODIFY, and two required change-register ADD actions; verified all affected IDs and captured the pre-change baseline. | `PENDING_OWNER_CONFIRMATION` |
| 2026-07-26 | 1 | Read-only Agent 2 adversary | Confirmed the direct-contradiction set, moved related rows to explicit Gate-2 classification, and required DEC-019 to remain unchanged while the new decision/change entries became separate ADD actions. | `CORRECTION_APPLIED` |
| 2026-07-27 | Basis | SCOPE_CHANGE | Fast-forwarded the isolated branch from `0f8349d90` to current accepted `main@fb16e32ed`; the App decomposition remained byte-identical and the frozen Gate-1 intake was preserved through `Gate_1_Basis_Update.md`. | `CURRENT_BASIS_VERIFIED` |
| 2026-07-27 | 1 | Ryan Tufts | “I CONFIRM SCA-APP-005 GATE 1 and permit you to pass through the subsequent gates too until you complete that scope change.” | `CONFIRMED_WITH_STANDING_GATES_2_TO_5_APPROVAL_INSIDE_ENVELOPE` |
| 2026-07-27 | 2 | Read-only Agent 2 source-concordance adversary | Re-verified the Root-owner/App-client boundary and found two omitted mapped deliverables: `DEL-05-01` carries SOW-009 but assigns canonical session storage to App; `DEL-05-02` carries SOW-015 but assigns generic runtime event persistence to App. | `CONSEQUENTIAL_VARIANCE_FOUND` |
| 2026-07-27 | 2 | SCOPE_CHANGE | Classified `DEL-09-03` as mapping-only `NO_CHANGE`, accepted all original linked-row dispositions, and stopped before Gate 3 because adding `DEL-05-01`, `DEL-05-02`, and two `_CONTEXT.md` writes expands the confirmed entity/write set. | `AWAITING_OWNER_VARIANCE_RULING` |
| 2026-07-27 | 2 | Ryan Tufts | “I Approve the SCA-APP-005 expansion for DEL-05-01, DEL-05-02, and their _CONTEXT.md metadata.” | `EXPANSION_APPROVED` |
| 2026-07-27 | 2 | SCOPE_CHANGE | Accepted the impact assessment with the approved expansion; preserved all IDs, packages, types, mappings, envelopes, lifecycle states, and explicit exclusions. | `GATE_2_ACCEPTED` |
| 2026-07-27 | 3 | Read-only Agent 2 adversary | Found the owner-expanded DEL-05-02 amendment still contradicted by unamended SOW-014/SOW-039, PKG-05 package scope, and repeated PKG-05 context metadata. | `CONSEQUENTIAL_VARIANCE_FOUND` |
| 2026-07-27 | 3 | SCOPE_CHANGE | Held the exact amendment before application and bounded the minimum additional set to SOW-014, SOW-039, PKG-05, and PKG-05 package-scope parity across five contexts; DEL-05-03/04/05 deliverable rows remain unchanged. | `AWAITING_OWNER_VARIANCE_RULING` |
| 2026-07-27 | 2/3 reopen | SCOPE_CHANGE | Reopened read-only impact analysis after the narrow preview proved non-exhaustive across D-GOV-20's eight daemon-owned seams; the old preview is superseded and no authoritative write occurred. | `EXHAUSTIVE_REVIEW_OPENED` |
| 2026-07-27 | 2/3 reopen | Fresh read-only Agent 2 | Enumerated every direct `MODIFY` and `NO_CHANGE` disposition across engines, credentials, sessions, delegation, tools, turn locks, interruption, and model residency; identified 29 SOW rows, 5 packages, 15 deliverables, 5 objectives, 25 contexts, and U1–U5. | `MATRIX_RETURNED` |
| 2026-07-27 | 2/3 reopen | Independent adversarial backcheck | Confirmed the exhaustive matrix and corrected the earlier narrow disposition of SOW-054/SOW-056 to `NO_CHANGE`; no additional entity was found. | `BACKCHECK_PASS` |
| 2026-07-27 | 2/3 reopen | Fresh independent backcheck | Rejected the first exhaustive matrix as incomplete: `SOW-056`, `SOW-062`, `DEL-05-03`, and `DEL-06-05` require direct boundary qualification; blanket cross-cutting ranges and notice deferral were also corrected. | `BOUNDED_CORRECTIONS_REQUIRED` |
| 2026-07-27 | 2/3 reopen | SCOPE_CHANGE | Issued Revision 2 with 31 SOW modifications, 17 deliverable modifications, exact row-level cross-cutting dispositions, the complete PKG-07/08/09 no-change inventory, and Root/Tier-0/PEC notices as coordination outputs. | `REVISION_2_ISSUED` |
| 2026-07-27 | 2/3 reopen | Adversarial reconciliation | Reconciled both backchecks directly against D-GOV-20 and the accepted App rows; confirmed Revision 2, including `SOW-054` no-change, acceptance row 544 no-change, `SessionRecord` modify, and `Explicit Deny Precedence` no-change. | `REVISION_2_BACKCHECK_PASS` |
| 2026-07-27 | 2/3 reopen | Ryan Tufts | “I Approve the corrected SCA-APP-005 Revision 2 envelope.” Provenance: in-session owner ruling, 2026-07-27. | `REVISION_2_APPROVED` |
| 2026-07-27 | 3 | SCOPE_CHANGE | Regenerated the exact amendment against Revision 2 and ran the deterministic D-GOV-20/entity/context concordance. | `APPROVED_AND_PASS` |
| 2026-07-27 | 4 | SCOPE_CHANGE | Applied the approved propagation set: authoritative decomposition, 25 contexts, SCA/audit pointers, and Root/Tier-0/PEC coordination-only notices; all deferred surfaces remain excluded. | `APPROVED_AND_APPLIED` |
| 2026-07-27 | 5 | SCOPE_CHANGE | Applied only the approved bounded amendment. No contract, pin, implementation, PRD, D-APP-48/49, APP-HOLD, parity, Piping, lifecycle, mapping, envelope, or dependency state changed. | `APPLIED_PENDING_POSTCHANGE_AUDIT` |
| 2026-07-27 | 5 | AUDIT_DECOMP | Post-change snapshot found 10/10 packages, 51/51 deliverables, 51/51 contexts, 51/51 valid SOW_V1 contracts, 78 valid ledger rows, 10/10 objectives, 0 blockers, 55 warnings, and 2 info findings. | `WARNINGS_NO_BLOCKER` |
| 2026-07-27 | 5 | SCOPE_CHANGE | Closed SCA-APP-005 for scope change only; updated the SCA pointer, preserved all deferred work, and returned the bounded tranche to CHANGE. | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |
| 2026-07-27 | 5 | AUDIT_DECOMP closure backcheck | Verified both pointers, required artifact completeness, fixed state fields, audit-count parity, supersession-map hash, closure consistency, and `git diff --check`. | `PASS` |

The standing approval applies only while the exact impact, amendment, and
propagation remain within the confirmed envelope. The exhaustive matrix is a
consequential expansion and therefore returns once as a complete owner ruling,
rather than being absorbed serially. No accepted App
decomposition, pointer, contract, lifecycle, product, runtime, Tier-0, PEC, or
Piping surface had changed when Gate 1 closed.
