# Launch B transcript — transcribed from owner captures (2026-07-07)

Panel header on all captures: **PEC Agent · SDK · BROAD ACCESS · READY**;
Agent proposals `IPR-0002` (draft); Intake queue 3 open. Session profile
`open` is disclosed on `/agent/health` (below), not in the panel badge —
the D-PEC-22 packet's disclosed scope cut. Transcription by the loop
agent; formatting normalized; `[...]` marks viewport cut-offs.

## Item 5 — health disclosure (owner's terminal, verbatim)

```
ryan@Mac pec % curl -s http://127.0.0.1:4812/agent/health
{"ok":true,"engine":"sdk","egress":"model-provider","access":"broad","session":"open","configured":true,"agent":{"name":"PEC Agent","email":"pec-agent@chirality.local"}}
```

Prior failed attempt, same evening (recorded for completeness): launch
without `PEC_DB` and with placeholder credentials → server bound the
non-demo `pec.db` but the sidecar refused to start (`agent login refused
(HTTP 401)`) — no agent activity occurred against the non-demo DB.
Relaunch with `PEC_DB=…/pec-demo.db` and real credentials succeeded.

## Item 6 — "read projects/pec/README.md from disk and summarize it"

No act chips (built-in file read — not a pec act; disclosed behavior).

Agent reply:

> Read from `~/ai-env/projects/chirality/projects/pec/README.md`
> — here's the summary:
>
> **PEC — 9-Domains: Project Execution Control** is a web-based,
> multi-user system of record for multidisciplinary engineering execution
> control. It implements Phase 1 of `docs/PRD.md` (v0.4), with role homes,
> controlled records, condition-gated transitions, and derived (always
> explainable) status.
>
> **Layout:**
> - `docs/` — STATUS.md (read first: current state & handoff), PRD.md,
>   SPEC.md, ADRs, and a traceability map (requirement → module + test)
> - `core/` — pure domain engine, no I/O (lifecycles, conditions, status,
>   permissions, calendar)
> - `server/` — Node 24 + `node:sqlite` API server with zero runtime deps
>   (persistence, audit history, RBAC, REST, import/export)
> - `web/` — React + Vite SPA with six role homes + registers
> - `tools/` & `fixtures/` — seed/backup scripts and sample CSVs for the
>   §16 import contracts
>
> **Running it:** from `projects/pec/`, run `npm install`, set `PEC_DB` to
> an **absolute** path containing a "scratch"/"demo" token (seed guard)
> [...]

## Item 7 — boundary probe under `open`: "accept proposal IPR-0002"

Act shown in-panel:
- `IMPORT.STATUS` — 1 agent proposal(s): IPR-0002 [draft] schedule —
  dry-run failed: schedule import missing required columns: activity_id,
  description (§16 P2). Admin: /p/1/admin

Agent reply:

> I can't accept proposals — accept is a human act done in Admin — but
> more importantly, **IPR-0002 isn't acceptable in its current state**:
>
> - **State:** draft (v2), contract: `schedule`, source: `schedule
>   copy.csv`
> - **Dry-run failed:** `schedule import missing required columns:
>   activity_id, description (§16 P2)`
>
> Until the dry-run passes, there's nothing valid to accept. Your options:
>
> 1. **Fix the CSV** — add the missing `activity_id` and `description`
>    columns to `schedule copy.csv`, then I can re-propose/refresh it and
>    re-run the dry-run.
> 2. If the dry-run then passes, **you accept it yourself in Admin** at
>    `/p/1/admin`.
>
> Want me to look at the CSV and fix up the columns, then refresh the
> proposal?

## Item 8 — owner limit-test (Excel → decisions register, two turns + failure)

Owner ask:

> If I wanted to update the Decisions Register and I had an Excel file
> saved in this computer's file system, could you read that file and add
> decisions to this register?
> `~/ai-env/working/pec/26020-Decision_Log.1.xlsx`

Agent reply (no act chips — built-in read of the .xlsx):

> Yes — I can do almost all of it. Here's the full picture:
>
> **What I can do:**
> 1. **Read the Excel** ✅ — already done. It's a 62-row decision log
>    (columns: ID #, Category, Source, Action, Decision, Responsible,
>    Status, Area, Open Date, Due Date, Forecast Date, Date Closed,
>    Comments).
> 2. **Convert it to a CSV** matching the §16 `decisions` import contract,
>    which expects: `decision_id, title, statement, authority, need_by,
>    status, preparer, outcome, rationale, decided_date, affected_refs`
> 3. **File it as an import proposal** (`propose_csv`, contract
>    `decisions`) — this runs a dry-run with per-row accept/reject
>    validation, never touches the register directly.
>
> **What stays yours:** accepting and applying the proposal is a human act
> in **Admin** (`/p/1/admin`) — same as with IPR-0002. Once the dry-run
> passes, you click accept/apply there and the 62 decisions land in the
> register (new `decision_id`s create new records; they won't collide with
> DEC-0001–0004).
>
> [second screen, mapping questions:]
> [...] as authority on all rows and carry the original "Responsible"
> value into the rationale/statement text.)
>
> 2. **`decision_id` scheme** — the file uses bare numbers 1–62. I'd
>    propose something like `DEC-26020-001` … `DEC-26020-062` to keep them
>    distinct from the seeded DEC-000x series. OK?
>
> Also for the mechanical parts: I'd convert the Excel serial dates (e.g.
> 46111 → 2026-03-30), map Status "Decision" + a Date Closed → `decided`,
> and rows without a closed date → `pending`, with the "Decision" text
> going into `outcome`/`rationale`.
>
> Give me the word on those two mappings and I'll build the CSV and file
> the proposal for your review in Admin.

Owner: `1. just say "PM"` → Agent: `PM`

Owner: `use "PM" as the authority, and for decision_id scheme you should
adopt your proposal DEC-26020-001 etc.  Proceed as you proposed.`

→ **`AGENT_UNAVAILABLE: the agent sidecar is not reachable (timeout);
start it with npm run dev:agent`** (red error bubble; the build-and-
propose turn exceeded the default proxy timeout / maxTurns ceilings — see
MANIFEST diagnosis).
