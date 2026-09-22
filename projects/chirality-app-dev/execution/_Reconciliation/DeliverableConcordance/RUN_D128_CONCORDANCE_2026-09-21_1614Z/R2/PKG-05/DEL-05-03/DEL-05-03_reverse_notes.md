# DEL-05-03 reverse-pass notes

## What was answered

- **Capability files**, in this order: BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCORE 50, SETTINGS 42, WOVEN 43. That is 315 rows in `DEL-05-03_reverse.csv`.
- **Responses:** CLAIMED_BY 1, PARTIAL 21, NOT_MINE 293.
  - The only CLAIMED_BY row is CAP-HARNESS-027, the configured API-key redaction helper, owned by `CLM-010.9`.
  - A capability is PARTIAL when DEL-05-03 owns only its redaction or secret-hygiene aspect and another deliverable owns the component.
- **Validation:** the reverse file was validated once against each of the seven capability files, and the errata file once. Every run gave `RESULT PASS errors=0 warnings=0`.
- **Seal:** the claims SHA-256 is unchanged (`5b4d6ec6…d6f7`).

## Errata (2 rows) and census

- **The errata.** CLM-004 and CLM-010.2 cite `electron/api-key-storage.ts` as `REACH=LIVE`.
  - CAP-ELECTRON-034 shows the storage symbols have no production or Runtime importer. The pack marks the module LIVE only because `api-key-ipc.ts` imports `isProviderCredentialId`. The store is STATE=DISABLED.
  - The proposed value is `REACH=LEGACY_ONLY` (UNREACHED at symbol level).
- **Effect on dispositions.** The Disposition stays IMPLEMENTED_DIFFERENTLY: live custody rests on `codex-effective-home.ts` (LIVE).
  - The Notes phrase "App keys in safeStorage" in those rows overstates the live mechanism. It is covered by the same erratum rationale.
  - These rows do not change to cite R4-Q1, because LIVE code (the Codex custody overlay) still meets them.
- **Census:** sealed and errata-applied figures are identical, because no Disposition changed. STALE_SPECIFICATION 19, PARTIALLY_IMPLEMENTED 9, IMPLEMENTED_DIFFERENTLY 6, NOT_AUDITABLE 6, DOCUMENTED_UNIMPLEMENTED 4, ALIGNED 3, UNKNOWN 2, REMAINING_STATE_MISMATCH 1.
- **Corroboration.** CAP-HARNESS-027 independently confirms the forward reading on CLM-010.3: run-logger's live use (chat titles) is inert in the renderer.

## Coverage gaps (no forward row can own these)

- **CAP-RTCORE-029 / RTCORE-017 / RTCORE-013.** The live Runtime paths where amended K-EVENT-6 redaction must run are Codex notification pass-through, the event journal and the host logger.
  - DEL-05-03 can only verify them. Decomposition SOW-041 gives Root/Runtime the generic run logger.
  - No App deliverable or App carrier names the Runtime owner of the missing structural redaction. It is PARTIAL here and needs an owner decision; the likely route is REM-1 or a Runtime deliverable.
- **CAP-RTCORE-006.** Account and sign-in ceremony data (device code, callback parameters) have no forward row beyond the REM-1 "account" field family. The SoW has no requirement for ceremony-data exclusion, although amended K-EVENT-6 and K-KEY-1 require it.
- **CAP-BUILD-028.** The secret-evidence scanner is excluded from DEL-05-03 scope (CLM-009). Amended K-KEY-1 lists the "secret-evidence scanner" as an enforcement surface, so its owner (PKG-09) should be confirmed.
