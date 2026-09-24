# Evidence portability repair diagnosis and handback

Candidate: `b92f250655d4a28fca93c9990e27025c15b7b877`. Executor `/root/live_manager/portability_repair`, TASK Type 2 child of `/root/live_manager`; delegated-harness-native execution, no descendants. Parent authorized evidence-only placement repair. Host permissions remain the enforcement boundary.

The original GEN8 failure reported 29 surfaces. A focused read-only probe using the existing `surface_roles` policy classified 23 as UNCLASSIFIED and six as CONTROL. Machine-specific execution roots and supplier source origins had been stored on active surfaces. Confidence is high: each original hit is enumerated in [MOVE_MANIFEST.json](MOVE_MANIFEST.json), and the unchanged classifier recognizes the raw destinations as evidence. No policy, test, harness or protected criterion changed.

Each original was moved byte-for-byte to one canonical raw record under `_run_records`; the old evidence path is a portable pointer. Six controls retain their complete operative text with portable root/supplier anchors and a historical-original pointer. Neutral raw filenames denote immutable execution snapshots, not relocated active controls; CONTROL filename precedence was explicitly checked. This does not change or reissue the historical briefs.

Every old path remains resolvable. To consume original JSON schemas or historical hash references, follow the pointer to the canonical raw bytes. `original_reference_base` from the manifest records the original document directory and applies only to otherwise document-relative links, never the raw storage directory. Explicit schema/field roots and declared repository, project, package, bundle or temporary-directory bases take precedence; repository-relative paths and absolute historical identities retain their original meaning. Existing historical source/hash rows remain unchanged and identify original bytes. This explicit indirection avoids silently rewriting historical provenance or duplicating packets.

Verification: all 29 raw files equal both their pre-move bytes and `HEAD` originals; all 29 pointer targets exist; all raw destinations classify EVIDENCE. Focused owned-tree scan finds zero remaining machine-path hits on CONTROL/UNCLASSIFIED surfaces. [Detailed verification](_run_records/focused-verification.json). Original failed pytest output is retained at [_run_records/original-gen8-failure.log](_run_records/original-gen8-failure.log); external source log was left untouched.

Source-only readiness: evidence repair is ready for manager independent review and full GEN8 rerun. No product source, configuration, Git index/revision, build, product test, browser, native process or endpoint was changed/executed. The focused probe is not a full GEN8 pass or acceptance claim. Full GEN8 remains manager-owned.

| ID | Original within LIVE_MANAGER | Role | Canonical raw record |
|---|---|---|---|
| 1 | `IMPLEMENTATION/DELEGATION.json` | UNCLASSIFIED | [`record-01.json`](_run_records/record-01.json) |
| 2 | `IMPLEMENTATION/FRONTEND/ACK.md` | UNCLASSIFIED | [`record-02.md`](_run_records/record-02.md) |
| 3 | `IMPLEMENTATION/MANAGER_ACTIVATION.md` | UNCLASSIFIED | [`record-03.md`](_run_records/record-03.md) |
| 4 | `IMPLEMENTATION/NATIVE/ACK.md` | UNCLASSIFIED | [`record-04.md`](_run_records/record-04.md) |
| 5 | `IMPLEMENTATION/NATIVE/FIXTURE_CLEANUP_REPAIR.json` | UNCLASSIFIED | [`record-05.json`](_run_records/record-05.json) |
| 6 | `IMPLEMENTATION/NATIVE/REPAIR_PLAN.json` | CONTROL | [`record-06.json`](_run_records/record-06.json) |
| 7 | `IMPLEMENTATION/NATIVE/REPAIR_RUNS.json` | UNCLASSIFIED | [`record-07.json`](_run_records/record-07.json) |
| 8 | `IMPLEMENTATION/NATIVE/RUNS.json` | UNCLASSIFIED | [`record-08.json`](_run_records/record-08.json) |
| 9 | `IMPLEMENTATION/REVIEW/BACKCHECK_ORIGINS.json` | UNCLASSIFIED | [`record-09.json`](_run_records/record-09.json) |
| 10 | `IMPLEMENTATION/REVIEW/CONSULTED_SOURCES.json` | UNCLASSIFIED | [`record-10.json`](_run_records/record-10.json) |
| 11 | `IMPLEMENTATION/REVIEW_BRIEF.md` | CONTROL | [`record-11.md`](_run_records/record-11.md) |
| 12 | `INTEGRATION/NATIVE/ARTIFACTS.json` | UNCLASSIFIED | [`record-12.json`](_run_records/record-12.json) |
| 13 | `INTEGRATION/NATIVE/PRE_RUN.json` | UNCLASSIFIED | [`record-13.json`](_run_records/record-13.json) |
| 14 | `INTEGRATION/NATIVE/RUNS.json` | UNCLASSIFIED | [`record-14.json`](_run_records/record-14.json) |
| 15 | `INTEGRATION/NATIVE/SELF_TEST/RUN_RESULT.json` | UNCLASSIFIED | [`record-15.json`](_run_records/record-15.json) |
| 16 | `INTEGRATION/NATIVE/SELF_TEST/RUN_STARTED.json` | UNCLASSIFIED | [`record-16.json`](_run_records/record-16.json) |
| 17 | `INTEGRATION/NATIVE_BRIEF.md` | CONTROL | [`record-17.md`](_run_records/record-17.md) |
| 18 | `INTEGRATION/REVIEW/BRIEF.md` | CONTROL | [`record-18.md`](_run_records/record-18.md) |
| 19 | `INTEGRATION/REVIEW/MANIFEST.json` | UNCLASSIFIED | [`record-19.json`](_run_records/record-19.json) |
| 20 | `PACKAGING/ARTIFACTS.json` | UNCLASSIFIED | [`record-20.json`](_run_records/record-20.json) |
| 21 | `PACKAGING/DESIGN/SOURCES.json` | UNCLASSIFIED | [`record-21.json`](_run_records/record-21.json) |
| 22 | `PACKAGING/REPAIR/NATIVE/IMMEDIATE_PRE_NORMAL_BUILD.json` | UNCLASSIFIED | [`record-22.json`](_run_records/record-22.json) |
| 23 | `PACKAGING/REPAIR/NATIVE/PRE_EDIT.json` | UNCLASSIFIED | [`record-23.json`](_run_records/record-23.json) |
| 24 | `PACKAGING/REPAIR/NATIVE/RUNS.json` | UNCLASSIFIED | [`record-24.json`](_run_records/record-24.json) |
| 25 | `PACKAGING/REVIEW/BRIEF.md` | CONTROL | [`record-25.md`](_run_records/record-25.md) |
| 26 | `PACKAGING/REVIEW/SOURCES.json` | UNCLASSIFIED | [`record-26.json`](_run_records/record-26.json) |
| 27 | `PACKAGING/SELF_TEST/BRIEF.md` | CONTROL | [`record-27.md`](_run_records/record-27.md) |
| 28 | `PACKAGING/SELF_TEST/RUN_RESULT.json` | UNCLASSIFIED | [`record-28.json`](_run_records/record-28.json) |
| 29 | `PACKAGING/SELF_TEST/RUN_STARTED.json` | UNCLASSIFIED | [`record-29.json`](_run_records/record-29.json) |

## Manager verification

The unchanged GEN8 invariant now passes: one test, exit0. Exact command, original failure and resulting raw pass are retained under `_run_records/gen8-result.json` and its links. Manager checked all29 moved originals against b92 and all portable-surface hashes, confirmed exact owned-only scope and unchanged product/harness/skill paths. Independent review remains pending at this authored return; the focused probe was not used as a substitute for this actual GEN8 execution.
