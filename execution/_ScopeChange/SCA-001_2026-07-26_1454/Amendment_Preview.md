---
amendment_id: SCA-001
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-07-26
status: awaiting_gate_3_approval
accepted_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md revision 1.0
requested_by: Ryan Tufts
upstream_authority: D-GOV-28; Root PRD Revision 6; O-11
---

# SCA-001 Gate 3 — Exact Amendment Preview

## Approval scope

This is the complete proposed revision 1.0 → 1.1 amendment. It is a preview
only. No file under `execution/_Decomposition/` has changed.

The exact candidate bytes are under `Gate_3_Candidate/`; the complete
seven-surface before/after is `Gate_3_Exact_Amendment.diff`. The candidate is
reproducible with `build_gate3_candidate.py` and passes all 50 deterministic
checks in `Gate_3_Validation.json`.

The amendment implements the Gate 2 ruling: add one new PKG-02 deliverable
rather than expanding DEL-02-02.

## Exact new lineage

```text
PRD §5.2 O-11
  → SOW-104
  → PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
  → DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
  → OBJ-001, OBJ-002, OBJ-004, OBJ-007
```

`DEL-02-02_Three_Layer_Authority_Boundary_Conformance` is byte-semantically
unchanged in the authoritative deliverable register candidate.

## A001 — sole source basis and revision control

The working surface advances from Root PRD Revision 5 to the exact adopted
Revision 6 bytes:

```diff
-sha256 e98031c14b4c6c9b2602545e6f80abd5019ead0af1ff460b3e4ea26135bb63eb
-basis 24726a73c64a849909e3615c32ef1a888b3dfd36
+sha256 0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d
+basis fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb (D-GOV-28 EffectiveSHA)
```

Revision metadata becomes v1.1 dated 2026-07-26. The accepted v1.0 SHAs are
retained explicitly as predecessor identities. The v1.1 status is
conditional: the v1.0 predecessor remains current until the owner confirms
Gate 5; that confirmation makes the approved exact v1.1 bytes current without
a self-authorizing status claim.

The seven stable decomposition filenames retain their `_v1_0` suffixes.
Gate 2 classified those exact paths as the direct amendment surfaces; renaming
them would add an unassessed path-propagation change. Revision identity moves
in document metadata and Git history.

## A002 — exact SOW-104 row

| Field | Approved-candidate value |
|---|---|
| ScopeItemID | `SOW-104` |
| InOutStatus | `IN` |
| Statement | Consequential work on generic runtime semantics uses a Root-owned standing scope carrier and declared runtime write locus; preserves the authority, security, residency, exclusion, and implementation-gate boundaries ruled by D-GOV-20; produces versioned-contract, affected-client conformance or migration, and proportionate regression evidence; returns release disposition to an accountable human; and does not transfer generic runtime ownership to App, PEC, or another client. |
| SourceRef | `PRD §5.2 O-11 [PROPOSED-origin; adopted D-GOV-28]` |
| PackageID | `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers` |
| DeliverableIDs | `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance` |
| ObjectiveIDs | `OBJ-001;OBJ-002;OBJ-004;OBJ-007` |
| PRDItem | `O-11` |
| Categories | `OperativeProduct;Evidence` |
| DecisionRef | `DEC-022` |
| OpenIssue | `FALSE` |
| Notes | Standing carrier activated one bounded runtime-change tranche at a time. D-GOV-20 remains the ruled architectural basis; D-T0-23 is a coordinating Tier-0 counterpart, not a Root scope source. O-11 is in effect through D-GOV-28. |

The Evidence classification reflects the required contract, conformance or
migration, regression, and release-disposition evidence. It does not move
evidence-system ownership out of PKG-05.

## A003 — exact DEL-02-06 row

| Field | Approved-candidate value |
|---|---|
| DeliverableID | `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance` |
| Name | Generic Runtime Stewardship and Release Assurance |
| ParentPackageID | `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers` |
| ResponsibleParty | Ryan Tufts |
| Type | `REQ_SLICE` |
| Description | Provide the standing Root carrier for consequential generic runtime semantic changes: preserve the D-GOV-20 boundary, produce versioned-contract and affected-client conformance or migration plus proportionate regression evidence, and return release disposition to an accountable human without transferring generic runtime ownership to a client. |
| AnticipatedArtifacts | Runtime change brief and declared write-locus record; versioned-contract delta or no-change record; affected-client conformance or migration matrix; proportionate regression evidence bundle; accountable-human release disposition |
| CoversScopeItems | `SOW-104` |
| SupportsObjectives | `OBJ-001;OBJ-002;OBJ-004;OBJ-007` |
| ContextEnvelope | `M` |
| ContextEnvelopeNotes | One bounded runtime semantic-change tranche and its affected-client evidence; split the activation if implementation or client breadth would exceed M. |
| AnticipatedWriteLocus | `runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; client implementation only through separately authorized client-owned tranches` |

`REQ_SLICE` is used because this is the standing carrier for an adopted
requirement, activated one bounded change tranche at a time. The carrier does
not assert that every runtime change fits one execution: an activation that
would exceed `M` must split before dispatch. Client implementation is
expressly outside the Root carrier's write authority.

## A004 — exact reconciliation set

### Package description

```diff
-... declared write scope and capability-boundary controls, and live registry discipline.
+... declared write scope and capability-boundary controls, live registry discipline,
+and continuing stewardship and release assurance for the Root-owned generic runtime.
```

### Objective mappings

`SOW-104` and `DEL-02-06` are added to OBJ-001, OBJ-002, OBJ-004, and
OBJ-007 in both the objective and forward-coverage registers. No other
objective mapping changes.

### Bidirectional traceability

- Add one O-11 forward row:
  `O-11 → SOW-104 → PKG-02 → DEL-02-06 → COVERED`.
- Add O-11 and SOW-104 to the PKG-02 reverse row.
- Add one traced DEL-02-06 reverse row.
- Forward population: 84 → 85, with 84 COVERED and the existing one
  `COVERED_WITH_RECORDED_DEFERRAL`.
- Reverse population: 51 → 52, all TRACED.

### Telemetry and open-issue parity

| Metric | v1.0 | Candidate v1.1 |
|---|---:|---:|
| Scope items | 103 | 104 |
| IN / OUT / TBD | 94 / 9 / 0 | 95 / 9 / 0 |
| Packages | 6 | 6 |
| Deliverables | 45 | 46 |
| Objectives | 7 | 7 |
| S / M / L / XL | 14 / 30 / 1 / 0 | 14 / 31 / 1 / 0 |
| Operative Product scope / deliverables | 26 / 18 | 27 / 19 |
| Evidence scope / deliverables | 18 / 16 | 19 / 17 |

OI-011 is corrected from the stale unassigned-responsibility statement to
`CLOSED_ASSIGNED_BY_D-GOV-27`; Ryan Tufts is already assigned across the
accepted register, and that existing assignment is carried to DEL-02-06.
No new decomposition open issue is created. The pending scaffold, G2
surface-ownership, and G3 work-graph refresh remain downstream handoff state,
not decomposition ambiguity.

DEC-022 and a v1.1 change-log entry record the owner-requested amendment,
boundary/stewardship distinction, exact mappings, envelope, planning locus,
and no-implementation effect.

## Candidate identity

| Surface | SHA-256 |
|---|---|
| Working surface | `2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18` |
| Scope ledger | `0d48abe08aa336ac5e495650451f286b4b717606f047adff931c45dacc8531a4` |
| Deliverable register | `ec32b36fdc078e44a7ca094e9c854a3be6b7d5917360fe5ef5f22ff3702a13b8` |
| Objective register | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` |
| Forward coverage | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` |
| Reverse trace | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` |
| Coverage telemetry | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` |

## Validation result and authority boundary

`Gate_3_Validation.json` reports `PASS`: 50 checks, 0 failures. It confirms
the new lineage, counts, unique IDs, resolved references, all IN items mapped,
all reverse units traced, no XL deliverable, DEL-02-02 unchanged, Root PRD
SHA parity, category telemetry, and candidate separation from authoritative
paths.

Approval of this Gate 3 preview authorizes only these exact amendment bytes
for the later Gate 5 application. It does not approve the Gate 4 propagation
plan, modify decomposition truth, create the deliverable scaffold or guard
state, authorize a runtime or client edit, release WORKING_ITEMS, or decide a
runtime release.

## Gate 3 question

Do you approve these amendments to the decomposition document?
