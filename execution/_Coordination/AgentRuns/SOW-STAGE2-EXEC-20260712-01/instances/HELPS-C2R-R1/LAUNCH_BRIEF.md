# HELPS-C2R-R1 Launch Brief — v1

Role: `HELPS_HUMANS` (Agent 1 root consumer repair owner)

## Objective

Repair the two root content/authority defects confirmed by RECON-C2F and
EVAL-C2F without changing the accepted transition contract:

1. Dual-format migration authority must equal exactly
   `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`; a merely syntactic or
   self-bound alternative must fail closed.
2. ISSUED preparation must require, validate as a bounded single-line value,
   and embed an explicit accepted-basis input in addition to the source
   commit, four source hashes, and status hash. This preparation remains
   lifecycle-neutral and does not satisfy H1.

## Basis

D-GOV-16 items 4, 6, and 8; accepted Stage-2 plan; C2R initial candidate and
tests; RECON-C2F and EVAL-C2F blocked evidence; C2F-REMEDIATION-001.

## Exact write scope

- `tools/scope_of_work/common.py`
- `tools/scope_of_work/convert_four_documents_to_scope_of_work.py`
- `tools/scope_of_work/test_scope_of_work_tools.py`
- `tools/reporting/test_generate_coverage_csv.py` (fixture authority refresh
  only; discovered by the mandated full-suite dependency)
- `skills/scope-of-work/BRIEF_SCHEMA.md` only if needed to name the concrete
  ISSUED accepted-basis input
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P2_ROOT/**`
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/HELPS-C2R-R1/**`

No other source path may change without a versioned parent amendment. Preserve
all existing dirty work. Do not delegate children.

## Required behavior and checks

- exact ruled authority succeeds in isolated path-scoped dual mode;
- `D-GOV-16@0123456`, another valid-looking SHA, malformed authority,
  missing authority, mismatched marker, non-isolated mode, and wrong path fail
  closed as applicable;
- SOW-only and complete legacy-only behavior remain unchanged;
- ISSUED conversion fails without accepted basis and succeeds only with all
  required bindings, embedding each exactly while leaving `_STATUS.md`
  byte-identical;
- add focused regression coverage, run focused Scope-of-Work tests and the
  full root tools suite, agent/skill checks if the skill schema changes,
  compile/diff/containment checks, and refresh C2R hashes/manifests/results.

## Denied and return

No deliverable/project/domain edits, conversion run, lifecycle/status act,
Git operation, release, H1/H2 action, or legacy retirement. Return `PASS |
PARTIAL | BLOCKED | DECISION_REQUIRED` with exact changed paths/hashes, test
evidence, blocker closure, remaining blockers, rerun requirements, and next
owner. Write terminal RETURN.md and STATUS.json.
