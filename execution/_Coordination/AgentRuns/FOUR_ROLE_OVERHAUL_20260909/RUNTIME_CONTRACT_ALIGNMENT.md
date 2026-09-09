# Runtime contract alignment

Inspected `tools/workflow_runtime/normalize_brief.py`, `resolve_workflow.py`, and
`README.md`. Shared contract now documents their structured brief selection,
precedence, paths, legacy profile label, ApplyEdits behavior, command policy
layers, and explicit resource selection. No whole-workflow compatibility
override is documented. Prose interpretation and host enforcement remain with
the caller/host.

The resolver result's tool_root naming ambiguity was relayed to HELP_HUMAN:
SPEC's command-layer TOOL_ROOT is instruction_root/tools, while legacy tools/...
expressions resolve against instruction_root. CLI --root is instruction_root.
The shared contract uses those meanings without depending on the ambiguous
result key. Final executable checks and any field correction remain with the
implementation worker and independent reviewer.
