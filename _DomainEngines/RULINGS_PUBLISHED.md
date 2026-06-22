# RULINGS_PUBLISHED — Tier-0 Bridge (2026-06-21)

The owner ruled all 8 tier-0 decisions in-session on 2026-06-21. This file is the **green-light signal** the project loops watch (per `NEXT_INSTANCE_PROMPT.md`). Canonical per-decision records: `_DECISIONS/D-T0-01..08_*.md` + `_DECISIONS/_REGISTER.md`. **Rulings bind to a git SHA when CHANGE publishes** (K-AUTH-2); until then, `Ruling SHA: TBD`.

## The rulings

| ID | Ruling |
|---|---|
| D-T0-01 | **Framework-root persona canonical**, as **new framework policy**. Two-way merge to root: app-dev conforms DOWN; OperationProposal merges UP. |
| D-T0-02 | **Keep both** → 7-token `ProfileStatus` (FM-01). |
| D-T0-03 | **L3 is the destination**, reached **risk-graded per-operation**; L0→L1→L2→L3; L4 future-only. |
| D-T0-04 | **OPEN RESIDENCY** — agent may see the private model + Class-B inputs; the app does not enforce privacy; any provider (local/Anthropic/other). **L3 not residency-blocked.** |
| D-T0-05 | **Confirmed** G1–G5. |
| D-T0-06 | **Persona cadence**; `VALIDATED` gated on the TOOLMAKER profile-schema validator. |
| D-T0-07 | **tier-0-owned versioning** referencing both versions; **DEC-041 confirmed**. |
| D-T0-08 | **Sequential** Fence-3: source types → MCP tools, after D-T0-01 + proven L2. |

## What is now actionable, by owner — STILL GATED

**Tier-0 (DOMAIN_ENGINE → human-gated framework-maintenance pass → CHANGE):** FM-01..04 are now **authorized in direction** but remain **gated diffs to be applied by a HELPS_HUMANS/framework-maintenance pass and published by CHANGE** — not self-applied. Update the DRAFT profile per rulings.

**Tier-1 (app-dev loop):** may begin (1) PKG-10 re-draft to the ruled canon; (2) SHA-pin `AGENT_DOMAIN_ENGINE.md` into DEL-10-01/03 `_REFERENCES.md`; (3) flow-A tier-0 versioning; (4) ProfileStatus/OperationProposal conformance. **Subject to its own fences + the RES-RECONCILE item below.** Tier-0 does not author this slice.

**Tier-2 (piping loop):** DEC-042-sanctioned prep only (validate-only trust-probe, surface-reconciliation, headless CLI entrypoint). **D-21 still held.**

## `RES-RECONCILE` — required follow-on from D-T0-04 (other loops own these)

The open-residency ruling **supersedes**, but tier-0 **cannot edit**, two working-root fences. Their loops must reconcile them to the ruling:
- **app-dev fence F1** (provider/network beyond Anthropic; PRD `FR-089`/`FR-125` P0 deny) → app-dev loop amends/repositions F1.
- **piping `OPS-K-PRIV-1` + no-required-network + `IP_AND_DATA_BOUNDARY`** → piping loop reconciles its privacy posture.

Until reconciled, those fences and this ruling **conflict on record** (surfaced, not silently resolved — K-CONFLICT-1). Live binding must not proceed against an unreconciled fence.

## Still gating the LIVE build (unchanged by these rulings)

The 4 asymmetric conditions still hold: **tier-0 adoption** (in progress) · **app-dev F3** · **piping D-21** · **DEC-041 automation condition**. Residency is no longer a 5th blocker.

## Next

DOMAIN_ENGINE: update the DRAFT profile, hand FM-01..04 + the two TOOLMAKER briefs to the owner-chosen workflows, and hand the `_DomainEngines/` file list to CHANGE (commit-note proposal in `bridge/.../Handoff_State.md`). Profile remains **DRAFT** (not VALIDATED — validator not built; D-T0-06) and **not ADOPTED**.
