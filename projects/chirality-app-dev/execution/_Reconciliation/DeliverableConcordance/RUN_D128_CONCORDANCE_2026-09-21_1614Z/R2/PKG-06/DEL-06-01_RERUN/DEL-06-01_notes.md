# DEL-06-01 notes (R2 rerun, pass 1 forward)

Independent rerun ledger for DEL-06-01 ChiralityPermissionOverlay and Mode Mapping. The original
ledger folder and `_verify` were not read. Basis: the frozen tree at `00115c719`.

## 1. Census

57 rows cover 34 indexed units, 4 REGISTER rows and 1 STATE row.

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 30 |
| CONTEXT_CLAIM | 10 |
| STATE_ASSERTION | 9 |
| ACCEPTANCE | 4 |
| REGISTER_DEFECT | 4 |

| Disposition | All rows | of which SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 21 | 4 |
| IMPLEMENTED_DIFFERENTLY | 13 | 0 |
| AUTHORITY_CONFLICT | 7 | 5 |
| PARTIALLY_IMPLEMENTED | 6 | 1 |
| ALIGNED | 5 | 0 |
| NOT_AUDITABLE | 3 | 0 |
| REMAINING_STATE_MISMATCH | 2 | 0 |

- **SEE rows (MR-4), 10 in total:**
  - CLM-007, 016, 023 and 033 point to CLM-001 (the repeated REF-006 MATCH note).
  - CLM-009.5, 009.6, 009.9, 027 and 031 point to CLM-004 (the mode conditions).
  - CLM-020 points to CLM-011 (the verification checks).
  - Without SEE rows there are 47 rows: STALE_SPECIFICATION 17, IMPLEMENTED_DIFFERENTLY 13,
    AUTHORITY_CONFLICT 2, PARTIALLY_IMPLEMENTED 5, ALIGNED 5, NOT_AUDITABLE 3,
    REMAINING_STATE_MISMATCH 2.
- **Split rate:** 4 of 34 units were split (12%), into 22 rows.
  - CLM-009 became 15 rows, one per DEL-06-01-REQ-001..015. The index lists no SubItems for it
    because the IDs are prefixed; the split follows the separately-numbered-REQ rule.
  - CLM-015 became 2 rows (amendment text; AC-001).
  - CLM-022 became 2 rows (lensing table; VER-001).
  - CLM-034 became 3 rows (ownership and evidence text; AC-002; VER-002).
- No errata file exists (pass 1).

## 2. Least-confident rows

No row is LOW. These MEDIUM rows have a plausible alternative reading:

- **CLM-009.3 (REQ-003, K-PERM-1 deny precedence): IMPLEMENTED_DIFFERENTLY.**
  - Alternative reading: AUTHORITY_CONFLICT. D-GOV-43 item 4 makes the user's Codex policy the
    only deny layer for Codex-native actions, which undercuts the unamended K-PERM-1.
  - It was kept as IMPLEMENTED_DIFFERENTLY because the Runtime still filters tools by mode and
    role, and the Codex sandbox does enforce denials.
- **CLM-009.4 (REQ-004, allowedTools): IMPLEMENTED_DIFFERENTLY.**
  - Alternative reading: ALIGNED. The live path restricts through "mode policy", which the
    requirement lists among acceptable mechanisms.
- **CLM-009.13 (REQ-013, product-owned contracts): ALIGNED.**
  - Alternative reading: PARTIALLY_IMPLEMENTED. Live `tool.permission` events embed the raw Codex
    payload.
  - K-EVENT-1 (as amended under D-GOV-43) permits preserved upstream payloads, so ALIGNED was
    kept.
- **CLM-034.1: STALE_SPECIFICATION (FACADE_DEPRECATION).**
  - Alternative reading: ALIGNED with a note. The cited facade file still exists and re-exports
    the descriptors.
- **CLM-022.2 and CLM-034.2: ALIGNED at module level on LEGACY_ONLY code.**
  - Whether these verifications still evidence product behaviour turns on R4-Q1.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` records REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD as
  MATCH. Their hashes do not reproduce (`HASH-RECOMPUTE@00115c719`).
  - REF-001, REF-004, REF-005 and REF-007 do reproduce (recomputed by this worker).
  - 19 SoW rows restate the MATCH state and cite REGISTER-1.
- **REGISTER-2.** `_DEPENDENCIES.md` lags `Dependencies.csv`:
  - it still says "no accepted dependency edges extracted";
  - it shows DEP-06-01-011..013 as ACTIVE, but the CSV marks them RETIRED;
  - it gives the DEP-06-01-014 target as UNKNOWN, but the CSV names the `appendHarnessEvent` path.
- **REGISTER-3.** `DEP-06-01-010` is SATISFIED only on the PRD MATCH premise, which no longer
  holds.
- **REGISTER-4.** The `_STATUS.md` header lags:
  - Last Updated reads 2026-07-12, but History has a 2026-07-19 entry;
  - the D-APP-19 approval fields are still presented as current, although D-APP-54 made them
    history.
- **STATE-1.** The `_CONTEXT.md` SCA-APP-001 note still names the Claude Agent SDK as the current
  path. This contradicts CONTRACT K-ENGINE-3 (Codex is the sole engine).
- **Carrier propagation.** No DEL-06-01 carrier cites D-APP-127 or D-GOV-43. The SoW still
  describes the in-process Claude SDK overlay as the product mechanism.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE (27 rows): the live path is Codex approval requests under a user-chosen
    `PolicySelection`. The overlay, `canUseTool` and the SDK options builder are LEGACY_ONLY.
  - DOC_HYGIENE (16 rows): the hash drift and metadata lag.
  - RUNTIME_EXTRACTION (3 rows): SCA-APP-005 rewrote the decomposition row and SOW labels, and
    explicitly left the ScopeOfWork unchanged.
  - Singles: FACADE_DEPRECATION, PRE_V3_DRIFT and CARRIER_PROPAGATION, one row each.
- **CAUSE2 secondaries:**
  - CARRIER_PROPAGATION on the MATCH rows, REGISTER-1, REGISTER-3, STATE-1, CLM-002 and CLM-014;
  - PRE_V3_DRIFT on CLM-005, 018, 019 and 021 (TBD paths were already stale before v3);
  - CODEX_SOLE_ENGINE on CLM-008;
  - DOC_HYGIENE on CLM-032.
- **GOVERNING records cited as direction:**
  - D-GOV-43 item 4, from the ruling and the revision-3 proposal text: "Full access is available
    by explicit user choice".
  - D-APP-127.
  - SCA-APP-005: its Propagation_Plan "Explicitly unchanged" list.
  - D-APP-68 item 4 (D-GOV-14 item 7): the SDK Agent bridge is retired.
  - D-APP-89 Option B: facade migration only, with the facade retained. D-APP-118 (retirement
    packet) is AWAITING_RULING.
  - D-APP-54 and D-APP-56 R5 P45.
- **AUTHORITY_CONFLICT rows** (CLM-004, 009.5, 009.6, 009.8, 009.9, 027, 031):
  - K-PERM-4, K-PERM-5 and K-PERM-6, TYPES 8.1 and SPEC 15.1/15.2 are unamended.
  - D-GOV-43 item 4 sets them aside without naming them. This includes the shipped "Full access"
    (bypass) mode, and readOnly running with approval on-request.
  - TYPES 13 `PolicySelection` already follows D-GOV-43, so TYPES is internally inconsistent.
  - These rows cite R4, or R4-Q1 where SPEC 15.x or the retained overlay is at stake.
- **NONE_FOUND (CLM-021 only).** Searched `execution/_Coordination/_DECISIONS/_REGISTER.md`:
  - grep for DEL-06-01, permission-overlay, bypass, dontAsk and PolicySelection: no rows;
  - grep for harness-contract, runtime-contracts and facade: D-APP-47, 48, 49, 76, 89, 101, 118.
- **CONTEXT steers.** `plans/steers/chirality_app_v3_*` and the codex host re-platform direction
  were grepped for "approval polic", sandbox, "full access" and "permission mode". No hits add to
  D-GOV-43 item 4.

## 5. Method friction

- **Prefixed REQ IDs are not indexed.** CLM-009's REQ IDs carry a deliverable prefix
  (`DEL-06-01-REQ-001`), so the index lists no SubItems and V-SUBITEMS does not force the split.
  - Proposal: the R1 SubItems extractor should also match `DEL-xx-yy-REQ-nnn`.
- **MR-4 fits bundled units poorly.** CLM-004's condition table bundles REQ-005, REQ-006 and
  REQ-009, and MR-4 makes those later numbered rows SEE rows of CLM-004.
  - The REQ rows still carry full evidence.
  - Proposal: allow SEE to point from a bundle to the granular numbered rows instead.
- **D-GOV-43 has no R4 question.** No named R4 question covers "K-PERM-* versus D-GOV-43 item 4",
  so plain R4 is used.
  - Proposal: frame an R4-Q4 for permission-mode invariants under user-chosen Codex policy.

## 6. Effort

- About 45 files or ranges read. These include:
  - the deliverable folder;
  - `permission-overlay.ts`, `subagent-bridge.ts`, `sdk-options-builder.ts`;
  - `codex-supervisor.ts`, `delegated-engine-adapter.ts`, `delegated.ts`,
    `runtime-method-service.ts`;
  - `chat-panel.tsx`, the permission route, cards and port;
  - CONTRACT, SPEC and TYPES slices, the register and the D-GOV-43 records.
- Git: log, show and blame -L against the frozen tree only.
- The context budget was adequate, not tight.
