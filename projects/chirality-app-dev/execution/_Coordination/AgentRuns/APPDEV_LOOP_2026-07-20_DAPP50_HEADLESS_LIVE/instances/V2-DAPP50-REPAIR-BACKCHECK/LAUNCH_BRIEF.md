# V2-DAPP50-REPAIR-BACKCHECK — EVALUATION Brief

## Frame and basis

- **Role:** fresh independent EVALUATION (Agent 1)
- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP50_HEADLESS_LIVE`
- **Branch/HEAD:** `codex/app-dev-dapp50-headless-live-20260720` /
  `fcf152bdae1e1764b11dfabf3f87d50c5680213d`
- **Commit chain:** G0 `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
  with parent `bc35e3b0049d990f494dd3610603be285c7aa9ed`; G1 is
  the two-path repair commit on G0
- **Authority:** D-APP-50 Option A and riders; D-APP-48 private pull contract;
  D-APP-53 residual routing; DEC-065 / TP-RUNNER-015 transport basis
- **Subject:** complete W1/G0 implementation, V1 findings, W3/G1 repair and
  cleanup, W2/W4 closeout, and Receipt-83/84 history
- **Decision criterion:** `ACCEPT` only if both V1 blockers are cured and the
  complete implementation, correction history, containment, and authority
  boundaries withstand adversarial backcheck
- **Scoring:** none
- **Delegation:** prohibited

Read full `AGENTS.md`, `agents/AGENT_EVALUATION.md`, all controls and terminal
records in this run, the complete V1 evaluation package, D-APP-50 packet/ruling,
D-APP-48 packet/contract, D-APP-53 packet, DEC-065 decision, TP-RUNNER-015,
DEL-10-01 status and both D-APP-50 run records, Receipt-83/84, both commits and
all implementation/test/docs they contain.

## Required evaluation

Independently attempt to refute:

1. Commit identity/topology and population: G0 exact 14 paths; G1 exact two
   repair paths and content hashes; no frontend source byte changed outside
   those commits; empty index and contained closeout/evaluation/control dirt.
2. V1 F-001 cure: the adapter fail-closes on the complete app-consumed DEC-065
   CLI result contract. Inspect exact top-level key set/identity, full policy,
   validation entries and diagnostic shapes/tokens, full runner-result nested
   structure/types/boundaries, unknown-key/padding rejection, and exit/diagnostic
   correlation. Test semantically meaningful malformed cases, not only fixture
   equality. Distinguish transport/result validation from an unclaimed
   exhaustive solver-semantic proof.
3. Original transport/security requirements: explicit absolute path plus exact
   SHA-256; realpath/regular-file/X_OK/hash immediately pre-spawn; shell-free
   direct `solve`; minimal environment; exact stdin; stdout-only JSON; timeout,
   reaping, separate 2 MiB caps, sanitized errors; runnerInputRef containment;
   exact profile/identity/registry gates and expected refusals.
4. Read-only/exclusive descriptor and normal permission/event/redaction/budget/
   evidence/artifact pipeline; no proposal/apply/accept, provider/network,
   output-path/sidecar, piping implementation, lifecycle, release, or
   professional/solver-truth expansion.
5. V1 F-002 cure: `projects/chirality-app-dev/frontend/dist` is absent; no
   material package/distribution artifact or relevant active process remains.
   Keep normal `.next` and `dist-electron` build outputs distinct. Do not clean.
6. Independently rerun the focused repaired suite (48 tests), generated catalog
   test, full frontend suite, typecheck, production build, managed premerge,
   pull-contract validator, dependency lint, receipt validator, authority
   corpus v9, repository self-check, validation pytest, and practitioner-harness
   pytest. Stop any server the evaluator itself owns. Do not package or release.
7. D-APP-48 exact final state: source pin is reachable G1; registry v14 and
   export hashes are byte-current; all other values/order and every false
   boundary flag preserved; strict duplicate-key JSON.
8. DEL-10-01 and history exactness: Remaining/lifecycle/Checking SHA preserved;
   W2 and W4 history lines/run records correctly distinguish initial closeout
   from repair; Receipt-83 prefix byte-identical; unique valid Receipt-84 with
   correct parent/cursor; decision register and unrelated deliverables unchanged.
9. Tracked/untracked/ignored/staged/cached/no-index/whitespace/write-scope
   containment, including proof that V2 changes only its evaluation root and
   terminal records.

## Outputs and write scope

Write exactly under:

- `projects/chirality-app-dev/execution/_Evaluation/DAPP50_HEADLESS_LIVE_REPAIR_BACKCHECK_FCF152B_2026-07-20/**`:
  `EVALUATION_PROTOCOL.md`, `FINDINGS.csv`, `EVALUATION_REPORT.md`, `HANDOFF.md`,
  and `MANIFEST.json`;
- this V2 instance: `RETURN.md`, `HANDOFF.md`, terminal `STATUS.json`.

Every other path is read-only. Do not delegate, repair, edit any receipt/status/
contract/source, stage, commit, push, open PR, merge, package, clean generated
state, or issue release/professional/solver-truth claims. Return terminal
`ACCEPT | BLOCK`, exact output hashes, coverage, findings/blockers/unknowns/
conflicts/waivers/reruns, subject-preservation proof, and final CHANGE only on
`ACCEPT`.
