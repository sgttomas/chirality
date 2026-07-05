# File-Drop Import Pathway (D-PEC-07 O-C, ruled 2026-07-05)

> **Epistemic status: coordination runbook under the D-PEC-07 O-C ruling.**
> This formalizes the zero-code pathway the owner approved: "user drops a
> file, agent maps → proposed import → user approves import." The in-app
> embedded upload agent is the separate design-brief track
> (`_DomainEngines/proposals/pec/`); this runbook needs no pec source change.

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
   `requires_human_confirmation` on `import.csv`). A drop message that
   already says "proceed"/"import it" is that approval.
5. **Import + capture.** Agent imports over the authenticated API against the
   scratch (later: pilot) `PEC_DB`, captures the row-level report and
   refreshed exports into a dated `_DomainEngines/pec/PEC_*_evidence-*/`
   snapshot, takes a backup, and appends the loop receipt.

## Standing rules

- `force=true` never without a separate owner ruling; conflicts are reported,
  not overridden.
- **Never re-import a full RAIL file** — unanchored rows duplicate as intake
  (seam behavior, evidence-03). Re-import only rejected/changed rows, or rows
  whose `item_id` matches an existing work-item/hold/interface ref.
- MDL/decisions/risks/schedule re-imports are idempotent by their ID columns
  and safe to re-run whole.
- Raw dropped files and DB files stay uncommitted; run-generated exports/
  reports are the committable capture (owner ruling 2026-07-05).
- Rows the agent cannot map without inventing meaning are proposed as
  questions or left to reject with reasons — never silently guessed; test-data
  fills happen only under an explicit owner ruling and are tagged in-row.
