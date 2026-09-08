# TASK launch brief — D85 store guard verifier

RequestedBy: WORKING_ITEMS. RunID: P1_STORE_GUARD_01.
ParentInstanceID: pec_d85_production. ChildInstanceID: VERIFY.
PackageID: PKG-01. DeliverableIDs: DEL-01-03.
TaskSkill: software-code-review. ApplyEdits: false.
Model request: gpt-5.6-sol. Reasoning: medium. ForkTurns: none.
Role and non-delegation evidence: instruction-asserted; this fresh Agent 2
must not delegate.

ScopePath and DeliverablePath:
`{WORKING_ROOT}/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard`.
WORKING_ROOT: `{REPO_ROOT}/projects/pec`.

Objective: independently review the frozen D-PEC-85 P-A implementation and
evidence for correctness, content-minimal bypass resistance, lifecycle safety,
scope compliance, and validity for WORKING_ITEMS technical fan-in. Report
defects to the parent; do not repair them.

ImplementationBrief:
`{ScopePath}/_run_records/P1_STORE_GUARD_01/children/AUTHOR/LAUNCH_BRIEF.md`.
AcceptedBasis: merged `D-PEC-85_RULING_2026-09-08.md`; exact V2 proposal;
DEL-01-03 ScopeOfWork.md; accepted decomposition revision 1.4; manager
activation/preimage/preflight/check-registration records.
DiffBasis: `origin/main` to the current working-tree candidate, limited to the
nine D85 product/configuration paths and authorized DEL-01-03 administration.
VerificationEvidence:
`{ScopePath}/_run_records/P1_STORE_GUARD_01/children/AUTHOR/**`.
PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`.

AllowedWriteTargets: only
`{ScopePath}/_run_records/P1_STORE_GUARD_01/children/VERIFY/**` for the durable
read-only review return. No product, configuration, status, memory,
coordination, receipt, or Git write is allowed.

Review all nine product/configuration paths and the author evidence directly.
Validate changed paths first. Trace the store interface, guard, persistence,
errors, lifecycle, and tests. Specifically assess:

- no raw or arbitrary prose can be admitted through misleading keys, forged
  dataclass values, mismatched classes, caller policy, or unsupported states;
- the five field classes have finite source-cited runtime domains and CON-001
  failures are located;
- every adapter record write passes one guard and rejected/duplicate records
  leave no residue with complete accepted/rejected accounting;
- effective ignore policy, later negation, and force-tracked store artifacts
  fail before directory creation or mutation; database, journal, WAL, shared
  memory, and temp shapes are covered;
- delete/reset/reopen behavior is safe for open and closed handles and tests
  operate only in temporary scratch Git checkouts;
- the core port leaks no SQLite, path, connection, or engine detail;
- there is no entity model, parser, reconciler, orientation, daemon, runtime
  integration, network call, third-party dependency, source rewrite, or
  scanner change;
- tests substantively execute VER-001..009 and do not merely self-assert
  mappings; documentation maps PRD §7.1/§7.2 honestly;
- normalized evidence is post-correction current, all five registered checks
  pass, scope validation is sound, default whitespace included untracked
  files, and the AUTHOR manifest is complete.

Use scope validation and affected-check selection as allowed by the skill.
Read code/tests/evidence directly. Do not run unregistered commands or change
the implementation. Persist `REVIEW.md`, normalized validation evidence, the
TASK run record, and a recursive `MANIFEST.json` that includes nested
manifests and excludes only its own root file.

ExpectedReturn: `PASS` or `FAIL`; actionable findings with exact locations,
impact, evidence, and remediation; scope/evidence verdict; blocking versus
non-blocking residual risks; validity for manager technical fan-in. Do not
perform artifact acceptance, lifecycle acceptance, CHECKING/ISSUED promotion,
release, system kill/parity conclusion, D83 inquiry completion, full
DEL-01-03 acceptance, or P1 completion.
