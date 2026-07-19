# TASK RUN — D-APP-68 DEL-04-01 Adoption Verdict (2026-07-19)

- **RunID:** `APPDEV_LOOP_2026-07-19_CONCORDANCE_RULINGS`
- **Instance:** `WI-PKG04`
- **Role:** WORKING_ITEMS (Agent 1), PKG-04 only
- **Basis:** `96563e8e09b89908e13e6b2f1f1139aca3283855`
- **Authority:** D-APP-68 recommendation 8, executing the owner ruling “I
  approve recommendations 1–8.”
- **Manifest slice:** 7 exact paths, SHA-256
  `27cab26e3b84d1971c6ba7541010c9849b4add9493d415b332a5165dc74e0cb0`
- **Outcome:** ACCEPT candidate for HELP_HUMAN fan-in; no lifecycle transition.

## Governed Result

The owner verdict is rendered as `ADOPT_WITH_RESIDUAL_RISK` for this
repository's demonstrator, pinned to
`@anthropic-ai/claude-agent-sdk@0.3.150` and observed Claude Code `2.1.150`.
`Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` assesses all twelve
DEL-04-01-REQ-015 categories and records bounded fallback triggers.

The decision consumes the D-APP-52 live probe without broadening it. The
development probe observed the live message sequence, version, session IDs,
controlled transcript placement, error shapes, and abort behavior. The
packaged proof observed the SDK-backed Read turn and platform binary under
`app.asar.unpacked`. RATE_LIMITED was not live-triggered. Signing,
notarization, publication, distribution, release readiness, and non-macOS-arm64
platform behavior remain outside the evidence.

## Twelve-Area Census

1. SDK API drift.
2. Settings leakage.
3. Allowed-tools misconception.
4. Transcript location.
5. Electron packaging.
6. SDK security boundary.
7. Subagent inherited permissions.
8. Session-mirror reliability.
9. Product-identity drift.
10. Platform dependency.
11. Reliance-boundary ambiguity.
12. Engine-adapter lock-in.

Each appears exactly once as a numbered assessment row in the decision record,
with evidence and a required `ADOPT_WITH_RESIDUAL_RISK` disposition.

## Exact Changed Paths

1. `Decision_Version_Pinned_SDK_Adoption_2026-07-19.md` — new pinned decision,
   live-evidence boundary, twelve assessments, fallback triggers, and explicit
   non-release/non-professional limits.
2. `ScopeOfWork.md` — current adoption-TBD slots reconciled to D-APP-68 while
   D-APP-65 pre-ruling state remains dated history; new CLM-031 records the
   current verdict.
3. `Evidence_CODEV-001_SDK_Probe_Record.md` — append-only supersession note
   points the stale subprocess-version and interrupt `BLOCKED_TBD` cells to
   D-APP-52 live evidence; historical observations are untouched.
4. `_CONTEXT.md` — appended D-APP-68 verdict and demonstrator/non-release
   boundary; `ResponsibleParty: TBD` preserved.
5. `MEMORY.md` — appended current memory note.
6. `_STATUS.md` — one dated History line only.
7. `_run_records/TASK_RUN_2026-07-19_DAPP68_adoption_verdict.md` — this record.

## Read-Only Evidence Integrity

The three manifest-fenced D-APP-52 evidence files remained byte-identical:

| File | SHA-256 |
|---|---|
| `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` | `65f912fbde8a996e3b1d12532a556a5b7a217692ca54e84029228fdb0bd3d747` |
| `Evidence_DAPP52_LIVE_PROBE_2026-07-18_summary.json` | `be155013371f51c1a52a364d19d9f164f9f2509bd921ca4d1af7b00b25a11686` |
| `Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` | `ac3507b043e5470a7ec16afebdf205e59f6b631b6ada552e44941fd603945e78` |

## Validation

- SOW-v1 validator: PASS.
- Exact SDK/Claude Code pins, twelve-row census, fallback section, and explicit
  non-release/non-professional boundary search: PASS.
- D-APP-68, D-APP-52, D-APP-65, D-GOV-14, reliance/product-boundary, runtime,
  and `AgentEnginePort` citation-path existence: PASS.
- `_STATUS.md` comparison against the basis: `Current State: IN_PROGRESS`,
  `Checking Approval SHA`, and the complete `Remaining` section byte-preserved;
  exactly one History line added: PASS.
- Read-only D-APP-52 evidence SHA-256 comparison: PASS.
- Authority corpus v9 status: no drift.
- App-dev receipt-contract validator: PASS.
- Seven-path manifest extraction/count/slice SHA, package-local changed-path
  allowlist, and exact new-path check: PASS.
- `git diff --check`: PASS.

## Preserved Exclusions and Handoff

No frontend source or test, dependency row, lifecycle state, Approval SHA,
another package, shared register, receipt, completion log, prior concordance
ledger, decomposition truth, or hard-fence surface changed. The decision makes
no release approval, issuance, certification, professional acceptance,
signing, notarization, publication, or external-distribution claim.

This package return is documentary fan-in evidence only. HELP_HUMAN remains
the next owner for cross-package acceptance and release of V1; CHANGE remains
the later Git publication owner.
