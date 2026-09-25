# Scientific foundation integration-context review

**No unresolved actionable integration finding.** Candidate
`0a2710fe75c0000af5fd20253f1b4c95a87ea924` (draft PR901), directly based on
`eec2855d829d9cd3704892fc7d603562fbd39b88`, is covered by this context review
together with the earlier complete foundation review. This clears the scoped
review only. Actual-head required CI, clean DEC-025 and practitioner gates are
still required; this return does not establish merge readiness by itself.

During this review, ROOT relayed an actual governance failure on `0a2710…`:
`ABS_PATH_IN_UNCLASSIFIED_SURFACE` at line 80 of
`INDEPENDENT_REVIEW/INTERMEDIATE_REPAIR_CHECKS.json`, where a literal captured
process log tail contains its original `/private/tmp` path. The reviewed narrow
repair relocates that record, byte-identically at SHA256
`ff6de732b86133dd84bb30243faae5d297020b3f8d3f00a59bac00a0b6000338`,
to `INDEPENDENT_REVIEW/_run_records/INTERMEDIATE_REPAIR_CHECKS.json` and changes
only its path in HANDOFF_WHITELIST. Existing harness classification designates
that structural folder as evidence. No raw output, source, test, tolerance or
policy is changed. The working delta is independently clear; its final commit
identity and actual-head CI rerun remain pending. The reported CI outcome is a
ROOT relay, not newly acquired remote evidence by this reviewer.

Executor `/root/physics_resume/joined_consumer_review` remains independent TASK,
original actual parent `/root/physics_resume`. ROOT directly assigned this
cross-manager integration review. The reviewer did not implement the foundation
or perform the cherry-pick. No delegation, source edits, heavy tests/build,
native UI, network or Git mutation occurred. Only this PRIMARY evidence
directory was written. PR901 was attached to the current task through the app
artifact tool; no GitHub operation was performed.

## Exact change and source coverage

The actual candidate-parent diff has **72 paths**, the same complete path set as
the reviewed `05a9baa3342e8a322536ce2286f4189553d43eec` foundation commit over
its `0a438…` base. Every one of the 72 candidate blobs matches that commit
byte-for-byte, and the clean working tree matches those candidate blobs. All ten
source/test/documentation files match SOURCE_FREEZE_04 and the prior independent
FINAL_CHECKED_BASIS. The other 62 paths preserve the same review, source-freeze,
failure, repair and executed-check evidence. No extra product, fixture, lock,
instruction or graph change was introduced.

The initial clean check preceded the evidence relocation above. The final
working-tree comparison permits exactly that relocation and its sole whitelist
path update; all ten source hashes and every other candidate blob still match.

The four modified-path preimages—Cargo.toml, adapter.py, lib.rs and the explicit
build helper—are themselves identical between the old reviewed base and current
main. Thus the cherry-pick does not compose a hidden edit into an existing
function. The old Rust library body and Python adapter prefix remain unchanged;
the historical CLI, canonical crate lock, checked-profile tests, old Python
adapter tests, test-session hook and canonical-hash corpus also match both
bases. `CHECKED_MANIFEST.json` binds every changed path and relevant context.

## Current context checked

Current-main callers continue to select their existing APIs. Python AnalysisRun
still imports `canonical_sha256_checked_v1` and names the I-JSON profile. The
desktop hash service and operation-applier WASM exports still expose/call the
unrestricted or checked-v1 routes; no binary64 export or runtime fallback was
added. The new symbol/profile search finds only the standalone authority, CLI,
adapter, its explicit build selection and dedicated tests. No solver, native
request/result carrier, Current/rule/export or SI-unit adoption occurs here.

The existing pytest controller still calls `build()` without a profile, which
selects the historical executable. The dedicated scientific test fixture selects
the new executable explicitly. The build script keeps separate environment
variables/executable names and defaults, and neither runtime adapter builds or
retries a different profile. Cargo dependency versions/features and lock data
are unchanged; the crate has only additive modules and a separately named
feature-gated CLI target.

Two relevant current-main differences from the original numerical branch were
inspected. Current main does not contain `canonical_json/tests/precision_transport.rs`
or the numerical-branch mechanics-generation JavaScript helper; its existing
package command directly runs the product example. This PR neither deletes nor
reintroduces those separate branch contributions. Its new tests depend only on
the present unchanged canonical corpus, old checked adapter and standard test
setup. The prior 24-Rust-test count includes that absent transport test and must
remain an observation of the original source checkout, not an asserted count
for this integration candidate.

The registered core/tests path rules still require Python/evidence-sweep checks;
the current CI numerical discovery and release/sweep paths were inspected for
their actual candidate responsibility. No passing gate was inferred from those
definitions. Shared Rust compilation and the packaged application build may be
affected by adding a module, so fresh registered compilation/build gates remain
necessary even though runtime profile selection is unchanged.

## Evidence reuse and limits

The original **24 Rust / 55 Python passes and 547-token conformance** remain
reusable evidence for the identical foundation implementation at their recorded
source/runtime scope. Both original resource findings and their final fixes are
preserved. The earlier full code/conformance review was not repeated, and no
new runtime pass is claimed here. Required current-candidate checks must record
their own actual counts, selected source identities, failures and limits.

Whole-diff whitespace checking reports retained `.patch` context-line spaces
and raw-log trailing blank lines only; these are preserved evidence bytes.
The ten owned source/test/documentation paths pass the scoped whitespace check.
This distinction is recorded rather than rewriting historical evidence to
silence a cosmetic report.

An actual native workflow is not established or newly activated by this
standalone change. There is no new user-facing native path to qualify here;
existing required build/regression/native obligations still follow the actual
candidate policy. Later native/WASM binding, typed field inventories, source
custody, computed-zero projection, scientific SI publication and consumer
adoption need their own authorized review and witnesses. This review does not
repair the original product large-real refusal or confer numerical accuracy,
engineering acceptance or release authority.
