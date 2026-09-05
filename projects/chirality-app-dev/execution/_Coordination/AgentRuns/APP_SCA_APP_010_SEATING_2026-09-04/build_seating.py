#!/usr/bin/env python3
"""Deterministic SCA-APP-010 seating and alignment builder (D-APP-108).

Run: APP_SCA_APP_010_SEATING_2026-09-04
Owner ruling: D-APP-108 (2026-09-04) — "adopt the list as presented", items
outside the thirteen carriers seated in the same pass, WORKING_ITEMS alignment
authorized in the same PR, eleven shell-redesign questions ruled.

Modes
  --freeze   record SHA-256 pre-images of every file this builder may write
             into Evidence/pre_images.json (no other write)
  --apply    assert the frozen pre-images, apply every transaction fail-closed,
             write Evidence/post_images.json and Evidence/seeded_items.json
  --check    assert the live files equal Evidence/post_images.json

Every transaction keys on text that must occur exactly once; any miss aborts
before any file is written. Nothing here changes lifecycle state, a Checking
Approval SHA, a dependency register, product source, the decomposition, the
companion register, the pointer, or any Root surface.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import textwrap
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent
EVID = RUN_DIR / "Evidence"
REPO_ROOT = RUN_DIR.parents[5]
APP = REPO_ROOT / "projects" / "chirality-app-dev"
EXEC = APP / "execution"
DECOMP_REL = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
DECOMP = REPO_ROOT / DECOMP_REL
SNAPSHOT_REL = "execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA"
SNAPSHOT = APP / SNAPSHOT_REL
FUTURE_WRITE_SET = SNAPSHOT / "FUTURE_WRITE_SET.csv"

DATE = "2026-09-04"
RULING = "D-APP-108"
RULING_REL = "execution/_Coordination/_DECISIONS/D-APP-108_RULING_SCA_APP_010_SEATING_AND_SHELL_QUESTIONS_2026-09-04.md"
RUN_ID = "APP_SCA_APP_010_SEATING_2026-09-04"
RUN_REL = f"execution/_Coordination/AgentRuns/{RUN_ID}/"
PIN_COMMIT = "dbd812a52d5ed0cb3ed173f3aaaa68703a914291"
APPLY_MERGE = "7795b0972cac147869607d994173753e4a2fc232"
POINTER_MERGE = "311a2f0b811d55315d6eb623130cad0be1417565"
DECOMP_SHA = "c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61"
COMPANION_SHA = "63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca"
POINTER_SHA = "b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0"
PLAN_HASH = "e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb"
SPEC_HASH = "d1643e3cf8156b7084b370aa8624bd5e87a75bfb4c0cd7b3a2552a4cbef82b45"
DEC_HASH = "8cc5bc8cb2eb0688ca3db69ed24e00bee9c460aefa1d7165cb1a129688a04ed1"
BRAND_HASH = "84b466fde1fea8418f41778a51ecadfde496322edeac14f6ec2aa508dc509d2b"
ROOT_NOTICE_REL = "execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md"

THIRTEEN = [
    "DEL-02-01", "DEL-02-02", "DEL-02-04", "DEL-02-05", "DEL-03-02", "DEL-04-04",
    "DEL-05-02", "DEL-06-03", "DEL-07-01", "DEL-07-03", "DEL-08-01", "DEL-08-03",
    "DEL-08-04",
]
OUTSIDE = ["DEL-02-03", "DEL-05-04", "DEL-09-04", "DEL-01-03"]
CARRIERS = THIRTEEN + OUTSIDE
PKG02 = {"DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-02-04", "DEL-02-05"}

# Decomposition anchors (line numbers in the applied post-image, verified at apply).
ROW_LINE = {
    "DEL-01-03": 300, "DEL-02-01": 307, "DEL-02-02": 308, "DEL-02-03": 309,
    "DEL-02-04": 310, "DEL-02-05": 311, "DEL-03-02": 318, "DEL-04-04": 329,
    "DEL-05-02": 337, "DEL-05-04": 339, "DEL-06-03": 348, "DEL-07-01": 357,
    "DEL-07-03": 359, "DEL-08-01": 368, "DEL-08-03": 370, "DEL-08-04": 371,
    "DEL-09-04": 381,
}
ANCHOR_LINE = {
    "SOW-001": 171, "SOW-002": 172, "SOW-004": 174, "SOW-006": 176, "SOW-007": 177,
    "SOW-008": 178, "SOW-010": 180, "SOW-081": 251, "SOW-082": 252, "SOW-083": 253,
    "SOW-084": 254, "PKG-02": 280, "OI-008": 602, "DEC-025": 634,
}

# ---------------------------------------------------------------- boilerplate
FRONTEND_CHECKS = (
    "registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` "
    "build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, "
    "`git diff --check`, repo-wide harness self-check and pytest, and the "
    "independent-review path (fresh read-only `TASK + software-code-review` PASS over "
    "100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration "
    "because `frontend/` is touched"
)
EVIDENCE_TAIL = (
    "durable non-secret bytes sufficient for independent recomputation per the "
    "`loop/LOOP_INIT.md` §7 Evidence contract: exact input/source identities and "
    "cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, "
    "effective environment, tool/runtime versions, and exit status; canonical "
    "stdout/stderr and machine-readable results; sorted manifests with recomputable "
    "hashes; cleanup proof for disposable state; and a bounded rerun method"
)
BASIS = (
    "Design basis `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` "
    f"(SHA-256 `{PLAN_HASH}`), cited only for what the tranche means when complete, "
    "never as a queue; status from current `main`"
)
SPEC = f"`03_TARGET_SPEC.md` (SHA-256 `{SPEC_HASH}`)"
ELECTRON_NOTE = (
    "additive `frontend/electron/**` changes stay under D-APP-98 Electron authority and "
    "the existing IPC sender policy"
)


def item(iid: str, gate: str, scope: str, **f: str) -> str:
    lines = [f"- **{iid}** (`{gate}`) — {scope}"]
    for key in ("Trace", "Plan", "Depends", "Write locus", "Checks", "Return", "Removed when"):
        lines.append(f"  {key}: {f[key.replace(' ', '_')]}")
    return "\n".join(lines)


# ---------------------------------------------------------------- items
ITEMS: dict[str, list[tuple[str, str, str]]] = {}  # carrier -> [(id, gate, text)]


def add(carrier: str, iid: str, gate: str, scope: str, **f: str) -> None:
    ITEMS.setdefault(carrier, []).append((iid, gate, item(iid, gate, scope, **f)))


add(
    "DEL-02-02", "DEL-02-02-V3-03", "SELECTABLE",
    "retire Workbench and Pipeline from the woven route and make the primary dialogue invariant (T1).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L308 (Workbench and Pipeline retired from the active shell with code, routes, and tests retained; the Work projection unmounted until an explicitly recorded plan/task source exists); SOW-001 L171 (the centre dialogue is never hidden, unmounted, or replaced; retired routes reachable but unmounted); SOW-007 L177 (presentation half retired by owner ruling, DEL-08-03 remains semantic owner); DEC-025 L634.",
    Plan=f"T1; SR-01, SR-06, SR-08; Q3 ruled {RULING} (the retired `/workbench` and `/pipeline` routes stay reachable by URL and unlisted; no 404). {BASIS}.",
    Depends="none (first tranche); DEL-08-03 dispatch semantics are consumed by nothing in the active shell and are not touched; no Root dependency.",
    Write_locus="`frontend/src/components/woven-dialogue/**` (route, shell, viewport, navigator, replay-lens mount; `work-projection.tsx` unmount with its empty-source disclosure test retained), `frontend/src/__tests__/components/woven-dialogue-*.test.tsx`, D-APP-36 render fixtures; `frontend/src/app/workbench/**` and `frontend/src/app/pipeline/**` untouched (retained routes); deliverable-local `_STATUS.md`/`MEMORY.md`/`_run_records/**`. No harness, IPC, or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the woven route renders with no focused-surface mode and no Workbench or Pipeline mount; a test proves the primary dialogue is never hidden, unmounted, or replaced under replay selection, panel resize, and expand; replay opens beside a visible primary; the Work projection is unmounted; `/workbench` and `/pipeline` remain reachable by URL with their existing tests green and no navigation entry; D-APP-36 render evidence and browser evidence; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS and browser evidence recorded; the Workflows view and proposal card are DEL-02-02-V3-04.",
)
add(
    "DEL-02-02", "DEL-02-02-V3-04", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed",
    "Workflows view, roadmap, New workflow form, library and bind, the derived rung with its two forms, the proposal card, and the workflow file read/write route (T3 part).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L308 (Workflows view, roadmap, New workflow form, library, and bind actions over governed workflow files; the transcript proposal card rendered from `proposal.*` events); SOW-081 L251; SOW-082 L252 (card actions are human acts applied by the app; one proposal per chat per trigger); OI-008 L602.",
    Plan=f"T3 part; SR-23, SR-24, SR-26; Q10 to Q14 ruled 2026-09-04 (SR-24; G2-CONFIRM); Q15 ruled {RULING} (a read-only currency line in the Workflows view comparing the file's `roadmapSource` hash against the current protocol or template); Q16 ruled {RULING} (position advances only at human gates, the file records who advanced it, concurrent editing documented as unsupported until the thesis §9.4.6 work). {SPEC} §4.3 and §5.10 for meaning. {BASIS}.",
    Depends="DEL-07-03-V3-01 (the front matter, roadmap grammar, gate markers, and bind copy semantics this view reads and writes); DEL-02-03-V3-01 (the right-panel view switcher hosts the Workflows view, which cannot mount before it); DEL-02-04-V3-01 (chat rung and declined-trigger convenience fields); the card's live `proposal.*` path is DEL-05-02-V3-02 after Root DEL-02-10 acceptance, so this item ships the card over fixtures for the four candidate event types and makes no live-event claim.",
    Write_locus="`frontend/src/components/woven-dialogue/**` (Workflows view, roadmap, New workflow and bind forms, rung forms, proposal card), a new K-PATH-2-contained read/write route under `frontend/src/app/api/working-root/workflow/**` limited to `.chirality/workflows/`, consumers of the DEL-02-04-owned additive state, fixtures and tests; deliverable-local state. No harness, MCP, instruction-root, or Root write.",
    Checks=f"{FRONTEND_CHECKS}; workflow-file writes prove K-PATH-2 containment and refuse a file with role, folder, or delegation policy unset.",
    Return=f"Workflows view lists, opens, follows, pauses, creates, and binds from the library with provenance (`roadmapSource` and hash) and the Q15 currency line; New workflow refuses role, folder, or delegation policy unset; position advances only at human-gate markers and records who advanced it (Q16); the proposal card renders Accept, Adjust, and Not now as human acts over the four fixture event types with once-per-chat-per-trigger enforcement visible; nothing is promoted silently; the file steers and never records status, approvals, or evidence; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS; live `proposal.*` consumption remains DEL-05-02-V3-02.",
)
add(
    "DEL-02-01", "DEL-02-01-V3-01", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed",
    "header removal, Stone tokens, composer context line with folder select, and the plain-language copy pass (T2).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L307 (header-less three-panel frame; composer context line with folder, agent, permissions, delegation, and rung; per-chat folder selection over the known-folder set); SOW-001 L171; SOW-002 L172 (folder chosen in the composer before the first message and fixed thereafter; a chat may have no folder; DEL-07-01 retains validation); SOW-005.",
    Plan=f"T2; SR-10 to SR-15, SR-18, SR-21; Q9 ruled {RULING} (full Mac-native set: native folder picker; known folders registered as macOS recent documents so they appear in the Dock and Open Recent menus; Reveal in Finder on each chat; a folder dropped from Finder onto the composer). {SPEC} §10 copy table for meaning. {BASIS}.",
    Depends=f"DEL-02-02-V3-03 (the woven route this item re-frames); DEL-07-01 folder validation consumed, not changed; DEL-02-04-V3-01 known-folder convenience fields; {ELECTRON_NOTE}.",
    Write_locus="`frontend/src/components/shell/shell-frame.tsx`, `chat-panel.tsx`, `persona-picker.tsx`, a new `folder-select.tsx`, `frontend/src/components/woven-dialogue/navigator.tsx`, `frontend/src/app/globals.css` (Stone token block with measured contrast), additive recent-documents registration and folder-drop IPC in `frontend/electron/main.ts` and `preload.ts` under the existing sender policy, tests; deliverable-local state. No harness, daemon, or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"no header in the woven route; wordmark in the left panel; the composer context line shows folder, agent, permissions, delegation, and rung from recorded state; folder select is live before the first message and a fixed label after, over the known-folder set with the native picker; known folders appear in the Dock and Open Recent menus; Reveal in Finder on each chat; a folder dropped from Finder sets the composer folder subject to DEL-07-01 validation; Stone token block with recorded contrast ratios; plain-language copy per the §10 table with the professional-boundary copy (DEL-01-03) unchanged; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS and browser evidence recorded.",
)
add(
    "DEL-02-01", "DEL-02-01-V3-02", "NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed",
    "left-panel chat organisation: search, titles, pins, groups, archive, and the context menu (T6 part).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L307 (left-panel chat navigator with local organisation); SOW-008 L178 (chat annotations as local convenience state owned by DEL-02-04).",
    Plan=f"T6 part; SR-03; Q1 ruled {RULING} (deleting a chat is a local hide only; the runtime session record is untouched and recoverable); Q6 ruled {RULING} (titles derived from the first message pass the existing redaction helper and stay editable). {BASIS}.",
    Depends="DEL-02-01-V3-01; DEL-02-04-V3-01 (additive annotation fields: titles, pins, groups, archive); the redaction helper under `frontend/src/lib/harness/**` consumed, not changed.",
    Write_locus="`frontend/src/components/woven-dialogue/navigator.tsx` and left-panel components under `frontend/src/components/shell/**`, tests; workspace-state schema changes belong to DEL-02-04; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"search, derived and editable titles with redaction proven on path-like and secret-shaped fixtures, pins, groups, archive, and a context menu; delete hides locally while a test proves the session record remains present and recoverable; no session-record mutation; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-02-01", "DEL-02-01-V3-03", "NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed",
    "folder per chat: `knownRoots`, multi-root session listing, the folder line in the chat list, and the provider root derived from the active session (T6 part).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L307 (per-chat folder selection over the known-folder set); SOW-002 L172; SOW-005; SOW-010 L180 (registered project identity/root bound in the boot request).",
    Plan=f"T6 part; SR-20, SR-21. {BASIS}.",
    Depends="DEL-02-01-V3-01 (folder select); DEL-02-04-V3-01 (`knownRoots` convenience field); DEL-07-01 validation; the provider root is derived from the active session's registered project identity with no new stored daemon field (the session-record fields are Root-owned).",
    Write_locus="session-list and chat-list components under `frontend/src/components/shell/**` and `woven-dialogue/**`, multi-root read paths in `frontend/src/lib/runtime-client/**` and `frontend/src/lib/woven-dialogue/**`, tests; deliverable-local state. No daemon or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the session list spans every known root with a folder line per chat; the provider root follows the active session; a chat with no folder is presented truthfully; invalid or instruction-root-contained paths are refused by DEL-07-01's validation with the refusal visible; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-02-01", "DEL-02-01-V3-04", "NOT_SELECTABLE_UNTIL: DEL-02-05-V3-05 landed",
    "app icon replacement (T7 renderer part); the pop-out panel window is deferred by Q5 and is not seated.",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L307; SOW-001 L171.",
    Plan=f"T7 renderer part; SR-05, SR-16; Q5 ruled {RULING} (defer the pop-out window; ship the icon). `05_LOGO_AND_BRAND.md` (SHA-256 `{BRAND_HASH}`) for the asset meaning. {BASIS}.",
    Depends="DEL-02-05-V3-05 (last T6 item); the `.icns` regeneration and packaging-integrity record are DEL-09-04-V3-02.",
    Write_locus="`frontend/src/app/icon.svg` (replacement; the Next `metadata.icons` file convention is retained per this deliverable's record-only note) or a new `icon.png` under the same convention, `frontend/public/chirality-app-icon.svg`, `frontend/build/icon-macos.svg` source, tests; deliverable-local state. No Electron window work.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the new icon renders through the Next metadata path and the public asset; the reproducibility record (source SVG hash to raster) is handed to DEL-09-04-V3-02; no window work; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS; a pop-out window would need a new owner ruling and its own item (Q5).",
)
add(
    "DEL-02-04", "DEL-02-04-V3-01", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed",
    "activity strip and Activity view; retire the resizable shelf; additive v1 workspace-state fields (T5).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L310 (per-view right-panel widths, expand state, chat annotations, known folders, chat rung and declined proposal triggers as additive v1 fields; the one-line activity strip in place of the resizable shelf); SOW-004 L174; SOW-008 L178.",
    Plan=f"T5; SR-07 (strip), SR-02 and SR-05 (per-view widths, expand), SR-03 and SR-24 (additive fields). {BASIS}.",
    Depends="DEL-02-02-V3-03; the Activity view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it, while the strip and the additive fields can; DEL-02-01-V3-02, DEL-02-01-V3-03, DEL-02-02-V3-04, and DEL-02-03-V3-01 consume the additive fields.",
    Write_locus="`frontend/src/lib/woven-dialogue/woven-workspace-state.ts` (additive v1 fields under the existing schema string with rollback-safe migration), `frontend/src/components/woven-dialogue/activity-shelf.tsx` retirement and the strip and Activity view components, migration guards and tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"a one-line activity strip in place of the resizable shelf; the Activity view in the right panel; additive fields (per-view widths, expand state, chat annotations, known folders, chat rung, declined proposal triggers) with migration tests proving prior state is preserved for rollback; convenience state never transfers session authority and never stands in for the workflow file; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-02-05", "DEL-02-05-V3-05", "NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed",
    "account row, account popover, and Settings view with the app-wide account and per-folder groups on the fake consent port (T6 part).",
    Trace="OUT-002, AC-002, VER-002; applied decomposition row L311 (explicit App account/consent UX carrier; one app-wide account; per-folder consent over the root-private `CODEX_HOME`; account row and popover; Settings view account and folder groups); OI-008 L602 (root-private login home is Root DEL-02-09's).",
    Plan=f"T6 part; SR-17, SR-19; Q7 ruled {RULING} (the account row shows only the local model server status; no OpenAI status dot and no API status dot, now or after DEL-02-05-V3-03); Q8 ruled {RULING} (the shared-login amendment is raised to Root now through the routed SCA-APP-010 notice `{ROOT_NOTICE_REL}`, so this item ships no notice). {BASIS}.",
    Depends="DEL-02-01-V3-01 (account row host); the Settings view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it, while the account row and popover can; the fake `HostedEngineConsentPort` until DEL-02-05-V3-03; Root DEL-02-09 for any live claim.",
    Write_locus="account row and popover under `frontend/src/components/shell/**`, the Settings view and its account and folder groups, the fake consent-port adapter unchanged in port behaviour, tests; deliverable-local state. No live-account, key, or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"account row with one app-wide account and the local model server status only, with a test proving no OpenAI or API status indicator is rendered; popover; Settings view hosting the split app-wide and per-folder consent groups plus the runtime, key, and appearance panels with port behaviour unchanged; fake-port evidence labelled as such; no live-account claim; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS; live flows remain DEL-02-05-V3-03.",
)
add(
    "DEL-03-02", "DEL-03-02-V3-01", "NOT_SELECTABLE_UNTIL: DEL-08-04-V3-02 selected",
    "boot-request binding carries the per-chat delegation policy (SOW-083).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L318 (bind project/persona/mode/delegation-policy/options requests); SOW-010 L180; SOW-083 L253 (`none` default; ask before each brief; approve each brief's writes; bounded briefs; no new delegation class); OI-008 L602 (the stored session-record field is Root DEL-02-11's).",
    Plan=f"T3 and T6 harness part; SR-24. {BASIS}.",
    Depends="DEL-08-04-V3-02 (the bridge that honours the bound policy; selected together); the persisted daemon field is Root DEL-02-11's (routed notice), so the App binds the policy in the boot request and carries it in App-side session state until Root accepts.",
    Write_locus="`frontend/src/app/api/harness/**` boot and session routes, `frontend/src/lib/harness/session-manager.ts` (binding only), boot-fingerprint and conformance tests; deliverable-local state. No daemon or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the boot request carries the delegation policy with `none` as the default and the boot fingerprint reflects it; conformance tests for each of the four values; no new delegation class; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS; the persisted daemon field remains Root DEL-02-11.",
)
add(
    "DEL-04-04", "DEL-04-04-V3-01", "NOT_SELECTABLE_UNTIL: DEL-07-03-V3-01 landed; DEL-07-01-V3-01 selected",
    "delimited roadmap-injection seam and layered-root composition (SOW-081, SOW-084).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L329 (composed from the bundled base and the client-owned organisation layer; a clearly delimited roadmap-injection block for a followed governed workflow); SOW-081 L251 (steers by delimited context injection, cites accepted truth, never records); SOW-084 L254.",
    Plan=f"T3 part; SR-23, SR-25; Q14 ruled 2026-09-04 (G2-CONFIRM). {BASIS}.",
    Depends="DEL-07-03-V3-01 (the file contract the seam reads); DEL-07-01-V3-01 (organisation-layer protection and pins the composer trusts); persona content hash and boot fingerprint updates.",
    Write_locus="`frontend/src/lib/harness/persona-manager.ts` (the composer; the row's `persona-composer.ts` label names this file), `frontend/src/lib/harness/instruction-root.ts` layered read, delimiting and hash tests, boot fingerprint tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the prompt is composed from the bundled base plus the client-owned organisation layer with the layer's pin verified; a followed workflow's roadmap is injected inside a clearly delimited block carrying source path and hash from a K-PATH-2-contained file; the boot fingerprint reflects the layer pin and roadmap hash; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-05-02", "DEL-05-02-V3-02", "NOT_SELECTABLE_UNTIL: Root acceptance of the additive proposal.* event types against HarnessEvent schema v2 routed to App (Root DEL-02-10)",
    "consume the `proposal.*` event types for replay and the proposal card (SOW-082).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L337 (consume the additive `proposal.*` event types for replay and the proposal card once Root accepts them); SOW-082 L252; OI-008 L602; K-EVENT-3.",
    Plan=f"T3 part; SR-24; Q13 ruled 2026-09-04 (proposals are additive harness event types in the session record); the routed notice `{ROOT_NOTICE_REL}` carries the four candidate types to Root. {BASIS}.",
    Depends="Root DEL-02-10 acceptance routed back (a `NOTICE_*` under `execution/_Coordination/`); DEL-05-02-V3-01 (schema v2 consumption); DEL-02-02-V3-04 (the card, fixture path first).",
    Write_locus="`frontend/src/lib/harness/session-events.ts` and `event-factory.ts` consumers, replay fixtures, tests; deliverable-local state. No schema or writer ownership.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"replay and the card consume `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and `proposal.declined` bound to the accepted schema identity with malformed-tail tolerance preserved; {EVIDENCE_TAIL}.",
    Removed_when="the accepted-type consumption lands citing the accepted identity.",
)
add(
    "DEL-06-03", "DEL-06-03-V3-01", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected",
    "the `propose` tool: schema, roster and policy validation, plan-reference resolution, once-per-chat enforcement, and `proposal.offered` emission.",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L348 (in-process deterministic `propose` specification-ladder tool; DEL-06-02 retains catalog validation and collision prevention); SOW-082 L252.",
    Plan=f"T3 part; SR-24, SR-26; Q11 and Q12 ruled 2026-09-04 (the specification tuple is folder, agent, delegation policy, roadmap, and permission mode); Q13 ruled 2026-09-04 (`proposal.offered` is an additive harness event type). {BASIS}.",
    Depends="DEL-02-02-V3-04 (card and rung forms that consume `proposal.offered`); DEL-08-01-V3-01 (clauses naming the triggers); DEL-06-02 catalog validation; roster and policy values read from the instruction root.",
    Write_locus="`frontend/src/lib/harness/mcp/**` (`mcp__chirality__propose` definition, schema, validation, once-per-chat state), wrapper metadata, in-process extension-boundary notes, tests; deliverable-local state. No remote MCP, plugin, provider, or network change.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"a deterministic in-process tool that validates the five-item tuple against roster and policy values, resolves plan references from Agent 1 procedures, refuses a trigger already declined in the chat, and emits only `proposal.offered`; F-APP-1 untouched; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-07-01", "DEL-07-01-V3-01", "SELECTABLE",
    "organisation-layer protection: hash pinning, write protection, and separation from the working root (SOW-084).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L357 (instruction-root write protection for both the bundled base and the client-owned, hash-pinned organisation layer); SOW-084 L254 (K-ROOT-1 applies to both layers; read-only during ordinary project execution; hash-pinned; packaging-checked; never a working root and never a proposal path); DEC-025 L634.",
    Plan=f"T3 prerequisite; SR-25; Q14 ruled 2026-09-04 (G2-CONFIRM). {BASIS}.",
    Depends="none for the policy helpers and fixtures; DEL-08-01-V3-01 owns the packaging checks; DEL-04-04-V3-01 consumes the pins.",
    Write_locus="`frontend/src/lib/harness/instruction-root.ts` and path-policy helpers, organisation-layer pin and protection fixtures, tests; `frontend/electron/daemon-instruction-root.ts` only if protection must be enforced at the daemon boundary (additive; D-APP-98); deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the organisation-layer path is validated as separate from the working root and refused as a working root or a proposal path; a pin file with a SHA-256 per asset is verified at boot; write protection is proven with fixtures for both layers; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-07-03", "DEL-07-03-V3-01", "SELECTABLE",
    "governed workflow file contract: front matter, roadmap grammar with gate markers, the steer-never-record rule, and bind copy semantics.",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L359 (front matter, roadmap grammar with gate markers, app-maintained position, library/bind copy semantics; the file steers and never records); SOW-081 L251.",
    Plan=f"T3 prerequisite; SR-23; {SPEC} §5.10; Q10 ruled 2026-09-04 (`.chirality/workflows/<slug>.md` under the chat's folder, a library, and Bind to this folder); Q16 ruled {RULING} (position advances only at human gates and the file records who advanced it). {BASIS}.",
    Depends="none.",
    Write_locus="`frontend/src/lib/workspace/**` (workflow file contract and validator beside the deliverable metadata scanners in `filesystem.ts`), fixtures, tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"a contract for front matter (agent role, folder, permission mode, delegation policy, where briefs run, `roadmapSource` and hash, app-maintained position with who-advanced attribution), a roadmap grammar with human-gate markers, bind copy semantics that retain `roadmapSource`, and a validator that refuses status, approval, or evidence fields; fixtures for each; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-08-01", "DEL-08-01-V3-01", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected",
    "proposal clauses in HELP_HUMAN and each Agent 1 package, skill-declared workflow templates, organisation-layer packaging checks; the routed agent-index notice and the G4 manifest.",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L368 (proposal clauses and named triggers in Agent 0 and Agent 1 packages; skill-declared workflow templates; organisation-layer packaging and pins; instruction-file changes under `agents/` or `skills/` ship the routed agent-index change notice); SOW-082 L252; SOW-084 L254.",
    Plan=f"T3 part; SR-19 discussion, SR-24, SR-25; Q14 ruled 2026-09-04 (G2-CONFIRM: the organisation layer the packaging checks verify). {BASIS}.",
    Depends="DEL-02-02-V3-04; DEL-06-03-V3-01 (the tool the clauses invoke); DEL-07-01-V3-01 (the layer protections the checks verify); an owner write-scope grant for `agents/**` and `skills/**` at selection (the 2026-09-04 session grant does not carry forward).",
    Write_locus="`agents/AGENT_HELP_HUMAN.md` and each Agent 1 package (rung-2 and rung-3 proposal clauses with named triggers and once-per-chat), `skills/*/SKILL.md` declared workflow templates, the App agent-conformance validator and integrity fixtures (`frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`, the `verify-instruction-root-integrity` script), organisation-layer packaging checks, the routed agent-index change notice under `execution/_Coordination/`, and the G4 instruction-tranche manifest; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}; G4 `validate_instruction_tranche_manifest.py`, `validate_skill_metadata.py`, and the AGENTS.md agent-index change-notice rule.",
    Return=f"a conformance validator proving each Agent 0 and Agent 1 package carries its proposal clause with named triggers and once-per-chat; skill-declared templates discoverable; organisation-layer pins and packaging checked; the routed notice and manifest; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS and the notice routed.",
)
add(
    "DEL-08-04", "DEL-08-04-V3-02", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected",
    "per-session delegation policy honoured by the managed delegation bridge, `none` by default (SOW-083).",
    Trace="OUT-001, OUT-002, AC-001, AC-002, VER-001, VER-002; applied decomposition row L371 (honour the per-chat delegation policy carried with the session as a narrowing input to managed delegation); SOW-083 L253 (only narrows what SCA-APP-008's carrier text allows; adds no delegation class).",
    Plan=f"T3 and T6 harness part; SR-24. {BASIS}.",
    Depends="DEL-03-02-V3-01 (the binding; selected together); DEL-08-04-V3-01 where the class-aware paths exist, otherwise the current managed bridge; the `managed-delegation.ts` sibling-overlap fail-close remains a required invariant.",
    Write_locus="`frontend/src/lib/harness/managed-delegation.ts` and `subagent-governance.ts` (policy check before admission), fixtures, tests; deliverable-local state. No daemon or Root write.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the bridge applies the session policy: `none` refuses `delegate_agent`; ask-per-brief routes an approval; approve-brief-writes requires write approval; bounded-briefs admits only sealed briefs within declared tools; `none` is proven as the default; no new class; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-02-03", "DEL-02-03-V3-01", "NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed",
    "right-panel view switcher, clickable file tree, in-app document viewer with drag and expand, and the bounded file read endpoint (T3).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L309 (working-root selector integration, bounded file tree display, deliverable summaries, scan-state feedback; unchanged by SCA-APP-010); SOW-002 L172 (DEL-02-03 provides the UI touchpoint); SOW-001 L171 (one-view-at-a-time right panel with files and document views) for the switcher's meaning; SOW-004 L174 (per-view widths and expand state, DEL-02-04).",
    Plan=f"T3; SR-02, SR-04, SR-05; Q4a ruled {RULING} (PDF in-panel through the renderer's built-in viewer; DOCX, XLSX, and PPTX through macOS Quick Look with an Open in default app action; zero new dependencies); Q4b ruled {RULING} (10 MB cap on the in-panel text path for text, markdown, code, and CSV; PDF and Quick Look previews uncapped). {BASIS}.",
    Depends=f"DEL-02-02-V3-03; DEL-02-04-V3-01 (per-view widths and expand state); DEL-07-01 path containment for the endpoint; Quick Look through Electron `previewFile` touches `frontend/electron/main.ts` and the IPC sender policy ({ELECTRON_NOTE}).",
    Write_locus="`frontend/src/components/shell/file-tree-panel.tsx`, `document-view.tsx`, the right-panel view switcher under `frontend/src/components/woven-dialogue/**`, a new bounded read endpoint under `frontend/src/app/api/working-root/file/**`, additive `frontend/src/lib/woven-dialogue/woven-workspace-state.ts` fields coordinated with DEL-02-04, additive Quick Look IPC in `frontend/electron/main.ts` and `preload.ts`, tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"every tree file opens in-panel (text, markdown, code, and CSV up to 10 MB; PDF through the built-in viewer) or hands off (Office files through Quick Look with Open in default app; oversized text shows its size and a hand-off); endpoint containment tests refuse traversal, symlink escape, and instruction-root paths; drag-to-resize and expand persist per view; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-02-03", "DEL-02-03-V3-02", "NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed",
    "reference chips in replies and activity rows, Ask and Attach from the viewer, and the quote row in the composer (T4).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L309; SOW-008 L178 (explicit next-turn context references and artifact anchors as convenience state, DEL-02-04).",
    Plan=f"T4; SR-09; Q2 ruled {RULING} (a quote travels as an attachment with `clientType: 'quote'`; no harness change and no Section 8 revision). {BASIS}.",
    Depends="DEL-02-03-V3-01; the DEL-02-05 attachment controls and the DEL-02-04 draft and attachment state consumed, not changed; `frontend/src/lib/harness/**` untouched.",
    Write_locus="viewer and chip components under `frontend/src/components/shell/**` and `woven-dialogue/**`, the composer quote row, `clientType` handling in `frontend/src/lib/woven-dialogue/**`, tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"chips in replies and activity rows resolve to tree files; Ask and Attach from the viewer; the composer quote row produces a `clientType: 'quote'` attachment carrying source path and range, proven by a wire-shape test and an empty `lib/harness/**` diff; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)
add(
    "DEL-05-04", "DEL-05-04-V3-02", "NOT_SELECTABLE_UNTIL: DEL-02-03-V3-01 landed",
    "Session view: the replay lens mounted in the right panel with a read-only banner and a parent link (T3 part).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L339 (selected-session read-only replay lens); SOW-006 L176 (the Session view is read-only, never takes the centre, and is distinct from the mounted primary).",
    Plan=f"T3 part; SR-08. {BASIS}.",
    Depends="DEL-02-03-V3-01 (the view switcher); DEL-02-02-V3-03 (replay beside a visible primary); the existing `selected-session-replay-lens.tsx`.",
    Write_locus="`frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx` mount and the right-panel Session view, tests; deliverable-local state.",
    Checks=f"{FRONTEND_CHECKS}.",
    Return=f"the Session view renders in the right panel with a read-only banner and a parent link, never takes the centre, and never transfers the primary dialogue's draft, attachments, or context; live versus replayed state stays explicit; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS; restart/resume continuity remains DEL-05-04-V3-01.",
)
add(
    "DEL-09-04", "DEL-09-04-V3-02", "NOT_SELECTABLE_UNTIL: DEL-02-01-V3-04 selected",
    "`build/icon.icns` replacement with packaging-integrity regeneration and the reproducibility record for the raster icon (T7 packaging part).",
    Trace="OUT-001, AC-001, VER-001; applied decomposition row L381 (macOS arm64 unsigned DMG; instruction-root assets plus SDK packaging posture proven valid); SOW-030, SOW-072.",
    Plan=f"T7 packaging part; SR-16; Q5 ruled {RULING} (icon only; no pop-out window); `05_LOGO_AND_BRAND.md` §4 (SHA-256 `{BRAND_HASH}`). {BASIS}.",
    Depends="DEL-02-01-V3-04 (source SVG and raster record); F-APP-2 and D-APP-97 (no signing, notarization, or distribution; unsigned DMG only).",
    Write_locus="`frontend/build/icon.icns`, `frontend/build/icon-macos.svg`, packaging-integrity summary regeneration under `frontend/scripts/**`, `Evidence/**`, deliverable-local state. No signing identity, notary call, or distribution.",
    Checks=f"{FRONTEND_CHECKS}; packaged launches run only under the AGENTS.md host-capability escalation rule.",
    Return=f"a regenerated `.icns` from the recorded source with the reproducibility record (source SVG hash, rasterization command and versions, per-size hashes) and an updated packaging-integrity summary; no signing or release act; {EVIDENCE_TAIL}.",
    Removed_when="merged with review PASS.",
)

# ---------------------------------------------------------------- record-only lines and history
RECORD_ONLY = {
    "DEL-08-03": (
        f"- {DATE} - SCA-APP-010 Gate-5 applied and seated ({RULING}): the contextual Pipeline presentation is retired from the active shell by owner ruling (G2-CONFIRM; SOW-007 presentation half); DEL-08-03 remains the presentation-neutral DECOMP/PREP/TASK/AUDIT dispatch semantic owner with code, routes, and tests retained; no active-shell consumer exists and any later consumer may not infer plans/tasks from conversational prose. No work item seated; no lifecycle, Checking Approval SHA, or dependency change."
    ),
    "DEL-01-03": (
        f"- {DATE} - {RULING} seating pass: the plain-language copy table in `plans/shell-redesign_2026-09-04/03_TARGET_SPEC.md` §10 (SHA-256 `{SPEC_HASH}`) is recorded as a candidate amendment to this deliverable's boundary copy, offered and not adopted; DEL-02-01-V3-01's copy pass leaves the professional-boundary copy unchanged. No item seated; no lifecycle, Checking Approval SHA, or dependency change."
    ),
}

CONTRACT_OBLIGATIONS = {
    "DEL-02-01": [
        "The centre dialogue is never hidden, unmounted, or replaced; the frame has no header row.",
        "The composer context line shows folder, agent, permissions, delegation, and rung from recorded state; a chat may have no folder and says so.",
        "Folder selection is live only before a chat's first message and fixed thereafter; invalid or instruction-root-contained paths are refused by DEL-07-01's validation with the refusal visible (Q9: native picker, macOS recent documents, Reveal in Finder, folder drop).",
        "Chat organisation acts on local convenience state owned by DEL-02-04 only; deleting a chat hides it locally and never mutates the runtime session record (Q1); derived titles pass the redaction helper (Q6).",
        "Existing routes, queries, aliases, and the loop-first UI remain compatibility surfaces; the retired Workbench and Pipeline routes stay reachable by URL and unlisted (Q3).",
        "The pop-out panel window is not in scope (Q5); the account row is hosted here and its presentation is DEL-02-05's.",
    ],
    "DEL-02-02": [
        "The primary dialogue is invariant; Workbench and Pipeline are unmounted from the active shell with code, routes, and tests retained and the routes reachable by URL (Q3); the Work projection stays unmounted until an explicitly recorded plan/task source exists.",
        "Who is working renders only canonical recorded sessions and exact parentage with source, authority class, responsible reference, currency, and evidence; unknown stays unknown and provenance-labelled.",
        "The Workflows view lists, opens, follows, pauses, creates, and binds governed workflow files with provenance (`roadmapSource` and hash), reports currency (Q15), and advances position only at human gates recording who advanced it (Q16); creation refuses role, folder, or delegation policy unset; the file steers and never records.",
        "The proposal card promotes nothing silently; Accept, Adjust, and Not now are human acts applied by the app; one proposal per chat per trigger; live `proposal.*` consumption waits on DEL-05-02 after Root DEL-02-10 acceptance.",
        "Presentation only: DEL-08-02 owns routing and guarded selection, DEL-08-03 dispatch semantics (no active-shell consumer), DEL-08-04 role and delegation semantics, DEL-08-05 child records, DEL-05-04 replay and projection, DEL-06-03 the `propose` tool, DEL-07-03 the workflow file contract.",
        "If implementation review finds cross-domain churn between the coordination and workflow views, a split is proposed before the envelope widens (row split trigger).",
    ],
    "DEL-02-04": [
        "Workspace-state changes are additive v1 fields under the existing schema string with rollback-safe migration that preserves prior state.",
        "Per-view right-panel widths, expand state, drafts, explicit next-turn context references, artifact anchors, selected replay references, panel state, chat annotations, known folders, chat rung, declined proposal triggers, and local presets are non-authoritative convenience state.",
        "Convenience state never transfers session authority, never stands in for the governed workflow file, and visible artifacts are not automatically model context.",
        "The one-line activity strip replaces the resizable shelf; the Activity view is a right-panel view.",
    ],
    "DEL-02-05": [
        "One app-wide account is presented; consent, network posture, and role are explained and controlled per folder over the root-private app-owned `CODEX_HOME`; `K-CONSENT-1` and the port's per-root login semantics are unchanged.",
        "The account row shows only the local model server status; no OpenAI status indicator and no API status indicator is rendered, now or after DEL-02-05-V3-03 (Q7).",
        "The Settings view hosts the split app-wide and per-folder account groups plus the runtime, key, and appearance panels with port behaviour unchanged; the fake port carries the UI until the accepted Root/App contract (DEL-02-05-V3-03).",
        "The root-private login home and any shared-login contract remain Root DEL-02-09's; the amendment is routed by the SCA-APP-010 Root notice (Q8) and live claims stay gated on the accepted contract, G3, G-CSP, and G4.",
        "Agent 0/1/2 role entry remains available for Codex sessions with the exact `role not mechanically enforced` and `Opt-in Preview` posture labels.",
    ],
    "DEL-03-02": [
        "App `/api/harness/*` and Desktop surfaces remain daemon clients; the daemon owns runtime session state.",
        "Boot and session-creation requests bind registered project identity/root, persona, mode, delegation policy, and options; the boot fingerprint reflects the real inputs.",
        "The delegation policy defaults to `none`, narrows managed delegation only, and adds no delegation class; the stored session-record field is Root DEL-02-11's (OI-008).",
    ],
    "DEL-04-04": [
        "The prompt is composed from the bundled base plus the client-owned, hash-pinned organisation layer; the layer's pin is verified before use (Q14).",
        "A followed governed workflow's roadmap is injected only inside a clearly delimited block that names its source path and hash, read from a K-PATH-2-contained file; the block is steering context and never records.",
        "Persona content hash and boot fingerprint tests cover the layer pin and the roadmap hash.",
    ],
    "DEL-05-02": [
        "Root-owned daemon `HarnessEvent` records are consumed for App audit and replay surfaces without owning the generic schema or writer.",
        "`proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and `proposal.declined` are additive candidates against the closed schema v2 (K-EVENT-3) and are consumed only after Root DEL-02-10 acceptance is routed back (OI-008).",
        "Accepted-turn and terminal-event persistence conformance is verified with malformed-tail tolerance preserved.",
    ],
    "DEL-06-03": [
        "MCP wrappers remain in-process and deterministic; no remote MCP, plugin, marketplace, provider, or network scope opens.",
        "The `propose` tool validates the specification tuple (folder, agent, delegation policy, roadmap, permission mode) against roster and policy values, resolves plan references from Agent 1 procedures, refuses a trigger already declined in the chat, and emits only `proposal.offered`.",
        "Catalog validation and collision prevention remain DEL-06-02's.",
    ],
    "DEL-07-01": [
        "Working-root validity, root separation, and path containment are enforced; instruction-root write protection covers both the bundled base and the client-owned organisation layer (K-ROOT-1).",
        "The organisation layer is hash-pinned, read-only during ordinary project execution, packaging-checked, separate from the working root, and never a working root or a proposal path.",
        "Security acceptance fixtures prove both layers' protection and the pin verification.",
    ],
    "DEL-07-03": [
        "Deliverable metadata, canonical memory, semantic placeholders, and document kit buckets are scanned and validated as before.",
        "The governed workflow file contract defines front matter (agent role, folder, permission, delegation policy, where briefs run, `roadmapSource` and hash), the roadmap grammar with human-gate markers, the app-maintained position with who-advanced attribution (Q16), and library/bind copy semantics (Q10).",
        "The file steers and never records: status, approvals, and evidence stay in deliverable records and the validator refuses them.",
    ],
    "DEL-08-01": [
        "Required instruction-root assets, agent metadata, write scopes, naming, and section markers are verified as before.",
        "Agent 0 and Agent 1 packages carry proposal clauses with named triggers and once-per-chat; skill-declared workflow templates are discoverable; the organisation layer's packaging and pins are checked.",
        "No runtime capability expands; any instruction-file change under `agents/` or `skills/` ships the routed agent-index change notice and the G4 manifest.",
    ],
    "DEL-08-03": [
        "DECOMP/PREP/TASK/AUDIT lane semantics, category and task-scope interpretation, dynamic scope, and disabled-option rules remain presentation-neutral and owned here.",
        "The contextual Pipeline presentation is retired from the active shell by SCA-APP-010 (code retained); no active presentation consumer exists.",
        "Any later consumer may not infer plans or tasks from conversational prose.",
    ],
    "DEL-08-04": [
        "The Chirality-managed delegation bridge enforces managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation and cleanup, and class-aware routing; native descent assigns no Agent 0/1/2 role.",
        "The per-chat delegation policy carried with the session (`none` by default) is honoured as a narrowing input to managed delegation and adds no delegation class.",
        "Role entry for Codex sessions carries the exact `role not mechanically enforced` label and `instruction-asserted` evidence marking where G-ROLE cannot prove non-delegation; WP-03/05 fixtures and D-GOV-35 remain required for the class-aware paths.",
    ],
}

CONTRACT_RULINGS = {
    "DEL-02-01": "Q1, Q3, Q5, Q6, Q9",
    "DEL-02-02": "Q3, Q10 to Q14, Q15, Q16",
    "DEL-02-04": "none (Q3 and Q14 are applied by sibling carriers)",
    "DEL-02-05": "Q7, Q8",
    "DEL-03-02": "none beyond SR-24",
    "DEL-04-04": "Q14",
    "DEL-05-02": "Q13",
    "DEL-06-03": "Q11, Q12, Q13",
    "DEL-07-01": "Q14",
    "DEL-07-03": "Q10, Q16",
    "DEL-08-01": "Q14",
    "DEL-08-03": "SOW-007 presentation retirement (G2-CONFIRM)",
    "DEL-08-04": "none beyond SR-24",
}


# ---------------------------------------------------------------- helpers
def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(msg: str) -> None:
    raise SystemExit(f"BUILD FAIL: {msg}")


def once(text: str, needle: str, where: str) -> None:
    n = text.count(needle)
    if n != 1:
        fail(f"{where}: expected exactly one occurrence of {needle!r}, found {n}")


def replace_once(text: str, old: str, new: str, where: str) -> str:
    once(text, old, where)
    return text.replace(old, new, 1)


def carrier_dir(cid: str) -> Path:
    hits = sorted(EXEC.glob(f"PKG-*/1_Working/{cid}_*"))
    if len(hits) != 1:
        fail(f"{cid}: expected one folder, found {hits}")
    return hits[0]


def split_row(line: str) -> list[str]:
    cells = re.split(r"\s\|\s", line.strip().strip("|").strip())
    return [c.strip() for c in cells]


def decomposition_rows() -> tuple[dict[str, dict], dict]:
    if sha(DECOMP) != DECOMP_SHA:
        fail("decomposition post-image hash mismatch")
    lines = DECOMP.read_text(encoding="utf-8").split("\n")
    rows: dict[str, dict] = {}
    for cid, ln in ROW_LINE.items():
        line = lines[ln - 1]
        if not line.startswith(f"| {cid} |"):
            fail(f"{cid}: row not at L{ln}")
        c = split_row(line)
        if len(c) != 10:
            fail(f"{cid}: expected 10 cells, got {len(c)}")
        rows[cid] = {
            "name": c[1], "type": c[3], "description": c[4], "outputs": c[5],
            "sow_refs": [s.strip() for s in c[6].split(",")],
            "obj_refs": [s.strip() for s in c[7].split(",")],
            "size": c[8], "notes": c[9],
        }
    for aid, ln in ANCHOR_LINE.items():
        if not lines[ln - 1].startswith(f"| {aid} |"):
            fail(f"anchor {aid} not at L{ln}")
    pkg = split_row(lines[ANCHOR_LINE["PKG-02"] - 1])
    if len(pkg) != 5:
        fail("PKG-02 row shape")
    return rows, {"name": pkg[1], "description": pkg[2], "inclusion": pkg[3], "exclusions": pkg[4]}


def wi_ids() -> dict[str, dict[str, list[str]]]:
    out: dict[str, dict[str, list[str]]] = {}
    for line in FUTURE_WRITE_SET.read_text(encoding="utf-8").splitlines()[1:]:
        wid = line.split(",", 1)[0]
        if not (wid.startswith("WI-") or wid.startswith("DEP-")):
            continue
        m = re.search(r"/1_Working/(DEL-\d\d-\d\d)_", line)
        if not m:
            continue
        out.setdefault(m.group(1), {"WI": [], "DEP": []})[wid[:2] if wid.startswith("WI") else "DEP"].append(wid)
    return out


def wrap(text: str) -> str:
    return textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False)


def targets(cid: str) -> list[Path]:
    d = carrier_dir(cid)
    if cid in THIRTEEN:
        return [d / n for n in ("ScopeOfWork.md", "_CONTEXT.md", "_STATUS.md", "MEMORY.md", "_REFERENCES.md")]
    return [d / "_STATUS.md", d / "MEMORY.md"]


# ---------------------------------------------------------------- transactions
def tx_scope_of_work(cid: str, text: str, row: dict, wi: dict) -> str:
    where = f"{cid}/ScopeOfWork.md"
    fm = re.search(r"^decomposition_basis: (.+)$", text, re.M)
    if not fm:
        fail(f"{where}: decomposition_basis missing")
    text = replace_once(text, fm.group(0), f"decomposition_basis: {DECOMP_REL}@{PIN_COMMIT}", where)
    old_scope = re.search(r"^project_scope_refs: \[(.*)\]$", text, re.M)
    old_obj = re.search(r"^package_objective_refs: \[(.*)\]$", text, re.M)
    if not old_scope or not old_obj:
        fail(f"{where}: refs front matter missing")
    new_scope = ", ".join(row["sow_refs"])
    new_obj = ", ".join(row["obj_refs"])
    text = replace_once(text, old_scope.group(0), f"project_scope_refs: [{new_scope}]", where)
    text = replace_once(text, old_obj.group(0), f"package_objective_refs: [{new_obj}]", where)
    purpose_old = f"in service of project scope [{old_scope.group(1)}] and package objectives [{old_obj.group(1)}]."
    purpose_new = f"in service of project scope [{new_scope}] and package objectives [{new_obj}]."
    text = replace_once(text, purpose_old, purpose_new, where)
    if cid == "DEL-02-02":
        text = replace_once(
            text,
            "- **OUT-001** — Work/Agents Coordination, Workbench, and Pipeline presentation contract grounded in SOW-006, SOW-007, OBJ-001, and OBJ-007.",
            "- **OUT-001** — Right-panel coordination, workflows, and proposal presentation contract grounded in SOW-006, SOW-081, SOW-082, OBJ-001, and OBJ-007 (SCA-APP-010; the earlier Work/Agents Coordination, Workbench, and Pipeline contract remains dated history).",
            where,
        )
        text = replace_once(text, "| OUT-001 | SOW-006 SOW-007 OBJ-001 OBJ-007 |", "| OUT-001 | SOW-006 SOW-081 SOW-082 OBJ-001 OBJ-007 |", where)
    old_hdr = "## SCA-APP-004 Gate-5 Current Contract (Controlling)"
    if old_hdr in text:
        text = replace_once(text, old_hdr, "## SCA-APP-004 Gate-5 Current Contract (Controlling until SCA-APP-010)", where)
        text = replace_once(text, "| SCA-APP-004 Gate-5 Current Contract; CLM-008 |", "| SCA-APP-010 Gate-5 Current Contract; CLM-008 |", where)
    items_here = ", ".join(i for i, _, _ in ITEMS.get(cid, [])) or "none (record-only)"
    obligations = "\n".join(f"{n}. {o}" for n, o in enumerate(CONTRACT_OBLIGATIONS[cid], 1))
    section = (
        "## SCA-APP-010 Gate-5 Current Contract (Controlling)\n\n"
        + wrap(
            "The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied "
            f"2026-09-04 at content commit `{PIN_COMMIT}`, merged as `{APPLY_MERGE}`; active "
            f"pointer moved as `{POINTER_MERGE}`) makes the centre dialogue the invariant "
            "primary surface and seats the prompted specification ladder. Where any earlier "
            "current-contract section or older clause in this document disagrees with the "
            "applied row below, this section controls. Earlier sections, clauses, and "
            "evidence remain dated compatibility history and are not deleted."
        )
        + "\n\n### Current responsibility\n\n"
        + f"`{cid} {row['name']}` ({row['type']}, applied decomposition row L{ROW_LINE[cid]}):\n\n"
        + wrap(row["description"])
        + "\n\n"
        + wrap("Applied row notes: " + row["notes"])
        + "\n\n"
        + wrap("Applied row outputs: " + row["outputs"] + ".")
        + "\n\n### Current acceptance obligations\n\n"
        + obligations
        + "\n\n### Seating and rulings\n\n"
        + wrap(
            f"Remaining items seated under {RULING} ({DATE}): {items_here}. Ruled "
            f"questions applied here: {CONTRACT_RULINGS[cid]}. Alignment writes "
            f"{', '.join(wi['WI'])} performed in run `{RUN_ID}`; dependency writes "
            f"{', '.join(wi['DEP'])} await the registered dependency-extract pass after "
            "owner acceptance of this alignment. No lifecycle, Checking Approval SHA, "
            "dependency-acceptance, product, or release act is implied."
        )
        + "\n\n"
    )
    once(text, "\n## Deliverable Definition", where)
    text = text.replace("\n## Deliverable Definition", "\n" + section + "## Deliverable Definition", 1)
    return text


def tx_context(cid: str, text: str, row: dict, pkg: dict) -> str:
    where = f"{cid}/_CONTEXT.md"
    m = re.search(r"^\| DeliverableName \| (.+?) \|$", text, re.M)
    if not m:
        fail(f"{where}: DeliverableName row missing")
    old_name = m.group(1)
    if old_name != row["name"]:
        text = replace_once(text, m.group(0), f"| DeliverableName | {row['name']} |", where)
        text = replace_once(text, f"# Context: {cid} {old_name}", f"# Context: {cid} {row['name']}", where)
    sec = re.search(r"^## Deliverable Scope\n\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
    if not sec:
        fail(f"{where}: Deliverable Scope section missing")
    body = (
        wrap(row["description"])
        + "\n\n"
        + wrap(f"Applied decomposition row L{ROW_LINE[cid]} (SCA-APP-010 Gate 5, {DATE}) notes: " + row["notes"])
        + "\n"
    )
    text = text[: sec.start(1)] + body + text[sec.end(1):]
    if cid in PKG02:
        psec = re.search(r"^\*\*ScopeDescription:\*\* (.*?)(?=\n\n\*\*InclusionCriteria)", text, re.M | re.S)
        if not psec:
            fail(f"{where}: ScopeDescription missing")
        wrapped = wrap("**ScopeDescription:** " + pkg["description"])
        text = text[: psec.start(0)] + wrapped + text[psec.end(1):]
        pn = re.search(r"^\| PackageName \| (.+?) \|$", text, re.M)
        if not pn or pn.group(1) != pkg["name"]:
            fail(f"{where}: PackageName mismatch")
    return text


def tx_references(cid: str, text: str, wi: dict) -> str:
    where = f"{cid}/_REFERENCES.md"
    if cid == "DEL-02-02":
        text = replace_once(
            text,
            "# References: DEL-02-02 Work/Agents Coordination, Workbench, and Pipeline UX",
            "# References: DEL-02-02 Right-Panel Coordination, Workflows, and Proposal UX",
            where,
        )
    refs = re.findall(r"^\| (REF-\d{3}) \|", text, re.M)
    if not refs:
        fail(f"{where}: no REF rows")
    n = max(int(r[4:]) for r in refs)
    r1, r2, r3, r4 = (f"REF-{n + k:03d}" for k in (1, 2, 3, 4))
    snap = SNAPSHOT_REL
    section = (
        "## SCA-APP-010 Gate-5 Authority\n\n"
        "| RefID | Path | Current use |\n|---|---|---|\n"
        f"| {r1} | `{snap}/Brief.md` | Owner-confirmed Gate-1 envelope A001 to A029 and frozen pre-image identities (G1-CONFIRM) |\n"
        f"| {r2} | `{snap}/Gate3/GATE3_AMENDMENT_PACKAGE.md` | Owner-approved exact amendment bytes (G3-CONFIRM), including this deliverable's applied row |\n"
        f"| {r3} | `{snap}/Propagation_Plan.md` | Owner-approved propagation plan (G4-CONFIRM); this deliverable's alignment writes {', '.join(wi['WI'])} and dependency writes {', '.join(wi['DEP'])} |\n"
        f"| {r4} | `{snap}/Handoff_State.md` | Gate-5 handoff state; derivative closure open pending downstream alignment and audits |\n\n"
        + wrap(
            f"Applied identities: decomposition post-image SHA-256 `{DECOMP_SHA}` at content "
            f"commit `{PIN_COMMIT}` (PR #708 merge `{APPLY_MERGE}`); companion register "
            f"post-image `{COMPANION_SHA}`; active pointer `execution/_ScopeChange/_LATEST.md` "
            f"SHA-256 `{POINTER_SHA}` (PR #711 merge `{POINTER_MERGE}`). The authority-corpus "
            "rows above are unchanged (corpus v20 has no decomposition member). Seating and "
            f"alignment are recorded under `{RULING}` and run `{RUN_REL}`."
        )
        + "\n\n"
    )
    once(text, "\n## Decomposition Entry", where)
    text = text.replace("\n## Decomposition Entry", "\n" + section + "## Decomposition Entry", 1)
    if cid == "DEL-02-02":
        text = text.rstrip("\n") + (
            "\n- SCA-APP-010 renames the current deliverable display name to\n"
            "  `Right-Panel Coordination, Workflows, and Proposal UX` without authorizing a\n"
            "  folder rename; stable deliverable ID `DEL-02-02` controls.\n"
        )
    return text


def history_line(cid: str, wi: dict | None) -> str:
    ids = [i for i, _, _ in ITEMS.get(cid, [])]
    selectable = [i for i, g, _ in ITEMS.get(cid, []) if g == "SELECTABLE"]
    if cid in RECORD_ONLY:
        return RECORD_ONLY[cid]
    seated = ", ".join(ids)
    sel = ", ".join(selectable) if selectable else "none"
    if cid in THIRTEEN:
        align = (
            f" `ScopeOfWork.md` re-pinned to the applied decomposition at `{PIN_COMMIT}` with a "
            "SCA-APP-010 Gate-5 Current Contract section; `_CONTEXT.md` and `_REFERENCES.md` "
            f"aligned ({', '.join(wi['WI'])})."
        )
    else:
        align = " Outside the thirteen SCA-APP-010 carriers: seating only, no Scope of Work, context, or reference change."
    extra = ""
    if cid == "DEL-02-02":
        extra = (
            " Display name is now `Right-Panel Coordination, Workflows, and Proposal UX`; "
            "existing DEL-02-02-V3-01 and V3-02 are read under the applied row (the Who is "
            "working view) without text change."
        )
    return (
        f"- {DATE} - SCA-APP-010 shell-redesign seating ({RULING}; owner adopted the seating "
        f"list as presented): Remaining items seeded {seated} (SELECTABLE: {sel}) with gate, "
        "dependency, write-locus, check, and return contracts; ruled questions cited by item."
        f"{align}{extra} Run evidence `{RUN_REL}`. No implementation, lifecycle, dependency-"
        "acceptance, release, or Root act; Current State, Checking Approval SHA, and lifecycle "
        "are unchanged."
    )


def tx_status(cid: str, text: str, wi: dict | None) -> str:
    where = f"{cid}/_STATUS.md"
    lu = re.search(r"^\*\*Last Updated:\*\* .+$", text, re.M)
    if not lu:
        fail(f"{where}: Last Updated missing")
    text = replace_once(text, lu.group(0), f"**Last Updated:** {DATE}", where)
    once(text, "\n## Remaining\n", where)
    once(text, "\n## History\n", where)
    if cid in ITEMS:
        block = "\n".join(t for _, _, t in ITEMS[cid])
        rem_start = text.index("\n## Remaining\n") + len("\n## Remaining\n")
        hist = text.index("\n## History\n")
        remaining = text[rem_start:hist].rstrip("\n")
        if remaining.strip() == "None.":
            # A bare placeholder, not an item (review F1); replaced by the seated items.
            remaining = ""
        for iid, _, _ in ITEMS[cid]:
            if iid in text:
                fail(f"{where}: {iid} already present")
        new_remaining = (remaining + "\n\n" if remaining.strip() else "\n") + block + "\n"
        text = text[:rem_start] + new_remaining + text[hist:]
    hl = history_line(cid, wi)
    hist = text.index("\n## History\n") + len("\n## History\n")
    tail = text[hist:]
    sec_end = re.search(r"\n## ", tail)
    dates = re.findall(r"^- (\d{4}-\d{2}-\d{2})", tail[: sec_end.start()] if sec_end else tail, re.M)
    # Ordering is judged from the first and last dated bullets of the section
    # (review F4: equal adjacent dates are not evidence of order). A section
    # whose dates are all equal or absent is appended at the end, as A12 did.
    newest_first = len(dates) >= 2 and dates[0] > dates[-1]
    if newest_first:
        text = text[:hist] + hl + "\n" + tail
    else:
        m = re.search(r"\n## ", tail)
        if m:
            end = hist + m.start()
            text = text[:end].rstrip("\n") + "\n" + hl + "\n" + text[end:]
        else:
            text = text.rstrip("\n") + "\n" + hl + "\n"
    return text


def tx_memory(cid: str, text: str) -> str:
    ids = ", ".join(i for i, _, _ in ITEMS.get(cid, [])) or "none (record-only history line)"
    if cid in THIRTEEN:
        basis = (
            "the applied decomposition row and the SCA-APP-010 Gate-5 Current Contract "
            "section in `ScopeOfWork.md` state the current responsibility"
        )
        head = f"SCA-APP-010 seating and alignment ({RULING})"
    else:
        basis = (
            f"the applied decomposition row L{ROW_LINE[cid]} (unchanged by SCA-APP-010) "
            "states the responsibility; this carrier was seated only and not aligned in "
            "this pass, so `ScopeOfWork.md` keeps its earlier pin and carries no "
            "SCA-APP-010 section"
        )
        head = f"SCA-APP-010 seating, outside the thirteen carriers ({RULING})"
    line = (
        f"- {DATE} - {head}: Remaining items {ids}; read `_STATUS.md` with this file before "
        f"any write; {basis}; nothing here is authority. No lifecycle, Checking Approval SHA, "
        "dependency, product, or release change."
    )
    return text.rstrip("\n") + "\n" + line + "\n"


# ---------------------------------------------------------------- modes
def all_targets() -> list[Path]:
    out: list[Path] = []
    for cid in CARRIERS:
        out.extend(targets(cid))
    return out


def rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT))


def freeze() -> None:
    EVID.mkdir(parents=True, exist_ok=True)
    pre = {rel(p): sha(p) for p in all_targets()}
    pre[DECOMP_REL] = sha(DECOMP)
    (EVID / "pre_images.json").write_text(json.dumps(pre, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"froze {len(pre)} pre-images")


def apply() -> None:
    pre = json.loads((EVID / "pre_images.json").read_text(encoding="utf-8"))
    for p in all_targets():
        if pre.get(rel(p)) != sha(p):
            fail(f"pre-image mismatch: {rel(p)}")
    if pre.get(DECOMP_REL) != DECOMP_SHA:
        fail("decomposition pre-image mismatch")
    rows, pkg = decomposition_rows()
    wi = wi_ids()
    for cid in THIRTEEN:
        if set(wi.get(cid, {}).get("WI", [])) == set() or len(wi[cid]["WI"]) != 5 or len(wi[cid]["DEP"]) != 2:
            fail(f"{cid}: FUTURE_WRITE_SET rows not found")
    staged: dict[Path, str] = {}
    for cid in CARRIERS:
        d = carrier_dir(cid)
        w = wi.get(cid)
        if cid in THIRTEEN:
            staged[d / "ScopeOfWork.md"] = tx_scope_of_work(cid, (d / "ScopeOfWork.md").read_text(encoding="utf-8"), rows[cid], w)
            staged[d / "_CONTEXT.md"] = tx_context(cid, (d / "_CONTEXT.md").read_text(encoding="utf-8"), rows[cid], pkg)
            staged[d / "_REFERENCES.md"] = tx_references(cid, (d / "_REFERENCES.md").read_text(encoding="utf-8"), w)
        staged[d / "_STATUS.md"] = tx_status(cid, (d / "_STATUS.md").read_text(encoding="utf-8"), w)
        staged[d / "MEMORY.md"] = tx_memory(cid, (d / "MEMORY.md").read_text(encoding="utf-8"))
    # Fail closed on every staged text before any write; pre-existing trailing
    # whitespace in untouched lines is not this builder's to change.
    for p, t in staged.items():
        original_lines = set(p.read_text(encoding="utf-8").split("\n"))
        if "\r" in t:
            fail(f"{rel(p)}: CR in staged text")
        for line in t.split("\n"):
            if line != line.rstrip() and line not in original_lines:
                fail(f"{rel(p)}: trailing whitespace in an introduced line: {line[:60]!r}")
    for p, t in staged.items():
        p.write_text(t, encoding="utf-8")
    post = {rel(p): sha(p) for p in all_targets()}
    (EVID / "post_images.json").write_text(json.dumps(post, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    seeded = [
        {"carrier": cid, "item": iid, "gate": gate, "selectable": gate == "SELECTABLE", "outside_thirteen": cid in OUTSIDE}
        for cid in CARRIERS for iid, gate, _ in ITEMS.get(cid, [])
    ]
    seeded += [{"carrier": cid, "item": None, "gate": None, "selectable": False, "record_only": True, "outside_thirteen": cid in OUTSIDE} for cid in RECORD_ONLY]
    (EVID / "seeded_items.json").write_text(json.dumps(seeded, indent=2) + "\n", encoding="utf-8")
    print(f"applied {len(staged)} files; seeded {sum(1 for s in seeded if s.get('item'))} items")


def check() -> None:
    post = json.loads((EVID / "post_images.json").read_text(encoding="utf-8"))
    bad = [rel(p) for p in all_targets() if post.get(rel(p)) != sha(p)]
    if bad:
        fail("post-image mismatch: " + ", ".join(bad))
    print(f"post-images verified for {len(post)} files")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    {"--freeze": freeze, "--apply": apply, "--check": check}.get(mode, lambda: fail("mode required: --freeze | --apply | --check"))()
