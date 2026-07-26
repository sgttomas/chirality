# Sealed Brief — APP-HOLD-1 Durable-Authority Backcheck

BriefID: `APP-HOLD-1-A2-AUTHORITY-BACKCHECK-2026-07-26`  
Parent: HELPS_HUMANS (Agent 1)  
Reviewer: same read-only ephemeral Agent 2 that authored the pass-1 review and
corrected-candidate backcheck  
Write targets: none  
Corrected-basis hash list: `AUTHORITY_BACKCHECK_BASIS_HASHES.sha256`  
Hash-list SHA-256:
`6e75c5349bde8121e06de8fb3eef37ee5c7003053bc1021595df3629f2802d46`

## Objective

Backcheck only AHB-001 and the consequent candidate-byte changes. Decide
whether the exact APP-HOLD-1 candidate now has a complete durable-authority
application path and may enter the owner gate.

## AHB-001 correction presented

1. Reserved the next available App decision identifier, `D-APP-75`, subject
   to a collision check immediately before application.
2. Added `D-APP-75_RULING_TEMPLATE.md` with explicit
   `PROPOSAL_TEMPLATE_NOT_RULED` status and `OwnerRuling: PENDING`.
3. Required later application to transcribe the owner's actual approval
   verbatim, record the accepted final hash-list identity, state the bounded
   no-repin effect, and update the App decision register.
4. Changed every candidate hold row to cite `D-APP-75`, and made the
   deterministic validator fail closed on any preparation-only or other
   authority value.
5. Added a negative fixture and
   `test_preparation_only_authority_fails_closed`.
6. Expanded the regression suite to 12/12 passing tests and regenerated the
   live scan at Git basis
   `918bb48b8fcee66c031d0d6d4040a46089f96067`; it still finds 53 contracts,
   exactly six held targets, and exact register parity.

## Required backcheck

- Verify every file listed in the corrected hash list.
- Verify that the template cannot itself be read as a ruling or application
  authority.
- Verify that the later application contract names all required durable
  surfaces and cannot proceed without actual owner approval.
- Verify the validator rejects preparation-only authority.
- Re-run the scan and tests where feasible.
- Disposition AHB-001 as `CLOSED | PARTIAL | OPEN`.
- Identify any new material defect caused by the correction.
- Return `ADMIT | ADMIT_WITH_WARNINGS | RETURN_FOR_CORRECTION`.
- Confirm no write and report engine/provider/model.

Do not edit, stage, commit, apply, or delegate.
