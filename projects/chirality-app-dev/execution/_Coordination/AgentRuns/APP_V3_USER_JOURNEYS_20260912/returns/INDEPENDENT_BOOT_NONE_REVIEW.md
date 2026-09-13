# Independent supplemental Codex boot-readiness review

Verdict: **PASS — no actionable finding in the bounded repair.**

Subject: author-frozen, uncommitted five-file repair on `46232f5f5c4b0e7aee8eb022fa11ebf54b1fb516`, identified by exact SHA-256 below. Read all four tracked diffs, the new helper, and `CODEX_BOOT_READINESS_REPAIR.md` (the actual author-return name). This supplements, and does not rewrite, INDEPENDENT_FINAL_REVIEW.md or its original candidate verdict.

Reviewer: independent TASK / Type 2, gpt-6-astra high, `/root/candidate_independent_review`; same parent-granted bounded review exception. No delegation, product edit, test rerun, build, Git mutation, live UI/API/model action, filtered operational-log read, or protected-state access. Only this supplemental return was written.

## Source assessment

Runtime's delegated Codex descriptor explicitly declares `boot: none`. RuntimeService.bootSession authorizes the project and validates role/selection, then durably records bootedAt and bootFingerprint without requiring engineSessionId. The first actual provider turn supplies that ID. Therefore an attachment rejection before provider startup can leave an already booted session without a provider ID. Requiring that ID to permit the first real turn creates the reported recovery loop.

The new shared isSessionBootConfirmed predicate correctly requires both nonempty Runtime boot stamps. Existing provider-session evidence continues to confirm readiness. The only new no-provider-ID case requires the exact v3 schema and canonical exported CODEX_ENGINE_ADAPTER_ID. A missing stamp, an unknown engine, a non-Codex engine or a legacy Codex record without provider identity does not acquire this exception. Trimming strings also avoids treating whitespace as evidence.

Both relevant consumers now use the same predicate: v3 operator projection when reopening a recorded chat, and pending-bootstrap reconciliation after a lost boot response. The latter retains its session ID, role and project-root comparisons before accepting readiness. The recovery continues the same created session and preserved draft; it introduces neither automatic reboot nor replacement session. Legacy projection behavior remains unchanged. Runtime authorization, source containment, engine selection and turn validation are untouched; this UI readiness decision does not authorize execution by itself.

Inspected controlled tests exercise rejection before the first provider thread, draft/attachment restoration across unmount/reload, same-session retry without a second create/boot, lost boot-response reconciliation, and genuinely incomplete boot stamps remaining held. Projection tests cover absent stamps and non-Codex/unknown adapters. The code's explicit schema check preserves the legacy restriction even though that exact new negative is not separately added to these tests. No additional test is needed to establish the straightforward branch in this bounded review.

## Validation and handoff

Author reports **69 focused tests PASS** across the two changed test files and **App/Electron typecheck PASS**, with all five source files unchanged afterward. These are attributed author results; no suites were duplicated. Parent's earlier 364 Runtime / 2223 frontend pass totals apply to the preceding frozen candidate, not a new full-suite claim for this supplement.

APP-HOLD reliance check: ALLOW, CLEAR/NOT_HELD for DEL-02-01 and DEL-03-01, entry `APP_V3_USER_JOURNEYS_20260912:INDEPENDENT_BOOT_NONE_REVIEW`, at base46232f5f5. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan SHA-256 `543a2272b489b62bda5db44c2fdd06c9f6da5fe8f7a47aedaf80b4b0525b6811`.

Bounded independent source review is complete. Parent owns committing the exact reviewed bytes, direct native recovery/attachment/viewer rechecks and release qualification. Missing Runtime stamps must still leave recovery unconfirmed. The actual historical session's fields and native outcome were not inspected or inferred here. This is derivative engineering evidence, not user acceptance or an authoritative governance snapshot; subsequent material changes require affected-scope review.

## Exact reviewed source bytes

| Repository-relative path | SHA-256 |
| --- | --- |
| `projects/chirality-app-dev/frontend/src/lib/harness/session-boot-readiness.ts` | `3f2f7fbfd0d5e85e02037e7d0b16271d4b88b563b4fdad954174ced7c16c68ac` |
| `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/operator-projection.ts` | `f75bfbc02343054736060e0799921f7da88a21e7881932a6d3a843af75f23c12` |
| `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx` | `afae13b239265f420c962d3a95198719df08b2dc646b143656a4559b2aa76c09` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/operator-projection.test.ts` | `a3267bd42035d69b945b6d51b0f83000e1fc6fab30162cb98bba64914f46f932` |
| `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-folder-binding.test.tsx` | `ea19d868f0536818081a1c8cf340a42c54663fee6e259e49eae6093798938ed9` |

Author return SHA-256: `f4beefbe27716ae967919b2f7387f8d17d270efcabe5011bf0a736ad9af9c5df`.
