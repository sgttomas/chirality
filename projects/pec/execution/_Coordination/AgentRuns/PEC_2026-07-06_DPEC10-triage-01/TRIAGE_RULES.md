# D-PEC-10 272-item triage run — batch rules (pre-registered)

> **Epistemic status: pre-registered triage rules.** Written and frozen BEFORE
> any disposition act of this run, per the run direction ("write down your
> batch rules first and apply them uniformly"). Facts only; no project-fact
> invention (F-PEC-2). The taxonomy is the rehearsal-01 taxonomy under the
> D-PEC-10 O-A riders (agent-act boundary: open-triage/disposition only;
> conversion may create the records a disposition names — never approval
> records; accept/apply/`force` are not part of this run and none arises).

## Corpus facts (verified against the live instance before ruling anything)

- 272 intake items, `INTK-0001..0272`, all `state=raised`, all
  `quick_type=action`, all `log=package`, project 1 (`26020`).
- Every `statement_verbatim` carries its source row id verbatim as a
  `[PKG-nn]` / `[PLAN-nnn]` prefix (the WF-9 audit-to-source key).
- Two source families:
  - **F-A discrete RAIL action rows** — `[PKG-61]..[PKG-134]`, 74 items
    (intake ids 1–56, 255–272): named actions/topics with a suggested owner
    and a specific need-by.
  - **F-B monthly level-of-effort plan rows** — `[PKG-135]..[PKG-200]` +
    `[PLAN-067]..[PLAN-198]`, 198 items (intake ids 57–254): per-discipline
    month-scoped effort lines ("Support DBM updates", "3D model
    continuation", …), need-by = month-end, no anchor suggestion.
- Mechanical scans run before ruling (recorded in the manifest):
  - **Zero exact duplicates**: no two items share (statement remainder +
    suggested owner + need-by).
  - **Deliverable-title matches** (remainder equals an MDL title, or exactly
    one MDL title begins with the remainder, case-insensitive): intake 19 →
    deliverable 450 "Design Basis Memorandum" (exact); intake 23 →
    deliverable 435 "Control System Architecture - Includes PLC, DCS, etc."
    (unique prefix). Intake 32 and 45 match four deliverables each →
    ambiguous, no single anchor.

## Rules (applied in order; first match wins; uniform across all 272)

- **R0 — no invention (F-PEC-2).** New record content only from verbatim
  source fields (statement, suggested owner, need-by). No decision record is
  created in this run: a decision record requires a decision authority
  (`authority_id NOT NULL`) and no RAIL/plan source row names one — assigning
  an authority would invent a project fact. No `duplicate` disposition
  without an exact triple match (scan found zero). No `merged`, `rejected`,
  approval-record, hold, risk, or interface creation in this run.
- **R1 — left un-dispositioned for the owner** (listed with reasons; items
  stay `raised`) when any of:
  - (a) the statement poses an unresolved either/or or pros/cons choice
    ("vs", "pro's Con's") — decision-shaped, and the decision authority is
    not named in the source (ambiguous authority is the owner's class);
  - (b) a bare-topic row whose specific subject already appears in an
    existing imported decision record — whether the row duplicates that
    decision is the owner's sameness judgment;
  - (c) regulatory / contractual / third-party matters (permit filings,
    requesting another contractor's native files).
- **R2 — `converted` → work item** when the statement remainder resolves to
  exactly one MDL deliverable per the pre-run scan AND the source row names a
  suggested owner: work item titled with the verbatim statement, anchored to
  that deliverable, owner = suggested owner, need-by = source need-by,
  kind `action`, log carried from the item. Note references `[item_id]`
  verbatim. (Per scan: exactly intake 19 and intake 23.)
- **R3 — `parked` with grounds** for everything else:
  - **R3-B** all F-B rows: month-scoped level-of-effort plan lines; the
    intake conversion families (work item / hold / risk / decision /
    approval record / interface) do not include plan items, and no single
    deliverable anchor is resolvable from the row;
  - **R3-A** F-A rows with no resolvable single anchor (including near-miss
    or multi-subject or bare-topic rows — the note records the nearest MDL
    title or the sibling item as fact where one exists).
- Conservative ladder (run direction): unsure convert-vs-park → park;
  unsure park-vs-owner → owner.

## Planned outcome under these rules (execution must match or stop)

| Class | Count |
|---|---|
| `converted` → work item (R2) | 2 (intake 19, 23) |
| `converted` → decision | 0 (R0 — no source-named authority) |
| `duplicate` | 0 (R0 — no exact triple exists) |
| `parked` (R3) | 255 (198 F-B + 57 F-A) |
| left un-dispositioned for owner (R1) | 15 (intake 15, 27, 28, 29, 32, 36, 41, 46, 47, 259, 260, 262, 264, 265, 266) |
| **Total** | **272** |

## The 15 owner-left items and the one-line reason each

| Intake | Source | Reason |
|---|---|---|
| INTK-0015 | [PKG-77] | R1(c): requesting Vector's (third-party contractor) native FEED files — contractual/third-party judgment. |
| INTK-0027 | [PKG-91] | R1(a): "Electric vs heat medium for NGL Mole Sieve" — either/or decision; authority not named in source. |
| INTK-0028 | [PKG-92] | R1(b): "Piping Specs" — existing decision ref 6 "Pipe Specs"; sameness is the owner's call. |
| INTK-0029 | [PKG-93] | R1(b): "Standby Generator Load" — existing standby-power decision series refs 13–16. |
| INTK-0032 | [PKG-100] | R1(b): "Sales Gas" — existing decision ref 33 (sales booster); also 4-deliverable anchor ambiguity. |
| INTK-0036 | [PKG-106] | R1(b): "Pipeline risers" — existing decision ref 59 "Determine location and configuration of pipeline inlet risers". |
| INTK-0041 | [PKG-113] | R1(a): "Plot Plan and pro's Con's list" — options analysis; decision-shaped, authority not named. |
| INTK-0046 | [PKG-123] | R1(c): "Permit Amendments" — regulatory filing judgment. |
| INTK-0047 | [PKG-124] | R1(c): "New Permit Required" — regulatory filing judgment. |
| INTK-0259 | [PKG-95] | R1(b): "Piping specs usage and suitability" — existing decision ref 6 "Pipe Specs". |
| INTK-0260 | [PKG-97] | R1(b): "Storage Strategy" — existing storage-tank decisions refs 23/49. |
| INTK-0262 | [PKG-99] | R1(b): "Truck Loading" — existing decision ref 7 "02-25 Truckout location". |
| INTK-0264 | [PKG-102] | R1(b): "Hybrid Amine System" — existing decision ref 2 (hybrid MDEA/sulfinol). |
| INTK-0265 | [PKG-107] | R1(b): "Flare KOD Combination" — existing decision ref 58 (KODs / flare radiant zone). |
| INTK-0266 | [PKG-108] | R1(b): "02-25 Electrical to Truck Out" — existing decision ref 7 "02-25 Truckout location". |
