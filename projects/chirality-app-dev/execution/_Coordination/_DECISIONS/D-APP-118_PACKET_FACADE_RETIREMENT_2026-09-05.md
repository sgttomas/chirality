# D-APP-118 — Facade retirement evidence and hold

Status: `PROPOSAL — AWAITING_RULING — RETIREMENT_NOT_READY`

Prepared 2026-09-05 by WORKING_ITEMS PKG-03 under HELP_HUMAN, D-APP-101.
No option is selected. Release disposition: **none**.

## Decision requested

Retain the facade and decide the later retirement preparation boundary. The
fresh census refutes an unqualified zero-consumer claim: the retained rollback
test imports 13 facade exports, and the contract-dependency validator requires
the facade directory and those 13 imports. A narrow deletion demonstrably
fails that validator. App and Root retirement rulings do not yet exist.

Non-binding recommendation: **Option A — hold deletion**, retain the tested
compatibility package, and require a separately bounded proposal for the
rollback-test and validator disposition plus current build/focused-test
evidence before reconsidering retirement. This packet supplies exact narrow
removal/inverse bytes as review material; it does not propose applying known
failing bytes. Option B is to defer reconsideration until a named owner
trigger. Neither option grants an App-to-Root write.

## Authority and immutable evidence basis

- D-APP-101 authorizes this packet only; D-APP-89 Option B retains the facade
  as a tested rollback path; D-APP-76 requires execution-time evidence and both
  applicable owner rulings before retirement.
- Source basis: `044a009e215e08b69c9e0887da424938a34aafcb`, branch
  `codex/app-loop-shell-20260905`. Accepted decomposition remains DEL-03-01's
  SOW basis at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`. The accepted
  dependency pointer names `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`.
  No prerequisite for Root v2 conformance is treated as satisfied here.
- Run snapshot: `execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg03_packet/`.
  `BRIEF.md`, `INPUT_IDENTITIES.json`, and `APP_HOLD.json` bind role/scope,
  1,047 source/authority identities, and the independent ALLOW reliance check.
  `evidence/MANIFEST.sha256` binds evaluator results, source-hit inventory,
  canonical command logs, candidate/inverse patches, and complete preimages.
  This is a derivative preparation snapshot, never decomposition truth.

## Fresh census and affected-client distinction

The evaluator searches all tracked live checkout files for the literal package
specifier and facade path, then separately inventories source/config/test hits
across App, runtime, tools, and project source roots. It found **348 matching
tracked files**. Most are governance, historical records, or copied evidence;
their existence is not an executable dependency. Exact paths/hashes are in
`evidence/consumer-inventory.json`; source lines and full search scope are in
`active-source-hits.json` and `source-search-scope.json`.

| Class | Finding and consequence |
|---|---|
| App ordinary product source | No literal facade import found. Ordinary production migration is supported by this bounded census. |
| App tests | `frontend/src/__tests__/lib/harness-contract-rollback.test.ts` has 13 dynamic import sites, one for each facade export. They remain executable consumers, not historical prose. |
| App validator | `frontend/scripts/assert-harness-contract-deps.mjs` reads the facade source directory, explicitly permits only the rollback test, and requires exactly 13 facade import probes. Deletion alone fails. |
| App package wiring | `package.json` generic `packages/*` workspace enrolls the only current App package; lockfile retains its workspace/link records. No root dependency on the facade remains. |
| Root runtime and clients | No literal executable facade importer found in tracked runtime source. Root tool-catalog's old source-path label is generated documentation text, not an import. Root contracts stay canonical. |
| PEC and other tracked clients | No literal executable importer identified by full-tree search. This is repository evidence; installed/out-of-repository consumers are unobserved and cannot be certified absent. |
| Piping / Tier 0 metadata | D-30 and D-APP-48 retain historical SHA-pinned package references. Piping explicitly records `runtimeDependencyInstalled: false`. The pull validator reads historical Git blobs, so deleting today's directory would not itself erase those pinned bytes. Existing successor/metadata disagreement remains governed by its own route. |
| History / source comments | Retained unchanged. `generate-tool-catalog.mjs` describes the old facade in a comment; neither that comment nor historical evidence is an executable consumer. |

Literal search cannot prove absence of external installations or arbitrarily
constructed dynamic specifiers. The known rollback/validator consumers already
make a literal zero-consumer assertion false; none were edited to force a pass.
After the parent's shared UI repairs, `FINAL_SOURCE_RECHECK.json` repeats the
active-source census over 1,034 tracked and nonignored untracked source/config
files: all literal source hits are identical to the initial census and all
16 candidate preimages remain unchanged. The original broad count remains a
dated tracked-tree inventory, not a claim that later evidence adds no matches.

`EXPORT_MAPPING.json` records all facade exports against Root's current package
manifest: 13 code exports have matching canonical subpaths. The facade also
exports its own `./package.json`; Root exposes no equivalent metadata subpath.
No caller of that metadata export was found. It is not included in the
13-probe runtime-identity claim and is not silently treated as equivalent.

## Exact narrow candidate and rollback

`evidence/candidate.patch` deletes 14 files under
`frontend/packages/harness-contract/` (package manifest plus 13 source files),
removes `workspaces: ["packages/*"]` from App `package.json` and the lockfile's
root package, and removes the lockfile's facade workspace/link entries. There
are **16 affected paths**, all App-owned. Generic workspace removal is valid
only for the current inventory, where this is the sole App package; rerun the
inventory before any future application. No Root file or successor identity
is changed. `change-manifest.json` records every pre/post SHA-256.

`rollback.patch` is the exact inverse; `preimage/` holds every original byte
and `postimage/` both edited JSON files. Disposable scratch proof:

1. Baseline contract-dependency validator: exit 0.
2. Candidate `git apply --check` and application: exit 0; all intended
   postimages verified byte-for-byte.
3. Candidate contract-dependency validator: exit 1 (`ENOENT` for the removed
   facade source directory). This is a predicted incompatibility, not a
   sandbox or dependency failure.
4. Inverse check/application: exit 0; all 16 preimages recovered exactly;
   restored validator exit 0. Scratch cleanup verified.

The rollback byte proof is complete. Runtime export-identity behavior still
requires the focused test evidence; inverse file restoration does not imply
that unexecuted tests passed. No candidate was applied to the working tree.

## Build and focused-test evidence

Parent-coordinated dependency restoration supplies exact-lock App dependencies
and built Root packages from `/private/tmp/chirality-dependencies-rrwmmitz`.
It does not change Root tracked bytes. `ROOT_EVIDENCE_BINDING.json` pins the
dependency-prep evidence; this manager independently rehashed its manifest and
all 79 current Root source identities. The temporary runtime must remain while
App's dependency links use it. Node v24.18.0, npm 11.16.0; package install scripts
were disabled. The initial absence of installed tools is superseded by this
documented environment, not by an inferred pass.

| Check | Result | Durable evidence |
|---|---|---|
| Root `npm run build` | PASS, exit 0, exact-source scratch runtime | Sibling `dependency_prep/RUNTIME_CHECKS.json` and `runtime-build-confirm` stdout/stderr |
| Root `npm run typecheck` | PASS, exit 0, same scratch | Same record and `runtime-typecheck` logs |
| Root `npm test -- tests/contracts-and-project.test.ts` | PASS, 10/10, same scratch | Same record and `runtime-focused-test` logs |
| App `npm test -- src/__tests__/lib/harness-contract-rollback.test.ts` | PASS, 13/13, original App cwd resolving the disclosed scratch Root packages | This instance's `focused_test/command.json`, `stdout.log`, `stderr.log` |
| App `npm run build` | Final PASS, exit 0; revised frozen shared App product tree, no inputs changed during check | `APP_FINAL_EVIDENCE_BINDING.json` pins parent `validation/build-02/` commands, source identities, environment and canonical logs |
| App `npm run typecheck` | Final PASS, exit 0 | Parent `validation/release-03/` registered result, release-quality summary and logs |
| App full Vitest / Section 9 | PASS, 1,622 tests / all 16 Section 9 checks | Same final `release-03/` evidence; full test command includes `--testTimeout=15000` |
| App premerge / release-quality wrapper | FAIL, exit 1; actual HTTP 503 `ENGINE_UNAVAILABLE`, runtime daemon client not configured; defer to PR CI under the documented missing-binding class | `release-03/binding-probe.json`, `registered-result.json` and canonical logs. This is not PASS or a retirement waiver. |
| Pure contract-deps candidate/inverse | Baseline PASS, narrow removal FAIL, restored PASS | Immutable `evidence/commands.json` and logs |

The App build/typecheck evidence above covers the parent's revised shared tree
after UI repair. This manager rehashed both final evidence inventories.
`APP_BUILD_EVIDENCE_BINDING.json` retains the earlier dated build separately;
the final binding supersedes it for fan-in. The premerge failure remains an
explicit environment limitation and no all-gates-pass claim is made.

These are retained-facade baseline checks. They do not prove the candidate
deletion works, establish Root acceptance of a supply unit, or replace the
later retirement gate. The known candidate failure prohibits a retirement-ready
conclusion regardless of eventual baseline App build results. No desktop pack,
release, or publication evidence is claimed for this packet.

## Draft Root request — not routed

To the Root coordination owner, through a future owner-granted App-to-Root
write: D-APP-76 requires a Root ruling on facade retirement. App's D-APP-101
preparation found no ordinary tracked production importer, but 13 rollback
imports and validator/package wiring remain. Review the exact D-APP-118
evidence snapshot and hold deletion pending an accepted App retirement packet,
current affected-client evidence, passing required Root/App checks, and a
separately scoped disposition for the rollback/validator consumers. No Root
runtime change, generic contract repin, D-APP-48 successor adoption, or
cross-loop implementation is requested by inference. The requested future
Root act must identify the exact acceptable retirement bytes and its scope.

Routing this text is `NOT_SELECTABLE_UNTIL: owner grants Root write scope`.
Its presence here is preparation evidence, not delivery, acknowledgement, or
an owner act. Deletion also remains gated on both later App and Root rulings.

## Handoff and rerun requirements

Closure verdict: preparation evidence produced; **retirement HOLD**. This
packet closes no DEL-03-01 lifecycle, changes no Checking Approval SHA, and
claims no release/distribution/professional reliance. The derivative package
is current only for the recorded source census; parent acceptance and
independent evidence review remain required. Recompute on source/import,
workspace/lockfile, validator, dependency environment, accepted upstream, or
owner-ruling change. `prepare_evidence.py --repo-root <checkout> --output
<new-empty-output>` reruns census, candidate, exact inverse and pure validator
proof in a disposable tree. Preserve each new result as a new snapshot; never
overwrite this evidence. To reproduce the recorded broad count of 348 rather
than a fresh census, use the clean recorded base commit: later committed
evidence itself adds documentary matches. Full build and focused-test reruns use the exact
commands/environment in their future parent-integrated evidence.
