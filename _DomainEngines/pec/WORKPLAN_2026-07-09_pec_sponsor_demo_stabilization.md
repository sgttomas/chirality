# PEC Work Loop — sponsor-demo stabilization standing plan

> **Epistemic status: owner-directed standing plan.** Created 2026-07-09 from
> the owner directions recorded in D-PEC-50. It replaces the prior
> reporting-product standing plan. Accepted decision
> packets and the live tree remain authoritative; this file is the loop protocol,
> durable owner intent, and ordering map, never a status ledger.

## Owner intent

PEC must demonstrate the complete reporting workflow for the sponsor:

1. the PE uploads the current dated XLSX source workbooks with an explicit
   coverage declaration;
2. the agent maps them through the proposal gate and a human reviews,
   accepts, and applies them;
3. the same facts appear in role-appropriate live views with real drill paths
   and direct filter/sort controls;
4. the sidecar produces a concise, template-quality Word draft that can be
   downloaded, opened, edited, and issued outside PEC; and
5. the PD/sponsor receives a strict read-only interface containing only real
   reporting and drill-down surfaces.

The demo database is rebuilt from the current input files whose basenames begin
with a date. At present the database-bearing set is the two 2026-07-07 XLSX
workbooks; the dated DOCX is the report template, not database content.
Undated legacy input files and old seed records do not enter the rebuilt TWD
demo database. System principals, project membership, and configuration needed
to operate the app are infrastructure, not project-source content.

The same demo database also carries a blank `TBL` project for rehearsing the
complete import workflow without disturbing populated TWD. TBL shares TWD's
demo people and role grants but begins with no packages, deliverables, work
items, proposals, or other project records. TWD remains the populated sponsor
view; TBL is the disposable workflow-demonstration target.

Reporting remains factual-or-absent. Percent complete is imported PE-attested
data, never an in-app edit or derivation. Issues are package-level action items,
risks, and holds; decisions and interfaces remain segregated. Reports are
drafted in PEC and issued outside it. Task management, planning, scheduling,
and professional approval claims remain out of scope.

Package discipline is also source-attested and may be multi-valued. The import
lane preserves every distinct MDL/RAIL association, and Packages must display
the complete set with direct discipline filter/sort/search controls. The
owner accepts the existing package action-item superset; that record model is
not narrowed for the demo.

## Loop protocol

0. **Discover.** Resolve the repo root, inspect git/receipts/registers/profile,
   run `self-check`, and verify every dated-map claim against the live tree.
1. **Select.** Execute the widest owner-authorized tranche. Demo blockers and
   end-to-end workflow continuity outrank deferred roadmap work.
2. **Fence.** Source work requires an owner-ruled D-PEC packet naming exact
   paths, data acts, checks, rollback, and any superseded prior ruling.
3. **Gate.** Adoption, ruling, acceptance, apply, and issuance remain human
   acts. Never infer a coverage declaration or lifecycle decision.
4. **Execute.** Branch-first. Keep concurrent scopes disjoint. Never mutate a
   non-demo database. Back up `pec-demo.db` before replacement and verify the
   backup read-only. Do not commit demo data or owner source files.
5. **Check.** At the final source SHA run self-check, coord-check, diff-check,
   full PEC typecheck/tests/build/drill, rendered DOCX review of every page,
   and browser passes at desktop and narrow viewports for every changed flow.
6. **Close.** Append a minimal receipt with owner directions verbatim, pointers,
   gate outcomes, checks, database backup/rebuild counts, and remaining blocks.

## Binding constraints

- F-PEC-1..4 continue unchanged except where an owner-ruled packet names an
  exact source or demo-data opening.
- No new runtime dependency without its own owner ruling. D-PEC-50 retains the
  zero-dependency posture.
- Upload is proposal-gated; the agent never accepts/applies.
- Sponsor/PD surfaces are read-only and role-tailored; server RBAC remains the
  authority even when the web shell hides irrelevant routes.
- Every displayed figure drills to contributing records or names an honest
  absence. Filters and sorting change presentation only, never source truth.
- Report basis annotations remain machine/PE-auditable but must not overwhelm
  sponsor prose. They use a restrained, removable visual treatment.
- `pec-demo.db`, backups, pilot inputs, and generated reports remain outside
  committed source. Replacement of the local demo DB is allowed only by an
  explicit owner direction and after a verified WAL-safe backup.

## Stabilization sequence

| Order | Tranche | Completion test |
|---|---|---|
| S0 | Governance and backup | D-PEC-50 recorded; existing demo DB backed up and verified before replacement |
| S1 | Dated-input-only demo rebuild | Populated TWD content from the dated MDL/RAIL workbooks plus blank TBL with matching demo roles; re-import is update-only/idempotent; no legacy seed content |
| S2 | Report composition | Generated DOCX follows the exemplar's concise hierarchy and page furniture, summarizes rather than dumps rows, renders cleanly, and exposes a browser download |
| S3 | PE full workflow | XLSX attach -> mapped proposal -> Admin review/accept/apply -> live views -> report draft/download works without shell/CLI intervention |
| S4 | PD/sponsor UX | Strict read-only navigation; real drills; sortable/filterable reporting tables including complete multi-discipline package values; no irrelevant mutation/admin/planning controls |
| S5 | Sponsor rehearsal | Desktop and narrow passes, no console errors, consistent counts, known-good backup/report safety copies retained |

## Parked work

- D-PEC-49 week-over-week observations remains owner-gated and is not required
  for this demo; the UI states the delta is absent.
- Interfaces remain absent until a current dated interfaces input is supplied.
- Needs audience remains unclassified until a current source column supplies it.
- Resource loading, schedule forecasting, task boards, report issuance, and
  professional approval remain outside this plan.

## Live pointers

- Decision registers: `_DomainEngines/_DECISIONS/_REGISTER.md` and
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- Source authorization: `D-PEC-50_sponsor_demo_full_workflow_stabilization.md`
- Profile: `_DomainEngines/profiles/pec.yaml`
- Report basis: `projects/pec/execution/_Coordination/REPORT_BASIS.md`
- Handoff ledger: `_DomainEngines/pec/LOOP_RECEIPTS.md`
