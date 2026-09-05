# PEC Task Management — candidate harvest report

**Status:** CANDIDATE REPORT — OWNER PROMOTION REQUIRED

**Date:** 2026-08-02

**Mode:** candidate harvest

**Invoking loop:** PEC

**Register:** `_DomainEngines/pec/_TaskManagement/REGISTER.csv`, schema 1.0

**Authority:** Decision support only. This report proposes; it does not create,
promote, prioritize, assign, defer, close, or disposition a register row. Only
the owner may promote candidates or rule dispositions (K-TM-3). No register
row was written during this harvest.

## Federation preflight

The mandatory read-only federation preflight completed before harvest:

- coverage: `COMPLETE`;
- canonical registers discovered and validated: 4 (`PEC`, `ROOT`, `APP`,
  `PIP`);
- invalid, unreadable, or ambiguous registers: 0;
- excluded lookalikes: 0;
- register writes: 0; and
- program-integrity observation: one `REMOTE_CLOSED_LOCAL_OPEN` relationship
  between `TM-PIP-023` and `TM-ROOT-053`. It does not involve the PEC register
  and is disclosed but not presented as a PEC candidate.

The derived projection is
`_DomainEngines/pec/_TaskManagement/.candidates/federation.json`. It is
gitignored, rebuildable, and not authority.

## Sweep boundary and coverage

The harvest covered the PRD §5.1 structured surfaces under the PEC loop's
standing and execution trees: the PEC decision register; every routed notice
in `projects/pec/execution/_Coordination/`; all five live
`Review_Findings.csv` files; the active reliance-hold register; current and
historical handoff-state files; packet open-question/conflict fields; the
decomposition `ScopeLedger.csv` TBD rows; new REVIEW snapshots; and governed
run-record markers.

The deterministic `taskmgmt scan` projection was used as a first pass and was
manually narrowed to PEC. Its declared v0 omissions (run-record markers,
review-report sections, and per-document token mode) were then checked
directly. Coverage for the enumerated PEC structured surfaces is `COMPLETE`.

Findings by source class:

- decision register: `D-PEC-02` remains non-ruled and is already represented
  by `TM-PEC-003`; `D-PEC-03` is a non-operative pointer row;
- notices: the three notices dated 2026-08-02 are not cited by a PEC row and
  produce candidates 01 and 02 below; older open-notice concerns are already
  represented by `TM-PEC-001`, `TM-PEC-002`, and `TM-PEC-006`, or were closed
  by their cited successor instruments;
- evaluation findings: no PEC `FINDINGS.csv` exists; among the five
  `Review_Findings.csv` files, two findings are `RESOLVED`, two files are
  header-only, and one finding is `DEFERRED` (candidate 03);
- holds: `ACTIVE_RELIANCE_HOLDS.csv` is valid and header-only;
- handoffs and new review reports: the only unresolved review blocker is the
  same DEL-01-06 `RF-001`; the D-PEC-75 handoff also carries OI-003 as an
  explicit open owner question (candidate 04);
- TBD register: nine PRD §16 open issues remain in `ScopeLedger.csv`; only
  OI-003 was carried into the new D-PEC-75 execution handoff. The other eight
  are standing product/decomposition questions that did not arise as new
  session residue and therefore fail the PRD §7.1 promotion gate for this
  harvest; and
- run-record markers: no new `NEEDS_HUMAN_RULING:`, `MISSING:`, or
  `TM-CANDIDATE:` marker remains unrepresented. The historical DEL-04-01
  marker is already represented by `TM-PEC-004`.

Per PRD §5.5, slates, `## Remaining` work lists, work graphs, and ordinary
dependency work were fenced from candidate creation.

## Candidate proposals

### CAND-PEC-2026-08-02-01 — shared Task Management instruction succession

TM-CANDIDATE: Disposition the two 2026-08-02 Task Management instruction notices now that the schema repair and federation preflight are both present in the shared instruction package | projects/pec/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_INSTRUCTION_SCHEMA_REPAIR.md; projects/pec/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_FEDERATION_PREFLIGHT.md

| Field | Proposed value |
|---|---|
| Concern | PEC has received successive schema-repair and federation-preflight notices for `AGENT_TASK_MANAGEMENT.md`; no PEC authority pin or live mirror requires amendment, so only the notices' local disposition remains. |
| SourceRef | `projects/pec/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_INSTRUCTION_SCHEMA_REPAIR.md`; `projects/pec/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_FEDERATION_PREFLIGHT.md` |
| SourceSha | `6cfd4a9e94fb4f9d0e02202f03a0c7b28c2b0d40b8f63c0c2e643c8af15c2494`; `d80f1c2c45227b182e78e37da03cc3db0cdcb4bf80f7a510c42f48e8d33dd148` |
| Domain lenses | Decisions; Checking; Approval |
| Proposed disposition | `INFORMATIONAL_NO_ACTION` — acknowledge the shared instruction succession without creating a PEC product, policy, lifecycle, or mirror-repair act. |

The live shared instruction SHA-256 is
`d8e50e1c35c6e512986800515c2642ea4696fe447f5a97f502a76cbb87625f28`,
matching the federation notice's candidate hash. This currency observation is
evidence only and creates no local pin.

### CAND-PEC-2026-08-02-02 — Root harness scope correction notice

TM-CANDIDATE: Disposition the Root harness scope-correction notice after confirming that PEC holds no live SHA pin or mirror requiring repair | projects/pec/execution/_Coordination/NOTICE_2026-08-02_ROOT_HARNESS_SCOPE_CORRECTION.md

| Field | Proposed value |
|---|---|
| Concern | The Root notice asks PEC to acknowledge or repin shared instruction surfaces on an ordinary currency pass, but no PEC-owned live pin or mirror of the superseded bytes was found. |
| SourceRef | `projects/pec/execution/_Coordination/NOTICE_2026-08-02_ROOT_HARNESS_SCOPE_CORRECTION.md` |
| SourceSha | `e4cc3b93f01542116e03fd1156454e8ac33cbf523e459524fe197414405d1044` |
| Domain lenses | Decisions; Checking; Approval |
| Proposed disposition | `INFORMATIONAL_NO_ACTION` — acknowledge the correction; no PEC policy, product, corpus-pin, or artifact change is required. |

### CAND-PEC-2026-08-02-03 — DEL-01-06 deferred VER-005 review obligation

TM-CANDIDATE: Preserve DEL-01-06 RF-001 until DEL-01-05 enforcement exists, then reopen it and rerun SELF_CHECK without waiving VER-005 | projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv row RF-001

| Field | Proposed value |
|---|---|
| Concern | DEL-01-06 cannot satisfy AC-005 or AC-006 until DEL-01-05 enforcement becomes available and the mandatory VER-005 rerun is executed, so RF-001 remains a durable deferred review obligation. |
| SourceRef | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv`, row `RF-001`; `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md`, “SELF_CHECK disposition and remaining gates” |
| SourceSha | `fa04561fe97cc33cc8198ef2f5dfa31b4c92f4aff41d591556e312f1e2e735bb`; `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| Domain lenses | Checking; Deliverables; Work; Planning |
| Proposed disposition | `RESOLVED_WITH_CHANGE` — available only after DEL-01-05 enforcement is produced and the required DEL-01-06 SELF_CHECK rerun closes RF-001 with exact evidence. If promoted now, the lawful interim posture is `DEFERRED` with that availability as its trigger, not closure. |

### CAND-PEC-2026-08-02-04 — OI-003 long-term loop-registry home and shape

TM-CANDIDATE: Obtain the PRD §16 ruling for OI-003's long-term loop-registry home and shape without treating DEL-01-06's replaceable local JSON default as that ruling | projects/pec/execution/_Decomposition/ScopeLedger.csv row SOW-077; projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md

| Field | Proposed value |
|---|---|
| Concern | D-PEC-75 produced only a replaceable local default and expressly left OI-003/SOW-077's long-term registry home, shape, later loop entries, and consumer activation undecided. |
| SourceRef | `projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-077`; `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md`, final paragraph |
| SourceSha | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`; `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| Domain lenses | Decisions; Planning; Deliverables; Approval |
| Proposed disposition | `RESOLVED_BY_DECISION` — cite the future PRD §16 owner ruling that selects or deliberately defers the long-term home and shape; if the ruling instead opens an SCA, the later lawful closure route would be `SUPERSEDED_BY_SCOPE_CHANGE`. |

## Closure-echo triage — PEC adoption is no longer pending

The federation evidence establishes that root row `TM-ROOT-100` is `CLOSED /
RESOLVED_BY_DECISION`, citing exact D-PEC-73 decision and routed-notice hashes.
No row in the PEC register and no candidate in the 2026-08-01 harvest says the
adoption remains pending.

Three local historical/presented records still retain pre-ruling language:

| SourceRef | SourceSha | Echo |
|---|---|---|
| `projects/pec/execution/_Coordination/TM_ADOPTION_PACKET_2026-07-31.md` | `cdbfdbc2c8240f0439bbac8626283c6dae611afc412d482af76fa1fcfff8ed58` | Status remains `PRESENTED — AWAITING LOOP OWNER RULING` and its predicted root closure cites indicative `D-PEC-72`. |
| `projects/pec/execution/_Coordination/NOTICE_D-GOV-32_TASK_MANAGEMENT_ADOPTION.md` | `baa94af04a8f47a4ca2087d783013f9b4186603d24a1b899dd6d76521c8f3bdd` | Says `TM-ROOT-100` tracks PEC adoption as pending Stage-B work. |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-73_task_management_adoption.md` | `2717ba9f6d2c0baeb8ac2096e4657745d683a79731af4db88dc93d5eaea4a89e` | Its “Live basis” historically records the root row as open at presentation time. |

This is a closure echo, not a new Action Item: D-PEC-73 O-A is effective, the
PEC register exists, and root `TM-ROOT-100` is closed. The packet, routed
notice, and supersede-never-edit decision record remain historical evidence;
this report proposes no rewrite and no duplicate register row.

## Routed-response drafts

None. None of the four proposed dispositions requires another loop to act:
the two Root notices need only PEC-local acknowledgment, and candidates 03
and 04 remain inside PEC's REVIEW/production and PRD §16 instruments. No file
was written into another loop's surface.

## Owner promotion gate

The owner may promote any subset of
`CAND-PEC-2026-08-02-01` through `CAND-PEC-2026-08-02-04`. Unpromoted
candidates remain report-only observations. Promotion does not adopt the
proposed disposition; disposition remains a separate owner act.

## Promotion and disposition outcome

The owner ruled the complete harvest slate on 2026-08-02:

| Candidate | Register row | Owner-ruled result |
|---|---|---|
| `CAND-PEC-2026-08-02-01` | `TM-PEC-007` | Promoted and closed in the same act as `INFORMATIONAL_NO_ACTION`, citing this report's live-instruction currency verification and no-required-pin finding. |
| `CAND-PEC-2026-08-02-02` | `TM-PEC-008` | Promoted and closed in the same act as `INFORMATIONAL_NO_ACTION`, citing this report's finding that PEC owns no live pin or mirror of the superseded bytes. |
| `CAND-PEC-2026-08-02-03` | `TM-PEC-009` | Promoted `DEFERRED`; trigger is DEL-01-05 enforcement availability, followed by the mandatory DEL-01-06 SELF_CHECK rerun closing RF-001 with exact evidence. VER-005 is not waived. |
| `CAND-PEC-2026-08-02-04` | `TM-PEC-010` | Promoted `DEFERRED`; trigger is an owner-initiated PRD §16 ruling on OI-003's long-term registry home and shape. DEL-01-06's replaceable local default is not that ruling. |

The owner accepted the closure-echo section as reported: no source rewrite and
no additional row. These acts create no product, policy, lifecycle, source,
release, professional-reliance, or cross-loop authority.
