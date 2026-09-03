# SCA-APP-008 Closure Addendum — 2026-09-03

This append-only record reconciles the immutable Gate-1 and Gate-5 handoff
bytes with later acts now present on `main`. It does not rewrite those dated
snapshots or confer implementation, lifecycle, release, publication, or
reliance authority.

## Stale historical claims and satisfying acts

| Historical claim | Preserved location | Later satisfying act on `main` |
| --- | --- | --- |
| Gate-1 remains `AWAITING_OWNER_ACCEPTANCE`, with assessment-only scope and no accepted application. | `Brief.md:3,7,65-73` | The owner-authorized Gate-5 content commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f` was merged by PR #662 at merge commit `d5e40b3c25fe527919f1d2d2a31ea97ce2835795`. |
| Gate-1 handoff remains `AWAITING_OWNER_ACCEPTANCE`; `_LATEST.md` is unchanged; owner review is required before later gates. | `Handoff_State.md:3,6,12-15,21-30,43` | The same PR #662 merge records the accepted Gate-5 application, and the later pointer act below records scope-change closure. |
| Gate-5 application is complete only on a candidate branch and still awaits owner merge. | `Phase5/Handoff_State.md:5-6,12,15,94-95,112-120,131-140` | PR #662 merged the exact Gate-5 application at `d5e40b3c25fe527919f1d2d2a31ea97ce2835795`. |
| `_LATEST.md` movement remains withheld and requires a separate owner act. | `Phase5/Handoff_State.md:13,15,81-86,96-97,125-126,139-140` | PR #665 merged the pointer act at `4251530ec8a5d5b7abfc035cbdde63dab7fa80f3`; current `execution/_ScopeChange/_LATEST.md` records `CLOSED_FOR_SCOPE_CHANGE_ONLY`. |
| The Root notice remains unrouted and requires a separate owner act. | `Phase5/Handoff_State.md:13,15,81-90,98-99,126-127,139-140` | PR #668 merged Root ingestion at `eb2ea19db5b86ad33760345d274b828d7a12e6cc`; the routed record is Root `execution/_Coordination/NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md`. |

Git history also establishes that PR #664 (`fde84c94d95160bd71ec4ac084e90803b79ebdc1`)
was the R10/R9 coordination transcription, not the Gate-5 application merge.

## Current pointer and preserved history

`execution/_ScopeChange/_LATEST.md` is the current pointer. Its
`CLOSED_FOR_SCOPE_CHANGE_ONLY` state governs discovery. The SHA-cited Gate-1
`Brief.md`, Gate-1 `Handoff_State.md`, and Gate-5 `Phase5/Handoff_State.md`
bytes are preserved unchanged as dated history.

## Genuinely open state

- The post-application dependency-closure audit remains `WARNINGS`: one
  nine-node SCC remains unresolved without silent linearization, five isolated
  deliverables remain visible, and one bidirectional pair remains
  informational.
- Every downstream gate and blocker named by the current `_LATEST.md` remains
  in force: WP-03/WP-05 fixtures; accepted Root/App account-consent contract
  work; TM-ROOT-106/122; C1; TM-APP-030; D-APP-97/F-APP-2; G1; G6a; all ten
  held DEL-02-06 bindings; and WP-09/WP-11 separation.
- Scope-change closure does not activate carriers or implementation and does
  not change SOW, lifecycle, release, publication, or reliance state.
