# Sealed Verifier Brief — T4 Adversarial Governed-Diff Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Posture:** fresh context; no shared authorship; read-only except the single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`; default `BLOCK` if uncertain.
- **Write scope:** exactly `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/RETURN_T4_GOVERNED_DIFF_1.md`.

## Scope under test

The staged diff (`git diff --cached`) against HEAD = commit `2a753e3fd` (T3 commit). This brief is the declared untracked addition besides your return.

## Claims to refute

1. **Whole-diff claim.** The staged diff touches only: the two new decision packets (D-APP-66, D-APP-67); `_REGISTER.md`; DEL-07-04 `_STATUS.md` + new `_run_records/TASK_RUN_2026-07-19_DAPP66_ruling_closure.md`; DEL-05-03 new `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md` + `_STATUS.md` + new `_run_records/TASK_RUN_2026-07-19_DAPP67_taxonomy_adoption.md`; run-directory files (`LAUNCH_BRIEF_PACKETS_T4.md`, `LAUNCH_BRIEF_ON_RULING_T4.md`, `RETURN_N8_PACKETS.md`, `RETURN_N9_ON_RULING.md`). **No file under `frontend/` changed** (the rulings authorize no code).
2. **Ruling fidelity.** Both packets carry §Human Ruling spans between the BEGIN/END OWNER RULING markers that are (a) byte-identical to each other, (b) byte-identical to Verbatim Block R in `LAUNCH_BRIEF_ON_RULING_T4.md` (fences stripped), and (c) hash (per the canonical convention: SHA-256 over UTF-8 bytes strictly between markers, excluding marker lines and delimiter newlines) to the recorded value `766058c8a5831859df867519ed3a19c3a5d91f00b16318401150322a4d134955` at 1332 bytes. Compute yourself with python3. The D-APP-66 packet Status records Option C; D-APP-67 records Option B; the dispositions match the selections (C = no code, checklist stays; B = committed-file taxonomy + quoting rule, runtime helper unchanged).
3. **Register discipline.** Exactly the two D-APP-66/67 rows changed, State AWAITING_RULING → RULED and Ruling-record cell only; 6-column shape preserved; every other row/byte identical to HEAD.
4. **Status-surface rules.** DEL-07-04 and DEL-05-03 `_STATUS.md`: each loses exactly its D-APP-53-Option-C deferred Remaining item and gains exactly one dated History line; every other Remaining item byte-intact; no Current State/lifecycle/`Last Updated`/`Checking Approval SHA` change.
5. **Taxonomy grounding.** In `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md`, spot-check 4 scanner citations (open `frontend/scripts/scan-secret-evidence.mjs` and confirm the cited line ranges support the stated rule); confirm Rule 4 states the runtime helper remains API-key-specific by ruling (no registry adopted) and no rule claims runtime behavior that does not exist; confirm the artifact contains no secret-shaped token and renders no acceptance/issuance.
6. **Consistency with the ruling.** Nothing in the diff implements Option A of either packet (no new error codes, no run-logger changes, no env-var registry); the DEL-07-04 run record states plainly that no code landed.
7. **Hygiene.** No credential material or unmarked `sk-ant-` continuation in the staged diff; repo-wide `python3 tools/practitioner_harness/harness.py self-check` exits 0 at the pinned baseline (INFO=15, NOT_APPLICABLE=2, REVIEW=33, WARN=6).

## Return format

`RETURN_T4_GOVERNED_DIFF_1.md`: verdict line first, then per-claim findings with evidence commands and observed values.
