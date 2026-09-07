# Final applied review — Root D-GOV-36 account-only amendment

Verdict: **PASS — LIVE APPLICATION MATCHES THE FROZEN REVIEWED CANDIDATE.**

Reviewer: bounded ephemeral Agent 2 under HELPS_HUMANS. Role and non-delegation are instruction-asserted. This review made no canonical, notice, receipt, App product/deliverable, Runtime, index, or Git mutation.

## Reviewed identity and state

- Frozen candidate patch SHA-256: `a4e94ea7a506cf71759208a7754fc8e1b218aeb0870952128529d2a1c9cca9ae`.
- Application HEAD basis: `a52e754491041b43ac4bc9414dff9becd52207ff`.
- Current validation HEAD and `origin/main`: `9428e4af44c91063f2188e31698e4c84d8549be9`.
- The fast-forward from the application basis to the validation basis has zero delta on the tracked target paths. The live tranche remains `APPLIED_UNPUBLISHED`; the 2026-09-07 amendment has no publication/effective identity yet.
- The candidate dispatch basis `1ffa47863b9a53ab359d84e1c72ca7d93a69b47d` remains historical and is not represented as the application or validation HEAD.

## Exact applied effects

The candidate contains exactly eight effects, and the live state matches all eight:

1. D-GOV-36 is byte-identical to the author postimage, SHA-256 `2697862a31ee856ae923c91af38a5e07f8997115a4bd1baabf083afb069939b1`.
2. `_DECISIONS/_REGISTER.md` is byte-identical to the author postimage, SHA-256 `2d487f56cd69f634c71495dbff9654de1ad3e11218733e37c263b778b3e8e907`; its diff changes only the D-GOV-36 row.
3. The G4 manifest is byte-identical to the author postimage, SHA-256 `c6351c30772c3ae14043a60fb3430bacbbc7d7ad2cb5fd5d09138f5ace6dcab6`.
4. The Root-origin App notice matches its author postimage, SHA-256 `0a6073781d267e18be144f05e77677b1e459747462f62f9743e94af0a86a3fb7`.
5. The Root-origin Runtime notice matches its author postimage, SHA-256 `7d7823b14de1e81911ca2384dead44253e56301d1f5e706c4bf783fdbb8d151d`.
6. The App receiving notice matches its author postimage and Root-origin pair, SHA-256 `0a6073781d267e18be144f05e77677b1e459747462f62f9743e94af0a86a3fb7`.
7. The Runtime receiving notice matches its author postimage and Root-origin pair, SHA-256 `7d7823b14de1e81911ca2384dead44253e56301d1f5e706c4bf783fdbb8d151d`.
8. Receipt 148 occurs once and is the exact author append suffix, SHA-256 `013249497fc4f9589856584cd34569e8639aee48c4efd1bd7c05cdfff36a2426`; the resulting full receipt file SHA-256 is `b47766923d655d7b7300f5399b72bb1ebb1abf7a15fc27b3fd9961871f5a9576`.

`git apply --reverse --check` passes for the frozen patch against the live tree. Forward apply fails as expected for an already-applied patch.

## Authority, metadata, and boundaries

- D-GOV-36 truthfully backfills the prior D126 candidate `4827bbe0cf309aa891c90bdf4c38586f726abb21` and PR #740 merge/effective identity `e1dee34315ff4ca448b0fbc14e5542b6bad9fac2`. That merge is an ancestor of current `origin/main`.
- Historical D126 substance is preserved; the current-facing metadata is corrected without treating the later amendment as published.
- The owner’s narrow amendment ruling supplies semantic/M2 authority, and the successor-resume direction authorizes faithful reviewed Root application. The eight live effects contain no invented exact-text, exact-file, boundary, M2, exact-head, or merge vote requirement.
- The amendment remains limited to dedicated authenticated account-only public Unix authority for nonexecuting bootstrap authentication, status/cancellation, and hosted-account lifecycle control/observation. It grants no project access or consent, model/tool execution, direct private-supervisor access, TCP listener, additional enrollment, implementation, supplier acceptance, protected-fixture use, readiness, lifecycle promotion, release, or downstream App/Runtime adoption.
- M6 is concrete: the manifest routes to both receiving paths, all four notice files exist, and each origin/receiving pair is byte-identical. The notices coordinate owning-loop follow-on and do not claim adoption.

## Checks evidence

The durable application evidence records postimage parity, Receipt 148 suffix parity, reverse applicability, Root G0–G4 CI-mode checks, instruction entrypoints, tranche-scoped whitespace, 836 tests plus 45 subtests, and `git diff --check` as passing. It retains the whole-worktree whitespace failure caused by shared untracked evidence instead of rewriting it as a pass, and defers the exact committed-range checks to CHANGE.

Independent spot checks reproduced the eight-effect patch inventory, all postimage comparisons, notice-pair identity, one-row register delta, receipt uniqueness/suffix identity, reverse applicability, D126 ancestry, validation-basis target stability, and G4 CI-mode PASS using the repository’s Python 3.13 interpreter. `/usr/bin/python3` lacks PyYAML; this operational interpreter limitation is already recorded in the application evidence and does not contradict the authoritative rerun.

Evidence identities:

- `APPLICATION_CHECKS.md`: SHA-256 `930fb317f9fd4b8eb0794ac73e8ad4fe6228e10dc9b76b9bfaa217ea5226406e`.
- `APPLICATION_CHECKS.json`: SHA-256 `139d85c89a418cc1bcdf7f16ededddaf2967df035731bacf3f2ff0032c158199`.
- `APPLIED_IDENTITIES.json`: SHA-256 `147d70ad72d078d0193b882a9e721f1ce9d9bfd116f437a7c17a8f86d8b191a2`.

This PASS covers the live applied, unpublished Root tranche. CHANGE still owns the recorded committed-range G4/whitespace checks, commit/push/PR sequence, matching-head evidence, and fetched-main observability backcheck under the standing Git grant.
