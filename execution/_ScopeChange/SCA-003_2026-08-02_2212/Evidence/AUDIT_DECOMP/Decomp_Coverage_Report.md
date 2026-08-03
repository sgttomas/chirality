# Decomposition Coverage Report — SCA003_GATE1_PRECHANGE

## Audit identity

| Field | Value |
|---|---|
| Variant | `SOFTWARE` |
| Repository basis | `97678a841ef58345c73d3470ed8de57c9b1405d2` |
| Decomposition | `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md` |
| Decomposition SHA-256 | `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49` |
| Scope | `DEL-02-04`, `DEL-02-06`, `DEL-03-01`, `DEL-06-04`; complete referential/folder context for `PKG-02`, `PKG-03`, `PKG-06` |
| Expected source snapshot | `execution/_ScopeChange/SCA-002_2026-07-29_0800/` |
| Expected handoff phase | `SCA-003 Gate 1 pre-change baseline` |
| Derivative status | This report is audit evidence, not decomposition truth |

## Verdict

`BLOCKER` — Gate-1 closure readiness is `FAIL`.

Structural coverage is complete: all packages, deliverables, contexts,
contracts, mappings, and ledger references tested in scope are coherent. The
blocking defect is a distinct authority-state inconsistency. The live
authoritative v1.2 working surface identifies itself as an unaccepted SCA-002
candidate, says all five gates remain pending, and says revision 1.1 remains
accepted. The immutable SCA-002 record and active pointer prove that the owner
accepted SCA-002, Gate 5 applied these exact working-surface bytes, and revision
1.2 is the accepted current basis.

## Check verdicts

| Check | Verdict | Evidence |
|---|---|---|
| 1 — Forward coverage: packages | `PASS` | All 6 Root packages exist; scoped PKG-02, PKG-03, and PKG-06 are 3/3. |
| 2 — Forward coverage: deliverables | `PASS` | 46/46 Root deliverables exist; full scoped-package context is 20/20; targets are 4/4. |
| 3 — Reverse coverage: folders | `PASS` | No reverse-only Root package or deliverable folder; none in the three scoped packages. |
| 4 — ID consistency | `PASS` | Folder and register IDs match after SOFTWARE normalization for all checked units. |
| 5 — Context fidelity | `PASS` | 4/4 target `_CONTEXT.md` files match name, package, type, responsible party, description, and `ContextEnvelope`. |
| 6 — Artifact presence and contract form | `PASS` with 14 `INFO` | 4/4 contracts validate as clean `SOW_V1`; 0/14 anticipated production outputs exist at `INITIALIZED`. |
| 7 — Objective mapping | `PASS` | Target mappings are 1/1, 4/4, 2/2, and 2/2; all seven whole-package objective aggregates agree between registers. |
| 8 — Scope-ledger integrity | `PASS` | 104/104 rows parse; no unresolved package, deliverable, or objective reference; the three scoped packages contribute 39 rows and 41 valid deliverable references. |
| 9 — Derivative-package parity | `SKIPPED` | Not variant-owned for SOFTWARE. |
| 9b — Package-shape conformance | `PASS` | §3 explicitly labels the working surface and six authoritative companions; heavy truth stays in companions and no publication derivative is treated as authority. |
| 10 — Active snapshot and handoff state | `BLOCKER` | `_LATEST.md` points uniquely to existing SCA-002 and the application append is truthful, but the live authoritative working surface contradicts their accepted/applied state. |
| 11 — Lifecycle distribution | `PASS` (informational) | Four target carriers are `INITIALIZED`; none is retired or unknown. |

## Blocker COV-001 — authority-state contradiction

**Severity: `BLOCKER`.** This is not a topology defect.

- Live surface evidence: `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` lines 1,
  6, 11–20, 559, and 597–607 says `SCA-002 CANDIDATE`, `not accepted`, all
  gates pending, and revision 1.1 still accepted. SHA-256:
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`.
- Owner-act evidence: SCA-002 `Decision_Log.md` lines 72–86 records
  `ACCEPT SCA-002 271d456a — Ryan Tufts 2026-07-29`; lines 109–137 record
  Gates 1–5 accepted/applied and revision 1.2 as current. SHA-256:
  `88b34598352c2b75159b24ccab86059d38dc38b1bd1f7de1f22cf6b552c8a794`.
- Application evidence: `Applied_File_Hashes.json` records that the live
  working surface is byte-identical to the approved candidate; SHA-256
  `48ab54fb2348805ff9608fde04490153c5304fda87f5b81d345221abc7261205`.
  `Gate_5_Validation.json` is 33/33 PASS; SHA-256
  `a20a8a225417c4cb8a5f41c4c85f2a5c4a5c36f1ff300d0485c85d508662ae25`.
- Handoff evidence: SCA-002 `Handoff_State.md` lines 77–96 records
  `ACCEPTED_AND_APPLIED`; SHA-256
  `d578eb0ae3b99a97cf3ed0f79af4c88e3f9e02b39dc7c4cf5b60f5ef8972f607`.
- Pointer evidence: `_ScopeChange/_LATEST.md` lines 3–8 and 23–25 names
  SCA-002 closed and v1.2 accepted; SHA-256
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

The contradiction is therefore proven, not inferred: the live file's bytes
are the accepted/applied bytes, but their current-facing status prose still
denies the acceptance and application. A future agent cannot safely discover
the accepted basis from the authoritative working surface alone.

## Structural coverage summary

| Population | Declared | Found | Result |
|---|---:|---:|---|
| Root packages | 6 | 6 | `PASS` |
| Root deliverables | 46 | 46 | `PASS` |
| PKG-02 deliverables | 6 | 6 | `PASS` |
| PKG-03 deliverables | 6 | 6 | `PASS` |
| PKG-06 deliverables | 8 | 8 | `PASS` |
| Target carriers | 4 | 4 | `PASS` |
| Target contexts | 4 | 4 matching | `PASS` |
| Target SOW contracts | 4 | 4 valid | `PASS` |

## What to fix for a cleaner rerun

Open the governed SCOPE_CHANGE amendment already represented by SCA-003 and
make the living working surface accurately state the accepted/applied SCA-002
state, while preserving the immutable SCA-002 snapshot and its frozen
candidate-era prefixes. Re-run this audit after the exact amendment is
owner-approved and applied. Do not treat the 100% structural coverage as
closure evidence until the authority-state blocker is removed.
