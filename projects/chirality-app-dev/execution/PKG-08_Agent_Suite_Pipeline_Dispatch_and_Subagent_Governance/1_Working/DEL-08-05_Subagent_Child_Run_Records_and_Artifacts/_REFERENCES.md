# References: DEL-08-05 Subagent Child Run Records and Artifacts

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `d01a61b69e7c8a577c882b5e8391379900d825bb5f2f29438823d466de8edc6d` | `d01a61b69e7c8a577c882b5e8391379900d825bb5f2f29438823d466de8edc6d` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `ec5fe07c43c11a1b7d1f2e3da38655c7db717081687984c064122172fc1abdf2` | `ec5fe07c43c11a1b7d1f2e3da38655c7db717081687984c064122172fc1abdf2` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `db5cd5b3c371d2223fc544cedebc8e86adbf99c1e5b54bdd853cb80084645867` | `db5cd5b3c371d2223fc544cedebc8e86adbf99c1e5b54bdd853cb80084645867` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `7ced6ce4157e2c11e6a82e581d96b7f59e91b3fff98e456ccb61c0d318874511` | `7ced6ce4157e2c11e6a82e581d96b7f59e91b3fff98e456ccb61c0d318874511` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `20bcf55a0a588b8875ad7d278b8e15a42e5f474e35553a9613ba72ee14aba35b` | `20bcf55a0a588b8875ad7d278b8e15a42e5f474e35553a9613ba72ee14aba35b` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `d2db92f4c9ae5cf103ea24a76a46b166a7955b6c77bafa7f9cd0b943ab5f63ec` | `d2db92f4c9ae5cf103ea24a76a46b166a7955b6c77bafa7f9cd0b943ab5f63ec` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-08-05`
- PackageID: `PKG-08`

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
