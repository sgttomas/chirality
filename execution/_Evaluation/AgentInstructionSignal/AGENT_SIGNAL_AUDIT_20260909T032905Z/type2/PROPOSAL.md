# Type 2 instruction signal audit — change proposal

Status: CANDIDATE / derivative decision support. Basis: HEAD `781b478176db46ca66ebd38991607612e0ce9338`; exact subject hashes are in `../SOURCE_MANIFEST.json` and `COVERAGE.json`. All 15 assigned files were read in full. This proposal changes no live instruction, skill, caller, tool, or governance record.

## Proposed direction

Make the recurring method available directly where it is used. For ten current packages, propose TASK skills; for two, propose deterministic audit tools; for AUDIT_EPISTEMIC, RESEARCHER, and TASK, propose smaller persistent instructions with focused behavioral judgment or execution semantics. These are target dispositions, with replacement and caller migration preceding retirement of a named instruction.

| Role | Target disposition | Replacement / remaining center |
|---|---|---|
| AGGREGATION | CONVERT_TO_SKILL | `aggregation` with an `estimate-collation` method profile |
| AUDIT_AGENTS | CONVERT_TO_SKILL | `agent-instruction-audit` |
| AUDIT_DECOMP | CONVERT_TO_SKILL | `decomposition-coverage-audit` |
| AUDIT_DEP_CLOSURE | CONVERT_TO_SKILL | `dependency-closure-audit` plus repaired graph analyzer |
| AUDIT_EPISTEMIC | SLIM | Claim-level judgment about warrant and visibility |
| AUDIT_GOVERNANCE | CONVERT_TO_SKILL | `governance-consistency-audit` |
| AUDIT_HYPERGRAPH_CLOSURE | CONVERT_TO_SKILL | `hypergraph-closure-audit` plus candidate validator |
| AUDIT_SCOPE_CLOSURE | CONVERT_TO_SKILL | `scope-closure-audit` |
| DOMAIN_HYPERGRAPH | CONVERT_TO_SKILL | `domain-hypergraph` discovery method around the existing builder |
| EVALUATION_DEPENDENCY_AUDIT | CONVERT_TO_TOOL | Candidate unified dependency-register audit CLI |
| EVALUATION_REPORT | CONVERT_TO_SKILL | `evaluation-dimension` |
| EVALUATION_STRUCTURE_AUDIT | CONVERT_TO_TOOL | Candidate unified workspace-structure audit CLI |
| PREPARATION | CONVERT_TO_SKILL | `workspace-scaffold`, using existing scaffold tools |
| RESEARCHER | SLIM | Independent source verification and recoverable bounded evidence production |
| TASK | SLIM | Bounded execution; progressively normalize mechanical fields in the harness |

Candidate names identify proposed destinations; these folders/tools do not yet exist. The inspected live inventory contains `evaluation-protocol` and `research-orchestration`, which are caller-side methods; neither supplies the proposed worker replacements.

## Common implementation basis

**Observation.** `docs/WORKFLOW_COMPONENT_STANDARD.md:339` currently requires frontmatter, body type, six-row Agent Type table, precedence, invariants, four delimited sections, applicable interfaces, and compatibility notes. `D-GOV-13_dedicated_agent2_requalification.md:11` approves the fourteen dedicated packages in this group as the compatibility baseline; its future-migration clause at line 38 permits conversion when replacements, callers, compatibility, historical references, validators, and tests land together. `skills/README.md:37` describes full method hydration, including the three companion files. The standard's qualification sequence (`:186`) expressly evaluates tools and TASK skills before a dedicated package.

**Observed consumers.** The app instruction parser requires the six table fields and four sections (`projects/chirality-app-dev/frontend/src/lib/harness/agent-instruction.ts:47`); managed dispatch resolves dedicated approval and type/class (`managed-delegation.ts:281`). The parent's shared inspection also identifies the successor runtime's type/class reader. Removing these machine fields from retained files requires a coordinated parser/manifest change, rather than a prose-only edit. Present enforcement varies by invocation class; this audit does not claim all prose constraints are already mechanically enforced.

**Proposed common edits.** Remove repeated naming-convention paragraphs and the repeated “The human does not read this document” slogans. Remove static revision/date recitals from active behavioral text; Git history and immutable decision evidence carry chronology. Express purpose once. Consolidate repeated evidence, output-root, snapshot, and conflict rules into one applicable contract. Move command recipes, brief schemas, and report templates into the method package or tool contract identified on each card. Machine metadata can move to a runtime manifest once its consumers support that representation. A reference alone is insufficient for runtime-critical material: the launch must hydrate the accepted method and its contracts.

**Governance and handoff.** Adoption of a conversion needs a user decision under D-GOV-13's replacement-first terms and the current instruction-change controls. A redesign of the required document envelope needs a superseding standard/validator decision; slimming within it can preserve the current parse contract. Agent-index changes require coordinated notices for affected authority corpora and SHA-pinned mirrors under `AGENTS.md`'s agent-index change-notice rule. Parent fan-in owns the cross-project routing inventory. Historical snapshots remain evidence. The probes below are proposed future checks, not executed behavior claims.

## AGGREGATION

**Core and disposition — CONVERT_TO_SKILL.** Bring separately produced records into a coherent cross-scope view while preserving where they came from and making ambiguity visible. Its characteristic judgment is choosing and explaining source sets, keys, and conflict treatment so incremental aggregation remains intelligible.

**Evidence.** `agents/AGENT_AGGREGATION.md:73` makes Estimate Collation the default mission; `:177` requires “stable unique keys” and incremental merging; `:192` prescribes a report package; `:311` identifies scalability and provenance as the purpose. `PROJECT_SETUP:586` invokes it for an approved aggregation strategy. `tools/reporting/merge_detail_csvs.py` is an existing component named at `AGGREGATION:209`, not an end-to-end replacement.

**Changes.**
- **PROTOCOL:** Carry source selection, mapping, and conflict judgment in a concise `aggregation` skill. Put estimate detail/BOE/risk/assumption handling (`:117–175`) into its estimate-collation profile. Replace the unconditional all-estimate glob in the sample merge command with the selected input manifest; the command should execute the selection the method actually made.
- **SPEC:** Consolidate provenance and conflict obligations repeated at `:59` and `:244`. Define row eligibility and totals once in the estimate profile; make currency treatment an explicit input before cross-currency totals.
- **STRUCTURE:** Move snapshot and coverage schemas (`:257–304`) to skill templates. Keep the stable namespaced record key in the short method description because it governs merging judgment.
- **RATIONALE/perimeter:** Reduce the introductory three-paragraph account and final rationale to the reason for traceable accumulation. Remove naming and implementation-choice commentary. Runtime defaults become brief-schema defaults.

**Caller/recovery/decision dependencies.** Migrate PROJECT_SETUP's allowlist and Phase 4.3, its BOE strategy interface, and PREPARATION's aggregation templates. TASK must receive the snapshot and any `_LATEST`/pipeline pointer paths as explicit write targets. The replacement must preserve prior-pipeline incorporation and duplicate/conflict evidence; generic CSV concatenation cannot establish this behavior. Uncertainty: all project-specific consumers of the estimate outputs are not inventoried here.

**Probe.** Two runs include the same deliverable with changed amounts and one invalid detail table. The result names the selected sources, exposes the collision, excludes invalid totals, and reports exact coverage without destroying prior evidence.

## AUDIT_AGENTS

**Core and disposition — CONVERT_TO_SKILL.** Compare each instruction's actual commitments with a named accepted design basis, identify discrepancies, and propose precise repairs. The useful recurring pattern is evidence-linked conformance judgment grounded in both the subject and its criterion.

**Evidence.** `agents/AGENT_AUDIT_AGENTS.md:126` invokes the validator first; `:146` supplies the rubric and paired excerpts; `:172` specifies a minimal patch plan. The current rubric is already external (`docs/rubrics/AUDIT_AGENT.md`), so hydration is an established pattern. EVALUATION lists this role in frontmatter (`AGENT_EVALUATION.md:3`); `skills/evaluation-protocol/SKILL.md` includes it in the toolbelt.

**Changes.**
- **PROTOCOL:** Keep validator → semantic rubric → prioritized finding → actionable patch as the method spine in `agent-instruction-audit`. Replace the separate metadata inventory recital with the fields the validator/rubric supplies. State whether a run is conformance repair or authorized redesign in its brief; “smallest safe edit” (`:175`) becomes the conformance mode's optimization criterion.
- **SPEC:** One validity block for coverage, paired evidence, finding disposition, and patch plan. Resolve `:116`'s optional patch plan against `:204`'s mandatory plan by making the expected artifact explicit in the method contract.
- **STRUCTURE:** Reference or template the existing rubric cards and issue schema; move timestamped folder boilerplate out of the method's behavioral core.
- **RATIONALE/perimeter:** Retain a single sentence linking traceability to actionable review. Remove version/naming/slogan material and duplicate mission/output lists.

**Caller/recovery/decision dependencies.** EVALUATION and its toolbelt dispatch TASK with explicit audit sources, rubric, standard version, and output root. Missing canon remains a partial inventory with blocked canon-dependent checks; missing scope remains FAILED_INPUTS. D-GOV-13 adoption and compatibility references apply. Uncertainty: rubric redesign may be necessary for a signal-focused mode; today's conformance rubric alone cannot answer whether accepted invariants should change.

**Probe.** A structurally valid agent follows a superseded reference and contains a semantic conflict. The candidate detects both, labels the governing basis, and distinguishes a conformance repair from a design proposal.

## AUDIT_DECOMP

**Core and disposition — CONVERT_TO_SKILL.** Reconcile declared scope with its materialized workspace in both directions, including the evidence supporting current closure. Its characteristic attention is to declared-but-absent entities, undeclared material, and active derivatives that misrepresent the accepted decomposition.

**Evidence.** `agents/AGENT_AUDIT_DECOMP.md:209–241` defines forward/reverse coverage; `:253` adds semantic context comparison; `:317–371` adds active-package/handoff checks. `AGENT_SCOPE_CHANGE.md:185` imports this file's heading-binding algorithm, and `:255/:537` consume coverage before and after amendments.

**Changes.**
- **PROTOCOL:** Keep resolve basis → compare declarations/materialization → inspect active derivative/handoff parity → explain discrepancies. Extract the twelve checks into `decomposition-coverage-audit/QA_CHECKS.md`. Use registered DOMAIN integrity validation for covered mechanical checks, recording residual semantic inspection rather than reimplementing those checks.
- **SPEC:** Replace the whole-run “Same inputs → same outputs” claim (`:71`) with deterministic inventories and explicitly documented semantic comparison judgments. Keep source-snapshot and coverage denominators explicit.
- **STRUCTURE:** Move variant tables (`:94–163`), heading-binding algorithm, and machine schemas into a shared decomposition contract and skill resources. First reconcile the matrix header at `:411` (`DeliverableID,PackageID`) with the schema at `:547` (`ProductionUnitID,PartitionID` plus concrete labels). Use one generated schema.
- **RATIONALE/perimeter:** Compress the history of DOMAIN additions and modular shape into the reason for comparing accepted scope, materialization, and current derivatives. Remove revision recitals and repeated validity/output inventory.

**Caller/recovery/decision dependencies.** Migrate SCOPE_CHANGE's imports and EVALUATION dispatch atomically. Keep `coverage_summary.json`, concrete labels, and PASS/WARN/FAIL `closure_readiness` stable until consumers migrate. The shared heading resolver has actual callers; moving it requires changing those references. Partial parses must disclose unavailable checks. Uncertainty: fuzzy context/filename matching has no verified deterministic implementation; conversion remains a skill with judgment.

**Probe.** Renumber all headings, introduce one undeclared folder, omit a declared unit, and make a derivative support count stale. The candidate preserves heading-based binding and reports each divergence with both declaration and filesystem evidence.

## AUDIT_DEP_CLOSURE

**Core and disposition — CONVERT_TO_SKILL.** Make the consequences of a dependency graph visible: missing targets, ambiguous edges, cycles, isolation, and coordination concentrations. It interprets topological evidence for the owning manager and supplies a reproducible rerun basis.

**Evidence.** `agents/AGENT_AUDIT_DEP_CLOSURE.md:147` says steps 1–4 are performed by a single deterministic call; `:171–211` specifies nine checks. Actual `tools/coordination/analyze_dep_closure.py:53` discovers only registers that exist; `:78–118` keeps rows from invalid-schema files; `:120–151` hard-codes ACTIVE filtering and adds no unknown-direction edges. `:195` defines “orphans” as isolated nodes, while the instruction's check 2 (`:179`) means missing targets. Its CLI (`:233`) accepts only root/output-dir, not the advertised scope/filter/normalization settings.

**Changes.**
- **PROTOCOL:** Replace the duplicated algorithm narrative with a concise run/inspect/interpret method and a check-to-tool coverage map. Repair or extend the analyzer to implement declared semantics before relying on its invocation for complete coverage.
- **SPEC:** Define missing-target and isolated-node findings separately. Remove the stale requirement for a per-run `analyze_closure.py` (`:246`) when the registered tool is used; record the invoked tool version/hash and evidence location instead, subject to reproducibility-contract acceptance.
- **STRUCTURE:** Align summary location: Outputs puts it under `Evidence/` (`:97`), SPEC/layout put it at snapshot root (`:246/:272`). Keep one canonical artifact contract in `dependency-closure-audit`.
- **RATIONALE/perimeter:** State the interpretation purpose once. Move defaults, thresholds, example commands, and output trees to the brief/tool contract. Delete claims of coverage that the tool does not supply.

**Caller/recovery/decision dependencies.** EVALUATION/toolbelt and dependency-extract rerun consumers need migrated references. Tool repairs precede conversion. Missing registers must remain nodes in the independent folder inventory; malformed inputs must degrade coverage explicitly. D-GOV-13 replacement terms apply. Uncertainty: no production graph run was executed, and downstream assumptions about the existing JSON metrics need inventory.

**Probe.** Include a registerless deliverable, malformed-schema file with an apparent edge, unknown direction, missing target, and two-node SCC. The candidate reports distinct categories with the chosen filters and no fabricated complete verdict.

## AUDIT_EPISTEMIC

**Core and disposition — SLIM.** Examine what a deliverable claims, what supports those claims, and whether uncertainty, conflict, and review status are visible enough to support reliance. It contributes claim-level judgment, especially when prose appears confident but its warrant is weak or absent.

**Evidence.** The role's defining question is explicit at `agents/AGENT_AUDIT_EPISTEMIC.md:12`; semantic claim discovery appears at `:158–175`, warrant judgment at `:230`, and cross-section alignment at `:247`. The same file devotes `:343–496` to brief/report/JSON/QA templates and `:503–527` to repeated explanation of its significance.

**Changes.**
- **PROTOCOL:** Express the movement as identify claims → inspect warrant/gaps/conflicts → compare requirements, verification, and intent → report limits. Keep focused passes in an on-demand `epistemic-audit` method resource with STANDARD/DEEP settings.
- **SPEC:** State claim evidence and classification obligations once. Replace the deterministic semantic-findings promise (`:77`) with fixed inventory/metric rules plus recorded interpretation limits. Make `INDETERMINATE` an explicit audit assessment distinct from the four warrant states: SPEC at `:314` permits only four while issue/summary schemas at `:422/:440` include it.
- **STRUCTURE:** Keep the Claim/Warrant/Status/Gap/Conflict/Ruling distinction and source-of-authority reference. Move schemas and production-format compatibility to hydrated method resources. Separate citation presence from source support so “provenance completeness” cannot silently become warrant adequacy.
- **RATIONALE/perimeter:** Replace claims such as “The audit tells them” (`:519`) and the “first agent” history with a concise account of helping a professional inspect reliance. Remove duplicated valid/invalid restatements and output layouts.

**Persistent-role decision.** Judgment alone does not distinguish this role from governance or conformance auditing, which also require semantic interpretation. The proposed long-term role hypothesis is a stable responsibility for examining the warrant of claims across changing methods and work products; the current file primarily prescribes one seven-pass deliverable audit and does not demonstrate that wider identity in use. SLIM is therefore a concrete next candidate, with the long-term named-role decision open. If the intended remit remains this recurring deliverable audit, `TASK + epistemic-audit` is the more direct method classification. D-GOV-13 supplies current compatibility authority, not evidence of superior role behavior.

**Caller/recovery/decision dependencies.** Preserve EVALUATION invocation, the accepted TYPES ontology, SOW reference namespaces, and its D-GOV-13 status during slimming. Owner decision: retain this judgment orientation as a named type or convert it to TASK plus the proposed method after comparison. Static inspection supplies a reason to test the smaller role; it establishes no performance advantage over TASK. Ambiguous production format still returns a scoped limitation rather than invented claim counts.

**Probe.** Give the candidate a well-labeled claim with a citation that fails to support its specific value, an unlabeled but source-supported claim, and conflicting verification criteria. Assess whether it distinguishes visibility, citation presence, substantive warrant, and disagreement.

## AUDIT_GOVERNANCE

**Core and disposition — CONVERT_TO_SKILL.** Compare the governance suite's stated rules, vocabulary, references, and enforcement claims with one another and their supporting evidence. Its most consequential judgment is recognizing where a local design choice is presented with more authority or universality than its warrant supports.

**Evidence.** `agents/AGENT_AUDIT_GOVERNANCE.md:121–248` supplies six recurring checks; `:251` adds claim-strength calibration. The calibration pass uses MAJOR/MINOR at `:270`, while SPEC `:330` and issue schema `:456` accept BLOCKER/WARNING/INFO. The brief default and output templates enumerate only passes 1–6.

**Changes.**
- **PROTOCOL:** Organize a short `governance-consistency-audit` method around inventory/reference checks followed by semantic coherence and claim calibration. Generate counts and reference inventories with tools; inspect meaning and warrant with the model. Give calibration an unambiguous pass ID and include it in defaults and summaries.
- **SPEC:** Unify severity/category enums; add an explicit claim-calibration category to the issue schema. Define orphan references as observations whose significance is assessed, rather than allowing unused IDs automatically to imply governance failure.
- **STRUCTURE:** Relocate the long brief/report/QA/JSON templates (`:339–540`) to skill resources. A single schema drives all output forms. Resolve the current `IssueType: K-CLAIM-1` prescription against a CSV schema with no IssueType column.
- **RATIONALE/perimeter:** Compress the six-pass recap; remove revision and repeated snapshot/conflict/evidence bullets in `:69–83`. Keep the reason for comparing authority claims with actual enforcement.

**Caller/recovery/decision dependencies.** Migrate EVALUATION and evaluation-protocol toolbelt. The skill consumes the current accepted standards; a user-requested challenge to those standards becomes a separately labeled proposal. Missing required documents retain partial-pass behavior and coverage gaps. Uncertainty: no unified governance scanner was identified; links and inventories are tool candidates, while semantic calibration remains model work.

**Probe.** A suite has consistent counts and working links but claims its local architecture is universally necessary. The candidate exposes the warrant mismatch and emits it in a schema-valid, summary-counted finding.

## AUDIT_HYPERGRAPH_CLOSURE

**Core and disposition — CONVERT_TO_SKILL.** Determine whether a graph snapshot's incidence, membership, and coverage correspond to its declared structure and workspace evidence. It makes an apparently coherent projection's missing bindings and unresolved inputs visible.

**Evidence.** `agents/AGENT_AUDIT_HYPERGRAPH_CLOSURE.md:179` enumerates nine mostly mechanical checks. `:161` explicitly notes there is no dedicated parse tool; `:54/:108` require a preserved analysis script. Existing `tools/aggregation/build_hypergraph.py` verifies its own generated graph, while this role audits an already supplied snapshot and workspace.

**Changes.**
- **PROTOCOL:** Move parsing, incidence/arity/membership checks and issue truncation into a candidate snapshot-validation tool. Keep basis selection, limits, comparison interpretation, and prioritized remediation in `hypergraph-closure-audit`.
- **SPEC:** Distinguish a valid audit with failed graph checks from a valid graph. Name unavailable and optional ledger checks consistently; optional absence at `:247` currently becomes INCOMPLETE while JSON `:365` also permits SKIPPED. Adopt one documented convention.
- **STRUCTURE:** Put schemas/thresholds/strict-mode policy in tool and skill contracts. Extend audit coverage to KNOWLEDGE_SUBJECT/HAS_SUBJECT/SUBJECT_MATERIALIZED_AS, present in the current builder but absent from the nine-check closure method. This is a contract alignment decision, not just prose compression.
- **RATIONALE/perimeter:** Reduce repeated root, snapshot, and command blocks to one invocation contract and one short explanation of structural closure.

**Caller/recovery/decision dependencies.** EVALUATION/toolbelt, DOMAIN_HYPERGRAPH's suggested follow-up, and PROJECT_SETUP's DOMAIN pipeline require migrated method names. Keep current summary compatibility or version it. The candidate tool must handle malformed CSVs with check-level incompleteness and preserve full finding counts when issue output is capped. Uncertainty: builder fixtures do not prove independent validation of arbitrary input snapshots; a new validator and adversarial fixtures are needed.

**Probe.** Supply a valid incidence table with a split subject-materialization bridge, missing category, and truncated issue cap. The result detects the current graph vocabulary's defects and preserves total findings separately from displayed findings.

## AUDIT_SCOPE_CLOSURE

**Core and disposition — CONVERT_TO_SKILL.** Follow an accepted amendment through its consequences and judge whether the recorded change has actually become coherent project state. Its attention reaches past files being edited to downstream reruns, retired references, supersession, and factual-use readiness.

**Evidence.** `agents/AGENT_AUDIT_SCOPE_CLOSURE.md:106–181` checks action execution and reruns; `:231–321` covers supersession and KTY remediation. `:197` instructs use of the registered DOMAIN integrity validator and explicitly avoids duplicate inline logic. Existing tools also accumulate supersession and validate remediation manifests.

**Changes.**
- **PROTOCOL:** Keep amendment → action evidence → propagated consequences → closure verdict as the skill spine. Move action-type matrices and DOMAIN adapters to `scope-closure-audit` resources. Consolidate the remaining repeated manifest validation with the tool's contract; leave semantic evidence sufficiency and readiness conflicts to model review.
- **SPEC:** Use one result/severity vocabulary. The invariants permit UNKNOWN severity (`:54`), preconditions use ADVISORY/ERROR (`:90–95`), but schema permits only four different values (`:431`). Represent uncertainty separately from severity. Make CLOSED versus CLOSED_WITH_OBSERVATIONS mutually exclusive (`:339–344`).
- **STRUCTURE:** Move action/report/JSON/QA templates to the skill. Add explicit evidence basis for rerun verification: dates and file existence (`:150–164`) are signals to inspect; completion should cite a matching successful run and its scope/input basis when available.
- **RATIONALE/perimeter:** Compress historical dispatch explanations and glossary into the method's purpose and minimum terms. Replace the fixed seven-day warning with recorded amendment recency and actual evidence gaps.

**Caller/recovery/decision dependencies.** EVALUATION dispatch ownership and SCOPE_CHANGE producer schemas remain explicit; migrate the toolbelt and any consumers of `scope_closure_summary.json`. D-GOV-13 and the scope-change/DOMAIN accepted contracts govern adoption. Missing required supersession/remediation artifacts remain findings even when files are absent. Uncertainty: some legacy runs may lack strong rerun receipts; report them as incomplete evidence rather than declaring failures purely from age.

**Probe.** A source-affecting amendment has a post-dated estimate snapshot covering the wrong scope, absent supersession files, and a deferred KTY row paired with publication-ready handoff. The candidate distinguishes each discrepancy and keeps closure open.

## DOMAIN_HYPERGRAPH

**Core and disposition — CONVERT_TO_SKILL.** Discover the semantic structure expressed by DOMAIN workspace evidence and prepare a traceable graph representation. Its judgment centers on identifying source-backed entities and distinguishing decomposition subjects from their materialized artifacts.

**Evidence.** `agents/AGENT_DOMAIN_HYPERGRAPH.md:19` supplies the two-layer distinction; `:155–296` performs evidence discovery; `:298` defines staging CSVs; `:329` delegates construction to `tools/aggregation/build_hypergraph.py`. Nevertheless, `:352–393` restates the hashing algorithm, sort rules, and all builder QA checks.

**Changes.**
- **PROTOCOL:** Keep source discovery, subject/artifact discrimination, staging, invocation, and interpretation in `domain-hypergraph`. Remove the embedded hashing algorithm/sort implementation from agent-facing method prose; use the builder's versioned contract and fixtures. Replace newest-mtime ledger selection (`:266`) with explicit accepted-basis selection or a reported ambiguity.
- **SPEC:** Separate staging completeness, tool success, graph defect findings, and run status. Scope determinism to identical staging plus tool version; metadata discovery can involve judgment. Preserve evidence for unresolved mappings.
- **STRUCTURE:** Relocate staging/graph schemas to tool-owned documentation generated or checked against implementation. Keep the semantic subject/artifact/Scoping distinction close to the discovery method. Add explicit accepted-upstream snapshot fields for derivative provenance.
- **RATIONALE/perimeter:** Compress the repeated graph argument and output enumeration. Remove assertions that the chosen representation is universally “right”; state which multi-party bindings this representation preserves in this application.

**Caller/recovery/decision dependencies.** Migrate PROJECT_SETUP Phase 2.6, its allowlist, and AUDIT_HYPERGRAPH_CLOSURE references. Existing builder and fixtures support tool construction from staging, not complete discovery. Publication pointers require explicit target authorization under TASK. Unknown ledger schemas remain partial discovery, with declared omitted layers. D-GOV-13 conversion requires new skill hydration/caller checks. Uncertainty: the accepted basis for treating Scoping's bridge as authoritative must be reconciled with derivative-package rules.

**Probe.** A KTY has anticipated filename hints but no subject IDs; another has a Scoping bridge and an artifact on disk; two ledgers conflict. The candidate creates only evidenced subject identities, records present/anticipated status, and exposes basis ambiguity.

## EVALUATION_DEPENDENCY_AUDIT

**Core and disposition — CONVERT_TO_TOOL.** Measure dependency-register structure and field completeness exhaustively and reproducibly. The result is an inventory of mechanical facts that EVALUATION can interpret alongside graph and content findings.

**Evidence.** `agents/AGENT_EVALUATION_DEPENDENCY_AUDIT.md:59–86` delegates column, anchor, evidence, and enum checks to tools; `:180` calls the work “primarily deterministic CSV parsing.” Existing wrappers use substring/line scanning: `check_implements_node.sh:20` counts any matching text, and `check_evidence_coverage.sh:24` parses with `awk -F','`. These are incomplete foundations for a robust CSV report.

**Changes.**
- **PROTOCOL:** Replace the sequence with one candidate CSV-aware audit CLI using the canonical schema/enum libraries. Validate exact fields and all rows; eliminate the 10–15-file enum sample (`:75`) and the brief-size edge case created by SPEC's minimum-ten requirement (`:113`).
- **SPEC:** Generate coverage, per-file checks, invalid fields, and denominators deterministically. Replace “MUST NOT modify any files” (`:37`) with a source-read/output-write tool contract. Define empty datasets and malformed files explicitly.
- **STRUCTURE:** Move Markdown/JSON/CSV output rendering into the tool. Separate optional graph evidence into the graph-audit capability rather than embedding an “if feasible” second audit here.
- **RATIONALE/perimeter:** Remove the dedicated instruction after caller replacement. Tool documentation carries input/output semantics; remove model-selection commentary and the ad hoc history recital.

**Caller/recovery/decision dependencies.** EVALUATION and evaluation-protocol must invoke the new tool and validate its exit status/artifacts. Existing tools need integration and repairs; merely renaming the current wrappers is insufficient. D-GOV-13 conversion approval and registered-tool contract/tests apply. Uncertainty: no unified CLI exists; fixture work should include quoted/multiline fields, empty files, and exact enums.

**Probe.** A dependency statement contains the text IMPLEMENTS_NODE while AnchorType is blank; another quoted field contains commas; one enum is invalid in the final file of a three-file set. The CLI reports all three accurately without a sample-size assumption.

## EVALUATION_REPORT

**Core and disposition — CONVERT_TO_SKILL.** Judge one requested dimension against its accepted criteria, showing how each piece of evidence supports a result and how those results support the score. Its distinctive contribution is calibrated scoring with an inspectable chain of reasons.

**Evidence.** `agents/AGENT_EVALUATION_REPORT.md:70–100` reads a supplied protocol, gathers evidence, applies checks, scores, and writes one report; `:124–169` is a full report template. `skills/evaluation-protocol/SKILL.md` already owns caller-level rubric acceptance and scoring policy.

**Changes.**
- **PROTOCOL:** Move the five-step method into `evaluation-dimension`. Keep check-by-check judgment and explicit insufficient-evidence treatment. Replace the broad tool menu with brief-selected evidence/tool inputs and a link to relevant tool contracts.
- **SPEC:** Reference the accepted rubric rather than treating the four locally worded grade descriptions (`:93–97`) as an independent scoring authority. Define the distinction between missing evidence and a demonstrated failed criterion.
- **STRUCTURE:** Move the single report template to the skill; retain check/result/evidence/justification as the interface consumed by EVALUATION.
- **RATIONALE/perimeter:** Keep the reason for a self-contained dimension return. Remove duplicated type/scope/role recitals and provider/model-selection discussion (`:178–186`).

**Caller/recovery/decision dependencies.** EVALUATION and its toolbelt dispatch `TASK + evaluation-dimension`, with accepted rubric, exact dimension, sources, and output target. Preserve report naming until synthesis consumers migrate. Fail explicitly when scoring criteria are absent; missing evidence during a valid run produces labeled observations. D-GOV-13 replacement terms apply. Uncertainty: generic TASK status/record fields add an outer wrapper; verify the parent can consume the unchanged dimension report without reconstructing it.

**Probe.** A rubric has one mandatory failed check and several strong optional checks. The candidate's score follows the accepted rubric rather than averaging away the mandatory failure, and its rationale cites the affected check.

## EVALUATION_STRUCTURE_AUDIT

**Core and disposition — CONVERT_TO_TOOL.** Inventory workspace structure, selected production formats, and lifecycle values against the declared filesystem contract. The useful output is an exhaustive, reproducible account of presence, absence, validity, and scope.

**Evidence.** `agents/AGENT_EVALUATION_STRUCTURE_AUDIT.md:56–110` prescribes enumeration, counts, states, required files, package trees, and tool roots. `tools/evaluation/count_deliverable_files.sh` already calls the SOW format validator. `extract_lifecycle_states.sh:14` extracts the first matching state anywhere in a file and omits RETIRED, which limits it as a canonical current-state reader.

**Changes.**
- **PROTOCOL:** Combine inventories into a candidate workspace audit CLI. Use an explicit production-unit inventory and variant argument; current DEL-only depth-limited `find` (`:57`) should not silently represent every possible execution workspace. Parse Current State as a field rather than a text occurrence.
- **SPEC:** Define audit validity by completed checks and honest results; current `:122` requires every extracted state to be valid, conflating successful auditing with a conformant subject. Resolve the source-read/report-write contradiction at `:37`.
- **STRUCTURE:** Generate counts and report tables from one data structure; preserve SOW/legacy/migration-format outcomes using the existing validator. Version the required-root list from the selected contract rather than copying it into multiple files.
- **RATIONALE/perimeter:** Remove the dedicated file after migration, carrying its input/output/check contract in tool docs and fixtures. Remove historic ad hoc-work narrative and runtime model commentary.

**Caller/recovery/decision dependencies.** EVALUATION/toolbelt consume structured tool output; current report headings can remain as a compatibility render. D-GOV-13, accepted SOW transition rules, and canonical lifecycle enum constrain the replacement. Malformed state values must be returned as findings rather than misread from history. Uncertainty: DOMAIN applicability needs an explicit owner-selected scope rather than assumed DEL/KTY equivalence.

**Probe.** A RETIRED deliverable has OPEN in its history, an initialized deliverable lacks production content, and another has unauthorized dual formats. The tool reports current states and distinct format violations with consistent totals.

## PREPARATION

**Core and disposition — CONVERT_TO_SKILL.** Materialize accepted decomposition entries into predictable workspace structure with source-faithful metadata and observable created/skipped results. Its characteristic judgment is distinguishing supplied content from placeholders while making reruns preserve existing work.

**Evidence.** `agents/AGENT_PREPARATION.md:106–269` has seven mode recipes; `:154/:236` delegate structure creation to the same scaffold tool; `:356–575` is predominantly templates. `tools/scaffolding/scaffold_deliverable.sh:30–51` creates empty stubs and reports only aggregate created/skipped counts. PROJECT_SETUP's Phase 2.1 (`:248`) already owns the call sequence and source fields.

**Changes.**
- **PROTOCOL:** Move the seven modes to `workspace-scaffold`; combine A/E and C/F through explicit PROJECT/SOFTWARE/DOMAIN bindings. Use existing scaffold tools; add a created-path manifest so metadata population applies exactly to newly created files. Current “fill the stub” steps can otherwise conflict with idempotency on reruns.
- **SPEC:** Consolidate no-overwrite, source fidelity, and minimum-fileset checks from invariants, Operating Rules, QA, and validity. Clarify whether `_MEMORY.md` is produced: STRUCTURE `:480` says it is created, while C/F and the five-file scaffolder omit that step.
- **STRUCTURE:** Move metadata templates into skill resources and existing `docs/templates/MEMORY_TEMPLATE.md`. Put folder sanitization in a tested utility. Correct Task G's `_Reconciliation/HypergraphClosure` (`:266`) to the accepted `_Evaluation/HypergraphClosure` target when adopting the migration.
- **RATIONALE/perimeter:** Keep the brief structural-reliability rationale. Remove the duplicate END:PROTOCOL delimiter (`:303/:319`), naming slogan, and the paragraph explaining how the four sections map to philosophy (`:66`).

**Caller/recovery/decision dependencies.** Migrate PROJECT_SETUP frontmatter and Phase 2.1, SCOPE_CHANGE's preparation handoffs, aggregation templates, and any actor checks using PREPARATION. Existing `write_status.sh` has actor/transition semantics, so a TASK skill must use an accepted equivalent actor identity rather than renaming calls casually. D-GOV-13 requires no-overwrite recovery tests. Uncertainty: all status-actor consumers and historical brief templates require parent-wide inventory.

**Probe.** Rerun against a partially scaffolded folder with edited `_CONTEXT.md`, missing `_REFERENCES.md`, and an existing advanced lifecycle state. Only missing authorized artifacts are created; existing content/state survives; the return identifies each skipped/created path.

## RESEARCHER

**Core and disposition — SLIM.** Verify a bounded research question against accepted evidence, independently testing load-bearing claims even when supplied confidently by the caller. Preserve an inspectable, recoverable packet that distinguishes discovered leads, direct readings, executed checks, and unresolved coverage.

**Evidence.** `agents/AGENT_RESEARCHER.md:115–135` combines logged retrieval, independent anchor verification, and partial-return recovery. `:24` inherits the rubric and packet schema from RESEARCH. `:181` supports COMPLETE/PARTIAL/FAILED_INPUTS; TASK's outer schema at `AGENT_TASK.md:396` has SUCCESS/FAILED/FAILED_INPUTS. `skills/research-orchestration/SKILL.md` additionally describes caller retry/resume and shared-packet practices.

**Changes.**
- **PROTOCOL:** Keep ground → freshness → retrieve/log → independently verify → return recoverable evidence. Remove repeated explanations of Type 1 ownership. Fix scaffolding before compression: the prescribed command (`:105`) generates its own packet name and updates `_LATEST` by default, while this role's writes are confined to supplied OUTPUT_DIR. Use explicit packet allocation and `--no-update-latest` for a packet-confined child; let the owner update pointers.
- **SPEC:** Consolidate the load-bearing rule repeated in invariants, protocol, validity, and rationale into one prominent obligation plus a concise packet validation reference. Preserve explicit PARTIAL coverage and READ/RUN distinctions.
- **STRUCTURE:** Keep a compact structured return contract; hydrate the shared research evidence schema rather than having the worker load the entire manager package for it. Define one packet ownership model across this role and research-orchestration.
- **RATIONALE/perimeter:** Reduce `:209–223` to the reason for independent verification and recoverability. Remove the argument that a generic brief would have to restate the method: existing skill hydration supplies a candidate alternative. Put runtime parameters and artifact schema details into a shared research contract.

**Persistent-role decision.** Independent verification can be expressed in a skill, just as claim calibration can in the governance-audit skill. The current reason to keep a smaller RESEARCHER during transition is concrete packet allocation, partial-return, and caller retry compatibility. A long-term dedicated identity would require a continuing context, tool, permission, or recovery responsibility beyond a hydrated method and normalized TASK contract. This inspection has not established one. The long-term choice stays open, with conversion to `TASK + research-evidence` favored if the recovery/ownership migration removes that distinction; a comparative behavioral probe could support a separate future role-design decision.

**Caller/recovery/decision dependencies.** RESEARCH frontmatter/dispatch (`AGENT_RESEARCH.md:3/:155`) and research-orchestration's resume/packet assumptions are live interfaces. D-GOV-13 remains applicable. A later conversion to `TASK + research-evidence` is plausible after PARTIAL status, packet allocation, ownership and retries are represented consistently; current TASK alone does not show that equivalence. Uncertainty: shared-packet collision behavior and resume semantics were inspected as contracts, not exercised.

**Probe.** A brief contains one false load-bearing anchor, retrieval is stale, and a tool fails after useful evidence is written. The candidate corrects or downgrades the anchor, preserves a usable partial packet, reports exact coverage gaps, and leaves unrelated pointers untouched.

## TASK

**Core and disposition — SLIM.** Complete one bounded assignment using its supplied method and return what happened in a form the caller can trust. Its enduring responsibility is faithful execution of the actual task contract, with explicit unresolved inputs and a clear account of results.

**Evidence.** `agents/AGENT_TASK.md:9–17` already states this compactly. `:122–187` performs path/token/brief normalization; `:208–222` parses skill metadata and intersects tool lists; `:254–320` describes run-record mechanics/checklists; `:323–380` repeats profile/separation guidance. Mechanical behavior occupies most of this package.

**Changes.**
- **PROTOCOL:** Keep receive effective contract → load method → execute → verify → return. Move token expansion, inline/file precedence, path containment, allowlist intersection, and run-record initialization into a candidate normalized-launch component that supplies explicit resolved values to the model. Preserve semantic assessment of ambiguous authority until a resolver can represent it faithfully.
- **SPEC:** Consolidate authorization once. Resolve missing-companion contradiction: `:205` stops the run, while checklist `:297` says “no error on absence.” Align managed read-only execution with Step 1 (`:532–533`), which unconditionally requests directory/record creation despite the runtime-record exception at `:239–242/:256`.
- **STRUCTURE:** Generate the machine record from normalized launch and execution evidence; provide a compact result schema to the model. Move deprecated profile parsing to a compatibility adapter. Deduplicate three descriptions of profile behavior (`:31`, `:55`, `:323`) and the repeated merge rules at `:512`.
- **RATIONALE/perimeter:** Keep the short rationale for variable skills and bounded briefs. Remove the naming convention and design guidance that tells a worker how to extend the architecture (`:354–380`); place that guidance in component-authoring documentation.

**Caller/recovery/decision dependencies.** This is an enabling change for proposed conversions, with wide caller impact. Standard §11, skills/README, managed-delegation launch generation (`managed-delegation.ts:384`), run-record consumers, G-role/path controls and native invocation modes must be tested together. A normalized-launch implementation is a proposed destination, not observed complete enforcement. Owner decision: which invocation classes receive the new normalization and what compatible fallback remains. D-GOV-13 approval is not attached to TASK, but root instruction-change governance still applies.

**Probe.** Compare inline/file path conflict, underscore skill alias, missing companion, narrowed allowlist, a managed read-only run, and an explicitly writable run. The concise role must receive an unambiguous effective contract and produce consistent results without duplicate or unauthorized records.

## Acceptance and limits

The proposals are based on source inspection, not measured model-performance comparisons. The relative benefit of a retained named role versus TASK plus a method remains an experimental question for AUDIT_EPISTEMIC and RESEARCHER. Conversion counts are architectural recommendations, not automatic deletions.

Suggested sequence: resolve contradictory live contracts; establish normalized launch/record and shared method hydration where needed; implement the two deterministic audit tools and their fixtures; migrate self-contained scoring/audit skills; migrate scaffold/research-adjacent producers once their ownership/recovery interfaces are reconciled; then assess larger reductions against the behavioral probes. A later rewrite should express each retained instruction through the four complementary sections, with a machine envelope the runtime actually understands.

No live change is accepted by this report. Parent fan-in must reconcile the Type 0/1 proposals, consumer inventory, governed decision scope, and downstream coordination before presenting an implementation tranche.
