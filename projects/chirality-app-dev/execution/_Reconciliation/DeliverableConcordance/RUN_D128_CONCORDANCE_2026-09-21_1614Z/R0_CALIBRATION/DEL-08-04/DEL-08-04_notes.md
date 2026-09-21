# DEL-08-04 — R0 calibration notes (forward pass)

Deliverable: `DEL-08-04` Type 2 Subagent Governance Bridge (PKG-08), lifecycle `IN_PROGRESS`.
Basis: frozen tree at `00115c719`. Ledger: `DEL-08-04_claims.csv` (80 rows).

## 1. Census

**Rows by ClaimType:**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 30 |
| STATE_ASSERTION | 18 |
| CONTEXT_CLAIM | 13 |
| ACCEPTANCE | 12 |
| REMAINING_WORK | 3 |
| REGISTER_DEFECT | 3 |
| EXCLUSION | 1 |

**Rows by Disposition:**

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 29 |
| ALIGNED | 27 |
| NOT_AUDITABLE | 9 |
| PARTIALLY_IMPLEMENTED | 6 |
| IMPLEMENTED_DIFFERENTLY | 3 |
| REMAINING_STATE_MISMATCH | 3 |
| DOCUMENTED_UNIMPLEMENTED | 2 |
| STALE_ASSESSMENT | 1 |

**Split rate.** 14 of the 39 indexed units were split (36%): SEC-1 (5), SEC-2 (3), SEC-3 (2), CLM-003, 004, 005, 009, 013, 025 and 028 (2 each), CLM-010 (11, one per R01–R11), CLM-016 (8: the dated note plus REQ-001..005, AC-001, AC-002, which sit under that heading), CLM-022 (3: records, VER-001, VER-002) and CLM-030 (4). Indexed units produce 75 rows. There are 5 run-local rows: REGISTER-1..3 and STATE-1..2.

## 2. Least-confident rows

- **SEC-1.2, CLM-016.3: native descent assigns no role** (IMPLEMENTED_DIFFERENTLY, LOW).
  - What the code does: the Runtime turns all four Chirality roles into Codex `[agents]` types (`native-role-config.ts:156-196`). This follows D-GOV-43 item 8, where native sub-agents "receive the intended role instructions". A native child spawned with a role type therefore runs under that role's instructions.
  - Role evidence still records `nativeDescendant` separately, and `role-policy.test.ts` shows role is not inferred from descent.
  - Alternative reading: the role is chosen through the configured agent type, not inherited by descent. On that reading the row is ALIGNED. Routed as R4.
- **CLM-005.2: "Live evidence is managed-delegation.ts …"** (STALE_SPECIFICATION, LOW).
  - The module is not on the production path.
  - Alternative reading: "live" means "current evidence files". On that reading the row is ALIGNED.
- **CLM-030.3: the approval-reference format is an open item with no Remaining entry** (REMAINING_STATE_MISMATCH, LOW).
  - Alternative reading: CLM-007's "approval-reference question" is a mislabel for the D-APP-53/117 decision-replay item. REM-1 tracks that item, so the row would be ALIGNED.
- **REM-3 gate: "DEL-02-02-V3-04 selected"** (MechanicallyUnblocked NO, MEDIUM).
  - DEL-02-02 still marks V3-04 `NOT_SELECTABLE_UNTIL`, but it also records a bounded read-only V3-04 slice on 2026-09-06. Whether V3-04 counts as "selected" is therefore ambiguous.

## 3. Register-defect summary

- **REGISTER-1.** DEP-08-04-011 is a constraint on "accepted DEL-02-07 process-supervisor" returns. Root `docs/CONTRACT.md` K-CONTROL-1 retires that supervisor-socket design (D-GOV-43 item 7). The same gate appears in REM-2 and REQ-005.
- **REGISTER-2.** Daemon wording survives in DEP-08-04-001 ("daemon-client dispatch"), DEP-08-04-009 ("daemon-owned operational managed delegation") and DEP-08-04-014 ("daemon session-record delegation-policy field"), and in `_CONTEXT.md` (STATE-1). Under A2 there is no daemon: the App owns the Runtime child (root K-RUNTIME-1). The peer item DEL-03-02-V3-01 was re-expressed for A2; DEL-08-04 was not.
- **REGISTER-3.** `_REFERENCES.md` uses REF-009 and REF-010 twice, once in the corpus table and once in the SCA-APP-010 table, for different sources. The SoW's REF-007 (CLM-006) is a machine-specific absolute path to `agents/AGENT_SOFTWARE_DECOMP.md`, which is absent at `00115c719`. `_REFERENCES.md` REF-007 is `workflows/software-decomp/WORKFLOW.md` instead.
- **Metadata drift outside the registers:**
  - CLM-002 lists CoversScopeItems as SOW-063 only, while the frontmatter and `_CONTEXT.md` carry SOW-063 and SOW-083.
  - CLM-004.2 and CLM-019 still list the DEL-04-01 SDK probe as an ACTIVE prerequisite, although DEP-08-04-005 was RETIRED on 2026-08-24.
  - SEC-3.2 says DEP-025/026 "await" extraction, but D-APP-109 performed it on 2026-09-05.

## 4. Direction and cause

**Main finding (SEC-1.1, SEC-2.1, CLM-003.1, CLM-016.2/.4; CODEX_SOLE_ENGINE).** The App-side managed-delegation bridge is not reachable from the production path, although its code and tests are intact:

- `ManagedDelegationService`, `evaluateSubagentGovernance` and `delegate_agent` registration are present in `frontend/src/lib/harness/`, and their tests pass in the APP gate transcript.
- Nothing in production reaches them. `runtime.ts` (TurnEngine, and the coordination-tools → read-tools → sdk-options-builder → claude-agent-sdk-manager chain) is imported by no App route and no Electron entry; the only other importer is a demo script.
- Live turns take the path `app/api/harness/turn/route.ts` → Runtime → Codex App Server.
- The only live delegation is Codex-native, through the `[agents]` table the Runtime configures.

Consequences:

- Requirements that describe how `delegate_agent` behaves when it is invoked hold at module level. I marked them ALIGNED (CLM-010.x), with notes that the module is off the live path.
- Claims that the product delegates through `delegate_agent`, or that it is the "sole" path, are IMPLEMENTED_DIFFERENTLY or STALE_SPECIFICATION (tag NATIVE_DELEGATION).
- No managed cancellation/cleanup code was found, and there is no class-aware (managed vs native) logic in `subagent-governance.ts`. Both are expected, since V3-01 is still open.
- The per-chat delegation policy (SOW-083) is not implemented anywhere (SEC-1.4, SEC-2.2, REM-3).

**Other causes:**

- **PRE_V3_DRIFT.** R05, the principles, the examples, the procedure step and the verification row all say "Agent 0 admits only named Agent 1". The 2026-08-16 TM-APP-044 repair made the code admit configured Agent 0→TASK and generalist Agent 2. It is recorded in the deliverable's MEMORY and follows root `AGENTS.md` ("HELP_HUMAN may … dispatch bounded Type 2 work directly"). The SoW text was never updated. App `docs/CONTRACT.md` K-SUBAGENT-1 still says "0→1 or 1→2", which may need a separate governing-doc look.
- **A2_TOPOLOGY.** Daemon wording and the DEL-02-07 supervisor gate (SEC-1.5, CLM-016.6, REM-2, REGISTER-1/2, STATE-1).
- **CARRIER_PROPAGATION.** Dated reconciliation notes are triplicated (CLM-007, CLM-016.1, CLM-031) and say only the approval-reference question remains open. Several items still marked "TBD" (decision-object shape, DEL-08-05 interface) are recorded as landed.

**CONTEXT records used:**

- `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md`, which transcribes D-GOV-43 items 4, 8 and 10 and whose ruling record is GOVERNING.
- `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/` (cited as a folder; not read in depth).
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` D1 (D-APP-74 supersession for multi-child). I read it but did not cite it in any row.

No CONTEXT record explains the frontend bridge being left unwired, beyond the general Codex re-platform direction. That is why DirectionEvidence cites the re-platform steer rather than NONE_FOUND. A stricter reader could tag SEC-1.1 as UNRECORDED_JUDGMENT.

**Governing records consulted:**

- App `docs/CONTRACT.md` K-SUBAGENT-1..3, K-UNTYPED-1 and K-ROLE-2.
- Root `docs/CONTRACT.md` K-RUNTIME-1 and K-CONTROL-1.
- `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` and its proposal items 8 and 10.
- `_DECISIONS/_REGISTER.md` rows D-APP-117 (AWAITING_RULING), D-APP-127 and D-APP-108.

## 5. Method friction

- **LatestDecision.** The column only takes `D-APP-nn`, but the controlling ruling for the native class is Root D-GOV-43, and D-APP-127 (its App application) does not mention delegation. I wrote `D-APP-127 (context)` and named D-GOV-43 in the notes. Proposed revision: allow `D-GOV-nn` in LatestDecision.
- **Reachability.** The conventions have no rule for code that exists and passes tests but is off the production path. I split the decision: conditional invariants → ALIGNED; claims about what the product does → IMPLEMENTED_DIFFERENTLY or PARTIALLY_IMPLEMENTED. Proposed revision: add a note token, or a CauseTag such as `OTHER:UNWIRED_MODULE`, for evidence that is present but unreachable.
- **PostReleaseBasis.** This cannot be decided without git, which is prohibited here. Every row is set to `NO`, but that is unverified. Proposed revision: the manager supplies the file list for the four post-release commits.
- **CLM-016 range.** The CLM-016 unit also contains the REQ-/AC- bullets. The index labels it only as a dated note, so splitting was required. The same applies to the VER bullets under CLM-022.
- **DirectionEvidence.** Direction recorded in declared state (another deliverable's `_STATUS`, or this deliverable's MEMORY) is not a CONTEXT source, so rows whose only explanation lives there can only cite NONE_FOUND (e.g. the PRE_V3_DRIFT rows).

## 6. Effort

- About 35 files or ranges read:
  - the 8 deliverable files;
  - 6 frontend source files and 5 test-case lists;
  - 6 Runtime source/test files;
  - the decisions register, 2 steers, D-GOV-43 and its proposal, App and Root CONTRACT excerpts;
  - DEL-02-02 and DEL-03-02 `_STATUS` excerpts.
- `_SEMANTIC*.md` was not read.
- Context was moderately tight: the 502-line SoW and the reachability tracing were the main cost. The oversize threshold should probably be about a 500-line SoW for this deliverable type.
