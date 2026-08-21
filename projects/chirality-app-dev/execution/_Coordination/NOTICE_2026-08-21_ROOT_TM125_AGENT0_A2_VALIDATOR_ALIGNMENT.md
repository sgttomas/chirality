# Routed Change Notice — Root TM-ROOT-125 Agent 0 / Agent 2 Alignment

Date: `2026-08-21`

From: `Chirality Root / HELP_HUMAN`

To: `Chirality App loop`

Status: `COORDINATION ONLY — NOT AUTHORITY`

The App loop adopts, acknowledges, amends, declines, or defers any local
response through its own instruments and cadence.

## Exact Root change

Root candidate tranche `ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821`
implements the Root-owned `TM-ROOT-125` alignment:

- `agents/AGENT_HELP_HUMAN.md` now allowlists canonical `TASK` and declares
  `allow_generalist_agent2: true`; its stale sentence saying that the Root
  validator and App harness still enforce Agent-1-only children was removed.
- `tools/validation/validate_agent_instructions.py` now admits an Agent 0
  child only when it is Agent 1 or the exact `TASK` role with Agent type 2;
  any other named Agent 2 remains `AGENT0_CHILD_TYPE` error.
- The same validator now permits `allow_generalist_agent2: true` on Agent 0
  or Agent 1 only; Agent 2 remains `GENERALIST_PARENT_TYPE` error.
- `tools/validation/test_validate_agent_instructions.py` pins the narrow
  positive paths and the non-`TASK`, unresolved-role, and Agent-2-generalist
  failing paths.

`AGENT_HELP_HUMAN.md` changed from Git blob
`f3901408e7d5f040cb1d52e6033152ccb2bf3ade` / SHA-256
`f0640b092c12f0f847e0d8df2786ca46bdf916f33e3330bdc54e202c788cbde3`
to candidate Git blob `a9e538c0d9603e18d9884e9f60489be6df8ba1ff` /
SHA-256 `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`.

The change does not broaden HELP_HUMAN write scope or human authority. The
existing sealed-brief, declared-context, tool, permission, containment,
durable-evidence, manager-validation, and Agent-2 non-delegation gates remain.
No App harness or product source changed in this Root tranche.

## App follow-on requested by its existing instruments

After the Root tranche lands, run the DEL-08-04 post-Root cross-surface
integration check already recorded in DEL-08-04 `## Remaining`, against the
App harness implementation at commit
`ac2cd801a06a0679bc86830c627218ccca78b658` and App Receipt 172. Confirm:

1. configured Agent 0 admission of allowlisted canonical `TASK` Agent 2;
2. configured Agent 0 admission of an explicitly enabled ephemeral
   generalist;
3. fail-closed rejection of unsupported named Agent 2, unresolved, missing
   opt-in, and Agent-2-parent routes; and
4. the affected Root validator/tests plus App `managed-delegation` and
   `harness-subagent-governance` checks pass together.

This is the reciprocal coordination notice requested by Root closeout. It is
not App acceptance, activation, lifecycle change, release, reliance, or
authority to edit Root surfaces.

## Pin and derivative census

No `agents/AGENT_HELP_HUMAN.md` entry exists in App's live
`execution/_Reconciliation/References/AUTHORITY_CORPUS.json`. The immutable
DEL-09-06 packaged-security instruction-root manifests/summaries and the
D-APP-86 parity baseline `SOURCE_MANIFEST.sha256` / `PACKAGE_MANIFEST.sha256`
do pin the prior SHA-256 above. They remain valid historical evidence of their
recorded runs, but are stale as evidence of current Root instruction bytes.
Do not overwrite them; regenerate only through the App-owned evidence or
release workflow if current-byte proof is required.

The older Agent-1-only narrative in Root `docs/TYPES.md` section 4.3,
`docs/WORKFLOW_COMPONENT_STANDARD.md` section 4.1, and
`docs/DBM_Agent_Instruction_Architecture.md` section 2 was outside this
bounded tranche's writable scope. Its concordance disposition remains a
separate Root-owned follow-on; this notice does not ask App to resolve it.

Root evidence: this notice; the tranche manifest; and
`execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/`.
