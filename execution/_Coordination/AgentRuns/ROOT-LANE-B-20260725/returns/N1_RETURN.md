# N1 Terminal Return — Guard capability G1–G4 (ROOT-LANE-B-20260725)

Executor: ephemeral bounded Agent 2 generalist, `opus-5`, sealed brief
`../briefs/GUARD-CAPABILITY-BRIEF.md`
Returned: 2026-07-25 · Status: COMPLETE · Fan-in: **ACCEPTED** (V1 passed)
Raw return: `N1_RETURN_RAW.md` (unedited executor return of record).

## Summary (as received and verified)

Eight new files under `tools/validation/` (four guards G1–G4 + four test
suites, 100 tests total), four CI steps appended to
`.github/workflows/governance-harness.yml` after the G0 step, and the Lane B
tranche manifest at
`docs/governance_harness/tranche_manifests/ROOT-LANE-B-20260725.yaml` (the
G4 discipline applied to its own tranche). All guards PASS-idle on the clean
tree; guard state (adapter, ownership register, work graph,
`root_guards.yaml`) deliberately NOT instantiated — that is root Project
Setup's act. Guard IDs match G0's `REQUIRED_GUARDS`; each docstring states
its future registration entry. One real bug found and fixed during the
executor's own verification (`lstrip("./")` mangling `.github/...` paths),
pinned by regression tests in three suites.

## Agent 0 fan-in verification (independent)

- Scope: `git status` shows exactly the declared files (plus this run
  record). Write scope held; no `execution/` state surfaces created.
- Battery re-run by Agent 0: `pytest tools/validation` **233 passed**
  (was 133); `pytest tools/practitioner_harness` **311 passed**; all four
  guards + G0 + path anchors exit 0; `harness.py self-check` exit 0.
- M6 pin survey (open item 3, closed here): no loop pins or mirrors any
  touched surface (AUTHORITY_CORPUS.json pins none of them; grep survey
  found only narrative mentions). Manifest `m6_notice` set to
  **none-required** with the basis recorded.
- Registry (open item 6, closed here): five rows added to
  `tools/REGISTRY.md` — G1–G4 **and G0**, which had never been registered
  (pre-existing gap found at fan-in). `tools/REGISTRY.md` added to the
  manifest's declared paths.

## Design dispositions (Agent 0, at fan-in)

1. **ACCEPT** G1's flagged scope choice (adapter absent + materialized
   structure → BLOCK): mirrors G2's ruled idle rule, cannot fire before
   materialization, and is exactly the §5.3 condition G1 exists to prevent.
2. **ACCEPT** the exit-2 operational-error convention (D-GOV-02 0/1/2
   class; exit 2 still fails CI; gate semantics unchanged).
3. **ACCEPT** the instruction-surface set (SPEC §0.2.2 enumeration +
   `.github/workflows/` on the workplan's named basis). `CLAUDE.md`
   exclusion carried as an open owner item, not silently decided.
4. **ACCEPT** G4 diff mode not wired into CI (historical tranches predate
   the manifest discipline; diff mode is the integration owner's
   per-tranche tool).

## Open items carried (for the record; none blocks this tranche)

1. Root Project Setup instantiates guard state + `root_guards.yaml`
   (packet §6 step 8; G0 gates on it).
2. Practitioner-harness adoption of the root adapter (root not in
   `PROJECT_ALIASES`; separate, separately-authorized change).
3. Owner decision: add `CLAUDE.md` to the guarded instruction-surface set,
   and/or add `.github/workflows/` to the SPEC §0.2.2 enumeration itself.
4. G2 decomposition cross-check deepens once an accepted root
   decomposition format exists.
5. G4 diff-mode usage policy (manual per-tranche vs future PR-scoped CI
   job requiring manifests on every instruction-surface PR).
