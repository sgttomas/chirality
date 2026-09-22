# DEL-02-05 — reverse-pass notes (RUN_D128 R2, PKG-02)

## Scope and inputs

- **Input:** `REVERSE_INPUT_capabilities.csv`, with 326 rows across 7 areas: BUILD, ELECTRON,
  HARNESS, RTCONTRACT, RTCORE, SETTINGS and SHELL.
- **Output:** `DEL-02-05_reverse.csv`.
- **Sealed ledger:** unchanged (SHA-256 `37d49dbb38b00288ad955d252cb1a9bbb245e0a56eaca482ef4e758e2ce3cbcc`).

## Responses

| Response | Rows |
|---|---|
| CLAIMED_BY | 12 |
| PARTIAL | 38 |
| NOT_MINE | 276 |

All BUILD rows are NOT_MINE. The secret-evidence scan (CAP-BUILD-028) and the packaged security
proofs belong to DEL-09-06, which retains key, credential-IPC and renderer validation.

## Errata

None.

The capability notes agree with the sealed rows on every point checked:

- **Disabled key panel and IPC.** The key panel and the credential IPC are disabled in the live
  composition (CAP-SETTINGS-009/010, CAP-ELECTRON-032/033, CAP-RTCORE-022).
- **Unrendered consent port and posture panel.** Neither is rendered (CAP-SETTINGS-013/016).
- **Local-model status row.** The row is never rendered in the hosted branch (CAP-SHELL-013).
- **Redaction.** It finds nothing to redact on the live path (CAP-HARNESS-027). This is
  consistent with the LOW PARTIALLY_IMPLEMENTED rows CLM-004.4, CLM-010.9 and CLM-011.4.

CAP-ELECTRON-034 tags `api-key-storage.ts` as TEST_ONLY at symbol level, while the sealed rows
keep the pack's module tag, LIVE, and record the same fact as `SYMBOL-UNREACHED`. This follows
the brief's rule for module-level tags, so it is not an erratum.

## Coverage gaps (for the manager and R3)

These are missing forward rows. Errata cannot express them.

1. **Preload coordination lead.** D-APP-71 Option 2 names DEL-02-05 the physical coordination
   lead for `frontend/electron/preload.ts` (CAP-ELECTRON-021). No SoW unit states this duty,
   which is recorded only in `_STATUS.md` History (2026-07-20). The row is answered PARTIAL via
   CLM-005.1, for the `apiKey` namespace only.
2. **Attachment picker and preview chips.** These are SOW-023/OUT-002 outputs (CAP-ELECTRON-025,
   CAP-SHELL-027, CAP-HARNESS-014), and D-APP-80 (SoW:19-23) records the note that assigns them.
   No indexed unit states their behaviour: multi-select, remove/clear, chips. They are answered
   PARTIAL via AC-002 (CLM-013.7).
3. **Live Codex account surface.** The surface is enabled and live: sign-in, cancel, sign-out,
   readiness and folder axes (CAP-SETTINGS-002..006, CAP-RTCORE-006/007). It is owned only
   through REM-1 (V3-03) and the retired REQ-001. No current SoW requirement describes it.
   Ownership is shared with DEL-04-05 and the Runtime.
4. **Settings Runtime group and Agent instructions group.** The live Settings groups include the
   Runtime group (CAP-SETTINGS-007) and the Agent instructions group (CAP-SETTINGS-012). No
   DEL-02-05 unit covers either one.
   - CAP-SETTINGS-012 is answered NOT_MINE: its product-instructions semantics lie outside
     DEL-02-05.
   - The presentation host for both groups is SEC-2.3 (Settings view).
