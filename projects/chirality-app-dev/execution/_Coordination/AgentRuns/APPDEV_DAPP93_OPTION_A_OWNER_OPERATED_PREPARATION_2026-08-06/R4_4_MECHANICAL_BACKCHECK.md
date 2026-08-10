# R4.4 mechanical backcheck

Verdict: `PASS — STABLE RAW-PRODUCER SUCCESSOR READY TO FREEZE`

Authority basis:

- R4.4 adoption SHA-256
  `6f1ee884c91b123d43cdb0aff816a5326f2065ca7b103f99e2f1a237c6af18bd`;
- work-graph amendment v1.10 SHA-256
  `397cd21daa4d4c52c87e08a778fff15dac71b4a247a6ff47520d21ac6f1366a3`;
- accepted sole verifier BLOCK SHA-256
  `a4c09714934163edd6181e5b932a20593bad1a98dab8ff8219fe5902b0a1e386`;
- accepted predecessor freeze SHA-256
  `7f4a9858f8ba2947ce1db522f82669678369b0a4ac3f09a20a5c66bc7747ddf1`.

## Mechanical results

| Check | Result |
|---|---|
| Ledger cardinality/range | PASS — 93 rows, 93 unique IDs, exact C196/C197 plus contiguous C1067-C1157 |
| Exhaustive command classification | PASS — 93/93 rows in `R4_4_COMMAND_INVENTORY.md` |
| Individually enumerated evidence inputs | PASS — C1130 17; C1146 30; C1149 17; C1150 2; C1153 2; C1154 3; C1155 6; C1156 8; C1157 4 |
| Evidence command code-span forbidden-token audit | PASS — 98 exact command spans; zero parser, loop, function, case/if/while, command substitution, logical chain, or derived-pipeline hits |
| C1105-C1108 raw exit sidecars | PASS — tee retained; immediate `pipestatus` assignment/printf retained; no branch, conditional, arithmetic enforcement, or explicit exit |
| Old runbook/evidence derived artifacts | PASS — zero `CONTROL_RANGE_INDEX`, `RETAINED_EVIDENCE_MANIFEST`, `COMPLETENESS_RESULT`, `PASS_COMPLETE`, `STOP_INCOMPLETE`, `d93_begin`, or `d93_end` tokens |
| Later-ingestion ownership | PASS — manifest, range, hash comparison, completeness, exact zero-exit/PASS crosscheck, and terminal verdict are explicit intake duties |
| Branch/precondition matrix | PASS — all nine required failure classes have satisfiable prerequisites and no impossible command |
| Raw producer/copy/hash matrix | PASS — 21/21 ordinary primary raw objects have exact producer/export, one-file returned copy or direct export, and one-file whole-file SHA stdout sidecar |
| C196/C197 preservation | PASS — exact rows retained; row SHA-256 `9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb` / `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52` |
| Ordinary order | PASS — runbook and ledger require C1145→C1144→C1130; pre-C196 routes invoke neither C1144 nor C1130 |
| Unaffected prepared-object identities | PASS — reconstruction manifest `774fed30…57f`, LLDB script `720ad198…5f8`, static revalidation `46ad1692…459` unchanged |
| Prepared index self-consistency | PASS — all eight embedded member hashes reproduce; index SHA-256 `3b66000b11cbc65e215d2669781b614eb6f14260d9c7552fb1d1f05cbf77c589` |
| Candidate trailing whitespace / `git diff --check` | PASS |
| Receipt validator | PASS |
| Authority corpus | PASS — v18, eight MATCH, no drift |
| Practitioner status | PASS — no findings for App project |
| Repository self-check | PASS — exit zero; existing non-blocking baseline findings only |
| Practitioner harness pytest | PASS — 349 passed |
| Frontend cleanliness | PASS — zero frontend dirty paths |
| Fixed temp root / returned path | PASS — both absent |
| Write containment | PASS — this repair adds/changes only authorized D-APP-93 run-local prepared/control records; inherited unrelated App dirty state preserved |
| Frontend runtime gates | SKIPPED — control/evidence documentation only; no product byte changed |

## Exact prepared identities

| Object | SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` |
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `4cebb0215e69817eac470e593604bd801e91411e2634ad558d8a82fd09e9c23d` |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `df92286f3a2638069138b4b610e4647e10b843fc0944a88f89729fcae83deeae` |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `e79f0dcdfab2a3d4263576260101eebd26840ac788cb748b634fda2687d819f3` |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `75158709c300891bfe266a6905ab49b51812bd738b119c04229f7ae5040f23a4` |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `ec6d6992caabb5e50ec2dc796ecf9d17b6a91d4b4a59fd36cbcc72f89945b9c6` |
| `prepared/PREPARED_PACKET_INDEX.md` | `3b66000b11cbc65e215d2669781b614eb6f14260d9c7552fb1d1f05cbf77c589` |

No packet command was approved or executed. No verifier was dispatched.
C196/C197 remain valid, exact, and unused. No runtime, debugger, package,
helper/GUI, signal, credential, product, release, reliance, Git mutation, Task
Management, or foreign-loop effect occurred.

