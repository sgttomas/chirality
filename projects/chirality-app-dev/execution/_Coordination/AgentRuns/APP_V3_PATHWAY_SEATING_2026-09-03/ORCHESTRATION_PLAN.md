# Orchestration Plan — APP_V3_PATHWAY_SEATING_2026-09-03

- **RunID:** `APP_V3_PATHWAY_SEATING_2026-09-03`
- **Plan version:** 1 (frozen before any write)
- **Selection authority:** `HUMAN` — Ryan Tufts' A12 multi-select on 2026-09-03 (transcribed verbatim in `plans/steers/chirality_app_v3_app_ruling_record_a12_2026-09-03.md`)
- **Supervisor:** HELP_HUMAN (Agent 0; Claude Fable 5.1), owner in-session
- **Executor:** one ephemeral Agent 2 generalist (Claude Fable 5.1, `claude-fable-5-1`) under a sealed brief; no delegation; a separate independent reviewer is dispatched by HELP_HUMAN over the resulting PR
- **Descriptive posture:** `TERMINAL_FAN_OUT_IN` with one node chain (N0 → N1 → N2 → N3 → N4) and a concurrent disjoint sibling tranche (A11 E2 concordance, merged as PR #680) that never shared a write path
- **Basis:** branch cut at `1537ddad1f9227dee1ba3233c0146694a779026a` (PR #679 merge); re-based before publication onto `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` (PR #680 merge) at the coordinator's direction. Both are fast-forward descendants of the required `1537ddad1` basis.
- **Working root:** `projects/chirality-app-dev`
- **Accepted upstream truth consumed:** applied decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at content commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f` (SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`); `execution/_ScopeChange/_LATEST.md` SHA-256 `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`; the SCA-APP-008 `Carrier_Map.md`; Root R17 record and steer; A1, A10, A11 records; the pinned plan HTML SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` (completion meaning only)

## Nodes

| Node | Objective | Read scope | Write scope | Return | Fan-in gate |
|---|---|---|---|---|---|
| N0 | Re-derive current state and map every plan WP/gate/AT to its App carrier, Root/external owner, or unseated state; prove containment | repo read-only | this packet (`MAPPING.md`, `COVERAGE_MATRIX.md`, `Evidence/pre_images.json`) | mapping and coverage evidence | packet present; no selection effect |
| N1 | Author the App successor workplan (protocol and pointers only) | as N0 | `loop/WORKPLAN_2026-09-03_app_dev_loop.md` (new) | workplan bytes | bytewise sorts after `WORKPLAN_2026-07-18b_…`; committed-HEAD selector picks it after merge |
| N2 | Seat the carriers: SOW re-basis (19) and decomposition-conformant amendment (4); `Remaining` items; explicit dependency rows only where needed; dependency schema/enum checks and closure audit | as N0 | the 19 carriers' `ScopeOfWork.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv` | pre/post identities (`SOW_IDENTITY_LEDGER.md`), `DEPENDENCY_REFRESH.md`, `Evidence/dep_closure/**` | all SOWs validate; schema/enum PASS; closure audit produced |
| N3 | Bind evidence contracts to every empirical/fixture/gate-evidence item | as N0 | folded into N2's `_STATUS.md` items and the workplan Evidence contract | — | every such item cites the contract |
| N4 | Validate, prove no gate/lifecycle/host/Root/release change, write A12 record, handoff, receipt, manifest; commit, push, open one unmerged PR | as N0 | `plans/steers/…a12…md`, `loop/LOOP_RECEIPTS.md` (append), this packet | `VALIDATION_EVIDENCE.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256` | checks pass; PR open and unmerged |

## Human decision points

- Owner byte review and merge of the candidate PR (confers selectability only).
- Every `SCOPE_AMENDMENT_REQUIRED` obligation (later SCOPE_CHANGE act).
- Every `NOT_SELECTABLE_UNTIL` gate or act named in the seated items.

## Constraints carried

Sealed write set (nothing else may change); no `docs/**`, `_REFERENCES.md`, corpus, `frontend/**`, register, decision, prior receipt, plan HTML, prior steer, Root surface, or SCA snapshot write; no implementation, lifecycle, host mutation, signing, release, publication, reliance, or Root act; never linearize an objective-relative cycle; conservative containment (unseated rather than invented).
