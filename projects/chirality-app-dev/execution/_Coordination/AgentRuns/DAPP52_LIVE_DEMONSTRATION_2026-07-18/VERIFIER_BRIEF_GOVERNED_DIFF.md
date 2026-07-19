# Sealed Verifier Brief — Adversarial Governed-Diff Verifier (refutation-only)

- **Parent:** HELP_HUMAN (Agent 0), RunID `DAPP52_LIVE_DEMONSTRATION_2026-07-18`
- **Posture:** fresh context; no shared authorship; read-only except the
  single return file; sole deliverable `COMMIT-SAFE` or `BLOCK`; default to
  `BLOCK` if uncertain. Use repo-relative paths only in the return.
- **Write scope:** exactly
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/DAPP52_LIVE_DEMONSTRATION_2026-07-18/RETURN_GOVERNED_DIFF_1.md`.

## Scope under test

The staged diff (`git diff --cached`) against `origin/main` =
`a91f72b19aeb6dbca7e565fe336c91ce7e841421`. The loop receipt (Receipt-71) is
appended after this verification by declared convention; your return file is
the single declared post-check addition inside the run directory.

Per the NM-5 rule, claims derive from the D-APP-60 governed-artifact
enumeration for every governed artifact the diff touches.

## Claims to refute

1. **Whole-diff claim.** The staged diff touches only: the run directory
   `execution/_Coordination/AgentRuns/DAPP52_LIVE_DEMONSTRATION_2026-07-18/`;
   two new frontend driver scripts (`frontend/scripts/run-dapp52-live-sdk-probe.mjs`,
   `frontend/scripts/run-dapp52-live-llm-demo.ts`); DEL-04-01 files
   (`Dependencies.csv`, `_DEPENDENCIES.md`, `_STATUS.md`, two new evidence
   JSONs, one new evidence MD, one new run record); DEL-04-03 and DEL-04-05
   (`Dependencies.csv` + `_DEPENDENCIES.md` each); DEL-10-03 (`_STATUS.md`,
   one new evidence JSON, one new evidence MD). No other byte differs from
   `origin/main`; nothing under `_DomainEngines/`, `projects/chirality-piping/`,
   or `projects/pec/` is touched.
2. **Dependency-register rules.** In the three touched `Dependencies.csv`
   files, exactly rows DEP-04-01-007/011/013, DEP-04-03-007, DEP-04-05-007
   changed; each moved `TBD → SATISFIED` (with `SEMANTIC_READY` proposed
   maturity) via appended dated FACT notes; no other row or header changed;
   `python3 projects/chirality-app-dev/execution/_Scripts/validate_dependencies.py`
   passes on each file (run it yourself, one CSV per invocation).
3. **Status-surface rules.** In both `_STATUS.md` diffs: no `Current State`,
   lifecycle, or `Checking Approval SHA` line changed; DEL-04-01 lost exactly
   its two D-APP-52-gated Remaining items and gained one dated History line;
   DEL-10-03 lost exactly the live-LLM-demonstration Remaining item and
   gained one dated History line; every other Remaining item is byte-intact.
4. **Evidence fidelity.** The three staged evidence JSONs are byte-identical
   to their session-temp sources under
   `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-help-human-agent-setup-b9bff5/fb6fcf91-eadf-42ba-bf6b-7921bf796aa0/scratchpad/`
   (`dapp52-live-sdk-probe/summary.json`, `dapp52-packaged-live-proof/summary.json`,
   `dapp52-live-llm-demo/summary.json`); each JSON records `"status": "pass"`
   and a passing redaction block; every factual claim in the two evidence MDs
   and the run record that cites a pack (versions, message sequences, error
   shapes, proposal ids/versions, resultSemantics, teardown, absence of
   accept/apply/force) is supported by the corresponding JSON content —
   spot-check at least: claudeCodeVersion 2.1.150; the phase-1 sequence and
   result top-level keys; the 401 error-shape text; proposalId 1 with version
   2 → 4; the resultSemantics string; `demoCastActs` NONE.
5. **Secret hygiene.** No staged file contains the substring `sk-ant-` or any
   credential material; the staged diff introduces no absolute-path GEN8
   regression beyond the pinned set (run
   `python3 tools/practitioner_harness/harness.py self-check` and confirm exit
   zero with the pinned anchor; run the frontend secret scan
   `npm run proof:secret-scan` from `projects/chirality-app-dev/frontend/` and
   report its verdict).
6. **Truthful attribution.** The run record's two D-APP-64 attribution blocks
   mark the selections as agent judgment (`OwnerCaseSelection: NONE`); the
   owner's act is recorded only as the in-session demonstration direction and
   key supply; no document claims an owner ruling that did not occur, no
   lifecycle/adoption/release/professional claim is made, and the RATE_LIMITED
   non-trigger is stated rather than papered over.

## Return format

`RETURN_GOVERNED_DIFF_1.md`: verdict line first, then per-claim findings with
evidence commands and observed values.
