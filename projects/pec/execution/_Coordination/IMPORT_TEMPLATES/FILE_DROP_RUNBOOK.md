# File-Drop Import Pathway (D-PEC-07 O-C, ruled 2026-07-05)

> **Epistemic status: coordination runbook under the D-PEC-07 O-C ruling.**
> This formalizes the zero-code pathway the owner approved: "user drops a
> file, agent maps → proposed import → user approves import." The in-app
> embedded upload agent is the separate design-brief track
> (`_DomainEngines/proposals/pec/`); this runbook needs no pec source change.

## v1.1 ruling (2026-07-05)

Owner ruling of record (verbatim, 2026-07-05, in-session, Ryan Tufts):

> S-2 (runbook v1.1): affirmed in full. RV-7: approval must follow the Step-3 proposed
> import — a drop-time "proceed"/"import it" message is not the approval; remove that
> shortcut. RV-8: scope the idempotency claim to the contracts actually evidenced (MDL,
> decisions); mark risks and schedule as code-implied but not yet evidenced. RV-9: change
> "(later: pilot) PEC_DB" to "pilot only under a future owner ruling." RV-10: add the
> export-and-compare verification as a standing rule. RV-11: note the commit-capture rule
> rides my 2026-07-05 basis and a materially new data source needs fresh confirmation of
> capture limits.

## v1.3 (2026-07-07)

Owner adoption of B-2 part 1 of the workflow-simplification brief
(`_DomainEngines/proposals/pec/BRIEF_2026-07-07_workflow_simplification.md`):
the standing-rules text superseded in-file by v1.2 step 5 is replaced by a
dated note, and step 5's discharged "until D-PEC-15 rules a convention"
condition now points at the 2026-07-07 ruling (interim rule stands). B-2
part 2 was declined — the v1.1 per-drop loop below remains current. No
import behavior changed.

## v1.4 (2026-07-09, D-PEC-35 O-A)

The embedded sidecar may now accept CSV, TSV, pipe/semicolon-delimited text,
or fixed-gap plain tabular text attachments. It canonicalizes safe header
variants, normalizes the content to the existing CSV proposal route, and
reports the selected contract, mapped headers, omitted source columns, and
required-cell gaps in the proposal result. Binary workbook parsing remains
out of scope until its own owner ruling after the revised MDL/RAIL templates.
The approval boundary is unchanged: the agent files or refreshes proposals;
the owner reviews, accepts, and applies in Admin.

## v1.5 (2026-07-09, D-PEC-39 O-A)

Every uploaded document may — and for period reporting should — carry a
PE-declared **coverage date range** (`coverage_start`/`coverage_end`,
YYYY-MM-DD, both or neither). Coverage rides the import proposal verbatim
(query params on the proposal route; "covering 2026-06-29 to 2026-07-05" to
the sidecar) and is never inferred from file content or timestamps. Overlaps,
gaps, and applied-without-declaration imports are CAUGHT as review signals on
`GET /api/projects/:pid/coverage` (COV-OVERLAP / COV-GAP / COV-UNDECLARED)
for agent/PE resolution — retroactive corrections are normal and are never
schema-blocked. Period-scoped read figures (`GET .../period-status`, and the
weekly standard report under `period_start`/`period_end`) name the applied
coverage declarations they rest on (PER-COV); a window no declaration covers
says so.

## v1.6 (2026-07-09, D-PEC-42 O-A)

The embedded sidecar now also accepts `.xlsx` workbooks natively (base64
attachment bytes; zero-dependency parser in the agent sidecar — pec
server/web runtime untouched). The parser reads sheets/cells (shared and
inline strings including rich-text runs, numbers, booleans, cached formula
values only — never formula evaluation, and 1900-system date serials emitted
as ISO dates), scans each sheet for a contract-shaped header row (title and
metadata rows above the header are tolerated), and feeds the matching sheet
into the same mapping → CSV proposal route as v1.4. All sheets — including
non-tabular ones (Rules of Credit, Data Dictionary, Lists, metadata blocks)
— are carried verbatim in the proposal result's workbook payload for the
D-PEC-41 full-fidelity capture; nothing is dropped. Anything the parser
cannot faithfully read (encrypted archives, zip64, unsupported compression,
the 1904 date system, malformed workbooks) is refused with a reported basis —
never guessed through. The approval boundary is unchanged: the agent files or
refreshes proposals; the owner reviews, accepts, and applies in Admin.

## The loop (per file drop)

1. **Drop.** Owner places the file under
   `projects/pec/pilot-scratch/input/` (gitignored; never committed) and
   tells the loop agent, naming the target contract if ambiguous and the
   covered dates (v1.5: "covering YYYY-MM-DD to YYYY-MM-DD") for period
   reporting.
2. **Map.** Agent SHA-256s the file, maps it to the §16/tracker contract per
   `IMPORT_MAPPING.md` (extending that doc for any new source shape), and
   writes the import-ready CSV under `pilot-scratch/import-ready/` for loop-run
   captures. In the embedded sidecar path, CSV/TSV/plain tabular attachments
   are normalized in memory to the same CSV proposal route before filing.
3. **Propose.** Agent presents: contract, row count, mapping/deltas, any
   fills (tagged in-row), expected accepted/reject profile, and which rows
   will land as unanchored intake.
4. **Approve.** Owner approves the import in-session (per the profile's
   `requires_human_confirmation` on `import.csv`). Approval must follow the
   Step-3 proposed import; a drop-time "proceed" or "import it" message is not
   the approval.
5. **Import + capture.** Agent imports over the authenticated API against the
   scratch `PEC_DB` (pilot only under a future owner ruling), captures the
   row-level report and refreshed exports into a dated
   `_DomainEngines/pec/PEC_*_evidence-*/` snapshot, takes a backup, and
   appends the loop receipt.

## Standing rules

- `force=true` never without a separate owner ruling; conflicts are reported,
  not overridden.
- *(v1.3, 2026-07-07)* The v1.1 "never re-import a full RAIL file" rule that
  stood here was superseded in-file by v1.2 step 5 (below), which governs RAIL
  re-imports; the superseded text is in git history. The v1.1 per-drop loop
  above stays current at owner direction (2026-07-07, B-2 part 2 declined).
- MDL and decisions re-imports are evidenced idempotent by their ID columns.
  Risks and schedule are code-implied idempotent but not yet evidenced as
  re-imports; report that status before proposing a whole-file re-import.
- Every import capture includes export-and-compare verification for the
  affected contract where the API exposes a register export.
- Raw dropped files and DB files stay uncommitted; run-generated exports/
  reports are the committable capture under the owner's 2026-07-05 basis.
  A materially new data source needs fresh owner confirmation of capture
  limits before its exports/reports are committed.
- Rows the agent cannot map without inventing meaning are proposed as
  questions or left to reject with reasons — never silently guessed; test-data
  fills happen only under an explicit owner ruling and are tagged in-row.
- *(v1.6, 2026-07-09)* Binary `.xlsx` workbooks are now accepted on the
  sidecar lane under D-PEC-42 O-A (the v1.4-era "convert to CSV/TSV or wait"
  rule is discharged). Workbook features the parser cannot faithfully read
  are refused with a reported basis; `.xlsm` macros are never executed
  (captured only as file provenance, per the D-PEC-42 scope).

## v1.2 — the weekly agent intake+triage cycle (D-PEC-10 O-A, ruled 2026-07-05)

Authorized mechanism (packet: `../_DECISIONS/D-PEC-10_agent_intake_triage.md`;
rehearsed: `_DomainEngines/pec/PEC_2026-07-05_DPEC10-rehearsal-01/`):

1. **Drop.** Owner places the weekly documents (RAIL, MDL — risks/schedule per
   D-PEC-14, Package Tracker per D-PEC-13 once ruled).
2. **Propose serially, one document at a time.** The agent (its own
   provisioned person, `is_admin=0`, coordinator) files one import proposal,
   the owner accepts + applies it at the screen, then the agent files the
   next. Anchors resolve at dry-run time, so a RAIL proposal filed before the
   MDL apply lands unanchored — file MDL first, or refresh the RAIL dry-run
   after the MDL apply. An apply moves the watermark; a proposal left pending
   across another apply just needs a refresh + re-accept (this is the guard
   working, not a fault).
3. **Accept/apply are the owner's screen acts, always.** A refreshed dry-run
   voids any prior acceptance (RV-13); the owner re-reviews from the new basis.
4. **Triage after the applies.** The agent open-triages and dispositions the
   un-dispositioned intake queue: `converted` routes to the correct record
   (decisions arrive via triage conversion or owner screen entry — D-PEC-10
   WF-10, never an import assumption), `parked`/`duplicate`/`rejected` with
   grounds in the note; items the agent cannot ground in a source row are left
   un-dispositioned for the owner. Conversion never creates approval records
   (agent-act rider).
5. **Re-import boundary (supersedes the v1.1 "never re-import a full RAIL
   file" rule, which predates the PR #82 repair).** Evidenced 2026-07-05: a
   full RAIL re-import updates un-dispositioned intake items in place (no
   duplication) and reports a changed statement as an OM-3 conflict; rows
   whose intake items are already **dispositioned** re-land as NEW intake
   items — drop dispositioned `item_id`s from the weekly export or expect and
   triage the re-landed rows. *(Standing per the 2026-07-07 D-PEC-15 ruling —
   indefinitely postponed; the interim rule stands.)*
6. **Capture.** Evidence per the L3-evidence convention when the run is a
   governed rung; routine weekly cycles log through the app's own history —
   the append-only record separates agent acts from the owner's by person.
