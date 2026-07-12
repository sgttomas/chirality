# Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Define the operational procedure for producing and later verifying the DEL-10-04 future fixture profile, validation tests, and adapter assumptions note without activating domain-engine implementation.

## Prerequisites

- Accepted PKG-10 amendment or explicit human authorization for future domain-engine work. Current sources keep domain profiles and operation proposals in future scope.
- Accessible source corpus for `docs/PRD.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PLAN.md`.
- ResponsibleParty assignment: TBD.
- Concrete future test path and adapter manifest location: TBD.
- Dependency posture: `_DEPENDENCIES.md` now contains extracted ACTIVE rows, but all satisfaction remains `PENDING`; accepted declared upstream/downstream closure and project graph validation remain TBD.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

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
   - For each negative case, record the deterministic expected failure or mark the expected output TBD.

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
   - Confirm this P3 four-documents task did not create, edit, or promote `Dependencies.csv`.
   - Confirm ResponsibleParty remains TBD.
   - Confirm no future fixture output is treated as professional approval, code compliance, external validation, or Chirality-owned solver truth.

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
| Expected failures documented | Future negative tests include deterministic expected failure evidence or explicit TBDs. |
| P3 scope preserved | `_STATUS.md`, `_SEMANTIC_LENSING.md`, metadata files, and dependency registers are not modified by the P3 four-documents pass. |

## Records

- Future fixture profile: TBD.
- Validation tests: TBD.
- Adapter assumptions note: TBD.
- Stable validation evidence record format: TBD.
- Human-approved boundary-notice wording fixture: TBD.
- TASK run record under `_run_records/`.
- `_STATUS.md` not changed during P3_ONLY because `_SEMANTIC_LENSING.md` declares `NO_STATUS_TOUCH`.
