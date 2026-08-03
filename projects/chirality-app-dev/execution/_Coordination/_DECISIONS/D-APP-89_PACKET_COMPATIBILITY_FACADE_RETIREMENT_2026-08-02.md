# D-APP-89 — App Compatibility-Facade Retirement Readiness

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-02 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Task Management link:** `TM-APP-031`

## 1. Decision requested

Choose whether to retire now, retain while completing the migration, or defer
the deprecated App package `@chirality/harness-contract`, which currently
re-exports Root-owned `@chirality/runtime-contracts`.

## 2. Authority and current evidence

| Evidence | SHA-256 | Current fact used |
|---|---|---|
| D-APP-49 ruling | `41e15c39a2fb307c13c24e337265586472fbc0dc21a71f4fb2d370efe97ea1dc` | Historical authority for the two accepted inert contract shapes; it is not current location authority. |
| D-APP-73 ruling | `8431b4d65bf980cd79e3f89ea7d4549757097cff9945335376d7daf560073836` | Prospectively rehomes generic runtime contracts to Root and retains App compatibility integration. |
| D-APP-76 ruling | `26bd39e3d383d0f19bed695a2a1515642875894e52a3c13a73c02ee9dc2e5638` | Explicitly deferred facade retirement to a separate evidence-backed owner gate and lists its required evidence. |
| DEL-03-01 `_STATUS.md` | `328dd412f829f1cea44913449fb05df52165dbcd2cf927827dff8bd4bab6270b` | The sole Remaining item is retirement after the one-cycle compatibility window closes. |
| D49 audit `FINDINGS.csv`, `D49-003` | `eb88b15632a7dfedd772b5cc32496d58c3612231b7c5194474f04666db836597` | Completion of the migration and retirement readiness were not established; an execution-time census and separate gate are required. |

### Current consumer census at packet preparation

A live source search outside `frontend/packages/harness-contract/**` finds 106
direct TypeScript importers of `@chirality/harness-contract`:

- 67 production `frontend/src/**` files; and
- 39 `frontend/src/__tests__/**` files.

The package also remains wired into `frontend/package.json`,
`package-lock.json`, `tsconfig.json`, and `next.config.mjs`. The facade contains
13 exported source files whose runtime content is deprecated re-export
plumbing to `@chirality/runtime-contracts`.

This census proves that removal without a migration tranche would break the
current App. It is packet-time evidence, not the execution-time census required
by D-APP-76.

## 3. Options

### Option A — Retire now through one conditioned atomic tranche

Select retirement as the current objective. Before any deletion, the
execution tranche must:

1. repeat the full execution-time consumer census;
2. migrate every App source/test import to the equivalent
   `@chirality/runtime-contracts` root or subpath;
3. update `package.json`, lockfile, TypeScript paths, Next transpilation, the
   contract-dependency validator, and every current reference that would
   otherwise keep the facade load-bearing;
4. demonstrate zero remaining executable App consumers;
5. obtain the applicable Root owner confirmation required by D-APP-76; and
6. atomically remove the package with exact rollback bytes.

If any consumer lacks an equivalent Root export or the Root confirmation is
not available, the tranche stops without deleting the facade and returns to
the owner. Option A therefore selects a retire-now objective, not permission
to delete the present load-bearing package blindly.

### Option B — Retain for one additional bounded migration cycle (recommended)

Keep the facade in place and authorize a migration-only tranche that moves all
106 current importers and build/config consumers to
`@chirality/runtime-contracts`, while preserving the facade as a tested
rollback/compatibility path. Return a new execution-time zero-consumer census,
Root/App evidence, exact deletion/rollback manifest, and final retirement
packet to the owner.

This option makes the compatibility window measurable: it ends only after the
migration lands and a subsequent clean census proves the facade is no longer
load-bearing. It does not close DEL-03-01 or `TM-APP-031` yet.

### Option C — Defer migration and retirement

Keep current imports, package/config wiring, and facade behavior unchanged.
Name a future trigger. DEL-03-01 and `TM-APP-031` remain open, and no claim may
say the one-cycle migration is complete.

## 4. Required evidence for A or B

The migration package must provide:

- a path-complete before/after consumer census distinguishing production,
  tests, scripts/config, lockfile, and documentary/historical references;
- a mapping from every facade export/subpath used by current consumers to its
  Root-owned successor;
- a manifest of exact edited and, for A, deleted paths with SHA-256 values;
- source-versus-reliance distinctions, including a statement that historical
  D-APP/decomposition/evaluation references are not rewritten merely because
  the executable package retires;
- affected-client evidence showing no App, Root, PEC, Piping, or external
  production consumer is silently broken;
- exact rollback bytes and sequencing;
- Root package build/typecheck and focused export probes;
- App tests, typecheck, build, and packaged dependency verification; and
- release disposition stating that the work creates no release or reliance
  authority.

Minimum validation:

1. `npm --prefix runtime run build` and `npm --prefix runtime run typecheck`;
2. focused Root/App contract export and identity tests;
3. from App `frontend/`: `npm run test`, `npm run typecheck`,
   `npm run harness:validate:contract-deps`, `npm run build`, and
   `npm run desktop:pack`;
4. zero executable imports of `@chirality/harness-contract` for A, or a
   precisely enumerated rollback-only facade use for B; and
5. standing corpus, receipt, practitioner-harness, self-check, and Git
   closeout validation.

## 5. Risks and non-effects

- Option A is high-churn: 106 direct importing files plus package/config/lock
  surfaces must change atomically, and current packet-time evidence says the
  facade is not yet retirement-ready.
- Option B incurs one additional compatibility cycle but isolates migration
  risk from irreversible removal and produces the evidence D-APP-76 requires.
- Option C preserves known technical debt and prolongs two package names for
  one semantic contract.

No option rewrites D-APP-49, D-APP-73, or D-APP-76 history; changes Root
runtime semantics; resolves D-APP-48 successor identity; changes generic
runtime/sandbox/Bash posture; advances lifecycle; or grants release,
distribution, or professional reliance. Historical documentary references
remain historical unless separately governed. The six D-APP-81 unknown
relations remain untouched.

## 6. Non-binding recommendation

Select **Option B**. The current facade is still a load-bearing import and
build boundary, so retirement readiness is contradicted by the live tree.
Complete a bounded direct-import migration first, preserve rollback for one
cycle, then return the evidence-backed removal gate required by D-APP-76.

## 7. Owner return tokens

- `APPROVE D-APP-89 OPTION A`
- `APPROVE D-APP-89 OPTION B`
- `APPROVE D-APP-89 OPTION C — TRIGGER: <trigger>`
