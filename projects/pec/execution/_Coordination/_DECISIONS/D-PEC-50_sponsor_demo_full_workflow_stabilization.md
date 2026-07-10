# D-PEC-50 — RULED: sponsor-demo full-workflow stabilization

**Status:** RULED 2026-07-09 — owner-directed execution
**Decision ID:** D-PEC-50
**Prepared by:** PEC work loop agent; ruling and direction are the owner's.
**Structure precedent:** sibling ruled packet
`D-PEC-48_reporting_vocabulary_alignment.md` (owner direction, exact fence,
verification/rollback, and human-ruling convention).

## Owner direction and supersession

Owner directions of record (Ryan Tufts, in-session, 2026-07-09):

> “We still have time to fix all this. Plan accordingly. Seek clarification
> when uncertain rather than assuming my intent for this app.”

> “1. Full workflow
> 2. Yes with all real and relevant click-throughs and direct controls over
> data tables to filter and sort views.
> 3. Yes rebuild the database from the recent input files only (the ones with
> filenames that start with a date).
>
> Consider revising or replacing the current workplan so these directives are
> integrated into the project's development loop.”

> “Proceed accordingly.”

This direction authorizes the stabilization outcome and replaces the prior
demo posture. It supersedes only the following earlier limitations:

- D-PEC-36/37 rejection of a web report viewer/export surface, narrowly enough
  to show a structured report result and download the generated draft;
- D-PEC-42's sidecar-only source fence, narrowly enough for the existing web
  agent attachment control to transmit XLSX bytes to that ruled parser; and
- the universal shell/navigation presentation, narrowly enough to provide the
  owner-directed strict PD/sponsor view.

All human-act, data-residency, factual-or-absent, proposal-gate, zero-dependency,
and no-issuance constraints remain unchanged.

## Authorized behavior

1. **Full PE workflow.** The agent panel accepts CSV/TSV/XLSX, declares the
   source coverage with the upload, maps through the existing sidecar parser,
   files an import proposal, and links the human to Admin for review,
   accept/apply. The agent still cannot accept/apply.
2. **Concise Word draft.** D-PEC-44 is fixed forward to match the completed
   exemplar's report form: disciplined hierarchy, narrative grouped summaries,
   running header/footer and page numbers, honest empty sections, compact basis
   notes, and no row dump. Activities report meaningful attested progress;
   package issues are consolidated without losing package/source references.
3. **Report result UX.** Standard report reads show a human-readable summary,
   and DOCX generation returns a safe browser download for the generated file.
   No report issuing/sending/storage workflow is added.
4. **Strict PD/sponsor shell.** Sponsor-only members see Overview, Packages,
   Disciplines, Deliverables, and Action & Hold Log. Agent, Raise, Plan, My Week,
   Registers, Admin, and other mutation/control affordances are hidden and
   direct web routes redirect to Overview. Server RBAC is unchanged.
5. **Table control.** Reporting tables have keyboard-operable column sorting,
   accessible labels, and relevant direct filters/search. Export reflects the
   displayed sorted/filtered rows. Drill links remain live.
6. **Demo rebuild.** Back up the current demo DB, then create a fresh TWD demo
   from system principals/configuration plus only current date-prefixed database
   input workbooks. The dated DOCX remains a template. Undated project-content
   inputs and legacy synthetic project records are excluded. Re-import of the
   same workbooks must update in place rather than duplicate.
7. **Responsive repair.** The strict shell and reporting pages are usable at
   desktop and narrow widths; navigation does not consume most of the initial
   narrow viewport and wide tables remain intentionally scroll-contained.

## Exact fence

Source execution may touch only:

- `projects/pec/agent-sidecar/**`
- `projects/pec/web/src/**`
- `projects/pec/server/src/agent-proxy.ts` and `projects/pec/server/src/api.ts`
  only if required for authenticated report download transport
- `projects/pec/server/test/**` and `projects/pec/agent-sidecar/test/**`
- `projects/pec/tools/rebuild-demo.ts`
- `projects/pec/package.json` (one rebuild script; no dependency change)
- `projects/pec/README.md`
- `projects/pec/execution/_Coordination/LAUNCH_RUNBOOK.md`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`
- `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_sponsor_demo_stabilization.md`
- this packet and the PEC decision register

Local/demo-data acts additionally authorized, never committed:

- WAL-safe backup and replacement of `projects/pec/pec-demo.db` plus WAL/SHM;
- generated reports under `projects/pec/pilot-scratch/reports/`;
- scratch databases and render/browser QA artifacts.

No `core/**`, no new dependency, no production/non-demo database, no report
issuance, no manual status/progress edits, no task-management or scheduling
surface.

## Verification and rollback

- PEC typecheck, all tests, production build, and pilot drill.
- Rebuild tool test/dry run on a scratch DB; exact dated input manifest; counts,
  quick-check, and update-only re-import verification.
- Render and inspect every generated DOCX page against the exemplar; content
  figures reconcile to report/view payloads.
- Browser walkthrough as PE and sponsor at desktop and narrow widths: upload,
  proposal review, all strict sponsor routes, filters/sorts/exports/drills,
  report generation/download; no console errors or page overflow.
- Self-check, coord-check, `git diff --check`, fence containment, and CI.
- Rollback source by reverting the tranche. Rollback demo data by stopping the
  app and restoring the verified pre-change backup.

## Human ruling

**RULED:** execute the owner-directed full workflow, strict PD view with real
drills/filter/sort controls, and dated-input-only demo rebuild described above.
The ruling basis is the verbatim owner direction and “Proceed accordingly.”
