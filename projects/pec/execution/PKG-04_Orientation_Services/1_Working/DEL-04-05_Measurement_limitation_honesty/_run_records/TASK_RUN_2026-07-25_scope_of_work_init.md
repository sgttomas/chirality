# TASK RUN — scope-of-work (MODE=INIT) — DEL-04-05

| Field | Value |
|---|---|
| RunKind | TASK + `scope-of-work`, MODE=INIT |
| Authorization | D-PEC-63 (PEC Phase 2.2 SOW initialization wave, batch B7) |
| RequestedBy | PROJECT_SETUP (Agent 1) |
| Executor | Agent 2 (sealed TASK instance); no delegation performed |
| Date | 2026-07-25 |
| ScopePath | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty` |
| ResolvedSkillVersion | `skills/scope-of-work/SKILL.md`, `chirality-skill-version: "1"`, `chirality-task-profile: NONE` |
| CompanionFiles read | `BRIEF_SCHEMA.md`, `TOOL_POLICY.md`, `QA_CHECKS.md` |
| DECOMPOSITION_BASIS | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b` (revision 1.2, `current_basis`) |
| SOURCE_STATE | `OPEN` (unchanged by this run) |

## Outputs

| Artifact | sha256 |
|---|---|
| `ScopeOfWork.md` (production) | `5cd16083ed6f17e8eaf43c7c79ad63afb0a14e6e8031c0aba87015dda3209ba4` |
| `_STATUS.md` (read-only, before == after) | `12c5b6ff45156a05a1c9fa905524e7876220098ce73122472222d768054ddf38` |

## Tool invocations

1. `python3 tools/scope_of_work/validate_scope_of_work.py "<ScopePath>"` —
   final line verbatim:
   `PASS format=SOW_V1 target=projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty`
2. `python3 tools/scope_of_work/derive_review_checklist.py "<ScopePath>"` — run
   twice to stdout, outputs byte-identical (`cmp` clean). `item_count` 15;
   `source.sha256` binds the production contract hash above. JSON not persisted.

`render_scope_of_work.py` not invoked (`RENDER_HTML: false`). Conversion tools
(`convert_four_documents_to_scope_of_work.py`, `finalize_scope_of_work.py`,
`map_scope_of_work_claims.py`, `report_scope_of_work_parity.py`) not invoked:
structurally CONVERT-only and INERT under MODE=INIT per the D-PEC-63 §3.1
pre-ruling; no evidence candidate exists or was produced.

## Contract shape

OUT 2 · CLM 17 · TBD 4 · REQ 14 · AC 15 · CON 4 · VER 14 · AX 11. Matrix rows
15 (14 × OUT-001, 1 × OUT-002). AC↔VER is 1:1 for AC-001..AC-014; AC-015 is
`HUMAN_REVIEW`. AC-014 states the range VER-001..VER-013, excluding its own
summary method VER-014. No unresolved local references.

## Quotation verification

Ten blockquoted upstream records (`DEL-02-03` REQ-001/004/005; `DEL-04-03`
REQ-001/005/008 and CON-003; `DEL-04-01` REQ-001/006 and CON-004) were
programmatically diffed, whitespace-normalized, against their source contracts:
all ten match verbatim. The `SOW-009` ledger row, the three §4.1 exhibit rows,
the four `A003b` lines, and the `A001` target cell were verified the same way.
Thirty-four inline quotations from `PRD.md`, `SOFTWARE_DECOMP.md`,
`_DEPENDENCIES.md`, `D-PEC-62`, and the DAG-gate exhibit were verified by
normalized substring match against those sources. **Zero elisions**; the
quotation record states that and enumerates the three non-elision artifacts
(source `..` range notation, source CSV double-quote escaping, and the `A001`
cell-scoped quotation).

## Write authorization and boundary

Writes confined to the two `AllowedWriteTargets`: `ScopeOfWork.md` and
`_run_records/`. `git status --porcelain` over the ScopePath after authoring
showed exactly one entry (`?? .../ScopeOfWork.md`). `_STATUS.md`, `_CONTEXT.md`,
`_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and `_SEMANTIC.md`
were read only and are byte-identical. Lifecycle untouched
(`STATUS_POLICY: NO_STATUS_TOUCH`); `OPEN` → `INITIALIZED` advancement remains a
separate deterministic act under D-PEC-63 §3.2.

## Grounding sources read (read-only)

`ScopeLedger.csv` (SOW-009 and adjacent rows) · `Deliverables.csv` (DEL-04-05
and every named neighbour, for PhaseHint and artifact naming) · `docs/PRD.md`
(§4.2, §5, §6 PEC-K-01..-11, §7.1–7.3, §8, §9.1 PEC-ORI-001..006, §9.2
PEC-RCN-002/004/006, §9.3 PEC-GAT-003/004, §9.4 PEC-PRS-007, §9.6 PEC-API-002/004,
§9.7 PEC-DSH-001, §10 PEC-SVC-001/002, §14, §16) · `SOFTWARE_DECOMP.md`
(frontmatter, §2.1, §3, §4, §5 PKG-04, §9 Vocabulary Map, §10 Open Issues) ·
deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`,
`Dependencies.csv`, `_STATUS.md` ·
`_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` (§4 strata preamble,
§4.1 edges, §4.2 constraints) · `_Coordination/_COORDINATION.md` ·
`_Coordination/_DECISIONS/D-PEC-62_...md` §1 ·
`_ScopeChange/SCA-002_2026-07-25_1042/Brief.md` (A001, A002) and
`Amendment_Preview.md` (A001, A002, A003b line 320) · upstream
`DEL-02-03/ScopeOfWork.md`, `DEL-04-03/ScopeOfWork.md`, and
`DEL-04-01/ScopeOfWork.md`.

## Notes

- The brief located `DEL-04-01`'s renderer designation at "its CLM-019 region".
  That contract defines CLM-001..CLM-018 and has no CLM-019 record; the
  designation is stated in its own voice at `DEL-04-01`/REQ-006 and
  `DEL-04-01`/CLM-015, and `DEL-04-01`/CLM-012 additionally embeds a quotation
  of `DEL-03-01`'s CLM-019, which names this deliverable. This contract binds
  the designation to `DEL-04-01`/REQ-006, quoted in full at CLM-013. It does
  not cite `DEL-03-01`'s contract as a basis: no dependency edge to it exists
  in this deliverable's register.
- `DEP-04-05-005` (`SourceRef` "location TBD", empty `EvidenceQuote`) and the
  matching empty `BasisCitation` on exhibit row `E-P36` are carried as
  observations at CLM-009 and AX-009; no locus was supplied and no quotation
  was composed for them.
