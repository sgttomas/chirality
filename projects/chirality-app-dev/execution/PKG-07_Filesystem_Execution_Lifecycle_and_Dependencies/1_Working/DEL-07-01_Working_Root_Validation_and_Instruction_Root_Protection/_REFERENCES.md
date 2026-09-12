# References: DEL-07-01 Working Root Validation and Instruction Root Protection

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `fa8fc9dcc2f0b1dae555f4e24288728bf956cd1fa2db144d5462a05a6b6e219e` | `fa8fc9dcc2f0b1dae555f4e24288728bf956cd1fa2db144d5462a05a6b6e219e` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `01e1c75cdf7bcc0dbac941f5e3c797f52dbb5bf3e8bec714ab167854ffa9ec67` | `01e1c75cdf7bcc0dbac941f5e3c797f52dbb5bf3e8bec714ab167854ffa9ec67` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835` | `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `5e9cb5e553a815cba6e3d5bf765c66290bc9e25c15c2e44a0a33bea7ed4d04dc` | `5e9cb5e553a815cba6e3d5bf765c66290bc9e25c15c2e44a0a33bea7ed4d04dc` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `8649ccba8f68107f2c6cb6d5014b2d69dad434a3bdd414310b8a91d53bf97fa4` | `8649ccba8f68107f2c6cb6d5014b2d69dad434a3bdd414310b8a91d53bf97fa4` | MATCH |
| REF-007 | `workflows/software-decomp/WORKFLOW.md` | Software decomposition method and grouped checkpoint protocol | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | MATCH |
| REF-009 | `workflows/software-decomp/resources/contract.md` | Software decomposition inputs, modes, and output contract | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | MATCH |
| REF-010 | `workflows/software-decomp/resources/method.md` | Software decomposition detailed method | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | MATCH |

## SCA-APP-010 Gate-5 Authority

| RefID | Path | Current use |
|---|---|---|
| REF-008 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Brief.md` | Owner-confirmed Gate-1 envelope A001 to A029 and frozen pre-image identities (G1-CONFIRM) |
| REF-009 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Gate3/GATE3_AMENDMENT_PACKAGE.md` | Owner-approved exact amendment bytes (G3-CONFIRM), including this deliverable's applied row |
| REF-010 | `execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Propagation_Plan.md` | Owner-approved propagation plan (G4-CONFIRM); this deliverable's alignment writes WI-041, WI-042, WI-043, WI-044, WI-045 and dependency writes DEP-017, DEP-018 |
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
- DeliverableID: `DEL-07-01`
- PackageID: `PKG-07`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
