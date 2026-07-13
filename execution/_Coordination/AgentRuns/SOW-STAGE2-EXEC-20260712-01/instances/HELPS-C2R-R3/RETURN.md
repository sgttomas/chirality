# HELPS-C2R-R3 Terminal Return

Verdict: `PASS`
Node: `C2R-R3`
Role: `HELPS_HUMANS` (Agent 1)
Delegation: none

The registered checklist caller now passes the raw supplied
`--migration-authority` to the exact resolver. A candidate bound to the exact
ruled marker rejects leading/trailing padded supplied authority, exits nonzero,
and emits no requested checklist artifact. Exact unpadded dual and SOW-only
checklists retain byte-stable item ordering, text, and linkage.

Changed source/test hashes:

- `tools/scope_of_work/derive_review_checklist.py` — `0ce012e63d873919c7ca589ce05cf1f2775259eee8312e2148677c17ab224438`
- `tools/scope_of_work/test_scope_of_work_tools.py` — `656445ed73f726dea65deb2604782ecf261a786630796dc164dbaae71c5a0703`

Verification: focused Scope-of-Work/reporting suite `19 passed`; full root tool
suite `792 passed`; Python compile PASS; `git diff --check` PASS; root
caller-manifest containment showed only the two authorized root hash deltas
before evidence refresh. No project, lifecycle, Git, release, H1/H2,
conversion, integration, or retirement action occurred; `.claude-worktrees/`
was not touched.

Blockers: none. Rerun C2R-R3 if the ruled authority, checklist/resolver input
contract, either repaired hash, or focused fixture changes. Next lawful owner:
parent fan-in and independent C2F-R1 rerun. P2_ROOT remains derivative evidence
and does not release integration or conversion.
