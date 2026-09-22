# SOW half B notes (SOW-043..SOW-084): RUN_D128 R2 extension item 5

Ledger: `SOW_claims.csv`. It has 62 rows covering 42 units, validates against `EXTENSION_INDEX_SOW_B.csv` with 0 errors and 0 warnings, and is sealed (SHA-256 in `RETURN.md`). No run-local keys were needed: no `SOW:REGISTER-n` or `SOW:STATE-n` rows (the reserved range 51–99 is unused).

## 1. Census

| ClaimType | Disposition | Rows |
|---|---|---|
| REQUIREMENT | ALIGNED | 36 |
| REQUIREMENT | PARTIALLY_IMPLEMENTED | 8 |
| REQUIREMENT | IMPLEMENTED_DIFFERENTLY | 8 |
| REQUIREMENT | DOCUMENTED_UNIMPLEMENTED | 3 |
| REQUIREMENT | AUTHORITY_CONFLICT | 2 |
| REQUIREMENT | STALE_SPECIFICATION | 1 |
| EXCLUSION | ALIGNED | 3 |
| EXCLUSION | AUTHORITY_CONFLICT | 1 |

- **Split rate.** 20 of 42 units (48%) are split into `.1`, a live-deliverable mapping row, and `.2`, a code or deferral row. A unit was split whenever its two parts took different dispositions. In 19 of the 20, `.1` is ALIGNED and the finding sits on `.2`. SOW-079 is the exception: both parts are non-ALIGNED.
- **SEE rows:** 0. No normative statement recurs within this half.
- **Other counts.**
  - Confidence: 24 HIGH, 35 MEDIUM, 3 LOW.
  - PostReleaseBasis YES: 3 rows (SOW-047.2, 048.2, 064.2). Each cites the Runtime application-tool hosting that `da95ec194` added.
  - HumanDecisionNeeded:
    - `R4-Q1`: 6 rows (045.2, 050.2, 052.2, 057.2, and ALIGNED rows 068 and 070 by rule 3);
    - `R4`: 2 rows (075.2, 076);
    - `R4-Q2; R4-Q5`: 1 row (044.2);
    - `R4-Q5`: 1 row (061.2);
    - `D-APP-116`: 1 row (059.2);
    - `D-APP-119`: 1 row (084.2);
    - `NO`: the remaining 50 rows.
- **Manager summary tokens.**
  - `NO_LIVE_DELIVERABLE` (2 rows):
    - SOW-079.1: the decomposition names DEL-04-01, but DEL-04-01 `_STATUS.md` records the item as `SCOPE_AMENDMENT_REQUIRED` and its SoW does not cite SOW-079.
    - SOW-080: its only owner, DEL-09-07, was retired by D-APP-127.
  - `NO_CODE_NO_DEFERRAL` (1 row): SOW-084.2, for its organisation-layer part only. The bundled base layer is live.

## 2. Least-confident rows (with alternative readings)

- **SOW-061.2 (LOW), PARTIALLY_IMPLEMENTED.** Codex `contextCompaction` reaches the App only as a generic `codex.notification`. There is no compaction-specific view and no replay check.
  - Alternative: DOCUMENTED_UNIMPLEMENTED with R4-Q1, since only the legacy Pi mapper emits named compaction events.
- **SOW-075.2 (LOW), AUTHORITY_CONFLICT.** The effective Codex home shares the user's `memories` and `sessions/` by reference (CTX SPIKE_DESIGN §3), outside the project checkout. DIRECTIVE §2 ("no hidden project memory") is unamended.
  - Alternative: ALIGNED, if Codex memories count as user-level context rather than project memory.
- **SOW-076 (LOW, OUT), AUTHORITY_CONFLICT.** The live chat panel ships a "Full access" mode (`danger-full-access`, approval `never`) and loads the user's Codex `config.toml`. This crosses the literal boundary. The governing texts point both ways:
  - D-GOV-43 and the amended CONTRACT K-UNTYPED-1 make approval and sandbox the user's choice.
  - PRD non-goals and CONTRACT K-PERM-6/K-SDK-1 are unamended and SDK-worded.
  - Alternative: ALIGNED, reading the boundary as naming only SDK `bypassPermissions` and Claude Code settings.
- **MEDIUM rows that could reasonably go another way:**
  - SOW-050.2: AUTHORITY_CONFLICT versus IMPLEMENTED_DIFFERENTLY. The live path exposes writes and shell from the first turn, against the decomposition's read-first sequencing invariant.
  - SOW-048.2: PARTIALLY_IMPLEMENTED versus ALIGNED at module level. The descriptor contracts are live modules, but the App registers no tools.
  - SOW-052.2: DOCUMENTED_UNIMPLEMENTED versus PARTIALLY_IMPLEMENTED. The live toolkit still collects `maxTurns`, but the Runtime ignores `opts`.
  - SOW-043: ALIGNED. The daemon-shape migration is read as deferred by DEL-05-01-V3-02, whose Root DEL-02-11 gate premise A2 may have changed.

## 3. Register-defect summary

No REGISTER rows. Observations for the manager:

- **The decomposition was never updated after D-GOV-43 / D-APP-127.** Its last change is the SCA-APP-010 Gate-5 application `dbd812a52`. As a result:
  - SOW-080 still reads IN, and its Notes say "F-APP-2/D-APP-97 remain active";
  - OI-003 and OI-007 still carry the DEL-09-07 installer and Root-owned supply;
  - OBJ-008 still lists SOW-080.
- **SOW-080** is recorded as STALE_SPECIFICATION under MR-11. D-APP-127 names DEL-09-07, and the ledger row lies outside the preserved set.
- **SOW-079 mapping.** The decomposition's §8 row for DEL-04-01 and its §9 row name DEL-04-01, but DEL-04-01 does not carry the item. SOW-079.1 is recorded as DOCUMENTED_UNIMPLEMENTED with CARRIER_PROPAGATION.
- **Cross-deliverable, not in this ledger.** DEL-07-03 `_STATUS.md` has no `## Remaining` section. Yet its History (2026-09-05) says DEL-07-03-V3-01 was "retained". This belongs to the PKG-07 ledger.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE, 15 rows: SDK-era mechanisms (canUseTool, hooks, Chirality overlay, Bash and path policy, the tool pool, `maxTurns`) replaced by Codex approval requests and the PolicySelection sandbox pairs.
  - A2_TOPOLOGY, 5 rows: SOW-056.2, 064.2, 075.2, 079.2, 080.
  - SHELL_REDESIGN, 2 rows: SOW-081.2, 084.2.
  - CARRIER_PROPAGATION, 1 row: SOW-079.1.
- **CAUSE2 secondaries:**
  - A2_TOPOLOGY: 044.2, 045.2, 076;
  - CODEX_SOLE_ENGINE: 056.2, 064.2, 075.2, 079.2;
  - DOC_HYGIENE: 079.1.
- **No `OTHER:` tokens used.**
- **Records cited:**
  - GOV: D-APP-127, with D-GOV-43 items 3 and 6 as it records them.
  - CTX:
    - `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/SPIKE_DESIGN.md`: §3 effective home, §4 PolicySelection and delegation, §6 event representation, §7 server requests ("we register none" for dynamic tools), §8, §10;
    - `APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md`, for SOW-079.1;
    - the amended App `docs/CONTRACT.md` K-UNTYPED-1.
- **Searches behind each `NONE_FOUND` DirectionEvidence:**
  - SOW-052.2: searched `_DECISIONS/_REGISTER.md` for "maxTurns / max-turn / max turn" (0 hits) and SPIKE_DESIGN.md (0 hits).
  - SOW-057.2: searched `_REGISTER.md` for "hook" (2 hits, both D-APP-04-era capability lanes and irrelevant) and SPIKE_DESIGN.md (no hook direction).
  - SOW-084.2: searched `_REGISTER.md` for "organisation" (1 hit, D-APP-119, AWAITING_RULING, cited in HumanDecisionNeeded) and SPIKE_DESIGN.md (none).
- **Code searches behind `NONE_FOUND` ImplementationEvidence:** SOW-057.2 (hook callbacks), SOW-080 (launchd installer), SOW-082 (`proposal.offered`, ProposalCard, propose tool), SOW-083 (per-chat delegation policy) and SOW-084.2 (organisation layer). Each search covered `frontend/src`, `frontend/electron` and `chirality-runtime/packages` (execution excluded).
- **Done-declaration context (Q-01..Q-13):** not relied on for any row.
- **D-APP-87** (dual target, domain-first; PENDING_EFFECT) is cited only as `(context)` on the domain rows.

## 5. Method friction

- **What counts as "explicit deferral".** A gated Remaining item (`NOT_SELECTABLE_UNTIL: …`) was read as deliverable text that explicitly defers the work. On that reading:
  - SOW-043, 063, 082 and 083 are ALIGNED;
  - SOW-084's SELECTABLE item DEL-07-01-V3-01 is not a deferral;
  - SOW-081's DEL-02-02-V3-04, whose gates appear landed, is not a deferral either.
  - Proposal: state in §8 whether a gated Remaining item satisfies "explicit deferral", or whether only a ruling or OUT/future-boundary text does.
- **R4-Q1 on ALIGNED rows.** Rule 3 is mechanical, so SOW-068 and SOW-070 cite R4-Q1 even though they are ALIGNED through the DEC-006/OI-005 deferral. Proposal: limit rule 3 to rows whose disposition rests on code.
- **Build-pipeline evidence has no REACH vocabulary.** `package.json` and `frontend/scripts/*.mjs` are not in `REACHABILITY.csv`. They were tagged `REACH=LIVE` as the product build pipeline, with a Note saying so, because `LEGACY_ONLY` plus UNREACHED would wrongly trigger R4-Q1. Proposal: add a `BUILD` reach class, or exempt build configuration from tagging.
- **The authority tier of decomposition rows.** RUN_BASIS §5 lists the decomposition as GOVERNING, yet Ruling D makes its ledger rows audit targets. AUTHORITY_CONFLICT was used only where a ruling contradicts the row's substance (SOW-050, 075, 076), not for mechanism changes (IMPLEMENTED_DIFFERENTLY).
- **The two-part split.** Nearly every non-ALIGNED IN row splits, because the mapping part is almost always ALIGNED. This doubles those rows without adding information. Proposal: make `.1` implicit when it is ALIGNED.

## 6. Effort

- **Files read:** about 25 files or ranges.
  - Rulebook and briefs; the decomposition's §9, §2.2, §11 and §12 ranges; D-APP-127.
  - About 20 deliverable `_STATUS.md` Remaining extracts and grep hits across the SoWs.
  - About 15 code files by grep and short ranges; SPIKE_DESIGN §3–4; the evidence-pack CSVs, read by script.
- **Budget:** the context budget was adequate but not loose.
- **Not done:** no test runs and no installs. Git was not needed beyond one `git log` on the decomposition file.
