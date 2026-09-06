# Independent design review — FINDING R1 OPEN

Reviewed the frozen candidate packet only. One substantive design correction is required before this candidate can receive a clean design-review PASS. This is not a lifecycle review or acceptance, implementation permission, supplier acceptance, or hold release.

## R1 — P2: resolution while waiting for child attribution

APPROVAL/REPORT.md:50 defines a bounded pre-association join and replay tombstones, but never defines how `serverRequest/resolved` invalidates a request still in that buffer. F02 covers request-before-association, while F12 begins with `establish-pending`; neither combines those states. Current `codex-session.ts:277–292` quarantines a resolution that has no recognized approval or tool entry. Retaining that path when adding a separate join buffer could allow a resolved callback to become an actionable prompt after late association. This is an omitted transition/oracle, not an observed supplier failure.

Require exact typed ID/thread/generation resolution correlation across queued and actionable states in the same serialized actor, with no queued promotion after matching resolution. Specify bounded tombstone/unknown-resolution handling, mismatch and cross-capability collision behavior, and resolution racing final publication/send reservation. Add traces for resolution during buffering and before request, typed-ID and thread/generation mismatches, and resolution versus send. Expected outcomes: no stale prompt or send when resolution wins; no fabricated human decision, grant, or supplier application; bytes already enqueued retain truthful delivery uncertainty. Correction must be a new versioned artifact because this packet is frozen, followed by independent backcheck.

## Checks that passed

- Sealed brief and frozen manifest match the supplied hashes; all 30 packet files match hashes and sizes. All 122 author input entries match present source bytes (duplicates included).
- All 58 coverage rows match their cited SOW matrix line, output, requirement/claim references and acceptance reference exactly: 43 unique outputs across seven deliverables. Per-carrier implementation, verification and evidence acceptance are separated. The map preserves all 16 OD6 identities, 18 residual limbs, nine holds and separate R16-B; it does not create dependency truth.
- Durable origin is separated from current authority and authenticated responder. Receive/display/respond/retire checks, post-persistence recheck, generation serialization, child and parent invalidation, no replay and settlement failure are explicit. Missing decline is not invented; cancel and whole-generation stop are not deny. Sent and supplier-applied remain separate.
- Closed v2 and four terminals remain unchanged by implication; negotiated child representation, SOCKS disposition, principal binding, historical audit access and session/grouping evidence remain owner choices. Fixture request digest recomputes exactly; all 33 fixture IDs are unique. Fixtures are specifications, not execution evidence.
- Root instruction authority, Runtime execution/consent, App presentation and domain acceptance are correctly separated. App-wide sign-in does not confer per-root readiness/consent. No-folder remains blocked pending an explicit context contract. D-APP-117 managed replay does not grant native-child approval authority.
- Accepted original, Candidate2 and Candidate3 identities and evidence limitations remain distinct. Protected proof remains unresolved and screening is not retried. Historical migration labels are read through later effective acceptance; merged/tested code does not fill held accepted source identity.
- The pre-freeze correction is accurate: the retained independent diagnosis supports possible child-before-association ordering from source, while actual Candidate2 evidence establishes FOREIGN_PRIMARY_TURN and zero approvals. It explicitly says lifecycle order was not retained. This review did not independently measure supplier ordering.

## Post-freeze App observation

COORDINATION_ADDENDUM.json is reviewed separately and does not alter the frozen manifest. The parent relays App's observation that selecting generic Electron coincided with isolated daemon exit, with connectivity restored after restart. Correlation does not establish cause, and no production fix is proved. The existing map correctly leaves production launcher/lifecycle qualification open.

App owns DEL09-04 helper/GUI packaging identity and consumer diagnosis. Runtime owns DEL-02-07 OUT-003/AC-003 acquisition/reconnect/generation fencing and OUT-004/AC-004 production two-job launch/broker ownership, plus DEL-02-11 OUT-003/AC-003 exactly-once terminalization and OUT-005/AC-005 crash/no-replay evidence. DEL-02-12 OUT-001/AC-001 and OUT-006/AC-006, then DEL-02-06 affected-client/release fan-in, require separately accepted consumer and Runtime results. App lead should name the boundary repair owner after diagnosis and exact scoped owner decisions. Reported headless 8/8 remains bounded evidence; GUI/production launch identity reliance remains unresolved. No implementation is authorized here.

## Handoff and limitations

Accepted upstream subject remains Gate3 V3 `547d1f3369e71aa96d1b61561f6b1603b978016c7335fca39f86df97ddd73fc3` with effective migration indexed by MIGRATION_ACCEPTANCE_2026-09-06.md. This review is a derivative snapshot of candidate design; product closure remains OPEN. R1 must be corrected and independently backchecked, then App consumer review and the consolidated owner slate remain next. Other declared owner choices and supplier/production evidence blockers remain unresolved. Rerun review after changed source, contract, supplier or candidate pins.

Only read-only file inspection and hash/consistency checks ran; no builds/tests/provider/supplier execution, network, credential access, protected-fixture retry, source edits, publication or acceptance occurred. One initial source read used the repository root rather than the Runtime project root and returned missing paths; the corrected reads succeeded. Semantic review covered the reports, fixtures and relevant cited source sections; input hash verification alone is not full semantic review of every historical source. Parent-relayed App findings were not independently reproduced.

Reviewer `/root/runtime_v3_design_review`, parent `/root` HELP_HUMAN; ephemeral Agent 2, no delegation, role instruction-asserted. OpenAI GPT-6; exact serving ID unavailable. Exact reviewed and verified identities are recorded in REVIEW_EVIDENCE.json.
