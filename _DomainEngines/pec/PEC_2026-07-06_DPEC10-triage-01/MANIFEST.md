# PEC D-PEC-10 triage 01 — the 272-item real-data intake triage run

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, or go-live claim
> (F-PEC-2). Dispositions here are scratch-basis evidence on the owner's
> designated standing pilot-scratch instance — no real-record durability
> claim (D-PEC-10 Scope note 4 / Receipt 26 "Another time").

## Basis (authority chain, each verified in the live tree before acting)

- **Mechanism:** D-PEC-10 O-A, owner-ruled 2026-07-05 (packet
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-10_agent_intake_triage.md`;
  ruling SHA `9dd310cc3`). The agent's ruled act is intake
  open-triage/disposition under its own provisioned person; the agent-act
  boundary riders bind this run (no approval records via conversion; no
  accept/apply/`force`; items the agent cannot ground are left for the owner).
- **Visibility basis:** D-T0-20 O-B, owner-ruled 2026-07-06 (enumerated OPEN
  surface (i)–(iv) under the agent person's RBAC, `is_admin=0`). The ruling
  text explicitly "discharges the D-PEC-10 Scope-note-4 visibility
  confirmation for the 272-item run" and clarifies "the pilot-scratch
  instance is within the scratch/demo mutation basis, so the 272-item triage
  run may proceed on it."
- **Gate outcome of record:** Receipt 32 ("the 272-item run on pilot-scratch
  is owner-clarified lawful (scratch/demo mutation basis)"); rehearsal
  precedent Receipt 30 + `PEC_2026-07-05_DPEC10-rehearsal-01/` (actor model,
  taxonomy, WF-9 convention, basis-prep-as-instance-setup).
- **Capture basis:** D-PEC-01 owner inputs of record (2026-07-05):
  "run-generated exports and reports may be committed unredacted"; capture
  limits beyond hashes/counts "none". This run's data is the same D-PEC-01
  source (the imported RAIL/plan rows) — no materially new data source.
- **Instance:** the owner's standing scratch instance
  `projects/pec/pilot-scratch/db/pec-scratch-import.db` (untracked), served
  by this run on `127.0.0.1:4899` only. The owner's dev server on `:4811`
  was live and untouched (verified holding no DB file open before backup).
  **DB retained after the run** — it is the owner's designated standing
  scratch instance (not deleted; unlike the rehearsal's throwaway DB).
- **Code:** `main` at `c0a3214cf` (no pec source change; no tracked file
  edited by this run — evidence files here are new).

## Actors (WF-8)

- **Agent:** `pec-agent@rehearsal.demo` (personId 46, name "PEC
  intake-triage agent (D-PEC-10)", `is_admin=0`, `coordinator` on project 1)
  — every act of the run: login, enumeration, 257 open-triage transitions,
  257 dispositions, 2 work-item creations via conversion, exports, logout.
  All through the live HTTP API; nothing bypassed RBAC.
- **Basis-prep vs act split (rehearsal-01 precedent):** the agent person did
  NOT exist in this instance (verified: no `pec-agent@*` row; pre-existing
  roles none). Provisioning (person insert with ephemeral scrypt password +
  coordinator grant on project 1) ran script-side as instance setup before
  the server started, not as a workflow act. Teardown after the run
  (script-side, disclosed): the ephemeral password hash was overwritten with
  a non-verifiable value and the (already-logged-out) session table checked
  — 0 rows remained. The person row and role grant remain in the standing
  instance so history attribution stays resolvable.
- **No human act occurred in this run.** No accept, no apply, no `force`
  (none arose — this run is triage-only; imports/proposals were out of
  scope and none was created). `is_admin` was never used. No LLM sidecar:
  the run used the rehearsal-01 direct-API mechanism; the triage judgment is
  the loop agent itself (no LLM API key sourced or fabricated).

## What happened

1. Preflight: `:4899` free; owner dev server on `:4811` noted live,
   untouched; no process held the scratch DB (lsof).
2. Pre-run backup (quiescent): db + wal + shm copied byte-identical to
   `pilot-scratch/backups/pre-triage-20260706/` (hashes below).
3. Basis-prep (script-side): agent person provisioned as above.
4. Server started on `PEC_PORT=4899` with `PEC_DB` = the pilot-scratch DB.
5. Agent login; full pre-triage enumeration as the agent: 272 items, all
   `raised`, exported before any disposition (`artifacts/01-…`).
6. Batch rules frozen BEFORE any disposition (`TRIAGE_RULES.md`), with two
   mechanical pre-run scans (zero exact duplicates; deliverable-title
   resolution finding exactly two single-anchor matches).
7. Triage in 11 batches of ≤25 (raw responses in `artifacts/batch-logs/`):
   255 `parked` with grounds, 2 `converted` → work items (WI-0001, WI-0002),
   15 left un-dispositioned for the owner. Zero plan-vs-actual mismatches.
   Every note carries the source `[item_id]` verbatim (WF-9).
8. Post-triage captures as the agent: raised queue (the 15 owner items),
   dispositioned queue (257), intake + rail register CSV exports, per-record
   history samples.
9. Logout; clean server shutdown (WAL checkpointed on close); teardown;
   post-run backup to `pilot-scratch/backups/post-triage-20260706/`.
10. History extract from the post-run copy: rows 2484–2999 (516 = 257
    transitions + 257 dispositions + 2 creations), **all actorId 46**; the
    prior watermark (2483) and the original import acts (actorId 1, the
    owner's D-PEC-01 basis) sit below it — the actor split is total.

## Counts (also `artifacts/10-counts.json`)

| Class | Count |
|---|---|
| total | 272 |
| converted → work item | 2 |
| converted → decision | 0 (no source-named authority — R0/F-PEC-2; see SUMMARY.md) |
| duplicate / merged / rejected | 0 |
| parked | 255 |
| left un-dispositioned for owner | 15 (INTK-0015, 0027, 0028, 0029, 0032, 0036, 0041, 0046, 0047, 0259, 0260, 0262, 0264, 0265, 0266 — one-line reasons in SUMMARY.md and TRIAGE_RULES.md) |

## Backups (SHA-256; byte-identical copies verified at capture)

Pre-run (`pilot-scratch/backups/pre-triage-20260706/`):

```
84350fdf37e3e3a19618bd446d2468e58012762f0400b29b91472ee50faad341  pec-scratch-import.db
8412ecf403188626d5b8f738b42387f4b34835840d00565933eb6e84b0ad190b  pec-scratch-import.db-wal
cfd13e9f2d489829366d93aa588b3c80b7950b3e323ad05b2546b3c2dd0b40e1  pec-scratch-import.db-shm
```

Post-run (`pilot-scratch/backups/post-triage-20260706/`; the server
checkpointed the WAL on clean close, so the post-run state is the single db
file):

```
94dc7a47206e22ac214a4835474aa28d980a10372718ab8f1e87126feff88ab9  pec-scratch-import.db
```

## Boundaries respected / disclosures

- Scratch/demo mutation basis only; the mutated DB is the owner-designated
  standing pilot-scratch instance, **retained** (not deleted) per its
  standing role; pre/post backups above. No other DB touched; the owner's
  `:4811` server untouched; `pec.db` / `pec-demo.db` / restore DBs untouched.
- **No accept or apply act occurred** (none arose; the run is triage-only —
  no import proposal was created). **`force` was never set by anyone.**
  `is_admin` never used. Conversion created work items only — never
  approval records (rider honored).
- No pec source change; no tracked file edited; no git commit/branch/push by
  this run; no tier-0 act; no register/receipt/profile write.
- **Schema auto-migration disclosed:** starting the server against the
  standing scratch DB auto-migrated its schema — `sqlite_master` diff vs the
  pre-run backup shows exactly one added table, `import_proposal` (created
  empty; 0 rows before, during, and after the run). The pre-run backup
  preserves the pre-migration schema. Row-level boundary claims are
  unaffected; this line records that the run altered the standing instance's
  schema, not just its rows (scratch mutation basis — lawful).
- No record-state invention: every state change through the RBAC'd API as
  personId 46 (F-PEC-2); new record content traces verbatim to source rows.
- Visibility stayed inside the D-T0-20 O-B enumeration (intake items and
  their dispositions; register exports; owner-dropped-file lineage); no
  external egress; instance content resides in this evidence dir per
  D-T0-14/D-T0-20 residency.
- **Read path for the pre-run scans and rule grounding (disclosed):** the two
  mechanical pre-run scans (duplicate-triple; deliverable-title resolution),
  the R1(b) existing-decision cross-references, and the post-run history
  extract (`artifacts/09-history-extract-run.csv`) were direct **read-only
  sqlite** queries run against byte-identical scratchpad copies of the
  scratch DB — the pre-run copy taken after the pre-run backup, BEFORE
  server start and BEFORE agent login; the post-run copy taken from the
  post-run backup after shutdown — never against the live DB file and never
  via `is_admin`; the content classes read (intake items and dispositions;
  MDL deliverable titles; decisions-register rows; run-window history; cast
  rows for script-side basis-prep verification) sit inside the D-T0-20 O-B
  enumeration ((i) intake items and their dispositions; (iii)
  register-export content classes; (iv) owner-dropped weekly-file content)
  on the scratch basis, with raw-view over these rows granted by the
  D-PEC-01 owner basis; all workflow acts and all authoritative captures
  went through the live HTTP API as the agent person.
- **Live-LLM sidecar not used** — direct API as the agent person
  (rehearsal-01 mechanism); no LLM API key sourced, hardcoded, or
  fabricated.
- Deltas found (live tree wins, recorded): (1) the run tasking said the
  admin bootstrap user is `admin@aurora.dev` per prior evidence — that was
  the rehearsal's seeded cast; this instance's admin is `ryan@chirality.ai`
  (personId 1, D-PEC-01 basis). No admin credential was needed or used:
  provisioning ran script-side per the rehearsal-01 basis-prep precedent.
  (2) `pilot-scratch/db/pec-scratch-import.db-shm` bore a same-day mtime at
  preflight while no process held the DB (lsof empty) — backed up as-is,
  byte-identical.

## Artifacts (SHA-256 in `SHA256SUMS`)

- `TRIAGE_RULES.md` — pre-registered batch rules + planned outcome (frozen
  before any disposition).
- `DISPOSITIONS.csv` — per-item table: intake id, ref, source `[item_id]`,
  disposition (or LEFT-FOR-OWNER), target records, grounds note.
- `SUMMARY.md` — readable outcome, the 15 owner-left reasons, observations.
- `artifacts/00-agent-login.json` — agent session (personId 46, no token).
- `artifacts/01-intake-pre-triage.json` — full 272-item export BEFORE any
  disposition, captured via the API as the agent.
- `artifacts/02-disposition-plan.csv` — the mechanical plan derived from the
  frozen rules (execution matched it 272/272).
- `artifacts/batch-logs/batch-01..11.jsonl` — raw open-triage + disposition
  API responses for all 257 acts.
- `artifacts/03-intk0019-converted.json`, `artifacts/04-intk0023-converted.json`
  — the two conversions (created WI-0001 / WI-0002).
- `artifacts/05-intake-post-raised-owner-left.json` — the 15 items left.
- `artifacts/06-intake-post-dispositioned.json` — the 257 dispositioned.
- `artifacts/07-export-intake.csv`, `artifacts/07-export-rail.csv` — §16
  register exports as the agent, post-triage.
- `artifacts/07-export-work-items.csv` — zero-byte capture (the work-items
  export returned empty on this instance's export shape); retained as-is and
  hash-pinned. The two created work items are visible in
  `07-export-rail.csv` rows 1–2, so no data is missing from the pack.
- `artifacts/08-hist-*.json` — per-record history extracts (converted items,
  created work items, parked and owner-left samples).
- `artifacts/09-history-extract-run.csv` — every history row of the run
  window (2484–2999): the WF-8 actor split in full.
- `artifacts/10-counts.json` — counts by disposition class.
- `artifacts/11-server-log.txt` — server log (startup line; the server logs
  no per-request lines).
