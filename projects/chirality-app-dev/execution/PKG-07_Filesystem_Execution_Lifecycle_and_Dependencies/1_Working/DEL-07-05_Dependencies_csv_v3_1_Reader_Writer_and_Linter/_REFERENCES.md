# References: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `2f52a24cee9badd4ae21347195d1e7d54739bbf41929d1da535e25429d2923b4` | `2f52a24cee9badd4ae21347195d1e7d54739bbf41929d1da535e25429d2923b4` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `2a63277adade281c0540e18c001bf607978e89e8b6876f50d00a2ea139701913` | `2a63277adade281c0540e18c001bf607978e89e8b6876f50d00a2ea139701913` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `aed33a0f059701be171eedd25caeab6b1530b4cf7e7c1addefe14d29f01684fa` | `aed33a0f059701be171eedd25caeab6b1530b4cf7e7c1addefe14d29f01684fa` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `6f0baacc2bd0b626f8fc0639624fd94bfd048445c9c5ebc4453ac09d8289bc98` | `6f0baacc2bd0b626f8fc0639624fd94bfd048445c9c5ebc4453ac09d8289bc98` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` | `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | `4f2c0a662fcd9eafdb20664997d05ce4734d99dd55a7ca2bb760ed9c94a60fab` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-07-05`
- PackageID: `PKG-07`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
