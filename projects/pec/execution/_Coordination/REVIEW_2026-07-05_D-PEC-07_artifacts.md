# Adversarial review — D-PEC-07 artifacts (packet, file-drop runbook, upload-agent brief)

> **Epistemic status: agent-authored review report — not authority.** Prepared
> 2026-07-05 at owner direction under the PEC work loop
> (`_DomainEngines/pec/WORKPLAN_2026-07-04_pec_loop.md`). Modeled on the
> archive's adversarial-citation-review convention (workplan step 4) and the
> decision-packet precedent of D-PEC-01..07. This report changes nothing:
> every fix below is a **candidate awaiting owner ruling** (K-AUTH-1;
> D-GOV-04). The ruled D-PEC-07 packet has NOT been amended.

**Reviewed at:** `main` `41744fe6d` (clean). **Artifacts under review** (Receipts 19–20):

- PACKET — `_DECISIONS/D-PEC-07_embedded_upload_agent_pathway.md` (RULED O-C)
- RUNBOOK — `IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md`
- BRIEF — `_DomainEngines/proposals/pec/BRIEF_2026-07-05_embedded_upload_agent_design.md` (CANDIDATE)

**Method / provenance.** Two independent passes, merged: (1) this loop's
multi-agent review — 7 independent finders (4 citation verifiers, 3 design
challengers), 52 candidate findings, every finding then adversarially
verified by two further agents (source-fidelity + governance-materiality
lenses), splits adjudicated against the live tree; (2) a second independent
agent assessment supplied by the owner, whose novel factual claims were each
re-verified against the live tree before inclusion (`http.ts`, `ADR.md`,
`SPEC.md`, `coord-check` runs all confirmed). Findings that failed
verification are listed in §4, not silently dropped. Provenance tags:
[P1] = pass 1, [P2] = pass 2, [both].

## 1. Verified clean (load-bearing checks that passed)

- Owner ruling and direction quotes are **verbatim-identical** across the
  packet, runbook epigraph, Receipt 19/20, and register row.
- Register provenance clean: `1a9e4071c` introduced ruling + runbook + brief;
  the `d0ec6c6f4` SHA backfill matches the sibling bare-SHA convention
  (D-PEC-01/04/05/06); merged via PR #79.
- Evidence numbers match the manifests (MDL 457/457 idempotent; RAIL 254/272
  intake; decisions 52/62 — evidence-03-era, superseded same day by
  evidence-04, correctly presented as dated facts).
- `api.ts:316` route/`config.manage` citation current; D-PEC-05 precondition
  wording ("until after D-PEC-01 pilot evidence is captured") supports the
  packet's precondition-met claim; `force=true` posture matches
  `pec.yaml:118`; pilot-scratch gitignore and the raw-files-uncommitted
  attribution both trace to the recorded 2026-07-05 owner basis.

## 2. Confirmed findings

Severity: **major** = false cited fact, misstated ruling, or gate-weakening
rule needing a fix; **minor** = imprecision/staleness worth fixing; **note** =
design consideration for the adoption/tranche gate. (Second-pass P1/P2/P3
roughly map to major/minor–major/minor.)

### 2.1 Ruled packet (fixes only by owner-ruled corrigendum — S-1)

| ID | Sev | Finding | Sources |
|---|---|---|---|
| RV-1 | major | "there is no file-upload UI … in the app today" (Verified-facts row) is **false**: the Admin page ships a routed CSV file-picker (`web/src/pages/Admin.tsx:108-109`, route `/p/:pid/admin`) posting to the very import route the row cites. Genuinely absent: a multipart upload *endpoint*, server-side file storage, an agent surface. Could mislead the brief-adoption ruling. [P1] | packet:32; Admin.tsx:108-109; main.tsx:182 |
| RV-2 | major | "D-T0-13 O-A staging (**L3 is the destination**…)" misstates the ruled staging: O-A ruled **L2 as destination, L3 future-only** until PEC exposes a proposal-shaped API. L3-as-destination was that packet's *unruled* O-C. [P1] | packet:19-20; D-T0-13:27 |
| RV-3 | minor | Header `Status: AWAITING_RULING` contradicts the filled Human-ruling section and the RULED register row; packet also lacks the sibling-convention in-packet `**Ruling SHA:**` line (where this archive keeps backfill provenance). [both] | packet:3,61; \_REGISTER.md:28; D-PEC-06:7 |
| RV-4 | minor | Lifecycle parenthetical omits `rejected` — profile is 5-state; the brief quotes it correctly, so packet and brief disagree. [P1] | packet:24; pec.yaml:130 |
| RV-5 | minor (contested) | F-PEC-1 glossed as "no pec source writes without a tranche authorization" — the fence is absolute (and also bars non-scratch DB runs); one verifier panel held this, one refuted it as a precedented compressed pointer. Owner's judgment. [P1] | packet:22; WORKPLAN:110-115; D-T0-15:31 |
| RV-6 | minor | `coord-check` REVIEW finding `COORD_PRECEDENT_NOT_NAMED` (K-INVENT-1): the packet names no precedent/pattern/skeleton for its structure. Confirmed by re-running `coord-check --diff` on both introducing ranges. [P2, verified] | cmd_coord_check.py:214-220 |

### 2.2 Runbook (coordination surface — amendable on ruling — S-2)

| ID | Sev | Finding | Sources |
|---|---|---|---|
| RV-7 | major | **Approval shortcut inverts the ruled sequence.** Ruled: "agent maps → proposed import → user approves import" — approval *after* the Step-3 proposal (counts, deltas, fills, reject/intake profile). Step 4's "A drop message that already says 'proceed'/'import it' is that approval" lets approval precede the proposal, collapsing the gate `requires_human_confirmation` holds. Both verifier lenses confirmed. [both] | runbook:20-22; packet:63-64; pec.yaml:117 |
| RV-8 | major | **Unevidenced idempotency stated as fact:** "MDL/decisions/**risks/schedule** re-imports are idempotent … safe to re-run whole." Only MDL (evidence-02) and decisions (evidence-04) were ever re-imported. **No risks import has ever succeeded** (evidence-01 holds only as-is reject payloads; risk-log population is still parked owner-side); schedule was imported once, never re-imported. Code-implied ≠ evidenced. [P1] | runbook:35-36; evidence-01 MANIFEST:108; evidence-04 MANIFEST |
| RV-9 | minor | "(later: pilot) `PEC_DB`" forward-writes an import basis no ruling grants (F-PEC-1 bars mutating non-scratch DBs; D-PEC-01 was scratch-only). Hedged/future-tense, but a standing doc is the wrong home for unruled forward authority. [P1] | runbook:23-24; WORKPLAN:114-115 |
| RV-10 | minor | The export-and-compare verification practiced in every evidence run is not captured as a runbook rule. [P1] | runbook:23-26; evidence-02 MANIFEST |
| RV-11 | minor | Capture-basis pointer missing: the committable-capture rule rides the 2026-07-05 owner basis (raw-view + unredacted-commit, `OWNER_INPUTS.md:36-37`). A materially new data source should get fresh owner confirmation of capture limits before its exports/reports are committed (D-T0-14 stays CLOSED; D-PEC-01's limits were owner-enumerated). The stronger "pathway is unlawfully broad" form was **refuted** — the basis was supplied as standing and the O-C ruling formalizes repetition — but the pointer is warranted. [P2, moderated] | runbook:37-38; D-PEC-01:60-62; D-T0-14:27 |

### 2.3 Brief (pre-adoption amendments — S-3)

| ID | Sev | Finding | Sources |
|---|---|---|---|
| RV-12 | major | **LLM-mapper clause carries no residency caveat.** "an LLM-backed mapper slots in … later" routes real instance content to an external model — egress, CLOSED under D-T0-14 and barred by F-PEC-3 absent a fresh ruling. The brief authorizes nothing, but adopting it as-is bakes in drop-in language with no flag. One sentence fixes it. [P1] | brief:27-30; D-T0-14:54-57; WORKPLAN:120-123 |
| RV-13 | major | **Profile-contract obligations absent:** `accepted_or_applied_requires` mandates "human approval bound to git SHA per K-AUTH-2" + "engine-controlled apply through PEC's RBAC API with append-only history/audit evidence." Brief defines neither; nothing binds the accepted proposal to the *mapped CSV's* hash (only the raw upload's), no proposal-version binding, no stale-proposal refusal semantics. [both, merged] | pec.yaml:133-135; brief:20-26,31-33 |
| RV-14 | minor | "spreadsheet/CSV upload" implies an in-app xlsx parser (zip container) and multipart handling — new runtime deps ADR-002/F-PEC-3 forbid; live body handling is UTF-8 text, 25 MiB cap (`readBody`). State v1 = CSV-only text body (conversion stays agent/client-side) or seek a dependency ruling. [both] | brief:18-19; ADR.md:16-22; http.ts:69 |
| RV-15 | minor | "history/audit like §16 imports today" is imprecise: imports write `history_entry` `kind='import'` only; `audit_event` is written additionally for approval outcome, issue event, waiver, permission/config change — not imports. Brief must choose history-only or specify new audit events for proposal/accept/apply. [P2 + P1-note] | brief:35; import/index.ts:69-74; SPEC.md:100-101 |
| RV-16 | minor | RBAC under-specified: upload gets `config.manage` (admin-only, `permissions.ts:217-218`); accept/apply is only "an RBAC'd in-app act" — unnamed. Brief should state who may upload / map / accept / apply / set `force` / read stored raw files+previews, and whether acceptance is admin work or a project-authority act. (A mandatory separation-of-duties claim was **refuted** — no such obligation exists in the governing archive.) [both, moderated] | brief:18,31-33; permissions.ts:217-218; api.ts:317 |
| RV-17 | minor | Dry-run/apply deterministic contract undefined: profile result schemas are `TBD` (`pec.yaml:112-113,132`; open issue `:159`); preview-stability of refs/sequence values (rolled-back tx still consumes seq/rowids); stale-dry-run detection between accept and apply (`lastChangeIsImport` reads live state); lifecycle has no failed/error terminal for a mid-apply throw. → name these as explicit tranche-packet obligations. [both, merged] | brief:24-26,31-33; pec.yaml:130-132; import/index.ts:62-67; db.ts:626-636 |
| RV-18 | minor | "Multi-file schedule support" mischaracterizes evidence-04: one owner-dropped `schedule.csv`, imported 127/127 through the existing seam with **no code change** — arguably not a "prerequisite repair" at all. Dry-run report field list also omits `intakeCreated`, the dominant RAIL outcome (238/254, then 272/272). [P1] | brief:24-25,42-44; evidence-04 MANIFEST:13-15,30 |
| RV-19 | minor | Upload-store lifecycle unspecified: an "outside the DB" store sits outside the only proven backup path (`VACUUM INTO` of the single DB file; restore is `copyFileSync`) — accepted-proposal source files can be lost on restore while the DB record survives. Retention/deletion, MIME/extension policy, project scoping (`:pid`), and read-side RBAC (register reads gate on membership only) all unstated. [both] | brief:18-19; tools/backup.ts:81,118; api.ts:41-50 |
| RV-20 | minor | `coord-check` `COORD_PRECEDENT_NOT_NAMED` also fires on the brief (see RV-6). [P2, verified] | cmd_coord_check.py:214-220 |
| RV-21 | note | CSRF posture: server's only cross-site defense is a SameSite=Lax HttpOnly cookie (no tokens, no Origin check); a browser upload route inherits this. Tranche-packet obligation. [P1] | server/src/auth.ts; brief:18 |

### 2.4 Register / coordination hygiene (S-4, S-5)

| ID | Sev | Finding | Sources |
|---|---|---|---|
| RV-22 | minor | `IMPORT_MAPPING.md` is stale for the two contracts D-PEC-07 newly exercised: the schedule section still says "`schedule.pdf` — not importable; contract is CSV/XER-derived" though `schedule.csv` is now the proven path (evidence-04, `SCH-{id}` mapping) — and runbook Step 2 tells the agent to map *per this doc*. Risks section likewise pre-population placeholder. [both] | IMPORT_MAPPING.md:96-99; runbook:15-17; evidence-04 MANIFEST:30 |
| RV-23 | minor | The brief-adoption + tranche-authorization gate is not machine-visible as an open register row: D-PEC-07's row is RULED (closed) while the residual owner gate lives only in Receipt 20's parked lanes. The register's stated purpose is keeping open work machine-visible; a residual row (register convention, header lines 14-18) makes the gate discoverable. [P2] | \_REGISTER.md:14-18,28; brief:50-54 |
| RV-24 | major (found in passing — pre-existing app code, not a defect of these artifacts) | **CSV formula-injection survives the import→export round-trip:** `esc` (`server/src/import/csv.ts:29-35`) neutralizes nothing for leading `=`/`+`/`-`/`@`; imported statements/titles are stored verbatim (work_item, decision, risk vectors confirmed) and re-emitted into register exports a pilot team opens in Excel. Correctly *misfiled* against D-PEC-07 — its lawful home is its own decision row (D-PEC-06 narrow-repair precedent). [P1] | csv.ts:29-35; import/index.ts:274-275,332,380-382 |

## 3. Second-pass items incorporated / moderated

All eleven second-pass findings were assessed; nine incorporated (RV-3, -7,
-11, -13, -14, -15, -16, -17, -22, -23, plus the coord-check pair RV-6/RV-20
after re-running the tool), two moderated where this review's adversarial
verification had refuted the stronger form (RV-11 capture-basis: the standing
owner basis is real; RV-16: no separation-of-duties obligation exists to
violate). The second pass independently corroborated RV-3, RV-7, RV-22 and
contributed the `http.ts`/`SPEC.md`/`coord-check` groundings now cited above.

## 4. Challenged and refuted (recorded for transparency)

Killed in two-lens verification, with the refutation grounds: register
SHA-annotation "drift" (bare-SHA IS the PEC-register convention); raw-files
attribution error (gitignore itself cites the owner ruling); "runbook lacks
partial-reject handling" (standing rules cover it); "agent principal
contaminates audit" (agent acts only on a rolled-back tx; the human applies);
"runbook doesn't say who drops" (it says Owner); standing-pathway-exceeds-
D-PEC-01 strong form (O-C ruling formalizes repetition on the supplied
basis); replay-duplication as an artifact defect (runbook's never-full-RAIL
rule fences it; brief lists the repair); migration-story/error-state/SoD as
*brief* defects at severity (tranche-packet scope per the adoption gate —
retained as named obligations in RV-16/RV-17).

## 5. Decision slate (owner ruling required for any execution)

| ID | Option | On ruling |
|---|---|---|
| S-1 | **Packet corrigendum** — header Status→RULED + `**Ruling SHA:** 1a9e4071c` line; dated corrigendum note correcting RV-1, RV-2, RV-4 (and RV-5 if affirmed); one-line precedent note (RV-6). Ruled text never rewritten. | One branch/PR carries all affirmed items + receipt. |
| S-2 | **Runbook v1.1** — RV-7 approval-follows-proposal (or owner explicitly rules drop-time pre-approval and it is recorded verbatim); RV-8 scope idempotency to evidenced contracts, mark risks/schedule code-implied-unevidenced; RV-9 "(later: pilot)" → "pilot only under a future owner ruling"; RV-10 export-compare rule; RV-11 capture-basis pointer. | Same PR. |
| S-3 | **Brief v1.1 pre-adoption** — RV-12 residency caveat; RV-13 K-AUTH-2/hash/version binding; RV-14 CSV-only v1; RV-15 history-vs-audit choice; RV-16 permission naming; RV-17 tranche-obligations checklist (+ RV-19, RV-21); RV-18 wording; RV-20 precedent note. Alternatively: adopt as-is and push all to the tranche packet. | Same PR; brief stays CANDIDATE. |
| S-4 | **New register rows** — (a) D-PEC-08: residual row for brief adoption + tranche authorization (RV-23); (b) D-PEC-09: CSV formula-injection neutralization in exports, packet AWAITING_RULING (RV-24, D-PEC-06 pattern; optionally also split the RAIL-idempotency repair out of the brief). | Same PR authors rows/packets; repairs wait for their rulings. |
| S-5 | **`IMPORT_MAPPING.md` refresh** — evidence-04 schedule extractor mapping + risks placeholder note (RV-22). | Same PR. |

**Non-binding recommendation:** all five (the second pass's O-C, extended
with S-4b/S-5). RV-7 is the one place the artifacts genuinely weaken a gate
the owner ruled; RV-12/RV-13 are cheap pre-adoption and expensive after.

**Checks:** this report rides its publishing PR with the loop's closeout
checks; results are recorded in `_DomainEngines/pec/LOOP_RECEIPTS.md`
Receipt 21.
