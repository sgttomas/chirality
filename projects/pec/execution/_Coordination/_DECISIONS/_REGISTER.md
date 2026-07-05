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
| D-PEC-01 | Pilot rehearsal and real MDL/RAIL/import authorization: whether, when, and with what data-residency basis the pilot team imports real spreadsheets and rehearses a real restore. | Real pilot execution; any agent-visible instance-data capture. | RULED | `D-PEC-01_pilot_rehearsal_real_data_authorization.md` | O-A affirmed 2026-07-05; ruling SHA TBD |
| D-PEC-02 | Post-pilot P3 scope selection after pilot feedback: monthly reconciliation loop, archive views, lessons learned, authority matrix/approval-route templates, and supersession-impact propagation. | P3 planning and implementation order. | NOT_PREPARED | - | - |
| D-PEC-03 | Pointer row: PEC tier-0 integration decisions D-T0-11..16 are governed in `_DomainEngines/_DECISIONS/`, not duplicated here. | Local agents finding the tier-0 gate surface. | NOT_PREPARED | - | `_DomainEngines/_DECISIONS/_REGISTER.md` |
| D-PEC-04 | PEC profile Gate 2 timing after D-PEC-01: whether to adopt now or keep `_DomainEngines/profiles/pec.yaml` DRAFT until pilot evidence validates the operation surface. | Profile adoption. | RULED | `D-PEC-04_profile_gate2_after_pilot.md` | O-B affirmed 2026-07-05; ruling SHA TBD |
| D-PEC-05 | PEC L3/proposal-shaped apply timing: whether to authorize L3 design now or defer until after D-PEC-01 pilot evidence. | L3 planning and proposal-shaped apply path. | RULED | `D-PEC-05_l3_deferred_after_pilot.md` | O-B affirmed 2026-07-05; ruling SHA TBD |
| D-PEC-06 | `seed.demo` guard repair authorization: make seed honor `PEC_DB` and refuse non-scratch/non-demo targets. | Narrow future code-change PR under `projects/pec/tools/**`. | RULED | `D-PEC-06_seed_demo_guard_repair_authorization.md` | O-A affirmed 2026-07-05; ruling SHA TBD |
