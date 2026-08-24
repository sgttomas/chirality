# N4 Mandatory Gate-4 Rollback

**RunID:** `APP_V3_GATE5_2026-08-24`
**Basis / HEAD:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Rollback state:** `COMPLETE — AUTHORITATIVE TRUTH RESTORED`
**Blocker state:** `OPEN — OWNER WRITE-SET DECISION REQUIRED`

## Recovery-source verification

The exact N1 recovery files were re-verified before restoration:

| Surface | Recovery SHA-256 | Bytes | Git blob OID |
| --- | --- | ---: | --- |
| decomposition | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `108079` | `48ae8edf982f3ce92e7a686993f3832501e42576` |
| App contract | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `27308` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` |
| companion register | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `88985` | `ab2e13344d1ce071d2c1167320b7c875c373eaaf` |

## Exact rollback lineage

| Surface | Pre-image | Applied image | Restored image | Result |
| --- | --- | --- | --- | --- |
| decomposition | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `PASS` |
| App contract | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `PASS` |
| companion register | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `PASS` |

The decomposition was restored with one `apply_patch`. The contract and
companion register were restored together with one successful `apply_patch`
group, preserving the Gate-4 atomic-group rule. Live-file `git hash-object`
and SHA-256 checks reproduced every required identity, and `git diff
--exit-code` over all three targets returned `0`.

## Post-rollback gates

- Authority corpus: v18, all eight members `MATCH`, `no drift`, exit `0`.
- `_LATEST.md`: SHA-256
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`.
- Task Management register: SHA-256
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.
- Frontend tree: `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- No dependency record, `_DEPENDENCIES.md`, `_REFERENCES.md`, authority-corpus
  file, closure-audit package, `_Evaluation` file, pointer, Root path,
  frontend path, SOW, status, context, lifecycle, receipt, or other project
  surface was written.
- The corrected companion-register candidate and all N0-N4 evidence remain
  preserved as non-authoritative derivative/run evidence.
- The N2 evidence-whitespace finding remains deferred and byte-preserved.

## Blocker and resume rule

Gate-4 section 5.4 requires the accepted authority-corpus regeneration
workflow. That workflow writes `AUTHORITY_CORPUS.json` and governed
deliverable `_REFERENCES.md`, but the Gate-5 steer's exact write set names
neither. The next owner act must decide whether to expand the exact write set
to those workflow outputs and then separately authorize resume/reapplication.
No resume or reapplication may be inferred from this rollback.

N5 was not run. Pointer and notice candidates were not produced. No PR exists
for this rolled-back application attempt.
