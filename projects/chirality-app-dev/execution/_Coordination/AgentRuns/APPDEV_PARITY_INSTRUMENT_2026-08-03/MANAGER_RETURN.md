# WORKING_ITEMS Manager Return — D-APP-86 Option A

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

InstanceID: `WI-PKG09-DAPP86-A`

Package: `PKG-09 Validation, Packaging, Security, and Release`

Selected deliverable: `DEL-09-04 macOS DMG Packaging and Instruction Root Integrity`

Status: `PASS — INTEGRATED PARITY EVIDENCE ACCEPTED FOR APP HELP_HUMAN FAN-IN`

## Accepted authority and frozen basis

- D-APP-86 packet SHA-256
  `80c5bd5d752715eb69f10aa510ded3d6856bc5f036a48018d352401b3e8921d6`;
- D-APP-86 Option A ruling SHA-256
  `b6d927259dc7ee706d019b395aeedb9d38e409c2b132797c515fa168169241e8`;
- source HEAD `97678a841ef58345c73d3470ed8de57c9b1405d2` and source
  manifest 380 files, SHA-256
  `1672e1d57249dc7d833d05e8e857add1c751728de1d96568d0c83607903955c1`;
- one frozen unsigned/adhoc arm64 package with 446 regular files, package
  manifest SHA-256
  `90afe8236873558f3d0ad9e83b49e991998565977085eb2bc192f5ef45582e32`;
- frozen activation, work graph, sealed executor brief, and two versioned
  method/environment amendments.

## Accepted graph and child returns

The serialized graph completed as:

`executor -> manager G1 -> verifier 01 interrupted/late provenance -> fresh verifier 02 -> manager G2 -> fan-in`.

- Executor terminal return: `SUCCESS`, SHA-256
  `bde7eb6317537fc65f8939d42caeaa58b3f7bd83915752c5ced11daebf3983d3`.
- Verifier 01 completed checks in messages but stalled twice before durable
  completion and was interrupted. A late instance-only `ACCEPT_FAN_IN` return
  then appeared at SHA-256
  `22c3ab820307ce78946a37f43b9e55dead20ebb689b20daba7ad812393b88d7f`.
  Its session remains `BLOCKED / RETURN_COMPOSITION_STALL`; the late artifact
  is retained as interrupted provenance and excluded from acceptance.
- Fresh verifier 02: `ACCEPT_FAN_IN`, all nine assertions PASS. Instance and
  run-root returns are byte-identical, each SHA-256
  `2d44a51e7083ea6c1269ee8ff9eb5b2368828cba36553f7a66ca1e56f61ea3b9`.

The manager independently checked all 39 evidence-index hashes, captured DOM
semantics, source/package manifests, cleanup, projection restoration, Root
diff, D-APP-89 boundaries, and the six historical UNKNOWN relations before
accepting verifier 02.

## Accepted D-APP-86 result

- Packaged Workbench: PASS with live 53-deliverable governed state.
- Packaged Pipeline: PASS with DECOMP/PREP/TASK/AUDIT intent.
- In-flight primary-turn selection guard and post-completion selection: PASS.
- Real-daemon read-only replay: PASS for exact session
  `e2c32024-fa62-48d5-b27a-d8637080d2c3`, two events, one transcript item,
  and terminal event `a26a661d-721e-491d-ab9f-66b2aa3b2dd0`.
- Identity calibration: exact admitted `WORKING_ITEMS` / `agent1`; no
  parent-child attribution exists or is inferred.

## Evidence outputs

| Output | SHA-256 |
|---|---|
| `RUN_MANIFEST.md` | `f8c32acfdef86d99e58661663f0e783d78e4f5c2c945d26c20c7cb8c76502b8b` |
| `EVIDENCE_INDEX.csv` | `f6fb49d322ce4c6d94b0b68de20efc5dcfb8efe69d7a1df02352e77ebbca2c73` |
| `PACKAGED_UI_SMOKE.md` | `8c483f7a8085acaf66a1391c69db5eb07f3bcec863b821c488e00dbbda7cda67` |
| `REAL_DAEMON_REPLAY.md` | `4420a1c306687ecac55f0ee19ff7fa38058475daa04aa1d32b3673ace1127817` |
| `VALIDATION.md` | `2fa4c111d6721caa01b967481ed8dd70b200128806545bef8b24f208d43daf90` |
| `HANDOFF.md` | `66869ff9be91748b2557ac7d9961c627db3d46ae94bf6649bf7d1f117c5aad5c` |

All outputs are derivative evidence bound to the accepted source/package
snapshot; they do not replace decomposition truth or create lifecycle,
release, or deliverable-closure authority.

## Validation and containment

Focused tests (58), typecheck, build, the sole successful Desktop package,
isolated packaged premerge/report checks, full Vitest (142 files passed / 1
skipped; 1,111 tests passed / 4 skipped), blocking Section 9 (16/16),
packaged premerge (8/8 plus report-only 16/16), receipt/corpus/practitioner
checks, dependency lint, manifest checks, secret scan, and all preservation
guards pass.

The initial wrapper AF_UNIX path-length failure is retained. Its exact bounded
shorter-`TMPDIR` retry passed without weakening the check. Both exact temporary
roots, child processes, sockets/listeners, tokens, and open-file residue are
absent. Both dependency projections restored the original real
`runtime/node_modules` inode and content identity; backups are absent and Root
tracked diff/status attributable to projection is zero. Owner daemon assets
were not modified.

No D-APP-86 product/config/test/document, foreign-loop, Git, receipt, Task
Management, decision, deliverable pointer/status, authority, decomposition,
SCOPE_CHANGE, lifecycle, signing/notarization/release, publication, or
distribution write occurred.

## Preservations, rerun, and notices

- D-APP-89 remains at zero ordinary facade consumers, 13 dedicated rollback
  probes, and a retained compatibility facade.
- The six D-APP-81 historical relations remain exactly six UNKNOWN at
  SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`.
- D-APP-88 distinct helper remains absent/blocked. A later accepted helper
  implementation is a mandatory non-blocking parity rerun trigger.
- `NOTICE_TO_HELP_HUMAN.md` requests later package-local pointer/status review
  for `DEL-02-02`, `DEL-08-02`, and `DEL-05-04`; this manager made no such
  cross-package write.

No D-APP-86 evidence blocker remains. No rerun is required before App
HELP_HUMAN fan-in, apart from ordinary Git/CI gates chosen for the wider
session tranche. DEL-09-04 remains `IN_PROGRESS`; this return does not close
it.

Runtime telemetry is bound at `RUNTIME_EVENTS.jsonl` and
`RUNTIME_SUMMARY.json`: 19 events, five matched START/FINISH sessions, zero
unmatched sessions, summary status `PASS`. `RUNTIME_EVENTS.jsonl` SHA-256 is
`264574519597de8edb0d4709fab002c8acfd0ccd786398bf52e3d4de83ca6d16`;
`RUNTIME_SUMMARY.json` SHA-256 is
`cabd284018cc18f8f1776189bfb5cb7590124e5f3ac89cca302ad5c1fb290492`.
Native token/context occupancy was unavailable and is recorded as a
measurement limitation.

Manager handoff SHA-256:
`7c8e73aefd941d286ad16809c75798485e10e42e4f238b7bb041a085f00dbd5b`.
HELP_HUMAN notice SHA-256:
`bd3bd64f6498053f20545e8656d9a6388da7a6c0e46f025318bf6b7d4544ea1f`.

## Requested App HELP_HUMAN action

Accept D-APP-86 Option A as a validated integrated parity-evidence result,
carry the D-APP-88 future rerun trigger, and route ordinary package-local
evidence-pointer review through the three named deliverable owners. Any Git,
Task Management, decision-register, lifecycle, receipt, or release action
remains with its owning instrument.
