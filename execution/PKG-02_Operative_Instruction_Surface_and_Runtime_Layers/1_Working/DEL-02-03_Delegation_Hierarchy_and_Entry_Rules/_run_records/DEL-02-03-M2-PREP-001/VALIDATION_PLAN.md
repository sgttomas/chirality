# Application-Tranche Validation Plan

Status: `DRAFT — EXECUTE ONLY AFTER D-GOV-35 RULING AND M2 AUTHORIZATION`

All commands run from the repository root. Exact outputs and exit codes must
be preserved in the application tranche's durable evidence and Root receipt.

## Pre-application gates

1. Confirm the draft's required historical basis resolves as a commit:
   `git cat-file -t 13201dfe7dc3b97c9aa36f6305cae604b48ef80f`
   must print `commit` (TM-ROOT-127).
2. Confirm the application worktree is on the owner-authorized branch and has
   not been synced or rebased without owner authorization. If `main` has
   advanced, stop and request sync authorization.
3. Reproduce SHA-256
   `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`
   for the N1 patch and
   `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`
   for pre-application `AGENTS.md`.
4. Run literal `git apply --check` against the N1 patch. Any mismatch stops
   application and requires fresh review.
5. Replace the draft manifest's pending M2 fields with the exact owner ruling
   and application authorization. Finalize the exact protected path set. The
   N1 proposal requires post-ruling concordance across
   `docs/WORKFLOW_COMPONENT_STANDARD.md`, `docs/TYPES.md`, and
   `docs/DBM_Agent_Instruction_Architecture.md`; exact bytes require review
   before application.

## Post-application validators

- `python3 tools/validation/validate_agent_instructions.py`
- `python3 tools/validation/validate_instruction_entrypoints.py`
- `python3 tools/validation/validate_instruction_tranche_manifest.py`
  after the finalized manifest is added to the live corpus
- a direct call to
  `tools.validation.validate_instruction_tranche_manifest.validate_manifest`
  on the finalized manifest path, preserving failures, notes, and parsed
  tranche id
- `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`
- `python3 tools/taskmgmt/taskmgmt.py validate --register execution/_Coordination/_TaskManagement/REGISTER.csv`
- `git diff --check`

The application owner must also reproduce the post-application `AGENTS.md`
SHA-256, verify that only owner-authorized protected paths changed, and verify
that the pre-change `ScopeOfWork.md` SHA-256 remains
`e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`
unless a separate SOW amendment is explicitly authorized.

## Notice and derivative closure

After the owner ruling and application, route finalized notices to App and
Piping, change `m6_notice.disposition` to `routed`, and record the actual
repo-relative notice paths. Receiving-loop acknowledgment is not adoption.

Regenerate the Root-owned Chirality App public-export projection through
`exports/chirality-app/export_public.py`, or record an explicit authorized
deferral. Never rewrite historical App/Piping evidence in place.

No validator output substitutes for semantic review, an owner ruling,
lifecycle acceptance, release, reliance, or merge authority.
