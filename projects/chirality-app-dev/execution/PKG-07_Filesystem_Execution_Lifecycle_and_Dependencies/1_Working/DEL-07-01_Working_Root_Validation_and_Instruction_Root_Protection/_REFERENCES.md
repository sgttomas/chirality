# References: DEL-07-01 Working Root Validation and Instruction Root Protection

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `dee943d3d87bf261bfd393c4dd9d474c01165a09cf0df94207361a4efa014d82` | `dee943d3d87bf261bfd393c4dd9d474c01165a09cf0df94207361a4efa014d82` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `735a85004c157f30c3a48c553b82d543e43bae0272bebf47c7273a41f8e1e8dc` | `735a85004c157f30c3a48c553b82d543e43bae0272bebf47c7273a41f8e1e8dc` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `ba7a62b2383293b54d059a60ce407aa3acdc3043afe61b6932958442e86343fb` | `ba7a62b2383293b54d059a60ce407aa3acdc3043afe61b6932958442e86343fb` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `f5ebe6453a871980a0c1fd3ff11c0132048ce4e765a9c23f48968648b133ebc2` | `f5ebe6453a871980a0c1fd3ff11c0132048ce4e765a9c23f48968648b133ebc2` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `4a8af7de5f6bfdf757cd6a73834c1fa00686b4581d27e13a191735a0b05e467b` | `4a8af7de5f6bfdf757cd6a73834c1fa00686b4581d27e13a191735a0b05e467b` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` | `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8` | HASH_MISMATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-07-01`
- PackageID: `PKG-07`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
