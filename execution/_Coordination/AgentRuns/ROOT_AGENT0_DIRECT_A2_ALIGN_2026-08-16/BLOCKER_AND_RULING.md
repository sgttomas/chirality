# BLOCKER_AND_RULING — brief v1 edit (a) blocked; owner ruled Option 1

Run: `ROOT_AGENT0_DIRECT_A2_ALIGN_2026-08-16`
Basis: `origin/main@b67197f5b647fbf0b972eee158e94c7215db9e6c`

## Blocker found while executing brief v1 edit (a)

Edit (a) appended `TASK` to the `subagents:` frontmatter of
`agents/AGENT_HELP_HUMAN.md`. With that line applied (working blob
`2e4755d9258e3a8c1e594bdbca4965e962673343`):

```text
$ python3 tools/validation/validate_agent_instructions.py
ERROR AGENT0_CHILD_TYPE                  agents/AGENT_HELP_HUMAN.md: Agent 0 child TASK must be Agent 1

Summary: 34 files, 1 errors, 0 warnings
exit=1
```

With the frontmatter line at base bytes: `Summary: 34 files, 0 errors, 0
warnings`, exit 0.

### Root validator rule (verbatim)

`tools/validation/validate_agent_instructions.py` L270-271:

```python
            if agent_type == "0" and child_type != "1":
                add(findings, "ERROR", "AGENT0_CHILD_TYPE", rel, f"Agent 0 child {child} must be Agent 1")
```

L274-280 additionally reject `allow_generalist_agent2: true` on any non-Agent-1
file (`GENERALIST_PARENT_TYPE`, "only Agent 1 may allow ephemeral generalist
Agent 2 children").
`tools/validation/test_validate_agent_instructions.py` L167-183
(`test_hierarchy_rejects_agent0_to_agent2`) pins `AGENT0_CHILD_TYPE` as the
intended behaviour. The validator is registered in `tools/REGISTRY.md` L52; it
is not currently invoked by `.github/workflows/`.

### App harness type rule (read-only finding; verbatim)

`projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts`
L274:

```ts
    if (parentType !== 1 || frontmatter.allow_generalist_agent2 !== true) {
      throw new HarnessError('INVALID_REQUEST', 400, 'Ephemeral generalist Agent 2 is not allowed');
```

L289-290:

```ts
  if (parentType === 0 && childType !== 1) {
    throw new HarnessError('INVALID_REQUEST', 400, 'Agent 0 may delegate only to named Agent 1 roles');
```

`projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts`
L160-168:

```ts
    const expectedType = parentType === 0 ? 1 : 2;
    if (agentType !== expectedType) {
      console.error(
        `[harness/subagent-governance] Candidate subagent rejected: ${subagentName} declares AGENT_TYPE=${formatAgentType(
          agentType
        )}; expected TYPE ${expectedType}.`
      );
      continue;
    }
```

Verdict: the App harness BLOCKS Agent 0 -> TASK (L289-290) and Agent 0 ->
ephemeral generalist (L274) regardless of the frontmatter allowlist; a `TASK`
entry in HELP_HUMAN's allowlist would be logged as rejected on every
governance evaluation (L160-168). Aligning the harness is a separate App
product-code tranche.

## Options presented to the owner

1. Drop edit (a); land the prose alignment only; park frontmatter, root
   validator (+ test), and App harness alignment as explicit follow-ons.
2. Widen the tranche to amend the root validator and its test; App harness
   would still block at runtime.

## Owner ruling (CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING RECORD)

2026-08-16, Ryan Tufts, verbatim: "I want Option 1."

Effect: brief amendment v2 (see `LAUNCH_BRIEF.md`) — frontmatter reverted to
base bytes; prose edits (b), (c), (d) kept; one factual sentence added to the
"Managers own management" bullet naming the still-enforcing surfaces; the two
follow-ons below are parked and stated in every notice.

## Parked follow-ons

- ROOT: `tools/validation/validate_agent_instructions.py` L270-280 and
  `tools/validation/test_validate_agent_instructions.py` L167-183, together
  with the `subagents: ... TASK` frontmatter alignment of
  `agents/AGENT_HELP_HUMAN.md`, in one later root tranche.
- APP: `managed-delegation.ts` L274, L289-290 and `subagent-governance.ts`
  L160-168 plus their tests, an App product-code tranche under App's own
  review posture.
