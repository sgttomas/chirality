# DEL-08-05 — forward-pass notes (RUN_D128, R2 PKG-08)

Sealed ledger: `DEL-08-05_claims.csv`, 77 data rows, SHA-256
`ba4729f5f4d65b6f81730b27cc51668f6045d34c758157a4a779d0b8a8ea47e0`. Validator: `RULES errors none |
warnings none`, `RESULT PASS errors=0 warnings=0`.

**Errata (added after the reverse pass).** `DEL-08-05_errata.csv` corrects one row, CLM-018.1:

| Field | Sealed | Errata-applied |
|---|---|---|
| Disposition | PARTIALLY_IMPLEMENTED | DOCUMENTED_UNIMPLEMENTED |
| Confidence | LOW | MEDIUM |

The census effect is shown side by side below. The tables in §1 give sealed figures.

| Figure | Sealed | Errata-applied |
|---|---|---|
| PARTIALLY_IMPLEMENTED | 12 | 11 |
| DOCUMENTED_UNIMPLEMENTED | 14 | 15 |
| LOW | 3 | 2 |
| MEDIUM | 32 | 33 |

All other figures are unchanged.

## 1. Census

**Rows by Disposition (sealed):**

| Disposition | Rows |
|---|---|
| ALIGNED | 16 |
| NOT_AUDITABLE | 14 |
| DOCUMENTED_UNIMPLEMENTED | 14 |
| STALE_SPECIFICATION | 12 |
| PARTIALLY_IMPLEMENTED | 12 |
| AUTHORITY_CONFLICT | 6 |
| IMPLEMENTED_DIFFERENTLY | 3 |

**Rows by ClaimType, then Disposition:**

- REQUIREMENT (41): 12 DOCUMENTED_UNIMPLEMENTED, 10 ALIGNED, 8 PARTIALLY_IMPLEMENTED,
  5 AUTHORITY_CONFLICT, 3 STALE_SPECIFICATION, 3 IMPLEMENTED_DIFFERENTLY.
- CONTEXT_CLAIM (17): 14 NOT_AUDITABLE, 3 STALE_SPECIFICATION.
- STATE_ASSERTION (6): 3 ALIGNED, 2 STALE_SPECIFICATION, 1 AUTHORITY_CONFLICT.
- ACCEPTANCE (6): 4 PARTIALLY_IMPLEMENTED, 2 DOCUMENTED_UNIMPLEMENTED.
- EXCLUSION (3): 3 ALIGNED.
- REGISTER_DEFECT (3): 3 STALE_SPECIFICATION.
- REMAINING_WORK (1): 1 STALE_SPECIFICATION.

**Coverage and splitting:**

- All 38 indexed units are covered: CLM-001..037 and REM-1.
- Run-local rows: REGISTER-1..3 and STATE-1.
- Split rate: 8 of 38 units (21%) were split, producing 43 sub-rows:
  - CLM-003: 4 rows (Attributes table rows);
  - CLM-004: 7 rows (Conditions table rows);
  - CLM-012: 13 rows (DEL-08-05-REQ-001..013);
  - CLM-013: 4 rows (Standards table rows);
  - CLM-018: 7 rows (the SubItems REQ-001..004, AC-001 and AC-002, plus the amendment paragraph);
  - CLM-025: 3 rows (the SubItems VER-001 and VER-002, plus the record list);
  - CLM-028: 2 rows;
  - CLM-037: 3 rows (the applied-row Description, Principal outputs and Notes columns).

**SEE rows (14), counted separately:**

- CLM-012.1, .2 and CLM-013.2 → CLM-006;
- CLM-012.7, CLM-013.4 and CLM-018.7 → CLM-003.3;
- CLM-012.9 → CLM-004.3;
- CLM-012.10 → CLM-004.5;
- CLM-012.11 → CLM-004.6;
- CLM-013.1 → CLM-007;
- CLM-013.3 and CLM-028.1 → CLM-003.2;
- CLM-034 → CLM-017;
- CLM-035 → CLM-009.

Without SEE rows there are 63 primary rows.

**HumanDecisionNeeded:** NO 51; R4-Q1 20; `R4; R4-Q1` 4; R4 2.

**Confidence:** HIGH 42, MEDIUM 32, LOW 3.

## 2. Least-confident rows

- **CLM-004.3 (redaction, K-EVENT-6), PARTIALLY_IMPLEMENTED, RUNTIME_EXTRACTION.**
  - No redaction step was found in the live runtime `session-store.ts` `appendEvent`, and
    `grep redact|sanitiz` over runtime `core/src` returns nothing. The App `run-logger.ts`
    redaction is LIVE.
  - Alternative reading: ALIGNED, if structural redaction runs upstream in a module I did not
    search (for example the Electron runtime-service host).
  - This is mainly a DEL-03 or DEL-05 store concern.
- **CLM-012.9 (DEL-08-05-REQ-009).** SEE row of CLM-004.3; same doubt.
- **CLM-018.1 (v3 REQ-001), PARTIALLY_IMPLEMENTED.**
  - `agent1-run-coordinator.ts` writes checkout AgentRun records under `_Coordination/AgentRuns/runtime/<runId>/`.
  - The module is LIVE-reachable per `REACHABILITY.csv`, through the `core/src/index.ts`
    re-export. However, `GovernedAgent1RunCoordinator` is instantiated only in
    `projects/chirality-runtime/tests/agent1-run.test.ts`.
  - Alternative reading: DOCUMENTED_UNIMPLEMENTED, because no product path runs it.
  - The same caveat, "test-only instantiation", is written into every row that cites this
    module: CLM-003.1, 004.2, 012.13, 018.4, 022 and 037.1/.3.

## 3. Register-defect summary

- **REGISTER-1..3.** In `_REFERENCES.md`, the CONTRACT (line 8), SPEC (line 9) and PRD (line 12)
  entries record `MATCH`. The recomputed hashes differ: `REFERENCE_HASHES.csv` shows Match=NO for
  all three, cited as `HASH-RECOMPUTE@00115c719`.
- **CLM-004.7** restates the PRD MATCH and points to REGISTER-3.
- **Other references.** I recomputed DIRECTIVE, TYPES and PLAN myself (read-only `shasum`); all
  three still match their recorded hashes, so they need no REGISTER row.
- **Related hygiene defects, filed as SoW rows rather than register rows:**
  - CLM-008 cites a method file by an absolute user-home path. The file
    (`agents/AGENT_SOFTWARE_DECOMP.md`) is absent at the frozen basis.
  - CLM-015 E-001 points to a `Procedure.md` that is not in the folder.
  - CLM-021 still calls the DEL-08-04 edge an ASSUMPTION, although `Dependencies.csv:5` and
    `:12` carry ACTIVE edges DEP-08-05-004 and DEP-08-05-011.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows |
|---|---|
| CODEX_SOLE_ENGINE | 16 |
| LIFECYCLE_GATE_PENDING | 8 |
| DOC_HYGIENE | 7 |
| PRE_V3_DRIFT | 7 |
| A2_TOPOLOGY | 5 |
| RUNTIME_EXTRACTION | 2 |
| NATIVE_DELEGATION | 1 |
| CARRIER_PROPAGATION | 1 |

**Central finding (reach).** Every module that defines or writes `ChildRunRecord`, the
`subagent.*` lifecycle events, `artifacts/subagents/`, the 16/512 KiB child-output limits, denied
child records or managed coordination persistence is REACH=LEGACY_ONLY:
`frontend/src/lib/harness/{agent-runtime-contract,sdk-message-mapper,tool-result-artifacts,managed-delegation,session-events}.ts`.

**What the live Codex path does instead:**

- Native children arrive as `tool.*` and `codex.notification` events
  (`delegated-engine-adapter.ts:277-289`).
- Live role and attribution evidence is `instruction-asserted` (`role-policy.ts`, used at
  `delegated-runtime.ts:321`).
- The native-child association exists in the runtime contracts.
- No checkout-contained descendant record is written by product code.

These rows cite R4-Q1. They are judged on the live path per CONVENTIONS §2.3.

**Secondary causes (`CAUSE2:`):**

- NATIVE_DELEGATION on most CODEX_SOLE_ENGINE and LIFECYCLE_GATE_PENDING rows;
- CARRIER_PROPAGATION on CLM-003.2 and STATE-1;
- A2_TOPOLOGY on CLM-018.4, CLM-037.3 and REM-1;
- CODEX_SOLE_ENGINE on CLM-004.1 and CLM-006;
- PRE_V3_DRIFT on CLM-012.12 and CLM-014.

**AUTHORITY_CONFLICT rows (6):**

- **CLM-006, CLM-012.1, CLM-012.2 and CLM-013.2** (HumanDecisionNeeded `R4; R4-Q1`):
  - `docs/TYPES.md` §10 (lines 520-555) now defines `ChildRunRecord` as `chirality-agent-runs/v2`,
    with `childInstanceId` and status `LAUNCHED|RUNNING|COMPLETED|FAILED|BLOCKED`. It was changed
    in `c9734a6ee` on 2026-07-11.
  - The SoW attributes to TYPES §10 a different set: `childRunId`, statuses `queued..denied`,
    `mode`, `capabilityPolicy`, `governance` and `contractVersion`. D-APP-40 and D-APP-56 UPD-138
    record that set.
  - DIRECTIVE §0 does not rank rulings against TYPES.
  - `contractVersion` is a string in the SoW but the numeric literal `1` in code.
- **CLM-037.2 and STATE-1** (R4):
  - The applied decomposition row and `_CONTEXT.md` require "daemon linkage metadata".
  - D-GOV-43 item 7 and D-APP-127 retire the daemon from the App path without naming this row.

**CONTEXT records used:**

- `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, WP-06 and AT-028;
- the done-declaration candidate: DONE-10, and Q-11 on whether managed multi-child execution is
  still in v3 done. Q-11 is a Ruling B question for R4 and is cited only as CTX.

**GOVERNING records cited as `GOV:`:**

- D-GOV-43 items 7, 8 and 9, from `docs/governance_harness/_PROPOSALS/.../D-GOV-43.proposed.md`
  as adopted by `D-GOV-43_codex_host_replatform.md`;
- D-GOV-35 item 5;
- D-APP-127, which retires APP-HOLD-1;
- D-APP-38, D-APP-40 and D-APP-56.

**NONE_FOUND searches:**

- **Register.** I read `_REGISTER.md` rows D-APP-38, 40, 56, 68, 70, 72, 74, 117 and 127, and
  grepped the D-APP-127 ruling for harness, descendant, child and DEL-08 terms. It does not name
  DEL-08-05.
- **CONTEXT.** I searched the done-declaration candidate (DEL-08-05, descendant, child-run,
  legacy, harness) and the release plan text (WP-06, DEL-08-05, AT-028, in-process, retained).
  The AgentRuns `APP_V3_*` folders that mention DEL-08-05 were located by filename only.
- **Rows whose DirectionEvidence stays NONE_FOUND after these searches:** CLM-004.3, 012.9, 008,
  015, 021 and 032.
- **UNRECORDED_JUDGMENT:** not used. A vocabulary mechanism fit every row.

**PostReleaseBasis:** NO on every row.

- Only two cited files are in `TOUCHED_PATHS.csv`: `session-store.ts` and `codex-supervisor.ts`.
- `git blame -L` at `00115c719` attributes all relied-on lines to other commits:
  - `session-store.ts` 654-662, 819-844 and 1126: `8b3643e6c`, `9b005c23a`;
  - `codex-supervisor.ts` 280-309, 518-519 and 590-591: `95b342519`, `9eaddb596`.

**REM-1 (MechanicallyUnblocked = NO):**

- DEL-08-04-V3-01 is still listed as Remaining in DEL-08-04 `_STATUS.md:17`.
- No G4 record was found.
- The item's APP-HOLD-1 check was retired by D-APP-127.
- Its write locus names the legacy harness, whereas D-GOV-43 item 9 has the App record AgentRuns
  from the event stream.
- The WP-03 "supervisor helper" premise of the gate may also be retired by D-GOV-43 item 7. This
  is inferred, so I did not assert a `MOOT:` token.

## 5. Method friction

- **LIVE reach versus product instantiation.** `REACHABILITY.csv` marks a module LIVE when a
  product entry imports it, even through a barrel re-export. `agent1-run-coordinator.ts` is LIVE
  that way but is instantiated only in tests.
  - Proposal: allow a `REACH=LIVE` qualifier (for example `INSTANTIATED=TEST_ONLY` in Notes), or
    add an instantiation column to the pack.
- **Governing documents changing after a ruling.** TYPES §10 changed on 2026-07-11, and its
  `ChildRunRecord` now diverges from a type that D-APP-40 and D-APP-56 treat as current. MR-11
  covers a ruling over *older* corpus wording, but here the GOVERNING document is the newer text.
  - I used AUTHORITY_CONFLICT.
  - Proposal: state explicitly that MR-11 applies only when the ruling postdates the wording;
    otherwise the row is AUTHORITY_CONFLICT.
- **PREGATHER.** Its anchors were accurate where I checked them. Two points need the §7
  discipline:
  - its "LIVE runtime" labels need the instantiation check above;
  - one of my greps (`grep -rln GovernedAgent1RunCoordinator projects/`) listed filenames under
    `projects/chirality-runtime/execution/**`. I opened none of those files and cite none of them.
    Future greps should exclude `*/execution/**`.
- **Scope of REFERENCE_HASHES.** Pack item 3 covers only CONTRACT, SPEC and PRD. TYPES carries the
  most relevant change for this deliverable, yet its hash still matches. A hash match therefore
  does not show semantic currency.

## 6. Effort

- **Files read** (about 45, line ranges where possible):
  - the deliverable folder: 8 files;
  - the rulebook, run basis, pack and pregather: 8;
  - decision records: 4;
  - governing documents, by grep and ranges: 5;
  - code and test files: about 20.
- **Git.** Read-only `log`, `blame -L` and `show --stat` against the frozen tree only.
- **Context budget.** Moderate, not tight. The PREGATHER locator saved most of the search effort.
