# D84 scanner repair activation

Status: ACTIVE / AUTHOR DISPATCH READY

Caller: HELP_HUMAN Agent 0. Manager: WORKING_ITEMS Agent 1 `/root/pec_d84_repair`. Package `PKG-01`; selected deliverable `DEL-01-05` only. Native descendant roles are instruction-asserted.

Selection authority is D-PEC-84 S-A plus exact L as observable on `origin/main` `62636f3a1ccc247af8c598b3c0a74ce9179d1fd3`. The execution branch is `codex/pec-d83-d84-execution-20260907` at accepted Iteration 02 commit `14f42e9ce17effa52e6415cc205a2df969b1256d`. Accepted prerequisites are D83 terminal seal `501366e971d57d8030a73269648ed55942cc6fc97842e44324b7886695c2bad6`, D84 L terminal seal `c9654a03635885fa22a450da153136d1a1ed6a01d9ac3a58059dd4b9cc233ae3`, and common seal `017802d4782b6d0362031e756be7b7b0e3cfae65347fd9b8f25014aa9fb22014`.

Live `_STATUS.md` is `IN_PROGRESS`, SHA-256 `7d3eeb9888f10f6e938c7a0c08ff22ee1907df89812064ee76a95e0fdaeae60c`. The three exact product preimages reproduce D84 TARGETS. Six pre-dispatch checks covering `dispatch-for-production` and `rely-for-production` for each product target returned `ALLOW`.

The frozen work graph is serialized terminal fan-out/fan-in:

1. `AUTHOR`: one TASK + `software-bounded-implementation` Agent 2 implements the two exact scanner repairs, tests the full specified matrix, and writes bounded BASIS/AUTHOR/CHECKS evidence.
2. `VERIFIER`: a fresh independent evidence-only Agent 2 starts only after manager acceptance of the author return. It writes only `VERIFICATION/**` and never repairs product or author evidence. Findings return to a separately recorded author correction attempt while preserving the initial review and failure evidence.
3. `BACKCHECK`: separately parent-dispatched RECONCILIATION work owns only the six exact `BACKCHECK/**` outputs after author and verifier pass. WORKING_ITEMS does not write or dispatch them.
4. `FAN_IN`: WORKING_ITEMS validates all returns and writes the terminal self-excluded seal and handoff. REVIEW, lifecycle acceptance, Remaining, release, receipts, and Git remain outside this activation.

Product writes are limited to the three exact files in `SCANNER/TARGETS.json`. Evidence writes are limited to the exhaustive subpaths adopted through `SCANNER_EXACT_ACTS_AND_EVIDENCE.md`, with the six `BACKCHECK/**` paths reserved to RECONCILIATION. No config, workflow, core, fixture tree, contract, SOW, dependency, status, Root, sister-project, database, service, lifecycle, acceptance, or Git write is allowed.

Passing evidence is finite scanner evidence only. It does not establish universal confinement, close VER-004 or OI-009, reapply the frozen D83 preview, accept repaired artifacts, re-enter CHECKING, issue, or release the deliverable.
