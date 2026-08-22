# Root Task Management closeout — TM-ROOT-125 (2026-08-21)

Status: **OWNER-RULED RESOLVED_WITH_CHANGE — ENGINEERING LANDED ON TASK BRANCH**

Invoking loop: Root

Branch: `codex/root-cross-loop-carriers-20260821`

Engineering evidence commit:
`702d88a4c14a291f647c2a2e6e5fa40185839318`

This record is Task Management closure evidence. It records the owner's
disposition of `TM-ROOT-125`; it is not semantic acceptance, an App-loop act,
release, publication, reliance, PR approval, or merge authority.

## Governing owner act

The owner directed:

> On landing, close TM-ROOT-125 per your register's rules and route the
> reciprocal coordination notice to the App loop naming exactly what changed.

The complete in-session direction is transcribed as
`CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING RECORD` at
`execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/OWNER_DIRECTION_TRANSCRIPT_2026-08-21.md`,
SHA-256
`88949cedbc1b20141b530275ccfef3dd0687f0a574fe9e1d94972f8c29ffdeff`.
The quoted direction, together with the landed engineering evidence commit,
authorizes this `RESOLVED_WITH_CHANGE` register disposition. It supplies no
ruling for `TM-ROOT-117` or either `DEL-02-06` decision gate.

## Nine-domain completeness scan

| Domain | Closure basis |
|---|---|
| Action Item | The validator/frontmatter mismatch stated by `TM-ROOT-125` is repaired in the engineering commit. |
| Assignment | `HELPS_HUMANS` produced and validated the instruction-surface tranche; `TASK_MANAGEMENT` records the owner-ruled closure; accountable authority remains human-only. |
| Prioritization | The owner selected this objective as the engineering product of the present cross-loop-unblock session. |
| Deliverables | The resolution lands in `agents/AGENT_HELP_HUMAN.md`, the Root instruction validator and tests, the G4 tranche manifest, and routed coordination notices. |
| Work | Canonical `TASK` and explicit Agent-0 generalist opt-in were admitted narrowly; the superseded negative test was replaced and the remaining rejection paths were pinned. |
| Planning | The engineering dependency commit precedes this register closure; App's later cross-surface check remains App-owned. |
| Approval | This row closes only under the quoted owner direction; PR review and merge remain separate owner acts. |
| Checking | Root validation, narrow policy tests, G0-G4, candidate-range G4 on the branch merge base, and App focused support tests passed as recorded below. |
| Decisions | `TM-ROOT-125` is disposed `RESOLVED_WITH_CHANGE`; no unrelated human-only decision is inferred. |

## Exact implemented change

- `agents/AGENT_HELP_HUMAN.md` now allowlists canonical `TASK`, declares
  `allow_generalist_agent2: true`, and no longer says the now-aligned Root
  validator and App harness remain Agent-1-only.
- `tools/validation/validate_agent_instructions.py` permits an Agent 0 named
  child only when the child is Agent 1 or the exact canonical `TASK` role with
  Agent type 2. Every other named Agent 2 remains rejected as
  `AGENT0_CHILD_TYPE`.
- The validator permits `allow_generalist_agent2: true` only on Agent 0 or
  Agent 1. Agent 2 remains rejected as `GENERALIST_PARENT_TYPE`.
- `tools/validation/test_validate_agent_instructions.py` pins the positive
  Agent-0-to-`TASK` and Agent-0-generalist paths and preserves fail-closed
  coverage for non-`TASK` Agent 2, unresolved children, and Agent-2 parents.
- The same commit ships the G4 manifest
  `ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821` and the required routed
  change notices.

The implementation does not expand HELP_HUMAN write scope, make Agent 2 a
manager, permit Agent 2 delegation, or waive sealed briefs, declared context,
tools, permissions, write containment, durable evidence, manager validation,
or human gates.

## Evidence identities

| Artifact | SHA-256 |
|---|---|
| `agents/AGENT_HELP_HUMAN.md` | `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981` |
| `tools/validation/validate_agent_instructions.py` | `c99e913ab67ebcbc53cb3487baf0d79fe4d05466ff32bc834124e952157dded1` |
| `tools/validation/test_validate_agent_instructions.py` | `e244a10f5b4558946baf3fad265903c4aa871b80eb5f6adbec0e9e7113a614f7` |
| `docs/governance_harness/tranche_manifests/ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821.yaml` | `83b678a2f98897aeb7e3e678e9f7c19b7910fc00222ee0666e5b1885df80d402` |
| H1 return | `c18e1f32e07c1e61f7aa0ef8f2e70fb83e210da107c95e102708e5919e34b72a` |
| HELP_HUMAN fan-in validation | `1c84957b347043a951b797389f45287a37c1b754d0e30246363268aaaf4359dc` |

## Validation evidence

- Full Root validation suite: `319 passed`.
- Live agent-instruction validation: `34 files, 0 errors, 0 warnings`.
- Narrow validator policy suite rerun after the dependency commit: `19 passed`.
- Instruction entrypoints: `PASS`.
- Governance harness G0-G4: `PASS`; all 40 manifests schema-valid.
- Post-commit G4 candidate range from branch merge base
  `e3e18d27740018efd12e73193c02395a9eca93c2..702d88a4c14a291f647c2a2e6e5fa40185839318`:
  `PASS`, 21 changed paths, 4 instruction-surface paths, one applicable new
  manifest.
- App focused support tests on byte-identical source/test inputs: `32 passed`
  across the managed-delegation, harness-subagent-governance, and
  coordination-tools files.
- Diff hygiene: `PASS`.

The literal two-dot check `origin/main..HEAD` was not used as proof after the
tracking ref advanced from the run basis to
`7d5a3f558dfa2e8e902df25fc9a3e813a9ab7048`: it includes four upstream-only
instruction paths absent from this branch and therefore blocks. The governed
branch-candidate range from the common ancestor passes. Final CHANGE closeout
must still evaluate PR mergeability against current `origin/main`; no sync
merge, rebase, or merge result is inferred here.

## Routed coordination and derivative disposition

- App reciprocal notice:
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`,
  SHA-256
  `eb765dc3bebbf9dd84842643fb22aa989539513843647b562098c96468547864`.
  It names the App-owned DEL-08-04 post-Root integration check against App
  commit `ac2cd801a06a0679bc86830c627218ccca78b658` and Receipt 172.
- Piping notice:
  `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`,
  SHA-256
  `858ead7d3a013b2aa9ea7b49dab1a6408030d24a9befb0cb383a5c23a86f9c72`.
- Tier-0/domain-engine notice:
  `_DomainEngines/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`,
  SHA-256
  `60f37ec3a92b7e6e6918c34b142361bb77598b0df561da3937d1fc1c81c48019`.

The notices are coordination, not authority. Existing App DEL-09-06
instruction-root evidence and the D-APP-86 parity baseline SHA-pin the prior
HELP_HUMAN bytes. Those immutable derivative packages remain untouched;
current-byte regeneration is deferred to their App-owned workflows.

## Recorded residuals and closure boundary

`docs/TYPES.md` section 4.3,
`docs/WORKFLOW_COMPONENT_STANDARD.md` section 4.1, and
`docs/DBM_Agent_Instruction_Architecture.md` section 2 retain older
Agent-1-only narrative. They were outside this bounded tranche and remain a
separate Root-owned concordance residual. That residual does not negate the
exact validator/frontmatter repair named by `TM-ROOT-125`, but it prevents a
claim of complete repository-wide prose concordance.

Closure quote used in the archived row:

> Engineering commit 702d88a4c admits Agent 0 to canonical TASK and explicit
> generalist opt-in while preserving all other named-Agent-2 fail-closed paths;
> routed notices and validation are recorded here.

No artifact-proof label applies. No merge was performed.
