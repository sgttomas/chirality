# DEL-08-05 — reverse-pass notes (RUN_D128, R2 PKG-08)

The sealed ledger `DEL-08-05_claims.csv` was not changed. Its SHA-256 was re-checked after the
reverse pass and is still `ba4729f5f4d65b6f81730b27cc51668f6045d34c758157a4a779d0b8a8ea47e0`.

## Inputs

- **Capability areas:** BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS and SHELL. They
  total 326 rows, as `REVERSE_INPUT_capabilities.csv` and `REVERSE_AREAS.md` list them.
- **Reading:** I read the area files under `R2/SURFACES/` and grepped each area's notes for
  deliverable-relevant content.

## Responses (326)

- **CLAIMED_BY (1):**
  - CAP-HARNESS-059 → CLM-006.
- **PARTIAL (9):**
  - CAP-HARNESS-032 → CLM-012.4;
  - CAP-HARNESS-048 → CLM-003.3;
  - CAP-HARNESS-056 → CLM-003.1;
  - CAP-HARNESS-057 → CLM-012.13;
  - CAP-RTCONTRACT-048 → CLM-018.1;
  - CAP-RTCORE-024 → CLM-018.1;
  - CAP-RTCONTRACT-037 → CLM-018.2;
  - CAP-RTCORE-029 → CLM-012.4;
  - CAP-RTCORE-043 → CLM-018.3.
- **NOT_MINE (316):** everything else.

**Why the event store and replay capabilities are NOT_MINE.** I answered NOT_MINE for
CAP-HARNESS-038, CAP-RTCORE-017, CAP-RTCONTRACT-020 and CAP-RTCONTRACT-022.

- DEL-08-05 restates the event-store invariants (CLM-004.4, CLM-007, CLM-012.6) and consumes those
  stores, but does not own them.
- The same reasoning applies to the descendant presentation rows (CAP-SHELL-034, 039 and 040),
  which belong to DEL-02-02, and to the admission rows (CAP-HARNESS-058, CAP-RTCORE-042), which
  belong to DEL-08-04.

## Errata (2 rows, one forward row)

Both rows correct CLM-018.1:

- Disposition: PARTIALLY_IMPLEMENTED → DOCUMENTED_UNIMPLEMENTED;
- Confidence: LOW → MEDIUM.

**Evidence:**

- CAP-RTCORE-024 and CAP-RTCONTRACT-048 record the governed Agent 1 runs path as `STATE=DISABLED`.
- I confirmed this at the frozen basis:
  - `projects/chirality-runtime/packages/core/src/runtime-service.ts:664-670` makes `runAgent1`
    throw `REQUIRED_DELEGATION_MISSING` when no `Agent1RunPort` is configured;
  - the App-owned composition supplies none.

**Effect on the ledger:**

- The sealed row's LEAST-CONFIDENT alternative is confirmed.
- The other rows that cite `agent1-run-coordinator.ts` already say "test-only instantiation", so
  they need no correction. Their dispositions do not rest on that module alone.

**Census effect:**

| Disposition | Sealed | Errata-applied |
|---|---|---|
| PARTIALLY_IMPLEMENTED | 12 | 11 |
| DOCUMENTED_UNIMPLEMENTED | 14 | 15 |

| Confidence | Sealed | Errata-applied |
|---|---|---|
| LOW | 3 | 2 |
| MEDIUM | 32 | 33 |

## Coverage gaps

None. Every capability that DEL-08-05 plausibly owns maps to an existing forward row.

Two observations for the manager:

- **No live capability for child-output artifacts.** No capability in these areas describes a
  LIVE child-output artifact (`artifacts/subagents/`) or a native-descendant checkout-record
  writer. This matches the forward DOCUMENTED_UNIMPLEMENTED findings (CLM-003.3 and CLM-018.6) and
  REM-1.
- **Touched lines in `codex-supervisor.ts`.** CAP-RTCORE-029 records `da95ec194` lines in
  `handleNotification` (526, 535-544 and 570-573). The forward rows rely only on lines 280-309,
  518-519 and 588-591, which blame to other commits, so PostReleaseBasis stays NO.

## Validator

- **reverse:** `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
- **errata:** `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
