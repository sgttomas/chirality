# Source Pack: Skill pack: estimate-prep

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/estimate-prep/BOE_STRUCTURE.md

### BOE Structure — Document Contracts

Companion reference for `skills/estimate-prep/SKILL.md`. Defines the structural contracts for the Basis-of-Estimate artifacts produced by the two phases.

---

#### BOE_Scaffold.md (Phase SCAFFOLD output)

Produced by Phase SCAFFOLD under `{snapshot}/Scaffold/BOE_Scaffold.md`.

##### Minimum contents

- **Per-deliverable table** with columns:
  - `DeliverableID`
  - `Name`
  - `Package`
  - `BASIS_OF_ESTIMATE`
  - `FALLBACK_POLICY`
  - `ALLOW_MIXED`
  - `Substance`
  - `Cost Drivers`
  - `Primary Roles`
- **Package cost ownership hints** (scope items mapped to multiple deliverables)
- **SOW multi-mapping warnings** (double-counting risks)
- Marked `DRAFT — requires human review`

---

#### BASIS_OF_ESTIMATE.md (Phase BOE output)

Produced by Phase BOE as `{snapshot}/BASIS_OF_ESTIMATE.md`.

If a canonical BOE exists for the project, follow its structure. Otherwise, the generated BOE MUST include these 10 sections in order:

1. **Purpose**
2. **Project Context**
3. **Estimation Scope** (in/out; base/options)
4. **Estimation Strategy** (methods, defaults, price source posture)
5. **Per-Deliverable Estimation Plan** (tiers, basis, fallback, mixed methods, cost drivers, ownership rules)
6. **Dependency-Informed Run Sequence** (tiers + chains + gates)
7. **Missing / Weak PRICE_SOURCES Register**
8. **Aggregation Strategy** (rollups; totals; optional evaluation view)
9. **Assumptions and Constraints Log**
10. **Document Control**

##### Section guidance

- **Per-Deliverable Plan (§5):** every deliverable from the decomposition MUST appear. Record cost ownership rules for every package with multi-deliverable scope overlap.
- **Run Sequence (§6):** every deliverable assigned a tier; tier assignments consistent with dependencies; cycles detected and reported in QA + Conflicts.
- **PRICE_SOURCES Register (§7):** identify and prioritize low-confidence items impacting the plan.
- **Assumptions Log (§9):** merge scaffold assumptions + BOE derivations with IDs and impact-if-wrong.

---

#### Run_Context.md (minimum fields — both phases)

Produced at the root of every snapshot folder.

- `RunID` (snapshot folder name)
- `AsOf` (timestamp)
- `Phase` (`SCAFFOLD` | `BOE`)
- `Mode` (`BOOTSTRAP` | `ENRICH`)
- `EXECUTION_ROOT`
- `DECOMPOSITION_PATH`
- `SOURCE_DOCUMENTS` (resolved list)
- `PROJECT_CONTEXT` (full block)
- `CURRENCY`
- `RATE_SCOPE` (SCAFFOLD only)
- `SCAFFOLD_PATH` (BOE only)
- `DEPENDENCY_SOURCES` (BOE only)
- `HUMAN_PRICING` (ENRICH mode only)
- `PRIOR_SNAPSHOT` (ENRICH mode only)
- `CANONICAL_PRICESOURCES_ROOT` (if used)
- `SCHEMA_MODE`
- `EXPORT_BUNDLE`
- `Warnings` (if any)

---

#### Publish_Manifest.md (handoff artifact — human-owned action)

Produced at `{snapshot}/Publish_Manifest.md` at the end of every run. Describes how to publish snapshot outputs to canonical locations — **publication is a human-owned step**.

##### Required contents

- **Snapshot path** (absolute or relative to `{EXECUTION_ROOT}`)
- **Intended canonical destinations** (e.g., `{EXECUTION_ROOT}/_PriceSources/` and `{EXECUTION_ROOT}/BASIS_OF_ESTIMATE.md`)
- **File-by-file copy list**
- **Warning** that publication requires human approval and review

If `Publish_Package/` exists (i.e., `EXPORT_BUNDLE=MANIFEST_AND_PACKAGE`), the manifest should point to it.

##### Human decision rights boundary

The manifest is a proposal. The skill MUST NOT:
- Copy files into `_PriceSources/` or other canonical locations.
- Create or modify `BASIS_OF_ESTIMATE.md` outside the snapshot folder.
- Commit to git or push to any remote.
- Take any irreversible publication action.

## Component: skills/estimate-prep/BRIEF_SCHEMA.md

### BRIEF_SCHEMA — estimate-prep

This skill runs in exactly ONE phase per invocation, selected by the `PHASE` brief parameter. The human gate is external: a human reviews `SCAFFOLD` output, then re-invokes with `PHASE=BOE`.

#### PHASE parameter (required, both phases)

| Value | Meaning |
|---|---|
| `SCAFFOLD` | Generate parametric pricing baseline + BOE scaffold for human review |
| `BOE` | Consume approved scaffold + dependency evidence; produce full `BASIS_OF_ESTIMATE.md` |

Any other value produces `RUN_STATUS=FAILED_INPUTS`. A single run MUST NOT span both phases.

#### Common required fields (both phases)

| Field | Type / values | Notes |
|---|---|---|
| `TaskSkill` | `estimate-prep` | Must match skill folder name |
| `PHASE` | `SCAFFOLD` \| `BOE` | Validated enum |
| `EXECUTION_ROOT` | Absolute path | Root of current execution/workspace |
| `DECOMPOSITION_PATH` | Absolute path | Latest decomposition markdown (PROJECT_DECOMP or SOFTWARE_DECOMP) |
| `SOURCE_DOCUMENTS` | Path or list of paths | RFP, addenda, specs, reference reports |
| `CURRENCY` | ISO-like code | e.g., `USD`, `CAD` |
| `PROJECT_CONTEXT` | Structured block | See block schema below |

##### `PROJECT_CONTEXT` block

| Sub-field | Required | Example |
|---|---|---|
| `Location` | Yes | `Alberta, Canada — Penhold/Red Deer` |
| `BaseYear` | Yes | `2024` |
| `ProjectType` | Yes | `Municipal Public Services Building` |
| `ProcurementModel` | Yes | `Design-Build`, `Design-Bid-Build`, `CM at Risk` |
| `EstimatedValue` | No | `$12M-$15M CAD` |
| `AdditionalContext` | No | `LEED target`, `phased construction`, `occupied renovation` |

#### Common optional fields (both phases)

| Field | Default | Allowed values |
|---|---|---|
| `OUTPUT_LABEL` | `AUTO` | Short label for snapshot folder naming |
| `SECONDARY_SOURCES` | — | Path(s) to secondary reference documents |
| `CANONICAL_PRICESOURCES_ROOT` | — | Path to existing canonical pricing library (e.g., `{EXECUTION_ROOT}/_PriceSources/`) |
| `SCHEMA_MODE` | `AUTO_FROM_CANONICAL` | `AUTO_FROM_CANONICAL`, `DEFAULT_COMPAT` |
| `EXPORT_BUNDLE` | `MANIFEST_ONLY` | `MANIFEST_ONLY`, `MANIFEST_AND_PACKAGE` |

#### PHASE=SCAFFOLD — additional fields

##### Optional (SCAFFOLD)

| Field | Default | Notes |
|---|---|---|
| `MODE` | `BOOTSTRAP` | `BOOTSTRAP` or `ENRICH` |
| `PRIOR_SNAPSHOT` | — | **Required if `MODE=ENRICH`** (unless `CANONICAL_PRICESOURCES_ROOT` is provided instead) |
| `HUMAN_PRICING` | — | Path(s) to human-provided pricing: quotes, rate tables, historical data, vendor proposals (CSV, markdown, PDF, structured text) |
| `RATE_SCOPE` | `PRODUCTION_ONLY` | `PRODUCTION_ONLY` or `PRODUCTION_AND_CONSTRUCTION` |
| `DISCIPLINE_HINTS` | — | Override or supplement discipline detection from decomposition |

#### PHASE=BOE — additional fields

##### Required (BOE)

| Field | Notes |
|---|---|
| `SCAFFOLD_PATH` | Path to approved SCAFFOLD snapshot (may have been modified by human after Phase SCAFFOLD) |

##### Optional (BOE)

| Field | Default | Notes |
|---|---|---|
| `DEPENDENCY_SOURCES` | `AUTO` | `AUTO` (reads per-deliverable `Dependencies.csv`) or explicit path(s) |
| `EVALUATION_CRITERIA` | — | Path to or structured block of evaluation criteria with point allocations |
| `AGGREGATION_HINTS` | — | Human-specified aggregation preferences |

#### Write boundary (both phases)

- Write target: `{EXECUTION_ROOT}/_EstimatePrep/` and nothing outside it.
- Each run creates a new immutable snapshot folder:
  - SCAFFOLD: `EPREP_SCAFFOLD_{LABEL}_{DATE}_{TIME}/`
  - BOE: `EPREP_BOE_{LABEL}_{DATE}_{TIME}/`

The brief SHOULD declare:

```yaml
AllowedWriteTargets:
  - "{EXECUTION_ROOT}/_EstimatePrep/"
```

#### Example brief — PHASE=SCAFFOLD (BOOTSTRAP)

```markdown
PURPOSE: Generate parametric pricing baseline + BOE scaffold for Penhold MSB proposal
RequestedBy: ORCHESTRATOR
ScopePath: {EXECUTION_ROOT}
TaskSkill: estimate-prep

AllowedWriteTargets:
  - "{EXECUTION_ROOT}/_EstimatePrep/"

RuntimeOverrides:
  PHASE: SCAFFOLD
  MODE: BOOTSTRAP
  EXECUTION_ROOT: /abs/path/to/Penhold_MSB_Proposal
  DECOMPOSITION_PATH: /abs/path/to/Penhold_MSB_Proposal/_Decomposition/LATEST.md
  SOURCE_DOCUMENTS:
    - /abs/path/to/RFP.pdf
    - /abs/path/to/Addendum_01.pdf
  CURRENCY: CAD
  PROJECT_CONTEXT:
    Location: "Alberta, Canada — Penhold/Red Deer"
    BaseYear: 2024
    ProjectType: "Municipal Public Services Building"
    ProcurementModel: "Design-Build"
    EstimatedValue: "$12M-$15M CAD"
  RATE_SCOPE: PRODUCTION_AND_CONSTRUCTION
  SCHEMA_MODE: AUTO_FROM_CANONICAL
  CANONICAL_PRICESOURCES_ROOT: "{EXECUTION_ROOT}/_PriceSources/"
  EXPORT_BUNDLE: MANIFEST_ONLY
  OUTPUT_LABEL: "Penhold_MSB"
```

#### Example brief — PHASE=SCAFFOLD (ENRICH)

```markdown
PURPOSE: Enrich SCAFFOLD snapshot with vendor quotes received since last run
RequestedBy: ESTIMATING_LEAD
TaskSkill: estimate-prep

AllowedWriteTargets:
  - "{EXECUTION_ROOT}/_EstimatePrep/"

RuntimeOverrides:
  PHASE: SCAFFOLD
  MODE: ENRICH
  EXECUTION_ROOT: /abs/path/to/Penhold_MSB_Proposal
  PRIOR_SNAPSHOT: "{EXECUTION_ROOT}/_EstimatePrep/EPREP_SCAFFOLD_Penhold_MSB_2024-03-15_0930/"
  DECOMPOSITION_PATH: /abs/path/to/Penhold_MSB_Proposal/_Decomposition/LATEST.md
  SOURCE_DOCUMENTS:
    - /abs/path/to/RFP.pdf
  HUMAN_PRICING:
    - /abs/path/to/quotes/mechanical_quote_acme.pdf
    - /abs/path/to/quotes/electrical_rates_q1_2024.csv
  CURRENCY: CAD
  PROJECT_CONTEXT:
    Location: "Alberta, Canada — Penhold/Red Deer"
    BaseYear: 2024
    ProjectType: "Municipal Public Services Building"
    ProcurementModel: "Design-Build"
  RATE_SCOPE: PRODUCTION_AND_CONSTRUCTION
  OUTPUT_LABEL: "Penhold_MSB_v2"
```

#### Example brief — PHASE=BOE

```markdown
PURPOSE: Generate full BASIS_OF_ESTIMATE.md from approved SCAFFOLD snapshot
RequestedBy: ESTIMATING_LEAD
TaskSkill: estimate-prep

AllowedWriteTargets:
  - "{EXECUTION_ROOT}/_EstimatePrep/"

RuntimeOverrides:
  PHASE: BOE
  EXECUTION_ROOT: /abs/path/to/Penhold_MSB_Proposal
  SCAFFOLD_PATH: "{EXECUTION_ROOT}/_EstimatePrep/EPREP_SCAFFOLD_Penhold_MSB_v2_2024-03-22_1430/"
  DECOMPOSITION_PATH: /abs/path/to/Penhold_MSB_Proposal/_Decomposition/LATEST.md
  SOURCE_DOCUMENTS:
    - /abs/path/to/RFP.pdf
  CURRENCY: CAD
  PROJECT_CONTEXT:
    Location: "Alberta, Canada — Penhold/Red Deer"
    BaseYear: 2024
    ProjectType: "Municipal Public Services Building"
    ProcurementModel: "Design-Build"
  DEPENDENCY_SOURCES: AUTO
  EVALUATION_CRITERIA: /abs/path/to/RFP_Section5_Evaluation.md
  EXPORT_BUNDLE: MANIFEST_AND_PACKAGE
  OUTPUT_LABEL: "Penhold_MSB_BOE_v1"
```

#### Notes

- `SCHEMA_MODE=AUTO_FROM_CANONICAL` + `CANONICAL_PRICESOURCES_ROOT` produces output CSVs whose headers match the canonical library exactly. Prefer this mode when a canonical `_PriceSources/` library exists.
- `EXPORT_BUNDLE=MANIFEST_AND_PACKAGE` writes an additional `Publish_Package/` subfolder inside the snapshot — this is still inside the write quarantine; human publication to canonical locations remains a separate approved step.
- All resolved defaults and chosen paths are recorded in the snapshot `Run_Context.md`.
- `PROJECT_CONTEXT` can be inlined in the brief (as shown) or provided as a path to a structured file — consult the invoker's brief conventions.

## Component: skills/estimate-prep/INDEX_MD_CONTRACT.md

### PriceSources/INDEX.md Contract (Phase SCAFFOLD)

Companion reference for `skills/estimate-prep/SKILL.md`. Defines the 7-section contract for `{snapshot}/PriceSources/INDEX.md`.

---

#### Generation sequence

1. Generate the file inventory portion using `tools/reporting/generate_index_md.sh {snapshot}/PriceSources/`.
2. Augment with the 7 required sections listed below.

---

#### Required sections

##### 1. Header block

Must include:
- `execution root`
- `BOE path`
- `currency`
- `base year`
- `region`
- `prepared date`
- `status`

##### 2. Data quality statement

With confidence level definitions aligned to ESTIMATING accuracy expectations:

| Confidence | Meaning | Accuracy |
|-----------|---------|----------|
| HIGH | Confirmed parameter or fixed allowance | Exact |
| MEDIUM | Parametric rate or typical effort estimate | +/-20-30% |
| LOW | Allowance or rough parametric | +/-30-50% |

##### 3. File inventory table

Columns:
- file name
- item count
- primary consumer / used-by

##### 4. PS-ID → file mapping

BOE price-source IDs mapped to files and key items.

##### 5. ESTIMATING run configuration

Three subsections:

- **Deliverable-to-Package mapping** table (Package → Deliverables)
- **Per-package `PRICE_SOURCES` mapping** — for each package, list the literal file paths ESTIMATING should load. Differentiate between:
  - production-only deliverables (staff rates + LOE + parameters)
  - dual-nature deliverables that also embed construction pricing (e.g., Schedule A/B)
- **ESTIMATING usage guidance** — include verbatim:
  > "use `RecommendedRate` as point estimate; flag `Confidence=LOW` items; record `Basis` in Detail.csv Method column."

##### 6. Open issues table

Issues affecting PRICE_SOURCES with impact and status.

##### 7. Gaps table

Items requiring parametric estimation or future quotes, with workaround.

---

#### Relationship to Detail.csv

The ESTIMATING agent consumes this INDEX.md to:
1. Locate `PRICE_SOURCES` file paths per package.
2. Apply confidence-based risk flags.
3. Record `Basis` values in `Detail.csv` rows.

Changes to INDEX.md structure impact ESTIMATING's Detail.csv generation.

## Component: skills/estimate-prep/QA_CHECKS.md

### QA_CHECKS — estimate-prep

Invariants and quality gates. These apply to **both** phases unless explicitly marked `SCAFFOLD only` or `BOE only`.

#### Universal invariants (both phases)

| # | Check | Validation |
|---|---|---|
| S1 | Write quarantine respected | No files created or modified outside `{EXECUTION_ROOT}/_EstimatePrep/` |
| S2 | Snapshot created | A new snapshot folder exists for the run, even if the run fails |
| S3 | Phase validated | `PHASE` is present and equals `SCAFFOLD` or `BOE`; invalid/missing = `RUN_STATUS=FAILED_INPUTS` |
| S3b | Single phase per run | Run did not span both phases; human gate between SCAFFOLD and BOE preserved |
| S10 | Status reporting | `QA_Report.md` declares `RUN_STATUS` = `OK` \| `WARNINGS` \| `FAILED_INPUTS` |
| S11 | Handoff artifacts | `Publish_Manifest.md` exists and references the run outputs |

#### Required artifacts per phase

##### SCAFFOLD — required files

| Artifact | Required |
|---|---|
| `Run_Context.md` | Yes |
| `QA_Report.md` | Yes |
| `Source_Index.md` | Yes |
| `Confidence_Summary.md` | Yes |
| `PriceSources/INDEX.md` | Yes |
| `Scaffold/BOE_Scaffold.md` | Yes |
| At least one pricing CSV appropriate to `RATE_SCOPE` | Yes |
| `Publish_Manifest.md` | Yes |
| `Override_Log.csv` | If `MODE=ENRICH` |
| `Conflicts.csv` | If conflicts detected |
| `Publish_Package/` | If `EXPORT_BUNDLE=MANIFEST_AND_PACKAGE` |

##### BOE — required files

| Artifact | Required |
|---|---|
| `Run_Context.md` | Yes |
| `QA_Report.md` | Yes |
| `Source_Index.md` | Yes |
| `BASIS_OF_ESTIMATE.md` | Yes |
| `Tier_Analysis.md` | Yes |
| `Decision_Log.md` | Yes |
| `Assumptions_Log.md` | Yes |
| `Publish_Manifest.md` | Yes |
| `Conflicts.csv` | If dependency cycles or contradictions detected |
| `Publish_Package/` | If `EXPORT_BUNDLE=MANIFEST_AND_PACKAGE` |

#### CSV schema integrity (SCAFFOLD only)

| # | Check | Requirement |
|---|---|---|
| S5a | Column names + order | Every generated CSV matches the canonical schema family (or the canonical file discovered via `AUTO_FROM_CANONICAL`) exactly — no invented columns |
| S5b | Key fields non-empty | No empty `ItemID`, `ParameterID`, `RoleID`, `TradeID`, or `DeliverableID` values |
| S5c | Recommended within range | For files with min/max/recommended columns, `RecommendedRate` (or `RecommendedPrice` / `RecommendedPercent`) MUST fall within `[Min, Max]` unless `Notes` provides explicit justification |
| S5d | No column additions | No columns may be added beyond what the canonical schema specifies |

#### Provenance tracking (SCAFFOLD only; schema-family-aware)

| # | Check | Requirement |
|---|---|---|
| S6a | Rate/pricing files (Families 1-7) | Every row has non-empty `Basis` (canonical enum or ENRICH addition) and non-empty `Confidence` (`HIGH`, `MEDIUM`, `LOW`, `N/A`) |
| S6b | Project parameters (Family 8) | Every row has non-empty `Source` (canonical enum) and non-empty `Confidence` |
| S6c | Level of effort (Family 9) | Every row has non-empty `Basis`. **No `Confidence` column exists; do not require or generate one** |
| S6d | Parametric defaults | Parametric values carry `Confidence=MEDIUM` or `LOW` with `Basis=PARAMETRIC`, never `HIGH` |
| S6e | `HIGH` confidence discipline | `HIGH` confidence values are traceable to a vendor quote, human confirmation, or source document — not to parametric defaults |

##### Canonical enum reference

| Context | Column | Canonical values | ENRICH additions |
|---|---|---|---|
| Rate/pricing files (Families 1-7) | `Basis` | `MARKET`, `PARAMETRIC`, `ALLOWANCE`, `N/A` | `QUOTE`, `HUMAN_PROVIDED`, `HUMAN_CONFIRMED` |
| Project parameters (Family 8) | `Source` | `ASSUMPTION`, `DESIGN_BASIS`, `CONFIRMED`, `DERIVED`, `PARAMETRIC` | `HUMAN_PROVIDED` |
| Level of effort (Family 9) | `Basis` | `PARAMETRIC` | `MARKET`, `HUMAN_PROVIDED` |

Values outside these enums require explicit justification in Notes or are treated as `FAILED_INPUTS`.

#### Override logging (SCAFFOLD + MODE=ENRICH only)

| # | Check | Requirement |
|---|---|---|
| S7a | Override log exists | `Override_Log.csv` is present in the snapshot |
| S7b | Coverage complete | Every overridden value is recorded in `Override_Log.csv` |
| S7c | Columns present | `OverrideID`, `File`, `Key`, `Field`, `PriorValue`, `PriorConfidence`, `PriorBasis` (or `PriorSource`), `NewValue`, `NewConfidence`, `NewBasis` (or `NewSource`), `HumanSource`, `Notes` |
| S7d | No silent `HIGH` upgrades | Overrides that change a `HIGH`-confidence value require human-source documentation |

#### BOE completeness (BOE only)

| # | Check | Requirement |
|---|---|---|
| S8a | Deliverable coverage | Every deliverable in the decomposition appears in the per-deliverable estimation plan |
| S8b | Cost ownership rules | Cost ownership rules exist for every package with multi-deliverable scope overlap |
| S8c | Run sequence produced | Canonical run sequence (tiers + within-tier parallelism + chains + gates) is present |
| S8d | Aggregation strategy | Rollups from deliverables to packages to project totals are defined |
| S8e | BOE sections present | If no canonical BOE format exists, the generated BOE includes all 10 required sections |

#### Tier sequencing validity (BOE only)

| # | Check | Requirement |
|---|---|---|
| S9a | Tier assignment | Every deliverable is assigned a tier (T0, T1, ...) |
| S9b | Dependency consistency | Tier assignments are consistent with the dependency DAG |
| S9c | Cycle detection | Cycles are detected and reported in `QA_Report.md` AND `Conflicts.csv` |
| S9d | Dependencies unmodified | Dependency registers are read-only inputs; no modifications |

#### Conflict surfacing (both phases)

- Conflicts MUST be surfaced in `Conflicts.csv`, not silently resolved.
- Conflict triggers:
  - Two or more human sources disagree for the same key
  - Canonical schema discovery fails / mismatches
  - Required inputs imply contradictory interpretations
  - Dependency cycles (BOE only)
- `Conflicts.csv` columns: `ConflictID`, `Key`, `Description`, `Contenders`, `ProposedAuthority` (optional PROPOSAL), `HumanRuling` (TBD until decided), `Notes`.
- `HumanRuling` remains `TBD` in every generated row — the skill does not fill this field.

#### Human decision rights (both phases)

The skill MUST NOT unilaterally decide any of the following. If any arise, flag them and halt the relevant step:

- Accept or issue the BOE strategy / publish to canonical locations
- Resolve conflicts between disagreeing sources
- Approve overrides that would change a `HIGH`-confidence value
- Make scope boundary decisions (in/out; base vs option vs alternate)
- Execute any irreversible publication action (git commit/push; copy into `_PriceSources/`)

Any such decisions surfaced during a run are recorded as proposals in the relevant log (`Decision_Log.md`, `Conflicts.csv`) with `HumanRuling=TBD`.

#### Failure reporting

| Status | Condition |
|---|---|
| `FAILED_INPUTS` | `PHASE` missing/invalid, required inputs missing, required inputs malformed, or single-run-spans-both-phases detected |
| `WARNINGS` | Run completed with surfaced conflicts, low-confidence items requiring attention, partial coverage, or schema discovery warnings |
| `OK` | Run completed with no warnings, no conflicts, and all required artifacts present |

`QA_Report.md` MUST declare exactly one `RUN_STATUS` value.

#### Success case — SCAFFOLD

A clean SCAFFOLD run reports:

- `RUN_STATUS=OK`
- Snapshot folder path
- Pricing files generated (file count + row counts)
- Confidence distribution summary
- BOE scaffold file path
- `Publish_Manifest.md` present
- No conflicts, no overrides requiring human ruling (or explicit statement of none)

#### Success case — BOE

A clean BOE run reports:

- `RUN_STATUS=OK`
- Snapshot folder path
- Deliverable count + tier distribution
- Cycle detection result (none, or listed)
- `BASIS_OF_ESTIMATE.md` path
- `Publish_Manifest.md` present
- Human modifications between scaffold snapshots logged in `Decision_Log.md`

#### Evidence and logs required per run

| Log | Purpose |
|---|---|
| `Run_Context.md` | All resolved defaults, chosen paths, phase, mode |
| `Decision_Log.md` | Defaults applied, methods used, human modifications logged |
| `Assumptions_Log.md` | Explicit assumptions with IDs and impact-if-wrong |
| `Source_Index.md` | Source document index |
| `Confidence_Summary.md` (SCAFFOLD) | Per-file confidence distribution |
| `Override_Log.csv` (SCAFFOLD + ENRICH) | Every override with before/after |
| `Conflicts.csv` (when needed) | Unresolved conflicts with proposed authority (human ruling TBD) |

## Component: skills/estimate-prep/SCHEMA_ANNEX.md

### Schema Annex — Canonical CSV Schemas

Companion reference for `skills/estimate-prep/SKILL.md`. The following 9 schema families cover all 18 canonical CSV files in the `_PriceSources/` library. Headers are listed in exact column order as observed on disk.

Hardened against the canonical `_PriceSources/` library **as of 2026-02-18**.

---

#### Family 1 — Standard Unit-Rate (9 files)

**Header:** `ItemID,Category,Description,Unit,RateMin,RateMax,RecommendedRate,Basis,Confidence,Notes`

| File | ID Prefix | Scope |
|------|-----------|-------|
| `Structural_Concrete_Rates.csv` | SC-xx | Concrete, formwork, rebar, structural steel, foundations |
| `Building_Envelope_Rates.csv` | BE-xx | Wall/roof panels, cladding, insulation, glazing, doors |
| `Mechanical_System_Rates.csv` | MS-xx | HVAC, plumbing, fire protection, exhaust |
| `Electrical_System_Rates.csv` | ES-xx | Power, lighting, telecom, fire alarm, solar-ready |
| `Earthwork_Civil_Rates.csv` | EC-xx | Clearing, excavation, fill, compaction, drainage |
| `Paving_Surfacing_Rates.csv` | PS-xx | Asphalt, aggregate, concrete aprons, curbs |
| `Underground_Utility_Rates.csv` | UU-xx | Water, sewer, gas, power, telecom; tie-in allowances |
| `Fees_Permits_Insurance.csv` | FP-xx | Bonds, insurance, permits, utility connections, environmental fees |
| `Interior_Architectural_Rates.csv` | IA-xx | Partitions, ceilings, flooring, paint, accessibility, signage, millwork, specialties |

**Observed `Basis` values:** `MARKET`, `PARAMETRIC`, `ALLOWANCE`, `N/A`
**Observed `Confidence` values:** `HIGH`, `MEDIUM`, `LOW`, `N/A`

**ESTIMATING guidance:** Use `RecommendedRate` as point estimate. Record `RateMin`/`RateMax` for risk analysis. Flag `Confidence=LOW` items for future vendor quote replacement.

---

#### Family 2 — Equipment Pricing (1 file)

**Header:** `ItemID,Category,Description,Unit,PriceMin,PriceMax,RecommendedPrice,Quantity_Assumed,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Equipment_Pricing.csv` | EQ-xx |

**Notes:** Uses `Price*` columns (not `Rate*`). `Quantity_Assumed` is present and may be blank for lump-sum items.

---

#### Family 3 — Optional Items Pricing (1 file)

**Header:** `ItemID,Category,Description,Unit,PriceMin,PriceMax,RecommendedPrice,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Optional_Items_Pricing.csv` | OPT-xx |

**Notes:** Uses `Price*` columns (not `Rate*`). **No `Quantity_Assumed` column** (unlike Equipment_Pricing). Options include base scope, alternates, and items pending resolution (e.g., OPT-18 = FF&E per OI-004).

---

#### Family 4 — Professional Staff Rates (1 file)

**Header:** `RoleID,Role,Category,HourlyRate_CAD,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Professional_Staff_Rates.csv` | R-xx |

**Notes:** Single rate per role — **no min/max/recommended pattern**. Column is `Role` (not `RoleName`). `Category` groups roles (e.g., `Design`, `Management`, `Construction`, `Admin`, `Specialty`). Currency is embedded in the column name (`HourlyRate_CAD`).

---

#### Family 5 — Construction Labour Rates (1 file)

**Header:** `TradeID,Trade,HourlyRate_CAD,BurdenMultiplier,FullyBurdenedRate_CAD,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Construction_Labour_Rates.csv` | T-xx |

**Notes:** Single rate with burden multiplier → fully burdened rate. No min/max pattern. ID column is `TradeID` (not `ItemID`).

---

#### Family 6 — Professional Design Fees (1 file)

**Header:** `ItemID,Discipline,Description,FeePercentMin,FeePercentMax,RecommendedPercent,FeeBase,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Professional_Design_Fees.csv` | DF-xx |

**Notes:** Uses `Discipline` (not `Category`). Fee percent columns use min/max/recommended pattern. `FeeBase` indicates the basis of the percentage (e.g., `construction_value`). Some items (DF-06/07/08) use `lump_sum` in percent fields when the fee is a fixed amount rather than a percentage.

---

#### Family 7 — Parametric Building Rates (1 file)

**Header:** `ItemID,BuildingType,Description,Unit,RateMin,RateMax,RecommendedRate,Basis,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Parametric_Building_Rates.csv` | PB-xx |

**Notes:** Uses `BuildingType` (not `Category`). Otherwise follows the standard unit-rate column pattern. Used for parametric cross-checks and fallback estimation.

---

#### Family 8 — Project Parameters (1 file)

**Header:** `ParameterID,Category,Parameter,Value,Unit,Source,Confidence,Notes`

| File | ID Prefix |
|------|-----------|
| `Assumed_Project_Parameters.csv` | PP-xx |

**Notes:** Uses `Source` column (**not** `Basis`). The `Source` enum indicates how the parameter was obtained. No rate columns — each parameter is a single `Value`.

**Observed `Source` values:** `ASSUMPTION`, `DESIGN_BASIS`, `CONFIRMED`, `DERIVED`, `PARAMETRIC`
**Observed `Confidence` values:** `HIGH`, `MEDIUM`, `LOW`

---

#### Family 9 — Level of Effort (2 files)

**Header:** `Execution,DeliverableID,DeliverableName,RoleID,Role,EstimatedHours,Basis,Notes`

| File | Scope |
|------|-------|
| `Proposal_Level_of_Effort.csv` | Multi-execution shared file (filter by `Execution` column) |
| `Level_of_Effort.csv` | Execution-specific file (single execution) |

**Notes:** **No `Confidence` column.** Provenance is conveyed via `Basis` alone. All columns are required — `Execution`, `DeliverableName`, and `Role` are NOT optional. `Basis` values observed: `PARAMETRIC`.

---

#### Basis and Source enum reference

| Context | Column | Observed canonical values | ENRICH additions |
|---------|--------|--------------------------|------------------|
| Rate/pricing files (Families 1-7) | `Basis` | `MARKET`, `PARAMETRIC`, `ALLOWANCE`, `N/A` | `QUOTE`, `HUMAN_PROVIDED`, `HUMAN_CONFIRMED` |
| Project parameters (Family 8) | `Source` | `ASSUMPTION`, `DESIGN_BASIS`, `CONFIRMED`, `DERIVED`, `PARAMETRIC` | `HUMAN_PROVIDED` |
| Level of effort (Family 9) | `Basis` | `PARAMETRIC` | `MARKET`, `HUMAN_PROVIDED` |

---

#### Confidence level definitions

| Confidence | Meaning | Typical Source |
|-----------|---------|----------------|
| `HIGH` | Human-confirmed, vendor-quoted, or source-document-derived | Vendor quotes, confirmed rate tables, RFP requirements |
| `MEDIUM` | Parametric market rate or comparable-project benchmark | Market data, industry benchmarks, comparable project data |
| `LOW` | Allowance or assumption-based placeholder | Rules of thumb, unvalidated allowances |

---

#### Override_Log.csv schema (ENRICH mode)

Minimum columns:
- `OverrideID`
- `File`
- `Key`
- `Field`
- `PriorValue`
- `PriorConfidence`
- `PriorBasis` (or `PriorSource` for Family 8 files)
- `NewValue`
- `NewConfidence`
- `NewBasis` (or `NewSource` for Family 8 files)
- `HumanSource`
- `Notes`

---

#### Conflicts.csv schema (when needed)

- `ConflictID`
- `Key`
- `Description`
- `Contenders` *(paths/refs; include values where possible)*
- `ProposedAuthority` *(PROPOSAL; optional)*
- `HumanRuling` *(TBD until decided)*
- `Notes`

## Component: skills/estimate-prep/SKILL.md

---
name: estimate-prep
description: Generates estimation input package (pricing library, LOE, project parameters, BOE) via two-phase run with PHASE=SCAFFOLD|BOE modes and a human gate between invocations.
compatibility: Chirality TASK; two-phase invocation pattern (human gate BETWEEN runs, not inside); writes to tool root _EstimatePrep/
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — estimate-prep

#### Purpose

Generate the complete input package consumed by ESTIMATING agents: pricing libraries, effort matrices, project parameter assumptions, and the Basis of Estimate (BOE).

This skill runs in two phases, invoked separately with a human gate between:

1. **SCAFFOLD** — generates a parametric pricing baseline + a BOE scaffold for human review.
2. **BOE** — consumes the approved scaffold + dependency evidence to produce the full `BASIS_OF_ESTIMATE.md` with tier sequencing, cost ownership rules, and aggregation strategy.

Each invocation runs exactly ONE phase, selected by the `PHASE` brief parameter. The human gate is external: a human reviews SCAFFOLD output, then re-invokes the skill with `PHASE=BOE`.

**Non-goal:** this skill MUST NOT compute or publish project totals, bid prices, or line-item estimates. It prepares inputs; ESTIMATING produces estimates.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

#### Phase parameter — single-run discipline

The `PHASE` parameter determines which pipeline executes. A single invocation runs exactly one phase:

| PHASE | Input expectation | Primary output |
|---|---|---|
| `SCAFFOLD` | Decomposition + source documents + project context (+ optional `HUMAN_PRICING` if `MODE=ENRICH`) | Pricing library CSVs + `PriceSources/INDEX.md` + `Scaffold/BOE_Scaffold.md` |
| `BOE` | Approved `SCAFFOLD_PATH` + dependency evidence | Full `BASIS_OF_ESTIMATE.md` + `Tier_Analysis.md` |

**Critical invariant:** a single run MUST NOT span both phases — the human gate between them is a non-negotiable decision point. If a brief requests both phases in one run, halt with `FAILED_INPUTS`.

#### Inputs

##### Common (both phases)

Required:
- `EXECUTION_ROOT` — root of the current execution/workspace
- `PHASE` — `SCAFFOLD` | `BOE` (validated enum; invalid = `FAILED_INPUTS`)
- `DECOMPOSITION_PATH` — path to the latest decomposition markdown (PROJECT_DECOMP or SOFTWARE_DECOMP)
- `SOURCE_DOCUMENTS` — path(s) to source documents (RFP, addenda, specs, reference reports)
- `CURRENCY` — ISO-like code (e.g., `USD`, `CAD`)
- `PROJECT_CONTEXT` — structured block (`Location`, `BaseYear`, `ProjectType`, `ProcurementModel`; `EstimatedValue` optional; `AdditionalContext` optional)

Optional:
- `OUTPUT_LABEL` — short label for snapshot naming (default `AUTO`)
- `SECONDARY_SOURCES` — path(s) to secondary reference documents
- `CANONICAL_PRICESOURCES_ROOT` — path to canonical pricing library (e.g., `{EXECUTION_ROOT}/_PriceSources/`) used for schema discovery and/or as ENRICH input
- `SCHEMA_MODE` — `AUTO_FROM_CANONICAL` (default) | `DEFAULT_COMPAT`
- `EXPORT_BUNDLE` — `MANIFEST_ONLY` (default) | `MANIFEST_AND_PACKAGE`

##### SCAFFOLD-specific

- `MODE` — `BOOTSTRAP` (default) | `ENRICH`
- `PRIOR_SNAPSHOT` — required if `MODE=ENRICH` (or use `CANONICAL_PRICESOURCES_ROOT`)
- `HUMAN_PRICING` — path(s) to human-provided pricing (quotes, rate tables, historical data, vendor proposals)
- `RATE_SCOPE` — `PRODUCTION_ONLY` (default) | `PRODUCTION_AND_CONSTRUCTION`
- `DISCIPLINE_HINTS` — override/supplement discipline detection from decomposition

##### BOE-specific

Required:
- `SCAFFOLD_PATH` — path to approved SCAFFOLD snapshot (may have been modified by human after Phase SCAFFOLD)

Optional:
- `DEPENDENCY_SOURCES` — `AUTO` (default; reads per-deliverable `Dependencies.csv`) or explicit path(s) to dependency registers
- `EVALUATION_CRITERIA` — path to or structured block of evaluation criteria with point allocations
- `AGGREGATION_HINTS` — human-specified aggregation preferences

All resolved defaults and chosen paths MUST be recorded in the snapshot `Run_Context.md`.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `PHASE` | Which pipeline to run | **Required** | `SCAFFOLD`, `BOE` |
| `MODE` | SCAFFOLD only: baseline vs enrichment | `BOOTSTRAP` | `BOOTSTRAP`, `ENRICH` |
| `RATE_SCOPE` | SCAFFOLD only: which rate files to generate | `PRODUCTION_ONLY` | `PRODUCTION_ONLY`, `PRODUCTION_AND_CONSTRUCTION` |
| `SCHEMA_MODE` | Whether to auto-match canonical file headers | `AUTO_FROM_CANONICAL` | `AUTO_FROM_CANONICAL`, `DEFAULT_COMPAT` |
| `EXPORT_BUNDLE` | Manifest-only vs manifest + copy-ready package | `MANIFEST_ONLY` | `MANIFEST_ONLY`, `MANIFEST_AND_PACKAGE` |
| `DEPENDENCY_SOURCES` | BOE only: dependency source policy | `AUTO` | `AUTO` or explicit path(s) |
| `OUTPUT_LABEL` | Label for snapshot folder naming | `AUTO` | free-form short token |

#### Tool usage

- The `allowed-tools` frontmatter field is intentionally omitted. The skill dispatches several utility scripts under `tools/` (enum validation, snapshot scaffolding, INDEX generation) but their invocation is guided operationally, not enforced through the TASK-consumed allowed-tools contract.
- Preferred utility scripts (invoked by the agent during the run when available):
  - `tools/validation/validate_enum.py` — validates `PHASE` input.
  - `tools/scaffolding/scaffold_tool_root.sh` — creates `_EstimatePrep/` tool root.
  - `tools/scaffolding/create_snapshot_folder.sh` — creates immutable snapshot folder.
  - `tools/reporting/generate_index_md.sh` — generates file inventory portion of `INDEX.md`.
- Reasoning + file-write operations generate the content (CSVs, scaffold, BOE) based on the canonical schemas in the Schema Annex.

Disallowed behavior:
- No writes outside `{EXECUTION_ROOT}/_EstimatePrep/`.
- No overwriting prior snapshots.
- No modification of `_PriceSources/`, `_Estimates/`, deliverable folders, decomposition outputs, or dependency registers.
- No recursive ingestion of prior `_EstimatePrep/` outputs unless explicitly provided as `PRIOR_SNAPSHOT` / `SCAFFOLD_PATH`.

#### Phase SCAFFOLD — method

1. **Resolve tool root + create snapshot folder.** Validate `PHASE` enum; bootstrap `_EstimatePrep/`; create `EPREP_SCAFFOLD_{LABEL}_{DATE}_{TIME}/`.
2. **Load decomposition.** Extract Package IDs, Deliverable IDs, scope items, disciplines, owner roles, variant hints.
3. **Load source documents.** Extract project name, location, owner, timeline, submission requirements, scope boundaries, referenced standards, constraints. Record `TBD` for items not found.
4. **Determine canonical schemas.** If `SCHEMA_MODE=AUTO_FROM_CANONICAL` and `CANONICAL_PRICESOURCES_ROOT` has a matching file, use its header exactly; otherwise use the Schema Annex (see `SCHEMA_ANNEX.md` for the 9 schema families).
5. **Generate `Professional_Staff_Rates.csv`** (Family 4). Default `Confidence=MEDIUM`, `Basis=PARAMETRIC`. ENRICH mode overlays human rates and logs each override.
6. **Generate `Level_of_Effort.csv`** (Family 9). Default `Basis=PARAMETRIC`. No `Confidence` column — provenance is `Basis` alone.
7. **Generate `Assumed_Project_Parameters.csv`** (Family 8). Uses `Source` column (not `Basis`); canonical enum: `ASSUMPTION`, `DESIGN_BASIS`, `CONFIRMED`, `DERIVED`, `PARAMETRIC`.
8. **Generate additional rate tables (conditional).** If `RATE_SCOPE=PRODUCTION_AND_CONSTRUCTION`, generate all applicable Family 1-7 files matching exact canonical schemas.
9. **Generate `PriceSources/INDEX.md`** with the 7 required sections: header block, data quality statement (HIGH/MEDIUM/LOW definitions), file inventory, PS-ID to file mapping, ESTIMATING run configuration (DEL-to-PKG mapping + per-package `PRICE_SOURCES` list + usage guidance), open issues, gaps. Full section contract: see `INDEX_MD_CONTRACT.md`.
10. **Generate `Scaffold/BOE_Scaffold.md`.** Per-deliverable table (DEL-ID, name, package, default basis, fallback policy, mixed-method flag, substance, cost drivers, roles), package cost ownership hints, SOW multi-mapping warnings. Marked `DRAFT — requires human review`.
11. **QA + handoff artifacts.** Produce `Confidence_Summary.md`, `QA_Report.md` with `RUN_STATUS`, `Decision_Log.md`, `Assumptions_Log.md`, `Source_Index.md`, `Override_Log.csv` (ENRICH only), `Conflicts.csv` (when needed), `Publish_Manifest.md` (always).

#### Phase BOE — method

1. **Resolve tool root + create snapshot folder.** Create `EPREP_BOE_{LABEL}_{DATE}_{TIME}/`.
2. **Load approved scaffold.** Read `SCAFFOLD_PATH`; diff against original scaffold if identifiable; log human modifications in `Decision_Log.md`.
3. **Load decomposition + dependencies.** Read `DEPENDENCY_SOURCES` (or `AUTO` for per-deliverable `Dependencies.csv`); build dependency DAG; detect cycles.
4. **Derive tier sequencing.** Assign tiers via topological layering (T0, T1, ...); identify sequential chains and parallelization opportunities; output `Tier_Analysis.md`.
5. **Generate per-deliverable estimation plan.** Tier assignment, basis/fallback/mixed-method from approved scaffold, substance and cost drivers, required price sources; package-level cost ownership rules.
6. **Generate dependency-informed run sequence.** Tiers in order + within-tier parallelism + sequential chains + gates.
7. **Generate aggregation strategy.** Rollups: deliverables to packages to project totals; add evaluation-weight views if `EVALUATION_CRITERIA` provided.
8. **Generate missing/weak PRICE_SOURCES register.** Identify and prioritize low-confidence items impacting the plan.
9. **Compile assumptions and constraints log.** Merge scaffold assumptions + BOE derivations with IDs and impact-if-wrong.
10. **Compile full `BASIS_OF_ESTIMATE.md`.** Follow canonical BOE structure if one exists; otherwise use the 10-section set: Purpose, Project Context, Estimation Scope, Estimation Strategy, Per-Deliverable Plan, Dependency-Informed Run Sequence, Missing/Weak PRICE_SOURCES, Aggregation Strategy, Assumptions Log, Document Control. Full section contract + handoff artifact contracts: see `BOE_STRUCTURE.md`.
11. **QA + handoff artifacts.** `QA_Report.md` with `RUN_STATUS`, `Decision_Log.md`, `Assumptions_Log.md`, `Source_Index.md`, `Conflicts.csv` (if cycles or contradictions), `Publish_Manifest.md` (always).

#### Outputs

##### SCAFFOLD snapshot

```
{EXECUTION_ROOT}/_EstimatePrep/EPREP_SCAFFOLD_{LABEL}_{DATE}_{TIME}/
  Run_Context.md
  PriceSources/
    [pricing library CSVs per RATE_SCOPE]
    INDEX.md
  Scaffold/
    BOE_Scaffold.md
    Package_Analysis.md
  Confidence_Summary.md
  QA_Report.md
  Decision_Log.md
  Assumptions_Log.md
  Source_Index.md
  Override_Log.csv          (ENRICH mode only)
  Conflicts.csv             (when needed)
  Publish_Manifest.md
  Publish_Package/          (optional; if EXPORT_BUNDLE=MANIFEST_AND_PACKAGE)
```

##### BOE snapshot

```
{EXECUTION_ROOT}/_EstimatePrep/EPREP_BOE_{LABEL}_{DATE}_{TIME}/
  Run_Context.md
  BASIS_OF_ESTIMATE.md
  Tier_Analysis.md
  QA_Report.md
  Decision_Log.md
  Assumptions_Log.md
  Source_Index.md
  Conflicts.csv             (when needed)
  Publish_Manifest.md
  Publish_Package/          (optional)
```

#### Non-negotiable constraints

- **Write quarantine.** Write ONLY under `{EXECUTION_ROOT}/_EstimatePrep/`. Never modify `_PriceSources/`, `_Estimates/`, deliverable folders, decomposition outputs, or dependency registers. Publishing to canonical locations is a separate, human-approved step handled by the invoker.
- **Snapshots are immutable.** Each run writes a new snapshot folder; never overwrite prior snapshots.
- **Phase separation.** SCAFFOLD and BOE are distinct invocations. A single run MUST NOT span both phases — the human gate between them is a non-negotiable decision point.
- **Provenance tracking is mandatory.** Every generated value carries provenance appropriate to its schema family: `Basis` + `Confidence` for Families 1-7; `Source` + `Confidence` for Family 8; `Basis` alone (no `Confidence`) for Family 9. Do not add columns that do not exist in the canonical schema for a given file.
- **Parametric defaults are not human confirmation.** Parametric values MUST be labeled `PARAMETRIC` with `MEDIUM` or `LOW` confidence, never `HIGH`. Only human-confirmed, vendor-quoted, or directly source-document-derived values earn `HIGH`.
- **No silent overrides.** When ENRICH mode overlays human data on a baseline, every override MUST be logged in `Override_Log.csv` (what changed, from what, to what, confidence change).
- **Conflicts are surfaced.** If two sources disagree or schema mismatches exist, produce `Conflicts.csv`; do not silently pick a winner.
- **Dependencies are read-only inputs.** Dependency registers inform tier sequencing in Phase BOE but are never modified by this skill.
- **No recursive ingestion.** Do not treat prior `_EstimatePrep/` outputs as "market evidence" unless explicitly provided as `PRIOR_SNAPSHOT` / `SCAFFOLD_PATH`.
- **CSV schema integrity.** Every generated CSV MUST match the exact column names and order specified by its schema family (or by the canonical file discovered via `AUTO_FROM_CANONICAL`). No invented columns.

#### Human decision rights (must remain human)

This skill may propose, but MUST NOT decide:

- Accepting / issuing the BOE strategy and publishing it to canonical locations.
- Rulings on conflicts (two quotes disagree, scope overlaps, contradictory dependency assertions).
- Approving any override that would change a `HIGH`-confidence value.
- Scope boundary decisions (in/out; base vs option vs alternate).
- Any irreversible publication action (git commit/push; copy into `_PriceSources/`).

Human rulings SHOULD be recorded in the scaffold/BOE artifacts (or in a separate decision log maintained by the invoker).

#### QA expectations

See `QA_CHECKS.md` for the full invariant + quality gate set. Summary:

- `RUN_STATUS` declared in `QA_Report.md` (`OK` | `WARNINGS` | `FAILED_INPUTS`).
- Snapshot folder created for every run (including failures).
- No writes outside `_EstimatePrep/`.
- CSV schemas match the canonical Schema Annex exactly.
- Provenance complete per schema family.
- `Publish_Manifest.md` exists and references the run outputs.
- Phase-specific required artifacts present (see `QA_CHECKS.md`).

#### Companion documents

This skill's detailed contracts live in adjacent companion files. Consult these when implementing:

- **`SCHEMA_ANNEX.md`** — 9 canonical CSV schema families covering 18 files in `_PriceSources/`; `Basis`/`Source`/`Confidence` enum references; `Override_Log.csv` and `Conflicts.csv` schemas. Hardened against the on-disk canonical library as of 2026-02-18.
- **`BOE_STRUCTURE.md`** — `BOE_Scaffold.md` contract (Phase SCAFFOLD), `BASIS_OF_ESTIMATE.md` 10-section contract (Phase BOE), `Run_Context.md` minimum fields, `Publish_Manifest.md` handoff contract.
- **`INDEX_MD_CONTRACT.md`** — 7-section `PriceSources/INDEX.md` contract including the ESTIMATING run configuration block.

## Component: skills/estimate-prep/TOOL_POLICY.md

### estimate-prep — Tool Policy

#### Preferred tool order

1. `tools/validation/validate_enum.py` — validate the `PHASE` input at the start of the run.
2. `tools/scaffolding/scaffold_tool_root.sh` — create the `_EstimatePrep/` tool root if it does not yet exist.
3. `tools/scaffolding/create_snapshot_folder.sh` — create the immutable per-run snapshot folder (`EPREP_SCAFFOLD_…` or `EPREP_BOE_…`).
4. `tools/reporting/generate_index_md.sh` — generate the file-inventory portion of `PriceSources/INDEX.md` during Phase SCAFFOLD.
5. Reasoning + file-write operations then produce CSVs, the BOE scaffold, the full BOE, and the handoff artifacts against the canonical schemas.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools` frontmatter field is intentionally omitted).

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- `tools/validation/validate_enum.py` — validates `PHASE` input.
- `tools/scaffolding/scaffold_tool_root.sh` — creates `_EstimatePrep/` tool root.
- `tools/scaffolding/create_snapshot_folder.sh` — creates immutable snapshot folder.
- `tools/reporting/generate_index_md.sh` — generates file inventory portion of `INDEX.md`.

#### Expected use of reasoning

Deterministic helpers are used operationally for enum validation, tool-root and snapshot folder creation, and the file-inventory portion of `INDEX.md`. Everything else — CSV content generation against the canonical Schema Annex, the BOE scaffold, the full `BASIS_OF_ESTIMATE.md`, tier sequencing, aggregation strategy, confidence assignment, override logging, conflict surfacing, and all QA/handoff artifacts — is produced by reasoning + file-write operations.

#### Disallowed use

- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.
- No writes outside `{EXECUTION_ROOT}/_EstimatePrep/`.
- No overwriting prior snapshots.
- No modification of `_PriceSources/`, `_Estimates/`, deliverable folders, decomposition outputs, or dependency registers.
- No recursive ingestion of prior `_EstimatePrep/` outputs unless explicitly provided as `PRIOR_SNAPSHOT` / `SCAFFOLD_PATH`.

#### Write boundary

Write ONLY under `{EXECUTION_ROOT}/_EstimatePrep/`, into a new per-run snapshot folder (`EPREP_SCAFFOLD_{LABEL}_{DATE}_{TIME}/` or `EPREP_BOE_{LABEL}_{DATE}_{TIME}/`). Snapshots are immutable — never overwrite prior snapshots. Never modify `_PriceSources/`, `_Estimates/`, deliverable folders, decomposition outputs, or dependency registers. Publishing to canonical locations is a separate, human-approved step handled by the invoker.
