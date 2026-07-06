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

## The loop (per file drop)

1. **Drop.** Owner places the file under
   `projects/pec/pilot-scratch/input/` (gitignored; never committed) and
   tells the loop agent, naming the target contract if ambiguous.
2. **Map.** Agent SHA-256s the file, maps it to the §16 contract per
   `IMPORT_MAPPING.md` (extending that doc for any new source shape), and
   writes the import-ready CSV under `pilot-scratch/import-ready/`.
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
- **Never re-import a full RAIL file** — unanchored rows duplicate as intake
  (seam behavior, evidence-03). Re-import only rejected/changed rows, or rows
  whose `item_id` matches an existing work-item/hold/interface ref.
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
