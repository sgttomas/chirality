# Sealed Agent 2 author brief

RequestedBy: `/root/pec_d84_repair` WORKING_ITEMS Agent 1 under HELP_HUMAN. RunID: `D84_SCANNER_REPAIR_2026-09-05`. PackageID: `PKG-01`. DeliverableID: `DEL-01-05`. Role and non-delegation are instruction-asserted. Do not delegate.

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; set `WORKING_ROOT={REPO_ROOT}/projects/pec`. Read root/project `AGENTS.md`, `projects/pec/loop/LOOP_INIT.md`, `agents/AGENT_TASK.md`, `docs/SOFTWARE_WORKFLOW_PROFILE.md`, `skills/software-bounded-implementation/SKILL.md`, this activation and brief, D-PEC-84 S-A/L rulings, selected `SCANNER/{PROPOSAL.md,TARGETS.json,REGRESSION_PLAN.md}`, and `FULL_02/R4_DECISION_PACKETS/SCANNER_EXACT_ACTS_AND_EVIDENCE.md`.

Objective: implement exactly two scanner repairs: (1) recognize import-derived aliases of the dynamic callable `importlib.import_module`, including module, from-import, and assignment aliases, while preserving the conservative dynamic-import BLOCK policy; (2) recognize bound and unbound `socket.sendto` and extract its operation-specific destination without treating payload or flags as endpoint evidence. Unknown or ambiguous recognized calls fail closed.

ApplyEdits: true.

Allowed product write targets only:

- `projects/pec/v2/tools/check_service_core_posture.py`
- `projects/pec/v2/tests/enforcement/test_dependency_assertion.py`
- `projects/pec/v2/tests/enforcement/test_locality_assertion.py`

Allowed evidence writes only beneath the run root:

- `BASIS/READ_MANIFEST.json`, `BASIS/HOLD_PREFLIGHTS.json`, `BASIS/TARGETS.json`, `BASIS/PREIMAGES/{checker.py,dependency_test.py,locality_test.py}`
- `AUTHOR/CHANGE_MAP.json`, `AUTHOR/POSTIMAGE_HASHES.json`, `AUTHOR/HANDOFF.md`
- `CHECKS/BEFORE_PROBES.json`, `CHECKS/AFTER_PROBES.json`, `CHECKS/REGRESSION_RESULTS.json`, `CHECKS/UNITTEST.log`, `CHECKS/POSTURE_CHECK.json`, `CHECKS/COMMANDS.json`, `CHECKS/CONTAINMENT.json`

Do not write `ACTIVATION.md`, `BRIEFS/**`, `DISPATCH_RECORDS.json`, `VERIFICATION/**`, `BACKCHECK/**`, `ROLLBACK/**`, root `OUTPUT_MANIFEST.json`, or root `HANDOFF_STATE.md`.

Before mutation, reproduce all three TARGETS preimages, the live `IN_PROGRESS` status hash, observable origin/main authority, branch basis, and all exact production `dispatch-for-production` and `rely-for-production` holds. Preserve byte-exact copies of the three preimages under `BASIS/PREIMAGES` using `apply_patch`. Stop on drift or a denied/malformed hold.

Capture both exact hashed counterexamples before the repair. Record the checker false-negative PASS outputs separately from an intentional before-state run of the new regression assertions that fails. Fixtures are source text parsed by the checker only; never import or network-execute them. Use scratch TMP/cache paths only; run no live service or non-scratch database.

Dependency acceptance matrix: exact aliased probe; `import importlib as lib`; unaliased and aliased from-import; assignment alias; literal dynamic third-party, stdlib, and workspace names all BLOCK under unchanged policy; unknown dynamic name BLOCK; static stdlib and admitted workspace controls PASS; direct/transitive third-party imports BLOCK; bare unrelated local callable is not newly classified as importlib. Findings identify importer and line and are deterministic once per call.

UDP acceptance matrix: bound two/three positional overloads and unbound three/four positional overloads; module/class/instance/callable aliases and inline constructor; external destinations BLOCK and report the actual endpoint even when payload resembles loopback; IPv4 loopback, IPv6 loopback including extra tuple fields, and local Unix destinations PASS even when payload resembles an external host. Pin the AST convention for `address=` with clear payload and optional flags. `host=`/`url=` without `address`, no destination, starred args, `**kwargs`, excessive arity, duplicate destination positions, unknown variables/expressions, or multiple possible bindings that do not all yield local destinations BLOCK fail-closed. No general constant propagation.

Preserve existing RF-002 HTTP/socket/urllib, direct/transitive dependency, registration failure, induced unreadable/tool-failure, and local transport regressions. Execute from `projects/pec` with recorded Python 3.10+ identity, `PYTHONDONTWRITEBYTECODE=1`, and scratch TMP/cache:

- `python3 -m unittest discover -s v2/tests/enforcement -p 'test_*.py'`
- registered `v2-core-posture` exact command from `software-workflow.json`
- any additional owning packet checks explicitly required by the accepted profile/LOOP_INIT for the changed tool, without running a service

Record actual total tests and added cases. Hash target files before/after plus evaluated core tree, config, and workflow; core/config/workflow bytes must remain unchanged. Confirm no source, fixture, or ignored-state pollution from checks. `git` is read-only for inspection; do not stage, commit, push, branch, merge, reset, restore, or amend.

Return the exact changes, evidence paths, checks, containment, finite limitations, residual blockers, and verifier inputs. Do not claim artifact acceptance, CHECKING, release, universal scanner completeness, VER-004/OI-009 closure, or Remaining application. Escalate any required extra path, policy change, ambiguous requirement, drift, hold, or unrelated worktree overlap.
