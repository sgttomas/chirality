# DEL-03-01 — reverse pass notes (worker A)

Capability file: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows).

Responses: 1 CLAIMED_BY, 2 PARTIAL, 57 NOT_MINE. The forward ledger is sealed and was not
edited.

## Forward-row observations exposed by the reverse pass

- **CLM-012.2 and CLM-019: overstated.**
  - What the forward rows say:
    - `section9.runtime_engine_contract` exists and is linked to
      `engine-conformance.test.ts`.
    - CLM-012.2 is STALE_SPECIFICATION.
    - REGISTER-1 says DEP-03-01-008 "still PENDING though linkage exists".
  - What CAP-HARNESS-059 shows:
    - The manifest's `evidenceFiles` entry for that ID is
      `src/lib/harness/agent-runtime-contract.ts`.
    - That file is a legacy in-process child-run record contract with no production
      importer.
    - It is neither the port (`runtime-contracts/agent-engine-port.ts`) nor a Codex-path
      artifact.
  - Consequences:
    - The linkage exists by ID only. Its evidence points at a legacy surface.
    - The TBD in CLM-012.2 is still stale as worded (the ID now exists), but the linkage is
      not substantive for the Codex engine.
    - DEP-03-01-008 staying PENDING is therefore defensible.
    - Suggest the verifier read REGISTER-1's DEP-008 remark and CLM-019's note as
      "linkage nominal, not substantive".
    - The disposition of CLM-019 (PARTIALLY_IMPLEMENTED) stands.
- **CLM-009.9 (stub retained): noted, disposition stands.** CAP-HARNESS-029 notes that the
  stub and legacy engine registry now serve only the controlled CI Runtime fixture and tests.
  That is consistent with "for tests", so ALIGNED still holds.
- **CLM-021 / CLM-003.4 (engine selection): consistent.** CAP-HARNESS-028 confirms the
  in-process stub/anthropic/agentSdk provider selection survives as a legacy path. This
  agrees with the forward rows (compatibility history, Codex sole engine).

## PostReleaseBasis revisit (calibration finding)

Method: read-only `git -C <frozen tree> show --stat` for `da95ec194`, `cb08dbe2f`,
`9ecbdecdf` and `ccb95e06a`.

What each commit touched:

| Commit | Touched |
|---|---|
| `da95ec194` | Runtime application-tools, `codex-supervisor`, `runtime-daemon`, `session-store`, `client`, `contracts/protocol` and `index`, plus 10 lines of `daemon/src/app-owned-composition.ts` |
| `cb08dbe2f` | `codex-supervisor` and one test |
| `9ecbdecdf` | Evidence files only |
| `ccb95e06a` | Export files and one Electron IPC contract line |

- The only overlap with forward evidence is `app-owned-composition.ts`, cited at `:214`
  (`engines.register(createDelegatedEngineAdapter(...))`). The `da95ec194` diff adds
  application-tools wiring (an import, a registry, supervisor/daemon arguments). It does not
  change the engine registration line; it only shifts its line number.
- No other cited file was touched.

**Rows that should change to YES: 0.** Assuming NO was correct for this deliverable. The
only caveat is that the cited line number `:214` reflects post-`da95ec194` numbering, which
is harmless because the frozen tree is the citation basis.
