# PEC Task Management notice triage — 2026-09-23

**Invocation:** Brief D1 (`AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/D1_TM_NOTICE_TRIAGE.md`) under D-PEC-86 §3 I-6 and D-PEC-73 Option A (on-demand invocation). TASK (Type 2) executed `Workflow: chirality-root:bundled:workflow:task-management` in bounded-intake mode for the three 2026-09-23 Root notices, with no delegation. This record makes recommendations only. It changes no PEC product, SOW, SPEC, decision register, lifecycle, source, release or reliance state. It creates no Action Item, promotion, disposition or foreign assignment.

**Basis:** `HEAD d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` plus the uncommitted HELP_HUMAN run files for D-PEC-86. Context origins and SHA-256:

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| PEC `AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/task-management/WORKFLOW.md` | `db06263d41f2a17e12b965a337dd6ba0baf3bd21c71ed6e5dc0de7997e101e9b` |
| `workflows/task-management/resources/contract.md` | `e1c97a76b8a411873ca86a6ef4351a7f76303e74331a52307a3705a83827c837` |
| `workflows/task-management/resources/method.md` | `7f9e0d5ea7c2b74e7148faf3d2a35efc6ddd0552efd4b577a1c56895f75fe2f8` |
| D-PEC-86 record | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |
| D-PEC-73 record | `2717ba9f6d2c0baeb8ac2096e4657745d683a79731af4db88dc93d5eaea4a89e` |
| Brief D1 | `17763a0fe524ac3c7d72e3aadeea0f93ec9bb006e7f13ce14cabea03caac8a46` |
| `tools/taskmgmt/taskmgmt.py` | `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101` |

The Root `AGENTS.md` and workflow `WORKFLOW.md`/`contract.md` hashes differ from those in `REGISTER_REVIEW_2026-09-22.md`. That is consistent with the Root tranches these notices announce. The 2026-09-22 hashes are context-origin records, not PEC pins; no PEC file pins either value.

## Federation preflight and scan

- `taskmgmt federation` result: `COMPLETE`, covering four canonical tracked registers and their archives (ROOT, APP, PIP, PEC). It reported 27 typed findings (1 `REMOTE_CLOSED_LOCAL_OPEN`, 22 `LOCAL_CLOSED_REMOTE_OPEN`, 4 `MISSING_NOTICE`), none involving a `TM-PEC` row, and no presented findings. The run made zero register writes, every register hash matched, and there were no operational errors. PEC counts: OPEN=9, DEFERRED=1, archived=15. Declared exclusions: untracked lookalikes, unsanctioned shapes, archives/exports/fixtures/projections, Notes prose, foreign-register writes and all disposition effects.
- `taskmgmt scan` result: `COMPLETE`, with 481 derived candidates across all scan roots. The only PEC candidates for this intake are the three notices, each classed `notice-not-in-ledger` with `known_to_register: false`. No tracked register (Root, App, Piping or PEC) cites these notices or their tranche IDs. The remaining candidates are outside this bounded intake and were not triaged (contract: no widening into a general harvest). Classes not implemented in the scan (run-record markers, review-report sections, per-document token mode) are named in the helper output.
- Both projections were written only to the session scratchpad outside the repository. No projection is tracked or relied on as authority.

## Triage

The shared-method changes these notices announce are the subject of SCA-005 (D-PEC-86 I-1), whose input is the drift between PEC's feed model and the App/Piping loops' current receipt, work-graph and LOOP_INIT shape. The PEC loop's own possible migration to the shared method is deferred by D-PEC-86 I-7 until SCA-005 closes and a later owner ruling. **No register row adopts, repins or schedules adoption of any shared-method change.**

| Notice (SourceRef) | SHA-256 | Recommendation | One-line justification |
|---|---|---|---|
| `projects/pec/execution/_Coordination/NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md` | `8e7170aee2c40ddd0f0be5b72f934d3af3fcdc158a1dc0a4d28a9f4f25850a71` | No row | The notice and its manifest (`ROOT-APP-PIPING-CENTRAL-RECEIPTS-20260923`, `e56dd83654b35875933a869f3d6ba9494ad10fa110c521f17a632f7aa38a40be`) state that PEC's loop, receipts and Remaining-based selection are unchanged and that adoption belongs to the PEC loop. The feed-model consequence is carried by SCA-005 (I-1), and the adoption decision is preserved by D-PEC-86 I-7 and its reserved "rule when PEC adopts the shared loop method". |
| `projects/pec/execution/_Coordination/NOTICE_2026-09-23_EVERGREEN_LOOP_INSTRUCTIONS.md` | `cc62933dd294c31cefa1c2abd5d36a742f5e67d48b9bcac6883dfd34baf95e5b` | No row | The manifest (`ROOT-EVERGREEN-DEVELOPMENT-LOOPS-20260923`, `bfe305e9461d228d171d5e66102f8dd2ba36f85570aa2fab13bdd6d430e5147f`) places PEC's loop and work selection outside the correction. PEC's `LOOP_INIT.md` and `AGENTS.md` pin neither the changed Root `AGENTS.md`, SPEC §9.8 nor `construct-local-work-graph`. The App/Piping LOOP_INIT shape change is SCA-005 feed-model input (I-1), and any PEC LOOP_INIT change is the I-7 deferral. |
| `projects/pec/execution/_Coordination/NOTICE_2026-09-23_SCOPED_PR_CI.md` | `26d763192e88432afb1d996ec99791591b7d72cb94ecb3dcac2acaf16db6f744` | No row | `docs/CI_SELECTION.md` (`563f0037a1c4dd91ffc787c7dd74600f33641a8d46a46afc201c607b1628f0c0`) routes PEC source, tests, fixtures and configuration to PEC workspace tests. Records-only PRs get the governance harness with an explicit not-applicable product result, and full coverage is available through `gh workflow run pec-tests.yml`. No PEC loop, AGENTS or decision surface pins the prior every-PR routing, and the notice keeps PEC's local check profile, evidence obligations and loop unchanged. No allocation gap exists: the effect is visible in ordinary PR evidence. |

**Eligibility basis** (`contract.md`, "Eligibility for development-loop intake"): each notice declares that it performs no PEC act. Every PEC consequence found has an identified home: SCA-005 (I-1), the D-PEC-86 I-7 deferral with its reserved owner ruling, or ordinary PR practice. The condition "no identified successor undertaking or receiving owner already carrying it" therefore fails for all three, and no missing allocation, decision or precursor remains for the register to hold. No existing TM-PEC row covers these notices. TM-PEC-001 (D-GOV-31 merge policy) concerns a different notice and is unaffected.

**Alternative for the owner, not minted:** if register visibility of the I-7 deferral is wanted, the only candidate is one `DEFERRED` row, "PEC loop adoption of the 2026-09-23 shared-method changes". It would cite the first two notices, use the trigger "SCA-005 checkpoint 3 accepted (SCA-005 closed)", and name D-PEC-86 I-7 in Notes. The next free ID is **TM-PEC-026**; the highest existing ID across `REGISTER.csv` and `REGISTER_CLOSED.csv` is TM-PEC-025. This record does not recommend it, because it would duplicate a decision record that already carries the deferral.

## Write-boundary observation

Brief D1 opens additive rows in `REGISTER.csv`. The selected method's contract says "TASK never writes register rows" and makes promotion and disposition human acts, with WORKING_ITEMS applying the recorded decision. Under Root `AGENTS.md`, the effective boundary is the intersection of the brief and the method restrictions. The no-row recommendation makes the conflict moot for this run: no register row was written. If the owner or HELP_HUMAN rules that a row should be minted after all, a manager should apply that decision as the recorded human act, rather than a TASK.

## Commands and exit codes (run from repository root)

| Command | Result | Exit |
|---|---|---|
| `python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` (before) | PASS, 10 rows | 0 |
| `python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` (before) | PASS, 15 rows | 0 |
| `python3 tools/taskmgmt/taskmgmt.py federation --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv --out <scratchpad>/pec-federation-2026-09-23.json` | COMPLETE, 4 registers, 27 findings, 0 presented, 0 writes | 0 |
| `python3 tools/taskmgmt/taskmgmt.py scan --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv --out <scratchpad>/pec-scan-2026-09-23.json` | COMPLETE, 481 candidates | 0 |
| `python3 projects/pec/execution/_Scripts/pec_reliance_hold.py --register projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <REGISTER.csv and this file> --operation candidate-validation` | ALLOW ×2 (hold register has no rows) | 0 |
| `validate` on both registers (after) | PASS, 10 rows and PASS, 15 rows; both registers byte-identical | 0 |

Register SHA-256 before and after (unchanged): `REGISTER.csv` `d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d`; `REGISTER_CLOSED.csv` `ea730ae06f0805c720bbb29aed6d681c323e6d3b0c4a38d53db27e1075fafd94`.

## Outstanding

- The owner or HELP_HUMAN reviews these recommendations (D-PEC-86 I-6: "None beyond ordinary review"). Accepting them needs no register edit. The optional TM-PEC-026 `DEFERRED` alternative stays unminted unless it is actually decided.
- The I-7 ruling on when PEC adopts the shared loop method remains with the owner after SCA-005 closes.
