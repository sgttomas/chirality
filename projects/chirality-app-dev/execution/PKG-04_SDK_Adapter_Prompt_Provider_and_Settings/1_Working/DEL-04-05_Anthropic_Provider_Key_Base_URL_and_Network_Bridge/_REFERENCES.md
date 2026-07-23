# References: DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | `14c77480c0a010c84be2adb9a8b2066e48118cf5063987a857efd3ae3f3a1317` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `6b67583097daac9d2d44153fe146d895ec370beead39b0a9714fea03b68236df` | `6b67583097daac9d2d44153fe146d895ec370beead39b0a9714fea03b68236df` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `083a106bdb9bd1950f84ec983cbf2a556fa354767e92c9ae7bb1ee574e89af3d` | `083a106bdb9bd1950f84ec983cbf2a556fa354767e92c9ae7bb1ee574e89af3d` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `bf404d5b232d0323af3140c3f72de285be02fcc903f23553ff9fa9ac4d4baf44` | `bf404d5b232d0323af3140c3f72de285be02fcc903f23553ff9fa9ac4d4baf44` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `11b1e9911f0edced41a9f94674c9e0a144c696ac52143c958042f55ae9b29d51` | `11b1e9911f0edced41a9f94674c9e0a144c696ac52143c958042f55ae9b29d51` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `7478bf32e351d868973914b07b8eae0bce0e1b32ed86aa4d7e42c6d4657b6db3` | `7478bf32e351d868973914b07b8eae0bce0e1b32ed86aa4d7e42c6d4657b6db3` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-04-05`
- PackageID: `PKG-04`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
