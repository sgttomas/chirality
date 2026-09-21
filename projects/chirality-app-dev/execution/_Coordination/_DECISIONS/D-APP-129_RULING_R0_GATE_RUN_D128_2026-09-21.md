# D-APP-129 Ruling: RUN_D128 R0 gate (conventions, done declaration, scale-out, scope extension)

**Status:** RULED
**Date:** 2026-09-21
**Decision ID:** D-APP-129
**RuledBy:** Ryan Tufts (owner), in-session direction to the HELP_HUMAN (Agent 0) session on 2026-09-21
**Run:** `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/`, activated by D-APP-128
**Decision basis (packet equivalent):**
- `…/R0_CALIBRATION/R0_CALIBRATION_REPORT.md` (SHA-256 `2e3554eb87972481b32627c019f1f2d290b109c2c7e699a745a3d815e4341361`), with `VERIFICATION.md` and `DOUBLE_BLIND_COMPARISON.md` beside it;
- `…/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` (SHA-256 `42f5f60a7fd5f69d69599ae4f8fac31897f2d0ab925b2e0036a45934e3c9eab5`);
- the gate slate HELP_HUMAN presented in session, items A–C and the later scope-extension proposal.

**Structural precedent:** the D-APP-55 R0 gate (loop Receipt 16), here recorded as its own register row.

## Ruling basis

The owner's words, verbatim, as recorded with SHA-256 in
`execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/OWNER_DIRECTION.md`:

> Add items 3-7 in the manner you indicated.  R0 gate: A as recommended; B option 2; C as recommended

The SHA-256 of this text is `0f41325e1a73a617efab38aa9d017350cda5913b6947826d4aff00db3ae9fea0`.

The owner then answered the structured question "Which governance items join the scope
extension alongside items 3-7?" with:

> Neither

The SHA-256 of this answer is `9957d09c21ebc6cad181d56bc43cbd9bde18999c98bd708a416c29fcd3705b7f`.

This record transcribes those directions and does not broaden them (K-AUTH-1; D-GOV-04).

## Recorded outcome

- **A. Conventions: as recommended.**
  - Every verdict in calibration report §7 (tables 7.1 and 7.2) is adopted as written:
    - `ADOPT` keeps the candidate rule;
    - `REVISE` replaces it with, or adds, the stated text;
    - no rule was marked `DROP`.
  - This includes MR-1..MR-11 as revised, and the new disposition `RETIRED_BY_RULING`.
  - It also includes these tags and files: the reachability tag `REACH=LIVE|LEGACY_ONLY|TEST_ONLY`, `_errata.csv` for pass-2 corrections, `CTX:`/`GOV:` DirectionEvidence prefixes, the tightened AuthorityTier and CauseTag rules, and the frozen-basis gate transcripts in place of MR-3.
  - The integrated rulebook is `…/CONVENTIONS.md`. `CONVENTIONS_CANDIDATE.md` stays as the R0 historical edition.
- **B. Done declaration: option 2.**
  - D-APP-128 ruling §5.5.3 required the owner's confirmation of the v3 done declaration
    before R2. **This ruling amends that requirement.**
  - R2 proceeds with the candidate as CONTEXT only.
  - Its 13 questions (Q-01..Q-13) are carried to R4 for ruling.
- **C. Scale-out: as recommended.** R2 runs:
  - with one WORKING_ITEMS manager per package;
  - with at most 3 managers concurrently, each with at most 4 concurrent children, so
    at most 16 agents including HELP_HUMAN;
  - with a per-manager evidence pack;
  - after the remaining 10 reverse-pass code areas, which run first under their own
    manager;
  - with one double-blind deliverable per wave.
  - **Package order:**
    1. PKG-04, 06, 08, 10 (the legacy-harness cluster);
    2. PKG-03, 05;
    3. PKG-02, 07;
    4. PKG-00, 01;
    5. PKG-09.
  - **Named R4 questions.** Three early findings become named questions that ledger rows
    cite in `HumanDecisionNeeded`. They are ruled at R4, not before R2:
    - `R4-Q1`: is the retained legacy in-process harness history, compatibility or
      obligation, given that K-PATH, K-ROOT, K-HOOK and SPEC §15.2 were not amended for
      D-GOV-43?
    - `R4-Q2`: the Codex engine has not been run through the K-ENGINE-2 conformance suite.
    - `R4-Q3`: the legacy `status_transition` tool accepts an actor string supplied by the
      agent itself.
- **D. Scope extension (items 3–7, "in the manner you indicated").**
  - The run's audit scope widens beyond the 54 deliverables to five surfaces:

    | Item | Surface | What is audited |
    |---|---|---|
    | 3 | Every `RULED` register row D-APP-86..D-APP-127 | Whether each ruling's stated effect landed in code or corpus |
    | 4 | `docs/BUILD_AND_RELEASE.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_RUNBOOK.md`, `docs/harness/reliance_boundary_register.md` | Audited with the PKG-09 wave. The CI workflows and release run records serve as evidence only. |
    | 5 | The decomposition scope ledger (SOW rows) | Coverage and mapping |
    | 6 | `instructions/AGENTS.md` | Audit-only. Repairs route to Root per D-APP-128 packet Δ10. |
    | 7 | `frontend/docs/harness/*.md` | Audit-only |

  - **Governance items 1a and 1b+2 are excluded.** App CONTRACT, SPEC, PRD, TYPES and
    DIRECTIVE, and `contract_invariant_coverage_register.csv`, are **not** audit targets.
    They remain GOVERNING only.
  - Conflicts involving them surface on the rows that encounter them, as
    `AUTHORITY_CONFLICT` under the revised MR-11.
  - Extension units are keyed and indexed per `CONVENTIONS.md` §8 and
    `R1_INVENTORY/EXTENSION_INDEX.csv`.

## What this authorizes

- R1b reverse-pass inventories for the remaining code areas.
- R2 package concordance and the extension ledgers under `CONVENTIONS.md`.
- R3 synthesis afterwards, under D-APP-128.

## Not authorized

- No repair.
- No lifecycle transition.
- No hold change.
- No confirmation of the done declaration.
- No ruling on R4-Q1..Q3 or on Q-01..Q-13.
- No audit of the governing documents or the coverage register.
- No agent-instruction or workflow change.
- No new standing surface.
- All D-APP-128 exclusions continue to apply.

## Dispatch precondition

No R2 or R1b work is dispatched until this record and its register row are merged to
`main`.
