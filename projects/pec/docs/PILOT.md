# PEC pilot runbook

How to take a real project live on PEC and run it for the pilot period. This is the operational
companion to the PRD (§16 imports, §18 success metrics) and STATUS "What's next" item B. Every step
here is rehearsable in advance with `npm run drill` — run that first; it must print `PASS`.

## 0. Pre-pilot rehearsal (the drill)

```bash
npm install
npm test          # 161 tests green, including the PEC-NFR-009 backup/restore round-trip
npm run drill     # full pipeline rehearsal on bundled fixtures → must PASS
```

`tools/pilot-drill.ts` rehearses, against a scratch database (never `pec.db`): the four §16 imports
in pilot order with row-level reject reporting, an MDL re-import to prove idempotency, a coordinator
triage pass over the unanchored intake, derived-view rendering inside the PEC-NFR-003 budget, and a
backup → mutate → restore cycle through `tools/backup.ts`.

**Shake down the real spreadsheets the same way** before go-live:

```bash
node tools/pilot-drill.ts --mdl mdl.csv --rail rail.csv --decisions decisions.csv --risks risks.csv
```

Fix rejected rows in the source spreadsheets (owners must match a person by email or exact name;
dates are `YYYY-MM-DD`; hold rows need a typed `hold_cause` — I-3) until the reject count is only
what you expect. Rows with an unmatched `deliverable_ref` are not errors: they land as unanchored
intake for triage (I-2).

## 1. Provision people and the project

P1 has no user-management UI (ADR-007: seeded users; SSO is P2). Provision by script: copy the
people/project/roles section of `tools/seed.ts` (§1–3) into a one-off setup script for the pilot
project — one `person` row per participant (email is the import match key), one `project`, and
`project_role` rows per §14. Set the project timezone and weekend days correctly: every working-day
threshold depends on them (PEC-NFR-010).

Then set thresholds for the pilot in **Admin → Thresholds** (defaults per PRD §8.4, PEC-OV-007).

## 2. Import, in this order

Order matters: MDL creates packages/deliverables/revisions; RAIL anchors onto MDL doc numbers.

| Step | Where | Contract | Notes |
|---|---|---|---|
| 1 | Admin → Import | `mdl` | Packages auto-created on first sight. Revisions are seeded **at their imported state** (history `kind=import`) — seeding, not transitions. |
| 2 | Admin → Import | `rail` | `type` = work-item kinds, `hold` (needs `hold_cause`), or `interface`. Unmatched `deliverable_ref` → unanchored intake, flagged in the triage queue. |
| 3 | Admin → Import | `decisions` | `decided` rows require an `outcome`. `affected_refs` (semicolon-separated doc numbers) link deliverables. |
| 4 | Admin → Import | `risks` | `probability`/`impact` are 1–5. |

Semantics to brief the document controller on:

- **Row-level reporting, nothing silent**: every row is accepted, updated, a conflict, rejected
  (with reasons), or lands as intake. Fix and re-import — re-imports are idempotent on the external
  id (`doc_no`, `item_id`, `decision_id`, `risk_id`).
- **Conflicts**: a record edited in-app since the last import is *not* overwritten; the row reports
  a conflict. `force=true` (checkbox in Admin) overwrites deliberately (PEC-NFR-004).
- **Lifecycle protection**: an import can seed a brand-new revision at any state, but never forces
  an existing revision's state — issue-affecting transitions only happen through the gated
  workflow (I-5, D-11).
- **Round-trip**: `Admin → Export` mirrors the same schemas, so the existing spreadsheets keep
  working during adoption (§16); `export/rail.csv` includes unanchored intake so nothing is lost.

## 3. The weekly coordinator triage (the habit that keeps the log clean)

Cadence per PRD §10; untriaged age is a governance signal (warn > 2 wd, escalate > 5 wd, §8.4).

1. **Log → Triage queue**: work oldest-first (the queue is sorted by untriaged age).
2. Open the item (`open triage`), read the statement as raised — it stays verbatim forever (OM-3).
3. Disposition it (PEC-AHL-004): **converted** (create the anchored work items / holds / risks /
   decisions / interfaces it resolves into — one intake may become several records, each
   back-linked), **merged**, **duplicate**, **rejected**, or **parked**.
4. Anchor every converted record to a real project object — unanchored work cannot enter plans or
   rollups (I-2). The raiser is notified automatically at routing and closure (PEC-AHL-007).
5. Sweep **Log → All open items** for overdue and aging rows; chase owners, raise holds where the
   cause is real and typed (I-3).

Target for the pilot (§18): median untriaged age ≤ 2 working days, ≥ 95 % of open items anchored.

## 4. Backups (PEC-NFR-009: RPO ≤ 24 h)

Schedule a **daily** backup on the host that runs the server:

```cron
15 2 * * *  cd /path/to/pec && node tools/backup.ts >> backups/backup.log 2>&1
```

`backup` takes a WAL-safe `VACUUM INTO` snapshot — safe while the server is running — into
`backups/pec-YYYYMMDD-HHMMSS.db` and keeps the newest 14 (two weeks of daily coverage). `PEC_DB`
and `PEC_BACKUP_DIR` override the locations; set them to match the server's environment.

## 5. Restore — and the one required rehearsal

Restore procedure (also printed by the tool):

1. Stop the server.
2. `node tools/backup.ts restore pec-YYYYMMDD-HHMMSS.db` — the tool integrity-checks the backup
   first and moves the live database aside to `pec.db.pre-restore*`; nothing is destroyed.
3. Restart (`npm start`), verify, then keep or remove the `.pre-restore*` files.

**Pilot-readiness gate**: PEC-NFR-009 requires one tested restore *of the real pilot data* before
go-live. The automated round-trip runs in CI (`server/test/coverage-backup-restore.test.ts`) and in
the drill; rehearse once against the real database without touching the live file:

```bash
# after the first real import, take a backup, then restore it to a scratch path:
node tools/backup.ts
PEC_DB=/tmp/pilot-rehearse.db node tools/backup.ts restore backups/pec-<latest>.db
PEC_DB=/tmp/pilot-rehearse.db PEC_PORT=4899 npm start   # open :4899, spot-check registers, stop
```

Record the date of that rehearsal in STATUS before starting the pilot.

## 6. During the pilot

- **Weekly**: coordinator triage (§3 above); leads work the package cockpit; PM reviews Overview
  drill-downs; export the sponsor brief for the steering meeting (PEC-OV-006).
- **Metrics**: the §18.1 pilot targets are all derivable from registers and exports — snapshot
  them weekly (deliverables represented, % anchored, untriaged age, condition-chain completeness
  on issued revisions, overdue decisions).
- **Weekly planning (P2)**: the planner sets capacity, plans the week (work, checks, and approvals
  all load capacity — I-9), and commits it — the commit generates everyone's My Week
  (PEC-PLAN-007). Leads open the review pack from the package page (PEC-PKG-009).
- **Feedback drives tuning**: the PRD is explicitly pilot-driven. Log product feedback as intake
  items in the pilot project itself (quick type `action`, log `internal`) so nothing is lost, and
  fold the themes into STATUS "What's next" — capacity thresholds, digest content, and lookahead
  cells are the P2 surfaces most likely to need pilot calibration (ADR-013).
