# Decomposition-standard and precedent notes (Agent 0 context assembly, step 8)

Run: ROOT-STEP8-DECOMP-20260725 · Date: 2026-07-25 · Basis: `24726a73c`
Source: read-only survey of `docs/DECOMPOSITION_STANDARD.md`, the three
decomposition managers, and materialized decompositions. Derivative evidence;
the surveyed sources govern.

## Standard (RATIFIED, D-GOV-14)

- 7 gates, every one human-gated (I1); no gate skipped. Gate 7's acceptance
  phrase: the human states the decomposition is the accepted basis for
  downstream work.
- Invariants I1–I10: human validation; no invention (unknowns → TBD + open
  issue); flat partitions; no overlap/no gaps; stable IDs; deterministic
  production-unit↔partition ID coupling; best-effort objective mapping;
  traceable rationale; ledger + telemetry (UnassignedINUnits must be 0);
  vocabulary discipline.
- Conforming output is a package: one working-surface document + authoritative
  companion registers + package-role labels on every artifact; monolithic
  renders are `derived publication artifact` only.
- The standard names no acceptance instrument; repo practice supplies two:
  (a) gate-log/status acceptance quoting the human (domain pack, per-gate
  snapshots), (b) exact-candidate-SHA ruling (governance acts). App-dev
  precedent: "Gates 1–7 accepted by implicit human approval per user
  instruction" — batch acceptance at explicit human direction is exercised
  practice.

## Manager selection (Agent 0, recorded before dispatch)

Selected: **SOFTWARE_DECOMP** (`agents/AGENT_SOFTWARE_DECOMP.md`).

- Owner's ruled vocabulary in the D-GOV-21 packet §1 ("Packages PKG and
  Deliverables DEL in the Execution folder") fixes Partition=PKG,
  ProductionUnit=DEL — excludes DOMAIN_DECOMP's CAT/KTY entities.
- PROJECT_DECOMP's own `PKG-XXX` 3-digit width contradicts SPEC §1's
  canonical `PKG-XX_{Label}`/`DEL-XX-YY_{Label}`; EPC framing unfit.
- SOFTWARE_DECOMP matches SPEC §1, matches the sole existing PKG/DEL
  materialization (`projects/chirality-app-dev`, 10 PKG / 51 DEL), and its
  Context Envelope discipline serves dispatchability of root deliverables.
- Known strain, surfaced not hidden: its intake framing is a software
  development SOW; the root product also contains the normative corpus and
  evidence machinery. The brief instructs conformance to the standard with
  strain recorded in Open Issues. No prior record names any manager; this
  selection is Agent 0 judgment under the owner's step-8 release and binds
  nothing — all seven gates plus the exact-candidate-SHA ruling remain the
  owner's.

## Location and acceptance plan

- Candidate lives at root `execution/_Decomposition/` (control-plane, not
  `PKG-*`/`DEL-*`; G0 unaffected), mirroring the project precedent.
- Acceptance vehicle: exact-candidate-SHA ruling over the staged candidate
  (all gate outputs inspectable; Gate Log marks each gate
  PENDING_OWNER_RULING until ruled). Gate-by-gate review remains available
  to the owner as an alternative.
- Post-ruling tranche (separate): decision record, register row, receipts,
  then root Project Setup instantiating guard state per
  `evidence/GUARD_STATE_SPEC.md`.
