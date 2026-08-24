# N4 Return — Post-application Validation Block

**Node:** `N4-SCOPE-CHANGE-01`
**Role:** `SCOPE_CHANGE` Agent 1
**Basis / HEAD:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `BLOCK — AUTHORITY_CORPUS_RECONCILIATION_WRITE_SET_CONFLICT`
**Authority effect:** `VALIDATION_EVIDENCE_ONLY — NO DEPENDENCY OR AUDIT WRITE`

## Fail-closed decision

Gate-4 section 5.4 requires the App authority corpus to be reconciled after
regenerating it through its accepted workflow. The accepted workflow is
defined by
`projects/chirality-app-dev/execution/_Reconciliation/References/_README.md`
and `reconcile_authority_corpus.py` as:

1. `status`;
2. `bump --reason ...`, which writes the existing
   `execution/_Reconciliation/References/AUTHORITY_CORPUS.json`;
3. `apply`, which rewrites authority rows in every governed deliverable
   `_REFERENCES.md`;
4. `audit`.

The Gate-5 steer says `Write set, exactly`. It does not list
`AUTHORITY_CORPUS.json` or any deliverable `_REFERENCES.md`; they are neither
new SCA additions nor run/control evidence nor dependency artifacts produced by
the registered extraction workflow. N4 cannot infer or widen the write set.

The read-only corpus status result is:

```text
corpus current_version: v18
  [MATCH] docs/DIRECTIVE.md            snapshot=e1a3d00b18fa live=e1a3d00b18fa
  [DRIFT] docs/CONTRACT.md             snapshot=6d3a082c5f08 live=842bf170e673
  [MATCH] docs/SPEC.md                 snapshot=eee520f783ce live=eee520f783ce
  [MATCH] docs/TYPES.md                snapshot=998785af3a0f live=998785af3a0f
  [MATCH] docs/PLAN.md                 snapshot=c2196a1076a5 live=c2196a1076a5
  [MATCH] docs/PRD.md                  snapshot=3c357da78277 live=3c357da78277
  [MATCH] AGENT_SOFTWARE_DECOMP.md     snapshot=ad849d9a9274 live=ad849d9a9274
  [MATCH] AGENT_DOMAIN_ENGINE.md       snapshot=bb2df7178d7b live=bb2df7178d7b
DRIFT: 1 ref(s) changed since v18; run `bump` to mint a new version.
```

Exit code was `1`. The read-only `audit` command returned exit `0` and
reported that all deliverable rows remain reconciled to corpus v18. That is
expected pre-regeneration state; it does not cure the live corpus drift or
satisfy Gate-4 section 5.4.

Therefore N4 stopped before dependency extraction, before dispatching
`AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION`, and before any
pointer, receipt, notice, corpus, reference, dependency, or audit write. No
TASK child or AUDIT_DEP_CLOSURE child was dispatched.

## Direct post-application validation completed before the block

All Gate-4 section 5 direct checks that do not require the unauthorized corpus
write passed:

- Applied decomposition:
  `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`,
  `112419` bytes.
- Applied App contract:
  `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`,
  `34877` bytes.
- Applied companion register:
  `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`,
  `98230` bytes.
- Transaction matcher: every D-01 through D-04 and C-01 through C-07 old
  pre-image is absent and approved post-image occurs once; D-05 anchors and
  insertions occur once; C-08 basis pre-image is absent and its application
  anchor/insertion occur once; C-09 through C-11 anchors/insertions occur
  once. Approved C-01 and C-06 substitutions are present exactly once.
- C-10 enforcement-map block: all six exact inserted rows occur once and the
  full insertion block occurs once.
- Topology: exactly 10 packages and 51 deliverables, with the same stable ID
  sets as the basis. The Objectives, Packages, and Scope Ledger sections are
  byte-identical to the basis. N2's relation-level proof additionally records
  unchanged parents, SOW relations, objective relations, and context-envelope
  relations.
- Contract/register parity: 83 unique contract invariant IDs; 83 unique
  register IDs in 50 families; identical ID sets; all 83 `SourceAnchor`
  values resolve to the exact live contract row; every `ContractSourceSHA256`
  and `AppDecompositionBasis` value equals the applied identity. Both new IDs
  occur exactly once in both surfaces.
- Root/App source concordance: ratified Root contract
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`
  and source identities `40cec2df...`, `fe81bc9a...`, `d20fd7dc...`, and
  `22e49ccf...` all reproduce.
- Protected surfaces: `_LATEST.md` remains `a0298fdc...`; Task Management
  register remains `eb37fba1...`; frontend tree remains `74e3dbe8...`; all
  eleven A2-frozen assessment identities reproduce.
- Containment before this return: only the three exact authoritative targets,
  new Phase-5 corrected candidate, and Gate-5 run/control evidence differ from
  the basis. No dependency record, `_DEPENDENCIES.md`, `_REFERENCES.md`, corpus
  file, closure package, pointer, frontend, Root, SOW, status, context, or
  lifecycle surface changed.

## Validator evidence

| Gate | Result |
| --- | --- |
| Agent instructions | `PASS` — 34 files, 0 errors, 0 warnings |
| Instruction entrypoints | `PASS` |
| Task Management register validation | `PASS` — 13 rows |
| App receipt validator, pre-append | `VALID` |
| `git diff --check` | `PASS` |
| Authority-corpus audit at v18 | `PASS`, but does not cure drift |
| Authority-corpus status | `FAIL/BLOCK` — one App-contract drift |
| Candidate whitespace vs `cc196023...` | `FAIL` — N2 `RETURN.md` has one blank line at EOF (line 92) |
| CI-form G4 | correctly deferred until a candidate commit exists |

The whitespace finding is an additional unreached-gate failure. It was not
repaired because the governing corpus/write-set conflict already required an
immediate stop, and the brief forbids further project mutation after that
determination.

## Downstream state

- Dependency extraction for DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05:
  `NOT_RUN_BLOCKED`.
- Named post-application closure audit: `NOT_RUN_BLOCKED`.
- New SCC result: `NOT_EVALUATED`; none was linearized.
- `_LATEST.md`: unchanged; no pointer candidate is an N4 output.

## Required owner/parent disposition

Per Gate-4's rollback rule, a validator failure before pointer movement calls
for restoring all Gate-5 authoritative target pre-images unless the owner
expressly authorizes a non-closure diagnostic state. N4 did not perform
rollback, as its sealed brief expressly reserved that action to the parent.

Recommended fail-closed disposition:

1. restore the decomposition from verified Git blob
   `48ae8edf982f3ce92e7a686993f3832501e42576` and require SHA-256
   `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`;
2. restore the contract and companion register together from blobs
   `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` and
   `ab2e13344d1ce071d2c1167320b7c875c373eaaf`, requiring SHA-256
   `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`
   and `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`;
3. preserve this failure evidence and the independently reviewed N0 candidate;
4. return the exact write-set conflict to the owner for a new authority act
   that either adds the accepted corpus `bump/apply/audit` surfaces to the
   application write set or explicitly dispositions Gate-4 section 5.4;
5. only after that ruling, repeat application/validation, repair the N2
   evidence whitespace in-scope, and perform the four registered dependency
   extractions plus the fresh named audit.

No application closure, pointer readiness, carrier activation, implementation,
lifecycle, release, publication, reliance, or acceptance claim is made.

## Rollback amendment — 2026-08-24

The parent subsequently directed the mandatory Gate-4 rollback. N4 executed
only that rollback and durable rollback/handoff evidence.

| Surface | Basis pre-image | Applied image validated by N4 | Restored image | Restored Git blob |
| --- | --- | --- | --- | --- |
| decomposition | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `48ae8edf982f3ce92e7a686993f3832501e42576` |
| App contract | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `d72b1184b978f8bfa8d84ff2124d0f2871ac2c84` |
| companion register | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` | `ab2e13344d1ce071d2c1167320b7c875c373eaaf` |

Before restoration, N4 re-verified the recovery files in
`/private/tmp/chirality-gate5-n1-recovery.UzeIkF/` against every required
SHA-256, byte count, and Git blob OID. The decomposition was restored by one
`apply_patch` operation. The contract and register were restored together in
one `apply_patch` group. A first dynamically generated numbered-hunk patch for
that group was rejected before write by the patch interface; immediate state
remained applied and intact. The same reverse diff with neutral hunk headers
then applied both files in one group. No partial contract/register state was
created.

Post-restoration verification proved each live target byte-identical to HEAD
and reproduced the three blob OIDs above. Authority-corpus `status` at v18
then returned exit `0`, with all eight members `MATCH` and `no drift.`

The corrected register candidate remains preserved as derivative evidence at
`Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv`, SHA-256
`62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3`.
All N0 through N4 failure evidence remains preserved. N2 `RETURN.md` remains
byte-identical at SHA-256
`94d9ee4dc4da060a270d8e07168c196dde9090bac1db0b7d6968692fefd012cc`;
its terminal blank-line whitespace finding is deferred, not repaired.

The application is rolled back. N5 was not run. No pointer candidate, notice
candidate, dependency extraction, closure audit, corpus version, reference
reconciliation, receipt, commit, push, or PR was produced.
