# H2 launch brief — PIA-U10 Pi identity proposal

Instance ID: `H2-PI-IDENTITY`
Parent: `HELP_HUMAN / ROOT_FOUR_LANES_2026-08-02`
Role: `HELPS_HUMANS` (Agent 1)
Plan: `ORCHESTRATION_PLAN_V5.md` / `WORK_GRAPH_V5.json`

## Objective

Prepare PIA-U10's exact candidate implementation-identity options and a
versioned collision-proof identity schema for human G1 selection. Do not
select, approve, implement, dispatch, or supersede anything.

## Required reads

- `AGENTS.md` and full `agents/AGENT_HELPS_HUMANS.md`;
- plan-v5 surfaces and the final owner-ruling record;
- all E1/E2 Option A artifacts, especially `OPTION_A_IDENTITY_BASIS.json`,
  `OPTION_A_DECISION_GATES.md`, and PIA-U10 in `OPTION_A_WORK_UNITS.csv`;
- D-GOV-20 and the D-APP-84 Root route;
- relevant Root runtime contracts/registry/fingerprint/session-evidence
  sources and App adapter/composition sources, read-only.

## Allowed writes

- `execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/identity_proposal/`;
- this instance directory.

## Required outputs

1. `identity_proposal/BASIS.json`;
2. `identity_proposal/ROOT_PI082_IDENTITY_OPTIONS.md`;
3. `identity_proposal/CANDIDATE_IDENTITY.schema.json`;
4. `identity_proposal/IDENTITY_FIELD_MATRIX.csv`;
5. `identity_proposal/ARTIFACT_MANIFEST.csv`;
6. `RETURN.md`; and
7. `STATUS.json`.

## Acceptance checks

- At least four G1 choices: Root-wrapper canonical, App-host explicitly
  registered, converged Root concrete adapter, and continue hold.
- Each option names compatibility, ownership, migration, evidence, rollback,
  and later owning instruments without inventing authority.
- The schema separates upstream package/version from Chirality implementation
  family and binds exact source/build/profile/registration/policy/client/
  packaging identities needed to prevent same-descriptor collision.
- Mutable run/evidence facts are distinguished from stable identity fields.
- JSON/CSV parse, schema self-validation, candidate whitespace, hash manifest,
  and `git diff --check` pass.
- No project-loop, runtime/source/dependency/lock/decision/decomposition/
  register/lifecycle/release/Git write and no future work dispatch.

## Stop gate

Return a decision request to HELP_HUMAN for human G1 selection of one target
for validation only, amendment, or continue hold. State explicitly that no
choice is Pi approval or App supersession.
