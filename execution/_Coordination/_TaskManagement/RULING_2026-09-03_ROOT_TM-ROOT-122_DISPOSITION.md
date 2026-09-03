# Owner ruling — TM-ROOT-122 disposition (2026-09-03)

AccountableHuman: `Ryan Tufts`

RunID: `ROOT_NOTICE_INGESTION_2026-09-03`

Authority record:
`plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md`

Authority record SHA-256: recorded in Receipt 131 and in the PR that
published this ruling record — the files merged together (R11 precedent).

## Provenance

On 2026-09-03, in the HELP_HUMAN session chat, after PR #680 (App Electron
concordance: D-APP-98 Electron authority concordance, corpus v20, TM-ROOT-122
echo prepared under A11 E2) had been reviewed, HELP_HUMAN asked the owner:

> The Root echo for TM-ROOT-122 (a named G1 blocker) is READY_TO_ROUTE.
> Routing it onto Root's coordination surface and dispositioning the Root
> row are Root-loop acts under your authority. How far should I take it
> after 680 merges?

The accountable human ruled by selecting one option, recorded verbatim:

<!-- BEGIN R18 OWNER RULING VERBATIM -->
```text
  [click] "Route + Root TM disposition (Recommended)" — One Root tranche (fable subagent), recorded as R18: ingest the App notice onto Root's coordination surface citing the 680 merge commit, run Root's federation preflight, and apply your ruling that TM-ROOT-122 closes RESOLVED_BY_DECISION on the App disposition plus applied concordance; Root receipt; unmerged PR for your review. TM-ROOT-106 untouched.
  "Route only" — not selected.
  "Not yet" — not selected.
```
<!-- END R18 OWNER RULING VERBATIM -->

Session context of record: earlier in the same session the owner ruled A11
option E2 ("fix the App docs first, then echo";
`plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md`, SHA-256
`6197bae1aad25e6fd7dfa6befb0212acb5da24654f49f97536dbc2d365aeca27`).
PR #680 applied that concordance and was merged by the owner's direction as
`8140daec7ab7165f8972451dbdd3a67b8bb2fd38`. The owner also directed that
PR #678 (merge `13d845ef822a935296b25aa5e574eda0373b4729`) and PR #679
(merge `1537ddad1f9227dee1ba3233c0146694a779026a`) be merged earlier the
same day. Those merges are the App-side basis of the notice this ruling
consumes; they are cited, not re-ruled.

## Federation preflight

The invocation-local deterministic federation survey
(`python3 tools/taskmgmt/taskmgmt.py federation --register execution/_Coordination/_TaskManagement/REGISTER.csv`)
completed before any register write: `COMPLETE`, four canonical registers,
all live and archive registers valid, 79 typed relationship findings
presented, zero invalid or unreadable inputs, zero ambiguities, zero
register writes. Per-register counts at preflight:

| Register | OPEN | DEFERRED | ELEVATED | CLOSED (live) | Archived |
|---|---|---|---|---|---|
| PEC | 16 | 1 | 0 | 1 | 7 |
| ROOT | 11 | 8 | 0 | 0 | 108 |
| APP | 8 | 3 | 0 | 0 | 33 |
| PIP | 11 | 23 | 0 | 0 | 8 |

Typed finding counts: `FOREIGN_LINK_TO_LOCAL=49`, `LOCAL_LINK_TO_FOREIGN=2`,
`REMOTE_CLOSED_LOCAL_OPEN=2`, `LOCAL_CLOSED_REMOTE_OPEN=22`,
`MISSING_NOTICE=4`. One `REMOTE_CLOSED_LOCAL_OPEN` finding names
`TM-ROOT-122` ↔ `TM-APP-041` (the App row closed `RESOLVED_BY_DECISION` on
2026-08-19 against D-APP-98): this is the closure echo the owner's ruling
resolves. The findings remain observations only and create no cross-loop
effect; the projection under `.candidates/` is gitignored and never
authority.

## Nine-domain completeness scan

| Domain | TM-ROOT-122 |
|---|---|
| Action Item | Electron authority drift (PI082-F09): D-APP-72 named `43.1.1` while the executable manifest pinned `43.2.0`, carried by no instrument in either loop. Exactly the live row. |
| Assignment | Root TASK_MANAGEMENT records the ruled disposition; the App loop owns the manifest and its own register; the accountable human is Ryan Tufts. No agent is accountable. |
| Prioritization | Row priority `LOW` is historical; the owner selected the disposition in this tranche. No priority is inferred. |
| Deliverables | Resolution landed in App surfaces: D-APP-98 and the PR #680 document concordance (nine governed App docs; authority corpus v20). Nothing lands in the Root register but the disposition and evidence. |
| Work | Ingest the App echo notice onto the Root surface (N1); record the exact closed-row fields and relocate mechanically (N2); publish the R18 pair (N3). |
| Planning | Root's 2026-08-03 notice named the closure condition — "closes on that App disposition" — and the App echo now supplies it with a final merge identity. G1 remains a separate owner gate. |
| Approval | The R18 owner act above is the sole disposition authority. A11 E2 and the PR #680 merge are App-side owner acts, cited as evidence. |
| Checking | Contract-drift check of every factual claim in the App notice against live bytes at the basis (`CONTRACT_DRIFT_CHECK.md`, verdict `NO_EXACT_DIVERGENCE`); register validate/archive/validate; final federation pass. |
| Decisions | `RESOLVED_BY_DECISION`, citing D-APP-98 (App decision) with the ingested Root notice and the PR #680 merge commit as the applied-concordance identity. `ScaRef` remains `NONE`. |

## Exact application

| Row | Closed disposition | Exact evidence |
|---|---|---|
| `TM-ROOT-122` | `CLOSED / RESOLVED_BY_DECISION`; `LastReviewed=Closed=2026-09-03`; `ScaRef` remains `NONE` | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-98_RULING_ELECTRON_AUTHORITY_2026-08-17.md`, SHA-256 `71dfc1ae6369acea1e49f71d68e45aaf9da8f14c5f6a77733845c43f3ee7c020`; `execution/_Coordination/NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`, SHA-256 `d7eb52af3fd3833b6af949e218c6c90b7566a751c90331fa643a1cc86bc40d78`; PR #680 merge commit `8140daec7ab7165f8972451dbdd3a67b8bb2fd38` |

Fields changed on the row, and nothing else: `Status` (`OPEN` → `CLOSED`),
`Disposition` (`` → `RESOLVED_BY_DECISION`), `EvidenceRef`, `EvidenceSha`,
`EvidenceQuote` (exact D-APP-98 sentence: "Electron `43.2.0`, as pinned in
`frontend/package.json` on `main`, is the App's recorded Electron authority
and the D-APP-72 successor for that single fact."), `LastReviewed`
(`2026-08-03` → `2026-09-03`), `Closed` (`` → `2026-09-03`), and one
appended dated `Notes` entry citing R18, the applied concordance (corpus
v20, PR #680 merge), and the statement that G1 itself is not passed by this
closure.

Row identities (SHA-256 of the complete newline-terminated CSV row):

| Image | Bytes | SHA-256 |
|---|---|---|
| `TM-ROOT-122` pre-image (live `REGISTER.csv` at basis) | 1118 | `6816c29c7b7414e66ff262b249f47bcab3cdcbca8cfb23480fb9ae39ba50c399` |
| `TM-ROOT-122` post-image (live, before archive; identical bytes after relocation to `REGISTER_CLOSED.csv`) | 2506 | `82034f7f36206679394eb89c2adc6d27b4d33822f39576e000e4a9274e2608b4` |
| `TM-ROOT-106` (unchanged; identical before and after) | 2235 | `8c917730f4638366a4ced323170542db28089d35a182ef84ff8b9dc808ec8686` |

The closed row was relocated from `REGISTER.csv` to `REGISTER_CLOSED.csv`
only through `tools/taskmgmt/taskmgmt.py archive` (1 row moved). Register
file identities:

| File | Pre-image SHA-256 (basis) | Post-image SHA-256 |
|---|---|---|
| `REGISTER.csv` | `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 rows: `OPEN=11`, `DEFERRED=8`) | `fb7ef7d816d348fa55fee596fbe1a427b745dad7c9b787180d2a9e677e3627af` (18 rows: `OPEN=10`, `DEFERRED=8`) |
| `REGISTER_CLOSED.csv` | `c8a58b08a30dea35fc361d08fec81e405fa08d40f04604709a6dd9b806e45e1c` (108 rows) | `995d7ffd46008e1f8a8e471105e799a89830ced97ff0a98b12b2f7b563692fbc` (109 rows) |

Both registers validate (`taskmgmt validate` PASS, 18 and 109 rows). The
final federation pass after relocation is `COMPLETE` over the same four
registers with zero register writes: ROOT `OPEN=10 DEFERRED=8` / 109
archived; 78 findings presented; `REMOTE_CLOSED_LOCAL_OPEN` fell from 2 to
1 (the `TM-ROOT-122` ↔ `TM-APP-041` echo is resolved); every other typed
count is unchanged.

A transcription slip in the first attempt at `EvidenceSha` (one character of
the D-APP-98 hash) was caught by the pre-archive recomputation assertion
before any archive or validation ran, and the field was rewritten from the
recomputed value. The corrected row above is the only row image that was
archived; no partially correct row reached `REGISTER_CLOSED.csv`.

## Effect boundary

`TM-ROOT-106` is untouched and unruled. Every other Root row is unchanged.
This ruling record and the register disposition do not pass G1; do not
change any Electron pin, lockfile, supply script, product source, or
decision record; do not lift any of the ten held DEL-02-06 bindings; and do
not grant any lifecycle, implementation, supply, release, publication,
signing, notarization, reliance, or App-surface act. The Root loop wrote no
App path. The register row records the human decision; it is not itself
authority for any cited external surface (K-TM-5).
