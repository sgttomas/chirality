# Evidence — DEL-04-05-V3-01: typed safeStorage states at the App credential bridge (2026-09-03)

> Derivative evidence (App AGENTS.md derivative-package rule). Accepted upstream:
> `main` at `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge). Run record:
> `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03/`. Executed by
> Claude Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 under HELP_HUMAN. No
> release, signing, lifecycle, or reliance claim.

## 1. Claim (AT-057 storage-state portion; RQ-002/003/004/012 preserved)

`frontend/electron/api-key-storage.ts` now classifies each provider's encrypted blob
into exactly one of `missing`, `storageUnavailable`, `decryptFailed`, `available`
(`readProviderCredential`, `probeProviderCredentialStorage`), and
`SafeStorageCredentialStore.status()` returns `{ configured, source, storage }` — the
accepted `ui | env | none` source and its precedence (UI safeStorage > `ANTHROPIC_API_KEY`
> `CHIRALITY_ANTHROPIC_API_KEY`; `CHIRALITY_OMLX_API_KEY` for oMLX) are unchanged. The
typed state is non-secret and orthogonal to the source: an environment credential can
be in use while the blob is `decryptFailed`, and both facts travel. No plaintext is
exposed by any state; a failed read never rewrites, truncates, or deletes the blob;
there is no fallback to a plaintext or alternate store; the daemon remains the sole
runtime credential owner (no `runtime/**` change — the daemon spreads the store's
status verbatim at `runtime/packages/daemon/src/runtime-daemon.ts:278`, so the field
reaches `RuntimeClient.credentialStatus()` and the Electron IPC projection as-is).

Exact definitions (from the source doc-comment): `storageUnavailable` —
`safeStorage.isEncryptionAvailable()` false, blob not opened; `missing` — no ciphertext
readable, or ciphertext decrypts to an empty string; `decryptFailed` — bytes read but
`safeStorage.decryptString` threw; `available` — decrypted to a non-empty key. The
only mutation on a read path is the existing owner-only permission-bit repair.

## 2. Source and fixture identities (SHA-256 at freeze)

| File | SHA-256 |
|---|---|
| `frontend/src/lib/credential-storage-state.ts` (new shared type/guard; renderer + main) | `b9a9e171ae8de26845d1868fe03510e3f4b8737a177460538127ba7376441e43` |
| `frontend/electron/api-key-storage.ts` | `086b249f461c7e1463a14239594dbf3f0a4e5f90febed0b55e75a27f015b2c3c` |
| `frontend/electron/api-key-ipc.ts` (projection: validates `storage`, derives `encryptionAvailable = storage !== 'storageUnavailable'`, fails closed on inconsistent answers) | `219b7d676ddaa84ca553af7645e0b52c9ce6c9baa36dfe4fef057685fdfba6f8` |
| `frontend/src/__tests__/electron/api-key-storage.test.ts` (fixtures) | `72de9a6104806f91f3fcf6bc044cd844211b880fb05842a283e74e0e3a954329` |
| `frontend/src/__tests__/electron/api-key-ipc.test.ts` | `2fa5c5ab4bbd2b1e63a0ed1e7a907ba13388d1c2da9c3a69dec008ab18f0cf59` |

## 3. Fixtures and non-destructive proof (`api-key-storage.test.ts`, describe "typed storage states")

Electron is mocked as in the existing file (`safeStorage.encryptString` → `enc:<value>`,
`decryptString` throws unless the prefix matches); blobs live in a per-test `mkdtemp`
userData root and are removed afterwards (cleanup proof: `afterEach rm -rf`).

| Fixture | Bytes | Assertions |
|---|---|---|
| Corrupt ciphertext | `00 ff 13 37 42 00 99 ab` written to `credentials/api-key.enc` | `readProviderCredential` → `{ state: 'decryptFailed' }`; probe → `decryptFailed`; `retrieveProviderApiKey` → `null`; serialized results contain no fixture plaintext; `encryptString` never called; **SHA-256 and raw bytes identical before/after three failed reads**; file still present (`hasStoredProviderApiKey` true) |
| Corrupt ciphertext through the store | same | `status('anthropic')` → `{ configured:false, source:'none', storage:'decryptFailed' }`; with `ANTHROPIC_API_KEY` set → `{ configured:true, source:'env', storage:'decryptFailed' }` and `get` returns the env value; blob bytes identical after |
| Explicit replacement only | same | blob unchanged until `set()` (then `enc:replacement-key`, `available`/`ui`) and `remove()` (then `missing`) |
| Unavailable store | valid `enc:…` blob present; `isEncryptionAvailable` → false | read → `storageUnavailable`; probe → `storageUnavailable`; retrieve → `null`; `decryptString` **never called**; `encryptString` never called; **bytes identical before/after**; file present |
| Unavailable store through the store | none / env | `status` → `storage:'storageUnavailable'` for both providers; env precedence preserved (`configured:true, source:'env', storage:'storageUnavailable'`); `set()` rejects "Secure storage is not available on this platform"; nothing written |
| Missing | no file | `missing` for both providers; `decryptString` never called; env not consulted by the read |
| Available | stored via `storeProviderApiKey` | read carries the value; probe carries only the state |
| Empty plaintext | `enc:   ` | `missing` |
| Provider isolation | oMLX valid + Anthropic corrupt | `omlx` `available`/`ui`, `anthropic` `decryptFailed` |

Existing status expectations were extended with the additive `storage` field; every
existing precedence and isolation test still passes (29 tests in the file).

## 4. IPC projection evidence (`api-key-ipc.test.ts`, describe "typed storage state")

Seven `(storage, source)` combinations are projected verbatim with
`encryptionAvailable` false exactly for `storageUnavailable`; five inconsistent or
unknown answers (`storage:'corrupt'`, non-string, `available` without `ui`, `ui`
without `available`, `ui` with `storageUnavailable`) fail closed to the existing
"Runtime daemon returned an invalid credential status" result without echoing any
field; a pre-typed-state daemon answer (no `storage`) maps to `available` for `ui` (by
construction a decryptable stored blob) and is otherwise left **without** a `storage`
field (`encryptionAvailable: true`, the basis shape) — such a daemon cannot tell
`missing` from `decryptFailed` or `storageUnavailable`, so no state is asserted and the
panel renders `unknown` (round-3 change on review MINOR-1; the round-1/2 behaviour had
synthesised `missing`).

## 5. Packaged observation

The packaged security proof (`npm run proof:packaged-security`, status pass;
retained under DEL-09-06 `Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/packaged-security-proof/summary.json`)
shows the real packaged daemon reporting `storage: "missing"` before store,
`"available"` with `source: "ui"` after store, and `"missing"` after remove, through
`RuntimeClient` — the field crosses the daemon boundary unchanged.

## 6. Commands, environment, rerun

cwd `projects/chirality-app-dev/frontend`; node v24.18.0, Vitest 4.1.10, TypeScript
5.9.3, Electron 43.2.0 (mocked in unit tests). `npx vitest run
src/__tests__/electron/api-key-storage.test.ts src/__tests__/electron/api-key-ipc.test.ts`
→ 87 passed, exit 0; `npm run typecheck` exit 0; `npm test` 1364 passed / 4 skipped,
exit 0. Full command table with exit statuses: run record `CHECKS.json`. Rerun: the
same commands after `npm ci` (frontend) and `npm ci && npm run build` (runtime).
