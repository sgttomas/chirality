# SCOPE_CHANGE return — SOW-077 / OI-003 Gate 1 intake

**RunID:** `PEC-DPEC77-78-20260802`
**InstanceID:** `scope-change-oi003`
**Status:** `COMPLETE / AWAITING OWNER GATE 1`
**Decomposition variant:** `SOFTWARE`

## Result

The next amendment ID is **`SCA-004`**. The owner-initiated
`D-PEC-78: O-A` ruling parses as a bounded `MODIFY`-only amendment: make the
existing PEC-local schema-v1 registry the accepted long-term answer to
`SOW-077`, map that scope item into the existing
`PKG-01 → DEL-01-06 → OBJ-004` lineage, and record `OI-003` as resolved.

No package, deliverable, objective, stable ID, dependency edge, lifecycle
state, source byte, registry byte, or foreign-loop surface is added, removed,
renamed, reclassified, or accepted by this return. Gate 1 has **not** been
confirmed.

## Normalized intake

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-004` |
| `ALLOW_RENUMBERING` | `false` |
| Human initiation | `D-PEC-78: O-A` |
| Current gate | Gate 1 — awaiting owner confirmation |

The ID was obtained from
`tools/query/scan_next_amendment_id.sh projects/pec/execution/_ScopeChange`,
which found accepted snapshots `SCA-001` through `SCA-003` and returned
`SCA-004`.

## Authority and exact evidence

| Evidence | SHA-256 | Relevant fact |
|---|---|---|
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md` | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` | Owner ruled `D-PEC-78: O-A`; the PEC-owned JSON/schema paths and typed port are the long-term service-registry home/shape |
| `projects/pec/execution/_Coordination/D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md` | `426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17` | Exact O-A path, contract, compatibility, absence, migration, and non-effect boundary |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | §16.3 asks the registry-home/shape question; the PRD does not answer it |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` | Accepted working surface; `SOW-077` remains TBD and `OI-003` remains open |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` | Authoritative pre-change `SOW-077` and `SOW-094` rows |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` | Authoritative pre-change `DEL-01-06` row |
| `projects/pec/v2/config/loops.json` | `e24db354841e1b33d3ec4f74330351deaa7a18df0e0cd9e26bde248b6aed503e` | Current one-entry PEC-local registry |
| `projects/pec/v2/config/loops.schema.json` | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | Current strict schema version 1 |
| `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` | `RegisteredLoop` and core-owned `LoopRegistry` port |
| `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` | Replaceable JSON adapter with strict located failures |

The accepted decomposition pointer identifies revision 1.3 as the current
basis, and `_ScopeChange/_LATEST.md` identifies `SCA-003` as the last accepted
amendment. The D-PEC-78 ruling is supplementary accepted authority resolving
an explicitly open PRD question; it does not contradict a prior admitted
fact. A `Supersession_Delta.csv` binding is therefore not preliminarily owed.

## Parsed atomic actions and exact fields

The exact replacement prose is a Gate 3 product. Gate 1 fixes the affected
entities and field windows as follows.

| Ref | ActionType | EntityType | EntityID | Requested change and exact fields | Affected semantic sections / surfaces |
|---|---|---|---|---|---|
| A001 | `MODIFY` | `OTHER` | `SOW-077` | `InOutStatus: TBD → IN`; replace `ScopeItemStatement` with the ruled PEC-local long-term registry obligation; retain §16.3 and add `D-PEC-78` to `SourceRef`/`DecisionRef`; set `PackageID=PKG-01`, `DeliverableIDs=DEL-01-06`, `ObjectiveIDs=OBJ-004`, `OpenIssue: TRUE → FALSE`; replace the provisional local-default note with the ruled home/shape, strict schema-v1, PEC-only ownership, and graceful-absence boundary | SSOW IN/TBD tables; `ScopeLedger.csv`; objective-side mapped-scope view |
| A002 | `MODIFY` | `OTHER` | `SOW-094` | Preserve status, statement, source, lineage, and objective; change only `DecisionRef`/`Notes` so the local-config default is recorded as the implementation basis now confirmed long-term by `D-PEC-78`, rather than as an unresolved placeholder | SSOW IN table; `ScopeLedger.csv` |
| A003 | `MODIFY` | `DELIVERABLE` | `DEL-01-06` | Preserve ID, package, name, type, envelope, phase, artifacts, and objective; change `CoversScopeItems: SOW-094 → SOW-077;SOW-094` and revise `Description` from “long-term home/shape stays open” to the ruled PEC-local long-term configuration, without changing source bytes | Deliverables section; `Deliverables.csv`; exact `_CONTEXT.md` mirror fields `CoversScopeItems` and `Description` plus basis provenance |
| A004 | `MODIFY` | `OTHER` | `OI-003` | Retain the row non-destructively; replace “undecided / §16 ruling” with `RESOLVED by D-PEC-78 O-A` and the selected PEC-local typed registry result; update open/resolved telemetry from `11 open / 2 resolved` to `10 open / 3 resolved` | Open Issues; Coverage & Telemetry |
| A005 | `MODIFY` | `OTHER` | amendment traceability | Add the SCA-004 decision/revision record and recompute accepted-basis/pointer text after later gates; preserve topology counts and all unrelated §16 decisions | Decision Log; Revision History; decomposition and SCA handoff pointers; SCA/audit evidence |

This is a type-level and mapping amendment, not a decomposition-ontology
change. No parent partition changes, so the parent-closure rule is not
triggered. Stable IDs are preserved.

## Gate 1 validation and invariants

| Check | Result | Evidence |
|---|---|---|
| Human initiated | `PASS` | Exact owner ruling `D-PEC-78: O-A` |
| Entity existence | `PASS` | `SOW-077`, `SOW-094`, `OI-003`, `PKG-01`, `DEL-01-06`, and `OBJ-004` all exist in accepted revision 1.3 |
| Valid fields | `PASS` | Every proposed cell is present in the SOFTWARE Scope Ledger or Deliverables schema |
| Lineage | `PASS` | `SOW-094` already establishes `PKG-01 → DEL-01-06 → OBJ-004`; A001 extends the same registry concern into that existing lineage |
| Reciprocal mapping | `PASS, conditional on same amendment` | A001's new `SOW-077 → DEL-01-06` mapping is paired with A003's `DEL-01-06 → SOW-077` coverage update |
| Package discipline / artifact-kind granularity | `PASS` | Registry configuration, core port/adapter boundary, and loader/tests remain within existing PKG-01 / DEL-01-06; no cross-package writer or new deliverable kind is introduced |
| Stable IDs / topology | `PASS` | Expected successor remains 94 scope items, 11 packages, 64 deliverables, 6 objectives, and 64 QA rows; no edge is added or removed |
| Scope-status telemetry | `PASS, expected successor` | Current `71 IN / 14 OUT / 9 TBD` becomes `72 IN / 14 OUT / 8 TBD` solely through SOW-077 |
| Register integrity | `PASS` | Current strict validator: 64 registers, 254 dependency rows, 0 errors, 0 warnings |
| Source behavior | `NO CHANGE REQUIRED` | D-PEC-78 expressly confirms the current paths/port/adapter; source hashes above are evidence, not amendment targets |
| Supersession | `NOT REQUIRED, preliminary` | The accepted decision fills a PRD §16.3 unknown; it overrides no prior governing value |

The latest governed full `AUDIT_DECOMP` evidence is
`execution/_Evaluation/DecompCoverage/COV_SCA003_POSTCHANGE_FINAL_2026-07-28_0831/coverage_summary.json`:
revision 1.3, `overall_status=OK`, 11/11 packages, 64/64 deliverables,
100% forward/reverse/context/objective coverage, package-shape `PASS`, and
zero blockers/warnings. A fresh SCA-004 pre-change audit snapshot is still
required when the amendment itself opens; this sealed intake could write only
this instance's return surfaces and therefore did not create one or move the
audit pointer.

## Preliminary impact and derivative classification

| Surface / package | Package role | Preliminary classification after approval | Owner / required follow-on |
|---|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | working decomposition truth | `DIRECT_EDIT` | SCOPE_CHANGE after Gates 2–4 |
| `execution/_Decomposition/ScopeLedger.csv` | authoritative companion register | `DIRECT_EDIT` | SCOPE_CHANGE exact A001/A002 rows |
| `execution/_Decomposition/Deliverables.csv` | authoritative companion register | `DIRECT_EDIT` | SCOPE_CHANGE exact DEL-01-06 row |
| `DEL-01-06/_CONTEXT.md` | variant-local metadata mirror | `DIRECT_EDIT` | SCOPE_CHANGE only if exact propagation is approved at Gate 4; paired `_STATUS.md`/memory rule remains binding |
| `_Decomposition/_LATEST.md`, SCA-004 snapshot, `_ScopeChange/_LATEST.md`, DecompCoverage snapshot | snapshot / handoff / derivative evidence | `RECOMPUTE` | SCOPE_CHANGE and AUDIT_DECOMP after later gates |
| `DEL-01-06/ScopeOfWork.md` SHA `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a` | accepted downstream production contract | `STALE_REBUILD_REQUIRED` | WORKING_ITEMS: reconcile header scope refs, CLM-003, REQ-005, CON-001, and related authority prose; no SCA direct write |
| `DEL-01-06/_REFERENCES.md` SHA `06b9c75afb1e7060d6326c4a171feb28da2474b7287e4033f400b97d2e38575d` | downstream reference packet | `STALE_REBUILD_REQUIRED` | PROJECT_SETUP/reference owner: add SOW-077 and successor decomposition pin |
| DEL-02-07 ScopeOfWork SHA `ddc837ca8b87ad8af52cfc4ec8b06c8fef883bbc3eeca9eea9949fb6280b007b` | downstream production contract | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS: convert OI-003-undecided prose to historical/settled authority while preserving interface isolation |
| DEL-03-01 ScopeOfWork SHA `756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19` | downstream production contract | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS: same; unresolved loop→project resolution remains separate |
| DEL-04-01 ScopeOfWork SHA `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f` | downstream production contract | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS: remove the false OI-003-open premise without adding an unrecorded dependency edge |
| DEL-00-03 accepted SPEC SHA `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315` | accepted derivative product specification | `STALE_REVIEW_REQUIRED` | DEL-00-03 owning workflow: update the general “open decisions” statement only under its own artifact gate |
| dependency registers and topology | downstream authoritative/control surfaces | `NO_CHANGE` | Preserve all 254 rows; the semantic core port was already the dependency seam |
| `projects/pec/v2/**`, lifecycle files, Task Management registers, prior SCA snapshots, decision/receipt records, foreign loops | source / control / historical authority | `NO_CHANGE` | Outside SCA-004; historical records remain historical |

The amendment makes no derivative current merely by changing decomposition
truth. Every stale contract or artifact must be regenerated or explicitly
deferred by its owning workflow and recorded in the later SCA handoff state.

## Risks and open unknowns for later gates

1. **Exact Gate 3 prose.** The owner chose the architecture, but the concise
   SSOW statement and notes still require an exact diff preview. They must
   carry the authority boundary without copying the entire packet into the
   ledger.
2. **Stable deliverable label.** This intake recommends retaining
   `DEL-01-06`'s name and folder (`Loop registry (local config default)`),
   because “local” still describes the selected home and avoids a needless
   path/identity ripple. A rename is not inferred from O-A.
3. **PRD byte posture.** PRD v2.2 still lists §16.3 among “Open product
   decisions.” D-PEC-78 is the accepted supplemental answer. SCA-004 must
   cite both; it does not silently amend the PRD.
4. **Contract-currency population.** Four active ScopeOfWork contracts and
   the accepted SPEC contain present-tense OI-003-open claims. Their exact
   repair population and review gates belong to WORKING_ITEMS / the relevant
   artifact owners, not SCOPE_CHANGE.
5. **Loop maps.** The PEC standing workplan still names the registry-home
   decision among open §16 items. It is a loop map, not decomposition truth;
   ordinary loop closeout may record the ruled delta, but historical receipts
   must not be rewritten.
6. **No foreign effect.** O-A creates no declaration or duty for Root, App,
   Piping, Bridge, or another consumer. A later addition/removal/retargeting
   of a PEC registry row remains a separate owner-gated PEC configuration
   change.

## Gate boundary

Only this instance's `RETURN.md` and `STATUS.json` were written. No
decomposition, `_LATEST.md`, prior SCA, deliverable contract, source,
register, decision, receipt, lifecycle, or foreign-loop surface was modified.

## Owner Gate 1 question

**Is this what you intend: open `SCA-004` as the `MODIFY`-only amendment above,
mapping `SOW-077` to the existing `PKG-01 → DEL-01-06 → OBJ-004` lineage,
recording `OI-003` resolved by `D-PEC-78 O-A`, preserving the DEL-01-06 stable
name/path and all source bytes, and advancing only to Gate 2 impact assessment?**
