# Fresh N0 rerun checklist

Status: `BLUEPRINT — ALL ITEMS MUST PASS BEFORE OR DURING DISPATCH`

## Pre-dispatch gate

- [ ] S2 exact bytes were owner-accepted before application.
- [ ] S2 application and Gate-5 validation are complete.
- [ ] Applied PRD/decomposition current-facing labels agree with accepted
      records and S1/AUDIT_DECOMP rerun no longer reports the blocker.
- [ ] Candidate staging directory contains exactly six final filenames.
- [ ] Candidate packet validator passes twice with identical output.
- [ ] Candidate manifest identity was presented to the owner.
- [ ] External acceptance record contains the exact valid manifest-bound token.
- [ ] Acceptance validator passes.
- [ ] Live `accepted_inputs/` contains only the six accepted bytes and matches
      candidate files byte-for-byte.
- [ ] N0-R2 child tool surface supports bounded non-shell reads, SHA-256,
      JSON/CSV parsing, validators, and exact return writes.
- [ ] No runtime/client/decomposition/PRD/register/lifecycle/Git write is in the
      N0-R2 brief.

## N0-R2 checks

- [ ] Repository/S2 applied basis identity matches every packet source field.
- [ ] `ScopeOfWork.md` SHA-256 is
      `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
      and validates as `SOW_V1` with zero issues.
- [ ] S2 decision, handoff, applied-file, and Gate-5 hashes match packet fields.
- [ ] Exact six-file membership, regular-file type, UTF-8/LF/whitespace, and
      no-extra-file checks pass.
- [ ] Five content hashes match `CANDIDATE_SET_MANIFEST.sha256`.
- [ ] Manifest SHA-256 matches the external owner acceptance token.
- [ ] `OPEN_ITEMS.csv` has the exact header and one-to-one TBD-001..016 rows.
- [ ] All packet files state fresh synthesis/not historical reconstruction.
- [ ] Packet acceptance is bounded to planning inputs and claims no semantic,
      runtime, lifecycle, client, or release act.
- [ ] No `{{...}}` placeholder remains in the live packet.
- [ ] `_STATUS.md` remains `INITIALIZED` and no earlier production activation
      is claimed.
- [ ] No Root-local `software-workflow.json` exists and no client profile is
      borrowed.
- [ ] `_DEPENDENCIES.md` still declares no upstream or downstream edge.
- [ ] N0-R2 writes are confined to its two exact basis return files.
- [ ] Prior N0 interruption is treated as rejected provenance, not fan-in.

## Manager fan-in

- [ ] Both N0-R2 outputs exist, parse, and cite exact refs/SHAs.
- [ ] All checks are PASS and verdict is `RELEASE_N1_N2_N3`.
- [ ] Candidate/input acceptance has not been misread as runtime semantic
      acceptance or implementation authority.
- [ ] WORKING_ITEMS records the fresh return as accepted before changing graph
      state or dispatching N1/N2/N3.

Any unchecked or failed item preserves `HELD_AT_N0`.
