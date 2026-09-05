# Decomposition Coverage Report — SCA-APP-009 Gate-5 Post-change R3

**Overall:** `BLOCKERS`
**Closure readiness:** `FAIL`
**Candidate basis:** `aa8554542e3d6d09a925f69e1114bea8e18532f8`

Authoritative inputs: decomposition SHA-256
`e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`;
companion SHA-256
`e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`;
unchanged `_LATEST.md` SHA-256
`12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`,
pointing uniquely to protected SCA-APP-008.

| Check | Verdict | Fresh result |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared packages resolve exactly once. |
| 2 Deliverable forward coverage | PASS | 52/52 declared deliverables resolve exactly once, including the structurally initialized DEL-09-07. |
| 3 Reverse folder coverage | WARNING | Undeclared PKG-00 and DEL-00-01/02 remain; 52/54 deliverable reverse coverage. |
| 4 ID consistency | PASS | No duplicate declared ID, parentless declaration, orphan ledger reference, or folder-prefix mismatch. |
| 5 Context fidelity | WARNING | 52 contexts present; 45 match and seven are partial. Three partials are newly exposed by approved carrier-semantic changes. |
| 6 Artifact presence | WARNING | 13/191 deterministic local-filename matches. Fifty IN_PROGRESS rows remain warning-level; OPEN DEL-09-07 is informational and its absent SOW is the approved structural state. |
| 7 Objective mapping | PASS | 10/10 objectives have live support; no declared deliverable or IN ledger row lacks mapping. |
| 8 Ledger integrity | PASS | 80 rows: 75 IN, four OUT, one TBD; all package/deliverable references resolve. |
| 9 Derivative parity | SKIPPED | Not SOFTWARE-variant-owned. |
| 9b Package shape | WARNING | Approved prose still says 81 IDs/48 families while the exact companion contains 83 IDs/50 families. |
| 10 Active snapshot/handoff | BLOCKER | SCA-APP-008 remains active and historically reconciled, but six required root artifacts remain absent. SCA-APP-009 remains a complete 24-file pre-audit subset, not current. |
| 11 Lifecycle | PASS | 51 IN_PROGRESS and one OPEN; 52 statuses read, 51 paired MEMORY files read, and DEL-09-07's MEMORY absence is required by the five-file scaffold boundary. |
| 12 Baseline comparison | PASS | The carried SCA-APP-008 blocker remains. No new blocker or major exists; topology and approved semantic deltas explain the warning movement. |

The post-change topology is exactly 10 packages, 52 deliverables, 80 scope
rows, and 10 objectives. Distribution is 75 IN / four OUT / one TBD; context
envelopes are S=9, M=41, L=2, XL=0. DEL-09-07 is exactly
`MIGRATION_SCRIPT` / `M`, belongs to PKG-09, covers SOW-080, and supports
OBJ-008. No declared deliverable is orphaned or parentless.

The companion is exactly 18 columns, 83 unique invariant rows, and 50
families, byte-identical to the accepted postimage. Its changes are the
approved carrier-semantic/pin consequences bound by the Gate-3 candidate;
this audit invents no additional carrier assignment. The main decomposition's
older 81/48 narrative remains an explicit package-shape warning.

The DEL-09-07 folder contains exactly `_CONTEXT.md`, `_STATUS.md`,
`_REFERENCES.md`, `_DEPENDENCIES.md`, and zero-byte `_SEMANTIC.md`, all regular
non-symlink files at their recorded hashes. It contains no `ScopeOfWork.md`,
`MEMORY.md`, `Dependencies.csv`, nested path, or sixth file. The state is OPEN
and makes no implementation or release-readiness claim.

The SCA-APP-009 folder contains exactly the 24 `PRE_AUDIT_24` artifacts named
by the revision-5 materialization matrix. `_LATEST.md` still points to
SCA-APP-008. The protected SCA-APP-008 tree remains byte-identical to basis
(Git tree `a9e659987bf4a684dedd207adb80eb190f87a2ec`; recursive ls-tree manifest
`fa7a0f69844b03db9479416f4d76d33cb7a3c04485efba6027aba165552f24a6`).
Its post-application dependency warnings, including the nine-node SCC, remain
carried; no silent linearization or protected-byte change occurred.

Compared with fresh pre-change, the occurrence-weighted result moves from one
blocker / 58 warnings / one info to one blocker / 61 warnings / two info.
The three net warnings are the three newly exposed context mismatches:
DEL-02-02, DEL-04-01, and DEL-05-01. The prior 81/48 warning remains, while
SOW-080 now resolves to the structural DEL-09-07 folder. There is no new
blocker or major, so this derivative result is `POSTCHANGE_AUDIT_READY`; the
carried blocker still prevents this audit from claiming closure readiness.

## What to fix for a cleaner rerun

- Reconcile the seven context descriptions only through their owning workflow.
- Reconcile the approved decomposition's 81/48 narrative with its exact 83/50 companion only through a governed authority amendment.
- Preserve the immutable SCA-APP-008 defect as history; a future active snapshot may satisfy the current package-shape contract without altering SCA-APP-008 bytes.

This audit authorizes no application, pointer movement, SOW creation,
dependency extraction, implementation, product work, release act, or severity
downgrade.
