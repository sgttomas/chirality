# Validation — GOV-D8-SIMPLIFICATION-20260729

Status: `PRE-COMMIT PASS`

## Basis and owner-act verification

- Worktree branch `gov/step4-sca-application` resolved to
  `2dace6ec6e3342a415342a539d5630969cbba39c` (frozen basis; clean before
  authoring).
- Owner direction verified byte-exact from the session transcript copy:
  181 bytes UTF-8, SHA-256
  `d89bcdef36398ec7c345a48e0b3d65b30c635cf09aed0bf8f2a5a3c89c1b33d0`.
- Receipt 64 fence re-verification: extracted between the
  `BEGIN/END OWNER RULING VERBATIM` markers, indentation stripped,
  re-hashed — 181 bytes, hash MATCH.
- Tranche-manifest embedded verbatim line re-hashed — 181 bytes, hash
  MATCH.
- Pre-edit `agents/AGENT_CHANGE.md` SHA-256 at basis matched the value
  quoted in the three M6 notices
  (`f59e5455e1eeac687f69f091a74974fbfb2fb0a520fcb3bc7db8ab24529a4c77`);
  post-edit SHA-256 is
  `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa`.

## CSV integrity

- Scope ledger: 105 CRLF line terminators before and after; SOW-042 row
  keeps 12 cells and `SourceRef` `PRD §5.3 D-8 [ADOPTED-D-GOV-31]`;
  only the statement cell changed.
- Deliverable register: LF-only before and after; DEL-04-06 row keeps 12
  cells; only Description and AnticipatedArtifacts changed.

## Deterministic checks (pre-commit)

- `python3 -m pytest tools/validation/test_validate_instruction_tranche_manifest.py -q`
  — 36 passed, exit 0 (grant cases rewritten as owner_direction cases;
  the undeclared `self_merge: true` failing mode preserved).
- `python3 tools/validation/validate_instruction_tranche_manifest.py`
  (G4 CI mode) — `G4 PASS (CI mode)`: all 17 manifests schema-valid,
  including `ROOT-D8-SIMPLIFICATION-20260729`, exit 0. The
  `ROOT-GOV31-PROPAGATION-20260729` manifest's declared
  `GRANT_CANDIDATE.md` path remains valid after the deletion — declared
  paths are not required to exist (a tranche may delete a path), so the
  historical manifest is unaffected.
- Census
  `grep -rn -i "bounded owner grant|merge_execution_grant|grant record"`
  over `docs/PRD_ROOT.md`, `execution/_Coordination/LOOP_INIT.md`,
  `agents/`, `execution/_Decomposition/`, the DEL-04-06 folder, and
  `tools/validation/` — zero live-normative hits. Two remaining hits are
  dated historical log entries in
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
  (DEC-023 decision-log row; §13 amendment-history entry), each
  describing the D-GOV-31/SCA-002 acts as they occurred — retained as
  historical citations.

## Post-commit checks (run against the tranche commit; results in HANDOFF_STATE)

- G4 diff mode
  (`--base 2dace6ec6e3342a415342a539d5630969cbba39c --head HEAD`).
- Committed-HEAD whitespace validator
  (`validate_candidate_whitespace.py --base-ref 2dace6ec6…`).
- `git diff --check`.
