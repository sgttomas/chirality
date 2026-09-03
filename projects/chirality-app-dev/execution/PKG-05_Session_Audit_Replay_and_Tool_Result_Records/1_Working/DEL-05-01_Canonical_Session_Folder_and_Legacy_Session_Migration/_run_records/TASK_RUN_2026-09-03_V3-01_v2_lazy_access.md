# TASK RUN — 2026-09-03 — DEL-05-01-V3-01 v2 lazy non-destructive access

| Field | Value |
|---|---|
| Deliverable | DEL-05-01 |
| Remaining item | DEL-05-01-V3-01 (`SELECTABLE` at basis) |
| Role / method | ephemeral Agent 2 implementer, `software-bounded-implementation` |
| Model | Claude Fable 5.1 (`claude-fable-5-1`) under HELP_HUMAN (Claude Fable 5.1) |
| Run record | `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/` |
| Basis | `0c683fb1657706316272951e4c3a0f7781b46009` |
| Branch | `codex/app-v3-nodeD-v2-session-access-2026-09-03` |
| APP-HOLD-1 | dispatch preflight `ALLOW` for DEL-05-01 |
| A1 re-stage | declared (`frontend/src/**` touched) — see run record `STEP0_DISCOVERY.md` |

## Scope executed

Typed, lazy, non-destructive access to v2 (2.0.0) project-local session
records in `frontend/src/lib/harness/session-manager.ts`; representative
fixtures under `frontend/src/__tests__/fixtures/sessions/v2/`; evaluator
`frontend/src/__tests__/lib/session-manager-v2-legacy-access.test.ts`;
existing `session-manager.test.ts` extended to byte-identity assertions.
Evidence packet: `Evidence/V3-01_v2_lazy_access_2026-09-03/`.

## Agent decision latitude exercised (D-APP-60 / D-APP-64; recorded here, cross-cutting copy in the run record)

1. **Legacy flat file retained after first touch** (rejected alternative:
   keep the pre-existing `rm` of the flat file per the D-APP-41 "removing"
   wording). Selected because the seated item, `docs/SPEC.md` §25.4, and
   the sealed brief require non-destructive access; R004 is honoured
   operationally (post-touch operations use the canonical record; the flat
   file is never written). Cleanup of the retained source is the unseated
   S-4 amendment.
2. **Typed failure carried under `SESSION_NOT_FOUND` with status 422**
   (rejected alternatives: 404 for all; `SDK_FAILURE` 500; a new
   `HarnessErrorType`). The union is Root-owned (`runtime/**`, outside the
   write locus); `kind`/`details.kind` is the discriminator; a dedicated
   type is a residual for the Root-routed schema work consumed by V3-02.
3. **Delete refuses unreadable records** (rejected alternative: delete by
   session id regardless). Preserves the existing "open first, then remove"
   contract and keeps every access non-destructive on failure; a UI-driven
   cleanup path for unreadable records is out of scope (S-4).
4. **List scoped materialization** (`materializeOnlyFor`): listing project A
   no longer writes canonical folders for sessions bound to project B
   (the prior code did). Rejected alternative: keep cross-project
   materialization for simplicity.

## Checks

See run record `CHECKS.json` (exact commands, cwd, exit codes). Pass/fail
summary lives in the closeout receipt.
