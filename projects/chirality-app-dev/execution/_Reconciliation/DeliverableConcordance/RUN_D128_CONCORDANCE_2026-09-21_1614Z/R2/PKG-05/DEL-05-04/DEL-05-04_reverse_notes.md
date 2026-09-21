# DEL-05-04 — reverse-pass notes (R2, PKG-05)

- **Scope:** 413 capability rows from 9 files, in this order: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS,
  SHELL, WOVEN.
- **Responses:** CLAIMED_BY 7, PARTIAL 15, NOT_MINE 391.
- **Validator:** PASS for each capability file (errors 0, warnings 0).
- **Sealed ledger:** unchanged. SHA-256 is still `ba18ac192ea6a17390b44b372504246b5eff3313ae3fc97e9d19092b3c9856e8`.
- **Errata:** none. No forward row was found to be wrong, so the census is unchanged from pass 1 (there are no
  errata-applied figures).

## Claimed and partial capabilities

- **CLAIMED_BY.** Each of these capabilities has one owning forward row:

  | Capability | Forward row |
  |---|---|
  | ROUTES-006 | CLM-004.1 |
  | RTCONTRACT-020 | CLM-010.2 |
  | RTCONTRACT-021 | CLM-010.5 |
  | WOVEN-019 | CLM-010.16 |
  | WOVEN-021 | CLM-004.2 |
  | WOVEN-022 | CLM-010.14 |
  | WOVEN-029 | CLM-010.17 |

- **PARTIAL.** These capabilities are shared with a neighbouring deliverable. DEL-05-04 owns only the replay or projection
  part:
  - DEL-05-01 shares session records and legacy migration (RTCORE-015).
  - DEL-05-02 shares event append and the writer (RTCORE-017, HARNESS-038).
  - DEL-08-05 and DEL-08-02 share parentage and routing (WOVEN-020, WOVEN-023).
  - DEL-02-02 and the shell share hosting and the sidebar (WOVEN-005, SHELL-005, SHELL-040).

## Coverage gaps: no forward row can be added by errata

- **1. WOVEN-021 / SHELL-031: resuming a recorded conversation.** The live behaviour is:
  - a direct history click auto-continues the recording;
  - the recording's role, permission and interaction mode are adopted;
  - `recoverActiveTurn` runs.

  DEL-05-04 covers this only as a divergence (CLM-004.2, CLM-010.14/15/19) and as the gated V3-01 item (REM-2). No carrier
  I can see owns continuation as positive scope. Owner is unclear: DEL-02-02, DEL-08-02 or DEL-05-01.
- **2. RTCORE-017 / RTCONTRACT-020: instruction history and resolved bases in the replay payload.** These are delivered in
  `runtime-daemon.ts:801-808` and consumed by the lens and the resume path. No DEL-05-04 SoW clause covers them. This is
  work delivered but not documented; the owner may be an instruction-basis deliverable.
- **3. RTCORE-029: redaction of Codex notifications before persistence.** They are persisted unredacted. That is recorded
  only through DEL-05-04's secret-handling rows (CLM-003.3, CLM-010.8). The writer-side obligation under K-EVENT-6 likely
  belongs to DEL-05-02, which the manager should check.
- **4. WOVEN-011 / WOVEN-012: chat titles and search read recorded transcripts through the replay reader.** They are
  answered NOT_MINE because they are navigator features. They do depend on the DEL-05-04 transcript projection.
