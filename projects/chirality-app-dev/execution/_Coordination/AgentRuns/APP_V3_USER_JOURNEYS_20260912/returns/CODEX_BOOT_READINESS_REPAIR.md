# Codex pre-thread boot readiness repair

Status: bounded implementation and focused checks complete; parent browser repeat and independent review pending. TASK / Type 2, gpt-6-astra medium, no delegation. Basis: candidate `46232f5f5c4b0e7aee8eb022fa11ebf54b1fb516` plus parent's ordinary UI reproduction of the recovered J09 draft. No commit, Runtime/source-auth change, live API/UI operation, supplier call or protected profile/session/event read performed. Diagnosis read only product source and the explicitly authorized filtered App log.

## Diagnosis

Concrete App readiness mismatch, not expected preservation of an unrecoverable historical failure. Runtime's delegated Codex adapter declares `boot: none` (`projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts`). Its Runtime boot path records `bootedAt` and `bootFingerprint` without creating a provider thread; `engineSessionId` is first established during the first actual supplier turn (`runtime-service.ts`, boot-none branch; `turn-coordinator.ts`, session:init handling). An attachment error before that first supplier initialization can therefore leave a legitimately boot-ready session with both stamps and no engineSessionId.

The App projection and Send reconciliation instead required all three fields. Reload projected this session as unconfirmed; Send only re-read the session and threw a local `ENGINE_UNAVAILABLE` while the field it demanded could only appear after the turn the UI was preventing. Repeated Send did not retry boot or submit a turn. The allowed filtered log recorded GET of the reported historical session returning 200, with no corresponding boot/turn POST, consistent with the source diagnosis. No hidden record was inspected; exact persisted field values were not inferred as observed data.

## Precise change

Inside `projects/chirality-app-dev/frontend/`:

1. New `src/lib/harness/session-boot-readiness.ts`: shared `isSessionBootConfirmed` requires nonempty Runtime `bootedAt` and `bootFingerprint`. A provider engineSessionId confirms traditional readiness. Without one, readiness is admitted only for canonical `chirality.session/v3` and the exported `CODEX_ENGINE_ADAPTER_ID`, whose Runtime adapter has boot:none semantics. Other and legacy adapters retain their existing provider-session requirement.
2. `src/lib/woven-dialogue/operator-projection.ts`: use that predicate for v3 bootstrapConfirmed.
3. `src/components/shell/chat-panel.tsx`: use the same predicate during pending-session reconciliation. Identity/role/root checks, boot-stamp requirements, incomplete-boot holds, session ID, draft and attachment restoration remain intact. No automatic reboot or replacement session was introduced.
4. `src/__tests__/lib/operator-projection.test.ts`: boot-ready Codex without provider ID, missing boot stamps, and other/unknown adapter coverage.
5. `src/__tests__/components/chat-panel-folder-binding.test.tsx`: first attachment rejected before provider startup, saved draft and attachment survive unmount/reload and resend on the same session; lost boot response reconciles from Codex boot stamps without new create/boot; truly incomplete Codex boots remain held.

## Validation

APP-HOLD-1 dispatch preflight, entry `APP_V3_USER_JOURNEYS_20260912:CODEX_BOOT_READINESS`, DEL-03-01: ALLOW / CLEAR / NOT_HELD; no active holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan `543a2272b489b62bda5db44c2fdd06c9f6da5fe8f7a47aedaf80b4b0525b6811`.

- `npx vitest run src/__tests__/lib/operator-projection.test.ts src/__tests__/components/chat-panel-folder-binding.test.tsx`: PASS, 2 files / 69 tests.
- `npm run typecheck`: PASS, frontend and Electron TypeScript.

No build or Git operation was run. Tests use controlled fixtures and mocked turn transport; parent owns actual J09/fresh-attachment behavior and candidate-wide gates.

## Handoff

Ready for fresh independent review. Parent should reload the candidate renderer, reopen the historical rejected-first-attachment chat and submit the preserved draft. It should submit a real same-session turn if Runtime boot stamps exist; missing stamps must still hold. Minimum ordinary-API diagnostic data, if any further ambiguity remains: schemaVersion, adapterId, status, and presence booleans for bootedAt, bootFingerprint, engineSessionId. Neither raw fingerprint values nor credentials/native hidden-state access are needed.

This is derivative implementation evidence, not product release or authoritative project acceptance. Diagnosis and local repair are closed; integrated UI confirmation and independent-review acceptance remain with parent.
