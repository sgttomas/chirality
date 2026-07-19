# Sealed Verifier Brief — T1 Adversarial Governed-Diff Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Posture:** fresh context; no shared authorship; read-only except the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`; default to `BLOCK` if uncertain. Repo-relative paths only in the return.
- **Write scope:** exactly `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_T1_GOVERNED_DIFF_1.md`.

## Scope under test

The staged diff (`git diff --cached`) against `origin/main` = `24dc7bfb291996936de7a8af04b9cb9e74c6485a`. Your return file is the single declared post-check addition inside the run directory.

## Claims to refute

1. **Whole-diff claim.** The staged diff touches only: the run directory `execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/` (ORCHESTRATION_PLAN, LAUNCH_BRIEF_GOVERNED_WRITES_T1, RETURN_N1_GOVERNED_WRITES); the new packet `execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md`; `execution/_Coordination/_DECISIONS/_REGISTER.md`; DEL-04-01 `{_STATUS.md,_CONTEXT.md,ScopeOfWork.md}`; DEL-00-02 `{_STATUS.md,_CONTEXT.md,ScopeOfWork.md}`; DEL-01-01 `{_STATUS.md,_CONTEXT.md,ScopeOfWork.md}`; DEL-10-03 `{Dependencies.csv,_DEPENDENCIES.md,_STATUS.md}`. No other byte differs from `origin/main`; nothing under `_DomainEngines/`, `projects/chirality-piping/`, or `projects/pec/` is touched.
2. **Verbatim-binding fidelity.** The packet's §3 owner-ruling span (bytes strictly between `<!-- BEGIN OWNER RULING VERBATIM -->` and `<!-- END OWNER RULING VERBATIM -->`, excluding marker lines and delimiter newlines) hashes (SHA-256) to the value recorded beside it in the packet, and is byte-identical to Verbatim Block A in `LAUNCH_BRIEF_GOVERNED_WRITES_T1.md` (fences stripped). Same for the §2 accepted-basis span vs Block B and its recorded hash. Compute both yourself with python3.
3. **Register discipline.** Exactly one row (D-APP-65) was appended to `_REGISTER.md`; every pre-existing row and all non-table text is byte-identical to `origin/main`; the new row has exactly 6 columns and State RULED.
4. **Status-surface rules (F-APP-4).** In all four `_STATUS.md` diffs: no `Current State`, lifecycle, `Last Updated`, or `Checking Approval SHA` line changed; DEL-04-01 lost exactly its approving-role Remaining item (list now `- None.`); DEL-00-02 lost exactly its R4-P47 ResponsibleParty item; DEL-01-01 lost exactly its R4-P47 item while its R4-P48 docs item survives byte-intact; DEL-10-03 lost exactly its DEP-10-03-004 item while the open_pipe_stress transport item survives byte-intact; each gained exactly one dated History line.
5. **Dependency-register rules.** In DEL-10-03 `Dependencies.csv`, only row DEP-10-03-004 changed; the change is confined to the Notes cell (append-only — all prior note text preserved verbatim as a prefix) and `LastSeen` (→ 2026-07-18); `SatisfactionStatus` remains `PENDING`, `Status` remains `ACTIVE`; the header and all other rows are byte-identical; `python3 projects/chirality-app-dev/execution/_Scripts/validate_dependencies.py` passes on the file (run it yourself).
6. **Truthful attribution / no forbidden effect.** The packet and every kit edit record the owner's act as acceptance of agent-presented recommendations (with the structured-question selections labeled as owner selections over agent-drafted prompts); role/ResponsibleParty assignments carry the explicit statement that no adoption verdict, acceptance, issuance, or sign-off is rendered; the DEP-10-03-004 annotation keeps the row PENDING and reaffirms F-APP-3; no document claims a lifecycle transition, release, or issuance.
7. **Hygiene.** No staged file contains credential material or the unmarked synthetic-token prefix pattern (`sk-ant-` followed by anything other than a fixture-marked test string); repo-wide `python3 tools/practitioner_harness/harness.py self-check` exits 0 at the pinned baseline (INFO=15, NOT_APPLICABLE=2, REVIEW=33, WARN=6) with no new GEN8 entries introduced by this diff.

## Return format

`RETURN_T1_GOVERNED_DIFF_1.md`: verdict line first (`COMMIT-SAFE` or `BLOCK`), then per-claim findings with the evidence commands you ran and observed values.
