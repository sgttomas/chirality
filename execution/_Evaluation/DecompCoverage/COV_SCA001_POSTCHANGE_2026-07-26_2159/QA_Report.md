# QA Report

## Input and section resolution

- Decomposition readable: PASS (`execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`; SHA-256 `2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18`).
- `Packages`, `Deliverables`, `Scope Ledger`, `Objectives`, and `Companion inventory` headings: present by exact semantic heading match.
- Authoritative companion registers parsed: PASS.
- Parse ambiguities: none.

## Scan coverage

- Package declarations/folders: 6 / 6.
- Deliverable declarations/folders: 46 / 45.
- `_CONTEXT.md` files read: 45.
- `_STATUS.md` files resolved: 45.
- ScopeOfWork contracts validated: 45/45.
- Scope-ledger rows checked: 104 total, 95 IN.
- Objective support surfaces compared: 7.
- Active SCA snapshot and handoff state checked: yes.

## Deterministic limits

- Artifact presence is filename-based and deliverable-folder-local. Controls and ScopeOfWork.md are excluded.
- No prior-run comparison mode was briefed; the invoking SCOPE_CHANGE owns pre/post interpretation.
- Missing DEL-02-06 metadata was not inferred from the candidate into a filesystem context.
- Git HEAD identifies the committed base, while the audited revision 1.1 and SCA Gate 5 bytes are uncommitted authorized working-state changes; their SHA-256 identities are recorded directly.

## Output validation

- Required snapshot artifact count: 8/8.
- Issue log and matrix schemas: valid.
- Summary JSON: parseable and required fields present.
- Every BLOCKER/WARNING carries decomposition and filesystem evidence pointers.
