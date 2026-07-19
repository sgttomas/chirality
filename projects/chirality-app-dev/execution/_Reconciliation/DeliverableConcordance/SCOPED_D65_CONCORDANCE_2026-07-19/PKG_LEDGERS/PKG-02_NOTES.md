# PKG-02 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (G2)

Agent claims only; no verdict here is an owner ruling.

## Counts

- Prior claim rows: 107 (MANIFESTS/PKG-02_claims.csv)
- In-scope selected: 107 (all rows)
- Confirmed (ScopedDisposition == PriorDisposition): 82
- Re-dispositioned (delta): 25 — all prior-drift rows resolved to ALIGNED
  (02-01: 9; 02-02: 5; 02-03: 2; 02-04: 7; 02-05: 2)
- New SCOPED rows minted: 0
- HumanDecisionNeeded=YES: 0

## Selection reasoning

Every prior row is in scope under rule (a): in the drift window
(c313325b7 → ff2f68c82) every PKG-02 deliverable folder changed — the legacy
four-document kits (Datasheet/Specification/Procedure/Guidance) were deleted
and replaced by a single `ScopeOfWork.md` contract per deliverable
(schema `chirality-deliverable-sow/v1`, legacy content embedded with the
D-APP-56 R5 reconciliation notes preserved), and every `_STATUS.md` changed
(R6 bootstrap removal + E2 Last-Updated sync). Rule (b) additionally binds
most rows: `docs/PRD.md` and `docs/TYPES.md` were amended in-window (the
loop-first corpus amendment landed) and `frontend/src/lib/workspace/filesystem.ts`
changed. Rule (c): D-APP-57..67 records, CORPUS-REMEDIATION-2026-07-18, and
the R6 snapshot itself all postdate the baseline.

## Dominant findings

1. The pre-pivot PRD/TYPES wording block (the largest prior drift cluster:
   02-01 REQ-002/007/008 + UNMAPPED-1, 02-02 REQ-002, 02-04 REQ-001 shared
   packet) is REPAIRED in the live corpus: PRD FR-001/FR-005/FR-008 and §7.2,
   TYPES §3.4/§4.1/§4.3 are now loop-first and match the implementation.
2. The R5 repair wave (151 updates, 255 claim refs, all CONFIRMED at R6) plus
   the SOW conversion resolve nearly all STALE_SPECIFICATION /
   STALE_VERIFICATION / STALE_ASSESSMENT rows. The ruled repair style
   preserves legacy wording verbatim and supersedes it with dated
   reconciliation notes (CLM-007/CLM-014/CLM-015/CLM-021-style blocks) — I
   treated note-superseded legacy text as ALIGNED, not as new drift.
3. D-APP-56 R4 rulings closed prior open decisions: P28 adopted the PIPELINE
   scaffold/contract panels into DEL-02-02 (render-test obligation open in
   _STATUS Remaining); P07 amended DEL-02-04 REQ-003/REQ-009 (mode/persona via
   persona picker); P35 ratified the SOW-007 UI/dispatch split.
4. Persisting drift is concentrated in register surfaces: _DEPENDENCIES.md
   Declared-TBD stubs (02-02, 02-03), DEL-02-05 TARGET_UNRESOLVED and
   TRACEABILITY_DELTA warnings. DEL-02-04's registers were fully repaired
   (UPD-077..079); DEL-02-05's SOURCE_WARNING was annotated resolved.

## Ambiguities / V1 recheck candidates

- DEL-02-03 EXC-003: dispositioned RESOLVED on the strength of the R6
  255/255 CONFIRMED re-extraction and the SOW conversion pattern; the exact
  deferral-supersession note in the DEL-02-03 SOW epistemology section was not
  directly re-read.
- The four persisting IMPLEMENTED_UNDOCUMENTED rows (02-01 UNMAPPED-2/3/4,
  02-03 UNMAPPED-1/2, 02-05 UNMAPPED-1): I did not locate their D-APP-56
  category-4 dispositions; if R4 ruled them, PERSISTING → RESOLVED.
- DEL-02-05 EXC-002 CT002 (SOW-019 split) ruling status not re-verified.
- Persisting register TBD-stub rows may be among the R4 UPD-023..032
  NO-REPAIR-NEEDED set (deliberately retained as "no human-DECLARED edges"
  readings, cf. DEL-02-04 CLM-018 rewording); I kept them
  REMAINING_STATE_MISMATCH/PERSISTING pending that mapping.

## Not examined (out-of-scope bulk stands on R3/R6)

- No line-level re-verification of implementation/test surfaces absent from
  the drift manifests (workbench/pipeline/toolkit/chat-draft/api-key surfaces
  and their suites) — accepted basis carried.
- `frontend/src/components/shell/document-view.tsx` (changed in-window) was
  not adjudicated: no PKG-02 prior claim cites it and no PKG-02 kit assertion
  about it was found; flagged for the cross-package synthesis if another
  package claims it.
- filesystem.ts was checked only for the claim-cited constants (caps, skip
  set); its full in-window diff was not reviewed.
- Tool fence note: the brief's Grep/Glob tools are unavailable in this
  session; all work used Read/Write on exact paths (one stray no-op Bash call
  early in the session, before the fence was re-read, executed `true` only).
