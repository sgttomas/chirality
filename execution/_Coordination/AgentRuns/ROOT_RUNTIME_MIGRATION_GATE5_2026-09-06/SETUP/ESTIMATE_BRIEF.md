# TASK historical effort successor mapping

PURPOSE: Execute estimate-snapshot as a bounded historical effort mapping under Gate4; do not invent a new current estimate.
RequestedBy: PROJECT_SETUP
TaskSkill: estimate-snapshot
TaskProfile: NONE
ScopePath: projects/chirality-runtime/execution/_Estimates/SCA005_SUCCESSOR
ApplyEdits: true
AllowedWriteTargets:
- projects/chirality-runtime/execution/_Estimates/SCA005_SUCCESSOR/

RuntimeOverrides:
- CHIRALITY_INSTRUCTION_ROOT: /Users/ryan/.codex/worktrees/341e/chirality
- SCOPE: DEL-02-06;DEL-02-07;DEL-02-08;DEL-02-09;DEL-02-10;DEL-02-11;DEL-02-12; historical DEL-04-11 mapped to root::GOV-04-11
- BASIS_OF_ESTIMATE: HISTORICAL
- CURRENCY: EFFORT_HOURS
- ESTIMATES_ROOT: projects/chirality-runtime/execution/_Estimates/SCA005_SUCCESSOR
- DECOMPOSITION_PATH: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md
- DEPENDENCY_SOURCES: execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv
- PRICE_SOURCES: execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/ (all exact historical stream files/method/summary/OWNER_ACCEPTANCE); execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/SCHEDULE_BASIS_POST_PHASE4/OWNER_ACCEPTANCE.md; projects/chirality-runtime/execution/_Decomposition/ approved register, hold map, source contracts and ownership overlay
- OUTPUT_LABEL: SCA005_HISTORICAL_SUCCESSOR
- UPDATE_LATEST_POINTER: FALSE
- FALLBACK_POLICY: STRICT
- ALLOW_MIXED_METHODS: FALSE
- ROUNDING: NONE

Explicit specialization: the approved migration derivative is HISTORICAL effort-hours mapping, not generic currency pricing or a new BOE. Parent HELP_HUMAN confirmed this interpretation and existing R8 inputs. ScopePath is the exact approved estimate output root, which also contains the mandatory local TASK run record; no execution-root run-record target is opened. Keep required skill provenance/QA/artifacts and actual enum/tool checks, but do not pretend unrelated price/rate/BOE prerequisites were satisfied. Report any unsupported method requirement candidly.

Revalidate all eight streams and 46 source line items where present. Exact source figures sum 1012 historical base hours, low560/high1464. Seven runtime streams sum920 base; Root GOV-04-11 carries92. Preserve per-stream ranges and exclusions, with R16-B and R18 later dispositions. No subtraction of migration effort or assumptions about completed feature work; current remaining effort is UNKNOWN unless accepted evidence quantifies it. Held/excluded effort is unknown, not zero. No calendar/staffing/rate/activation/acceptance.

Read approved runtime publication wrappers for actual authority. Source historical snapshots remain immutable. Produce all meaningful standard snapshot artifacts plus exact source-to-successor map and current-remaining flags. Fresh snapshot under declared root, actual TASK pending/final local record there, no _LATEST. Include explicit owner disposition PENDING for new derivative. No production, metadata, Git mutations or delegation. Model GPT-6, exact serving ID unavailable; instruction-asserted role.
