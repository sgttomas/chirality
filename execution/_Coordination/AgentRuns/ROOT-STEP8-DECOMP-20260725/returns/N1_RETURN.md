# N1 Terminal Return — Candidate first root decomposition (fan-in accepted)

Run: ROOT-STEP8-DECOMP-20260725 · Executor: Agent 1 instance, SOFTWARE_DECOMP
role, `opus-5`, sealed brief `../briefs/ROOT-DECOMP-BRIEF.md`
Returned: 2026-07-25 · Status: CANDIDATE STAGED · Fan-in: **ACCEPTED** after
adversarial verification (V1) and directed corrections.
Raw returns of record (unedited): `N1_RETURN_RAW.md` (authoring),
`V1_RETURN_RAW.md` (verification). The correction round is recorded in this
file and in the run transcript; the raw N1 return still carries the
pre-correction BLOCKER-1 sentence in its §3 — that discrepancy is recorded
here, deliberately, rather than edited away.

## What was produced (as received and verified)

Candidate first root decomposition of the Chirality Root product, derived
solely from the adopted PRD (`docs/PRD_ROOT.md`, sha256-pinned, basis
`24726a73c`), staged under root `execution/_Decomposition/`:

- Working surface `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` + six
  authoritative companion registers (scope ledger 103 rows; deliverable
  register 45; objective register 7; F4 forward 84; F4 reverse 51;
  coverage telemetry).
- Partition: **6 packages / 45 deliverables** (PKG-01 Product Definition,
  Normative Basis & Authority · PKG-02 Operative Instruction Surface &
  Runtime Layers · PKG-03 Governed Execution Structure & Root Containment ·
  PKG-04 Developmental Machinery & Change Control · PKG-05 Evidence,
  Provenance & Audit · PKG-06 Self-Application, Variants & Release).
- **All seven gates PENDING_OWNER_RULING. Nothing accepted by any agent.**

## Independent verification (V1, ephemeral Agent 2, `opus-5`)

V1 re-derived every count, re-enumerated the PRD's 42 §5 commitments and 7
objectives from source, re-verified all four sha256 pins, and read all 103
ledger rows and 45 deliverables. Everything structural held: F4 closed in
both directions (84/84 covered, 51/51 traced, zero dangling IDs in six
directions), D-15 category coverage exact on recount, I3–I10 conformance,
SPEC ID format, G2 literal containment 51/51, source purity (every SourceRef
names the PRD; zero scope from context documents), scope hygiene, and
candidate posture (no acceptance language anywhere).

Findings and dispositions (Agent 0, at fan-in):

1. **BLOCKER-1 — CORRECTED before staging.** Narrative gloss claimed every
   package participates in ≥3 categories; PKG-02 participates in 2. The
   registers never carried the error. N1 (resumed) corrected the working
   surface §8 and telemetry §4 to the recounted fact; post-edit grep
   confirms the false claim appears nowhere under `execution/_Decomposition/`.
2. **MAJOR-1 — ROUTED TO OWNER as OI-013.** OBJ-2's success condition ends
   "demonstrated at root and in at least one situated working root"; no
   deliverable covers the situated-root half and no deferral is recorded.
   F4 is not formally tripped (objective-granularity coverage), but the gap
   is real. The candidate now records it as OI-013 with disposition
   PENDING_OWNER_RULING; no agent chose cover-vs-defer.
3. **MINOR-1 — CORRECTED** (§6 source-section tally, recounted).
4. **MINOR-2..6 — ACCEPTED AS REVISION-TIME ITEMS**, not gating: §8.1
   non-goal granularity; DEL-06-07→OBJ-004 weak mapping; CSVs carrying
   package-role labels via companion inventories only; DEL-03-05
   anticipated artifacts naming real guard-state paths from the live
   validators (verified real, not invented scope); GOVERNANCE_TRANCHE
   declared-unused vocabulary entry.

## Items requiring owner attention at the ruling (beyond the gates)

- **OI-013** (above): cover OBJ-2's situated-root clause or record a
  reasoned deferral.
- **OI-001** (source currency, D-14-class REVIEW finding): the adopted PRD
  bytes present §9.1 obligations (a)/(b)/(c) and conflicts C-1..C-4 as
  open, but the governance register records them discharged (D-GOV-23/24,
  the C-2/C-4 correction tranche, and the C-3 confirmation at the D-GOV-22
  ruling). The candidate keeps the derived scope IN, expressed as standing
  verification/maintenance rather than re-performance. Owner confirmation
  requested; adopted bytes were not touched (D-13).
- **OI-002**: adopted bytes say PROPOSED items are inert until the adoption
  instrument's ruling; the D-GOV-22 register row says the 17 PROPOSED items
  take effect. The ledger carries source labels unchanged and asks for
  confirmation (F6 discipline).
- **OI-003/OI-004** (framing strains, disclosed): SOFTWARE_DECOMP's SOW
  framing vs the root product's nature; and the reading that in-force
  commitments generate standing conformance deliverables rather than
  one-shot construction — the candidate's largest judgment call.

## Agent 0 fan-in verification (independent)

- Scope: `git status --porcelain` shows exactly `execution/_Decomposition/`
  and this run record, across both the authoring and correction rounds.
- Battery at fan-in: 233 validation + 311 practitioner-harness tests pass;
  G0–G3 idle-PASS; path anchors 996 surfaces PASS. `_Decomposition` is on
  the path-anchor validator's exclusion list, so the machine-absolute-path
  sweep was run separately by N1 and re-run by V1 — clean.
- No `PKG-*`/`DEL-*` directory exists anywhere; no instruction surface
  touched; `execution/_harness/` not created. Step 9 remains fully gated.
