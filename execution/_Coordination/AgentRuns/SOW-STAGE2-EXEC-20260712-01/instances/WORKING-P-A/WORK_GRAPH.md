# WORKING-P-A Package Work Graph — v10

Status: `FROZEN FOR DISPATCH`
Selection authority: `AGENT_0` sealed P-A launch under the human-accepted
D-GOV-16 Stage-2 plan
Posture: `MIXED`
Package: App `PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies`
Members: `DEL-07-01` through `DEL-07-06`
Basis: synchronized `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`;
P3 B1/G3 PASS; Stage-1 App evidence
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`
Amendment: `PILOT-VALIDATION-001`

## Nodes and ownership

| Node | Owner | Depends on | Writes | Return / gate |
|---|---|---|---|---|
| EXTRACT | WORKING-P-A | activation preflight | `candidates/P4_PILOTS/APP-PKG07/**`; child isolated-workspace seeds | six exact candidate blobs and hashes |
| V-01-A | TASK-APP-DEL-07-01 | EXTRACT, PILOT-VALIDATION-001 | own child instance/evidence only | FAILED_SUBSTRATE — nonterminal after two recovery turns; evidence unaccepted |
| V-01-R1 | TASK-APP-DEL-07-01-R1 | EXTRACT, PILOT-VALIDATION-001, V-01-A disposition | fresh own child instance/evidence only | terminal PASS |
| V-02 | TASK-APP-DEL-07-02 | EXTRACT, V-01 slot release | own child instance/evidence only | terminal PASS |
| V-03 | TASK-APP-DEL-07-03 | EXTRACT, V-02 slot release | own child instance/evidence only | terminal PASS |
| V-04 | TASK-APP-DEL-07-04 | EXTRACT, V-03 slot release | own child instance/evidence only | terminal PASS |
| V-05 | TASK-APP-DEL-07-05 | EXTRACT, V-04 slot release | own child instance/evidence only | terminal PASS |
| V-06 | TASK-APP-DEL-07-06 | EXTRACT, V-05 slot release | own child instance/evidence only | terminal PASS |
| FAN-IN | WORKING-P-A | six TASK PASS | package manifests/checks/handoff/return | package PASS or blocking handoff |

Shared reads are permitted. Child writes are disjoint. Initial dispatch was
serialized because one shared Agent-2 slot was available. After the P-P
manager checkpointed and released its slot, Agent 0 authorized at most two
concurrent App verifier children. Numeric replenishment occurs only after a
predecessor terminal PASS is manager-accepted. The ordering is a substrate
constraint, not a semantic dependency. WORKING-P-A is the sole extraction and
package-integration owner.

## Fan-in gates

Each child must reproduce source/status/candidate identity, current P3-bound
legacy-only `LEGACY_FOUR_DOC` validity, extracted target-only `SOW_V1`
validity, map and target closure, parity/source-line preservation,
deterministic checklist, repeated safe deterministic render,
control/lifecycle containment, Stage-1 evidence identity, separate
schema/content/preservation/substrate verdicts, and an exact five-path future
replacement manifest. Per `PILOT-VALIDATION-001`, no synthetic dual overlay,
conversion, marker insertion, authority weakening, or candidate mutation is
allowed. Six terminal PASS returns plus package-level registered App checks
are required.

Any drift, semantic delta, missing source/member, authority mismatch, child or
required-check failure, live-project write, or scope breach blocks P-F. No
child repairs content. No project, Git, lifecycle, conversion integration,
H1/H2, release, or retirement write is authorized.

## Runtime amendment 001

`TASK-APP-DEL-07-01` completed deterministic core tool outputs but never
produced a terminal return/status after two parent interrupt/resume recovery
attempts and no reported semantic blocker. The parent classified it as an
execution-substrate failed attempt. Its immutable brief, DISPATCHED status,
PENDING run record, and partial outputs are preserved but unaccepted; no PASS
is inferred. `TASK-APP-DEL-07-01-R1` is a fresh replacement that must
independently reproduce every v2 gate before V-02 may release.

## Runtime fan-in 002

`TASK-APP-DEL-07-01-R1` returned terminal `PASS` with a `SUCCESS` TASK run
record. Manager fan-in independently confirmed terminal status/return,
`LEGACY_FOUR_DOC` live validity, `SOW_V1` target validity, exact candidate and
source/status identity, the exact five-row replacement manifest, and a clean
App project working tree. V-01-R1 is accepted and the serialized Agent-2 slot
is released to V-02.

## Runtime scheduling amendment 003

Agent 0 reported that WORKING-P-P checkpointed `HOLD_SLOT` and ended its turn,
freeing one Agent-2 slot. V-02 remains active and V-03 is released concurrently
under its pre-sealed disjoint brief. No more than two App children may be
active; subsequent numeric nodes release only after a predecessor terminal
PASS is accepted at manager fan-in.

## Runtime fan-in 004

`TASK-APP-DEL-07-02` returned terminal `PASS` with a `SUCCESS` TASK run record.
Manager fan-in confirmed terminal status/return, valid split-state formats,
exact candidate/source/status identity, 31/31 mappings, 353/353 source lines,
byte-stable checklist/render pairs, the exact five-row future replacement
manifest, and clean App/Git containment. V-02 is accepted and its slot is
released to V-04 while V-03 remains active.

## Runtime fan-in 005

`TASK-APP-DEL-07-03` returned terminal `SUCCESS/PASS` with a `SUCCESS` TASK
run record. Manager fan-in confirmed terminal status/return, valid split-state
formats, exact candidate/source/status identity, 31/31 mappings, 339/339
source lines, byte-stable checklist/render pairs, the exact five-row future
replacement manifest, and clean App/Git containment. V-03 is accepted and its
slot is released to V-05 while V-04 remains active.

## Runtime fan-in 006

`TASK-APP-DEL-07-04` returned terminal `PASS` with a `SUCCESS` TASK run record.
Manager fan-in confirmed terminal status/return, valid split-state formats,
exact candidate/source/status identity, 34/34 mappings, 383/383 source lines,
byte-stable checklist/render pairs, the exact five-row future replacement
manifest, and clean App/Git containment. V-04 is accepted and its slot is
released to V-06 while V-05 remains active.

## Runtime fan-in 007

`TASK-APP-DEL-07-05` returned terminal `PASS` with a `SUCCESS` TASK run record.
Manager fan-in confirmed terminal status/return, valid split-state formats,
exact candidate/source/status identity, 35/35 mappings, 419/419 source lines,
byte-stable checklist/render pairs, the exact five-row future replacement
manifest, and clean App/Git containment. V-05 is accepted; V-06 remains the
only active verifier.

## Runtime fan-in 008

`TASK-APP-DEL-07-06` returned terminal `PASS` with a `SUCCESS` TASK run record.
Manager fan-in confirmed terminal status/return, valid split-state formats,
exact candidate/source/status identity, 29/29 mappings, 309/309 source lines,
byte-stable checklist/render pairs, the exact five-row future replacement
manifest, and clean App/Git containment. V-06 is accepted and no verifier
remains active.

## Package fan-in 009

All six accepted verifier returns pass the corrected gate. Aggregate manager
checks confirm 191/191 mappings, 2,173/2,173 source lines, six exact P3-bound
candidate rows, a 30-row future replacement manifest, its exact 30-row inverse
rollback manifest, deterministic checklist/render pairs, Stage-1 blob identity,
safe HTML, schema/hash/path/diff hygiene, and an unchanged App project at the
accepted base. FAN-IN is `PASS`; the derivative candidate package is ready for
HELP_HUMAN cross-package P-F review only. No integration or lifecycle authority
is implied.
