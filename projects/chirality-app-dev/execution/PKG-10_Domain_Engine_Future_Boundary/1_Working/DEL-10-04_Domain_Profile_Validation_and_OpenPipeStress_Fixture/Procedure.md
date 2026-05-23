# Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

## Purpose

Define the operational procedure for producing and later verifying the DEL-10-04 future fixture profile, validation tests, and adapter assumptions note without activating domain-engine implementation.

## Prerequisites

- Accepted PKG-10 amendment or explicit human authorization for future domain-engine work. Current sources keep domain profiles and operation proposals in future scope.
- Accessible source corpus for `docs/PRD.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PLAN.md`.
- ResponsibleParty assignment: TBD.
- Concrete future test path and adapter manifest location: TBD.
- Dependency extraction and project graph validation: TBD; `_DEPENDENCIES.md` currently has no accepted upstream/downstream edges.
- Source warning acknowledged: REF-006 PRD hash mismatch is treated as warning only for this run.

## Steps

1. Confirm scope gate.
   - Verify PKG-10 remains future-boundary/gated scope unless a human-approved amendment says otherwise.
   - Do not create or activate domain-engine endpoints, protected-path write behavior, or operation-apply workflows during this deliverable-local drafting run.

2. Define fixture validation target.
   - Use `docs/TYPES.md` Section 11.1 as the candidate `DomainEngineProfile` shape.
   - Mark any field semantics not defined by the accessible source corpus as TBD.

3. Draft or review a future OpenPipeStress fixture profile.
   - Use OpenPipeStress only as fixture profile data.
   - Keep OpenPipeStress solver assumptions in the profile or adapter-assumptions layer.
   - Do not add OpenPipeStress assumptions to Chirality core runtime.

4. Define deterministic validation checks.
   - Check required profile fields.
   - Check protected/proposal path separation.
   - Check operation descriptors against `OperationProposal` concepts where operation fixtures are present.
   - Check deterministic adapter manifest presence or mark manifest rules TBD.
   - Check boundary notice presence.

5. Define negative validation cases.
   - Missing required field.
   - Overlapping protected and proposal paths.
   - Missing boundary notice.
   - Operation fixture without required human gate.
   - Fixture or documentation that implies professional approval, code compliance, external validation, or Chirality-owned solver truth.

6. Produce adapter assumptions note.
   - Separate accepted source facts from ASSUMPTION and TBD items.
   - Identify which assumptions are profile-level, adapter-level, operation-proposal-level, or explicitly excluded from core runtime.

7. Verify no implementation activation occurred.
   - Confirm no current-release endpoint/tool activation was introduced.
   - Confirm no Dependencies.csv was created by this four-documents task.
   - Confirm ResponsibleParty remains TBD.

## Verification

| Verification Item | Expected Evidence |
|---|---|
| Four-document kit exists | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are non-empty. |
| Future-boundary posture preserved | Documents state that PKG-10 remains future-boundary/gated scope. |
| Requirements source-grounded | Requirements cite accessible source sections or are labeled ASSUMPTION/TBD. |
| OpenPipeStress not core | No instruction treats OpenPipeStress as Chirality core runtime behavior. |
| Protected path policy preserved | Direct protected-domain writes are disallowed in requirements and guidance. |
| Human gate preserved | Domain operations require explicit human acceptance before application. |
| Professional boundary preserved | No language claims automated approval, code compliance, external validation, or solver truth ownership. |

## Records

- Future fixture profile: TBD.
- Validation tests: TBD.
- Adapter assumptions note: TBD.
- TASK run record under `_run_records/`.
- `_STATUS.md` transition to INITIALIZED only after all four document files are non-empty.
