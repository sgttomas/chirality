# Candidate Harvest Report — Chirality App Dev — 2026-08-02

Mode: `candidate harvest`

Authority: decision support only. This report promotes, prioritizes, disposes,
closes, or elevates nothing. The owner rules every register mutation.

Register home:
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/`

## 1. Federation preflight

The mandatory read-only federation preflight completed with coverage
`COMPLETE`. Four canonical Git-tracked registers were discovered, read, and
validated; no lookalike was included, no path was excluded by discovery, and
no register byte changed.

| Register | Rows | SHA-256 | Validation |
|---|---:|---|---|
| `_DomainEngines/pec/_TaskManagement/REGISTER.csv` | 6 | `85b8e0a66975ffa44fec6db8597940ff2d87f61e8bd09316d1ea0e1d874a9c91` | PASS |
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | 103 | `79bb9b166b63e1faa6364e33bf141512eed0fad2b3bb700fe26c90bdccfe98b5` | PASS |
| `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv` | 24 | `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` | PASS |
| `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv` | 24 | `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` | PASS |

Typed-field findings were 24 expected App-to-Root linked-row references and one
program-integrity observation: Root row `TM-ROOT-053` is open while linked
Piping row `TM-PIP-023` is closed. The latter is disclosed but is not an App
promotion candidate because neither row belongs to the invoking App register.

Derived projection:
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/.candidates/federation.json`
(gitignored, rebuildable, never authority).

## 2. Sweep coverage

The deterministic v0 scan was used as a first pass, then completed manually
for App-local classes the tool does not yet implement and for canonical-copy
dedup defects caused by same-named `HANDOFF_STATE.md` files.

| PRD §5.1 surface | App-local coverage | Result |
|---|---|---|
| Decision register non-ruled rows | 1 register | 0 candidates; every row is `RULED` |
| Notices vs ledgers | 20 local notices; all canonical ledgers surveyed program-wide | 9 notices absent from every ledger |
| Evaluation `FINDINGS.csv` | 14 files | 40 rows whose source status is not one of the scanner's closed tokens |
| `Review_Findings.csv` | 0 files | No source |
| HOLD registers | live register plus one proposal copy | Live register is header-only; 0 open rows |
| Handoff blockers / coverage gaps | 14 tracked `HANDOFF_STATE.md` files | 10 file-level current/stale handoff candidates; terminal no-blocker files omitted |
| `Open_Questions.csv`, `Amendment_Candidates.csv`, `Conflicts.csv` | 0 files | No source |
| `*TBD_Register.csv` | 0 files | No source |
| New review reports | `plans/chirality_app_dev_maturity_survey_2026-08-01.html` rechecked against current bytes | 5 candidate observations; numeric/`Remaining` claims not relied upon |
| Receipt parked lanes | 1 historical `Parked lanes:` field | 1 stale lane candidate |
| Explicit markers | 555 tracked `_run_records` plus governed App control/SCA returns | 0 run-record signatures; 2 semantic marker candidates after folding one duplicate marker pair |

Total presented: 67 candidates. Ten are proposed for new promotion; one is
proposed for disposition against an existing App row; two existing App rows
are proposed to remain unchanged; the rest are closure-echo, duplicate,
informational, superseded, or OBE observations.

The App next-work slate and deliverable `## Remaining` sections were examined
only to prevent false promotion. They remain fenced work-discovery surfaces
under the TASK_MANAGEMENT non-negotiable rule and are not harvested as Action
Items. The parity concern is included only because it is independently present
in the review report and already has register row `TM-APP-002`.

The six D-APP-81 clause-6 `HISTORICAL_RELATION_UNKNOWN` relations were verified
as preservation state and are not candidates. No byte or classification in
that population is changed or proposed for change.

## 3. Candidates from notices absent from every ledger

### CH-N01 — AUDIT_GOVERNANCE stale-reference repair

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_AUDIT_GOVERNANCE_STALE_DBM_REFERENCE_REPAIR.md`
- SourceSha: `28222953e38ebafbdb6aef85229a4823e7bba3e034c4c5bd5f0afc852cb7dfa0`
- Concern: The notice is absent from every ledger, but its stated instruction SHA matches live `AGENT_AUDIT_GOVERNANCE.md` and no App-local mirror of the retired Pass-5b title was found.
- Domain lenses: `Checking; Decisions`
- Proposed disposition: `INFORMATIONAL_NO_ACTION`

### CH-N02 — product-delivery direction

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`
- SourceSha: `3231f46463e5a9d2b93793ae39b3b78a041878220932b369d76a976601090cb3`
- Concern: The App loop has not yet ruled how its UI, packaging, and runtime-contract planning will serve both the standalone desktop target and the per-domain control-plane skin described by Root owner intent.
- Domain lenses: `Deliverables; Work; Planning; Approval; Decisions`
- Proposed disposition: `RESOLVED_BY_DECISION` after an App-owned adoption/amend/decline/defer ruling; **promotion proposed**.

### CH-N03 — Root governance-document simplification

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_GOVERNANCE_DOC_SIMPLIFICATION.md`
- SourceSha: `d1500dd428f42431dd19b638f3f0bbc0e75834ce7d721b6d9ba9ca8cb6424525`
- Concern: The notice is absent from every ledger, but its owner-ruled App pin removal is present in packaging, integrity verification, tests, and the Root workflow, while remaining PRD/SPEC mentions are conditional on the integrity policy.
- Domain lenses: `Deliverables; Checking; Decisions`
- Proposed disposition: `INFORMATIONAL_NO_ACTION`

### CH-N04 — Root harness-scope correction

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_HARNESS_SCOPE_CORRECTION.md`
- SourceSha: `f6923e7335f76fc413dd56d5735f0299c31bbf83187bce1b660bfb23ae007a11`
- Concern: The deleted Root-wide Bash-serialization wording survives in App history only as an explicitly former, undefined marker, while the App-owned managed-delegation policy remains independently governed.
- Domain lenses: `Work; Approval; Checking; Decisions`
- Proposed disposition: `INFORMATIONAL_NO_ACTION`

### CH-N05 — Task Management federation preflight

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_FEDERATION_PREFLIGHT.md`
- SourceSha: `b82bb366f15007369bb5fa0ffaf31c05e3c8822b42b2f7576eb93bee2c94ef99`
- Concern: The notice is absent from every ledger, but the published TASK_MANAGEMENT instruction has the notice's candidate SHA and this invocation successfully exercised the required preflight without identifying an App mirror to repin.
- Domain lenses: `Checking; Decisions`
- Proposed disposition: `INFORMATIONAL_NO_ACTION`

### CH-N06 — Task Management instruction-schema repair

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_INSTRUCTION_SCHEMA_REPAIR.md`
- SourceSha: `6f6bd502dc11bb9f365afa585b837f6fadc0eb34fde78725157cedcf5cac2422`
- Concern: The schema-repair notice's instruction SHA has been superseded by the later federation-preflight instruction SHA, and no App-local active pin to either historical value was found.
- Domain lenses: `Checking; Decisions`
- Proposed disposition: `OBE`

### CH-N07 — TASK_MANAGEMENT agent-index addition

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_AGENT_INDEX_TASK_MANAGEMENT_2026-07-31.md`
- SourceSha: `993829fea4f840253e0474076d0ad980c3b4411f3e0bbd0f6064ef8c666f722d`
- Concern: The notice remains unledgered even though D-APP-83 already adopted Task Management for this loop and minted its App register.
- Domain lenses: `Approval; Decisions`
- Proposed disposition: `RESOLVED_BY_DECISION` citing D-APP-83.

### CH-N08 — D-GOV-31 merge-gate succession

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md`
- SourceSha: `8f8d064d0bc464321668c424d58975f90ad0ba80268178f4796573a99fcad0fc`
- Concern: No App decision explicitly adopts, acknowledges, amends, declines, or defers the shared merge-gate succession, so the notice says the stricter local discipline remains controlling despite later practice following the shared pattern.
- Domain lenses: `Approval; Checking; Decisions`
- Proposed disposition: `RESOLVED_BY_DECISION`; **promotion proposed**.

### CH-N09 — D-GOV-32 Task Management standard

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-32_TASK_MANAGEMENT_STANDARD.md`
- SourceSha: `a42ed6f849cb620a70e66162366d606f9e47f2133a000106342d10c1d32f785b`
- Concern: The notice remains unledgered even though its requested App Stage-B adoption ruling was completed by D-APP-83.
- Domain lenses: `Approval; Decisions`
- Proposed disposition: `RESOLVED_BY_DECISION` citing D-APP-83.

## 4. Candidates from evaluation findings

Each row below is a distinct structured source row. “Promotion proposed” means
the concern remains current enough to merit an App register row or ruled
consolidation; all other rows are closure-echo or informational candidates.

### Source E1 — App runtime and basis evaluation

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/FINDINGS.csv`

SourceSha for every E1 row:
`dcfd8289ec78e31c933993e460deaca00ad3a69e536a3646479ed7c334da7ed8`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E01 / `FindingID=OD6-001` | The six unresolvable historical SOW bases still read active-held in the source although D-APP-78/80/81 established, repinned, and released the current accepted population. | Deliverables; Approval; Checking; Decisions | `RESOLVED_BY_DECISION` |
| CH-E02 / `FindingID=OD6-002` | The source's historical-vs-current decomposition observation was consumed by the terminal-basis and concordance sequence. | Deliverables; Checking; Decisions | `RESOLVED_BY_DECISION` |
| CH-E03 / `FindingID=OD6-003` | The missing consolidated current-byte SOW acceptance binding was supplied by the accepted basis/concordance artifacts and complete repin sequence. | Deliverables; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E04 / `FindingID=OD6-004` | The planned-but-absent invariant register was added and accepted by SCA-APP-006. | Deliverables; Approval; Checking | `SUPERSEDED_BY_SCOPE_CHANGE` (`SCA-APP-006`) |
| CH-E05 / `FindingID=OD6-005` | The PKG-00 controls remain intentionally outside the decomposition-derived repin population and require no corrective act. | Deliverables; Checking | `INFORMATIONAL_NO_ACTION` |
| CH-E06 / `FindingID=OD6-006` | The missing SOW-064 traces and obligation partition were added to DEL-06-02/03 by SCA-APP-006 and propagated into current contracts. | Deliverables; Approval; Checking | `SUPERSEDED_BY_SCOPE_CHANGE` (`SCA-APP-006`) |
| CH-E07 / `FindingID=OD6-007` | The D-APP-48 source-identity conflict is still material but has a newer, narrower current-location finding in D49-004. | Deliverables; Approval; Decisions | `OBE` in favor of CH-E33/D49-004 |
| CH-E08 / `FindingID=OD6-008` | The historical-only observation boundary of the D-APP-48 pull validator remains true and is already bounded by later rulings. | Checking; Decisions | `INFORMATIONAL_NO_ACTION` |
| CH-E09 / `FindingID=OD6-009` | Piping's stale synchronized-consumption reliance was routed and retired as current effect by Piping SCA-008. | Approval; Checking; Decisions | `SUPERSEDED_BY_SCOPE_CHANGE` (`SCA-008`) |
| CH-E10 / `FindingID=OD6-010` | The byte-identical D-APP-49 migration is accepted provenance rather than an unresolved action. | Deliverables; Checking | `INFORMATIONAL_NO_ACTION` |
| CH-E11 / `FindingID=OD6-011` | D-APP-76 admitted the current-location executable audit and explicitly closed this named evidence gap. | Checking; Approval; Decisions | `RESOLVED_BY_DECISION` |
| CH-E12 / `FindingID=OD6-012` | Root/App/PEC still lack a ruled cross-version negotiation and incompatibility policy for the shared runtime API. | Deliverables; Planning; Approval; Checking; Decisions | `RESOLVED_BY_DECISION`; **promotion proposed**, with Root route only after ruling |
| CH-E13 / `FindingID=OD6-013` | The generic degraded-mode contract remains incomplete beyond bounded daemon-unavailable fail-closed behavior. | Deliverables; Planning; Approval; Checking; Decisions | `RESOLVED_BY_DECISION`; **promotion proposed**, with Root route only after ruling |
| CH-E14 / `FindingID=OD6-014` | The consumer-topology census is informational and correctly bounds Piping as a non-client. | Checking | `INFORMATIONAL_NO_ACTION` |
| CH-E15 / `FindingID=OD6-015` | A governed live PEC consumption proof for the shared daemon remains absent. | Deliverables; Work; Checking; Decisions | `RESOLVED_WITH_CHANGE`; **promotion proposed**, with PEC/Root route only after ruling |
| CH-E16 / `FindingID=OD6-016` | The stale D-APP-75 effective-state label was cured by its additive effective-state closeout. | Checking; Decisions | `RESOLVED_WITH_CHANGE` |
| CH-E17 / `FindingID=OD6-017` | The daemon/helper shared Electron bundle identity remains a current owner-choice residual despite recovery evidence. | Deliverables; Planning; Approval; Decisions | `RESOLVED_BY_DECISION`; **promotion proposed** |

### Source E2 — CQF1 initial evaluation

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/CQF1_CONCORDANCE_57652BA1_2026-07-20/FINDINGS.csv`

SourceSha for every E2 row:
`ea9d926613b2b753a7e3552d028f1628bd1ed809dabe3302ac0f85558c74010c`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E18 / `FindingID=V1-001` | The initial technical-boundary omission was repaired and sustained by later CQF1 rechecks. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E19 / `FindingID=V1-002` | The false replay-consumer claim was corrected and sustained by later CQF1 rechecks. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E20 / `FindingID=V1-003` | The unsupported ANSI affinity was corrected and sustained by later CQF1 rechecks. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E21 / `FindingID=V1-004` | The false terminal-LF/whitespace QA pass was repaired and independently rechecked. | Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E22 / `FindingID=V1-005` | The old fixed caller-count comment is no longer present in the live helper source. | Work; Checking | `RESOLVED_WITH_CHANGE` |

### Source E3 — CQF1 repair recheck

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/CQF1_CONCORDANCE_57652BA1_2026-07-20/RECHECK_R1_REPAIR/FINDINGS.csv`

SourceSha for every E3 row:
`bf4d69fd1b0f4022246dda38959b4b2d8d959c7fa6b118abd848a66536eb9e54`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E23 / `FindingID=V1R-001` | The fresh-child boundary substitution was repaired in the later versioned CQF1 fan-in. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E24 / `FindingID=V1R-002` | The omitted physical-owner alternatives were restored or explicitly carried in the later CQF1 package. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E25 / `FindingID=V1R-003` | The wrong v7 path labels are preserved as nonconsequential history with current evidence using exact paths. | Checking | `INFORMATIONAL_NO_ACTION` |

### Source E4 — CQF1 repair-2 recheck

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/CQF1_CONCORDANCE_57652BA1_2026-07-20/RECHECK_R1_REPAIR2/FINDINGS.csv`

SourceSha for every E4 row:
`43ba5e391b2a867cda1d2cea098859b757c140ff125762ef4210dd4932025f05`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E26 / `FindingID=V1R2-001` | The duplicate-key status defect was cured by the additive control reissue and parser backcheck. | Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E27 / `FindingID=V1R2-002` | Earlier wrong-path labels remain harmless additive history. | Checking | `INFORMATIONAL_NO_ACTION` |

### Source E5 — CQF1 control reissue

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/CQF1_CONCORDANCE_57652BA1_2026-07-20/RECHECK_R1_CONTROL_REISSUE/FINDINGS.csv`

SourceSha for every E5 row:
`4d6803b30e8276efb2ee035f3800d01796a12cd95194ce93059e432d5006304f`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E28 / `FindingID=V1R3-001` | The source status token is not scanner-closed, but the row itself says the control repair is sustained and interoperable. | Checking | `RESOLVED_WITH_CHANGE` |
| CH-E29 / `FindingID=V1R3-002` | The historical wrong-path labels are explicitly nonconsequential and require preservation only. | Checking | `INFORMATIONAL_NO_ACTION` |

### Source E6 — D-APP-49 current-location audit

SourceRef prefix:
`projects/chirality-app-dev/execution/_Evaluation/DAPP49_CURRENT_LOCATION_AUDIT_2026-07-27_FB16E32/FINDINGS.csv`

SourceSha for every E6 row:
`eb88b15632a7dfedd772b5cc32496d58c3612231b7c5194474f04666db836597`

| Candidate / SourceRef row | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-E30 / `FindingID=D49-001` | D-APP-76 admitted the evidence and durably closed the named OD6-011 current-location gap. | Checking; Approval; Decisions | `RESOLVED_BY_DECISION` |
| CH-E31 / `FindingID=D49-002` | The compatibility-facade ownership boundary is already established by D-APP-73/SCA-APP-005 and is not itself an action. | Deliverables; Checking; Decisions | `INFORMATIONAL_NO_ACTION` |
| CH-E32 / `FindingID=D49-003` | Completion of the one-cycle facade migration and readiness to retire the App compatibility facade remain unruled. | Deliverables; Planning; Approval; Checking; Decisions | `RESOLVED_BY_DECISION`; **promotion proposed** |
| CH-E33 / `FindingID=D49-004` | D-APP-48 still lacks an accepted current Root-owned successor identity despite the preparation route selected by D-APP-76. | Deliverables; Planning; Approval; Decisions | `RESOLVED_BY_DECISION`; **promotion proposed**, with Root route only after ruling |
| CH-E34 / `FindingID=D49-005` | The broad runtime-compatibility umbrella remains unproven but is better handled through the narrower CH-E12, CH-E13, and CH-E15 concerns. | Deliverables; Planning; Checking | `INFORMATIONAL_NO_ACTION` if those narrower candidates are promoted |
| CH-E35 / `FindingID=D49-006` | The focused audit recorded a high-severity dependency-audit notice and a Node module-type warning with no later explicit disposition found. | Work; Checking | `RESOLVED_WITH_CHANGE`; **promotion proposed** |
| CH-E36 / `FindingID=D49-007` | The original audit's missing run provenance is an admitted limitation that cannot be retroactively reconstructed and was not relied upon without qualification. | Checking | `INFORMATIONAL_NO_ACTION` |

### Sources E7–E9 — D-APP-50 historical blockers

| Candidate | SourceRef | SourceSha | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|---|---|
| CH-E37 | `projects/chirality-app-dev/execution/_Evaluation/DAPP50_HEADLESS_LIVE_BACKCHECK_F67D4470_2026-07-20/FINDINGS.csv row FindingID=F-001` | `dbb8bb8aa455dbf76ffc37a3e31998f24fec95d0278e44aa9612797eb3ad1adf` | The incomplete DEC-065 result validator was repaired and retained through the final accepted backcheck. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E38 | `projects/chirality-app-dev/execution/_Evaluation/DAPP50_HEADLESS_LIVE_BACKCHECK_F67D4470_2026-07-20/FINDINGS.csv row FindingID=F-002` | `dbb8bb8aa455dbf76ffc37a3e31998f24fec95d0278e44aa9612797eb3ad1adf` | The cancelled packaging residue was removed and its absence was sustained by later evaluation. | Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E39 | `projects/chirality-app-dev/execution/_Evaluation/DAPP50_HEADLESS_LIVE_REPAIR_BACKCHECK_FCF152B_2026-07-20/FINDINGS.csv row FindingID=V2-F-001` | `5d8e60f86ff322689cb4656ff55f0c8f0d2fa23e0176fb31935b6f74e0d4e3b0` | The missing result-envelope checksum correlation was repaired and freshly exercised by the final run. | Deliverables; Work; Checking | `RESOLVED_WITH_CHANGE` |
| CH-E40 | `projects/chirality-app-dev/execution/_Evaluation/DAPP50_HEADLESS_LIVE_FINAL_BACKCHECK_55A066FD_2026-07-20/FINDINGS.csv row FindingID=V3-F-001` | `5fe679285bbadec59a97f4b82428c0283614dff03dd31ae887fd3a0363b1a175` | V4 ran the five omitted commands and the completion evaluation explicitly closes V3-F-001. | Work; Checking | `RESOLVED_WITH_CHANGE` |

## 5. Handoff-state candidates

These are file-level candidates because the handoff schema is prose-shaped.
Ordinary deliverable work repeated inside historical blocker lists is not
promoted.

| Candidate | SourceRef | SourceSha | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|---|---|
| CH-H01 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md` | `0cdf6296f8413b8bbd4e3a41eed3a2352671de2398743e423b64d091510ecee8` | The handoff still says PR/owner merge pending although the run merged; surviving residuals are now carried by current deliverable surfaces and later decisions. | Work; Approval; Checking | `OBE` |
| CH-H02 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP84_REV2_RULING_ROUTE_2026-08-02/HANDOFF_STATE.md` | `18843ec0a1c409ff0d37e34ac9f482358e4c002cc6f778dd1e3515e98e76e170` | The Root-conditioned successor sequence remains current but is already carried by migrated row TM-APP-024 and its Root-linked source. | Planning; Approval; Decisions | `DUPLICATE` (`TM-APP-024`) |
| CH-H03 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP85_OPTIONA_RULING_2026-08-02/HANDOFF_STATE.md` | `8ef5cdc1a38dbbf02c381e2cc1b6aecae7b855cf80399e09251b325e6b9d350b` | The handoff's activation-pending-main state is superseded by merged activation and D-APP-85 execution closeout. | Approval; Checking; Decisions | `OBE` |
| CH-H04 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP85_POSTPILOT_RECONCILE_PACKET_2026-08-02/HANDOFF_STATE.md` | `017299a3242a989930707f3535ddcfdd83ff3859c02e09739950d5079cd6cec9` | The packet's awaiting-ruling state is superseded by both D-APP-85 owner rulings and R6 closeout. | Approval; Checking; Decisions | `OBE` |
| CH-H05 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-19_CODE_TESTS/HANDOFF_STATE.md` | `80c802199e98bbe4fa44b48739244c4e96f9d7b5d23dd5a3d574f8d57a9b7787` | The historical Git-closeout-pending state is overtaken by the merged code/test tranche. | Work; Approval; Checking | `OBE` |
| CH-H06 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-19_CONCORDANCE_RULINGS/HANDOFF_STATE.md` | `111cc573d3abae73c5a752cc7f1233c7b0f8b3d3f7f808a123d2be0500e491c8` | The historical CHANGE-publication handoff is overtaken by the merged D-APP-68 tranche. | Work; Approval; Checking | `OBE` |
| CH-H07 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE/HANDOFF_STATE.md` | `f9c42f8360c1d0888c80b728d779497b0f7f227907adafcb5db97d40760d2715` | The append-only handoff ends on released V3 and retains earlier blocker language, but D-APP-70/71 and later accepted evaluation/application records supersede those active-state claims. | Work; Approval; Checking; Decisions | `OBE` |
| CH-H08 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION/HANDOFF_STATE.md` | `783a4e8c9cade4b6897ca4d1bb3991f55ed46f4dad7443b2c55bd5dab6bba9ba` | The R1-only active-node handoff is overtaken by the completed D-APP-71 application/backcheck state. | Work; Checking; Decisions | `OBE` |
| CH-H09 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01/HANDOFF_STATE.md` | `e41d7f3a55709dbc7caeffd494411d68edbc3cf75123fbda16013d1bc8a7b097` | The Revision-1 packet's awaiting-owner-ruling state is superseded by D-APP-84 Revision 2 and its recorded ruling. | Approval; Decisions | `OBE` |
| CH-H10 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/HANDOFF_STATE.md` | `7a41419476075eab899cb69afd0eef8432f64e1ff3a50f0faba041a2b0cb331a` | The handoff still says owner merge pending although the redesign merged; its residuals were either repaired later or remain in current deliverable work surfaces. | Work; Approval; Checking | `OBE` |

## 6. Review-report candidates, reverified

The source below is candidate input only, not findings of record:
`plans/chirality_app_dev_maturity_survey_2026-08-01.html` at SourceSha
`2826a26c12fa793857a6e42baae7f7a5513dea66b89ced43b3ae034ddf3d02e9`.

| Candidate / SourceRef section | Concern | Domain lenses | Proposed disposition |
|---|---|---|---|
| CH-R01 / `§3 Parity instrument` | Reverification confirms the parity instrument remains unselected, but the concern is already carried by TM-APP-002. | Deliverables; Checking; Decisions | `DUPLICATE` (`TM-APP-002`) |
| CH-R02 / `§4 HZN-004 PRD staleness` | The duplicate §17 heading and pre-§17 ownership conflict were repaired, and the current PRD/corpus bytes support disposition of existing row TM-APP-003. | Deliverables; Checking; Decisions | `DUPLICATE` (`TM-APP-003`); use CH-M02 for row maintenance |
| CH-R03 / `§4 DEL-03-06 orphan` | SCA-APP-007 classified the DEL-03-06 container as misrouted DEL-09-06 evidence, migrated it, and adopted no DEL-03-05/06 decomposition entry. | Deliverables; Approval; Checking | `SUPERSEDED_BY_SCOPE_CHANGE` (`SCA-APP-007`) |
| CH-R04 / `§4 D-APP-82 PENDING_PR_MERGE` | The D-APP-82 current-state record is repaired without changing the ruling. | Checking; Decisions | `RESOLVED_WITH_CHANGE` |
| CH-R05 / `§5 D-APP-83 awaiting` | The survey's D-APP-83 awaiting-ruling statement is overtaken by D-APP-83 Option A adoption. | Approval; Decisions | `OBE` |

The report's six historical UNKNOWN relations are preservation-only and were
not harvested. Its `48 ## Remaining bullets` statement is neither re-used nor
recounted because `## Remaining` is a fenced work surface.

## 7. Explicit marker and receipt candidates

### CH-M01 — DEL-03 historical stable-ID reuse provenance audit

- SourceRef: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-007_2026-08-01_DEL03_Legacy_Evidence_Ownership/RUN_SUMMARY.md` marker, corroborated by the same marker in `Brief.md`
- SourceSha: `71d0b7f4e55504e4594a396d9bbb1bb1da766530c470983c1967477c0acdf129` (`RUN_SUMMARY.md`); corroborating `Brief.md` SHA `9c9cb85812d2afaf73af48a35310bd83bb2e245e29a1911af9d0eeb373310809`
- Concern: Historical reuse of DEL-03-01 through DEL-03-04 stable IDs lacks an explicit old-to-vNext supersession map and merits a provenance-only audit without changing current accepted identities.
- Domain lenses: `Deliverables; Checking; Decisions`
- Proposed disposition: `RESOLVED_WITH_CHANGE` through a bounded provenance artifact; **promotion proposed**.

### CH-M02 — TM-APP-003 closure echo

- SourceRef: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/PRD_OWNERSHIP_DAPP82_CURRENT_STATE_2026-08-01/RECONCILIATION_RETURN.md` marker
- SourceSha: `e11510fbb02e9e029c6d31f5651963f518023aa15ed28d56d2f960328c2085a6`
- Concern: Existing row TM-APP-003 remains deferred even though current `docs/PRD.md` has one §17, one §18, reconciled Root runtime ownership, and authority corpus v18 pins its current SHA.
- Domain lenses: `Checking; Decisions`
- Proposed disposition: `RESOLVED_WITH_CHANGE` on owner-directed row maintenance; **do not mint a new row**.
- Reverified evidence: `projects/chirality-app-dev/docs/PRD.md` SHA `3c357da78277f4c15ecee7cbba6c0a198bc1568b612229eeba63cb1d5972ea7b`; `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json` SHA `9aa9dec22dc416d04e385247acbce2dfeb40478f06c54629360497fad6258203`.

### CH-L01 — historical receipt parked lane

- SourceRef: `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` Receipt 0 `Parked lanes:` field
- SourceSha: `55b71adca9a29a7f797f7b2ca43b321f1866bb9376ce493f5d019593661b04ec`
- Concern: Receipt 0 parks owner rulings on open App decision rows, but the current decision register has no non-ruled row.
- Domain lenses: `Approval; Decisions`
- Proposed disposition: `OBE`

## 8. Proposed owner ruling slate

No selection is inferred. The following are the only proposed new promotions:

1. `CH-N02` — dual-target product-delivery direction.
2. `CH-N08` — App disposition of D-GOV-31 merge-gate succession.
3. `CH-E12` — shared-runtime version negotiation/incompatibility policy.
4. `CH-E13` — complete degraded-mode contract.
5. `CH-E15` — governed live PEC daemon-consumption proof.
6. `CH-E17` — daemon/helper bundle-identity decision.
7. `CH-E32` — App compatibility-facade retirement gate.
8. `CH-E33` — accepted current Root successor for D-APP-48.
9. `CH-E35` — dependency-audit and Node module-type warnings.
10. `CH-M01` — DEL-03 historical stable-ID provenance audit.

Separate existing-row rulings proposed:

- close `TM-APP-003` as `RESOLVED_WITH_CHANGE` using CH-M02 evidence;
- retain `TM-APP-002` unchanged because parity remains unselected; and
- retain `TM-APP-024` unchanged because D-APP-84 remains Root-conditioned.

All other candidates are proposed for no-row treatment or, if the owner wants
the register itself to preserve their closure echo, for the exact taxonomy
disposition shown above.

## 9. Routed-response drafts

None is authored yet. No promotion ruling exists in this session, so there is
no lawful new App register row ID to place in a reciprocal notice. If the owner
promotes CH-E12, CH-E13, CH-E15, or CH-E33 (or another cross-loop candidate),
the closeout tranche will include a draft only under the owner's gate, with the
inbound report SHA-256, the newly ruled App row ID, and exact evidence refs. No
foreign loop surface will be written.

## 10. Mutation statement

- App register rows written: `0`.
- Foreign register rows written: `0`.
- Other-loop files written: `0`.
- Six D-APP-81 historical UNKNOWN relations changed: `0`.
- Parity option selected: `no`.
