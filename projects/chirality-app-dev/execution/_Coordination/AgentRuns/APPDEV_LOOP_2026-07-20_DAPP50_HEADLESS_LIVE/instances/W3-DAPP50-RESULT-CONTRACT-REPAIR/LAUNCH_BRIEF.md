# W3-DAPP50-RESULT-CONTRACT-REPAIR — Sealed WORKING_ITEMS Brief

## Identity and basis

- **Role:** WORKING_ITEMS (Agent 1), sole serialized repair owner
- **Branch/HEAD:** `codex/app-dev-dapp50-headless-live-20260720` /
  `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
- **Findings to cure:** V1 F-001 and F-002 only
- **Delegation/Git:** prohibited

Read full `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`, run controls through
`updates/v5.md`, V1 protocol/findings/report/handoff/manifest/terminal records,
W1/G0/W2 records, D-APP-50, DEC-065, TP-RUNNER-015, the live app adapter/tests,
the piping `openpipestress-runner.rs` `CliOutput`/result construction, the
headless runner result types, schema, and committed solve witness. Reproduce
HEAD, subject hashes, findings, and exact cleanup inventory before changing
anything.

## F-002 exact cleanup

Before deletion, require all of these predicates:

- the only top-level members of `frontend/dist/` are `builder-debug.yml` and
  `mac-arm64/`;
- the only member of `frontend/dist/mac-arm64/` is `Chirality.app/`;
- `builder-debug.yml` is 948 bytes and the app tree is exactly 163 regular
  files totaling 839,495,218 bytes (total 164 / 839,496,166);
- every target is ignored by `frontend/.gitignore:4:dist/`, none is tracked or
  staged, and birth/mtime evidence matches V1's 2026-07-20 11:13 interval;
- realpaths remain inside the exact app-dev `frontend/dist/` root and contain
  no symlink escape or mount boundary.

If any predicate differs, return `BLOCK`; do not delete partially. Immediately
before deletion, require the target to be a non-symlink directory whose
realpath equals exactly
`/Users/ryan/.codex/worktrees/2d6d/chirality/projects/chirality-app-dev/frontend/dist`
and whose complete inventory is still exactly 164 files / 839,496,166 bytes.
On exact match, recursively delete only that exact absolute directory and
verify it is absent. The whole directory is an explicit target because V1
proved the directory itself was born during W1 and contains no pre-existing or
non-packaging member. Do not use a glob, `git clean`, unresolved variable, or
touch `.next`, `dist-electron`, source, control, or other ignored state. Record
before/after path, count, bytes, mtimes, ignored/tracked classification, and
absence. Recoverability: generated ignored packaging output, reproducible only
by rerunning packaging, not Git-restorable.

## F-001 repair contract

Modify exactly these implementation paths unless a terminal `BLOCK` proves a
third path indispensable:

- `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`

Replace shallow output acceptance with strict fail-closed structural validation
of the app transport contract for DEC-065 `solve` CLI output:

1. Require exact allowed top-level keys and all required fields, including
   `artifact`, `schema_version`, `deliverable_id === "DEL-10-05"`,
   `package_id === "PKG-10"`, `command === "solve"`,
   `operation === "solve"`, `policy`, `request_validation`,
   `result_validation`, `runner_result`, and the ruled diagnostics member(s)
   shown by the final CLI contract. Reject unknown keys, including `padding`.
2. Require the exact DEC-065 policy key set, value types, and settled values:
   policy ref, binary, stdout default, explicit-output posture, local foreground
   process, and false network/telemetry/daemon/hidden-mutation/direct-SQL flags.
   Reject missing, extra, ill-typed, or contradictory policy fields.
3. Validate request/result validation objects and every diagnostics array as
   arrays of records with required diagnostic code/message/severity shape and
   allowed severity values. Preserve top-level and runner-result diagnostic
   correlation.
4. Require the full 11-key `runner_result` set from the final solve output and
   validate core nested structural/type/boundary fields: run/job identifiers,
   job state/progress/cancellation values, analysis-status strings,
   result-envelope reference shape, result refs, audit-manifest reference,
   privacy/provenance/professional-boundary objects, diagnostics, and no
   unknown runner-result keys. Validate presence/types/tokens needed by the app
   transport; do not claim exhaustive solver-semantic validation.
5. Preserve exit correlation: exit 0 only with no blocking diagnostic and a
   completed result; exit 1 only with at least one blocking diagnostic; exit 2
   remains input/usage refusal. Schema-invalid output fails closed with the
   stable result-schema mismatch code, never partial acceptance.
6. Replace the incomplete positive fixture with a structurally complete,
   invented fixture bound field-for-field to the committed piping witness
   shape. Add negative tests for every V1 defect: missing/incorrect deliverable
   and package ids, incomplete/contradictory/extra policy, missing/ill-typed/
   extra validation/result fields, incomplete/extra runner_result, bad nested
   types/tokens/diagnostics, extra top-level `padding`, and exit/result
   mismatches. Keep existing executable/path/hash/timeout/oversize/profile/
   containment/redaction tests green.

Do not change descriptors, registry version, tool catalog, runtime docs,
read-tools wiring, pull contract, status, run record, Receipt-83, decision
state, lifecycle, piping/tier-0/pec, or any unrelated source.

## Checks and return

Run focused tests, adjacent relevant tests, full frontend Vitest, typecheck,
build/premerge without packaging, pull-contract validator (expected to remain
valid for current commit until a new repair commit exists only if exported
contract bytes did not change), receipt validator, corpus status, self-check,
validation/practitioner pytest, diff/no-index/scope checks, and the exact
post-cleanup absence/process check. Do not run packaging, network proof, or
instruction-root bundle proof.

Write only this W3 instance's `RETURN.md`, `HANDOFF.md`, and terminal
`STATUS.json` beyond the two repair files; cleanup affects only the exact
generated targets above. Return `REPAIRED_AWAITING_G1_COMMIT | BLOCK` with exact
repair hashes, tests, cleanup before/after inventory, retained boundaries,
blockers/unknowns/waivers, and the G1 commit-only next gate. No status/receipt/
repin/Git closeout occurs in W3.
