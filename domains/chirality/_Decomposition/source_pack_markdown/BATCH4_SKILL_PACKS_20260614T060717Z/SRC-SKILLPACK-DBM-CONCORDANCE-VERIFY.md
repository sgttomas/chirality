# Source Pack: Skill pack: dbm-concordance-verify

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/dbm-concordance-verify/BRIEF_SCHEMA.md

### BRIEF SCHEMA - dbm-concordance-verify

This file defines the INIT-TASK dispatch contract for `TASK + dbm-concordance-verify`.

#### Purpose

Use this skill after deterministic package concordance and source-supersession checks have produced findings, but before DBM_PUBLISHER accepts package readiness.

#### Scope model

- `ScopePath` should be the immutable package snapshot directory.
- `AllowedWriteTargets` must name exactly:
  - `Publication_Concordance_Verification.md`
  - `Publication_Concordance_Verification_Findings.csv`

The brief must not grant write access to section folders, planning artifacts, KTY folders, or source authority files.

#### Required brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `PURPOSE` | string | Why verification is being run | `Verify semantic concordance before package readiness.` |
| `ScopePath` | path | Package snapshot directory | `/abs/root/_Publication/DBM/package/RUN-20260421-120000/` |
| `TaskSkill` | string | Must equal this skill name | `dbm-concordance-verify` |
| `AllowedWriteTargets` | list[path] | Exact verification outputs | `[/.../Publication_Concordance_Verification.md, /.../Publication_Concordance_Verification_Findings.csv]` |
| `RuntimeOverrides.SECTIONS_ROOT` | path | Current section outputs root | `/.../_Publication/DBM/sections/` |
| `RuntimeOverrides.CONCORDANCE_REGISTER_PATH` | path | Frozen register | `/.../_Planning/Publication_Concordance_Register.csv` |
| `RuntimeOverrides.CONCORDANCE_FINDINGS_PATH` | path | Deterministic concordance findings | `/.../Publication_Concordance_Findings.csv` |
| `RuntimeOverrides.OUTPUT_VERIFICATION_PATH` | path | Markdown verification output | `/.../Publication_Concordance_Verification.md` |
| `RuntimeOverrides.OUTPUT_VERIFICATION_FINDINGS_PATH` | path | CSV verification findings output | `/.../Publication_Concordance_Verification_Findings.csv` |
| `ExpectedOutputs` | list[path] | Same two verification outputs | `[/.../Publication_Concordance_Verification.md, /.../Publication_Concordance_Verification_Findings.csv]` |

#### Optional brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `RuntimeOverrides.SOURCE_SUPERSESSION_FINDINGS_PATH` | path | Source-supersession findings when validation ran | `/.../Source_Supersession_Findings.csv` |
| `RuntimeOverrides.PUBLICATION_RULES_PATH` | path | Approved publication rules | `/.../_Planning/Publication_Rules.md` |
| `RuntimeOverrides.PUBLICATION_INPUT_MANIFEST` | path | Frozen manifest | `/.../_Planning/Publication_Input_Manifest.md` |
| `RuntimeOverrides.PACKAGE_SNAPSHOT_PATH` | path | Package snapshot root | `/.../_Publication/DBM/package/RUN-20260421-120000/` |
| `CustomInstructions` | string | Run-specific emphasis only | `Pay special attention to shared utility values.` |

#### Runtime-override guidance

- `SECTIONS_ROOT` must contain complete current section bundles.
- The skill reads synthesized section outputs only. It must not be asked to inspect raw KTY-local source files.
- `SOURCE_SUPERSESSION_FINDINGS_PATH` should be provided whenever `validate_source_supersession.py` ran.

#### Example INIT-TASK brief

```md
PURPOSE: Verify semantic concordance before final DBM readiness.
ScopePath: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/
TaskSkill: dbm-concordance-verify
AllowedWriteTargets:
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification.md
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification_Findings.csv
RuntimeOverrides:
  SECTIONS_ROOT: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/sections/
  CONCORDANCE_REGISTER_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Concordance_Register.csv
  CONCORDANCE_FINDINGS_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Findings.csv
  OUTPUT_VERIFICATION_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification.md
  OUTPUT_VERIFICATION_FINDINGS_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification_Findings.csv
ExpectedOutputs:
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification.md
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/package/RUN-20260421-120000/Publication_Concordance_Verification_Findings.csv
```

## Component: skills/dbm-concordance-verify/QA_CHECKS.md

### QA CHECKS - dbm-concordance-verify

#### Minimum output validity checks

The run is valid only when all of the following are true:

1. Both required outputs exist:
   - `Publication_Concordance_Verification.md`
   - `Publication_Concordance_Verification_Findings.csv`
2. All writes stayed inside the package snapshot directory named in the brief.
3. Every register key receives a verdict in the markdown report.
4. Every blocking verdict appears in the findings CSV.
5. No section outputs, planning artifacts, KTY files, or register files were modified.

#### Required verification findings schema

`Publication_Concordance_Verification_Findings.csv` must contain at least:
- `AssertionKey`
- `Verdict`
- `Blocking`
- `ImpactedSections`
- `DeterministicFindingRefs`
- `SourceSupersessionRefs`
- `EvidenceRefs`
- `Explanation`
- `RecommendedAction`

Allowed `Verdict` values:
- `CONFIRMED`
- `NORMALIZATION_ARTIFACT`
- `SEMANTIC_MISMATCH`
- `IMPLICIT_CONFLICT`
- `OMITTED_REQUIRED_ASSERTION`
- `REGISTER_GAP`
- `NEEDS_HUMAN_RULING`

#### Required report structure

`Publication_Concordance_Verification.md` must contain these H2 headings in order:

1. `## Verification Summary`
2. `## Per-Key Verdicts`
3. `## Deterministic Finding Interpretation`
4. `## Implicit Conflicts`
5. `## Register Gaps`
6. `## Human Rulings Required`

#### Verdict requirements

- `SEMANTIC_MISMATCH`, `IMPLICIT_CONFLICT`, and `REGISTER_GAP` verdicts require explanation with section references.
- `OMITTED_REQUIRED_ASSERTION` verdicts must identify the section, assertion key, and whether the section emitted `OMITTED_WITH_RATIONALE`, `OMITTED_BLOCKING`, or no row.
- `NORMALIZATION_ARTIFACT` verdicts must state why the underlying engineering values agree.
- `NEEDS_HUMAN_RULING` verdicts must explain what information is missing or ambiguous.

#### Failure reporting expectations

Use `FAILED_INPUTS` when:
- required runtime overrides are missing,
- the section root, register, or deterministic findings file is missing,
- output paths fall outside the package snapshot directory.

Use `FAILED` when:
- required outputs cannot be written despite valid inputs,
- the run cannot complete semantic verification for internal reasons.

## Component: skills/dbm-concordance-verify/SKILL.md

---
name: dbm-concordance-verify
description: Post-synthesis cross-section semantic concordance verification for rewritten DBM package outputs.
compatibility: Chirality TASK; dispatched by DBM_PUBLISHER after deterministic package concordance and source-supersession findings exist.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - dbm-concordance-verify

#### Purpose

Verify semantic concordance across the synthesized DBM section outputs after deterministic concordance checks have run. The skill reads all section bodies and assertion outputs together, interprets deterministic findings in context, and emits a package-local semantic verification report plus findings CSV.

This skill is a verifier only. It does not rewrite sections, modify the frozen concordance register, dispatch other workers, or read raw KTY-local source files.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatcher: `DBM_PUBLISHER` during Gate 6 after `check_concordance.py` and source-supersession validation have emitted package findings.

#### Inputs

##### Required

- `SECTIONS_ROOT`
- `CONCORDANCE_REGISTER_PATH`
- `CONCORDANCE_FINDINGS_PATH`
- `OUTPUT_VERIFICATION_PATH`
- `OUTPUT_VERIFICATION_FINDINGS_PATH`

##### Optional

- `SOURCE_SUPERSESSION_FINDINGS_PATH`
- `PUBLICATION_RULES_PATH`
- `PUBLICATION_INPUT_MANIFEST`
- `PACKAGE_SNAPSHOT_PATH`

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `SECTIONS_ROOT` | Root containing all current `SEC-*` section output folders | **Required** | Path under `_Publication/DBM/sections/` |
| `CONCORDANCE_REGISTER_PATH` | Frozen approved concordance register | **Required** | CSV path under `_Publication/DBM/_Planning/` |
| `CONCORDANCE_FINDINGS_PATH` | Deterministic `check_concordance.py` findings | **Required** | CSV path under the package snapshot |
| `OUTPUT_VERIFICATION_PATH` | Semantic verification markdown output | **Required** | `Publication_Concordance_Verification.md` under package snapshot |
| `OUTPUT_VERIFICATION_FINDINGS_PATH` | Semantic verification findings CSV output | **Required** | `Publication_Concordance_Verification_Findings.csv` under package snapshot |
| `SOURCE_SUPERSESSION_FINDINGS_PATH` | Source-supersession findings when validation was run | unset | CSV path under package snapshot |
| `PUBLICATION_RULES_PATH` | Approved publication rules for restatement and TBD policy context | unset | Markdown path |
| `PUBLICATION_INPUT_MANIFEST` | Frozen input manifest for admitted-source context | unset | Markdown path |
| `PACKAGE_SNAPSHOT_PATH` | Immutable package snapshot root | inferred from outputs | Path under `_Publication/DBM/package/` |

#### Tool usage

This is a reasoning-only semantic verification skill. It has no deterministic tool requirement and therefore omits `allowed-tools`.

Disallowed behavior:
- no writes outside `OUTPUT_VERIFICATION_PATH` and `OUTPUT_VERIFICATION_FINDINGS_PATH`,
- no modification of section outputs,
- no modification of `Publication_Concordance_Register.csv`,
- no modification of KTY-local files or planning artifacts,
- no raw KA/KTY source reads; verify only synthesized section/package outputs.

#### Outputs

- `{OUTPUT_VERIFICATION_PATH}` - markdown report with one verdict per register key plus summary findings
- `{OUTPUT_VERIFICATION_FINDINGS_PATH}` - CSV findings for package readiness aggregation

#### Verification observations

This skill produces semantic observations for agent/human review. It does not produce automatic readiness verdicts or blocking decisions. All observations are candidates for human disposition.

Allowed observation types:
- `CONFIRMED` - sections agree semantically
- `NORMALIZATION_ARTIFACT` - apparent mismatch is formatting/normalization only, not an engineering conflict
- `SEMANTIC_MISMATCH` - sections disagree on an engineering fact
- `IMPLICIT_CONFLICT` - section prose implies a value/state that contradicts another section
- `COVERAGE_GAP` - synthesized sections reveal a potentially material item absent from another section
- `NEEDS_HUMAN_RULING` - the verifier cannot safely determine agreement without human/domain judgment

All non-CONFIRMED observations are presented as candidate findings for disposition. None automatically block readiness.

#### Method

1. **Validate inputs and write boundary.** Confirm required paths exist and output paths resolve under the package snapshot.
2. **Read synthesized section outputs.** Read all `SEC-##.md`, `SEC-##_QA.md`, `SEC-##_ASSERTIONS.csv`, and `SEC-##_ASSERTION_DISCOVERY.csv` under `SECTIONS_ROOT`.
3. **Read frozen control artifacts.** Read the concordance register, deterministic findings, and source-supersession findings when provided.
4. **Verify every register key.** For each `AssertionKey`, compare section prose, assertion rows, omission statuses, and deterministic findings in context.
5. **Interpret deterministic findings.** Distinguish real engineering disagreement from normalization artifacts.
6. **Search for semantic gaps in synthesized prose.** Identify implicit conflicts and register gaps visible in section text or discovery outputs.
7. **Emit fixed outputs.** Write the markdown report and findings CSV. Do not rewrite any input.

#### Findings CSV schema

`Publication_Concordance_Verification_Findings.csv` must contain:
- `AssertionKey`
- `Verdict`
- `Blocking`
- `ImpactedSections`
- `DeterministicFindingRefs`
- `SourceSupersessionRefs`
- `EvidenceRefs`
- `Explanation`
- `RecommendedAction`

#### Report structure

`Publication_Concordance_Verification.md` must contain:
1. `## Verification Summary`
2. `## Per-Key Verdicts`
3. `## Deterministic Finding Interpretation`
4. `## Implicit Conflicts`
5. `## Register Gaps`
6. `## Human Rulings Required`

## Component: skills/dbm-concordance-verify/TOOL_POLICY.md

### TOOL POLICY - dbm-concordance-verify

#### Preferred tool order

No deterministic tools are required. The verifier reads already-produced package and section artifacts and performs semantic reasoning.

#### Allowed deterministic tools

##### TASK-enforced

None. The skill omits `allowed-tools`.

##### Operationally invoked

None.

#### Expected use of reasoning

Use strong-model semantic reasoning to compare section prose, assertion rows, deterministic findings, and source-supersession findings across the full package context.

#### Disallowed use

- Do not invoke publication tools.
- Do not dispatch other agents or skills.
- Do not read raw KTY-local source files.
- Do not rewrite section bodies, section QA, planning artifacts, or the concordance register.

#### Write boundary

Writes are limited to:
- `Publication_Concordance_Verification.md`
- `Publication_Concordance_Verification_Findings.csv`

Both outputs must resolve under the current immutable package snapshot directory named in the brief.
