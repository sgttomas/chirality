# Sealed launch brief — A2-READONLY-BACKCHECK

RunID: `ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03`

PlanVersion: `2`

Parent: `HELPS_HUMANS` Agent 1 under `HELP_HUMAN`

Child form: fresh ephemeral generalist Agent 2; no delegation permitted

Selection authority: signed `TM105-A` and Owner Addition 3, ruling transcript
SHA-256 `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`

## Purpose

Independently backcheck the repaired TM105 carrier. Recompute the evidence
manifest and inspect the full repaired package, not merely the manager's repair
description. Verify closure of initial refutation findings B-01 through B-03
and NB-01 through NB-02, then adversarially test the complete package for any
new blocking issue.

## Declared context

- `AGENTS.md`
- `agents/AGENT_HELPS_HUMANS.md`
- all manager-authored files at this run root
- `instances/A2-READONLY-REFUTATION/RETURN.md`
- source files listed in the repaired `EVIDENCE_MANIFEST.tsv`, only as needed

## Frozen repaired review basis

| Artifact | SHA-256 |
|---|---|
| `ORCHESTRATION_PLAN.md` | `b3eb262bb92d752942ae6bad3e8ac4a68720ca70da11c64dfa96c13490450e72` |
| `EVIDENCE_MANIFEST.tsv` | `2dbac7d2e106608201176eed454eaec4b28ef4aa49810e35841fda27d7819b7d` |
| `CONTRACT_CANDIDATE.md` | `5d5ae4e9fbdc5de469d657c7fe036dab291b948df0afb67ecd3d987b80e51fa6` |
| `CONTRACT_MATRICES.json` | `23ead45e551c8b25e6631eb93f47af8e2b5c34caba6240c2dc2f481fd48f3ef4` |
| `CONSUMER_LOCAL_BOUNDARY.md` | `c2abb01c544833b2657a8af8f61fe3264284ff6f9ae15c07139e2e92db11dab9` |
| `AFFECTED_SURFACE_COMPATIBILITY_MAP.md` | `2cd1cbdccf28084c5257e4d9ada164803f5842a14201b24ae935b035ef74e405` |
| `OPEN_DECISIONS_AND_ACCEPTANCE_FORM.md` | `911839b8cf73dee10e740963ed7c95a5d4350fc30d11bbb412fe017f8329ff8e` |
| `instances/A2-READONLY-REFUTATION/RETURN.md` | `1b11a2642527a41a54be7eae95aa05a7e39759836a00d4e0c9fd56faf7338b7f` |

These hashes freeze the semantic review basis. Do not treat later manager
artifacts such as validation, package manifests, returns, or handoff files as
inputs to this backcheck.

## Permissions and write target

- Read: repository and this run carrier.
- Write: only
  `execution/_Coordination/AgentRuns/ROOT_TM105_GENERIC_CONTRACT_CANDIDATE_2026-08-03/instances/A2-READONLY-BACKCHECK/RETURN.md`.
- No canonical, register, notice, lifecycle, source/test, App/Piping, or Git
  changes. No network. No delegation. Do not edit manager-authored artifacts or
  the first review return.

## Required return

Write `RETURN.md` with:

1. `PASS`, `PASS_WITH_NONBLOCKING_FINDINGS`, or `FAIL` verdict;
2. verified ruling hash, evidence-source hashes, and repaired artifact hashes;
3. one explicit disposition for each B-01/B-02/B-03/NB-01/NB-02;
4. complete checks for authority calibration, all TBDs and ownership,
   identity/capability/audit/interruption/budget/fail-closed matrices,
   consumer-local boundary, no fallback, compatibility/currentness, and next
   human gate;
5. any new blocking/non-blocking findings with exact evidence;
6. confirmation that only the allowed return was written; and
7. rerun trigger.

Acceptance: no unresolved blocking finding. `PASS` validates only candidate
package consistency and does not accept semantics or authorize implementation.
