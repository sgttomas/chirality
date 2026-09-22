# References: DEL-07-04 Status Transition API and MCP Tool

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `a07418a7b1bb7919d7f9e495e42e81f1b47a0a389cab9dbd3909cb81c992bcc1` | `a07418a7b1bb7919d7f9e495e42e81f1b47a0a389cab9dbd3909cb81c992bcc1` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `57411f8df49e6316d8d3bc9674d698b1c8478e639aad331115d4f67bcca97363` | `57411f8df49e6316d8d3bc9674d698b1c8478e639aad331115d4f67bcca97363` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `8b0d805b6abc6d4a493463440394ea9bb39f23fba84483f05007fe724447fe13` | `8b0d805b6abc6d4a493463440394ea9bb39f23fba84483f05007fe724447fe13` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835` | `334bd49602a68900cc877053493d0edb66e370919f77b768b3db679ed4087835` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `5e9cb5e553a815cba6e3d5bf765c66290bc9e25c15c2e44a0a33bea7ed4d04dc` | `5e9cb5e553a815cba6e3d5bf765c66290bc9e25c15c2e44a0a33bea7ed4d04dc` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `17ca3f3c2b868771a0cbcafeb0928c5416cd8bc88d79639838cefe1462e46054` | `17ca3f3c2b868771a0cbcafeb0928c5416cd8bc88d79639838cefe1462e46054` | MATCH |
| REF-007 | `workflows/software-decomp/WORKFLOW.md` | Software decomposition method and grouped checkpoint protocol | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | `fd79f8001404a99c3438500fae413d56193dc1db408b3416bdee20414977d452` | MATCH |
| REF-009 | `workflows/software-decomp/resources/contract.md` | Software decomposition inputs, modes, and output contract | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | `f6f159169c00ba5191b24d9b8f99625a392530b8bf9c06af388fcb612fdd618f` | MATCH |
| REF-010 | `workflows/software-decomp/resources/method.md` | Software decomposition detailed method | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | `1442f0cee8b5c4fa294e369e1742468613fa945b998f106629c6bb9c783935e3` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-07-04`
- PackageID: `PKG-07`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.

## Source currency — 2026-09-22

The corpus hash rows above preserve their accepted snapshot; they are not a perpetual currentness claim. The parent owns D-APP-38 recomputation/application for this closeout. Gate-5 SCA-REF labels distinguish amendment references from the corpus REF labels without changing the referenced authority bytes.
