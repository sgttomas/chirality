# SCA-003 Decision Log

## Authorizing basis

| Item | Value |
|---|---|
| Owner direction | Open the Root SCOPE_CHANGE intake prepared for `TM-ROOT-107` with its two exact named inputs |
| Intake handoff | `execution/_Coordination/_TaskManagement/SCOPE_CHANGE_INTAKE_TM-ROOT-107_2026-08-02.md` |
| Input 1 | D-APP-84 REV2 Root route at SHA-256 `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a` |
| Input 2 | Product-delivery owner-intent record at SHA-256 `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03` |
| Authority limit | Intake/assessment only; neither input is Root product or decomposition authority; all five human gates remain separate |

## Gate state

| Gate | State | Effect |
|---|---|---|
| Gate 1 — intake | `PREPARED_BLOCKED_PENDING_BASIS_RECONCILIATION_AND_OWNER_CONFIRMATION` | Exact inputs verified; zero action rows parsed; provisional no-change disposition recorded; current accepted-basis contradiction blocks confirmation |
| Gate 2 — impact | `NOT_OPENED` | No `Impact_Assessment.md` is authored or accepted |
| Gate 3 — amendment | `NOT_OPENED` | No exact amendment preview or candidate bytes exist |
| Gate 4 — propagation | `NOT_OPENED` | No propagation plan or `Amendment_Actions.csv` exists |
| Gate 5 — execute and validate | `NOT_OPENED` | No authoritative or metadata write; `_LATEST.md` unchanged |

## Manager determinations

1. The owner direction is sufficient to open Gate-1 work but does not itself
   answer “Is this what you intend?” against the parsed output.
2. Exactly two inputs govern the requested assessment; later repository state
   is used only to validate currentness and does not become a third scope input.
3. The input pair does not specify an atomic decomposition edit. Creating one
   would violate the no-invention rule.
4. Current carrier allocation supports a provisional zero-action/no-change
   disposition; see `Provisional_Disposition.csv`.
5. The former Root Bash/full-worktree paragraph cited by D-APP-84 is no longer
   live. Owner commit `e012e5824` removed it and assigned development-time
   containment to the harness; this overtakes that part of the route without
   deciding generic App runtime sandbox semantics.
6. The live Root working surface and PRD carry candidate/predecessor labels
   inconsistent with the accepted-state records. This is an independently
   verified basis-integrity blocker and cannot be silently repaired here.
7. The pre-change audit was delegated read-only under the sealed brief in
   `Evidence/AUDIT_DECOMP/LAUNCH_BRIEF.md`. It returned `BLOCKER` at
   `RETURN.md` SHA-256
   `3d2a09dd35da0c26bc87a1e156c7b1a5e35fd7875ff9a39d4294b8d6a369a868`:
   structural coverage PASS, authority-state consistency FAIL, closure
   readiness FAIL. The return is evidence, not a human gate or repair grant.
