# Amendment 01 — audit tool partition and workflow stages

Authority: parent HELP_HUMAN authorized a fourth bounded writer for independent audit repairs within the accepted 3–5 worker arrangement. Observed native spawn returned `/root/working_items/audit_tools`.

The audit worker owns `tools/evaluation/`, `tools/coordination/analyze_dep_closure.py`, and `tools/coordination/test_analyze_dep_closure.py`, plus its evidence subtree. Those paths are removed from runtime_tools ownership. The originally proposed `tools/audit_dep_closure/` directory does not exist; inspection established the exact analyzer location. Other coordination tools remain with runtime_tools. All participants received the scope amendment through this parent.

The optional execution contract supports `stages: {name: {compatible_roles, tools}}`. A bounded TASK stage in an orchestration workflow must be explicitly compatible. Stage restrictions are composed with, and do not widen, outer capability and command restrictions. Design owner has been informed.

Audit CLI agreement: `audit_dependencies.py --root PATH --output report.json`; `audit_structure.py --root PATH --output report.json --variant PROJECT|SOFTWARE|DOMAIN [--inventory JSON] [--isolated-migration --migration-authority VALUE]`. Reports distinguish run_status from subject_status; a completed audit with findings is not an execution failure. Exact inventory semantics are documented with the tool.
