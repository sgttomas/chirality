# NOTICE — HELPS_HUMANS intake of REQUEST_2026-07-25 (routed), 2026-07-25

Routed to this surface by the session Agent 0 after adversarial fan-in
(one sealed refutation round, 3 CRIT + 6 MAJ + 3 MIN, all applied via a
versioned brief amendment before this notice was issued). Dispatch was
owner-directed: "…we should dispatch the cleanup for OI-013."

All 8 items intake-complete. **Item 2 (OI-013) is closed on the tooling
side**: `tools/validation/validate_decomposition_registers.py` is live
and tested (29 tests; full validation suite 153 passing), and reproduces
R4's measurements exactly — 87 `EVQ-001` locus/quote duplications, 33
`EVQ-003`/`EVQ-004` empty-evidence rows, 120 EXECUTION rows, 135 ANCHOR
rows clean. Cross-register (`XRG`) and dependency-binding (`DRB`) checks
pass clean, confirming the defect is confined to evidence cells.

Note on `EVQ-001`: the duplication runs in **both** directions. Some
rows carry the exhibit's quote text in the locus column; others (e.g.
`DEP-03-01-008..013`, `'PEC-RCN-002 feed list (DL-4)'`) carry a locus in
the quote column. Repair must inspect each row, not apply one
transformation.

**PEC follow-on — the closure gate, stated precisely.** Run
`validate_decomposition_registers.py projects/pec/execution --json
<snapshot>/register_findings.json` for exact row IDs; `--families EVQ`
isolates the evidence checks. The gate is **not** "re-run to exit 0"
taken naively — some of the 120 rows may be real dependencies with no
quotable source text, and demanding a quote for those would be demanding
a fabrication. The gate is: **zero `EVQ-001`**, and **every
`EVQ-003`/`EVQ-004` row individually dispositioned** — either given a
real locus and a real quote, or covered by a declared waiver in
`Dependencies_EvidenceWaivers.csv` carrying an attributed, substantive
rationale. With every row so dispositioned, exit 0 is a truthful closure
signal; waived rows remain visible as WARNINGs and under `--strict`.
(The waiver mechanism is new, additive contract surface no accepted
decision yet blesses — flagged for the owner; it is isolated and cheap
to swap if a different honest-empty convention is preferred.)

Items 1, 3, 4, 5, 6, 7, 8 are dispositioned with change proposals in
`plans/helps_humans_tooling_consolidation_2026-07-25/`, **awaiting owner
approval**. Four carry amendments worth noting: item 3 has a second,
unreported defect (deliverable count 96 vs 64 — the state-count
denominator is also wrong); item 6 is not fragile but already broken,
and the fix required an explicit heading-normalization spec verified
against three live SOFTWARE documents; item 7's `DEL-NN-NN/REQ-NNN` form
is not currently safe; item 5's `CheckNumber` needs a type change, not a
range widening.

**Correction to an earlier draft of this notice:** it stated that
`SOFTWARE_DECOMP.md` lines 536/635/651 carried the same off-by-one and
needed PEC repair. **That was wrong.** All three resolve correctly
against the live section map. They are independent corroboration that
the *agent tables* are wrong. **No repair is required, and editing them
to match the agent tables would introduce the defect.**

This is coordination, not authority. The receiving loop adopts, amends,
or declines under its own instruments. The repair of the 120 EXECUTION
rows is a PEC-loop act requiring its own owner-ruled packet (the
deliverable-local `Dependencies.csv` files are outside PROJECT_SETUP's
default writable fence).
