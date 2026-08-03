# S4 SCOPE_CHANGE return — COV-POST-001 exact candidate

Status: `CANDIDATE_READY — STOPPED_BEFORE_APPLICATION`

## Result

Against frozen live decomposition SHA-256
`69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`,
S4 prepared one exact metadata-only candidate SHA-256
`23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`.
Exact unified diff SHA-256 is
`205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e`.

Only the three COV-POST-001 passages change. Each records completed exact
SCA-003 acceptance/application, cites owner-ruling SHA-256 `12f7c46e…89129`
and applied-file evidence SHA-256 `f2781dd2…01cc8`, and refers confirmation
status only to the SCA-003 `Decision_Log.md`. The corrected passages contain
neither `pending` nor `confirmed` as current-facing state.

## Validation

`COV_POST_001_Validation.json` reports 20/20 PASS:

- all 12 frozen authority/source/protected hashes reproduce;
- candidate equals the live source after exactly three authorized
  replacements;
- future-truth wording constraint passes;
- all 89 decomposition identifiers remain unchanged;
- DEC-023 is byte-preserved and decision-row count is unchanged;
- PRD, companion registers, `_LATEST.md`, applied/audit evidence, and live
  decomposition remain unchanged.

## Durable evidence

| Artifact | SHA-256 |
|---|---|
| Exact candidate | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| `COV_POST_001_Exact_Amendment.diff` | `205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e` |
| `COV_POST_001_Validation.json` | `feccaf181660b6bf06f4a92066108ff3678553e1bbca5d28c794bfda81b174af` |
| `COV_POST_001_Candidate_Presentation.md` | `b662d36eaa96ebfa187087c7ef87e57a8438565925b118bb0c8f8e86a9e9bfea` |
| `validate_cov_post_001_candidate.py` | `924831ce5f29d34fae996c1194c2150ade7830e1862ae6bcccfaa898588f3bb4` |
| SCA-003 `Decision_Log.md` | `7da702b0478b20bd4a0cbb50fa6014b6459f192ccbf198ac9933cef4260bf60b` |
| SCA-003 `Handoff_State.md` | `b698462e7a309108005abf617b30bd4b52f1bddd96d1b107e372eb18a2b0f031` |

## Next owner gates

`COV_POST_001_Candidate_Presentation.md` carries the exact acceptance token
followed by the separate exact application token, both bound to candidate
`23f6ae0f` and diff `205edf58…5e92e`.

No application, human confirmation, SCA closure, `_LATEST.md`, companion,
DEL-packet/N0, runtime/client/project, lifecycle/release/reliance, Task
Management, or Git action occurred. COV-POST-001 remains open on the unchanged
live source until separately accepted, applied, and backchecked.
