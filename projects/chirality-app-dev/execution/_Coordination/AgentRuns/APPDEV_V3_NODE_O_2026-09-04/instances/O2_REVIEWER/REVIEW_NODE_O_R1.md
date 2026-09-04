# Independent review — Node O DEL-09-01-V3-01 revision 3

## Verdict

**PASS**

Finding count: **0 BLOCKER, 0 MAJOR, 1 MINOR, 3 NOTE**.

This verdict is over frozen basis `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40` and frozen candidate head `c32c5ae668b9d44115c28a96839917f2ffe4c950`. The review was performed read-only from the separately created detached worktree `/private/tmp/chirality-app-v3-section8-rev3-20260904/nodeO-review-r1`. I did not delegate, edit tracked repository files, push, open a PR, alter a status/receipt, or remove the review worktree.

## Findings

### MINOR O-R1-M1 — machine-absolute interpreter path in a coordination instruction

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_O_2026-09-04/REVIEW_O2_HANDOFF.md:17` embeds `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3`. `docs/SPEC.md` §0.2.4 says instruction, coordination, and plan files MUST NOT embed machine-absolute paths; those paths are permitted only in run records and evidence artifacts where they record completed execution.

Impact is limited to portability and host-identifier hygiene. It does not affect the revision-3 evidence, source/evaluator identities, comparison, or independently reproduced behavior. Replace the literal path with a portable Python-3.13 requirement or placeholder during the post-review narrative rebase, and update the Node O coordination manifest. Runtime evidence does not need to be reminted.

### Notes

1. The retained failed attempt's two-entry per-run manifest intentionally covers only `artifacts/**` and `logs/**`; its empty `private/lsof-port-52126.stderr` is outside that per-run scope but is covered and verified by the 383-entry outer evidence-bundle manifest. This is not an integrity gap.
2. The review's first sandboxed full-Vitest execution failed only because TCP and Unix-socket `listen` calls were denied with `EPERM`. The required host-permitted rerun passed the complete suite. The initial frontend install likewise encountered sandbox DNS denial, then succeeded with the exact approved network retry. Neither is a product/evidence failure.
3. Current `origin/main` is `745e3b7ba088a0ffcc9c16030efcc48aa1e706d7`, solely PR #697 after the evidence basis. Its complete diff from `e2f8317da` is two modified plan files. This is non-triggering and permits an evidence-preserving narrative-only rebase after PASS.

## Frozen diff and scope review

- Reviewed 100% of `git diff e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40..c32c5ae668b9d44115c28a96839917f2ffe4c950`, including every commit and changed file.
- Commit inventory: exactly one commit, `c32c5ae668b9d44115c28a96839917f2ffe4c950` (`evidence(app): record Section 8 revision 3 after CSP merge`).
- Diff inventory: 89 files, 6,024 insertions, 4 deletions; 87 added and 2 modified. Binary-form diff SHA-256: `b61f624f93aa2e79f8d76fdfe1f77bff167e9351cae9a5bb48094fd00876762a`.
- Every changed path is under either the DEL-09-01 evidence/run-record locus or `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_O_2026-09-04/`.
- Exact `validate_change_scope.py` invocation with the frozen basis/head and those two allowed roots: `PASS`, `violations: []`.
- No tracked `frontend/**`, `runtime/**`, `.github/**`, product, test, CSS, runner, comparator, workflow, package manifest, or lockfile byte changed.
- `_STATUS.md`, `MEMORY.md`, and `loop/LOOP_RECEIPTS.md` are byte-unchanged across the candidate. O1 remains `REVIEW_READY`; O2 remains `pending_dispatch` with no verdict. There is no premature closeout.
- `git diff --check`: PASS. Final tracked status in the detached checkout: clean.
- Visual review: **N/A**. The candidate contains no tracked UI, CSS, geometry, copy, control, or other product byte.

## Selectability and governance boundaries

- Accepted revision-2 application basis is `ede175910c67b384332324622b17695f69e6a715`.
- PR #695 merged at `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40` and changed the named trigger paths `frontend/electron/main.ts` and `frontend/electron/renderer-window-policy.ts`, plus five related frontend/test files. DEL-09-01-V3-01 revision 3 was therefore selectable and non-vacuous.
- PR #696 is already included in the basis and is confined to `projects/chirality-app-dev/plans/shell-redesign_2026-09-04/**`; it is not a revision trigger.
- The A1 declaration is accurate: proof execution writes ignored/generated `frontend/**`; historical R20 remains historical; this evidence is not owner proof and confers no future reliance entitlement.
- APP-HOLD scan at frozen head: `PASS`, 53 contracts, 0 held, register match, register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`.
- APP-HOLD dispatch and review reliance preflights for DEL-09-01: `ALLOW` / `ALLOW`.
- DEL-09-01 ScopeOfWork validation: `SOW_V1`, valid, no issues.
- Receipt validator: `VALID`, frozen through Receipt-52.
- Authority corpus: current `v20`; all eight sources match; no drift.
- RQG §13 mapping accurately separates the DEL-09-01 contribution from unproved live-provider, model-switching, PEC, export, and other owners' surfaces.
- F-APP-2 semantic review found only explicit boundary/negative statements and named validation surfaces. The candidate makes no release, lifecycle, G5/G6a, signing, notarization, publication, distribution, certification, professional-approval, packaged-app, host-act, or release-readiness claim.

## Source, evaluator, runner, and comparator identity

- `EVALUATOR_BYTES_revision3.tsv` was independently recomputed against `ede175910` and `e2f8317da`: all 19 rows match their Git blobs and current SHA-256 values; 12 evaluator/input rows are `SAME`, and exactly the seven PR-#695 trigger rows are `CHANGED`.
- `EVALUATOR_BYTES_revision3.tsv` SHA-256: `b7061660d827ffb03c5806c030cca98e8947fa5cf952ed7c746c41c631257d16`.
- Accepted revision-2 runner commit: `9dfbb7962cd22b56b1899d10c05c3e97f2a10d2f`.
- `rerun-section8-local.sh` is byte-identical at the accepted runner commit and the revision-3 application basis; SHA-256 `81e662a81aa750e943b19761a622040d9edb5cd783ac35913959a7caecf8b109`.
- `compare-section8-summaries.py` is likewise byte-identical; SHA-256 `91d4a395621e0a0a89625f01beccbc4b1708e4b5f8eb0bd48b3abf389db51e05`.
- The committed comparator was independently replayed with the retained relative path form and reproduced `COMPARE_RESULT_revision3.txt` byte-for-byte. Its behavior projection is equal to accepted revision 2, contains the exact eight required rows in order, requires every status to pass, and excludes the retired legacy row.

## Retained revision-3 evidence

- Successful retained run environment: clean exact application basis `e2f8317da`; Darwin 25.6.0 arm64; Node 24.18.0; npm 11.16.0; Electron 43.2.0; Next 15.5.21; Vitest 4.1.10; stub provider; disposable user data; mock keychain; port 52127; release quality enabled.
- Retained Section 8 stable summary: `pass`, 8/8 required rows, SHA-256 `ee89c9ce35acbdfb09c7ba44b354e35a86aa9db7d557f92d85080081270bbc82`.
- Retained release-quality summary: `pass`, `releaseClaim: false`, SHA-256 `c8599f2f5580b109718a854cf8ad19aef363d4eecaec703428e34b39a13b07ac`.
- Retained bundles: Electron main `a3c3309f93c99d96b9d3be6b573e9e9d52a592086c590c47cdef749ac9718180`; CLI `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.
- Retained successful run manifest: 63 entries, exact `artifacts/**` plus `logs/**`, path-sorted and checksum-valid; manifest-file SHA-256 `14291495dfb8f270631143a02cc869969af599e72b56b6848a4f196b9f0edb82`.
- Retained failed-attempt manifest: 2 scoped entries, path-sorted and checksum-valid; manifest-file SHA-256 `0796ec9595f58d61553c51811823fa72b6502832d6033f9642b554e16bf0600e`.
- Evidence-bundle manifest: 383 entries, exact bundle membership excluding itself (including nested manifests), path-sorted and checksum-valid; manifest-file SHA-256 `444d99e40e9cd0749153beec1869875676e97209dfb97c873b3b52edfb99f8e8`.
- Node O AgentRuns manifest: 13 entries, exact package membership excluding itself, path-sorted and checksum-valid; manifest-file SHA-256 `d05f881ae9b745070b708cda318781610853c163d68bce236f60e10fdee8cf5d`.
- All 35 changed JSON files parse; the strict check rejected duplicate keys and non-finite constants. All five changed SSE files contain valid JSON in all 37 `data:` records.
- Secret scan: zero blocked findings. Retained registration has only `projectId`, `clientId`, token-file path, and project-manifest hash; no token value is preserved. Host-identifying values in actual run evidence are limited to explicitly disclosed scratch/tool paths and local `lsof` usernames. O-R1-M1 is the one coordination-file exception.
- Honest first attempt: exit 74 before build/daemon launch because `Electron.app` was absent; supervisor recorded empty final coalition, no listener/socket, and removed its temporary root. No pass was inferred.
- Electron materialization is reproducible and package-native: cached `electron-v43.2.0-darwin-arm64.zip` SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28` matches `node_modules/electron/checksums.json`; `node node_modules/electron/install.js` materialized the app. I independently repeated that checksum check and installation route.

## Independent build and test reproduction

- Runtime `npm ci --ignore-scripts` and `npm run build`: PASS.
- Frontend `npm ci --ignore-scripts`: PASS after the approved network retry.
- Electron cached archive checksum and package-native installer: PASS.
- Frontend typecheck: PASS.
- Exact retained focused set: 4 files, 83 tests: PASS.
- Broader impacted focused set: 4 files, 99 tests: PASS.
- Full frontend Vitest with required host bindings: 165 files passed, one declared suite skip; 1,567 tests passed, four declared skips.
- Frontend production/Next/Electron build: PASS.
- Rebuilt bundle SHA-256 values exactly equal the retained revision-3 bundle hashes.
- Registered Python 3.13.14 checks: harness self-check exit 0 (known repository baseline only), app-hold-integrity PASS, practitioner-harness pytest 350 passed.
- Frontend repository secret scan after the independent run: 7,485 files scanned, 0 blocked findings, 26 allowed fixtures.

## Independent real-daemon reproduction

The unchanged retained runner was executed from exact frozen checkout `c32c5ae668b9d44115c28a96839917f2ffe4c950` with fresh external output root `/private/tmp/chirality-nodeO-r1.1c8FcM/run`, port 52129, `WITH_RELEASE_QUALITY=1`, `SKIP_BUILD=0`, and disposable user data.

Results:

- Runner exit: 0.
- Environment records exact frozen head and zero tracked dirty paths before and after.
- Real Electron daemon started over its disposable Unix socket; project registration used the bundled CLI; Next served on 127.0.0.1:52129.
- Premerge: exit 0; Section 8 `pass`, 8/8; Section 9 `pass`, 16/16 in report-only premerge posture.
- Release quality: exit 0; full test, typecheck, standalone-blocking Section 9, premerge, and both summary-consistency checks pass; `releaseClaim: false`.
- Independent three-way comparison (fresh run, retained revision 3, accepted revision 2): `BEHAVIOUR_PROJECTIONS_EQUAL=true`, exit 0, exact ordered eight-row projection.
- Fresh run manifest: 63 entries and exactly 63 files under `artifacts/**` plus `logs/**`; all checksums pass. Manifest-file SHA-256 `2c25347b24d8e5757495b794c519a31070055f0efbcb271d86be051ab2a565e5`.
- Fresh stable summary SHA-256 `0d358aba46ab999999c790d9e30da62eba5146228841216947c0a1ae9ad6a794`; differing run-specific bytes are expected, while the behavior projection is identical.
- Fresh release-quality summary SHA-256 `babdee51fb7a09c90664ec3d104401699bdb53a953a4c810b54685624c5054c3`.
- Fresh captured JSON parses; five SSE files contain 37 valid JSON `data:` records; secret-pattern scan passes.
- Containment: daemon exposed no TCP listener; its control socket was 0600 and runtime directory 0700; only the Next server listened on the selected loopback port.
- Continuous descendant audits recorded 634 daemon and 599 Next samples with zero violations.
- Cleanup: both process groups empty; coalition sweep passed after three consecutive empty observations; final coalition empty; final port-listener count 0; socket absent; transient LaunchAgent absent; user-data root, harness temp root, private registration bytes, and temporary LaunchAgent root absent.

## Main-advance disposition

`origin/main` advanced from the evidence basis only through PR #697 (`745e3b7ba088a0ffcc9c16030efcc48aa1e706d7`). The complete advance is:

- `M projects/chirality-app-dev/plans/shell-redesign_2026-09-04/05_LOGO_AND_BRAND.md`
- `M projects/chirality-app-dev/plans/shell-redesign_2026-09-04/README.md`

No named DEL-09-01 revision-trigger, source/evaluator, runner, comparator, product, runtime, test, or workflow surface changed. Therefore PR #697 is non-triggering. **A narrative-only rebase after this PASS is permitted and owed; revision-3 runtime evidence must not be reminted.** The rebase should also resolve O-R1-M1 and refresh only the affected coordination/narrative manifest and later authorized closeout material.
