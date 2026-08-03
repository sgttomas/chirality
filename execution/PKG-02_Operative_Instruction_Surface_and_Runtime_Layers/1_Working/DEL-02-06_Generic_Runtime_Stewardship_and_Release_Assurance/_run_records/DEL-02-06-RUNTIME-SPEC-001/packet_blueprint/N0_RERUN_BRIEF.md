# Sealed fresh Agent 2 brief — N0-R2 basis and accepted-input proof

Status: `BLUEPRINT — DO NOT DISPATCH`

- RequestedBy: `WORKING_ITEMS/W2`
- ParentRunID: `ROOT_FOUR_LANES_2026-08-02`, plan version 4
- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- ParentInstanceID: `W1-DEL0206`
- ChildInstanceID: `N0-R2`
- PackageID: `PKG-02`
- DeliverableID: `DEL-02-06`
- Objective: independently prove the applied S2 basis, exact owner-accepted
  six-file live packet, lifecycle, Root-profile absence, dependency truth, and
  write containment; release N1/N2/N3 only if every check passes.
- Dependencies: S2 exact candidate owner-accepted/applied/validated; external
  packet owner-acceptance record validated; exact accepted candidate copied
  byte-for-byte to live `accepted_inputs/`.
- AcceptedBasis: accepted `ScopeOfWork.md`; S2 application/validation records;
  continuation ruling; candidate presentation record; external owner
  acceptance record; live six-file packet; prior N0 interruption as rejected
  provenance only.
- DeclaredReads: original N0 governance/deliverable read scope, applied S2
  evidence, candidate presentation/acceptance/application evidence, live
  `accepted_inputs/`, and the two packet validators. No runtime implementation
  or foreign client read is needed for N0-R2.
- AllowedTools: bounded non-shell file reads, SHA-256, JSON/CSV parsing, exact
  packet validators, Scope-of-Work validator, and `apply_patch` for the exact
  return files. Tool availability must be proven before dispatch. No Bash,
  network, runtime tests, implementation command, or delegation.
- AllowedWriteTargets: new `basis/N0_R2_RETURN.md` and
  `basis/BASIS_REPORT_R2.json` only.
- ExpectedOutputs: machine-readable per-check PASS/FAIL, exact evidence refs
  and SHAs, acceptance-token verification, write-containment proof, and one
  terminal `RELEASE_N1_N2_N3 | HOLD` verdict.
- AcceptanceCriteria: no inherited result from prior N0; all six live bytes
  match the manifested/accepted candidate; manifest identity matches the
  external owner token; S2 current-facing labels and acceptance records agree;
  candidate state is planning-input accepted only; `ScopeOfWork.md` hash and
  lifecycle match; profile/dependency/write checks pass; no unresolved
  placeholder exists.
- EXCLUSIONS: no repair, reconstruction, semantic acceptance, runtime/client
  write, profile borrowing, dependency declaration, lifecycle change,
  implementation, release, register write, Git action, or N1/N2/N3 dispatch by
  the child.
- Escalation: any byte/hash/token mismatch, S2 drift, candidate mutation,
  contradictory status, missing tool, undeclared file, profile/dependency
  change, or write-boundary defect returns `HOLD`.

Agent 2 must not delegate. WORKING_ITEMS, not N0-R2, releases dependants after
validating the terminal return.
