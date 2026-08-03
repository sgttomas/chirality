# A2 Read-only Verifier Brief — D-APP-89 Option B

Status: `FROZEN — DISPATCH AUTHORIZED`

RequestedBy: App `HELP_HUMAN` through `WORKING_ITEMS`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ParentInstanceID: `WI-PKG03-DAPP89-B`

ChildInstanceID: `A2-DAPP89-VERIFY-01`

Role form: fresh ephemeral Agent 2 generalist, read-only, no delegation

Package: `PKG-03`

Deliverable: `DEL-03-01`

## Objective

Independently verify the complete Attempt 02 candidate and evidence against
D-APP-89 Option B. Review 100% of the implementation manifest and all required
acceptance boundaries. Do not repair, edit, install, project dependencies,
delete caches, or touch Git state. Return `PASS`, `FAIL`, or `BLOCKED` with
exact findings and evidence.

## Accepted predecessor candidates

- base HEAD `97678a841ef58345c73d3470ed8de57c9b1405d2`;
- D-APP-89 packet SHA-256
  `7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc`;
- D-APP-89 ruling SHA-256
  `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22`;
- Attempt 02 return SHA-256
  `24c37ac9babef12766925efe616b2cc408f26678b0afad691df0142df9a1234c`;
- Attempt 02 command evidence SHA-256
  `da40073d3b0522479fe6bbd1d186a6e5bb0ee5a4adab9e99af0653735b7f1a83`;
- fresh manifest SHA-256
  `353977870953eef45a1366cb6bc039560a56605aac7d3a8436c5b3f38f411d4c`.

These are candidates to verify, not facts to assume.

## Declared reads

- D-APP-89 packet/ruling and D-APP-73/76 boundaries as needed;
- all files named in `IMPLEMENTATION_MANIFEST_ATTEMPT02.sha256`;
- base-HEAD counterparts of every changed tracked file;
- retained facade package and Root contracts exports/source/package metadata;
- all D-APP-89 run-local briefs, evidence, dispositions, attempts, telemetry,
  command results, transient inventory, and DEL-03-01 status/memory;
- Git diff/status and preservation surfaces for Root, Piping, PEC, decision,
  authority, decomposition, six UNKNOWN, lifecycle, and Checking Approval SHA.

## Allowed operations

Read/search/hash/diff/parse operations only. Non-mutating deterministic
validators may be run only when they do not modify the tree. Do not run tests,
builds, packaging, installs, dependency projection, or commands that update
caches or generated outputs. Do not write a verifier file; return your full
structured result to `WORKING_ITEMS`, which will persist it.

## 100% verification requirements

1. Recalculate all 114 manifest hashes and prove the manifest's path set is
   exactly the candidate implementation/state set, with no missing executable
   importer/config/validator/test path.
2. Reproduce the base before census: 67 production files, 39 ordinary test
   files, 176 import occurrences, and the package/config/lock categories.
3. Prove the after state has zero ordinary executable App facade references,
   exactly 13 dedicated rollback probes, no root App facade dependency, no
   root lock dependency, no TS aliases, and no Next facade transpile target.
   Classify the two retained workspace lock strings, facade identity, validator
   assertions, script comment, and historical/documentary references.
4. Verify every used and retained facade root/subpath has an exact existing
   Root export; every retained facade source remains a direct re-export; no
   Root export was invented and no facade export removed.
5. Review every source/test diff and establish it is one-for-one specifier
   replacement with imported symbols and runtime semantics unchanged, except
   the dedicated rollback test and strengthened validator/config/manifest
   changes expressly authorized.
6. Validate the rollback procedure, exact affected-client boundary,
   source-versus-history distinction, release/no-reliance disposition, and
   later-retirement gate.
7. Check the complete validation evidence: Root build/typecheck/focused 8/8;
   App rollback 13/13; full 1111 passed/4 skipped; App typecheck,
   contract-deps, build, desktop pack, packaged dependency and instruction-root
   integrity passes. Confirm environment failure/retry history is preserved,
   no passing claim is made for a failed attempt, and final Amendment 04
   projection/restoration evidence is coherent.
8. Prove facade tree equals base; Root tracked diff is zero; original
   `.vite`-only `runtime/node_modules` restoration/backup absence is coherent;
   retained App dependency/build outputs are ignored derivative state and not
   tracked implementation.
9. Prove DEL-03-01 remains `IN_PROGRESS`, Checking Approval SHA is unchanged,
   Remaining truthfully preserves the later retirement gate, dependencies are
   unchanged, and no deliverable closure is claimed.
10. Prove no PRD/authority/decomposition/scope-change/Task Management/receipt/
    completion-log/foreign-loop/Git write belongs to this tranche, and all six
    D-APP-81 UNKNOWN relations are untouched.
11. Audit write containment, `git diff --check`, evidence SHA bindings,
    derivative status, blockers/reruns, and next-owner semantics.

## Return schema

- `VERDICT: PASS | FAIL | BLOCKED`
- requirement-by-requirement findings 1–11 with exact evidence;
- discrepancies by severity and whether they block manager fan-in;
- exact independently recalculated counts/hashes;
- confirmation of read-only/no-delegation behavior;
- final recommendation: `ACCEPT_FAN_IN` or `REJECT_FAN_IN`.
