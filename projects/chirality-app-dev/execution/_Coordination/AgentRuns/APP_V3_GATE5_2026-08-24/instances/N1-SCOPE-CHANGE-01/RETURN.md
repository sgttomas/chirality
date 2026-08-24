# N1 Return — Gate-5 Pre-image Freeze, Reconstruction, and Collision Census

**Node:** `N1-SCOPE-CHANGE-01`
**Role:** `SCOPE_CHANGE` Agent 1
**Basis / HEAD:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `PASS — LIVE APPLICATION MAY PROCEED TO N2/N3`
**Authority effect:** `EVIDENCE_ONLY — NO LIVE AUTHORITATIVE TARGET WRITTEN`

## Private rollback truth

Recovery root:
`/private/tmp/chirality-gate5-n1-recovery.UzeIkF`

The root is mode `0700`; every recovery file is mode `0600`. Each file was
materialized from the exact steer-named Git blob with `git cat-file blob`, not
copied from the mutable worktree. `git hash-object` of the materialized bytes
reproduced each source OID.

| Recovery file | Source blob OID | Verified SHA-256 | Bytes |
| --- | --- | --- | ---: |
| `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `48ae8edf982f3ce92e7a686993f3832501e42576` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | 108079 |
| `CONTRACT.md` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | 27308 |
| `contract_invariant_coverage_register.csv` | `ab2e13344d1ce071d2c1167320b7c875c373eaaf` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | 88985 |
| `_LATEST.md` | `c6ce8b2a92c67506887d95c88790a445dbc5668d` | `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` | 1347 |

Exact materialization method:

```text
umask 077
mkdir -p /private/tmp/chirality-gate5-n1-recovery.UzeIkF
chmod 700 /private/tmp/chirality-gate5-n1-recovery.UzeIkF
git cat-file blob <exact-oid> > /private/tmp/chirality-gate5-n1-recovery.UzeIkF/<target-name>
chmod 600 /private/tmp/chirality-gate5-n1-recovery.UzeIkF/*
git hash-object /private/tmp/chirality-gate5-n1-recovery.UzeIkF/<target-name>
shasum -a 256 /private/tmp/chirality-gate5-n1-recovery.UzeIkF/<target-name>
```

## Private candidate reconstruction

Candidate root:
`/private/tmp/chirality-gate5-n1-candidates.eJwTTx`

The root is mode `0700`; each file is mode `0600`. Full candidates and
rollback copies are not stored in Git. The durable deterministic method is
`N1_RECONSTRUCT.py`, SHA-256
`140843342f278fb3bfdfc87e29b15a233d2743c1b19a6ff10b8950c6b62a2608`.
Its private result JSON is SHA-256
`5c11a534b5d5dc1525a55d73d62fd0aa8e58a15576322f102c79092ed38af140`.

Exact invocation:

```text
python3 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N1-SCOPE-CHANGE-01/N1_RECONSTRUCT.py --repo . --candidate-dir /private/tmp/chirality-gate5-n1-candidates.eJwTTx
```

The method extracted the exact fenced Gate-3 D-01..D-05 and C-01..C-11
transactions, required every old or insertion anchor exactly once, and
applied them in approved order. It substituted only the approved Phase-2b
C-01 LF row and resolved Phase-2b C-06 LF row. C-08 additionally proved its
basis anchor once in the live pre-image, its absence after C-04, and its
post-C-04 application anchor once. N0's corrected register was copied into
the private candidate area only after its full-file identity was required.

| Candidate | SHA-256 | Bytes | Recorded comparison |
| --- | --- | ---: | --- |
| decomposition | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | 112419 | exact Gate-3/Gate-4/A3 required identity |
| App contract | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | 34877 | exact Phase-2b reconstruction record identity |
| corrected companion register | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | 98230 | byte-identical (`cmp` exit 0) to independently reviewed N0 candidate |

Approved substitution identities:

- C-01: `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616`
- C-06: `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`

Anchor counts were `1` for D-01, D-02, D-03, D-04, both D-05 anchors,
C-01 through C-07, the C-08 live basis anchor, the C-08 post-C-04
application anchor, and C-09 through C-11. The superseded C-08 basis anchor
count after C-04 was the required `0`.

## Mechanically re-derived invariant collision census

The census ran against the live App contract, live authoritative companion
register, and ratified Root `docs/CONTRACT.md`. It separately counted exact
contract-row IDs, companion-register ID-column values, and all literal prose
occurrences so incidental prose could not be silently ignored.

| Proposed ID | App exact row / literal | Register ID / literal | Root exact row / literal | Result |
| --- | --- | --- | --- | --- |
| `K-CONSENT-1` | `0 / 0` | `0 / 0` | `0 / 0` | `PASS — COLLISION FREE` |
| `K-UNTYPED-1` | `0 / 0` | `0 / 0` | `0 / 0` | `PASS — COLLISION FREE` |

There was no incidental prose and therefore no ambiguity.

## End-of-node immutable-surface proof

The live pre-images remained exact after reconstruction:

- decomposition `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`;
- App contract `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`;
- companion register `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`;
- `_LATEST.md` `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`;
- Task Management register `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`;
- frontend tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`;
- ratified Root contract `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`
  and A4-A source blobs `40cec2df...`, `fe81bc9a...`, `d20fd7dc...`, and
  `22e49ccf...`.

All eleven A2 assessment files re-hashed to their owner-accepted identities,
and `git diff --exit-code HEAD` over the existing snapshot excluding the new
Phase5 additions returned `0`. No existing Gate-1/2/3/4, Phase-1/2/2b, Root,
frontend, register, pointer, contract, decomposition, SOW, lifecycle, status,
or dependency byte was edited by N1.

## Handoff

N1 is `PASS`. N2 may atomically install only the private decomposition
candidate above after independently rechecking its full identity. N3 may
atomically install the private contract and corrected-register candidates as
one group after independently rechecking both full identities. If any live
pre-image has changed since this record, both nodes must stop before write.
