# Return B4: SCA-006 checkpoint-group-1 package (WORKING_ITEMS, node R1)

**Role and method.** WORKING_ITEMS (Type 1) ran `Workflow: chirality-root:bundled:workflow:scope-change`, checkpoint group 1 only (method parts A and B). The model was claude-opus-5-5 (Claude Code, host-reported) at high effort, as the steer requested. The brief is `B4_SCA006_CHECKPOINT1.md` in the HELP_HUMAN scratchpad (SHA-256 `87612acaa41fb3975a87fddd6a97803a4968e0f0d1d1df837ce0373e82d0ae90`). Two HELP_HUMAN addenda arrived in-session and are quoted in `Brief.md`.

**Publication.** PR https://github.com/sgttomas/chirality/pull/922 from `claude/pec-sca006-cp1-package` to `main`, **not merged**. The package bytes the verifier approved are at commit `0aa65beef`. Verdict 03 was recorded at `17a4433d8`. This return lands in the commit after that, which is the PR head reported in the hand-back.

**Status.** Nothing is accepted. `Decision_Log.md` row SCA006-CP1 is `AWAITING_OWNER`. No PRD, `projects/pec/AGENTS.md`, decomposition, register, pointer, Scope of Work, SPEC, `_CONTEXT.md`, `_STATUS.md`, `_DECISIONS/**`, work graph, STATUS/README, `v2/**` or foreign file changed.

## Package (`projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `205a46c04f2db6d34bead78db3064a02ff9d9d66a5e54fa9ff06b5c6314a1831` |
| **`Impact_Assessment.md`** (the owner accepts it by this hash) | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` |
| `Amendment_Actions.csv` (PROPOSED) | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` |
| `Pre_Change_Coverage.json` (byte copy of `COV_SCA005_POSTSETUP_2026-09-25_1606/coverage_summary.json`) | `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d` |
| `Decision_Log.md` | `8a01bd653eca52bb8ffae947ffce28d83d7da6beaf690b35c72563f88615547a` |
| `Handoff_State.md` | `4526797c0bab914906b13cf095078508f9df2f8ea606fb4a4542dda5ce55f9df` |

No pre-change audit folder was created. Every audit input is byte-identical between the audited commit `995af4f36` and the base `13df8b795` (Impact Assessment §2.1).

## Action counts (recommended set DQ-a + ENV-a + BUD-a + GATE-a + INS-a)

- **Total:** 54 actions, 12 ADD and 42 MODIFY.
- **By entity type:** 31 OTHER, 14 DELIVERABLE, 4 VOCAB_TERM, 3 PACKAGE, 2 OBJECTIVE.
- **By group:**
  - K: 13 PRD loci.
  - I: 4 AGENTS.md loci.
  - D: 26 decomposition rows, including:
    - SOW-097..100;
    - DEL-08-06 and DEL-10-13;
    - C3, SOW-003/060/080 and OI-006;
    - PKG-04/08/10 and OBJ-001/002;
    - 3 new vocabulary terms and one modified term.
  - S: 11 derivative advisories.
- **Part-A validation:** 54/54 PASS.
- **Scope of Work population:** 32 contracts, 9 AFFECTED and 23 NOT_AFFECTED (IA §7.1).
  - Proposed S4 set: DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04 and DEL-04-03.
  - Review level: DEL-03-04, DEL-10-03 and DEL-00-03.
  - DEL-01-06 is NOT_AFFECTED on its own evidence.
- **Option deltas (IA §13):**

  | Option | Actions | SOW population |
  |---|---:|---|
  | DQ-b | 49 | 7 AFFECTED |
  | DQ-c | 43 | — |
  | ENV-b | 52 | — |
  | BUD-b | 54 | — |
  | GATE-b | 61 with DQ-a | 15 AFFECTED |

## Owner question set (IA §15; manager recommendation in brackets)

1. CP1-A: confirm the parsed change set [confirm].
2. CP1-B: accept `Impact_Assessment.md` at SHA-256 `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` [accept].
3. CP1-DQ: direct query through tool calls [a].
   - (a) specify now with a read-only `agent` access class;
   - (b) specify now under the `harness` class;
   - (c) defer behind a new §16 access-class decision.
4. CP1-ENV: the reliance envelope [a].
   - (a) a new PEC-ORI-007 mapped to DEL-04-03;
   - (b) fold it into PEC-ORI-003.
5. CP1-BUD: response budgets [a].
   - (a) a new PEC-API-006 mapped to DEL-08-03, with its numbers set at P1;
   - (b) fold them into PEC-API-004.
6. CP1-GATE: the reliance gate [a].
   - (a) a standing gate for any release that advertises reliance (SOW-100, DEL-10-13);
   - (b) extend the P1 exit test.
7. CP1-INS: the AGENTS.md change [a].
   - (a) an instruction tranche at checkpoint 3;
   - (b) a separate tranche afterwards.
8. CP1-RC: R-C stays excluded under D-PEC-90 [confirm].

To take every recommendation, the owner can reply: "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded." Nothing asks about CHECKING.

## Checks (worktree root; zsh; python3 3.13.7)

| Check | Result |
|---|---|
| `validate_decomposition_registers.py projects/pec/execution --strict` | before and after: 66 registers, 263 rows, 0 errors, 0 warnings, exit 0 |
| Preimage hashes | the PRD, SOFTWARE_DECOMP, registers, D-PEC-90 pins and the selected proposal hash all match (IA §2) |
| `Amendment_Actions.csv` against the contract columns and enums | 54 rows, 9 columns, 0 errors |
| `validate_scope_change_packet.py` | exit 1: the schema does not fit. It validates a PKG-00 consumable packet, as in SCA-005 |
| Reliance-hold preflight, `exact-correction-preparation` | `ALLOW` for 9 targets (the verifier also got `candidate-validation` `ALLOW`); the register has a header only |
| `git diff --check` | clean |
| Practitioner-harness self-check | exit 0; pre-existing REVIEW findings only |
| `validate_pec_loop_receipts.py` | VALID |
| Containment | the branch diff against `origin/main` touches only the snapshot folder and these `returns/` files |

## Verifier verdicts

All three rounds used one fresh `pec-reviewer` instance on opus, read-only, resumed between rounds.

| Round | Candidate | Verdict | Findings | Disposition |
|---|---|---|---|---|
| 01 | `e2855e552` | PASS WITH MINOR | 7 MINOR, 5 NOTE | all repaired |
| 02 | `64677504b` | PASS WITH MINOR | 2 MINOR, 2 NOTE | all repaired |
| 03 | `0aa65beef` | PASS | none blocking | — |

Verdicts: `returns/B4_VERIFIER_VERDICT_01.md`, `_02.md` and `_03.md`, each with the manager's dispositions.

## Children

- **A1 locus inventory.** `pec-task`, opus, read-only. It returned 232 loci and a 32-row SOW population, and its quote verifier found no failures. The outputs are in the manager scratchpad and are not committed; their hashes are in the Handoff.
- **Verifier.** Recorded above.
- **Enforcement.** Read-only use by the `pec-task` child was asserted in its instructions. The reviewer's no-write limit is enforced by its tool set.

## Containment

The branch changes only these files: the six files in the snapshot folder, plus `B4_SCA006_CHECKPOINT1.md` and `B4_VERIFIER_VERDICT_01..03.md` under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/`. The branch also merged `origin/main` `bec8bdd65`. The graph was not written.

## What the caller must resolve

1. **Present the package to the owner.** Ask for the checkpoint-1 decision; the question set is above. Only after acceptance does WORKING_ITEMS write the group-1 decision snapshot under `checkpoint_snapshots/` and prepare checkpoint 2.
2. **Basis drift.** The package was prepared at `13df8b795`, and the branch merged `bec8bdd65`. Only D-PEC-94 (the owner-confirmation section), `_REGISTER.md`, the work graph and STATUS/record files moved. The drift is recorded in IA §2.2 as not material.
3. **Work graph.** The graph (HELP_HUMAN-maintained) should record:
   - that R1's package is ready;
   - the proposed S4 set from IA §7.1;
   - that DEL-01-06 is not SCA-006-bound;
   - that the R4 Runtime notice should be named in the checkpoint-2 plan (the manager recommends it).
4. **Carried to checkpoint 2 or later.**
   - The tier-0 profile (`_DomainEngines/profiles/pec.yaml` L81) needs its own amendment before any PEC tool surface is declared or invoked.
   - The PROJECT_SETUP packet for DEL-08-06 and DEL-10-13.
   - The instruction-tranche manifest for the AGENTS.md change (INS-a); I1 may ride with it.
   - The supersession bindings SB-1..SB-6.
5. **Not verified here.** The manager's helper scripts and the child inventory live only in the scratchpad. A later reviewer re-checks by re-reading the cited lines, which IA Annex B lists.
