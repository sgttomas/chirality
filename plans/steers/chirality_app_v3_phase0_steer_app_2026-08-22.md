# STANDING DIRECTION — App-dev loop — v3 release pathway, Phase 0 (WP-00 guard + WP-01 App half)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: App Phase 0 of the v3 release pathway. Target workspace: App-dev loop. Paste together with `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-22 and updated with the
owner's G0 rulings of the same day. Paste whole, together with the attached
`plans/steers/chirality_app_v3_g0_record_2026-08-22.md`. Transcribe both verbatim into the closeout receipt as
CHAT_TRANSCRIPTION. Where the G0 record is marked AMENDS PLAN it supersedes
Revision 3.1's text.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains `13201dfe7dc3b97c9aa36f6305cae604b48ef80f` (PR #615).
- Plan `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` SHA-256
  `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — input, not authority.
- **WP-00 guard (G0 C2):** `git rev-parse origin/main:projects/chirality-app-dev/frontend`
  = `374de16c4c4172b04f3e5c4e49eb745721846a30` (identical at `1b375af4f`). This
  tranche writes nothing under `projects/chirality-app-dev/frontend/`. Re-check
  the tree id at closeout and state it in the receipt. Until the owner's
  DEL-09-04 capture or an explicit deferral is transcribed, that guard binds
  every later tranche too.
- `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` SHA-256
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`
  (active SCA-APP-007, `CLOSED_FOR_SCOPE_CHANGE_ONLY`) — SCA-APP-008 is the next ID.
- Last App receipt is 185. This tranche writes Receipt 186.
- Highest App register id is TM-APP-044; no register row is written here.
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Produce the App-side governed basis for the v3 pathway: the SCA-APP-008 Gate-1
assessment with carriers and the App half of the objective-relative DAG, a
Task Management triage packet for the owner, and a preparation-lane baseline
evidence report. No contract, code, register, lifecycle, or pointer write.

## Nodes (N=3, write-disjoint; sealed briefs under `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE0_2026-08-<DD>/instances/<NODE>/`)

### N1 — SCOPE_CHANGE: SCA-APP-008 Gate-1 assessment + App DAG
Write target: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-<DD>_<HHMM>_V3_Release_Pathway/` only.
Produce (assessment only; status `AWAITING_OWNER_ACCEPTANCE`; `_LATEST.md` untouched):
- `Brief.md`, `Impact_Assessment.md`, `Carrier_Map.md` seating every App work
  item the plan names, as amended by the G0 record:
  - DEL-04-01 stays a probe; DEL-08-04 stays managed and carries an explicit
    **D-APP-103 interaction statement = "defers"** (the per-attempt
    decision-replay packet is prepared after SCA-APP-008 applies so it covers
    both descendant classes once; one sentence, no new instrument — G0 D3);
  - **G0 D1:** state that the D-APP-74 exclusion (`D-APP-74_RULING_2026-07-23.md:100-104`)
    is tranche-scoped to SCA-APP-004, and that SCA-APP-008 authorizes
    multi-child managed execution and the root `AGENTS.md` Agent 0/1/2 graph as
    App capabilities for the v3 carriers (DEL-08-04 / DEL-08-05 amendments;
    `managed-delegation.ts:480-496` already checks active siblings) —
    prospective supersession, no retroactive edit;
  - **G0 A3 parity:** Agent 0/1/2 role entry for Codex sessions is a product
    requirement; the Agent 2/TASK mode carries the "role not mechanically
    enforced" label state when G-ROLE fails; UX carrier shows it;
  - `subagent-governance.ts:205-213` change seated in WP-06 *conditional on the
    Root D-GOV-35 ruling* (not before);
  - six credential IPC handlers in `frontend/electron/api-key-ipc.ts:110-169`
    to adopt the `runtime-control-ipc.ts:85` `isAuthorizedSender` policy;
    two-job installer via runtime-control IPC; consent UI including the
    **three per-root command-network postures (G0 A7)** and the per-root login
    explanation (G0 A9); v2→v3 migration; **resume-continuity behaviour (G0 A4)**
    in the session UX; DEL-09-04 re-stage rule;
  - new account/consent UX carrier; new release-operations carrier (WP-11)
    with the runbook authored in WP-09; **macOS arm64 only, second target
    deferred to a post-rc.1 scope change (G0 B1)**; no App Sandbox (G0 A5);
    Opt-in Preview label (G0 A8);
  - RQG §13 Shared Runtime Gate mapping (`docs/RELEASE_QUALITY_GATES.md:161`);
    D-APP-97 / F-APP-2 remain active through preparation, lift only at G6a with
    the exact candidate (G0 D2); TM-APP-030 left to G-HELPER (G0 B2);
    TM-ROOT-122 Electron drift named as a G1 blocker only (G0 B4 — no pin
    amendment here).
- `Contract_Amendments.proposed.md`: proposed (not applied) text for App
  CONTRACT.md rows K-CONTROL-1 (second socket), K-ROLE-2, K-NET-1 (service
  endpoints + three command-network postures), K-KEY-1 (OAuth/device-code/
  keyring/safeStorage/typed decrypt failure), K-EVENT-3/4/6 (closed schema v2),
  plus the consent-port and untyped-code rows.
- `WORK_GRAPH.json` + `DAG.md`: App half of the release-pathway DAG; cross-loop
  edges to Root as *notice edges* citing Root's SCA-004 notice by path+SHA if it
  has landed, else marked `PENDING_ROOT_SCA-004`; SCCs with proposed moves;
  cycle edges non-gating until resolved. Dispatch `AUDIT_DEP_CLOSURE`; include return.
- `Handoff_State.md` (four-state form) and a draft reciprocal notice to Root
  kept inside the folder (routed only after owner acceptance).
Check surface: `WORK_GRAPH.json` parses; node ids resolve to live App
deliverable folders or named Root notice edges; AUDIT_DEP_CLOSURE return present;
`_LATEST.md` SHA unchanged; nothing under `docs/` or `frontend/` touched.

### N2 — TASK_MANAGEMENT: G0 triage packet
Write target: `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/TRIAGE_PACKET_2026-08-<DD>_V3_G0.md` only (plus a harvest file beside it if candidates exist).
Produce:
- TM-APP-027 / 028 / 032: byte-exact re-check of each live Trigger against the
  DEL-02-06 acceptance-005 snapshot (`execution/PKG-02_*/1_Working/DEL-02-06_*/_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`
  + `SNAPSHOT_MANIFEST.sha256`): confirm the "complete immutable binding
  manifest" condition is not met (ten `HELD_UNAVAILABLE`), cite the TM-APP-032
  Notes entry of 2026-08-21, record G0 B3 verbatim. Recommendation only.
- TM-APP-025: transcribe G0 B1 as the owner's disposition with closure path
  (RESOLVED_BY_DECISION when SCA-APP-008 applies). TM-APP-030: transcribe G0 B2.
- Candidate rows (harvest only): HostedEngineConsentPort; credential-IPC sender
  authorization; per-root command-network consent postures; `subagent-bridge.ts:6`
  stale `rulingRef` (cites D-APP-10, actual basis D-GOV-14 item 7);
  secret-evidence scanner `.jsonl` gap.
Check surface: `tools/taskmgmt/taskmgmt.py validate --register
projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`
passes with the register byte-identical to basis.

### N3 — evidence-only: preparation-lane baseline
Write target: `projects/chirality-app-dev/execution/_Evaluation/V3_PREP_BASELINE_2026-08-<DD>/` only.
Produce `REPORT.md` with every fact cited as `path:line` + blob SHA-256 at
basis, no code change: Electron `43.2.0` in `frontend/package.json:67` and
lockfile vs governed `43.1.1`; `electron/api-key-storage.ts:83-105` safeStorage
null-collapse; `electron/cli-launcher.ts:19-20` bundled `runtime-cli/chirality-cli.mjs`
path and `:57` `ELECTRON_RUN_AS_NODE=1`; `runtime/packages/cli/src/launch-agent.ts:250-254`
hard-coded `--runtime-daemon`; `frontend/scripts/scan-secret-evidence.mjs`
extension list; `.github/workflows/desktop-release-template.yml:62-68`
credential hard-fail; `src/lib/harness/sdk-options-builder.ts:49-52`
`CHIRALITY_ALLOW_SDK_BYPASS`; `tool-path-policy.ts` argument-only inspection;
`_DomainEngines/profiles/pec.yaml:34-45` suffix globs; `managed-delegation.ts:480-496`
sibling overlap check; RQG §13 text; BUILD_AND_RELEASE.md release steps.
Conclude with the AT-ids (plan §10.1) each fact feeds.
Check surface: every cited line quoted verbatim and reproducible with
`git show origin/main:<path> | sed -n '<n>p'`.

## Not selectable in this tranche
`projects/chirality-app-dev/frontend/**`, `projects/chirality-app-dev/docs/**`,
`projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md`,
`.../_TaskManagement/REGISTER.csv` and `REGISTER_CLOSED.csv`, any `_STATUS.md`,
`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**`, `runtime/**`,
root `docs/**`, `AGENTS.md`, `plans/**`. No foreign-loop writes (Root surfaces),
no artifact download, no login/logout act (WP-00 is owner-executed), no pin
changes (G0 B4), no sync/rebase without owner authorization, no merge.

## Failure rule
Unlimited repair with fresh re-review per node. A node that cannot complete
returns its handoff state with blockers; never narrow or widen silently.

## Closeout
One tranche, one branch `codex/app-v3-phase0-2026-08-<DD>`, one PR to `main`,
commits in order N3 → N2 → N1 (N1 may cite N3's report). Append Receipt 186 to
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` after the fact, in-PR, with:
this steer and `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` as CHAT_TRANSCRIPTION (record its
SHA-256); per-node write sets; the frontend tree id at start and end; every
cited SHA; validator outputs. Run before pushing:
`tools/validation/validate_candidate_whitespace.py --base-ref origin/main`,
`tools/validation/validate_app_dev_loop_receipts.py --repo-root . --validation-commit <HEAD>`,
`tools/taskmgmt/taskmgmt.py validate --register <app register>`. Do not merge.
If `main` advances, request sync authorization and record it. HELP_HUMAN
byte-verifies before endorsement.
