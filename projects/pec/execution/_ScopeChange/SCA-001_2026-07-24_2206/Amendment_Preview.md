---
amendment_id: SCA-001
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-07-24
status: awaiting_gate_3_approval
accepted_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md revision 1.0
requested_by: Ryan Tufts
authority: D-PEC-61
---

# SCA-001 Gate 3 — Exact Amendment Preview

## Approval scope

This is the complete proposed revision 1.0 → 1.1 amendment. It is a preview
only: none of the text or register rows below has been applied to
decomposition truth.

The amendment preserves 94 scope items, 64 deliverables, 11 packages, 6
objectives, all stable IDs, all package lineage, and all product functions.
It makes PEC's self-bootstrap direction explicit for PEC's own construction;
it does not privilege `FULL_GRAPH`, self-bootstrap, or any Agent 0
coordination pattern as PEC's universal product purpose.

## A001 and A004 — working-surface source basis and intake

### Front matter

```diff
-revision: "1.0"
+revision: "1.1"
 date: 2026-07-24
-accepted: 2026-07-24 (Gate 7 owner ruling, verbatim in the Gate Log; D-PEC-60 closure)
+accepted: 2026-07-24 (original Gate 7 owner ruling under D-PEC-60; revision 1.1 successor accepted through SCA-001 under D-PEC-61)
 agent_persona: SOFTWARE_DECOMP
 method_reference: agents/AGENT_SOFTWARE_DECOMP.md (conforms to docs/DECOMPOSITION_STANDARD.md)
-session_authorization: D-PEC-60
-source_corpus: projects/pec/docs/PRD.md (v2.0, adopted 2026-07-24, D-PEC-58)
+session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61
+source_corpus: projects/pec/docs/PRD.md (v2.1; v2.0 adopted 2026-07-24 by D-PEC-58, directed-bootstrap clarification adopted by D-PEC-61)
```

### Intake summary and validation obligations

```diff
-The work is a greenfield software build of the product defined by PRD v2.0:
+The work is a greenfield software build of the product defined by PRD v2.1:
```

The final bullet of §1.2 changes exactly as follows:

```diff
 - **Validation obligations carried by the PRD** (§11–§12): the pre-P1
   Step-0 cost baseline measurement, the permanent harness parity diff, the
-  standing kill test, and the P1–P4 exit tests. (P0 governance is complete
-  and is not scope for this decomposition.)
+  standing kill test, the P1–P4 exit tests, and directed full-DAG
+  self-bootstrap validation for PEC's own build. (P0 governance is complete
+  and is not scope for this decomposition.)
```

### Hard Constraints §1.3

Append after C15:

```diff
+| C16 | Directed self-bootstrap for PEC's own build: `PROJECT_SETUP` materializes the accepted decomposition as `FULL_GRAPH`; later nodes consume only PEC capabilities produced and accepted by predecessor nodes; no node depends on the capability it creates; observed friction routes to evidence-linked candidates and human gates; the file-native fallback remains operable | PRD v2.1 §12, D-PEC-61 |
```

C16 is construction-specific. It does not change the §5 modes ladder or
declare a preferred eventual PEC consumer mode.

### Intake postures and references

```diff
-1. **Requirement source = PRD v2.0 alone.** The 46 PEC-\*-NNN requirements,
+1. **Requirement source = PRD v2.1 alone.** The 46 PEC-\*-NNN requirements,
    11 PEC-K invariants, §3 outcomes, §11 metrics/falsification clause, §5
    modes ladder, and §12 exit tests are the scope-item source. Governance
    instruments (workplan, fences, D-GOV/D-T0 rulings) enter as constraints,
    not scope; the frozen corpus enters as reference, not scope.
```

```diff
-| R1 | `projects/pec/docs/PRD.md` (v2.0, adopted 2026-07-24, `D-PEC-58`) | Source corpus |
+| R1 | `projects/pec/docs/PRD.md` (v2.1; v2.0 adopted 2026-07-24 by `D-PEC-58`, directed-bootstrap clarification adopted by `D-PEC-61`) | Source corpus |
...
-| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..60` | Pivot, adoption, follow-ons, session packets |
+| R6 | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57..61` | Pivot, adoption, follow-ons, decomposition acceptance, directed-bootstrap/SCA opening |
```

### SSOW source statement

```diff
-Atomic scope items normalized from PRD v2.0. `SourceRef` cites the PRD
+Atomic scope items normalized from PRD v2.1. `SourceRef` cites the PRD
 requirement ID or section. Splits of enumerated requirements (PEC-RCN-002's
 feed list; PEC-STR-003's bridge list) are recorded in the Decision Log
-(DL-4, DL-5). Hard constraints C1–C15 (§1.3) bind every item and are not
+(DL-4, DL-5). Hard constraints C1–C16 (§1.3) bind every item and are not
 repeated as scope items unless they also require built or verified behavior
 (DL-7/DL-8).
```

Historical rows DL-7, DL-9, DL-10, DL-11, DL-14, and OI-010 remain unchanged
because they describe the state and decisions at their original gates.
DL-16, below, records the successor constraint and extension.

## A002 — SOW-064

### `SOFTWARE_DECOMP.md` §2.1

```diff
-| SOW-064 | IN | Bootstrap: the first loop the P1 reconciler ingests is PEC v2's own build | §12 | First validation of the thesis; §12-internal tension resolved at Gate 2 (OI-010, DL-10) |
+| SOW-064 | IN | Directed bootstrap: P1 first ingests PEC v2's accepted full dependency DAG as its initial file-native coordination state; later DAG nodes consume only PEC capabilities already produced and accepted by predecessors, while observed coordination friction is captured as evidence for candidate functions and boundary or amendment decisions | PRD v2.1 §12, D-PEC-61 | Introduced in P1 and standing thereafter; observations grant no authority or scope, the file-native fallback remains operable, and generality is validated against a structurally different loop (extends OI-010; DL-10, DL-11, SCA-001) |
```

### `ScopeLedger.csv`

Replace the complete `SOW-064` row:

```diff
-SOW-064,IN,Bootstrap: the first loop the P1 reconciler ingests is PEC v2's own build,§12,PKG-10,DEL-10-10,,DL-10; DL-11,FALSE,"First validation of the thesis; §12-internal tension resolved at Gate 2 (OI-010, DL-10)"
+SOW-064,IN,"Directed bootstrap: P1 first ingests PEC v2's accepted full dependency DAG as its initial file-native coordination state; later DAG nodes consume only PEC capabilities already produced and accepted by predecessors, while observed coordination friction is captured as evidence for candidate functions and boundary or amendment decisions","PRD v2.1 §12, D-PEC-61",PKG-10,DEL-10-10,OBJ-006,"DL-10; DL-11; SCA-001",FALSE,"Introduced in P1 and standing thereafter; observations grant no authority or scope, the file-native fallback remains operable, and generality is validated against a structurally different loop"
```

The lineage fields remain exactly `PKG-10` and `DEL-10-10`.

## A003 — DEL-10-10

### `SOFTWARE_DECOMP.md` §5 compact control row

```diff
-| DEL-10-10 | Bootstrap self-ingest validation | TEST_SUITE | S | P1 | SOW-064 |
+| DEL-10-10 | Directed bootstrap self-ingest validation | TEST_SUITE | M | P1 | SOW-064 |
```

`P1` remains the introduction point. Standing use thereafter is carried in
the authoritative deliverable description and artifact contract, not encoded
as a new phase or lifecycle state.

### `Deliverables.csv`

Replace the complete `DEL-10-10` row:

```diff
-DEL-10-10,PKG-10,Bootstrap self-ingest validation,The first loop the P1 reconciler ingests is PEC v2's own build (OI-010 resolution); validated as part of P1 acceptance.,TEST_SUITE,TBD,Self-ingest validation record,SOW-064,,S,,P1
+DEL-10-10,PKG-10,Directed bootstrap self-ingest validation,"Introduced in P1 and used as a standing validation thereafter. Maintain one bootstrap progression record showing ingestion of PEC's accepted full dependency DAG, capability cutovers only after predecessor acceptance, observed coordination friction, proposed/rejected/unnecessary functions, fallback operation, and routes to human-gated decisions or amendments.",TEST_SUITE,TBD,"Bootstrap progression record: DAG ingestion; capability cutovers; observed friction; proposed, rejected, and unnecessary functions; fallback evidence; amendment routes",SOW-064,OBJ-006,M,"M because the standing progression evidence spans the full DAG, capability cutovers, negative function dispositions, fallback proof, and human-gated amendment routes; keep one cohesive validation record",P1
```

### `ContextBudgetQA.csv`

Replace the complete `DEL-10-10` row:

```diff
-DEL-10-10,PKG-10,S,LOW,None,
+DEL-10-10,PKG-10,M,MEDIUM,Hold envelope; validate as one standing progression record,"M because the record spans the full DAG, capability cutovers, negative function dispositions, fallback proof, and human-gated amendment routes; split only if evidence volume prevents one coherent progression"
```

`Type=TEST_SUITE`, `ResponsibleParty=TBD`, `PackageID=PKG-10`,
`CoversScopeItems=SOW-064`, and `PhaseHint=P1` remain unchanged.

## A004 — objective, package summary, coverage, and change register

### OBJ-006 mapping

The objective statement and `SourceRef=§11` remain unchanged. Replace only
the support columns:

```diff
-| OBJ-006 | The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed | §11 | SOW-020, SOW-057..060, SOW-084, SOW-085, SOW-093 | DEL-01-04, DEL-03-04, DEL-10-01, DEL-10-04, DEL-10-05, DEL-10-09, DEL-10-11, DEL-10-12 |
+| OBJ-006 | The product thesis remains measurable and falsifiable: adoption, parity, defect, and collision metrics are gathered in system behavior and the §11 falsification clause stays armed | §11 | SOW-020, SOW-057..060, SOW-064, SOW-084, SOW-085, SOW-093 | DEL-01-04, DEL-03-04, DEL-10-01, DEL-10-04, DEL-10-05, DEL-10-09, DEL-10-10, DEL-10-11, DEL-10-12 |
```

### PKG-10 summary

```diff
-| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, bootstrap self-ingest | SOW-025, 055, 058..064, 084, 085, 093 (12) | The behaviors under test (their home packages) |
+| PKG-10 | Validation & Measurement | Release-gating proof and metrics: kill test, no-ruling-write verification, Step-0 baseline, defect/adoption/collision/parity measurement, seeded-conflict, TTL-honesty and stream-loss tests, usage observability, directed bootstrap progression evidence | SOW-025, 055, 058..064, 084, 085, 093 (12) | The behaviors under test (their home packages) |
```

The assigned set and count remain unchanged.

### Coverage & Telemetry

```diff
 | ScopeItemCount | 94 (71 IN / 14 OUT / 9 TBD) |
 | PackageCount | 11 (PKG-00..PKG-10) |
 | DeliverableCount | 64 |
 | ObjectiveCount | 6 |
 | UnassignedScopeItems (IN without package) | **0** |
 | ScopeItemsWithoutDeliverableMapping (IN) | **0** |
 | UnmappedObjectives | **0** (every objective backed at both scope-item and deliverable level, §3) |
-| IN items without objective mapping | 32 (intentional best-effort posture, §3 mapping notes — parsers/mechanics serve objectives through the record tier) |
-| ContextEnvelopeCounts | S 29 / M 33 / L 2 / XL 0 |
+| IN items without objective mapping | 31 (intentional best-effort posture, §3 mapping notes — parsers/mechanics serve objectives through the record tier) |
+| ContextEnvelopeCounts | S 28 / M 34 / L 2 / XL 0 |
 | OpenIssuesByType | 11 open (9 §16 owner decisions: OI-001..009; 1 architecture ADR: OI-012; 1 tooling follow-on: OI-013) / 2 resolved (OI-010, OI-011 at Gate 2) |
 | Deliverable single-package membership | 64/64; every `DEL-XX-YY` prefix matched to its parent package |
-| Revision | 0.9, 2026-07-24 |
+| Revision | 1.1, 2026-07-24 (SCA-001) |
```

Append to the Coverage-check provenance paragraph:

```diff
 Coverage-check provenance: every IN scope item traces §PRD → SSOW →
 package → deliverable(s) in `ScopeLedger.csv`; OUT items record the
 boundary (permanent vs deferred); TBD items carry their open-issue IDs.
+SCA-001 pre/post integrity evidence lives in
+`execution/_ScopeChange/SCA-001_2026-07-24_2206/`; the expected
+pre-scaffold `AUDIT_DECOMP` `FAILED_INPUTS` result is a filesystem
+limitation, not register-coverage evidence (OI-013 remains open).
```

### Decision Log / Change Register

Append after DL-15:

```diff
+| DL-16 | 2026-07-24 | SCA-001, requested by owner Ryan Tufts and opened by D-PEC-61, adds construction-specific constraint C16, expands SOW-064 and DEL-10-10 into directed full-DAG bootstrap progression evidence, maps both to OBJ-006, and re-envelopes DEL-10-10 S→M; no package, deliverable, objective, scope item, product function, stable ID, or dependency edge is added or removed | `FULL_GRAPH` supplies direction for PEC's own governed construction without becoming a universal PEC product mode; capability-before-consumption keeps the bootstrap acyclic, observed friction remains evidence rather than authority, the file-native fallback remains operable, and dependency-edge materialization stays with PROJECT_SETUP |
```

This is the SCA-001 Change Register entry required by SCOPE_CHANGE. Existing
DL rows are not rewritten.

### Revision history

Append after revision 1.0:

```diff
+| 1.1 | SCA-001 | Directed full-DAG self-bootstrap clarification under D-PEC-61: +C16; expanded SOW-064 and DEL-10-10; OBJ-006 mapping; DEL-10-10 S→M; PRD v2.1 source reconciliation; telemetry and handoff parity; topology unchanged |
```

## `_Decomposition/_LATEST.md` successor wording

After Gate 5 validation and owner confirmation, replace the complete file
with:

```markdown
# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.1**
(**`current_basis`** — accepted 2026-07-24 as the SCA-001 successor under
`D-PEC-61`).

## Handoff state

- **Basis:** D-PEC-60 SOFTWARE_DECOMP revision 1.0 over PRD v2.0, amended by
  SCA-001 to reconcile PRD v2.1's directed-bootstrap clarification adopted
  by D-PEC-61. SCOPE_CHANGE Gates 1–5 were separately owner-confirmed.
- **Package:** working surface + `ScopeLedger.csv` (94 rows) +
  `Deliverables.csv` (64) + `ContextBudgetQA.csv` +
  `Companion_Inventory.csv` (unchanged).
- **Closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`.** Revision 1.1 is the
  accepted decomposition basis. No package, deliverable, objective, scope
  item, product function, stable ID, or dependency edge was added or removed.
- **Verification:** deterministic pre/post register-integrity comparison
  confirms 94 scope items (71 IN / 14 OUT / 9 TBD), 11 packages,
  64 deliverables, 6 objectives, zero dangling mappings,
  `SOW-064 → PKG-10 → DEL-10-10 → OBJ-006`, and Context Envelope counts
  S 28 / M 34 / L 2 / XL 0.
- **AuditState: `WARNINGS`.** Pre/post `AUDIT_DECOMP` cannot measure
  filesystem coverage before Project Setup because no package/deliverable
  folders exist; its contract-required `FAILED_INPUTS` result is preserved.
  OI-013 remains the durable register-validator follow-on.
- **Blockers / open issues:** none blocks Project Setup. OI-001..009 remain
  the §16 owner decisions; OI-012 remains the core-isolation ADR; OI-013
  remains the validator follow-on.
- **ReadyForNextPhase: `REGEN_ONLY`.** `PROJECT_SETUP` is the next owner.
  `FULL_GRAPH` is already owner-selected; Project Setup must materialize the
  complete accepted dependency graph and blocker computation from revision
  1.1. Its Phase 1.3 dependency-maturity threshold and register-storage
  choices remain at their normal owner gate.
- **Fallback and authority:** the full DAG is PEC's initial file-native
  self-ingestion corpus; later nodes may consume only predecessor
  capabilities already produced and accepted. Observed friction may generate
  evidence-linked candidates or amendment requests but changes no accepted
  scope and grants no authority. File-native fallback remains operable.
```

The pointer does not claim that dependency extraction, scaffolding,
estimation, scheduling, implementation, or heterogeneous-loop validation is
complete.

## Companion Inventory result

`Companion_Inventory.csv` is `NO_CHANGE`.

No filename, package-role label, package membership, or description of a
companion's responsibility changes. Revision identity lives in
`SOFTWARE_DECOMP.md` front matter and `_LATEST.md`, not in the inventory
schema. Editing the inventory would create churn without restoring any
parity field.

## Explicit unchanged surfaces

- PRD v2.1 and its project pointers: already governed by `D-PEC-61`.
- `Companion_Inventory.csv`: exact `NO_CHANGE` result above.
- All Scope Ledger rows except `SOW-064`.
- All Deliverables rows except `DEL-10-10`.
- All Context Budget QA rows except `DEL-10-10`.
- Package IDs, deliverable IDs, objective IDs, scope item IDs, and counts.
- Package assignment and deliverable lineage for `SOW-064`/`DEL-10-10`.
- Historical Gate Log, OI-010, and existing DL-1..15 rows.
- `Dependencies.csv`, package/deliverable scaffolding, estimates, schedules,
  implementation, and frozen reference corpus.

## Gate 3 approval question

**Do you approve these amendments to the decomposition document?**
