# SCA Supersession Backfill — Controller Prompt

Use this prompt to resume after context compaction.

---

## Your Role

You are the campaign controller for the West Doe Two-Root DBM campaign. The 8-phase campaign is complete — both DBMs are published with source-fidelity corrections. You are now executing Change 7 from the supersession binding implementation plan: backfilling `Supersession_Map.csv` and `Supersession_Delta.csv` for the accepted SCA-001 through SCA-004 chain in both roots.

---

## What Is Already Done

The supersession binding governance and tooling are fully installed (commits `b14d3ee` and `2900446`):

- `agents/AGENT_SCOPE_CHANGE.md` — `Supersession_Map.csv` schema (13 columns), `Supersession_Delta.csv`, `SupersessionBindingPresent` flag in `Amendment_Actions.csv`
- `agents/AGENT_AUDIT_SCOPE_CLOSURE.md` — Pass 6 supersession binding verification
- `agents/AGENT_DBM_PUBLISHER.md` — Gate 1 freezes supersession map, revised ConflictPrecedence (SCA overrides source only when explicitly bound)
- `skills/dbm-section-publish/SKILL.md` — `SUPERSESSION_MAP_PATH` in RuntimeOverrides, structured binding enforcement
- `skills/dbm-publish/SKILL.md` — `validate_source_supersession.py` as Gate 6 sub-check
- `skills/dbm-concordance-seed/SKILL.md` — `SourceFidelityCritical` and `SourceExpectedValue` columns
- `tools/publication/validate_source_supersession.py` — new deterministic validator
- `tools/publication/render_dispatch_briefs.py` — propagates supersession and applicability fields

---

## What Remains — Change 7: Backfill

For each root (C&L and Deepcut), for each accepted SCA (SCA-001 through SCA-004):

1. Read the existing `Decision_Log.md` and `Amendment_Actions.csv` in the SCA snapshot
2. Identify which actions changed facts that conflict with the cleaned source Process DBM at `domain-test/domains/West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/`
3. Produce `Supersession_Delta.csv` for that SCA with the source reference bindings
4. Produce the cumulative `Supersession_Map.csv` in the active (SCA-004) snapshot
5. Update `Amendment_Actions.csv` to add the `SupersessionBindingPresent` column

The schema for `Supersession_Map.csv` is defined in `agents/AGENT_SCOPE_CHANGE.md` under "### Supersession Map Schema". The `OverrideType` values are `SUPERSESSION` and `SUPPLEMENTARY_EXTENSION`.

---

## Both Roots — SCA Chain

### Comp & Liquids (03-25)

SCA snapshots at `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_ScopeChange/`:

| SCA | Key Changes | Expected Supersession Bindings |
|---|---|---|
| SCA-001 | Value engineering: non-regenerative caustic, VRU reroute to 04-25 SOC, KTY retirements | Stabilizer retirement, SOC retirement, VRU reroute |
| SCA-002 | Consolidation: stabilizer/SOC/heat medium to 04-25; 3 KTYs retired | Heat medium retirement, condensate dehydration retirement |
| SCA-003 | Full remediation: terminology, shared interfaces, flare boundary, LACT routing, compressor hp, incinerator framing | Terminology normalizations (NGL, Cross-Facility, NRM NEBC Connector), LACT scope, compressor hp resolution |
| SCA-004 | KTY-07-07 Mechanical Package Structure | Supplementary extension (no source override) |

Estimated: ~15-20 supersession bindings total.

### Deepcut (04-25)

SCA snapshots at `domain-test/domains/West_Doe_Deepcut_DBM/_ScopeChange/`:

| SCA | Key Changes | Expected Supersession Bindings |
|---|---|---|
| SCA-003 | Full remediation: terminology, shared interfaces, specification corrections | Terminology normalizations, pipeline naming |
| SCA-004 | KTY-07-07 Mechanical Package Structure | Supplementary extension (no source override) |

Estimated: ~10-15 supersession bindings total.

---

## Subagent Model — 4 Parallel Opus Agents + Controller Merge

Each SCA snapshot is independent. The work is parallelized by SCA group, not by root.

```
CONTROLLER (this session)
│
├── Agent 1: C&L SCA-001 + SCA-002 (retirements, consolidations)
│   ├── Read Decision_Log.md + Amendment_Actions.csv for both snapshots
│   ├── Identify source-affecting actions
│   ├── Write Supersession_Delta.csv in each snapshot
│   └── Update Amendment_Actions.csv with SupersessionBindingPresent
│
├── Agent 2: C&L SCA-003 + SCA-004 (terminology, interfaces, supplementary)
│   ├── Same workflow for both snapshots
│   └── SCA-004 is likely SUPPLEMENTARY_EXTENSION only (KTY-07-07)
│
├── Agent 3: Deepcut SCA-003 (terminology, interfaces)
│   ├── Same workflow for one snapshot
│   └── ~10 bindings expected
│
├── Agent 4: Deepcut SCA-004 (supplementary only)
│   ├── Same workflow for one snapshot
│   └── ~2 bindings expected (KTY-07-07)
│
└── Controller: Merge step (sequential, after all 4 agents)
    ├── For C&L: concatenate SCA-001 + SCA-002 + SCA-003 + SCA-004 deltas
    │   into cumulative Supersession_Map.csv in the SCA-004 snapshot
    ├── For Deepcut: concatenate SCA-003 + SCA-004 deltas
    │   into cumulative Supersession_Map.csv in the SCA-004 snapshot
    └── Verify both cumulative maps
```

All 4 agents run in parallel. They touch completely independent SCA snapshot directories. No serialization needed for the delta production. Only the cumulative merge is sequential.

### Common inputs for all agents

Each agent reads:
1. The supersession map schema from `agents/AGENT_SCOPE_CHANGE.md` (search for "Supersession Map Schema")
2. The cleaned source Process DBM from `domain-test/domains/West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/Process_DBM_fixed.md`
3. The canonical source data tables from `domain-test/domains/West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/data/*.csv`

### Per-agent outputs

Each agent writes into its assigned SCA snapshot directory:
1. `Supersession_Delta.csv` — new supersession bindings for that SCA
2. Updated `Amendment_Actions.csv` — existing file plus the `SupersessionBindingPresent` column

Each agent does **not** produce the cumulative `Supersession_Map.csv` — that is the controller's merge step.

### Agent assignment table

| Agent | Root | SCAs | Snapshot Paths | Est. Bindings |
|---|---|---|---|---|
| 1 | C&L | SCA-001, SCA-002 | `West_Doe_Comp_and_Liquids_DBM/_ScopeChange/SCA-001_*/`, `SCA-002_*/` | ~8 |
| 2 | C&L | SCA-003, SCA-004 | `West_Doe_Comp_and_Liquids_DBM/_ScopeChange/SCA-003_*/`, `SCA-004_*/` | ~12 |
| 3 | Deepcut | SCA-003 | `West_Doe_Deepcut_DBM/_ScopeChange/SCA-003_*/` | ~10 |
| 4 | Deepcut | SCA-004 | `West_Doe_Deepcut_DBM/_ScopeChange/SCA-004_*/` | ~2 |

### Controller merge step

After all 4 agents complete:
1. **C&L cumulative map:** Read the 4 delta CSVs (SCA-001 through SCA-004), concatenate in SCA order, write `Supersession_Map.csv` into the active SCA-004 snapshot
2. **Deepcut cumulative map:** Read the 2 delta CSVs (SCA-003 and SCA-004), concatenate in SCA order, write `Supersession_Map.csv` into the active SCA-004 snapshot
3. Verify both cumulative maps

---

## Verification

After the merge step:
1. Verify each cumulative `Supersession_Map.csv` covers the known source-affecting decisions from the campaign
2. Verify every `SupersessionBindingPresent = YES` action in each snapshot's `Amendment_Actions.csv` has at least one corresponding row in that snapshot's `Supersession_Delta.csv`
3. Spot-check that `SupersededAuthorityRef` values are non-empty for all `SUPERSESSION` rows and point to real sections/lines in `Process_DBM_fixed.md` or `data/*.csv`
4. Run `validate_source_supersession.py` against one root to confirm it produces correct PASS/FINDING classifications (this requires the concordance register to have `SourceFidelityCritical` and `SourceExpectedValue` columns — that is a separate follow-on task; the backfill itself does not modify the concordance register)

---

## Key References

| Artifact | Path |
|---|---|
| Supersession map schema | `agents/AGENT_SCOPE_CHANGE.md` (search for "Supersession Map Schema") |
| Cleaned source Process DBM | `domain-test/domains/West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/Process_DBM_fixed.md` |
| Source data tables | `domain-test/domains/West_Doe_Combined/_Sources/west_doe_process_design_basis_clean/data/*.csv` |
| C&L SCA snapshots | `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_ScopeChange/` |
| Deepcut SCA snapshots | `domain-test/domains/West_Doe_Deepcut_DBM/_ScopeChange/` |
| Validator tool | `tools/publication/validate_source_supersession.py` |
| Backfill plan context | `plans/WEST_DOE_TWO_ROOT_DBM_SOURCE_FIDELITY_RESET_AND_TARGETED_RERUN_PLAN.md` §3 (root cause) and the plan file at `.claude/plans/deep-coalescing-rivest.md` Change 7 |

---

## User Profile

Oil & gas project manager, new to Chirality. Frame explanations in PM terms. Values iterative plan review, sequencing discipline, no overclaims, governance authority in the main thread. Prefers right-sized dispatch — match agent count to task complexity.
