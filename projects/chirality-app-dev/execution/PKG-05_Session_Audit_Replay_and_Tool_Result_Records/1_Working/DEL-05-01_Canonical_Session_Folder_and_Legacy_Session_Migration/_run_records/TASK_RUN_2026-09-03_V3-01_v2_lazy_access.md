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

1. **Legacy flat file retained after first touch — NOT agent latitude;
   owner-ruled (A13).** At the first freeze this was recorded here as a
   latitude exercise. The independent reviewer (F1, MAJOR) found that the
   accepted Scope of Work carried, verbatim (pre-amendment),
   `DEL-05-01-R010`: "If both canonical folder and legacy flat records exist
   for the same `sessionId`, resolution MUST prefer defined canonical values,
   preserve legacy-only fields, write the merged canonical `session.json`,
   and remove the flat record." and the CLM-012 verification row "... duplicate
   fixture tests proving merge precedence, legacy-only field preservation, and
   flat-file removal." — so the fork was between accepted instruments and
   owner-class. It was presented to the owner and ruled 2026-09-03 as **A13**
   (`plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md`,
   "Ratify retention"): R010 and CLM-012 were superseded and amended in
   `ScopeOfWork.md` (CLM-032) in this tranche; D-APP-41 is historical on this
   point. Cleanup of the retained source remains the unseated S-4 amendment.
   Rejected (owner, not selected): "Reinstate removal"; "Archive instead".
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
5. **A13 F2 — changed legacy source after consumption: "ignore and
   diagnose"** (rejected alternative: "re-merge and update marker"). Once
   the `legacySource` marker is present, a flat file whose sha256 differs is
   reported as a `legacySourceChanged` diagnostic and ignored. Safer because
   the canonical record is the accepted truth after consumption; re-merging
   would let an external edit of a retained source silently alter the live
   record and would resurrect fields a writer removed — exactly the F2
   hazard. `docs/SPEC.md` §8.3 lists `session.json` contents as SHOULD-include
   and tolerates additional fields (the daemon's own `RuntimeSessionRecord`
   carries an analogous `legacy: { sourcePath, migratedAt }` marker and its
   `normalizeLegacy` spreads unknown fields through), so no schema requires a
   re-merge.
6. **A13 F3 — list resilience: re-resolve read-only and diagnose** (rejected
   alternative: swallow the candidate as the basis did). A materialization
   write failure is retried read-only; a readable record is listed
   unmaterialized with a `materializationFailed` diagnostic; an unreadable one
   becomes a typed failure entry; the listing never aborts. `getById`/`resume`
   still surface the environment fault so a following `save` cannot assume
   persistence.

## Review round 1 (2026-09-03)

`execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/instances/D2_REVIEWER/REVIEW_ROUND_1.md`
over commit `3b6b4758bca7cd0e4ac84f9685052a0548c4ca2e`: 0 blocking / 1 major
(F1, owner fork → A13) / 2 minor (F2 marker, F3 list-abort); all three
applied in the second local commit; N2 error-type proposal carried as a
Root-routed residual. Deterministic gates reproduced by the reviewer.

## Checks

See run record `CHECKS.json` (exact commands, cwd, exit codes). Pass/fail
summary lives in the closeout receipt.
