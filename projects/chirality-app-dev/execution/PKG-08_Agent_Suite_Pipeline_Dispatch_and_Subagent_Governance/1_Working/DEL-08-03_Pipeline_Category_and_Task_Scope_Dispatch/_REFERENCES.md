# References: DEL-08-03 Pipeline Category and Task Scope Dispatch

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `e1a3d00b18fa728f0886f036774c4825ad8f65f3245b56b4545da2714a903031` | `e1a3d00b18fa728f0886f036774c4825ad8f65f3245b56b4545da2714a903031` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `eee520f783ce0161c84bb8c2bd570b7521b3f6926bceea8cde7d387bbc3df990` | `eee520f783ce0161c84bb8c2bd570b7521b3f6926bceea8cde7d387bbc3df990` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `998785af3a0f14a87424339ccb6b242b8932f7a572c4336ac47538c64f3e3169` | `998785af3a0f14a87424339ccb6b242b8932f7a572c4336ac47538c64f3e3169` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `c2196a1076a5e2de44faca7df506a72f0401d0a0161f77a8b583a1d0d7e239ff` | `c2196a1076a5e2de44faca7df506a72f0401d0a0161f77a8b583a1d0d7e239ff` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `d9bcdcb701de08942242425a085e39dad3cba07396cbcf64970a1c4433541485` | `d9bcdcb701de08942242425a085e39dad3cba07396cbcf64970a1c4433541485` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-08-03`
- PackageID: `PKG-08`

## SCA-APP-004 Authority Lineage

| Source | Role | Treatment |
|---|---|---|
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Amendment_Preview.md` | Owner-approved presentation-neutral DEL-08-03 amendment and semantic ownership partition | GOVERNING FOR THIS RECONCILIATION |
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Propagation_Plan.md` | Owner-approved Gate-5 write scope, no-change set, and downstream dispatch/projection validation | GOVERNING FOR THIS RECONCILIATION |
| `execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | Prospective Woven Dialogue ruling preserving dispatch while superseding fixed placement | GATE-5 AUTHORITY; path/hash verified during integration |

The authority-document hashes above are reconciled to authority corpus v16
after the SCA-APP-004 Gate-5 authority/decomposition fan-in.

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
- Work/Agents presentation consumes but does not own DEL-08-03 dispatch
  semantics. Only explicitly recorded work sources may be projected; dialogue
  is not silently converted into tasks.
