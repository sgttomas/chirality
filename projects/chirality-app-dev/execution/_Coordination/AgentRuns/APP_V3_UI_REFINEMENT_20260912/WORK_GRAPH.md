# Work graph — APP_V3_UI_REFINEMENT_20260912

Recorded work graph per App AGENTS.md (multi-agent path). Stages run
concurrently where write scopes are disjoint; fan-in and integration are
owned by the implementing session.

| Node | Owner | Write scope | Items |
|---|---|---|---|
| S0 orientation | session | none (read-only maps) | all |
| A catalog navigation layer | TASK A (Type 2, Fable 5.1 medium) | `workflows/catalog.yaml`, `workflows/catalog.schema.json`, `workflows/index.json`, `tools/validation/build_workflow_index.py`, `tools/validation/test_workflow_catalog.py`, `projects/chirality-runtime/packages/contracts/src/v3.ts`, `projects/chirality-runtime/packages/core/src/method-catalog.ts`, `projects/chirality-runtime/tests/method-catalog.test.ts` (+ fixtures) | 11 (authoritative layer) |
| B update discovery (main/preload) | TASK B (Type 2, Fable 5.1 medium) | `frontend/electron/app-update*.ts` (new), `frontend/electron/main.ts`, `frontend/electron/preload.ts`, `frontend/src/types/chirality-window.d.ts`, `frontend/src/components/shell/app-update-provider.tsx` (new), `frontend/src/__tests__/electron/app-update*.test.ts`, `frontend/src/__tests__/electron/folder-preload.test.ts` if bridge shape is asserted | 8 (feature core) |
| C conversation, menus, account, Plan tab, App catalog UI, About and indicator | session | `frontend/src/components/**` except B's files, `frontend/src/lib/shell/**`, `frontend/src/lib/woven-dialogue/**`, `frontend/src/app/globals.css`, `frontend/src/app/layout.tsx`, `frontend/src/__tests__/components/**`, `frontend/src/__tests__/lib/**` | 1-7, 9, 10, 11 (App side), 12, 8 (renderer UI) |
| R independent review | fresh reviewer (Fable 5.1) | none | all |
| M governance records | session | tranche manifest, notices, run record | 11 |

Contracts fixed before dispatch (so A, B and C proceed in parallel):

1. `MethodDescriptor.navigation?: MethodNavigation` in `@chirality/runtime-contracts/v3`:
   `{ category: 'core' | 'specialist' | 'superseded'; tier: 'primary' | 'supporting'; order: number; displayName?: string; group?: { key: string; label: string }; supersededBy?: string }`.
   Emitted by the Root index generator from `workflows/catalog.yaml` `navigation`; read through by the Runtime catalog; project and user workflows carry no navigation and are categorised by source in the App.
2. `window.chirality.appUpdate` bridge: `get(): Promise<AppUpdateState>`, `check(): Promise<AppUpdateState>`, `openDownload(): Promise<{ ok: boolean; error?: string }>`, `subscribe(listener): () => void`, `onShowAbout(listener): () => void`; `AppUpdateState` as defined in `frontend/electron/app-update-ipc-contract.ts` (status `idle | checking | up-to-date | update-available | failed`, `failure.code` in `no-release-source | policy | network | invalid-feed`).

## Packaged hand-off continuation after PR #775

The original source graph is complete and merged at `85f19f019`. This continuation
has no product-source write target. HELP_HUMAN performs the single build and
checks, prepares the owner notes, and validates the independent return. A fresh
read-only Type 2 reviewer checks the frozen record diff and its supporting build
evidence. Git closeout follows the standing grant. Owner native verification
precedes deletion of the old build checkout; notarization and publishing remain
separate owner acts. The review brief and return are recorded beside the earlier
ones in `briefs/` and `returns/`.

The reviewer uses `gpt-6-astra`, medium, under the owner's prior explicit model
direction for this session. The handoff's Fable models are unavailable here;
this does not change the attribution of the earlier Fable work or reviews.

Owner-added live checks: parent directly exercises stall/hard-loss/reload and panel controls; one bounded Type 2 maps the observed reconnect mismatch read-only in parallel. Parent validates diagnosis against direct observations, then assigns any bounded repair and a fresh independent source review before new source is merged or rebuilt. The install-over comparison remains the owner's packaged check.

The later owner request supersedes the source-free scope above. Two bounded
Astra/medium Type 2 authors completed recovery/cause propagation and the
constrained panel-width correction in distinct files. Parent validated their
returns, integrated the actual App/Runtime path through direct UI checks, and
ran the full suites. A fresh Astra/medium TASK using software-code-review reviews
the complete frozen diff under `briefs/REVIEW_LIVE_RECOVERY.md`. Only then does
Git integration proceed, followed by one replacement package from the merge.
Existing packages remain preserved; the owner performs install-over acceptance.

The first recovery review found an ambiguous-submission identity defect. The
same bounded recovery author repaired the request, attachment and replay path;
the parent validates its return with the full suites and a direct reload check.
A fresh gpt-6-astra/high Type 2 reviews the complete new frozen candidate under
`briefs/REVIEW_LIVE_RECOVERY_FINAL.md`. This bounded escalation uses the owner's
standing exception because the boundary determines truthful completion. A
separate gpt-6-astra/medium packaging child is prepared under
`briefs/REPLACEMENT_PACKAGE.md` and waits for the reviewed merge revision before
any setup or build. No source author serves as independent reviewer.

## Product guidance and release-source continuation

The owner's latest request adds automatic shared/role instruction delivery,
the saved product AGENTS.md direction, updates from the public chirality-app
release repository, and the `Turn into workflow` label. The package remains
held to include these changes once. A fresh Astra/medium TASK audits the
instruction path read-only under `briefs/PRODUCT_INSTRUCTION_AUDIT.md` while
HELP_HUMAN studies the product draft and release-source integration. Bounded
authors follow the settled path, with disjoint writes, then a fresh independent
review covers the complete new candidate. The prior recovery source review
and live evidence remain valid for that unchanged source.

A separate Astra/medium TASK owns the bounded release-checker and button-label
files under `briefs/PUBLIC_RELEASE_UPDATES.md`. It does not edit Electron main,
instruction delivery, product text or governing records, leaving those writes
available to the parent and instruction author after the audit returns.

The instruction audit found native role wiring absent and hot resume overrides
ignored by Codex 0.154.0. A bounded Astra/medium Runtime author implements the
explicit product source, per-thread named role configuration and verified idle
refresh under `briefs/PRODUCT_INSTRUCTION_RUNTIME.md`. HELP_HUMAN owns the
product text, App-owned editable file/settings, packaging and governing
alignment. Source qualification and native child/edit checks precede the fresh
independent review and consolidated package.

Native instruction editing exposed the stock idle-cache delay; the existing
Runtime author corrected that bounded integration and retained the failed
observation. The parent records specialist fan-in in
`PRODUCT_GUIDANCE_AND_UPDATES.md`. Fresh independent Astra/high review follows
`briefs/REVIEW_PRODUCT_GUIDANCE.md`, under the standing exception for this
consequential instruction-delivery boundary. The packaging child still waits.
