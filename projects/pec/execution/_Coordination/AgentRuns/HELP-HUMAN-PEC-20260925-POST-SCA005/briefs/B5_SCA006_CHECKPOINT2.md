# Brief B5 — SCA-006 checkpoint-group-2 package (WORKING_ITEMS, scope-change workflow)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node R2. Role: WORKING_ITEMS (Type 1). Model steer: `claude-opus-5-5`, high reasoning, for you and your children.

**Authority.** The owner accepted SCA-006 checkpoint group 1 on 2026-09-25 with "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded". That acceptance authorizes preparing checkpoint 2.

**Stage.** Checkpoint group 2 preparation only (method parts A and B). Produce one complete reviewable package, have it independently verified, and stop. Do not apply anything.

## Method

`Workflow: chirality-root:bundled:workflow:scope-change`. Load `workflows/scope-change/WORKFLOW.md`, `resources/contract.md` and `resources/method.md`, and record their SHA-256.

Settings:
- Variant: `SOFTWARE`.
- `CONTEXT_ROOT = projects/pec/execution/`.
- `DECOMPOSITION_PATH = projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5).
- `SCOPE_CHANGE_ROOT = projects/pec/execution/_ScopeChange/`.
- `AMENDMENT_ID = SCA-006`.
- `ALLOW_RENUMBERING = false`.

Where the method is silent on form, mirror SCA-005's checkpoint-2 package (`_ScopeChange/SCA-005_2026-09-23_2139/`): `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, `PRD_V2_3_SUCCESSOR_DIFF.md`, `CP2_CANDIDATE/`.

## Accepted basis (read first; verify hashes; stop and report on any mismatch)

1. **The group-1 pointer and snapshot.**
   - `projects/pec/execution/_ScopeChange/SCA-006_GROUP-1_AUTHORIZED.md`.
   - `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`: `DECISION.md`, `ACCEPTED_MANIFEST.csv`, `Handoff_State.md`. Read in particular the baseline note and the carried items.
2. **The SCA-006 package** `_ScopeChange/SCA-006_2026-09-25_1912/`:
   - `Impact_Assessment.md` (accepted, `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691`);
   - `Amendment_Actions.csv` (accepted intake, `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891`);
   - `Brief.md`, `Pre_Change_Coverage.json`, `Decision_Log.md` and `Handoff_State.md`.
3. **The earlier run records:** `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B4_SCA006_CHECKPOINT1.md` and `B4_VERIFIER_VERDICT_0{1,2,3}.md`.
4. **Decisions:**
   - `_DECISIONS/D-PEC-90_*` (proposal and ruling; R-A grant, direct-query answer, clarifications) and `D-PEC-91` (the response-budget carry-forward and the 2^53−1 limiting-component rule);
   - `D-PEC-67` (the K03-A exact row coordinated with App) and the L-A1 reliance-hold control. That control stays distinct from operational reliance.
5. **Live canonical package:**
   - `execution/_Decomposition/` (revision 1.5, `SOFTWARE_DECOMP.md` `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`), its registers and `_LATEST.md`;
   - `docs/PRD.md` v2.3 (`fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`);
   - `_ScopeChange/_LATEST.md` (names SCA-005);
   - `projects/pec/AGENTS.md` (fences F-PEC-1..4; the K-02 gloss);
   - `docs/DECOMPOSITION_STANDARD.md`.
6. **The D-PEC-95 act** (PR #924, `abfd0897b`; run root `execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/`). It changed 119 derivative paths after the reused baseline audit. The package must state that Impact Assessment §2.1's byte-identity statement no longer holds exactly. It must also plan the checkpoint-3 audit so that the resolution of COV-068/069/072/073 is attributed to D-PEC-95, not SCA-006.
7. **The tier-0 profile** `pec.yaml` (find its path, for example under `_DomainEngines/`). Its L81, or the current equivalent, needs its own act before any PEC tool surface is declared or invoked. Read it and plan that act; do not write it.

## What the package must contain

The owner has already selected, and you apply exactly without re-asking:
- DQ-a (read-only `agent` access class);
- ENV-a (PEC-ORI-007 → SOW-097 → DEL-04-03);
- BUD-a (PEC-API-006 → SOW-098 → DEL-08-03, numbers at P1);
- GATE-a (a standing §12 gate, SOW-100, DEL-10-13; the §12 P1 row text is not edited);
- INS-a (the `AGENTS.md` change is an instruction tranche at checkpoint 3);
- R-C excluded.

**Part A — exact amendment.**
- `Amendment_Preview.md`: a diff-style preview across the method's semantic sections, with the full child closure for the added SOW-097..100, DEL-08-06 and DEL-10-13, and objective mappings that satisfy the union rule.
- Candidate postimages, not applied, under `SCA-006_2026-09-25_1912/CP2_CANDIDATE/`:
  - `_Decomposition/SOFTWARE_DECOMP.md` as revision 1.6;
  - every affected register;
  - `docs/PRD.md` as the v2.4 successor candidate;
  - `projects/pec/AGENTS.md` as the instruction candidate.

  Record the preimage and postimage SHA-256 of each.
- `PRD_V2_4_SUCCESSOR_DIFF.md`: section by section against v2.3, covering PEC-K-03, C3, §1.1, §8 (agents, the four access classes), §9 (PEC-ORI-007, PEC-API-006, PEC-API-007), §11 metric 4, the §12 standing gate and P3 row, §15, §16.6, and the header.
  - The exact prose must keep "non-authoritative" in the authority sense, and keep pull-oriented, consumer-owned use.
  - PEC-K-01/K-02, K-AUTH-1, D-GOV-01 and Root PRD N-1 stand.
  - Nothing may imply reliance is available before a release that passes the gate.
- `AGENTS_MD_CANDIDATE_DIFF.md` for the four `AGENTS.md` loci.
  - Name the instruction-tranche manifest that checkpoint 3 will write, and the notices it will send.
  - Say whether the work-graph node I1 residual corrections ride the same tranche. They are "Implementation does not exist yet" and the pre-v3 role names in `projects/pec/AGENTS.md`. If they ride, include them in the candidate, clearly separated.

**Part B — propagation plan.** Write `Propagation_Plan.md`, covering:
- **Per-action propagation.** ADD goes through preparation or PROJECT_SETUP for DEL-08-06 and DEL-10-13, as a later owner-ruled packet. MODIFY becomes `_CONTEXT.md` edits per deliverable.
- **The downstream rerun advisory:**
  - dependency extraction for the new deliverables and edges;
  - the SOW currency set, taken exactly from the accepted Impact Assessment §7.1 (the 9 AFFECTED), mapped to the work graph's S4 and D1 nodes;
  - the DEL-00-03 SPEC premise;
  - the four dependency EvidenceQuotes the Impact Assessment flags;
  - the tier-0 profile act;
  - the post-change audit plan.
- **Package-role classification** of every touched surface.
- **Derivative status** per package.
- **The closure validation lane.**
- **Foreign-surface notices.**
  - D-PEC-90 grants Root and App notices.
  - The checkpoint-1 manager recommended a Runtime notice too. State its basis, or recommend it as an owner question.

**Other outputs.**
- `Amendment_Actions_CP2.csv`: the exact final action register. Each row cites its intake Seq.
- `Supersession_Delta.csv`: the bindings SB-1..SB-6 from Impact Assessment §9.3, plus any others the exact text needs.

**Checkpoint-2 owner question set,** at the end of `Propagation_Plan.md`:
- accept the exact amendment and propagation plan together, citing the SHA-256 of every package file and postimage;
- only the choices that are genuinely still open, each with a recommendation.

Do not re-ask settled selections.

## Write boundary (only)

Work in your isolated worktree, on branch `claude/pec-sca006-cp2-package`, cut from fresh `origin/main` after PR #926 has merged.

Inside `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`, write only:
- the new files `Amendment_Preview.md`, `Propagation_Plan.md`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`, `PRD_V2_4_SUCCESSOR_DIFF.md`, `AGENTS_MD_CANDIDATE_DIFF.md` and `CP2_CANDIDATE/**`;
- additive updates to `Decision_Log.md`: the SCA006-CP2 row goes to `PREPARED / AWAITING_OWNER`, with the package hashes;
- additive updates to `Handoff_State.md`: a dated amendment section and the contract state fields.

Also write your return and verdicts: `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B5_SCA006_CHECKPOINT2.md` and `returns/B5_VERIFIER_VERDICT_NN.md`.

Do NOT modify:
- `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` or `Pre_Change_Coverage.json`;
- `checkpoint_snapshots/**`, any `*_AUTHORIZED.md` or `_ScopeChange/_LATEST.md`;
- the live decomposition or registers, `docs/PRD.md`, `projects/pec/AGENTS.md`, any SOW, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md` or `_DEPENDENCIES.md`;
- `v2/**`, `software-workflow.json`, the tier-0 profile, `loop/**`, `docs/STATUS.md`, `README.md`, `_DECISIONS/**`, the work graph, or any Root, sister or foreign path.

Commit your return to the branch before you hand back.

## Checks

Record each command, cwd, interpreter and exit code in `Handoff_State.md` and in your return:
- `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` on the live tree, and on a scratch copy with the candidate postimages in place;
- `tools/coordination/analyze_dep_closure.py` on the scratch copy, if the dependency registers change;
- the preimage hash checks;
- `validate_scope_change_packet.py`, if its schema fits; report if it does not;
- a parse check of both action CSVs against the contract;
- `validate_instruction_entrypoints.py` and `validate_instruction_tranche_manifest.py` on a scratch copy with the `AGENTS.md` candidate in place, if they apply to a candidate;
- the reliance-hold preflight (`pec_reliance_hold.py`, operation `exact-correction-preparation`) for the decomposition, the registers, `docs/PRD.md` and `projects/pec/AGENTS.md`;
- `git diff --check`;
- containment of `git diff --name-only origin/main` against the write boundary.

## Delegation and verification

You may dispatch bounded TASK children (`pec-task`, opus) for drafting in disjoint files, such as the PRD candidate, the register postimages and the `AGENTS.md` candidate. You integrate the results and own the package.

Before returning, dispatch one fresh read-only verifier (`pec-reviewer`, opus). It checks:
- every selection applied exactly and nothing unselected added;
- child closure, stable IDs and invariants, including the union rule;
- supersession bindings;
- the PRD candidate against D-PEC-90 R-A and its limits (authority stays file-native; no reliance before the gate; R-C excluded);
- the `AGENTS.md` candidate against Root governance and PEC's fences;
- the D-PEC-95 baseline statement;
- the write boundary.

Loop until nothing is blocking, and save each verdict. If CI shows "Update the PR base", report it; do not repair it.

## Publication

Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`. Do not merge. The PR publishes a candidate; it applies nothing.

## Return

- PR URL and head SHA.
- The package file list with SHA-256.
- Action counts: intake against CP2 final, with the delta explained.
- The counts that change.
- The Runtime-notice and I1 dispositions.
- The checkpoint-2 owner question set.
- Check results.
- Verifier verdicts.
- Containment.
- Anything unresolved.
- The delegation record.

## Limits

- No PRD, instruction, decomposition, SOW, pointer, access-class, tier-0 or `v2/**` application.
- No CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
- No foreign write.
