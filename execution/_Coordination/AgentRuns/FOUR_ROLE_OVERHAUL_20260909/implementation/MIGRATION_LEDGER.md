# Four-role migration ledger

Root implements the user-approved replacement under D-GOV-41. This ledger supersedes the earlier audit roster recommendations while preserving those reports as evidence. It records all 34 original agent packages and 45 original method packages; the machine ledger also maps all 183 original package files and records source/destination hashes.

Status: implementation complete, final review and validation passed. App and Runtime adoption remains held.

## Agent dispositions

| Original role | Result | Destination |
|---|---|---|
| AGGREGATION | workflow | `workflows/aggregation/WORKFLOW.md` |
| AUDIT_AGENTS | workflow | `workflows/audit-agents/WORKFLOW.md` |
| AUDIT_DECOMP | workflow | `workflows/audit-decomp/WORKFLOW.md` |
| AUDIT_DEP_CLOSURE | workflow | `workflows/audit-dep-closure/WORKFLOW.md` |
| AUDIT_EPISTEMIC | workflow | `workflows/audit-epistemic/WORKFLOW.md` |
| AUDIT_GOVERNANCE | workflow | `workflows/audit-governance/WORKFLOW.md` |
| AUDIT_HYPERGRAPH_CLOSURE | workflow | `workflows/audit-hypergraph-closure/WORKFLOW.md` |
| AUDIT_SCOPE_CLOSURE | workflow | `workflows/audit-scope-closure/WORKFLOW.md` |
| CHANGE | workflow | `workflows/change/WORKFLOW.md` |
| DBM_PUBLISHER | workflow | `workflows/dbm-publisher/WORKFLOW.md` |
| DOMAIN_DECOMP | workflow | `workflows/domain-decomp/WORKFLOW.md` |
| DOMAIN_ENGINE | workflow | `workflows/domain-engine/WORKFLOW.md` |
| DOMAIN_HYPERGRAPH | workflow | `workflows/domain-hypergraph/WORKFLOW.md` |
| DRAWING_EXTRACT | workflow | `workflows/drawing-extract/WORKFLOW.md` |
| EQUATION_AUDIT | workflow | `workflows/equation-audit/WORKFLOW.md` |
| EVALUATION | merge-workflow | `workflows/evaluation-protocol/WORKFLOW.md` |
| EVALUATION_DEPENDENCY_AUDIT | tool | `tools/evaluation/audit_dependencies.py` |
| EVALUATION_REPORT | workflow | `workflows/evaluation-report/WORKFLOW.md` |
| EVALUATION_STRUCTURE_AUDIT | tool | `tools/evaluation/audit_structure.py` |
| HELPS_HUMANS | retain-role | `agents/AGENT_HELPS_HUMANS.md` |
| HELP_HUMAN | retain-role | `agents/AGENT_HELP_HUMAN.md` |
| PDF2MD | workflow | `workflows/pdf2md-orchestration/WORKFLOW.md` |
| PREPARATION | workflow | `workflows/preparation/WORKFLOW.md` |
| PROJECT_DECOMP | workflow | `workflows/project-decomp/WORKFLOW.md` |
| PROJECT_SETUP | workflow | `workflows/project-setup/WORKFLOW.md` |
| RECONCILIATION | workflow | `workflows/reconciliation/WORKFLOW.md` |
| RESEARCH | merge-workflow | `workflows/research-orchestration/WORKFLOW.md` |
| RESEARCHER | workflow | `workflows/researcher/WORKFLOW.md` |
| REVIEW | workflow | `workflows/review/WORKFLOW.md` |
| SCOPE_CHANGE | workflow | `workflows/scope-change/WORKFLOW.md` |
| SOFTWARE_DECOMP | workflow | `workflows/software-decomp/WORKFLOW.md` |
| TASK | retain-role | `agents/AGENT_TASK.md` |
| TASK_MANAGEMENT | workflow | `workflows/task-management/WORKFLOW.md` |
| WORKING_ITEMS | retain-role | `agents/AGENT_WORKING_ITEMS.md` |

## Existing method packages

All 45 keep their existing folder names under workflows/ and use WORKFLOW.md.
Project/knowledge packages retain selected brief/tool/check resources; document
packages consolidate those contracts into CONTRACT.md. The 183 original file
destinations are explicit in MIGRATION_LEDGER.json. Legacy package status and
historical schema literals remain identified. New orchestration receives
WORKING_ITEMS; bounded contributions receive TASK or an ephemeral Type 2.

## Retained-role content and intentional omissions

WORKING_ITEMS’ package activation, software activation, and representation
migration methods move into selected project-setup, software, and scope-of-work
resources. TASK normalization and policy contracts move into the Root resolver,
structured-brief adapter, and runtime documentation. Source policy ceilings move
into agents/registry.json; workflow restrictions remain separate.

The human explicitly excluded NEXT_INSTANCE_PROMPT and NEXT_INSTANCE_STATE
contracts from workflows and resources. Their frozen source evidence remains;
INTENTIONAL_OMISSIONS.json records the removed passages. The new workflow library
contains neither contract. The four role descriptions preserve the agreed roles,
including HELPS_HUMANS’ reflective design relationship.

## Verification and adoption

Concrete audit repairs and verification are recorded in each child return:
project_workflows/RETURN.md, document_workflows/RETURN.md, runtime_tools/RETURN.md,
and audit_tools/RETURN.md. Fresh integration review and final checks are separate
from author reports. MIGRATION_VALIDATION.json verifies source coverage, original
Git hashes, destinations, aliases, links, the human exclusion, and preservation
of the downstream referenced corpus.

Five routed notices identify downstream consumers, authority corpus snapshots,
SHA-pinned mirrors, and adoption work. Existing accepted records retain their
original bytes. Export staging carries the adoption hold; this tranche neither
adopts the format for downstream loops nor publishes a release.

## Tool implementation precision

The new shared deterministic replacements are audit_structure.py and
 audit_dependencies.py under tools/evaluation/. The existing dependency-closure
analyzer is repaired and its report schema is versioned. Scaffolding, research
allocation, brief builders, validators, the resolver and structured adapter have
the recorded integration changes and tests.

The hypergraph-closure workflow retains direct CSV inspection and its existing
per-run analyze_hypergraph_closure.py evidence contract, with corrected vocabulary
and optional-check treatment. This tranche does not claim that a new reusable
hypergraph snapshot-validator CLI was implemented. Earlier audit suggestions for
such additional shared tools remain design candidates; their proposed existence
is separate from the concrete contradiction repairs in the accepted migration.
