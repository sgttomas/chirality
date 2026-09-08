# TASK launch brief — D85 store guard author

RequestedBy: WORKING_ITEMS. RunID: P1_STORE_GUARD_01.
ParentInstanceID: pec_d85_production. ChildInstanceID: AUTHOR.
PackageID: PKG-01. DeliverableIDs: DEL-01-03.
TaskSkill: software-bounded-implementation. ApplyEdits: true.
Model request: gpt-5.6-sol. Reasoning: medium. ForkTurns: none.
Role and non-delegation evidence: instruction-asserted; this Agent 2 must not
delegate.

ScopePath and DeliverablePath:
`{WORKING_ROOT}/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard`.
WORKING_ROOT: `{REPO_ROOT}/projects/pec`.

Objective: implement the exact D-PEC-85 P-A first store lifecycle and
content-minimal guard slice after the manager-owned store-check registration.

AcceptedBasis: merged `D-PEC-85_RULING_2026-09-08.md`; exact selected V2
proposal SHA-256 `0da4d163c5d36fde15d7336256f412c1f31a6ac4e5d60c1d55c8e388c000541b`;
DEL-01-03 ScopeOfWork.md; accepted decomposition revision 1.4; manager
activation, preimage, preflight, work graph, and check-registration records in
`_run_records/P1_STORE_GUARD_01/`.

AllowedWriteTargets, exactly:

- `{WORKING_ROOT}/v2/src/pec_v2/core/ports/store.py`
- `{WORKING_ROOT}/v2/src/pec_v2/core/content_minimal_guard.py`
- `{WORKING_ROOT}/v2/src/pec_v2/adapters/storage/__init__.py`
- `{WORKING_ROOT}/v2/src/pec_v2/adapters/storage/sqlite_store.py`
- `{WORKING_ROOT}/v2/tests/storage/test_store_lifecycle.py`
- `{WORKING_ROOT}/v2/tests/storage/test_content_minimal_guard.py`
- `{WORKING_ROOT}/v2/docs/STORE_LIFECYCLE_AND_GUARD.md`
- `{WORKING_ROOT}/.gitignore`
- `{ScopePath}/_run_records/P1_STORE_GUARD_01/children/AUTHOR/**`

The manager exclusively owns `software-workflow.json`; do not edit it.

Implementation requirements:

- Provide a core-owned typed store capability for batch admission, readback,
  explicit located failures, close, safe delete/reset, and empty recreation.
  Consumer signatures expose no SQLite connection, engine, or concrete path.
- Use only Python standard-library SQLite, at the adapter default
  `.pec-v2/record_store.sqlite3`. Runtime code must not rewrite governed source.
- Route every persistence write through one content-minimal guard. Use an
  explicit field-class enum and runtime type/domain checks. A metadata-looking
  key never authorizes its value. Reject unknown field classes, raw prose, and
  caller-supplied permissive policy.
- Admit only source-cited, tightly validated metadata: normalized
  repository-relative paths, nonnegative integer counts excluding booleans,
  explicit SHA/hash value types with finite formats, and a finite documented
  KnownState vocabulary. Unsupported or prose-derived state values return a
  located limitation under CON-001.
- Persist only generic guarded metadata envelopes, without defining the
  fourteen DEL-01-01 entities or domain DDL. Preserve accepted/rejected
  accounting; a rejected record leaves no residue and causes no silent loss,
  truncation, or substitution.
- Tests use temporary isolated scratch Git checkouts only and must cover
  ignored database/journal/temp artifacts, creation, restart, closed and open
  reset/delete, empty recreation, interface isolation, admission/readback,
  explicit record+field rejection, atomic no-residue behavior, accounting,
  three test-local reconciler/presence/event stand-in shapes sharing the same
  boundary, no dependency/network call, and VER-001..009 mapping.
- Append only `/.pec-v2/` to `.gitignore`.
- Documentation records the interface and lifecycle, field-class decisions
  against PRD §7.1/§7.2, exact requirement-test mapping, CON-001 limits, and
  the boundaries: no real consumers, entity model, parser, reconciler,
  orientation, daemon, runtime integration, kill/parity result, full
  DEL-01-03, or P1 completion.

Authorized registered checks: use the project profile from cwd
`{WORKING_ROOT}`. Select affected checks with project-relative paths, then run
only the resulting `v2-store-guard`, `v2-api-contract`, `v2-core-posture`,
`v2-loop-registry`, and `harness-self-check` entries through
`run_registered_checks.py`. Record Python version, exact commands, exit codes,
and normalized outputs. Run `validate_change_scope.py` against the eight
product paths plus this child evidence directory. Run `git diff --check` and
default `validate_candidate_whitespace.py --base-ref origin/main`, including
untracked files, before sealing.

ExpectedReturn: implemented paths and behavior; normalized check evidence;
scope validation; requirement/test map; residual risks and blockers. Output
manifests must recursively include nested manifests and exclude only their own
root manifest. Do not claim acceptance, merge, lifecycle promotion, release,
system kill/parity, D83 inquiry completion, full DEL-01-03, or P1 completion.

Escalation: stop and return the exact question if an admission needs a data
class outside the five PEC-K-10 classes, if any write target must expand, or if
the strict guard cannot support the bounded demonstration without adding a
parser, entity model, or consumer integration.
