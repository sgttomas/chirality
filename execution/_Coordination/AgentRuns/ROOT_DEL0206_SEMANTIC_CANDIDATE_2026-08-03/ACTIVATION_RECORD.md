# Activation record — ROOT_DEL0206_SEMANTIC_CANDIDATE_2026-08-03

- Status: `ACTIVE — AUTHOR ATTEMPT 2 DISPATCH READY`
- Parent: `HELP_HUMAN`
- Manager: `WORKING_ITEMS` Agent 1
- Package: `PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`
- Selected deliverable: `DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance` only
- Objective: apply the accepted 27-row owner selection to a new immutable
  semantic-candidate package, deterministically validate the author return,
  then obtain a genuinely fresh independent read-only semantic refutation.
- Posture: `TERMINAL_FAN_OUT_IN`, serialized `AUTHOR -> REFUTER -> MANAGER_FAN_IN`
- Authority: signed owner ruling transcript
  `execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`
  SHA-256 `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- Selection package identity: SHA-256
  `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`.
- Signer/date: `Ryan Tufts`, `2026-08-03`.
- Repository basis observed at activation:
  `88e7590d3664d4f1daf91bed2a8899bda0748b92`.
- Accepted Scope of Work: SHA-256
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Semantic patch plan: SHA-256
  `e51075494a14576aa8d9357b6ad21928ea47065a2aa2488a02b6a4b96359cee1`.
- Accepted upstream handoff: SHA-256
  `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`.

## Exact ordered selection

`D1-A D2-A D3-A D4-A D5-B D6-A D7-A D8-A D9-A TBD-001-A TBD-002-A TBD-003-A TBD-004-A TBD-005-A TBD-006-A TBD-007-A TBD-008-A TBD-009-A TBD-010-A TBD-011-A TBD-012-A TBD-013-A TBD-014-A TBD-015-A TBD-016-A CENSUS-A COMPAT-DELTA-A`

The census tuple is exactly
`(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)`, which is allowed by the
accepted semantic patch plan. `TBD-001-A` supplies only the grammar
`root-runtime-<positive-decimal-epoch>`; the candidate must preserve an
explicit owner-supplied future epoch placeholder and must not mint a value.

## Accepted current inputs

The author and refuter must bind these source identities:

- `decision_support/PACKAGE_MANIFEST.sha256` — `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`
- `decision_support/OWNER_SELECTION_MATRIX.csv` — `57b27b486e4c06d23425e3dd0760904a1b4a04bf0bcf49e0610b6c677a398c92`
- `decision_support/OWNER_SELECTION_SLATE.md` — `35006e9e862e26bcd3356d4dc3a95bec31f7f4ca361142b0431c6e35ca9b5598`
- `clients/N2_CLIENT_CENSUS.md` — `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52`
- `evidence/N3_EVIDENCE_DESIGN.md` — `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0`
- `integration/RECOVERY_SPEC_CANDIDATE.md` — `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`
- `integration/COMPATIBILITY_DISPOSITION_CANDIDATE.md` — `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`
- `integration/DEGRADED_MODE_DELTA_CANDIDATE.md` — `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b`
- `integration/OPEN_ITEM_MAP.md` — `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`
- `integration/IMPLEMENTATION_PLAN_CANDIDATE.md` — `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`

## Profile and execution boundary

The accepted Root contract states that no Root-local `software-workflow.json`
exists. Client-local profiles were inspected only as current evidence:

- App profile SHA-256 `97b6717a5991549367aa098629fbd7140bce7c7c226a15ef9419c0c3397f65e9`
- Piping profile SHA-256 `3a6fd86bd362eed5e1fbcda05dcde961fca8ad46cb14375ce3dd79c3872e09b7`
- PEC profile SHA-256 `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b`

No client profile is borrowed. No registered software check, source edit,
test execution, implementation, lifecycle, release, reliance, Git, or
foreign-loop act is authorized.

## Write ownership

- Manager-only coordination root:
  `execution/_Coordination/AgentRuns/ROOT_DEL0206_SEMANTIC_CANDIDATE_2026-08-03/`
- Immutable deliverable-local run record:
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/`
- AUTHOR owns only `candidate/**`, `application_trace/**`, and
  `author/RETURN.md` under the deliverable-local run record.
- REFUTER reads the exact frozen candidate and writes only
  `refuter/RETURN.md` under the deliverable-local run record.
- WORKING_ITEMS owns activation, briefs, work graph, deterministic validation,
  package manifest, manager return, and handoff.

## Closure boundary

Closure can cover only semantic-candidate authoring and independent
refutation. Exact candidate-byte acceptance is the next accountable-human
gate. Implementation, client conformance, compatibility repinning, Tier-0 or
PEC adoption, lifecycle, release, reliance, Git, and merge remain separate.
