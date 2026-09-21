# DEL-06-02 — reverse-pass notes (worker A)

**Capability files answered, in order:** BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SETTINGS, SHELL. There are 326 rows.

| Response | Rows |
|---|---:|
| CLAIMED_BY | 3 |
| PARTIAL | 9 |
| NOT_MINE | 314 |

- **Errata:** none. No `_errata.csv` was written, so the sealed and errata-applied census figures are identical (see `DEL-06-02_notes.md` §1).
- **Seal:** the claims SHA-256 is unchanged (`006bf3c8…a3a26`).

## Ownership reading

- **CLAIMED_BY:**
  - RTCONTRACT-042, the descriptor registry;
  - RTCONTRACT-044, the MCP tool-name vocabulary;
  - BUILD-036, the catalog generator (the D-APP-70 mapping).
- **PARTIAL:** these are capabilities whose paths contain DEL-06-02 logic inside a wider surface:
  - `tool-pool.ts` inside HARNESS-040;
  - the unknown-tool check inside HARNESS-030;
  - allowed and disallowed list emission inside HARNESS-031;
  - the fingerprint in HARNESS-060;
  - the readOnly policy mapping in RTCONTRACT-019;
  - Runtime requested-tool restriction in RTCORE-020;
  - the application-tool catalog in RTCONTRACT-034 and RTCORE-033, which is my LOW-confidence STATE-2 reading.
- **NOT_MINE:** HARNESS-043 (permission overlay, DEL-06-01) and HARNESS-050/057 (MCP tool implementations, DEL-06-03 and the delegation owner) are deliberately answered NOT_MINE.

## Coverage observations

These are for the manager. They are not errata.

- **Runtime-fingerprint reach disagrees.** CAP-HARNESS-060 classifies `runtime-fingerprint.ts` as `REACH=TEST_ONLY` (its only importer is a test fake). The pack's `REACHABILITY.csv`, which the ledger follows, gives `LEGACY_ONLY`. The ledger rows CLM-006 and CLM-010.12 therefore carry `REACH=LEGACY_ONLY`.
  - The disposition does not change: REQ-012 is judged on the live `runtime-service.ts` fingerprint.
  - The two maps disagree, and the manager may want to reconcile them.
- **RTCONTRACT-042 reach.** It marks the registry `REACH=LEGACY_ONLY` (consumers are legacy; the barrel only makes it LIVE). The ledger tags `REACH=LIVE` per the pack, with a barrel-only note in Notes (see notes §5). No disposition changes.
- **Uncaptured behaviour.** No capability row captures the Runtime `restrictRequestedTools` readOnly `READ_TOOL` regex filter as a behaviour of its own; it is folded into RTCORE-020 and RTCORE-039. The forward ledger covers it in CLM-010.2 and CLM-010.11.
- **Forward coverage gaps:** none found.
