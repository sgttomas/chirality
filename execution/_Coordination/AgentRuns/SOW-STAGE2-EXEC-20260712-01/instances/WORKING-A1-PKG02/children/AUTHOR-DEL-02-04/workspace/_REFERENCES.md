# References: DEL-02-04 Toolkit Options and Local UI State

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `2f52a24cee9badd4ae21347195d1e7d54739bbf41929d1da535e25429d2923b4` | `2f52a24cee9badd4ae21347195d1e7d54739bbf41929d1da535e25429d2923b4` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `d370ca35529ce661fccc41ab5acd9c51fbfb579ce4a29bd2850efd855cd4c938` | `d370ca35529ce661fccc41ab5acd9c51fbfb579ce4a29bd2850efd855cd4c938` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `5359175e560de31694c6839ab84db03de4619cbf251fc87b62e2dc3f0e6bba5a` | `5359175e560de31694c6839ab84db03de4619cbf251fc87b62e2dc3f0e6bba5a` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `11b1e9911f0edced41a9f94674c9e0a144c696ac52143c958042f55ae9b29d51` | `11b1e9911f0edced41a9f94674c9e0a144c696ac52143c958042f55ae9b29d51` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `6e7c1c67a3dee4bede5959a50a5d332cd7455f215355eaf8a7c7cd7da4b0c619` | `6e7c1c67a3dee4bede5959a50a5d332cd7455f215355eaf8a7c7cd7da4b0c619` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-02-04`
- PackageID: `PKG-02`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
- `docs/ui/UI_POLISH_EXECUTION_PLAN.md` is a non-authoritative evidence-routing checklist derived from REF-006 FR-006, D-APP-36, and the current loop-first design.
