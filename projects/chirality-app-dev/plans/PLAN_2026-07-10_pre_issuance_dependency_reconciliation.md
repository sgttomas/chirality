# PLAN - Pre-Issuance Dependency-Row Reconciliation

**Status:** CLOSED (executed 2026-07-10; DRQ-01..11 DONE; 89/100 rows SATISFIED, 11 left open with recorded gates — see closure report). Adopted by the owner's D-APP-53 ruling (Option A, 2026-07-10).
**Persona:** WORKING_ITEMS
**Authority basis:** `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md` (Option A, no
riders); packet `D-APP-53_PACKET_SUCCESSOR_QUEUE_SELECTION_2026-07-10.md` §3 Option A; INSP-05 roadmap
addendum §5 (`plans/artifacts/insp05_roadmap_addendum_2026-06-21_inspection_orphans.md` lines 68–69).
**Mode:** branch-first + PR (no commit discipline granted by the ruling; never self-merge).

## 1. Purpose

Close the unsatisfied local dependency rows left explicit by the INSP-05 addendum §5 and ORN-13's
bounded closeout: verify each open row against live evidence, land the evidence or retire/replace rows
per the v3.1 schema, and produce a DepClosure-consistent reconciliation record per deliverable.
Issuance is explicitly out of scope (F-APP-4); this queue discharges the issuance *prerequisite* only.

## 2. Scope and row inventory (re-derived from live registers, 2026-07-10)

Ten deliverables, 100 open rows (`Status=ACTIVE`, `SatisfactionStatus` ∉ {SATISFIED, WAIVED,
NOT_APPLICABLE}): DEL-01-02 (24), DEL-01-03 (12), DEL-01-04 (13), DEL-04-01 (7 of 13), DEL-09-03 (13),
DEL-10-01 (3), DEL-10-02 (2 of 5), DEL-10-03 (8), DEL-10-04 (8), DEL-10-05 (10). The addendum names
deliverables, not row IDs; this inventory is the live-register enumeration and is re-derived at
execution time (recompute; do not trust this paragraph if the filesystem disagrees).

## 3. Reconciliation rules (fixed for every row)

1. **Close only on cited live evidence.** A row moves to `SATISFIED` only with a concrete, resolvable
   evidence pointer recorded in the row (`EvidenceFile`/`Notes`): anchor rows — the target node/SOW/OBJ
   verified present in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` and still
   listing the deliverable; doc-corpus prerequisite rows — the target file present with `_REFERENCES.md`
   `MATCH` under the D-APP-38 corpus; execution rows — the depended-on artifact/test/capability verified
   present in the live tree. When in doubt, leave the row open and record why in the reconciliation
   record. Never fabricate or approximate an evidence pointer.
2. **Retire, not delete** (SPEC §6.2; REQ-DEL-07-05-008). Replacement = retire the old row
   (`Status=RETIRED`, `SatisfactionStatus=NOT_APPLICABLE`) + add a new row with a new `DependencyID`,
   cross-referenced in `Notes`. Precedent: DEP-04-01-008, DEP-10-02-004 (RUL-SCC-* pattern).
3. **Mutation mechanism.** Governed direct CSV reconciliation under this ruling, validated per register
   with `execution/_Scripts/validate_dependencies.py`. The frontend writer's satisfaction-transition map
   (`frontend/src/lib/dependencies/schema.ts`) governs app-mediated writes; governed direct
   reconciliation follows the established RUL-SCC-*/CHANGE precedent (single-pass state change with the
   authorizing basis in `Notes`). Every mutated row cites `D-APP-53` in `Notes` and bumps `LastSeen` to
   the reconciliation date.
4. **Maturity columns.** On `SATISFIED`, set `ProposedMaturity` to the row's `RequiredMaturity` value
   (DEL-10-02 satisfied-row precedent). Leave maturity untouched on rows left open.
5. **Owner-gated rows stay open.** Rows whose satisfaction is a genuine owner judgment or is fenced are
   annotated (Notes updated with the live state and the gate) but NOT closed: DEP-10-03-004 and
   DEP-10-04-004 (whether D-APP-50/51/52 constitute the "accepted amendment" — F-APP-3-adjacent, owner
   call); DEP-10-04-006 (ResponsibleParty assignment — owner act; addendum §5 fences
   owner-authority/responsible-party TBD fields); DEP-04-01-007's live-subprocess residual (owner-gated
   D-APP-52 live-LLM demonstration). DEP-10-02-005 (path glob/hook API) stays open on absence of live
   evidence. DEL-01-03 responsible-party/owner-authority TBD fields (issuance-gate sign-off) are outside
   this queue per addendum §5 line 80.
6. **Reconciliation record per deliverable:** `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`
   in the deliverable directory — per-row table (row ID, prior state, new state, basis/evidence pointer,
   or left-open reason), the standard derivative-evidence disclaimer (does not replace decomposition
   truth, source/test evidence, decision records, or human lifecycle approvals; authorizes no issuance),
   and a hygiene section for any summary/pointer repairs.
7. **`_DEPENDENCIES.md` sync.** Counts tables and lifecycle summaries updated to match the CSV in the
   same tranche; stale run-note warnings (e.g. resolved REF-006 HASH_MISMATCH) corrected with a dated
   note, not silently rewritten.
8. **No lifecycle transitions.** `_STATUS.md` stays `CHECKING` everywhere; no `CHECKING -> ISSUED`
   (F-APP-4). No writes outside `projects/chirality-app-dev/**`.

## 4. Queue

| ID | Deliverable | Open rows | Extra scope | Status |
|---|---|---:|---|---|
| DRQ-01 | DEL-01-02 Reliance Boundary Register | 24 | Fix DEP-01-02-018 TargetLocation literal (Append-Only → Append_Only) | DONE |
| DRQ-02 | DEL-01-03 Product Identity and Professional Boundary Copy | 12 | Responsible-party TBD fields stay out of scope (§3.5) | DONE |
| DRQ-03 | DEL-01-04 Scope Boundary and Retired Scope Register | 13 | — | DONE |
| DRQ-04 | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | 7 | Repair stale DEP-04-01-006 HASH_MISMATCH note; sync `_DEPENDENCIES.md` summary with CSV (DEP-04-01-008 RETIRED); update stale `TBD_PROBE_ENVIRONMENT` warning | DONE |
| DRQ-05 | DEL-09-03 Unit and Integration Test Expansion | 13 | Refresh stale decomposition line pointers (+6 offset); retire stale PRD_HASH_MISMATCH warning | DONE |
| DRQ-06 | DEL-10-01 DomainEngineProfile Contract Draft | 3 | Supersede the 2026-07-02 annotate-only note (satisfaction mutation now authorized by D-APP-53) | DONE |
| DRQ-07 | DEL-10-02 Protected Path and Proposal Path Policy | 2 | Sync `_DEPENDENCIES.md` summary (DEP-10-02-004 RETIRED); DEP-10-02-005 stays open | DONE |
| DRQ-08 | DEL-10-03 OperationProposal Record and Human Gate Workflow | 8 | DEP-10-03-004 annotate-only (§3.5) | DONE |
| DRQ-09 | DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture | 8 | DEP-10-04-004/-006 annotate-only (§3.5); repair stale REF-006 note | DONE |
| DRQ-10 | DEL-10-05 Domain Boundary Notices and Solver Truth Separation | 10 | Repair stale REF-006 note | DONE |
| DRQ-11 | Repo-wide closure: v3.1 linter over all ten registers; fresh immutable `CLOSURE_*` DepClosure snapshot via `tools/coordination/analyze_dep_closure.py`; acceptance audit; update `DepClosure/_LATEST.md` only after audit | — | Snapshot discipline per `PLAN_COMPLETION_LOG.md` 2245–2248 | DONE |

## 5. Validation gates (before PR)

- `python3 execution/_Scripts/validate_dependencies.py` clean on every touched register.
- DRQ-11 snapshot: `schema_invalid = 0`, `scc_count = 0` (acyclic), acceptance audit recorded, then
  `DepClosure/_LATEST.md` updated.
- `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` exit 0;
  `reconcile_authority_corpus.py status` no drift (no authority document changes expected);
  `git diff --check` clean. Frontend gates only if runtime files are touched (none expected).

## 6. Stop conditions / boundaries

Stop and surface: any row whose closure would require an owner act or fence crossing (record it as
left-open instead); any staging stray outside `projects/chirality-app-dev/**`; a validation failure not
repairable within the tranche. The four hard fences stand (F-APP-1 as amended by D-APP-44, F-APP-2,
F-APP-3, F-APP-4). No self-ruling; truthful attribution throughout (K-AUTH-1).

## 7. Finalization

On DRQ-11 completion: update this plan's rows, record closeout in `plans/PLAN_COMPLETION_LOG.md`,
append the loop receipt, open the PR (no self-merge), and surface the left-open owner-gated row list
as the queue's residual for the owner.
