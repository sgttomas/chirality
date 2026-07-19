# TASK RUN — D-APP-52 Live-Demonstration Closures (2026-07-18)

RunID `DAPP52_LIVE_DEMONSTRATION_2026-07-18`; Agent 1 (WORKING_ITEMS
posture) executing a sealed brief from HELP_HUMAN as mechanical conformance;
branch `claude/dapp52-live-demonstration`.

## Basis

- Owner's in-session act 2026-07-18 (Ryan Tufts, owner at screen,
  short-lived owner-supplied key never persisted): execution of the live
  demonstration the D-APP-52 packet deferred.
- D-APP-52 ruling O-A riders 1–11.
- D-APP-64 reasoned-selection overlay
  (`execution/_Coordination/_DECISIONS/D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md`).
- Code SHA at capture `a91f72b19aeb6dbca7e565fe336c91ce7e841421`; model
  `claude-sonnet-5`.

## Packs and artifact SHA-256

| Pack | Script | Status | Repo artifact | SHA-256 |
|---|---|---|---|---|
| PACK1 dev SDK probe | `frontend/scripts/run-dapp52-live-sdk-probe.mjs` (new) | pass; redaction pass | `Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json` (this deliverable) | `be155013371f51c1a52a364d19d9f164f9f2509bd921ca4d1af7b00b25a11686` |
| PACK2 live-LLM pec demo | `frontend/scripts/run-dapp52-live-llm-demo.ts` (new) | pass; redaction pass | DEL-10-03 `Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18_summary.json` | `9286ad2bbc0bf3bc9c62c6a9b09dc089b217b7e449c7c166f9b4ea660bccd82f` |
| PACK3 packaged live proof | `frontend/scripts/run-live-packaged-agent-sdk-read-tool-proof.mjs` (existing, fresh `desktop:pack` bundle) | pass; redaction pass | `Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` (this deliverable) | `ac3507b043e5470a7ec16afebdf205e59f6b631b6ada552e44941fd603945e78` |

All three artifacts are byte-verbatim copies of the session-temp captures,
re-verified secret-free (`sk-ant-` absent) before and after copy.

## Closures performed

- `DEP-04-01-007` → SATISFIED (all four recorded needs stand; last residual
  — live Claude Code subprocess version 2.1.150 — live-confirmed;
  TargetLocation TBD resolved to `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`).
- `DEP-04-01-011` → SATISFIED (exact observed live `query()` message
  sequence recorded; Evidence_HANDOVER_CONSUMPTION section B basis stands).
- `DEP-04-01-013` → SATISFIED (live-confirmed error shapes AND packaged live
  behavior recorded; RATE_LIMITED not live-triggered; DEL-04-05 RQ-011
  four-class gap remains that deliverable's gated item).
- Consumer mirrors `DEP-04-03-007` and `DEP-04-05-007` → SATISFIED.
- Evidence narratives written: `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md`
  (this deliverable) and DEL-10-03
  `Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18.md`.
- `_DEPENDENCIES.md` tables synced in DEL-04-01 / DEL-04-03 / DEL-04-05;
  `_STATUS.md` Remaining items discharged in DEL-04-01 (two D-APP-52-gated
  items) and DEL-10-03 (live-LLM demonstration item); no `_STATUS.md` state
  or lifecycle change anywhere.

## D-APP-63 rider check

Performed: no DEL-04-04 (PersonaComposer / instruction-root)-relevant output
was produced by any pack — no new dependency row is minted; the retired
`DEP-04-01-012` stays retired.

## In-run fact

Model-id substitution: `claude-sonnet-4-20250514` returned a live 404 and
`claude-sonnet-5` was substituted for the captures. Recorded as an ordinary
in-run fact, not a separate D-APP-64 exercise.

## D-APP-64 attribution block 1 — evidence-home selection

```
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: deliverable-folder evidence homes (DEL-04-01 for PACK1/PACK3; DEL-10-03 for PACK2)
JudgedBy: HELP_HUMAN orchestrator, RunID DAPP52_LIVE_DEMONSTRATION_2026-07-18 (executed by Agent 1 GOV-WRITES child)
OwnerCaseSelection: NONE
RejectedAlternatives: pec-loop _DomainEngines/pec/ surface — F-APP-3 fence for this loop; the pec loop may mirror under its own authority
RationaleArtifact: this run record (_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md)
IndependentVerifier: NOT_REQUIRED per D-APP-60 calibration
EffectStatus: EFFECTIVE
PreservedGates: F-APP-3 (_DomainEngines/** untouched); no _STATUS state/lifecycle transitions; no receipts/register/frontend writes; no commit
```

## D-APP-64 attribution block 2 — full closure of DEP-04-01-013

```
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: full closure of DEP-04-01-013 after running the packaged proof (PACK3) against a fresh desktop:pack bundle, with the RATE_LIMITED non-trigger noted plainly
JudgedBy: HELP_HUMAN orchestrator, RunID DAPP52_LIVE_DEMONSTRATION_2026-07-18 (executed by Agent 1 GOV-WRITES child)
OwnerCaseSelection: NONE
RejectedAlternatives: narrowing the row to a packaged-live residual (unnecessary once the proof passed); closing without packaged evidence (would overstate)
RationaleArtifact: this run record (_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md)
IndependentVerifier: NOT_REQUIRED per D-APP-60 calibration
EffectStatus: EFFECTIVE
PreservedGates: D-APP-52 rider scope (no adoption verdict, release, or professional claim); DEL-04-05 RQ-011 gap left as that deliverable's gated item; no fabricated RATE_LIMITED shape
```

## Addendum — post-verification remediation (2026-07-18, orchestrator)

The adversarial verifier returned BLOCK on the committed-source hygiene claim
only (RETURN_GOVERNED_DIFF_1.md; all evidence/closure/attribution claims
held). Remediation, before any commit: (a) the probe driver's synthetic
invalid-key template now carries the secret scanner's sanctioned "fake"
fixture marker (`sk-ant-api03-fake-invalid-…`) — the committed driver differs
from the capture-time driver by that marker and its comment only; the
captured evidence is unchanged and never contained the synthetic value;
(b) the practitioner-harness live-baseline pins were consciously updated
(severity anchor and GEN8 set) for the two sealed briefs of this run and for
the merged chirality-piping D-54 record whose findings pre-existed this
tranche at its base (repair-first). A fresh verifier re-checked the
remediated tranche after this addendum was written.
