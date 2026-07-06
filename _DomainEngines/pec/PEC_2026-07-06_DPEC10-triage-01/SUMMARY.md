# D-PEC-10 272-item intake triage — readable summary

> **Epistemic status: immutable evidence snapshot** (D-T0-13). Facts only; no
> pilot-readiness, correctness, or go-live claim (F-PEC-2). Dispositions are
> scratch-basis evidence on the owner's standing pilot-scratch instance — no
> real-record durability claim (D-PEC-10 Scope note 4).

## Outcome at a glance

| Class | Count | Notes |
|---|---|---|
| Total intake items | **272** | INTK-0001..0272, all `raised` pre-run |
| `converted` → work item | **2** | INTK-0019 → WI-0001 (anchored to MDL deliverable 450 "Design Basis Memorandum"); INTK-0023 → WI-0002 (anchored to MDL deliverable 435 "Control System Architecture - Includes PLC, DCS, etc.") |
| `converted` → decision | **0** | Rule R0: a decision record requires a decision authority; no RAIL/plan source row names one — assigning one would invent a project fact (F-PEC-2). Decision-shaped items are in the owner-left list instead. |
| `duplicate` | **0** | Rule R0: the pre-run scan found zero exact triples (statement remainder + suggested owner + need-by). Same-text pairs with differing dates/owners are parked with a factual cross-reference note, never collapsed. |
| `parked` (with grounds) | **255** | 198 monthly level-of-effort plan rows (`[PKG-135]..[PKG-200]`, `[PLAN-067]..[PLAN-198]`) — intake conversion cannot create plan items; 57 discrete RAIL rows with no resolvable single anchor. |
| Left un-dispositioned for the owner | **15** | Reasons below; items remain `raised`. |

Every disposition note carries the source `[item_id]` verbatim (WF-9
audit-to-source). Every act of the run — 257 `open_triage` transitions, 257
dispositions, 2 record creations (history rows 2484–2999, 516 rows) — is
attributed to the agent person (personId 46, `is_admin=0`, coordinator); no
other actor acted during the run window.

## The 15 items left for the owner (each with its one-line reason)

| Intake | Source | Statement (remainder) | Reason |
|---|---|---|---|
| INTK-0015 | [PKG-77] | MLE to dicsuss reaching out to Vector for the native files and information on FEED | Third-party contractor's files — contractual judgment (R1c). |
| INTK-0027 | [PKG-91] | Electric vs heat medium for NGL Mole Sieve | Either/or decision; authority not named in source (R1a). |
| INTK-0028 | [PKG-92] | Piping Specs | Existing decision ref 6 "Pipe Specs" shares the subject; sameness is the owner's call (R1b). |
| INTK-0029 | [PKG-93] | Standby Generator Load | Existing standby-power decision series refs 13–16 (R1b). |
| INTK-0032 | [PKG-100] | Sales Gas | Existing decision ref 33 (sales booster); anchor also ambiguous — 4 MDL matches (R1b). |
| INTK-0036 | [PKG-106] | Pipeline risers | Existing decision ref 59 "Determine location and configuration of pipeline inlet risers" (R1b). |
| INTK-0041 | [PKG-113] | Plot Plan and pro's Con's list. | Pros/cons options analysis; decision-shaped, authority not named (R1a). |
| INTK-0046 | [PKG-123] | Permit Amendments | Regulatory filing judgment (R1c). |
| INTK-0047 | [PKG-124] | New Permit Required | Regulatory filing judgment (R1c). |
| INTK-0259 | [PKG-95] | Piping specs usage and suitability | Existing decision ref 6 "Pipe Specs" (R1b). |
| INTK-0260 | [PKG-97] | Storage Strategy | Existing storage-tank decisions refs 23/49 (R1b). |
| INTK-0262 | [PKG-99] | Truck Loading | Existing decision ref 7 "02-25 Truckout location" (R1b). |
| INTK-0264 | [PKG-102] | Hybrid Amine System | Existing decision ref 2 (hybrid MDEA/sulfinol) (R1b). |
| INTK-0265 | [PKG-107] | Flare KOD Combination | Existing decision ref 58 (KODs / flare radiant zone) (R1b). |
| INTK-0266 | [PKG-108] | 02-25 Electrical to Truck Out | Existing decision ref 7 "02-25 Truckout location" (R1b). |

## Observations recorded as fact (candidate register-row material, not prose fixes)

1. **The 198-item monthly plan block dominates the queue.** These rows are
   month-scoped level-of-effort lines per discipline; the intake conversion
   families (work item / hold / risk / decision / approval record /
   interface) offer no plan-item target, so they park. If the owner wants
   them landing as plan items, that is a conversion-family or import-path
   design question (its own register row), not a triage judgment.
2. **Decision conversion needs an authority the sources never carry.** The
   imported decisions register has real per-row authorities; RAIL rows do
   not. Until a source document or owner convention names decision
   authorities, converted→decision cannot be executed without invention, so
   decision-shaped RAIL rows will keep landing in the owner-left class.
3. **Near-miss anchors are common.** Several RAIL rows name deliverables in
   close-but-not-exact words ("Major Equipment List Mechanical" vs MDL
   "Mechanical Equipment List"). An owner-ruled alias/mapping convention
   would convert more of these without judgment risk.
4. **Same-text pairs with different dates/owners exist in the RAIL source**
   (e.g. [PKG-64]/[PKG-72] "Project Execution Plan"; [PKG-68]/[PKG-79]
   "Value Engineering Sessions"). Left un-collapsed; the parked notes
   cross-reference the siblings factually.
