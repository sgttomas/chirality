# PEC Human Decision Register - Preparation Tracking

**Created:** 2026-07-04. Non-governing tracking surface. This register tracks
PEC-local decision-packet preparation and ruling pointers. It confers no
authority: agents prepare packets labeled `PROPOSAL`; only the human project
authority rules. PEC tier-0 registration decisions remain in
`_DomainEngines/_DECISIONS/_REGISTER.md`.

**Packet location:** `execution/_Coordination/_DECISIONS/D-PEC-XX_<slug>.md`

**Row states:** `NOT_PREPARED` -> `AWAITING_RULING` (packet drafted) -> `RULED`
(pointer to the human record).

**Residual-work rows (convention, owner-ruled 2026-07-03):** a ruling that
leaves residual work does not reopen or annotate the ruled row; the residue
gets its own new row with its own provenance and an open ruling cell until the
owner rules. This mirrors the tier-0/piping convention and keeps open work
machine-visible.

| ID | Decision | Blocks | State | Packet | Ruling record |
|---|---|---|---|---|---|
| D-PEC-01 | Pilot rehearsal and real MDL/RAIL/import authorization: whether, when, and with what data-residency basis the pilot team imports real spreadsheets and rehearses a real restore. | Real pilot execution; any agent-visible instance-data capture. | RULED | `D-PEC-01_pilot_rehearsal_real_data_authorization.md` | O-A affirmed 2026-07-05; ruling SHA `3e4ba7543` |
| D-PEC-02 | Post-pilot P3 scope selection after pilot feedback: monthly reconciliation loop, archive views, lessons learned, authority matrix/approval-route templates, and supersession-impact propagation. | P3 planning and implementation order. | NOT_PREPARED | - | - |
| D-PEC-03 | Pointer row: PEC tier-0 integration decisions D-T0-11..16 are governed in `_DomainEngines/_DECISIONS/`, not duplicated here. | Local agents finding the tier-0 gate surface. | NOT_PREPARED | - | `_DomainEngines/_DECISIONS/_REGISTER.md` |
| D-PEC-04 | PEC profile Gate 2 timing after D-PEC-01: whether to adopt now or keep `_DomainEngines/profiles/pec.yaml` DRAFT until pilot evidence validates the operation surface. | Profile adoption. | RULED | `D-PEC-04_profile_gate2_after_pilot.md` | O-B affirmed 2026-07-05; ruling SHA `3e4ba7543` |
| D-PEC-05 | PEC L3/proposal-shaped apply timing: whether to authorize L3 design now or defer until after D-PEC-01 pilot evidence. | L3 planning and proposal-shaped apply path. | RULED | `D-PEC-05_l3_deferred_after_pilot.md` | O-B affirmed 2026-07-05; ruling SHA `3e4ba7543` |
| D-PEC-06 | `seed.demo` guard repair authorization: make seed honor `PEC_DB` and refuse non-scratch/non-demo targets. | Narrow future code-change PR under `projects/pec/tools/**`. | RULED | `D-PEC-06_seed_demo_guard_repair_authorization.md` | O-A affirmed 2026-07-05; ruling SHA `3e4ba7543` |
| D-PEC-07 | Embedded upload-agent pathway: how "owner uploads a file → agent takes action to update things" is realized (loop-agent pathway now vs L3 in-app design brief vs both), now that D-PEC-05's pilot-evidence precondition is met. | The stated end goal; any L3 design brief; formalized file-drop import runs. | RULED | `D-PEC-07_embedded_upload_agent_pathway.md` | O-C affirmed 2026-07-05; ruling SHA `1a9e4071c` |
| D-PEC-08 | Source-tranche authorization for the adopted embedded upload-agent design brief. | Any implementation of the upload-agent brief under `projects/pec/{server,web,core}/**`. | RULED | `D-PEC-08_upload_agent_source_tranche_authorization.md` | O-A affirmed 2026-07-05 (in-session steer); tranche packet `../TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md` |
| D-PEC-09 | CSV formula-injection neutralization in exported CSVs. | Any source change that changes CSV export escaping or neutralization behavior. | RULED | `D-PEC-09_csv_formula_injection_repair.md` | O-A affirmed 2026-07-05; source change + merge authorized in-session |
| D-PEC-10 | Agent-performed intake triage: mechanism for the embedded agent to triage/disposition intake items (owner direction 2026-07-05: delegate intake of the imported items to the agent once it has the capability). Triage is an RBAC'd in-app act today (`intake.triage`: coordinator/pm/admin); an agent pathway needs its own proposal-shaped design + authorization. Widened 2026-07-05 by the owner workflow intent of record (quoted verbatim in the packet): five source documents, weekly cycle, agent as primary update means, obligations WF-1..11 + rehearsal gate. | Agent triage of the 272 imported intake items; the owner's weekly agent-update workflow. | RULED | `D-PEC-10_agent_intake_triage.md` | O-A affirmed 2026-07-05; ruling SHA `9dd310cc3` |
| D-PEC-13 | Package Tracker import contract + proposal-shaped agent path (D-PEC-10 obligation WF-5, parked by construction — no §16 contract exists; owner direction 2026-07-05: its own row, never an awkward MDL mapping). Carries the sixth-contract L3-scope question (D-PEC-12 §2: "Any other operation family needs its own row."). | The Package Tracker half of the owner's five-document weekly workflow. | NOT_PREPARED | - | - |
| D-PEC-14 | Risk Log + Schedule proposal-path live evidence (D-PEC-10 obligations WF-3/WF-4): a live-API scratch-basis exercise captured as evidence, or a per-contract test under a ruled source tranche — undischarged by the RAIL+MDL rehearsal per direction item 3. | WF-3/WF-4 discharge; the risks/schedule half of the weekly workflow at evidence level. | NOT_PREPARED | - | - |
| D-PEC-15 | Post-disposition weekly re-import behavior: RAIL rows whose intake items are already dispositioned re-land as NEW intake items on the next full re-import (rehearsal-01 observation, IPR-0006 dry-run: 4 of 7 rows would re-land; un-dispositioned rows update in place). Needs a ruled convention — drop dispositioned `item_id`s from the weekly export, expect-and-triage the re-landed rows, or a source change under its own tranche. Interim rule documented in `../IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md` v1.2 step 5. | A clean weekly re-import cycle once triage is routine. | NOT_PREPARED | - | - |
| D-PEC-11 | Pointer row: PEC profile Gate-2 adoption (successor to the D-PEC-04 O-B deferral) is governed in tier-0 — ruled 2026-07-05, recorded in the `D-T0-12` packet's dated adoption note. | Local agents finding the adoption record. | RULED | - | `_DomainEngines/_DECISIONS/D-T0-12_pec_profile_lifecycle.md` (Gate-2 adoption note, 2026-07-05) |
| D-PEC-12 | L3 operation-proposal semantics for the import seam: single record of authority (in-app `import_proposal`), scope (five §16 contracts), agent-propose/human-accept-apply split, CLOSED-residency report visibility, evidence convention, profile edits. Companion to tier-0 `D-T0-18`. | Any L3 / proposal-shaped apply path; profile `integration_level` advance. | RULED | `D-PEC-12_l3_import_proposal_semantics.md` | Ruled with owner amendment 2026-07-05 (full agency inside the mechanical harnesses; verbatim in packet) |
