# References: DEL-10-03 OperationProposal Record and Human Gate Workflow

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
| REF-008 | `workflows/domain-engine/WORKFLOW.md` | Domain-engine integration method and human-gate protocol | `922b6dadbc8a8f71899954a6f7e47b45df753fb81a6ca644218a9cf642b0e94e` | `922b6dadbc8a8f71899954a6f7e47b45df753fb81a6ca644218a9cf642b0e94e` | MATCH |
| REF-011 | `workflows/domain-engine/resources/contract.md` | Domain-engine inputs, modes, and output contract | `414cccf9805318c6a450d17077cc1091a47e82ac7be5e2ac48596a6789ac6998` | `414cccf9805318c6a450d17077cc1091a47e82ac7be5e2ac48596a6789ac6998` | MATCH |
| REF-012 | `workflows/domain-engine/resources/method.md` | Domain-engine detailed method | `e3bbb3e344c7c5eb69d5288b190287595b739333b09825541f58305e20926caf` | `e3bbb3e344c7c5eb69d5288b190287595b739333b09825541f58305e20926caf` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-10-03`
- PackageID: `PKG-10`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.

## Current observation — 2026-09-22

The author-stage repair preserved ExpectedSHA256 values while recomputing observed hashes. Manager integration subsequently adopted authority corpus v25 under D-APP-38, including the accepted D-GOV-43/D-APP-127 application to App DIRECTIVE; the current table carries those adopted authority hashes. Historical MATCH prose records its dated source state. Decomposition and lifecycle approval pins remain unchanged. REF-008/011/012, where present, name the current domain-engine workflow resources; `agents/AGENT_DOMAIN_ENGINE.md@77a327727` citations name a retained historical source, not those current bytes.
