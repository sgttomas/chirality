# References: DEL-03-02 Thin TurnEngine and Session Locking

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `88178c2504637eb87425474ad721eb35a9e838547c84b44d183ebaa4c2404251` | `88178c2504637eb87425474ad721eb35a9e838547c84b44d183ebaa4c2404251` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `c72ac9c9acede1cde590302225715e4ab4b73778e14bff44ac930d46c34f9dfa` | `c72ac9c9acede1cde590302225715e4ab4b73778e14bff44ac930d46c34f9dfa` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `b3aa26e8dfa8610b12b912c182b5a23646ca71e4a5fc76cb6018872c3c77ef21` | `b3aa26e8dfa8610b12b912c182b5a23646ca71e4a5fc76cb6018872c3c77ef21` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `292b5d5636e169a4f7901f5be6e7054108f131328652a6d087b3d3332c6c2f19` | `292b5d5636e169a4f7901f5be6e7054108f131328652a6d087b3d3332c6c2f19` | MATCH |
| REF-007 | `workflows/software-decomp/WORKFLOW.md` | Software decomposition method and grouped checkpoint protocol | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | MATCH |
| REF-009 | `workflows/software-decomp/resources/contract.md` | Software decomposition inputs, modes, and output contract | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | MATCH |
| REF-010 | `workflows/software-decomp/resources/method.md` | Software decomposition detailed method | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | MATCH |

## SCA-APP-010 Gate-5 Authority

| RefID | Path | Current use |
|---|---|---|
| REF-008 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Brief.md` | Owner-confirmed Gate-1 envelope A001 to A029 and frozen pre-image identities (G1-CONFIRM) |
| REF-009 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Gate3/GATE3_AMENDMENT_PACKAGE.md` | Owner-approved exact amendment bytes (G3-CONFIRM), including this deliverable's applied row |
| REF-010 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Propagation_Plan.md` | Owner-approved propagation plan (G4-CONFIRM); this deliverable's alignment writes WI-021, WI-022, WI-023, WI-024, WI-025 and dependency writes DEP-009, DEP-010 |
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
- DeliverableID: `DEL-03-02`
- PackageID: `PKG-03`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
