# Amended return — WI-PKG04-API-KEY-PRECEDENCE-01

RUN_STATUS: `SUCCESS`

Node: `N1 / PKG-04 / DEL-04-05`
Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`
Branch: `codex/app-api-key-precedence-20260820`
Frozen graph: `ORCHESTRATION_PLAN_V2.md` / `WORK_GRAPH_V2.md`

## Accepted implementation

`SafeStorageCredentialStore` resolves credentials once and projects either the
credential for `get` or the non-secret `{ configured, source }` status, where
`source` is `ui | env | none`. It preserves:

1. stored safeStorage/UI;
2. `ANTHROPIC_API_KEY`;
3. `CHIRALITY_ANTHROPIC_API_KEY`.

oMLX remains isolated to its stored value and `CHIRALITY_OMLX_API_KEY`.
Unsupported/unconfigured providers report `none`. No credential value crosses
the status API, and get/set/remove, storage, and error behavior remain intact.

| SHA-256 | Accepted product path |
|---|---|
| `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db` | `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` |
| `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4` | `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` |

## Accepted proof loop

- Bounded implementer `TASK-PKG04-API-KEY-STATUS-SOURCE-IMPLEMENT-02`:
  `SUCCESS`.
- Focused storage Vitest: PASS, 20/20.
- Full frontend Vitest: PASS, 150 files and 1,167 tests; 1 file and 4 tests
  skipped.
- Frontend/Electron typecheck and build: PASS.
- Practitioner harness: PASS, 350 tests.
- Repository self-check: PASS, exit 0; unchanged unrelated baseline of
  4 REVIEW / 31 WARN.
- APP-HOLD integrity: PASS; reliance ALLOW for DEL-04-05, DEL-02-05,
  DEL-09-06, and DEL-09-04.
- Secret scan before review: PASS, 5,833 files, zero blocked findings.
- Post-calibration secret scan: PASS, 5,839 files, zero blocked findings.
- Explicit scope and whitespace checks: PASS, zero violations.
- Frozen identity: `FROZEN_DIFF_MANIFEST_V3.md`, 12 subjects.
- Fresh Review 03 `TASK-PKG04-API-KEY-STATUS-SOURCE-REVIEW-03`: PASS,
  12/12 hashes matched, both source/test files and exact diff reviewed 100%,
  daemon serialization/N2 consumer trace passed, zero findings.

## Deliverable calibration

- `Evidence_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20.md`, `_STATUS.md`, and
  `MEMORY.md` now record the amended store-owned source fact and Review 03.
- DEL-04-05 remains `IN_PROGRESS`; `## Remaining` stays empty.
- Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- No lifecycle, dependency, lockfile, root runtime contract, IPC, other
  package, shared fan-in, receipt, completion-log, Git, push, or PR action was
  performed.

## Exact N2 handoff

Daemon `credentialStatus` runtime responses now carry non-secret
`source: 'ui' | 'env' | 'none'`. N2 must validate and consume this store-owned
field in its local IPC consumer, remove environment-based source re-inference,
and preserve structured daemon-unavailable behavior plus store/remove
contracts. Its focused proof must show simultaneous persisted UI and
environment credentials report `ui`, environment-only reports `env`, none
reports `none`, and no credential material is exposed.

Blockers: none within amended N1.
Human rulings needed: none.
Rerun: none while all twelve frozen v3 subjects remain byte-identical. Any
changed product/test or frozen evidence subject requires proportional checks,
a new manifest, and fresh review.
Next owner: Agent 0 may accept this terminal handoff and release N2.
