# D-PEC-65 — DRAFT v2: OI-013 register evidence repair (120 EXECUTION rows, 64 deliverable-local registers)

**Status:** DRAFT v2 — AWAITING OWNER RULING (v1 refuted 2026-07-25: 3 CRIT /
7 MAJ / 5 MIN, one MAJ refuted-in-part; all dispositions applied — log in §8)
**Date drafted:** 2026-07-25 · **Drafted by:** session Agent 0 (PROJECT_SETUP posture)
**Depends on:** D-PEC-62 (seeded registers), D-PEC-63 (wave closure; defect scale
measured at closure refutation R4), the OI-013 tooling closure
(`tools/validation/validate_decomposition_registers.py`, live at `c6ae772ad`,
merged to main in PR #353), and the routed notice
`../NOTICE_2026-07-25_helps_humans_oi013_response.md` (which states the closure
gate this packet adopts).

---

## 1. Owner direction of record (2026-07-25)

1. "update the version reference in that `_COORDINATION.md` and then **we
   should dispatch the cleanup for OI-013**" — executed on the tooling side
   (validator live, tested, measurements reproduced).
2. Carry-forward directive over the three-item decision slate ("Here's where
   we left off, I want to carry forward with these"), whose item 3 read:
   "The PEC register repair — fixing the 120 seeded EXECUTION rows is a
   PEC-loop act needing its own packet … Say the word and I'll draft
   D-PEC-65." This packet is that draft. The same directive carried forward
   item 2, recording the owner's acceptance of the **evidence-waiver
   mechanism** (sidecar `Dependencies_EvidenceWaivers.csv`; only
   EVQ-003/EVQ-004 waivable, never EVQ-001) as the accepted honest-empty
   convention — this packet builds on that convention.

The repair itself executes only on this packet's ruling: the deliverable-local
`Dependencies.csv` files are outside PROJECT_SETUP's default writable fence.

## 2. Defect basis (measured, not estimated)

Source: D-PEC-63 closure refutation R4 (independent scan of all 64 registers),
independently reproduced by `validate_decomposition_registers.py` against the
live corpus (exit 1, 153 ERROR findings), and re-reproduced by the v1
refutation of this packet:

- **EVQ-001 = 87** — locus/quote duplication: `SourceRef` and `EvidenceQuote`
  carry identical non-empty text (the seeding exhibit's `BasisCitation` in
  both cells, with the exhibit's `Rationale` in `Statement`; seeder mechanism
  confirmed at `seed_local_dependencies.py:130-132`). The duplication runs in
  **both directions**: some rows carry quote text in the locus column (e.g.
  `DEP-00-02-003`), others (e.g. `DEP-03-01-008..013`) a locus in the quote
  column. Repair must inspect each row; no single transformation is safe.
  **55 of the 87** duplicated values embed a quoted span, so repairing
  EVQ-001 without cleaning the locus cell would unmask EVQ-002 WARNINGs —
  the repair standard in §3.1 therefore requires quote-free loci.
- **EVQ-003 = EVQ-004 = 33** (the identical 33-row set) — empty
  `EvidenceQuote` with `SourceRef` `"location TBD"` (mirroring an empty
  exhibit `BasisCitation`).
- **All 135 ANCHOR rows are clean.** The defect is confined to the 120
  EXECUTION rows and is systemic to the D-PEC-62 seeding generator, not
  instance-level. `XRG` and `DRB` families pass clean (exit 0).
- All 120 EXECUTION rows share one `EvidenceFile`: the D-PEC-62 PLAN exhibit
  — which D-PEC-62 §3.3 ruled **frozen gate provenance, consulted only as
  history**. Evidence repair must therefore re-point rows at live accepted
  sources (§3.1), not re-ground them on the exhibit.
- `analyze_dep_closure.py`'s "Evidence coverage 255/255" tests `EvidenceFile`
  presence only and is not a counter-signal.

No topology defect exists: 64 files, 255 rows = 135 ANCHOR + 120 EXECUTION,
62 nodes / 120 edges, orphans 2, SCCs 0 — all invariants hold and must
survive the repair unchanged.

## 3. Ruled behavior (proposed)

### 3.1 Repair method

Sealed ephemeral Agent 2 repair dispatches (opus-5), fanned out **per package**
(11 packages, all 11 defect-bearing; concurrency ≤ 4), write sets disjoint by
construction (deliverable-local files only). Per root-doctrine
package-parallel rules, **repair children are bounded-file-tool-only (no
Bash)**; all validator and closure-tool runs are the dispatcher's own acts at
fan-in. Each dispatch:

- Inspects **every EXECUTION row individually** in its package's registers.
  ANCHOR rows are read-only.
- Grounding order for real evidence (accepted live truth first; exhibit
  last, as history only, per D-PEC-62 §3.3):
  `execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.2 `current_basis`)
  and its companion registers (`Deliverables.csv`, `ScopeLedger.csv`), then
  `docs/PRD.md` v2.1, then (for wave members) the accepted upstream
  `ScopeOfWork.md` contracts and deliverable-local `_CONTEXT.md` (OI carrier),
  and only lastly the frozen D-PEC-62 exhibit
  (`SEED_D-PEC-62/edges_v02.csv` / PLAN) as provenance for what the seeder
  intended — never as the cited evidence source.
- A repaired row gets: a **real locus** in `SourceRef` (section / row /
  anchor; it must contain **no quoted span** — EVQ-002's machine test must
  not fire), a **verbatim quote** in `EvidenceQuote` copied from the cited
  locus, and an **`EvidenceFile` re-pointed to the document the quote
  actually lives in**. `EvidenceFile`, `SourceRef`, and `EvidenceQuote` must
  name one coherent document.
- **Fabrication is prohibited.** If no quotable source text exists for a real
  dependency, the row is NOT given an invented quote: it is covered by
  declared waiver rows in the deliverable-local
  `Dependencies_EvidenceWaivers.csv` sidecar (create-if-needed; columns per
  the validator contract: `DependencyID, WaivedCheck, Rationale, DeclaredBy,
  DeclaredOn`). Waivers are keyed per `(DependencyID, WaivedCheck)` pair:
  **a fully-waived empty-evidence row requires two rows — one waiving
  `EVQ-003` and one waiving `EVQ-004`** (an expected fully-waived corpus
  carries 2 waiver rows per waived dependency). Each waiver carries a
  substantive attributed rationale (`DeclaredBy` = `TASK-repair/D-PEC-65`,
  `DeclaredOn` = date, both required per EVQ-009; rationale ≥ 30 chars,
  policed by EVQ-008; a waiver whose row later gains real evidence becomes an
  EVQ-007 ERROR and must be removed in the same change). Only
  `EVQ-003`/`EVQ-004` are waivable — **every EVQ-001 row must be truly
  repaired**, never waived.
- Editable cells per row: `SourceRef`, `EvidenceQuote`, `EvidenceFile`, and
  — only where the seeded `Statement` verbatim-duplicates the exhibit
  `Rationale` in a way that misstates the dependency claim — `Statement`,
  with every `Statement` edit individually flagged in the run record. All
  other cells (IDs, classes, targets, maturities, `SatisfactionStatus`,
  `Confidence`, `Origin`, `FirstSeen`/`LastSeen`, `Status`, `Notes`) are
  untouched. No rows added or deleted; no schema change; no reordering.
- Returns a structured per-row disposition table: `REPAIRED` (locus + quote +
  evidence file) / `WAIVED` (rationale) / `ALREADY-CLEAN`, with per-file
  before/after row counts.

### 3.2 What this packet does NOT open

No `_STATUS.md` writes; no lifecycle transitions; no `ScopeOfWork.md` edits;
no decomposition-truth writes (`SOFTWARE_DECOMP.md` and the central registers
are read-only — evidence-cell repair in deliverable-local registers amends no
accepted decomposition content, so no SCA session is required;
`AGENT_SCOPE_CHANGE.md` classifies `Dependencies.csv` as downstream truth);
no source work (`F-PEC-1` unaffected). Children carry no Bash (§3.1).

### 3.3 Fan-in, refutation, and records

Dispatcher (session Agent 0) fan-in per package:

- **Validator re-run is whole-corpus** (the tool has no package-scoping flag;
  pointing it at a package directory scans zero files and false-greens):
  `validate_decomposition_registers.py projects/pec/execution --json …`, then
  findings filtered by path prefix for the package under fan-in. Snapshot
  deltas are read from the JSON `error_count` and per-finding `severity`
  fields, not the human summary table (which prints default severities).
- **Deterministic 100% quote check** (dispatcher-run): every `REPAIRED` row's
  `EvidenceQuote` is verified as a verbatim substring (`grep -F`-equivalent)
  of its cited `EvidenceFile`. This is the machine floor under §5's "truly
  repaired" — no repaired quote ships unverified.
- Fence check: `git status --porcelain` **diffed against the pre-repair
  porcelain baseline recorded in `REPAIR_D-PEC-65/` at dispatch time** (the
  tree may carry unrelated external-tranche modifications); commits are made
  by explicit path list, never `git add -A`.
- Spot-read of repaired rows.

Per the standing steer, a **sealed adversarial refutation round precedes
closure**: refuters verify (a) locus *aptness* of repaired rows (does the
cited locus actually warrant the dependency claim) on a minimum 20% sample
per package plus 100% of `Statement` edits — verbatim-ness is already 100%
machine-checked above, (b) every waiver rationale is substantive and true,
(c) invariants unchanged. Findings are dispositioned at fan-in; defects route
to fresh sealed revision dispatches, never inline repair.

Durable records: `execution/_Coordination/REPAIR_D-PEC-65/` — porcelain
baseline, before/after `--json` snapshots
(`register_findings_{before,after}.json`), per-package fan-in records,
refutation log, closure record.

## 4. Exact fence (writes authorized by this packet when RULED)

- `projects/pec/execution/PKG-*/*/DEL-*/Dependencies.csv` in any lifecycle
  folder (`1_Working`/`2_Checking`/`3_Issued`; today all 64 are in
  `1_Working`) — EXECUTION-row
  `SourceRef`/`EvidenceQuote`/`EvidenceFile`/flagged-`Statement` cells only
- Sibling `Dependencies_EvidenceWaivers.csv` (create-if-needed, waiver rows only)
- Sibling `_run_records/` (create-if-needed — 32 of 64 folders lack it; repair
  run records)
- `projects/pec/execution/_Coordination/REPAIR_D-PEC-65/**`
- **Closure pointers opened by this packet** (per-tranche clause, precedent
  D-PEC-62 §3.5/§4 — these are NOT default-writable): `_COORDINATION.md`
  item, `_DECISIONS/_REGISTER.md` (D-PEC-65 row),
  `_DomainEngines/pec/LOOP_RECEIPTS.md` (receipt append),
  `projects/pec/docs/STATUS.md` (a single one-line amendment if warranted)
- Git: scoped commits per fan-in batch by explicit path; merge to local main
  per standing closeout practice. Nothing else.

## 5. Verification and the closure gate (calibrated)

**Before** (must reproduce, recorded as the baseline snapshot): exit 1;
`EVQ-001 = 87`, `EVQ-003 = 33`, `EVQ-004 = 33`, ERROR = 153; XRG/DRB exit 0.

**The closure gate — stated precisely (per the routed notice; NOT naive
"exit 0"):**

1. **Zero `EVQ-001`** and **zero `EVQ-002`** — every duplication truly
   repaired (verbatim-ness 100% machine-verified per §3.3) and no
   quote-shaped loci left behind.
2. **Every `EVQ-003`/`EVQ-004` row individually dispositioned** — real locus
   + verbatim quote + coherent `EvidenceFile`, or valid declared waiver rows
   (both checks waived per §3.1).
3. With 1–2 satisfied, `validate_decomposition_registers.py
   projects/pec/execution` exits **0** as a truthful signal (read from JSON
   `error_count = 0`); waived rows remain visible as WARNINGs; the `--strict`
   run's output is recorded (not required to be 0 — that is the
   waiver-visibility channel working, and with EVQ-002 held at zero its
   WARNING stream is waivers only).
4. Invariants byte-identically unchanged: 64 files, 255 rows (135/120),
   `analyze_dep_closure.py` at D-PEC-62 landing values (62 nodes / 120
   edges, orphans 2, SCCs 0, IMPLEMENTS_NODE 64), census `32 INITIALIZED /
   32 OPEN`, and blocker state 24 BLOCKED / 40 UNBLOCKED reproduced by
   `python3 projects/pec/execution/_Coordination/WAVE_D-PEC-63/report_blocker_state.py
   projects/pec/execution --output <REPAIR_D-PEC-65 snapshot>` (repo-root
   relative; re-run 2026-07-25 reproduced 24/40 exactly).
5. Waiver census reported to the owner at closure (waived-dependency count +
   waiver-row count + per-package distribution). **No waiver quota or target
   exists** — a high waiver count with honest rationales beats a low count
   with fabricated quotes.

## 6. Rollback

`git revert` of the repair commits restores all 64 registers and removes the
sidecars; no pointer surgery required. Receipt/register lines are annotated,
never deleted (D-PEC-62 rollback lesson). Note EVQ-007 semantics on any
partial rollback: a surviving waiver over a row that regained real evidence
turns ERROR — re-run the validator after any revert.

## 7. Human ruling

_Reserved for the owner. Defaults proposed above: per-package fan-out with
file-tool-only children, `EvidenceFile` re-pointing required for coherence,
Statement edits allowed only where flagged, waiver attribution
`TASK-repair/D-PEC-65` (two rows per fully-waived dependency), 100%
machine verbatim-quote check + 20% human locus-aptness sampling floor.
Rule as drafted, or amend any default._

## 8. Refutation log (v1 → v2, 2026-07-25)

Sealed opus-5 refuter vs draft v1: **3 CRIT / 7 MAJ / 5 MIN**; every §2
measurement, the fence glob (64/64), the sidecar/waivability contract, the
closure-gate-vs-notice mapping, the no-SCA classification, and write
disjointness were independently CONFIRMED. Dispositions, all applied in v2:

- **C1 ACCEPTED** — waivers key per `(DependencyID, WaivedCheck)`; v1's
  singular "a declared waiver row" made the gate unreachable (33 residual
  EVQ-004 ERRORs). v2 §3.1 requires two rows per fully-waived dependency.
- **C2 ACCEPTED** — no package-scoping flag exists; a package-directory run
  scans 0 files and exits 0 (false-green). v2 §3.3 mandates whole-corpus
  runs filtered by path prefix.
- **C3 ACCEPTED** — `LOOP_RECEIPTS.md` and per-tranche `docs/STATUS.md`
  upkeep are NOT default-writable (`projects/pec/AGENTS.md`; receipts file
  is repo-root). v2 §4 opens them explicitly per-tranche (D-PEC-62
  precedent).
- **M1 ACCEPTED** — 55/87 duplicated values embed quote spans; naive EVQ-001
  repair unmasks EVQ-002. v2: quote-free loci required; gate adds
  `EVQ-002 = 0`.
- **M2 ACCEPTED** — `EvidenceFile` (uniformly the frozen PLAN exhibit) was in
  neither cell list. v2: editable, re-pointing required for
  file/locus/quote coherence.
- **M3 ACCEPTED** — v1's grounding order led with the exhibit D-PEC-62 §3.3
  froze as history-only. v2 inverts: accepted rev-1.2 truth first, exhibit
  last as provenance only.
- **M4 ACCEPTED** — root doctrine forbids Bash-bearing package-parallel
  children. v2: children are file-tool-only; validator runs are the
  dispatcher's.
- **M5 ACCEPTED** — 20% sampling could not carry "truly repaired." v2 adds
  the 100% deterministic verbatim-substring check; human sampling retargets
  locus aptness.
- **M6 REFUTED-IN-PART** — the reproducing command exists
  (`WAVE_D-PEC-63/report_blocker_state.py`, re-run 2026-07-25: 24/40 exact);
  the refuter's repo search missed it. Its fix stands anyway: v2 §5.4 names
  the exact command.
- **M7 ACCEPTED** — tree carries concurrent external-tranche modifications.
  v2: porcelain baseline recorded at dispatch; explicit-path commits only.
- **m1–m5 ACCEPTED** — lifecycle-folder fence wording; `_run_records/`
  create-if-needed; EVQ-007/EVQ-009 semantics stated; exhibit + `_CONTEXT.md`
  placed in the grounding order; JSON-not-summary snapshot rule.
