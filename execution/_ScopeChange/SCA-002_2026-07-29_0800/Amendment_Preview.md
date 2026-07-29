---
amendment_id: SCA-002
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-07-29
status: awaiting_gate_3_approval
accepted_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md revision 1.1
requested_by: Ryan Tufts (through the D-GOV-31 adoption ruling)
upstream_authority: D-GOV-31; Root PRD Revision 7; D-8 successor + annex §5.3.1
---

# SCA-002 Gate 3 — Exact Amendment Preview

## Approval scope

This is the complete proposed revision 1.1 → 1.2 amendment. **It is a
candidate only. No file under `execution/_Decomposition/` has changed.** The
exact candidate bytes are under `Gate_3_Candidate/`; the complete
three-surface before/after is `Gate_3_Exact_Amendment.diff`; the candidate is
reproducible from the frozen basis with `build_gate3_candidate.py` and passes
all 37 deterministic checks in `Gate_3_Validation.json`.

Owner approval of this preview is **PENDING**. Approval would authorize only
these exact bytes for a later, separately gated application act.

## A001 — exact SOW-042 row (scope ledger line 43)

Superseded `ScopeItemStatement` (verbatim):

> Git closeout runs through the change-management role with human-gated pull
> requests and never self-merge.

Successor `ScopeItemStatement` (verbatim, aligned with the live D-8 row):

> Git closeout in every registered loop runs through the shared
> change-management role with human-gated pull requests as the standing
> default; a bounded owner grant, recorded before or at exercise, may
> authorize merge execution under the merge-gate policy in PRD annex §5.3.1,
> which preserves K-MERGE-1 and the four closeout identities (semantic
> approval, approved source SHA, merge authorization, effective merge SHA).
> Each loop's stricter local merge discipline remains controlling until that
> loop adopts or acknowledges the policy under its own instruments.

Every other cell is byte-preserved: `ScopeItemID=SOW-042`, `InOutStatus=IN`,
`SourceRef=PRD §5.3 D-8 [TRANSCRIBED]` (bracket retained — see the flagged
owner decision in `Impact_Assessment.md`), `PackageID=PKG-04…`,
`DeliverableIDs=DEL-04-06…`, `ObjectiveIDs=OBJ-002`, `PRDItem=D-8`,
`Categories=DevelopmentalMachinery`, empty `DecisionRef`, `OpenIssue=FALSE`,
empty `Notes`. The statement cell becomes CSV-quoted because the successor
text contains commas; the row's CRLF record terminator is preserved.

## A002 — exact DEL-04-06 row (deliverable register line 27)

Superseded `Description` (verbatim):

> Keep git closeout running through the change-management role with
> human-gated pull requests and no self-merge.

Successor `Description` (verbatim):

> Keep git closeout running through the shared change-management role with
> human-gated pull requests as the standing default; preserve K-MERGE-1 and
> the four closeout identities (semantic approval, approved source SHA, merge
> authorization, effective merge SHA) in every closeout; a bounded owner
> grant recorded per PRD annex §5.3.1 before or at exercise may authorize
> merge execution within its recorded scope and term.

Superseded `AnticipatedArtifacts` (verbatim):

> Closeout checklist; no-self-merge evidence; PR gate notes

Successor `AnticipatedArtifacts` (verbatim):

> Closeout checklist; four-identity closeout evidence (semantic approval,
> approved source SHA, merge authorization, effective merge SHA);
> bounded-owner-grant records when a grant is exercised; PR gate notes

Every other cell is byte-preserved: ID, name, `ParentPackageID=PKG-04…`,
`ResponsibleParty=Ryan Tufts`, `Type=CI_CD_CHANGE`,
`CoversScopeItems=SOW-042`, `SupportsObjectives=OBJ-002`,
`ContextEnvelope=S`, `ContextEnvelopeNotes=One narrow procedural control.`,
`AnticipatedWriteLocus=execution-tree`. The file's LF terminators are
preserved.

## A003 — working-surface change register, revision metadata, source pin

Traceability-required minimum in
`Chirality_Root_SOFTWARE_DECOMP_v1_0.md` (the file contains no old-text
occurrence):

1. Title and header: `SCA-002 CANDIDATE v1.2`, dated 2026-07-29, source-basis
   commit `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (D-GOV-31 effective
   merge; PRD Revision 7), predecessor identities for v1.1 and v1.0 retained
   explicitly, run `GOV-STEP4-SCA-20260729`.
2. Status banner: replaced with a candidate banner stating that revision 1.1
   remains the accepted basis, that these v1.2 bytes take effect only upon
   the SCA-002 owner gate confirmations plus a separately gated application
   act, and that no owner acceptance has occurred at drafting time.
3. §2.1 REF-001: sha256 advances
   `0e36a03a… → 15fba9c3…` and basis
   `fb0b3d24… (D-GOV-28 EffectiveSHA) → ea3db360… (D-GOV-31 effective merge;
   PRD Revision 7)`.
4. §13: DEC-023 records the restatement, its D-GOV-31 authority, the retained
   `[TRANSCRIBED]` bracket flag, and the candidate-only condition; one Change
   Log entry dated 2026-07-29 mirrors it.

No Gate Log row, package, deliverable, objective, scope, telemetry, or
downstream-note content changes. The candidate working surface carries no
literal occurrence of the superseded phrase.

## Candidate identity

| Surface | Basis (v1.1) SHA-256 | Candidate (v1.2) SHA-256 |
|---|---|---|
| Working surface | `2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18` | `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49` |
| Scope ledger | `0d48abe08aa336ac5e495650451f286b4b717606f047adff931c45dacc8531a4` | `61992b3c43da62f4ecbb1f43bab4d1c62835be19102763645f2418abe6b478d7` |
| Deliverable register | `ec32b36fdc078e44a7ca094e9c854a3be6b7d5917360fe5ef5f22ff3702a13b8` | `b18ebe6b9bc3cdac6bd0bd78f6470be328a81783c7c6ab5b55478b506c61e8da` |

The four untouched decomposition surfaces are not copied into
`Gate_3_Candidate/`; they are `NO_CHANGE` and remain at their basis
identities recorded in `Pre_Change_Register_Baseline.json`.

## Validation result and authority boundary

`Gate_3_Validation.json` reports `PASS`: 37 checks, 0 failures — basis
integrity, PRD Rev 7 subject parity, single-record isolation per CSV, column
counts, terminator preservation, unique IDs, status counts, lineage
preservation, successor-policy token presence, old-text absence, and
working-surface change-register presence.

This preview approves nothing by itself. It does not modify decomposition
truth, issue or exercise any grant, alter any loop's merge discipline,
rewrite any frozen record, or authorize application; application follows only
after owner acceptance, as a separate gated act.

## Gate 3 question (for the owner, at review)

Do you approve these amendments to the decomposition document?
