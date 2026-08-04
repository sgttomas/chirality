---
amendment_id: SCA-003
doc_kind: scope_change.basis_reconciliation_exact_preview
created: 2026-08-02
status: AWAITING_EXACT_OWNER_APPROVAL
---

# SCA-003 antecedent basis reconciliation — exact candidate preview

## Authority and limit

The owner ruled `ROUTE SCA-003 BASIS RECONCILIATION as proposed` in
`OWNER_RULING_2026-08-02_CONTINUATION.md`. That ruling authorizes this
preparation and routing. It expressly does not waive applicable gates,
pre-accept unpresented bytes, authorize application, or authorize foreign-loop
writes.

The exact full candidate bytes are under `Basis_Reconciliation_Candidate/`.
The complete two-file before/after is
`Basis_Reconciliation_Exact_Amendment.diff`. Deterministic validation is
`Basis_Reconciliation_Validation.json` (`PASS`, 17/17 checks).

## Exact source and proposed identities

| Order | Target | Current SHA-256 | Proposed SHA-256 | Owning gate |
|---:|---|---|---|---|
| 1 | `docs/PRD_ROOT.md` | `278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c` | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` | Root product-basis M2 exact-candidate acceptance, then separately authorized application |
| 2 | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49` | `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c` | SCOPE_CHANGE impact/amendment/propagation acceptance, then application after target 1 |

Exact diff SHA-256:
`c3ce8db08a45563f27948793cde925afd5d3d3d0f570789bdd49fda045788f72`.

## BR-001 — Root PRD current-facing control metadata

Current:

- top control calls Revision 7 an adoption-ready candidate and Revision 6 the
  current accepted product basis;
- the general PROPOSED-origin row says D-8 has no reliance until D-GOV-31;
- §10.4 presents Revision-7 candidate document control as current;
- the same live file's D-8 row says `ADOPTED (Rev 8)`.

Proposed:

- prepend a current Revision-8 accepted-status layer citing D-GOV-31,
  Receipt 64, and effective policy commit
  `602dd71b8c123d8a47a36644db1453f515c0f778`;
- explicitly time-scope, retain, and relabel the Revision-7 candidate header,
  mechanics, and control table as historical proposal evidence;
- reconcile only the PROPOSED-origin reliance note to D-GOV-31 + Receipt 64;
- add §10.5 current Revision-8 document control.

The validator proves all 43 stable-commitment rows and the complete §5.3.1
accepted-policy annex are byte-identical to the live Revision-8 source.

## BR-002 — decomposition current-facing acceptance/source metadata

Current:

- title/header/status call v1.2 an unaccepted SCA-002 candidate and revision
  1.1 the accepted basis;
- REF-001 pins PRD Revision 7 SHA-256 `15fba9c3…3748` at
  `ea3db360…adb`;
- downstream notes still prohibit work until an already-ruled Gate 7.

Proposed:

- state revision 1.2 as the accepted current basis, citing exact SCA-002
  acceptance token `ACCEPT SCA-002 271d456a`, Receipt 63, and PR #417 merge
  `6e21530f7182ca2a7e7831b9528f85889a4a4467`;
- pin REF-001 to the exact paired PRD candidate SHA-256
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`
  and the Receipt-64 Revision-8 basis;
- append DEC-024 and a current Change Log entry while keeping DEC-023 and the
  original SCA-002 candidate entry byte-preserved as time-scoped history;
- correct the downstream Gate-7/acceptance review notes.

The validator proves the decomposition identifier set remains exactly 89 and
the two companion registers remain untouched at SHA-256 `3deed192…59c2` and
`a29759be…1395`.

## Excluded effects

No scope item, stable commitment, package, deliverable, objective, ID,
mapping, status row, count, topology, runtime behavior, lifecycle, release,
reliance, register row, or foreign-loop product basis changes. Exact contract,
activation, client, implementation, and release work remains separately gated.

## Exact human decisions required

First, accept or return the candidate, assessment, and propagation plan. The
exact acceptance token is:

```text
ACCEPT SCA-003 BASIS RECONCILIATION c3ce8db0: accept
Basis_Reconciliation_Impact_Assessment.md and
Basis_Reconciliation_Propagation_Plan.md; approve exact PRD candidate SHA-256
d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4 and
exact decomposition candidate SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c;
preserve immutable SCA-002 evidence and prior candidate history; no scope,
topology, mapping, count, or substantive requirement change.
```

That token approves the exact candidate and the impact/propagation gates; it
does not apply bytes or authorize the M2 collateral writes. After acceptance,
the separate application ruling is:

```text
APPLY SCA-003 BASIS RECONCILIATION c3ce8db0: authorize the Root product-basis
M2 applying workflow to apply exact PRD SHA-256 d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4
first and satisfy its tranche-manifest, routed-notice, and export-disposition
obligations; then authorize SCOPE_CHANGE to apply exact decomposition SHA-256
69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c,
validate the paired REF-001 pin, rerun AUDIT_DECOMP, and return the applied
state for confirmation. Do not change _ScopeChange/_LATEST.md, scope,
topology, mappings, counts, substantive requirements, runtime, lifecycle,
release, reliance, or Task Management state; do not merge.
```

If either candidate needs correction, return both with exact replacement
text. Do not accept or apply only one half of the pair.
