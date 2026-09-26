# B5 verifier verdict 01 — SCA-006 checkpoint-2 package

Reviewer: a fresh `pec-reviewer` (read-only TASK; Claude Code Agent tool, `model: opus`, host-mapped to claude-opus-5-5), dispatched by the B5 WORKING_ITEMS manager.
- Brief: `BRIEF_V_VERIFIER.md` (session scratchpad), SHA-256 `f319a23973833c12b1e9373abc478554939f8d21ed3d223dfe57d0fec0fd25b4`.
- Candidate: `87a3f29b76635938db7a35ad2226d1db1468ab33`.

The manager transcribed the verdict below verbatim from the reviewer's hand-back. The manager's dispositions follow it.

---

**Verdict: PASS WITH MINOR.** Nothing is blocking. There are 3 MINOR findings and 5 NOTEs.

Candidate: branch `claude/pec-sca006-cp2-package` at `87a3f29b76635938db7a35ad2226d1db1468ab33`. The pushed remote head equals it, and the worktree is clean. The brief `BRIEF_V_VERIFIER.md` hashes to `f319a239…fd25b4` and B5 to `142d6be0…abefb4`, both as quoted. I claim no owner act.

## Checks

1. **Selections applied exactly — PASS.**
   - DQ-a: the four access classes and the read-only `agent` class appear in PRD §8, SOW-003 and DEL-08-01.
   - ENV-a: PEC-ORI-007 → SOW-097 → DEL-04-03.
   - BUD-a: PEC-API-006 → SOW-098 → DEL-08-03, with numbers at P1.
   - GATE-a: a new §12 paragraph, SOW-100 and DEL-10-13. The P1 row is byte-identical in the diff.
   - INS-a: `AGENTS.md` changes apply only through the checkpoint-3 tranche.
   - R-C: no text makes PEC citable as authority.
   - Every PRD hunk H-01..H-17 maps to Seq 1–13. Every decomposition hunk maps to Seq 18–43.
   - The listed "pure mirrors" are legitimate: the §1.2 gate and P3 lines, the §3 intro, the `orientation` vocabulary row, the §2 intro, §1.5 R1, and the DEL-08-03/08-06 QA cells. So are the DecisionRef traceability suffixes, which follow the existing `"; "` convention.
   - No change lacks a covering Seq.
2. **Child closure, stable IDs and invariants — PASS.** Recomputed from the candidate CSVs:
   - 100 scope items (74 IN / 18 OUT / 8 TBD);
   - 68 deliverables (64 active / 4 retired) and 68 ContextBudgetQA rows;
   - active envelopes S 28 / M 34 / L 2;
   - PKG-04 / 08 / 10 assigned scope 7 / 8 / 13.

   The union rule holds on 64/64 active rows. Back-references and package membership are consistent. No IN item lacks a package, deliverable or objective, and every active deliverable has an objective. There are 29 vocabulary terms and 13 issues (10 open / 3 resolved). No ID is removed, reused or renumbered. Row order and columns are preserved. The OBJ-001/002 views match the ledger.
3. **Supersession bindings — PASS, with MINOR-2.** SB-1..SB-6 map to D-001/002/003/018/005–008/011. The seven added rows are justified. The 16 YES rows equal the 16 `Supersession_Delta.csv` DecisionIDs. Preimage quotes are exact, except the elided D-021 and D-022.
4. **PRD candidate against D-PEC-90 R-A and its limits — PASS.**
   - Every "operational reliance" is gated on the §12 gate.
   - "Non-authoritative" is kept and defined in the authority sense. Pull-oriented, consumer-owned use is kept.
   - The K-01, K-02 and K-11 rows are byte-identical. §16.6 stays open, and includes agent credentials.
   - Every section the brief requires is covered. C3 is in `Amendment_Preview.md` §A-18.
5. **`AGENTS.md` candidates — PASS, with MINOR-3.**
   - Only the four SCA-006 loci change, plus I1 in the with-I1 candidate. Fences, frozen corpus, write scopes, reliance holds and the other eight checks rows are byte-identical.
   - I1 is cleanly separated: the diff from without-I1 to with-I1 contains only I1 hunks.
   - I1 is true at `7f33b4dd5` and still true at the new `origin/main` `283835358`: `legacy.retiredRoles` matches; `software-repository-reconnaissance` and `software-test-planning` are workflows; `software-code-review` and `software-defect-diagnosis` are skills; `software-bounded-implementation` is historical-only; `chirality-change` is a project skill.
   - The manifest draft (`852b1d5b`) and the Root, App and Runtime notices (`43cfa318`, `eb927e1f`, `385e5e2f`) hash as quoted and name their basis.
   - The Runtime-notice basis is true: DEL-02-06 `ScopeOfWork.md` L459–461 and `SOURCE_PINS.json` S4, S5 and S6 pin `projects/pec/AGENTS.md`, `Deliverables.csv` and `ScopeLedger.csv`.
6. **D-PEC-95 baseline — PASS.**
   - The statement appears in `Amendment_Preview.md` §13, `Propagation_Plan.md` §"Basis currency since checkpoint 1" and `Handoff_State.md`.
   - The 119 paths are confirmed by the D-PEC-95 ruling.
   - `git diff 13df8b795 4d5f7b911` shows only the claimed three-file drift.
   - COV-068/069/072/073 are in the baseline IssueLog.
7. **Propagation plan — PASS.**
   - Every Part B item is present.
   - The 9 AFFECTED contracts of §7.1 map to S4/D1, with the conservative hold matching `WORK_GRAPH.md` S4.
   - The only open questions are Q-CP2-A, Q-CP2-1 and Q-CP2-2. No settled selection is re-asked, and there is no CHECKING question.
8. **Hash integrity — PASS.** Everything matches:
   - all 14 package and postimage hashes;
   - all live preimages, including the PRD `fff27a66`, `AGENTS.md` `c9d3b44d`, both `_LATEST.md` files, `pec.yaml` `6858d567` and the three A2 `_CONTEXT.md` files;
   - the three A2 postimages, recomputed by applying the plan's diffs (`b28ada46`, `74b12e73`, `95fa815a`);
   - the pre-acceptance variant `3ad0de68`;
   - the SOW and SPEC hashes in §B4 and §B5, the child briefs, and every quoted proof-script hash.
9. **Write boundary — PASS, with a NOTE.**
   - `git diff --name-only origin/main...HEAD` lists only the 16 allowed files inside the SCA-006 folder.
   - `Impact_Assessment.md`, `Amendment_Actions.csv`, `Brief.md` and `Pre_Change_Coverage.json` equal their accepted hashes.
   - `Handoff_State.md` is append-only.

## Findings

1. **MINOR.** `Amendment_Preview.md` L65 says "Each row's Description states its exact text". Several rows of `Amendment_Actions_CP2.csv` still carry intake prose that no longer matches the candidate:
   - L4 (Seq 3) keeps "DQ-b instead states … DQ-c leaves …".
   - L27 (Seq 26) keeps "Under DQ-c this row is TBD with new OI-014 instead".
   - L33 (Seq 32) keeps "S -> M recommended".
   - L25 (Seq 24) quotes the intake SOW-097 wording rather than the candidate bytes ("pin (examined-through SHA), per-feed coverage and freshness with stated limitations, …"). Seq 38 has the same problem.
   - L55 (Seq 54) calls Propagation Plan section B3 a "graph node".

   Each row's "Exact text:" pointer reaches the exact text, so this is not blocking. Repair:
   - remove the clauses for unselected options and the word "recommended";
   - quote the candidate text for Seq 24 and Seq 38;
   - reword the preview sentence to "states its scope and points to its exact text".
2. **MINOR.** Some `Supersession_Delta.csv` rows are not full exact statements.
   - L16 (D-021) and L17 (D-022) elide their `SupersededFactTextOrValue` with "...". The contract (`resources/contract.md` L400) calls for "the original authority value or statement".
   - Several `ReplacementFactTextOrValue` cells paraphrase the candidate. L3 (D-002) drops "and no agent, harness or loop is required to query PEC (PEC-K-01, PEC-K-11)". L4 (D-003) and L13 (D-014) are abbreviated.

   The accumulator will carry these forms into `Supersession_Map.csv`. Repair: use the full preimage and candidate strings, or state in Notes that the value is an excerpt.
3. **MINOR.** The `AGENTS.md` lineage has no D-PEC number for SCA-006, although Q-CP2-2 (a) would create one.
   - Product Posture (`AGENTS.candidate.md` L32–34; without-I1 L32–34) names SCA-005's adoption "under `D-PEC-92`" but gives SCA-006's adoption no D-PEC number.
   - Governance Pointers (L207–209; without-I1 L201–203) is a list of D-PEC register rows, and the new item names none.
   - Q-CP2-2 (a) recommends a new D-PEC register row, and the byte-fixed candidate has no slot for its number.

   Repair: add a D-PEC number slot to AGENTS §9 and to both candidates, or record the omission as deliberate.
4. **NOTE.** `Decision_Log.md` L6 changes the front-matter `status:` in place, outside the SCA006-CP2 row the brief names. This is state bookkeeping, but it is not strictly additive.
5. **NOTE.** `origin/main` has moved to `283835358` (PR #931, the wave-2a closure: workflows, `index.json` and a PEC notice). No PEC preimage changed, and the I1 facts hold there. The branch is now behind main, so CI may show "Update the PR base"; report that, do not repair it. No PR exists yet for this branch.
6. **NOTE.** The PRD PEC-API-007 row adds a tier-0 obligation: "Before any such tool is declared or invoked, the PEC Domain Engine Profile … is amended". This comes from the Seq 26/SOW-099 notes, not from the Seq 7 description. It is consistent with `pec.yaml` L14 and L81, and it grants nothing.
7. **NOTE.** The proof scripts live only in the session scratchpad. The diff documents stay mechanically re-provable from the repository alone. Consider preserving the scripts with the checkpoint-3 evidence.
8. **NOTE.** Whether Root `AGENTS.md` L54–55 is compatible with post-gate operational reliance remains for Root to confirm. The Root notice routes that question correctly and claims no confirmation.

## What I ran

Interpreter: Python 3.13.7.

- **Hashing and reading (all exit 0).**
  - `shasum -a 256` over the brief, B5, CANON, every package file, the preimages, the basis records, the proof scripts, and the Runtime `ScopeOfWork.md` and `SOURCE_PINS.json`.
  - `git` from the worktree: `fetch origin main`; three-dot and two-dot `diff --name-only`; `diff --check origin/main...HEAD` (clean); `ls-remote`.
- **Proof and parse scripts.**
  - `python3 prove_preview.py` (cwd `B5/decomp`): exit 0; 43 hunks and 17 register rows; no errors. It rewrote the scratch `proof_result.json`.
  - `python3 prove_diff.py` (cwd `B5/prd`): exit 0; 17 hunks, byte for byte.
  - `python3 check_csv.py <package>` (cwd `B5/mgr`): exit 0.
- **Validators on the live tree (cwd repo root).**
  - `validate_decomposition_registers.py --strict`: exit 0, 0/0.
  - `validate_instruction_entrypoints.py .`: exit 0.
  - `validate_instruction_tranche_manifest.py`: exit 0.
  - `validate_pec_loop_receipts.py --repo-root .`: exit 0.
  - `validate_scope_change_packet.py`: exit 1 as expected, because the schema does not fit this packet.
- **`pec_reliance_hold.py`** (cwd `projects/pec`): ALLOW, exit 0, for all 8 targets. That is `exact-correction-preparation` for the decomposition, its 4 registers, the PRD and `AGENTS.md`, and `candidate-validation` for the package.
- **Scratch overlay** under `scratchpad/verifier_v/`, outside the repository.
  - `validate_decomposition_registers.py --strict`: exit 1 by design; 0 ERROR and 2 WARNING (DRB-008 for DEL-08-06 and DEL-10-13).
  - `analyze_dep_closure.py`: exit 0; COMPLETE/PASS; 263 rows; 0 SCCs.
  - `validate_instruction_entrypoints.py` on a light copy with the preimage, the without-I1 candidate and the with-I1 candidate: exit 0 each time.
- **Read-only ad-hoc Python recomputations:** register invariants and the union rule; the EvidenceQuote break scan (exactly DEP-09-06-003 and DEP-10-03-003 break); the A2 postimages; the pre-acceptance hash; the extraction hashes of the manifest and notices; the `workflows/index.json` facts at both main heads.

No Git state changed, and I wrote no repository file. My only writes were scratch copies under `scratchpad/verifier_v/` and the proof script's rewrite of `B5/decomp/proof_result.json`.

---

## Manager dispositions (B5 WORKING_ITEMS)

| Finding | Disposition |
|---|---|
| 1 (MINOR) | **Repaired.** `Amendment_Actions_CP2.csv` Descriptions are regenerated:<br>• unselected-option clauses (DQ-b/DQ-c/ENV-b/BUD-b/GATE-b) and "recommended" are removed;<br>• Seq 24–27 and Seq 38–40 quote the candidate text;<br>• Seq 54 says "Propagation_Plan.md §B3".<br>The preview sentence now reads "states its scope and points to its exact text". |
| 2 (MINOR) | **Repaired.** `Supersession_Delta.csv` rows D-021 and D-022 carry the full preimage statements. D-002, D-003 and D-014 carry the full candidate strings. Every `Replacement` cell that remains an excerpt says so in Notes. |
| 3 (MINOR) | **Recorded as deliberate; no candidate change.** At preparation time no D-PEC number exists for the checkpoint-2 act, and the canon forbids naming one that does not exist. The candidates cite the group-2 snapshot folder instead, and a D-PEC register row under Q-CP2-2 (a) points to that folder. This follows the D-PEC-92 pattern, where the register row points to the snapshot. `Propagation_Plan.md` §A4 now states that the checkpoint-3 tranche may add the register-row number as a lineage completion only if the owner's checkpoint-2 act directs it; otherwise the folder citation stands. |
| 4 (NOTE) | **Kept.** The front-matter `status:` is the log's state field, updated as SCA-005's log was at the same stage; row content is additive. |
| 5 (NOTE) | **Noted.** Not merged; reported to HELP_HUMAN if CI asks for a base update. |
| 6 (NOTE) | **Noted.** The PRD diff §3 attributes it to Seq 7 with the SOW-099 notes as its source; it grants nothing. |
| 7 (NOTE) | **Carried** to the checkpoint-3 brief as a recommendation, in the return. |
| 8 (NOTE) | **Agreed.** |
