# Evidence dependency and acquisition order

Status: `ORDER PLAN ONLY — NO SEMANTIC SELECTION`

## Selection rule

Prioritize evidence that constrains trust boundaries and mechanical
enforcement before schema or value design. Do not collect timing/budget data
against an unselected or unqualified backend and do not materialize no-TBD
bytes while any critical evidence item remains open.

## Waves

| Wave | Briefs | Gate to advance |
|---|---|---|
| 0 | AB-01 threat model; owner/platform/vendor fact request | principals, assets, deployment topology, trust anchors, release targets, and protected-data unknowns are either supplied or explicitly held open |
| 1 | AB-02 backend/topology; AB-09 DEL/compatibility alignment | at least one backend/topology has reproducible mechanical/adversarial evidence; DEL links have exact consistency/conflict/non-coverage dispositions |
| 2 | AB-03 platform matrix; AB-07 retention/privacy | exact candidate platform cells and evidence-store obligations exist; unsupported cells remain closed |
| 3 | AB-08 conformance/no-fallback | implementation-family inventory and exact evidence suite exist; fixture/fallback paths are classified |
| 4 | AB-04 timing; AB-05 budget/workload | representative clean measurements exist for every candidate platform/backend/tool/effect cell; empirical data is separate from product choices |
| 5 | AB-06 schema/state/digest candidates | all upstream evidence is hash-bound; schemas have migration, negative, and cross-language vectors; unresolved facts remain explicit |
| 6 | successor/refutation preparation | only after every implementation-critical TBD has an exact evidenced candidate value; then prepare one no-TBD successor and commission fresh independent refutation |

## Hard stops

1. The current host's `sandbox-exec` failure prevents treating it as a qualified
   backend witness.
2. One macOS/arm64 observation cannot establish a supported platform matrix.
3. Current descriptor budgets are implementation facts, not generic default or
   maximum evidence.
4. TM112's accepted 2000 ms plus 500 ms daemon-stop policy is not transferable
   to generic tool interruption.
5. DEL-02-06 V2 is usable only for exact compatibility/alignment analysis; it
   does not resolve TM105 lifetime or continuation by implication.
6. No byte gate may be presented until all 21 implementation-critical TBDs are
   absent from a successor and a fresh refuter has completed.

## Immediate bounded actions

1. Acquire the owner-supplied facts enumerated in `OWNER_VENDOR_PLATFORM_FACTS.md`.
2. Run AB-01 before asking a backend designer to narrow AB-02.
3. Commission AB-09 as a documentary crosswalk in parallel with AB-01; it may
   record only exact coverage/conflict/non-coverage.
4. Prepare clean reproducible environments only after AB-02 identifies bounded
   backend candidates and AB-03 names candidate platform cells.
5. Preserve this carrier as the Phase-1 census baseline; later evidence runs
   must cite it and record drift rather than mutating it.
