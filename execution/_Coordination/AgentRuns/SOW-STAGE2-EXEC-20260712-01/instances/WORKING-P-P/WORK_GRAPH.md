# WORKING-P-P Intra-Package Work Graph — v3

Status: `COMPLETE — 4/4 MANAGER-ACCEPTED PASS`
Selection authority: `HUMAN` through accepted D-GOV-16 Stage-2 plan and sealed
WORKING-P-P brief v1
Posture: `MIXED`
Package: Piping `PKG-13_Physical Design Knowledge and Constraint Engine`
Selected set: `DEL-13-01`, `DEL-13-02`, `DEL-13-03`, `DEL-13-04`
Basis: `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`
Amendments: `PILOT-VALIDATION-001`; `SCHEDULING_AMENDMENT_v3.md`

## Ownership and sequence

Version 2 replaced the over-specified transient-dual criterion with the
accepted two-state atomic gate: current legacy-only validates as
`LEGACY_FOUR_DOC`; the byte-exact extracted target alone validates as
`SOW_V1`. No child inserts a marker, invokes conversion, overlays content, or
mutates a candidate.

Version 3 changes scheduling only: after App pilot PASS and explicit parent
slot release, at most two disjoint Piping verifier children run concurrently.
The manager launches 13-01 and 13-02 first and replenishes the numeric next
only after accepting a terminal PASS. All v2 child briefs and acceptance gates
remain unchanged.

The manager is the serialized extraction and package-integration owner. It
extracts the four exact Stage-1 candidate blobs into disjoint candidate
directories, freezes each child brief and isolated verification workspace,
and runs package-level registered checks. The four Agent 2 TASK verifier nodes
are logically independent and have disjoint writes. Runtime concurrency is
bounded to two by `SCHEDULING_AMENDMENT_v3.md`.

| Node | Owner | Dependencies | Runtime state | Read scope | Write ownership | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|---|
| `M0-PREFLIGHT` | WORKING-P-P | B1G PASS | PASS | refs; P3/P2; project authority/profile; exact four live deliverables | manager instance/candidate evidence only | synchronized basis and zero source/status/candidate drift | exact refs, rows, hashes, lifecycle, authority |
| `M1-EXTRACT` | WORKING-P-P | M0 | PASS | Stage-1 commit and four SOW blobs | `candidates/P4_PILOTS/PIP-PKG13/**`; child workspace seeds | four exact candidate hashes and immutable input copies | 4/4 expected candidate hashes; no semantic regeneration |
| `V-13-01` | TASK + `scope-of-work` VERIFY | M1; parent slot release | PASS — MANAGER ACCEPTED | one P3 row; current source/control set; frozen legacy-only copy; extracted SOW-only target; Stage-1 evidence; active tools | `instances/WORKING-P-P/children/TASK-PIP-13-01/**` | amended twelve-part two-state verification return | terminal PASS; exact five-path future replacement manifest |
| `V-13-02` | TASK + `scope-of-work` VERIFY | M1; parent slot release | PASS — MANAGER ACCEPTED | same bounded classes for DEL-13-02 | `instances/WORKING-P-P/children/TASK-PIP-13-02/**` | amended twelve-part two-state verification return | terminal PASS; exact five-path future replacement manifest |
| `V-13-03` | TASK + `scope-of-work` VERIFY | M1; parent slot release | PASS — MANAGER ACCEPTED | same bounded classes for DEL-13-03 | `instances/WORKING-P-P/children/TASK-PIP-13-03/**` | amended twelve-part two-state verification return | terminal PASS; exact five-path future replacement manifest |
| `V-13-04` | TASK + `scope-of-work` VERIFY | M1; parent slot release | PASS — MANAGER ACCEPTED | same bounded classes for DEL-13-04 | `instances/WORKING-P-P/children/TASK-PIP-13-04/**` | amended twelve-part two-state verification return | terminal PASS; exact five-path future replacement manifest |
| `M2-CHECKS` | WORKING-P-P | M1 | PASS | frozen candidates; registered project profile; root validators | manager evidence only | applicable package checks and inapplicability record | all applicable checks PASS; see `CHECKS.md` |
| `M3-FANIN` | WORKING-P-P | V-13-01..04 PASS; M2 PASS | PASS | four terminal child packages and manager checks | package manifests, handoff, RETURN/STATUS | exact 4/4 fan-in | zero drift/failure/project write; P-F recommendation only |

Edges: `M0 -> M1`; `M1 -> each V`; parent slot release gates each `V`;
`M1 -> M2`; `V-13-01..04 + M2 -> M3`. Verifier nodes may run in any
capacity-valid order because their writes are disjoint, subject to the v3
numeric replenishment rule and maximum concurrency two. The manager never
substitutes its own verification for a missing child return.

## Escalation and authority gates

Any source/status/candidate delta, semantic change, missing member, failed
tool/check, project-path write, authority conflict, or invalid child return
blocks M3 and is reported upward. H1, H2, the ISSUED PKG-01 member, project
content, lifecycle, Git, integration, release, and legacy retirement remain
outside this graph. P-F stays parked until both P-A and P-P independently PASS.

Human decision points: none inside preparation. H1/H2 remain later explicit
human gates and are not implied by this graph.
