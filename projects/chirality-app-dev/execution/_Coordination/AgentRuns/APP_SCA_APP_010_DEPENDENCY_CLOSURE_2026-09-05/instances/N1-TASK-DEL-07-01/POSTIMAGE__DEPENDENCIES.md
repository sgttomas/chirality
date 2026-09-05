# Dependencies: DEL-07-01 Working Root Validation and Instruction Root Protection

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor validation.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] MISSING_DECOMPOSITION`: the explicit decomposition path was available.
- Conservative exclusion: no dependency edge was emitted for `DEL-06-04`; `Guidance.md` identifies the relationship as an inferred coordination note, not an accepted dependency edge.

### 2026-09-05 run (SCA-APP-010 dependency closure, DEP-017/DEP-018 report-only preview)

- Run: `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` instance `N1-TASK-DEL-07-01`; `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=RECONCILIATION`; `SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`, `ANCHOR_DOC=ScopeOfWork.md`, `EXECUTION_DOC_ORDER=[ScopeOfWork.md, _CONTEXT.md, _STATUS.md]`; `_STATUS.md` read only for its `## Remaining` section; `_REFERENCES.md` read to resolve document pointers. Excluded as sources: `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `MEMORY.md`, `Assessment_*`, `Evidence*`, `_run_records/**`.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` found at the pinned identity SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; applied row L357; amended Scope Ledger rows SOW-002 L172 and SOW-084 L254; reverse view L405/L430/L478/L487; OI-008 L602; DEC-025 L634). Companion register SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` SHA-256 `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`.
- Pre-images verified before extraction: `Dependencies.csv` SHA-256 `0584937814e740879a05178547536c49ba9d03ef36bbbc0e6a83c15b4726224c` (5 data rows); `_DEPENDENCIES.md` SHA-256 `a40fe07268822d3247b0f8790c09f91b4a60857f8ab55c71b7e2640b7af2f5c9`.
- Legacy four-document kit (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) no longer exists in this folder. Rows DEP-07-01-001 and DEP-07-01-005 were re-evidenced to live `ScopeOfWork.md`, `_STATUS.md#Remaining`, and decomposition `#L<n>` bytes; no row was retired for lost evidence because every relation is still stated. Rows DEP-07-01-002 and DEP-07-01-003 were refreshed to the live `_CONTEXT.md` traceability line (`SOW-002, SOW-027, SOW-075`) and the amended ledger rows. DEP-07-01-004 (RETIRED) is byte-identical.
- Added anchors: DEP-07-01-006 (SOW-075; on the applied row and in `_CONTEXT.md` since D-APP-80 but never extracted), DEP-07-01-007 (SOW-084; introduced by SCA-APP-010), DEP-07-01-008 (OBJ-006), DEP-07-01-009 (OBJ-008). Objective anchors use `TargetType=UNKNOWN` per the brief's existing objective-anchor convention with the raw reference preserved.
- Added execution rows: DEP-07-01-010 (INTERFACE, DOWNSTREAM, DEL-04-04 consumes the organisation-layer pins; `_STATUS.md#Remaining` and L487), DEP-07-01-011 (INTERFACE, DOWNSTREAM, DEL-02-03 UI touchpoint consumes working-folder validation; L172/L405/L309; `Confidence=MEDIUM`, transferred artifact labelled ASSUMPTION), DEP-07-01-012 (CONSTRAINT, UPSTREAM, K-ROOT-1 applied to both instruction-root layers; L254; REF-002 resolves by pinned hash to `projects/chirality-app-dev/docs/CONTRACT.md` L42).
- Considered and not emitted (information-flow rule; reported, not suppressed): (a) DEL-08-01 — L487 and `_STATUS.md#Remaining` state only an ownership split ("DEL-08-01 owns packaging and conformance checks"); the live sources do not state that DEL-07-01 supplies or consumes a named artifact with DEL-08-01, and the owner of the pin-file contract that both boot verification (DEL-07-01) and packaging checks (DEL-08-01) read is unstated; (b) DEL-06-04 — remains a coordination note (ScopeOfWork.md CLM-026; human ruling X-002 open); (c) `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` — cited by the seated item "only for what the tranche means when complete, never as a queue", so no edge; (d) `frontend/electron/daemon-instruction-root.ts` (D-APP-98) — a conditional write locus, not an edge; (e) SOW-002's "app-scoped set of known folders" (SOW-008, DEL-02-04) — no transfer to or from DEL-07-01 is stated on the amended rows.
- Root-owned semantics: none apply to this carrier (OI-008 covers SOW-010/081/082/083, none of which is on row L357); no `TargetType=EXTERNAL` row was needed.
- Fence results: F1 NONE (DEL-07-01 is not an SCC-001 member; the two deliverable targets DEL-04-04 and DEL-02-03 are not SCC-001 members, so no reverse-edge condition can arise); F2 NONE (every `TargetLocation` is a project-relative path or a `_REFERENCES.md`-pinned document; the DEP-07-01-005 `frontend/...` locations predate the fence and are preserved unchanged); F3 NONE (every new row traces to L357, L172, or L254 prose or the seated `## Remaining` item). `FENCE_F1_CANDIDATES`: none. `FENCE_F2_CANDIDATES`: none. `NEEDS_HUMAN_GRAPH_DECISION`: none.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: `tools/validation/validate_id_format.sh` uses a generic three-digit profile that rejects the accepted App two-digit IDs (`DEL-07-01`, `PKG-07`, `DEP-07-01-NNN`, `SOW-NNN`); no ID was changed. Schema validator VALID (29 columns, 12 data rows); all 25 distinct enum values VALID; exactly one ACTIVE `IMPLEMENTS_NODE`.
- No `[WARNING] FLOATING_NODE`, no `[WARNING] AMBIGUOUS_ANCHOR`, no `[WARNING] MISSING_DECOMPOSITION` for this run.
- The D-APP-56 R5 P45 "current register summary" block below is dated history as of this run; the `## Lifecycle Summary` reflects the 2026-09-05 post-image.
- Report-only preview: this text and the matching `Dependencies.csv` are proposed post-images produced under `AllowedWriteTargets` limited to the run's instance folder; the carrier bytes were not changed by this run. They become the carrier's register only through the owner's review of `PREVIEW.md` and a separately authorized write.

## Extracted Dependency Register

12 rows: 11 ACTIVE, 1 RETIRED; 7 ANCHOR, 5 EXECUTION.

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-07-01-001 | ANCHOR | OTHER / IMPLEMENTS_NODE | DEL-07-01 Working Root Validation and Instruction Root Protection | ACTIVE | `ScopeOfWork.md#Current responsibility`; decomposition #L357 |
| DEP-07-01-002 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-002 Per-chat working-folder selection and validation | ACTIVE | `_CONTEXT.md#Traceability`; decomposition #L172, #L405 |
| DEP-07-01-003 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-027 Path containment and instruction-root protection | ACTIVE | `_CONTEXT.md#Traceability`; decomposition #L197, #L430 |
| DEP-07-01-004 | EXECUTION | CONSTRAINT | REF-006 `docs/PRD.md` reference state MATCH | RETIRED | `_REFERENCES.md` |
| DEP-07-01-005 | EXECUTION | PREREQUISITE | UNKNOWN (multi-file) landed implementation modules | ACTIVE | `ScopeOfWork.md#CLM-018`, `#CLM-014`; `_STATUS.md#Remaining` write locus |
| DEP-07-01-006 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-075 Local project truth, no hidden project memory | ACTIVE | `ScopeOfWork.md` front matter and D-APP-80 note; decomposition #L245, #L478 |
| DEP-07-01-007 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-084 Layered instruction root | ACTIVE | `ScopeOfWork.md#Current acceptance obligations`; decomposition #L254, #L487 |
| DEP-07-01-008 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | OBJ-006 (TargetType UNKNOWN) | ACTIVE | `ScopeOfWork.md` front matter; decomposition #L267 |
| DEP-07-01-009 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | OBJ-008 (TargetType UNKNOWN) | ACTIVE | `ScopeOfWork.md` front matter; decomposition #L269 |
| DEP-07-01-010 | EXECUTION | INTERFACE (DOWNSTREAM) | DEL-04-04 PersonaComposer from Instruction Root consumes the organisation-layer pins | ACTIVE | `_STATUS.md#Remaining`; decomposition #L487, #L329 |
| DEP-07-01-011 | EXECUTION | INTERFACE (DOWNSTREAM) | DEL-02-03 Working Root File Tree and Scope Scan UI consumes working-folder validation | ACTIVE | decomposition #L172, #L405, #L309; `ScopeOfWork.md#CLM-003` |
| DEP-07-01-012 | EXECUTION | CONSTRAINT (UPSTREAM) | REF-002 `docs/CONTRACT.md` K-ROOT-1 applied to both layers | ACTIVE | `ScopeOfWork.md#Current acceptance obligations`; decomposition #L254 |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| ACTIVE rows | 11 |
| RETIRED rows | 1 |
| ANCHOR rows | 7 |
| EXECUTION rows | 5 |
| Satisfaction `NOT_APPLICABLE` | 8 |
| Satisfaction `SATISFIED` | 1 |
| Satisfaction `PENDING` | 3 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:47:21-0600 | UPDATE | CONSERVATIVE | located | 5 | SOURCE_HASH_MISMATCH |
| 2026-09-05T00:36:54-0600 | UPDATE | CONSERVATIVE | located at pinned identity `c7c05169…771e61` (L357) | 11 | PROJECT_ID_FORMAT_PROFILE |

## Downstream Handoff Notes

- Consumer: `RECONCILIATION`. This register is deliverable-local; project-graph assembly and cycle handling stay with AGGREGATION and the closure analyzer.
- Accepted upstream: applied decomposition `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; carrier `ScopeOfWork.md` re-pinned to that identity (SCA-APP-010 Gate-5 Current Contract, D-APP-108 seating).
- Cross-deliverable edges to reconcile against the counterpart registers: DEP-07-01-010 (DEL-04-04 should carry the UPSTREAM counterpart for pin consumption under SOW-084), DEP-07-01-011 (DEL-02-03 should carry the UPSTREAM counterpart for working-folder validation under SOW-002). Neither target is an SCC-001 member.
- Open for the owner, not blocking this register: the pin-file contract shared by DEL-07-01 boot verification and DEL-08-01 packaging checks has no stated owner in the live sources (no edge emitted; see Run Notes); DEL-06-04 remains a coordination note under human ruling X-002.
- Closure lifecycle: DEP-07-01-010, -011, -012 are `PENDING` until DEL-07-01-V3-01 merges with review PASS; DEP-07-01-005 stays `SATISFIED` for the landed modules only.

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-130
- **Current counts:** ACTIVE 4; RETIRED 1; NOT_APPLICABLE=4; SATISFIED=1.
- **Correction:** DEP-07-01-005 resolves to landed implementation modules and is SATISFIED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.

---

**Addendum (2026-07-18 — D-APP-62 scoped interpretation):** Under the
D-APP-62 ruling (O-A, 2026-07-18), the assertion above that `_SEMANTIC.md`
is invalid evidence / was not read or consumed is scoped to
dependency-extraction evidence: it bars `_SEMANTIC.md` from serving as
evidence for dependency rows. Its recorded consumption as the primary input
to `_SEMANTIC_LENSING.md` is a different act, outside that scope and
consistent with it. See
`execution/_Coordination/_DECISIONS/D-APP-62_PACKET_SEMANTIC_ADMISSIBILITY_SCOPE_2026-07-18.md`.
