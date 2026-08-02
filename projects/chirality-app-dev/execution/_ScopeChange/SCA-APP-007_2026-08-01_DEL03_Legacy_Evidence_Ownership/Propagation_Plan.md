# Gate 4 Candidate — Evidence Migration and Routing Repair

**Gate state:** `APPROVED_2026-08-01`
**Execution state:** `GATE_5_CLOSED_FOR_SCOPE_CHANGE_ONLY`

## Direct authoritative writes

None. The decomposition and `_ScopeChange/_LATEST.md` remain unchanged.

## Exact operational repair

1. Compute a SHA-256 manifest for all 38 source files.
2. Use Git-aware moves to place both proof bundles at:
   `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Historical_DEL-03-06/`.
   Preserve each historical bundle directory name and every file byte.
3. Add a provenance record and post-move SHA-256 manifest under the target
   `Evidence/` directory. The record maps old paths, new paths, source commits,
   the accepted `DEL-09-06` ownership basis, and SCA-APP-007.
4. Remove the now-empty
   `execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/`
   directory structure. No evidence file is deleted.
5. Correct `frontend/scripts/run-network-policy-proof.mjs`:
   - default owner/output root: accepted `DEL-09-06` path;
   - generated directory prefix: `NETWORK_POLICY_PROOF_`;
   - synthetic message label: `DEL-09-06 network-policy proof run`;
   - summary title: `Network Policy Proof Run Summary`;
   - preserve the existing `CONF-002` OCSP/CRL proof-limitation note exactly;
     its governance status is not part of this migration.
6. After paired read of `DEL-09-06/_STATUS.md` and `MEMORY.md`, append a dated
   provenance-only history note to each. Preserve `IN_PROGRESS`, Remaining
   items, authorization basis, and Checking Approval SHA exactly.
7. Do not edit immutable historical SCA, coordination, audit, or proof files.
   Use the new provenance map to resolve former live paths.

The operational changes are owned by the appropriate implementation/evidence
workflow (`WORKING_ITEMS` with bounded TASK execution). SCOPE_CHANGE owns the
candidate, gate record, no-topology backcheck, and handoff state; it does not
silently perform collateral work before approval.

## Validation and fan-in

- pre/post SHA-256 manifests match for all 38 moved evidence files;
- Git diff shows moves plus the explicit new provenance files, not evidence
  deletion/recreation;
- `node --check frontend/scripts/run-network-policy-proof.mjs` passes;
- the focused contract-pin test that covers the proof script passes;
- repository search finds no current implementation output route or generated
  current label for retired `DEL-03-06`/old network `OI-002` outside immutable
  historical artifacts;
- decomposition file SHA-256 remains
  `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`;
- scoped post-change AUDIT_DECOMP reports no `DEL-03-06` reverse-coverage
  residue and no new blocker;
- the six D-APP-81 clause-6 historical `UNKNOWN` relations remain byte-identical;
- `git diff --check` passes.

## Explicit exclusions

- no live proof run is required merely to migrate old evidence and correct its
  default output owner;
- no dependency extraction, estimate, schedule, release, lifecycle, authority
  corpus, PRD, or contract rerun is authorized by this plan;
- no historical proof content or prior ruling is rewritten.
- no `CONF-002` disposition is inferred or changed.

## Gate 4 decision

The human approved the exact seven-step operational repair and validation plan
above. Gate 5 executed only this plan. Independent fan-in passed the migration,
identity, routing, metadata, corpus, receipt, whitespace, and post-change audit
checks. The post-change snapshot is
`execution/_Evaluation/DecompCoverage/COV_SCA_APP_007_POSTCHANGE_DEL03_RECON_2026-08-01_2026-08-01_1754/`.

The exact contract-pin manifest entry passed 6/6 and the frozen routing
assertions passed 14/14 through a deterministic Node TypeScript loader. The
canonical Vitest wrapper remains a non-blocking rerun advisory because this
checkout has no installed Vitest dependency. Final human confirmation is
was retained as a non-blocking rerun advisory. The owner confirmed the
validated state and closed Gate 5 for scope change only.
