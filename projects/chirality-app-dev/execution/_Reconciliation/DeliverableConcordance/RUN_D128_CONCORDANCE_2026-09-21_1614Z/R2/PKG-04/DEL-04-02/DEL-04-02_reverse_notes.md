# DEL-04-02 — reverse-pass notes (RUN_D128, R2 wave 1, PKG-04)

The forward ledger is sealed, and its SHA-256 is unchanged at the end of this pass:
`ea592f358e25220cd3f99e837c2bd5bf0c2cf3cde7f302ddee0223b46943bbe5`.

## 1. Response counts

- **320 capability rows answered** across 7 areas: BUILD 41, ELECTRON 35, HARNESS 60, RTCONTRACT 53,
  RTCORE 50, SETTINGS 42, WORKSPACE 39.
- **Result:** CLAIMED_BY 0, PARTIAL 15, NOT_MINE 305.
- **PARTIAL rows, by the forward row they point to:**
  - **Retained Claude builder (legacy path):**
    - HARNESS-031 → CLM-009 (options module inside the Claude adapter);
    - HARNESS-030 → CLM-010.1 (legacy default options);
    - HARNESS-043 → CLM-010.7;
    - HARNESS-040 and HARNESS-060 → CLM-010.10;
    - RTCONTRACT-042 → CLM-010.5;
    - RTCONTRACT-044 → CLM-011;
    - RTCONTRACT-045 → CLM-010.12.
  - **Live analogues of option construction:** RTCORE-005, RTCORE-025, RTCORE-028 and
    RTCONTRACT-019, all → CLM-009.
  - **App option inputs, per the `_CONTEXT.md` scope:** HARNESS-019 and WORKSPACE-006 →
    CLM-010.1.
  - **CHIRALITY_GLOBAL_MODEL tier:** RTCORE-048 → CLM-028.
- **Why no CLAIMED_BY:** DEL-04-02 wholly owns no capability. The builder shares
  CAP-HARNESS-031 with the adapter owners (DEL-04-01 and DEL-04-03).

## 2. Errata (6 rows, 3 ClaimKeys)

- **CLM-010.1, ImplementationEvidence.** The sealed row tags
  `compatibility-session-policy.ts:54` as `REACH=LIVE`, taken from the pack's REACHABILITY.csv.
  - The pack reached it only through the `core/src/index.ts` barrel re-export.
  - A grep of the frozen tree finds no importer or instantiation of `CompatibilitySessionPolicy`.
    CAP-RTCORE-048 agrees: REACH=LEGACY_ONLY, UNREACHED, DISABLED.
  - Proposed value: `REACH=LEGACY_ONLY (UNREACHED)`. The disposition does not change.
- **CLM-028, four fields.** The same reach correction removes the premise of the sealed
  IMPLEMENTED_DIFFERENTLY reading, which was that the env-model tier had moved to live Runtime code.
  No reachable code honours `CHIRALITY_GLOBAL_MODEL`.
  - ImplementationEvidence: the reach tag is corrected as for CLM-010.1.
  - Disposition: PARTIALLY_IMPLEMENTED. This is the alternative the sealed row flagged as
    LEAST-CONFIDENT.
  - Confidence: MEDIUM, up from LOW.
  - Notes: rewritten.
- **CLM-010.10, ImplementationEvidence.** `runtime-fingerprint.ts` is imported only by tests
  (`src/__tests__/api/harness/*`), so the tag is `REACH=TEST_ONLY`, not LEGACY_ONLY. CAP-HARNESS-060
  agrees. The disposition does not change.

### Census, sealed versus errata-applied

| Figure | Sealed | Errata-applied |
|---|---|---|
| ALIGNED | 14 | 14 |
| PARTIALLY_IMPLEMENTED | 11 | 12 |
| STALE_SPECIFICATION | 10 | 10 |
| REMAINING_STATE_MISMATCH | 5 | 5 |
| NOT_AUDITABLE | 5 | 5 |
| IMPLEMENTED_DIFFERENTLY | 2 | 1 |
| LIFECYCLE_REASSESSMENT_REQUIRED | 1 | 1 |
| Confidence LOW / MEDIUM / HIGH | 1 / 26 / 21 | 0 / 27 / 21 |
| HumanDecisionNeeded ≠ NO | 31 | 31 |

## 3. Legacy-builder versus live-path judgement (asked by the manager)

I judged the requirement rows against the retained module. On reflection I am **not correcting
that choice by errata**. It stays a flagged interpretation for R4-Q1.

- **Why I kept it.**
  - DEL-04-02-REQ-001..014 are written as obligations on the builder ("The builder MUST …").
    CONVENTIONS §2.3 says a claim about the retained module itself is judged at module level.
  - The live-path divergence is recorded once, at deliverable level, on these rows:
    - CLM-009: IMPLEMENTED_DIFFERENTLY, R4-Q1;
    - CLM-004 and CLM-023: STALE_SPECIFICATION;
    - STATE-1 and STATE-2.
  - The reverse pass strengthens those rows rather than contradicting them:
    - CAP-HARNESS-031 is STATE=DISABLED, meaning the Claude engine is not composed in the product;
    - CAP-BUILD-015 verifies that app.asar contains no legacy Claude SDK, so the builder does not
      ship at all;
    - CAP-RTCORE-005 confirms that the live settings posture shares `~/.codex`.
- **The case for correcting.** The strict reading is that SOW-016, 045, 047 and 052 are product
  requirements, so they should be judged on the live path. If R4-Q1 is ruled that way, the
  errata-equivalent changes would be:
  - REQ-001 fallback: PARTIALLY_IMPLEMENTED. The live model comes from the per-turn model/effort
    and signed-in catalog (CAP-RTCORE-025), and no tools or maxTurns fallback exists.
  - REQ-003/004 settings isolation: ACCEPTED_DIVERGENCE is not available because the SoW text does
    not acknowledge the change. The row would be IMPLEMENTED_DIFFERENTLY: Codex shares the user's
    configuration by D-GOV-43 design, and K-SDK-1 is scoped to the Claude adapter, which does not
    ship.
  - REQ-005/006 tool mapping: DOCUMENTED_UNIMPLEMENTED. Codex native tools are not mapped from
    `opts.tools`.
  - REQ-008 maxTurns: DOCUMENTED_UNIMPLEMENTED. The toolkit sends `maxTurns` in optsPayload
    (CAP-WORKSPACE-006, LIVE), but grep finds no consumer in `runtime-daemon-harness-port.ts`,
    `delegated-engine-adapter.ts` or `codex-supervisor.ts`. The live App therefore offers a
    max-turn control with no effect.
  - REQ-007/014 permission posture: IMPLEMENTED_DIFFERENTLY, through the fixed mode →
    approval/sandbox mapping (CAP-RTCONTRACT-019).
- **Recommendation.** Leave the sealed rows as they are and let the R4-Q1 ruling select the
  reading. The REQ-008 live gap is the most concrete product finding here and should be carried to
  R4 whichever reading is chosen.

## 4. Coverage gaps

No forward row is missing for anything this deliverable owns under its SoW. Two gaps under the
`_CONTEXT.md` scope are for the manager:

- **Silent toolkit options.** `_CONTEXT.md` scope is "App/project option inputs". On the live
  path, `tools` and `maxTurns` from CAP-HARNESS-019 and CAP-WORKSPACE-006 appear to be dropped
  without notice. No forward row audits the live consumption of optsPayload.
- **Owning deliverable.** Whether DEL-04-02 or a PKG-05 turn deliverable owns that live
  consumption is not evident.

## 5. Capabilities that look owned elsewhere

- **DEL-04-01:** HARNESS-031 (manager and proof spawn), BUILD-031, BUILD-041.
- **DEL-04-03:** HARNESS-032.
- **DEL-04-04:** HARNESS-040.
- **DEL-04-05:** HARNESS-027, HARNESS-036, ELECTRON-032/033, SETTINGS-009/010.
- **PKG-06:** HARNESS-043, HARNESS-044, HARNESS-047, HARNESS-050/051, RTCONTRACT-044.
- **PKG-08:** HARNESS-058.
- **PKG-09:** BUILD-015.
- **PKG-03/05:** RTCORE-005, RTCORE-025, RTCORE-028.

## 6. Capability-file and pack accuracy

- **Pack REACHABILITY.csv, two tags contradicted by importer grep:**
  - `compatibility-session-policy.ts` is LIVE in the pack but unreached (barrel-only re-export).
    The capability file is right.
  - `runtime-fingerprint.ts` is LEGACY_ONLY in the pack but TEST_ONLY; again the capability file
    is right.
- **Suggestion for the verifier:** treat any pack LIVE tag reached only through an `index.ts`
  barrel as suspect.
- **Capability files:** no REACH or STATE tag was contradicted by code that I read.

## 7. Effort

- **Read:** the capability listing (320 rows, as a compact projection), 15 full capability rows,
  and three importer greps against the frozen tree.
- **Context budget:** comfortable.
