# References: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `c2fb9ecbbc37a98577a64a3e7e641de8c26b3145ad8cc40dc4a9a014aa66a12b` | `c2fb9ecbbc37a98577a64a3e7e641de8c26b3145ad8cc40dc4a9a014aa66a12b` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `3741bb7ec389c12f0856cf64acc27d4d17b77d1683275564b75182fcdbab5187` | `3741bb7ec389c12f0856cf64acc27d4d17b77d1683275564b75182fcdbab5187` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `87ced649beae245e7b0290b3ef8afb46681d04e671964a0583fdce83a7ccb586` | `87ced649beae245e7b0290b3ef8afb46681d04e671964a0583fdce83a7ccb586` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | MATCH |

## SCA-APP-010 Gate-5 Authority

| RefID | Path | Current use |
|---|---|---|
| REF-008 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Brief.md` | Owner-confirmed Gate-1 envelope A001 to A029 and frozen pre-image identities (G1-CONFIRM) |
| REF-009 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Gate3/GATE3_AMENDMENT_PACKAGE.md` | Owner-approved exact amendment bytes (G3-CONFIRM), including this deliverable's applied row |
| REF-010 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Propagation_Plan.md` | Owner-approved propagation plan (G4-CONFIRM); this deliverable's alignment writes WI-056, WI-057, WI-058, WI-059, WI-060 and dependency writes DEP-023, DEP-024 |
| REF-011 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Handoff_State.md` | Gate-5 handoff state; derivative closure open pending downstream alignment and audits |

Applied identities: decomposition post-image SHA-256
`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content
commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (PR #708 merge
`7795b0972cac147869607d994173753e4a2fc232`); companion register post-image
`63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; active
pointer `execution/_ScopeChange/_LATEST.md` SHA-256
`b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (PR #711
merge `311a2f0b811d55315d6eb623130cad0be1417565`). The authority-corpus rows
above are unchanged (corpus v20 has no decomposition member). Seating and
alignment are recorded under `D-APP-108` and run
`execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/`.

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-08-03`
- PackageID: `PKG-08`

## SCA-APP-004 Authority Lineage

| Source | Role | Treatment |
|---|---|---|
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Amendment_Preview.md` | Owner-approved presentation-neutral DEL-08-03 amendment and semantic ownership partition | GOVERNING FOR THIS RECONCILIATION |
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Propagation_Plan.md` | Owner-approved Gate-5 write scope, no-change set, and downstream dispatch/projection validation | GOVERNING FOR THIS RECONCILIATION |
| `execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | Prospective Woven Dialogue ruling preserving dispatch while superseding fixed placement | GATE-5 AUTHORITY; path/hash verified during integration |

The authority-document hashes above are reconciled to authority corpus v16
after the SCA-APP-004 Gate-5 authority/decomposition fan-in.

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
- Work/Agents presentation consumes but does not own DEL-08-03 dispatch
  semantics. Only explicitly recorded work sources may be projected; dialogue
  is not silently converted into tasks.
