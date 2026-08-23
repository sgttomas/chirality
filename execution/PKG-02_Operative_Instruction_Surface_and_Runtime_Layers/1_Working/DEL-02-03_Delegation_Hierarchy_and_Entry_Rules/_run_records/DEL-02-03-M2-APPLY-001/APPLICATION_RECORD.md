# Application Record

Status: `APPLIED`

## Exact instruction application

The literal command
`git apply docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/AGENTS.proposed.patch`
applied the ruled delta. Post-application `AGENTS.md` SHA-256 is
`377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.

A scratch reconstruction extracted basis `AGENTS.md` from `origin/main`,
applied the same literal patch with Git, reproduced that SHA-256, and compared
byte-identical to the live application candidate.

## Concordance disposition

Each named stale sentence was replaced once with the R1-A ruled wording:

> Agent 0 dispatches named Agent 1 managers and may directly dispatch bounded Agent 2 instances under the same sealed-brief, declared-scope, and durable-evidence requirements.

The replacements are one-line diffs in:

- `docs/WORKFLOW_COMPONENT_STANDARD.md` line 145;
- `docs/TYPES.md` line 202; and
- `docs/DBM_Agent_Instruction_Architecture.md` line 31.

No other byte in those three files changed. The Workflow-Component Design
Standard remains an external normative standard, not an agent.

## Governed record and manifest

- D-GOV-35 records R1-A under the D-GOV-34 pre-publication convention.
- The decision register adds one D-GOV-35 row.
- The proposal and packet README point to the ruled decision; the packet
  inventory uses its declared exact/normalized SHA conventions.
- Live manifest
  `ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml` uses branch-time basis
  `b143444bd497eae1b1b638670a33e6df756d9084`, carries R1-B, declares the full
  changed instruction surface, uses `human-gated-pr`, sets `self_merge: false`,
  and records routed notices plus the explicit public-export deferral.

## Routed notices

- `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`

Both notices identify the pre/post `AGENTS.md` SHA-256 values, the two
delegation classes, the `instruction-asserted` evidence boundary, and the
pinned/mirrored surfaces and receiving-loop follow-ons enumerated by
D-GOV-35 `IMPACT.md`. They are coordination, not authority.

## Lifecycle and derivative posture

DEL-02-03 `Current State` remains `INITIALIZED`; `_STATUS.md` received one
History line only. No hold was lifted. Root-owned
`exports/chirality-app/**` regeneration is explicitly deferred to the next
export release under R1-B. Historical App/Piping evidence remains immutable.
