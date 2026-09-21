# V shard DEL-10-01: verifier notes (R0 calibration)

- **Shard:** a fresh, evidence-only TASK. Unit DEL-10-01, 43 SELECTION items.
- **Basis:** frozen tree `00115c719`. Git use was limited to read-only `log`/`show`.
- **Output:** `V-DEL-10-01.csv`.
- **Status:** these are verifier readings, not rulings.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 35 | 29 | 2 | 4 |
| b | 7 | 6 | 0 | 1 |
| c | 1 | 1 | 0 | 0 |
| **Total** | 43 | 36 | 2 | 5 |

**REFUTED rows:**

- **CLM-016.1.** CauseTag should be RUNTIME_EXTRACTION, with GOVERNING direction D-APP-73/76/89. The row has UNRECORDED_JUDGMENT.
- **REM-1.** Disposition should be REMAINING_STATE_MISMATCH / A2_TOPOLOGY. The row has ALIGNED.

**CONTESTED rows:** CLM-004.5, CLM-007.1, CLM-026.2, CLM-028.1, CLM-002.

**Clean re-checks:**

- **PostReleaseBasis.** All 43 items say `NO`, and that is correct. None of the files touched by `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a` is cited as evidence.
- **Line citations.** Every SoW line citation resolves at the frozen tree, and so does every code or test line citation that was checked.

## (ii) Systematic patterns

1. **UNRECORDED_JUDGMENT and MR-6 UNKNOWN were set after a search that skipped GOVERNING records.**
   - The worker searched only the CONTEXT sources, or grepped too narrowly, and then declared the direction absent.
   - **CLM-016.1.**
     - The move is recorded by GOVERNING rulings:
       - D-APP-73 (RULED 2026-07-22) extracts the harness to the root runtime.
       - D-APP-76 recognizes the "D-APP-73 prospective rehome" of the D-APP-49 modules.
       - D-APP-89 Option B migrates importers to `@chirality/runtime-contracts` and keeps the facade.
       - D-APP-118 (facade retirement) is AWAITING_RULING.
     - The reverse notes also date the relocation wrongly. It is pre-v3:
       - `8b3643e6c` (2026-07-22) added the mirror.
       - `99fe2edae` (2026-07-23) turned the facade into a re-export.
       - `df7d62308` (2026-09-05) only moved the project folder.
     - The worker suggested RUNTIME_EXTRACTION might apply if a direction record existed. It does exist, and it is GOVERNING, not just CONTEXT.
   - **REM-1.**
     - The row says D-T0-23/D-PEC-56 appear on no App governing surface. That is false:
       - decomposition `DEC-019` (line 628);
       - `docs/harness/reliance_boundary_register.md:150-178`.
     - The register retires the RB-PEC-ADAPTER adapter-service, RBAC, scratch/demo and pilot assertions.
     - It also says D-GOV-43 replaces the one-daemon boundary on the App path, so PEC socket compatibility is not an MVP prerequisite.
     - The worker's own LOW alternative reading was correct.
   - **Convention gap.** `DirectionEvidence` is defined as CONTEXT-only, so a divergence explained by a GOVERNING ruling has no slot.
     - Proposal: allow a GOVERNING citation in `LatestDecision` to defeat UNRECORDED_JUDGMENT.
     - Also require a register-row grep before either tag (UNRECORDED_JUDGMENT, or MR-6 UNKNOWN) is used.

2. **The CauseTag vocabulary overlaps, and the worker applied it inconsistently.**
   - PRE_V3_DRIFT and UNRECORDED_JUDGMENT can both apply to the same row. Examples:
     - **CLM-007.1:** the guard optionality dates from `f4d7deb28` (2026-07-04).
     - **CLM-016.1:** the relocation dates from 2026-07-22.
   - The worker used PRE_V3_DRIFT for CLM-028.1 on that same timing basis, but not for these two.
   - **CLM-007.1** also ignores the D-APP-49 packet's ruled mitigation, which was to mirror the validator. The validator has `required=False` for the status and integration enums (`tools/validation/validate_domain_engine_profile.py:525-526`).
   - Proposal: state a precedence rule, e.g. "mechanism tag > PRE_V3_DRIFT > UNRECORDED_JUDGMENT", or add a separate Mechanism field (worker friction item 1).

3. **AuthorityTier and ClaimType were applied inconsistently.**
   - **CLM-028.1** is a CONTEXT_CLAIM but carries AuthorityTier `LOCAL_DESIGN`. The rule requires `NOT_APPLICABLE`. It is also disposed IMPLEMENTED_DIFFERENTLY, although the skeleton is explicitly illustrative and the code matches CLM-006.
   - **SPEC §18 rows** (CLM-004.1, CLM-014.2) get tier `PRD`, while App `CONTRACT` K-DOMAIN rows get `GOVERNANCE_INVARIANT`.
     - The rulebook does not say whether App `docs/SPEC.md` counts as "SPEC" for GOVERNANCE_INVARIANT.
     - Proposal: say explicitly that App DIRECTIVE/CONTRACT/SPEC/TYPES count.

**Lesser observations:**

- **Staleness versus reachability pull in opposite directions** (CLM-004.1 against CLM-021.4 / CLM-024 / CLM-002).
  - CLM-004.1 is stale because "live" is false in the product.
  - CLM-021.4 and CLM-024 are stale because "not activated" is false in code.
  - Both readings hold only because they measure against different surfaces: CLM-004.1 against product reachability, the others against the ruled code surface. The conventions should name which surface counts.
  - CLM-002's "Current posture: not current implementation" row was left ALIGNED although the analogous CLM-024 wording was marked stale.
- **MR-1 is ambiguous when the assessed guidance line is itself stale** (CLM-026.2: STILL CURRENT versus OVERTAKEN).
- **CLM-004.5 is internally inconsistent.** It is ALIGNED, yet RemainingWork is UNKNOWN and the AssessmentEvidence is STILL CURRENT for a PARTIAL finding.
- **CLM-004.1 confirmed.**
  - Static reachability matches the worker's reading:
    - `read-tools.ts` has one non-test importer, `sdk-options-builder.ts`.
    - `lib/harness/runtime.ts` is imported only from `__tests__`.
    - Neither Runtime packages nor Electron wire `mcp_servers`.
  - A stronger CONTEXT record exists than the plan-final §3.1 the row cites: `V3_DONE_DECLARATION_CANDIDATE` OOS-08 ("Piping integration … remain deferred", PKG-10). It would support V3_RELEASE_SCOPE as an alternative CauseTag.
- **The class c item** (CAP-HARNESS-053 PARTIAL → CLM-016.2) holds. The registry is DEL-10-01's; the completeness and rule-check tools are its siblings'.

## (iii) Effort

- **Files read:** about 25, mostly by grep or line range.
  - Deliverable, 7: SoW in full, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `Dependencies.csv`, `_DEPENDENCIES` (grep), Assessment (grep).
  - Code and tests, 8.
  - Decision records and register, 6.
  - `docs/TYPES`, `docs/PLAN`, `reliance_boundary_register`, the decomposition (grep).
  - Plan-final (grep) and the done-declaration candidate (slice).
- **Git:** about 10 read-only `log`/`show` calls.
- **Context:** not tight.
