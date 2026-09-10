# References: DEL-10-01 DomainEngineProfile Contract Draft

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
| REF-008 | `workflows/domain-engine/WORKFLOW.md` | Domain-engine integration method and human-gate protocol | `922b6dadbc8a8f71899954a6f7e47b45df753fb81a6ca644218a9cf642b0e94e` | `922b6dadbc8a8f71899954a6f7e47b45df753fb81a6ca644218a9cf642b0e94e` | MATCH |
| REF-011 | `workflows/domain-engine/resources/contract.md` | Domain-engine inputs, modes, and output contract | `414cccf9805318c6a450d17077cc1091a47e82ac7be5e2ac48596a6789ac6998` | `414cccf9805318c6a450d17077cc1091a47e82ac7be5e2ac48596a6789ac6998` | MATCH |
| REF-012 | `workflows/domain-engine/resources/method.md` | Domain-engine detailed method | `e3bbb3e344c7c5eb69d5288b190287595b739333b09825541f58305e20926caf` | `e3bbb3e344c7c5eb69d5288b190287595b739333b09825541f58305e20926caf` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-10-01`
- PackageID: `PKG-10`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
