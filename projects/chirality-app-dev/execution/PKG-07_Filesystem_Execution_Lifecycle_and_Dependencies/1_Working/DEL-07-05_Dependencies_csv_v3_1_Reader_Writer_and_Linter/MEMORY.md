# MEMORY - DEL-07-05

## Runs

- 2026-09-27 — `APP-REMOVE-LEGACY-FORMS-2026-09-27` (SCA-APP-011 code change; checkpoint-group-3 candidate, lands with the SCA-APP-011 scope text after group-3 acceptance): removes the dependency route and `fetchDeliverableDependencies`. The dependency read, write, recorded-register, write-failure and symlink cases move to `frontend/src/__tests__/lib/deliverable-contracts.test.ts` and call the library directly. No lifecycle change. Evidence: [receipt](../../../_Coordination/AgentRuns/APP-REMOVE-LEGACY-FORMS-2026-09-27/RECEIPT.md); amendment `execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/`.
- 2026-09-26 — `APP-RECORDED-REGISTER-2026-09-26` (follow-up FU5): the new
  `frontend/src/lib/dependencies/recorded-register.ts` reads the recorded
  register, the union of the `_DEPENDENCIES.md` declared sections (legacy
  headings included) and `Dependencies.csv`, and judges each arc by its
  supplier. It covers the D-GOV-49 accepted-DAG split with `DAG_PENDING`. The
  dependencies API, MCP `deps_read` and the workbench/pipeline panels expose it
  additively as `recordedRegister`. The CSV rows stay as register evidence.
  Parity fixtures check it against the Root tools. No lifecycle change and no
  dependency acceptance. Evidence:
  [receipt](../../../_Coordination/AgentRuns/APP-RECORDED-REGISTER-2026-09-26/RECEIPT.md).
- 2026-09-27 — `APP-EXECUTION-ROOT-2026-09-27`: a deliverable's recorded-register
  read now takes its execution root from the outermost `execution/` folder,
  checked against the adapter manifest, as the reopening checks do, instead of
  from the path shape. A deliverable not exactly at
  `<execution root>/PKG-*/<lifecycle folder>/DEL-*` gets `NOT_ASSESSED` with a
  warning. No lifecycle change and no dependency acceptance. Evidence:
  [receipt](../../../_Coordination/AgentRuns/APP-EXECUTION-ROOT-2026-09-27/RECEIPT.md).

## Decisions And Evidence

- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-077: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.

- 2026-07-12 - D-APP-56 R5 P45 executed UPD-133: current kit/register metadata now reflects live ruled state; dated history and genuine TBD/gates remain preserved. No lifecycle transition occurred.

- 2026-09-22 — D-APP-131: bounded R5 repair and R6 backcheck recorded in `execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/R6_2026-09-22/`. Current work is only in `_STATUS.md ## Remaining`; prior evidence and lifecycle remain unchanged.

## Record closeout — 2026-09-22

D-APP-131/132 and D-GOV-43/D-APP-127 now govern the current ScopeOfWork and Remaining interpretation. Earlier SDK/daemon, four-file, matrix/default-role, source-MATCH and pre-release planning statements remain dated history. Current work, owning surface, checks and gates are in `_STATUS.md`; the W07_10_ROWS.csv derivative accounts for original residual keys. No lifecycle/approval-SHA refresh, product completion, new native result, or release is asserted.
