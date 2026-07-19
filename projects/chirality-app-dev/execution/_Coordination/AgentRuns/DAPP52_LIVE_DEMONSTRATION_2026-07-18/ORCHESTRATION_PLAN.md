# Orchestration Plan — D-APP-52 Live Demonstration (owner act) and Closures

- **RunID:** `DAPP52_LIVE_DEMONSTRATION_2026-07-18`
- **Orchestrator:** HELP_HUMAN (Agent 0), Claude Fable 5, this session
- **Authority:** the D-APP-52 ruling (O-A, riders 1–11) whose live-LLM
  demonstration was deferred key-absent at ruling; the owner act occurred
  in-session 2026-07-18 — the owner (Ryan Tufts, K-AUTH-1) directed
  "Proceed with the D-APP-52 live demonstration; I am at the screen." and
  supplied a short-lived API key for the purpose (direction recoverable from
  the session; transcribed in Receipt-71 as chat evidence). Agent selections
  inside the demonstration are exercises under the D-APP-64 reasoned-selection
  overlay, attributed in the run record's attribution blocks.
- **Base:** branch `claude/dapp52-live-demonstration` off `origin/main` =
  `a91f72b19aeb6dbca7e565fe336c91ce7e841421`; Step-0 battery green at start
  (receipt validator VALID through Receipt-70; corpus no drift; self-check at
  the re-pinned anchor).

## Live executions (performed by the orchestrator at the owner's screen)

| Pack | Driver | Result |
|---|---|---|
| Dev SDK probe (4 phases) | `frontend/scripts/run-dapp52-live-sdk-probe.mjs` (new) | PASS — live message sequence, error shapes, interrupt, transcript placement; redaction scan clean |
| Live-LLM pec demonstration | `frontend/scripts/run-dapp52-live-llm-demo.ts` (new) | PASS — model-driven propose/validate/refresh/validate on scratch pec (loopback :4909); no accept/apply act; force never used; DB deleted; redaction clean |
| Packaged live read-tool proof | `frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs` (existing) vs fresh `desktop:pack` bundle | PASS — Read tool + proof token observed; redaction clean |

Key handling: owner-supplied short-lived key held in a 0600 session-temp env
file outside the repo; reached the SDK only through its env option; every
pack secret-scanned; the key appears in no repo file and no artifact.

## Work graph

| Node | Role | Work |
|---|---|---|
| N1 GOV-WRITES | WORKING_ITEMS-posture child, sealed brief | Evidence files + summary artifacts into DEL-04-01 and DEL-10-03; dependency-row closures 007/011/013 + consumer mirrors; `_DEPENDENCIES.md` syncs; `_STATUS.md` Remaining updates; run record with rider check and D-APP-64 attribution blocks |
| N2 VERIFIER | fresh adversarial child, sealed refutation-only brief | Enumeration-derived claims over every governed artifact touched + evidence-fidelity + whole-diff claim |
| N3 CLOSEOUT | Agent 0 | Receipt-71, check battery, commit, PR; owner merge remains terminal |

## Node returns

- **N1 GOV-WRITES — RETURNED, complete, no deviations.** Evidence files +
  three byte-verbatim summary artifacts landed (SHA-256 recorded in the
  evidence MDs and the child return); five dependency rows closed SATISFIED
  with dated FACT notes; three `_DEPENDENCIES.md` syncs; two `_STATUS.md`
  Remaining discharges with History lines and no state/lifecycle/SHA change;
  run record with rider check and two D-APP-64 attribution blocks; dependency
  validator PASS on all three touched CSVs.
- **N2 VERIFIER — chain to `COMMIT-SAFE`.** RETURN_1: BLOCK on the
  committed-source hygiene claim only (unmarked synthetic-token template in
  the new probe driver; GEN8 pin exceedance incl. the pre-existing merged
  piping D-54 record); every evidence/closure/attribution claim held.
  Remediation: fixture-marked the driver template; conscious baseline re-pin
  (severity anchor and GEN8 set) with dated notes; disclosed run-record
  addendum. RETURN_2 and RETURN_3: remediation sound but each prior return's
  own verbatim quote of the unmarked token re-tripped the gate — each quote
  fixture-defused in place with a disclosed editorial note, preserved
  verdicts untouched. RETURN_4 (fresh terminal recheck): **COMMIT-SAFE** on
  all checks — secret scan zero blocked, pins pass, self-check exit zero,
  staged scope exact, substantive closures re-confirmed. All four returns
  preserved in this directory.
