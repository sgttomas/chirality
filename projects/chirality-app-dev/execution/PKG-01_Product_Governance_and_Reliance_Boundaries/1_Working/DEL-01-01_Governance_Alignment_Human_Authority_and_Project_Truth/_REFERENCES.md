# References: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

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

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-01-01`
- PackageID: `PKG-01`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
