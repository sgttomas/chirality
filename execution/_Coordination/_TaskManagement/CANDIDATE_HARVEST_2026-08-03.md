# Root Task Management — Candidate Harvest Report (2026-08-03)

Status: **DECISION SUPPORT ONLY — NOT AUTHORITY — NO REGISTER ROWS WRITTEN**

Invoking loop: Root
Register home: `execution/_Coordination/_TaskManagement/`
Mode: Candidate harvest (generational pass, step 2)
Current basis: `def4437d1` (HEAD of the generational-pass worktree, equal to
`main` at session start)
Delta boundary: merge `59cb1e27e` (PR #487, 2026-08-02), the landing of the
prior root harvest + deferral-review generation.

This report presents observations and proposed dispositions only. Promotion,
priority, assignment, deferral, elevation, disposition, and closure remain
owner acts. `SourceSha` values are SHA-256 digests of the current cited source
bytes at the basis above.

Sweep execution note: the deterministic `taskmgmt scan` ran first; three
read-only ephemeral Agent 2 generalist sweeps (owner-steered `opus-5` model)
were then dispatched under sealed briefs — root-surface delta, sibling-loop
closeouts, and scan-output screening — with fan-in validation of load-bearing
claims (PR #491 merge state, G4 CI wiring, Piping response landing) performed
deterministically by the manager before this report was written. No child
wrote any file.

## 1. Mandatory federation preflight

Command:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register execution/_Coordination/_TaskManagement/REGISTER.csv
```

Verdict: **COMPLETE**.

- 4 canonical Git-tracked registers discovered, read, and validated (all
  PASS): Root (37 live: 5 OPEN / 32 DEFERRED; 74 archived), App (11 live;
  24 archived), Piping (27 live; 3 archived), PEC (12 live; 3 archived).
- 0 excluded lookalikes; 0 invalid, unreadable, or ambiguous inputs;
  0 operational errors; `register_writes: 0`.
- 90 typed-field findings presented program-wide: 47 `FOREIGN_LINK_TO_LOCAL`,
  22 `LOCAL_CLOSED_REMOTE_OPEN`, 21 `REMOTE_CLOSED_LOCAL_OPEN`; all other
  classes zero.
- The 21 `REMOTE_CLOSED_LOCAL_OPEN` pairs are all App↔Root and are treated in
  §5 (bulk maintenance observation), not as promotion candidates.

The projection at `.candidates/federation.json` is gitignored, rebuildable,
and never authority.

## 2. Full §5.1 sweep coverage

| §5.1 source class | Sweep result | Root-harvest result |
|---|---|---|
| Decision registers — non-ruled rows | Deterministic scan: 0. App decision register manually confirmed all-RULED (90/90 rows, D-APP-86..90 inspected) | No new candidate |
| Notice files vs. ledgers | 29 tracked-open + 45 not-in-ledger raw observations; every notice dated 2026-08-02/03 manually inspected in full | CH-20260803-01, -02; screened families in §4 |
| Evaluation `FINDINGS.csv` | 156 raw open-status observations; only newly landed file is `PI_0820_CONCORDANCE_2026-08-02_97678A8` (10 rows) | CH-20260803-12, -13; screened F-rows in §4 |
| `Review_Findings.csv` | No new root-owned open row since boundary | No new candidate |
| HOLD registers | No newly changed open HOLD row | No new candidate |
| Handoff blockers | 37 raw observations; `ROOT_FOUR_LANES` and DEL-02-06 handoff surfaces read manually (see scanner-defect disclosure below) | CH-20260803-11; maintenance items in §5 |
| Packet open-question/conflict fields | 64 raw observations; DEL-02-06 `accepted_inputs/OPEN_ITEMS.csv` (16 rows) read manually — its filenames fall outside the v0 scanner's match set | CH-20260803-11 |
| TBD registers | 21 raw rows, all pre-boundary (prior seed/migration set) | No new candidate |
| New review reports | `ASSESSMENT_2026-08-02_LOOP_PATTERN_CONVERGENCE.md` (expressly routes itself to this harvest; its re-entry condition — dev-loop fan-in landed — is satisfied) | CH-20260803-09 |
| Receipt parked lanes | Receipts 86–89 inspected; no new parked lane; Receipt 88 carries the DEL-02-06 deferral trigger | §5 maintenance (TM-ROOT-108/-110) |
| Run-record markers | Exact-line scan of the full 959-file delta for `TM-CANDIDATE:` / `NEEDS_HUMAN_RULING:` / `MISSING:`; false `none` records excluded; `ROOT_FOUR_LANES` grepped in full (zero live markers — commit `446584562` moved its findings into the SESSION_RECON notice) | 8 markers in the SESSION_RECON notice (6 root-filed, 2 loop-owned); 1 App-routed marker (graceful stop) |
| Slates / `## Remaining` / work graphs | Fenced per PRD §5.5; the DEL-02-06 D1–D9 decision slate held at its named owner gate was NOT harvested (only its deferred-gate carrier question is presented, CH-20260803-11) | Not harvested |

Deterministic scan summary: 327 deduplicated observations (59 canonical-copy
duplicates folded), 79 with coarse `SourceRef` overlap with the root register;
projection at `.candidates/scan.json` (gitignored, non-authoritative).

**Scanner under-coverage disclosure (found this session, compensated
manually):** `dedup_canonical()` keys on `(loop, basename, class, id)`, which
collapses distinct same-named surfaces — e.g. all 12 root `HANDOFF_STATE.md`
blocker candidates collapse to one 2026-07-28 survivor, dropping the current
`ROOT_FOUR_LANES_2026-08-02/HANDOFF_STATE.md` from `scan.json` entirely;
`scan_handoff_blockers()` skips any line containing the substring `none`
anywhere; `scan_packet_fields()` matches only three fixed filenames. All three
gaps were closed by manual inspection in this sweep and are jointly presented
as CH-20260803-08.

Two prior-premise corrections recorded for traceability: the SESSION_RECON
notice carries 8 markers (not 6); the TM-PIP-026 closure notice is
pre-boundary (`c07ea11b1`) and was never recorded as assessed by the prior
generation — this report is its assessment of record (§4, S5).

## 3. Promotion slate — Root rows recommended

### CH-20260803-01 — Root RuntimeDaemon graceful-stop connection-drain contract

- **SourceRef:**
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md`
  (addressed "To: Root runtime owner / Root coordination loop"; requested
  actions 1–6 and its `TM-CANDIDATE:` marker)
- **SourceSha:**
  `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`
- **Concern:** Root's `RuntimeDaemon.stop()` awaits Node `server.close()`
  before socket unlink and owner-record removal
  (`runtime/packages/daemon/src/runtime-daemon.ts:90-102`, SHA-256
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` — hash
  matches the notice's citation exactly), and Root has no defined
  connection-drain/termination contract for graceful shutdown with live
  Unix-socket/SSE clients. App's D-APP-88 R2 drill evidences a fresh helper
  completing first-signal shutdown while the post-GUI helper never logs
  `desktop.shutdown.completed`; D-APP-88 Option B is held BLOCKED/PARTIAL on
  Root's reproduction/disproof, drain-contract definition, and bounded tests.
- **Domain lenses:** Deliverables; Work; Planning; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (runtime repair + drain
  contract + tests + evidence), or `INFORMATIONAL_NO_ACTION` only with
  recorded disproving evidence.
- **Existing-row overlap:** none. Adjacent-distinct: `TM-ROOT-108`
  (accepted-turn reconciliation across restart — different defect).
- **Route posture:** Routed response to App owed on ruling (notice items 5–6
  require Root's exact commit/test/evidence references back). Note: no
  root-side copy of this inbound notice exists on `execution/_Coordination/`;
  this row plus the closeout receipt would become Root's inbound record.

### CH-20260803-02 — Shared receipt-validator count-detector false positive (TM-PIP-030 elevation)

- **SourceRef:**
  `execution/_Coordination/NOTICE_2026-08-03_PIPING_TM-PIP-030_RECEIPT_COUNT_DETECTOR_ELEVATION.md`
  §Concern and §Requested Root treatment
- **SourceSha:**
  `712949a99240acdbec49bfaae085a50ba514287dde0cca13c7d9cf4cdc60fa9c`
- **Concern:** `tools/validation/loop_receipt_contract.py` `COUNT_PATTERNS`
  (lines 51–56; SHA-256
  `1b6907f5cc9ec4506a9954562a99df3e43c4fa62fab120f1dbec2726c4f687aa`) treats a
  numeric governed identifier followed by a test noun as an exact execution
  count — `DAG-008 test expectations` fired as a test count. Piping repaired
  its receipt prose, left the shared detector unchanged, and elevated with
  `TM-PIP-030` OPEN / `ElevatedTo=Root`. The false-positive class will re-fire
  for any loop.
- **Domain lenses:** Checking; Work; Decisions.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (narrow the detector +
  regression test); `REJECTED`/`INFORMATIONAL_NO_ACTION` if the owner rules
  prose discipline sufficient.
- **Existing-row overlap:** none; genus-adjacent to TM-ROOT-110/-111.
- **Route posture:** Closure-echo notice to Piping owed on disposition so
  `TM-PIP-030` can close under Piping's instruments with a reciprocal Root
  row ID (the notice expressly awaits one).

### CH-20260803-03 — Practitioner-harness decision-register parser silently reports zero

- **SourceRef:**
  `execution/_Coordination/NOTICE_2026-08-03_SESSION_RECON_TM_CANDIDATES.md`
  marker 1 (lines 14–21)
- **SourceSha:**
  `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`
- **Concern:** `tools/practitioner_harness` `status` reports "No rows parsed"
  for `docs/governance_harness/_DECISIONS/_REGISTER.md`, which visibly
  contains ruled rows — parser/format drift yielding a silent false-clean
  governance status instead of a D-GOV-02 WARN finding.
- **Domain lenses:** Checking; Work.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (parser repair +
  WARN-on-empty + regression fixture).
- **Existing-row overlap:** none.

### CH-20260803-04 — Instruction-entrypoint validator covers two of nine launcher surfaces

- **SourceRef:** same SESSION_RECON notice, marker 2 (lines 23–30)
- **SourceSha:** `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`
- **Concern:** `tools/validation/validate_instruction_entrypoints.py` (SHA-256
  `a20c5c621936ba8527a057b26181e28972358bd796dbaf4b05683ec61e2cae79`) pins
  `PROJECTS = ("chirality-app-dev", "chirality-piping")` and byte-checks only
  those two dev launchers; root, bridge, and PEC catalog entries and all four
  `taskmgmt-init-prompt.md` launchers are unvalidated — the exact drift class
  this validator exists to catch was found live in the uncovered files during
  the Receipt 89 remediation.
- **Domain lenses:** Checking; Work.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (extend target set +
  tests). Triage cross-link to TM-ROOT-110/-111 (guard-coverage genus).
- **Existing-row overlap:** none.

### CH-20260803-05 — Root idle workplan has no Step 0 while LOOP_INIT requires one

- **SourceRef:** same SESSION_RECON notice, marker 3 (lines 31–37)
- **SourceSha:** `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`
- **Concern:** `execution/_Coordination/WORKPLAN_2026-07-27_root_idle.md`
  (SHA-256
  `ef4e998140ea2d846e35dd86d19d76bc5038bf515a41ff5e90b834745669198c`)
  contains no Step 0, while `LOOP_INIT.md` §2 requires running the target
  workplan's Step 0 before selecting or dispatching work; every root session
  either skips a required step or improvises one.
- **Domain lenses:** Planning; Checking.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (amend the idle workplan),
  or `OBE` if the owner selects a successor workplan carrying a Step 0.
- **Existing-row overlap:** none.

### CH-20260803-06 — TM-APP-032 cross-loop wait has no root-side carrier (D-APP-48 successor identity)

- **SourceRef:** same SESSION_RECON notice, marker 4 (lines 38–47);
  corroborated in App register row `TM-APP-032`
  (`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`,
  SHA-256 `bd863e1a873b5e8bafc83f0ae8aa06569d89a1100650ee43e57fcfc30581c1de`)
  and independently re-found by the App loop's own post-D-APP-90 harvest
  ("Root may harvest its own marker")
- **SourceSha:** `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`
- **Concern:** App row `TM-APP-032` is DEFERRED with sole trigger "Root's
  accepted successor identity for D-APP-48", but no live or archived root row
  references D-APP-48 and no Root response names such an identity — a
  cross-loop wait nothing on the root side can ever fire.
- **Domain lenses:** Action Item; Planning; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — either mint the root
  counterpart row (this one) and eventually rule the successor identity, or
  rule that an existing row (TM-ROOT-035 / -105 / -107) carries it and route
  a notice so App re-cites its trigger.
- **Existing-row overlap:** none by SourceRef; substantively adjacent to
  TM-ROOT-035/-105/-107.
- **Route posture:** Routed notice to App owed either way (App must amend its
  trigger under its own instruments; Root cannot foreign-write).

### CH-20260803-07 — `taskmgmt.py` loop attribution breaks on PEC's split home

- **SourceRef:** same SESSION_RECON notice, marker 5 (lines 48–56)
- **SourceSha:** `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`
- **Concern:** `tools/taskmgmt/taskmgmt.py` `loop_of_source()` (lines
  390–399; SHA-256
  `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101`) derives
  loop identity from the first two path segments, attributing
  `projects/pec/execution/**` to a loop with no register while PEC's register
  lives at `_DomainEngines/pec/_TaskManagement/`; the deterministic layer
  disagrees with the governed topology, and the binding survives only as
  launcher prose.
- **Domain lenses:** Checking; Work.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (loop alias + tests);
  courtesy notice to the PEC loop on landing.
- **Existing-row overlap:** none (closed TM-PIP-026 concerned a different,
  already-repaired defect in the same file).

### CH-20260803-08 — Harvest scanner under-coverage: basename dedup collapse, `none`-substring skip, packet-filename pin

- **SourceRef:** `tools/taskmgmt/taskmgmt.py` `dedup_canonical()` (lines
  402–423, key on `(loop, basename, class, id)`), `scan_handoff_blockers()`
  (line 383), `scan_packet_fields()` filename set; evidenced by
  `.candidates/scan.json` `dedup_dropped_copies: 59` and the absence of
  `ROOT_FOUR_LANES_2026-08-02/HANDOFF_STATE.md` from all 327 candidates
- **SourceSha:** `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101`
- **Concern:** The deterministic sweep silently drops distinct same-named
  surfaces (12 root `HANDOFF_STATE.md` blocker sets collapse to one 2026-07-28
  survivor; distinct FINDINGS rows sharing an ID across evaluation reruns
  fold), skips blocker lines containing `none` anywhere in the string, and
  misses packet fields not named `Open_Questions.csv` / `Conflicts.csv` /
  `Amendment_Candidates.csv`. Both prior and current generations compensated
  by manual inspection; the workaround is undocumented tribal practice.
- **Domain lenses:** Checking; Work.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` (path-aware dedup key,
  value-anchored `none` exclusion, extensible packet-field match + fixtures).
- **Existing-row overlap:** none.

### CH-20260803-09 — Four loop-pattern convergence options await an owner ruling

- **SourceRef:**
  `execution/_Coordination/ASSESSMENT_2026-08-02_LOOP_PATTERN_CONVERGENCE.md`
  "Convergence candidates (unranked options, not selections)" and the fourth
  candidate at lines ~118–123; owner sequencing direction recorded verbatim:
  "We're going to attend to this once each dev loop has landed"
- **SourceSha:**
  `0db93f986795763093e6e54d19f22570f3c6d34fe7a3764dad417270375728ae`
- **Concern:** Four named governance-to-code convergence options — shared
  committed-HEAD plan-loader; per-loop-parameterized receipt validator
  extended to root/PEC; single reliance-hold script; generalized
  `list_deliverable_status.py` + DAG-surface materialization — remain
  unranked and unselected. The assessment's stated re-entry condition
  (dev-loop fan-in landed) and its in-flight guard are both now satisfied/
  spent (PRs #491–#502 merged).
- **Domain lenses:** Prioritization; Planning; Approval; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` (owner ranks, selects, or
  declines); selected options then close under their own instruments.
  Triage note: options overlap CH-20260803-02/-04 (validator quality genus) —
  the owner may collapse them into one shared-validator workstream.
- **Existing-row overlap:** none.
- **Route posture:** adoption acts are foreign (PEC, App, Piping) and would be
  routed on selection.

### CH-20260803-10 — Public-export derivatives knowingly stale against the applied Root PRD

- **SourceRef:**
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/PRD_Application_Export_Disposition_2026-08-03.md`
  "Derivative observation and disposition"
  ("DEFERRED — REGENERATION REQUIRED AT NEXT AUTHORIZED EXPORT RELEASE")
- **SourceSha:**
  `a5de5ae0ef0cd3a1d17b9c9527eebdeacd6e68fe7b981e2b632b84c20d07ead6`
- **Concern:** The H3 lane applied the SCA-003 basis reconciliation to
  `docs/PRD_ROOT.md` (Revision 8) but export derivatives were not
  regenerated: `exports/chirality-app/export-manifest.csv` still records the
  pre-application size/SHA for `docs/PRD_ROOT.md`. The deferral is recorded
  with a trigger but has no carrier, so no instrument tracks that a governed
  manifest currently asserts a superseded hash.
- **Domain lenses:** Deliverables; Checking.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` at the next authorized
  export release (staging tree + manifest + report regenerated), or
  `INFORMATIONAL_NO_ACTION` if the owner rules the deferral record itself a
  sufficient carrier.
- **Existing-row overlap:** none (closed TM-ROOT-052 concerned the
  README/profile description, a different defect).

### CH-20260803-11 — DEL-02-06 owner-selection gate: deferral precondition now satisfied, no register carrier

- **SourceRef:**
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/accepted_inputs/OPEN_ITEMS.csv`
  (16 rows, 15 `UNRESOLVED`); gate text in
  `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/HANDOFF_STATE.md`
  and Receipt 88 ("a dedicated owner selection session against committed main
  after PR #491 merges")
- **SourceSha:**
  `26f967b5773dd0f0c1a91f6378b7037cf6ba253288b1902652764fbfc27dc351`
- **Concern:** Sixteen accepted-packet open items (TBD/OD6), the D1–D9
  decision slate, the affected-client census (PEC `UNRESOLVED`), and the
  compatibility-delta proposal all hang on one deferred owner-selection gate.
  The deferral's precondition — PR #491 merged to main — is now satisfied
  (merge `d7acbbff8` verified in ancestry), and the deferral commitment is
  carried only in a run-record handoff and receipts, with no register row.
  The slate contents themselves are fenced at their named owner gate and are
  NOT harvested here; only the gate-carrier question is presented.
- **Domain lenses:** Planning; Approval; Decisions.
- **Proposed disposition:** ONE row (not sixteen), closing
  `RESOLVED_BY_DECISION` when the dedicated selection session rules the set —
  or, alternative the owner may prefer: no new row, with TM-ROOT-108's empty
  `Trigger` updated to the Receipt 88 text (§5, M3) as the honest carrier.
- **Existing-row overlap:** heavy by design — TM-ROOT-035 (trigger is
  DEL-02-06 activation), -046 (census boundary ↔ FRESH-OPEN-005/-009/-011/
  -013), -105 (TBD-001..003/-007/-008/-015/-016), -108 (routed into this
  lane), -109 (TBD-001/-015). A single carrier row avoids duplicating four
  existing rows sixteen times.

### CH-20260803-12 — Pi adapter implementation-identity collision (PI082-F07, BLOCKER)

- **SourceRef:**
  `execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/FINDINGS.csv`
  row `PI082-F07` (Status OPEN, RecommendedOwner "Root owner and
  SCOPE_CHANGE")
- **SourceSha:**
  `10c9e70b1db6e456d287c46e02578087958c89da763e829919823ddc3d0917d0`
- **Concern:** Root's `runtime/packages/engine-pi-omlx` and App's
  `pi-agent-engine-adapter` declare the same pi/omlx package/version
  descriptor while exposing different implementations; the Desktop registers
  the App-local one and the identity schema cannot distinguish implementation
  family, making evidence produced under the descriptor unattributable. The
  2026-08-03 ruling selected G1-B for validation only, expressly not final
  architecture; PIA-U30 (Root-side identity proof) is blocked on this.
- **Domain lenses:** Deliverables; Approval; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` (owner binds a canonical
  implementation identity + collision-proof schema) — or `DUPLICATE` of
  TM-ROOT-106 if the owner rules the identity question inseparable from the
  version question. Presented as a distinct BLOCKER with a distinct remedy;
  the owner may well fold it.
- **Existing-row overlap:** TM-ROOT-106 (Pi version concordance) lists
  canonical adapter identity among unmet closure conditions; TM-ROOT-035,
  -107, -109 adjacent.
- **Route posture:** downstream App rerun (PIA-U22/U23, D-APP-72 successor)
  once identity is bound — via the already-routed G1-B handoff, not a new
  notice.

### CH-20260803-13 — Electron authority drift: D-APP-72 names 43.1.1, executable manifest pins 43.2.0 (PI082-F09)

- **SourceRef:** same `FINDINGS.csv`, row `PI082-F09` (Status OPEN, HIGH);
  the routed G1-B handoff expressly excludes "D-APP-72/SCA-APP-002 Pi
  `0.80.10` or Electron `43.1.1` supersession" from what it performs
- **SourceSha:** `10c9e70b1db6e456d287c46e02578087958c89da763e829919823ddc3d0917d0`
- **Concern:** No successor authority exists for the Electron prerequisite,
  and unlike the five App-owned findings this drift is currently carried by
  no instrument in either loop.
- **Domain lenses:** Deliverables; Approval; Checking.
- **Proposed disposition:** `RESOLVED_BY_DECISION` if the owner folds it into
  the Pi successor fact set (TM-ROOT-106 lane); or decline the row and route
  it to App as part of the CH-20260803-01/-06 response notice.
- **Existing-row overlap:** TM-ROOT-106 by neighborhood (version-authority
  genus), not by named substance.

## 4. Screened candidates — no new Root row recommended

### S1 — Piping DAG pointer form vs. status-tool argument form (SESSION_RECON marker 6)

The notice files this under "Shared-tool candidates (root register)", but the
cited tool exists only at
`projects/chirality-piping/tools/coordination/list_deliverable_status.py`
(no root copy; the convergence assessment independently calls it
"project-local"). Piping owns both the tool and `_DAG/_LATEST.md` (SHA-256
`04f24cd88d16b38d6da00ae2dee32f0387381ee41659de2e352cba07127736e3`).
**Proposed:** `INFORMATIONAL_NO_ACTION` at root + routed notice to Piping
(ownership conflict surfaced, not resolved — the owner may instead rule it
root-owned, which would move it to the slate as `RESOLVED_WITH_CHANGE`).

### S2 — SESSION_RECON markers 7–8 (loop-owned)

Marker 7: App-dev and Piping `LOOP_INIT.md` each claim verbatim reusability
then hardcode their own loop directory — owned by those loops. Marker 8:
`init/piping-resume-one-time.md` residuals, including one substantive
unresolved evidence-loss question (six untracked artifact sets in a
now-deleted worktree, restoration unrecorded) — owned by Piping.
**Proposed:** `INFORMATIONAL_NO_ACTION` at root; a routed notice to Piping
carrying marker 8's evidence-loss question is recommended for the owner's
consideration (marker 7 is cosmetic and both loops' TM services already scan
these surfaces).

### S3 — App-owned Pi evidence findings PI082-F03/F04/F05/F08

Clean-install, packaged production-route proof, packaged-closure notices, and
0.82.0 oMLX-proof staleness map one-to-one onto PIA-U20/U21/U22/U24/U25 in
`projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-03_ROOT_PI_G1B_APP_WORK_ACCEPTANCE_HANDOFF.md`
(all `PROPOSED / NOT ACCEPTED / NOT DISPATCHED`). Already routed; App-owned.
**Proposed:** `INFORMATIONAL_NO_ACTION`; root visibility runs through App's
disposition of that handoff.

### S4 — PI082-F01/F10 (Pi version conflict; approval boundary)

Substantively the standing concern of `TM-ROOT-106` (F10 names the row
verbatim). **Proposed:** no new row; record
`execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/FINDINGS.csv`
as additional evidence on TM-ROOT-106 at its eventual closure. PI082-F02/F06
are `PASS` records, not open items.

### S5 — TM-PIP-026 scanner-repair closure notice

Expressly asks Root to create no row; the defect was repaired root-side at
PR #482 with a regression fixture, and Piping closed `TM-PIP-026`
`RESOLVED_WITH_CHANGE`. Pre-boundary (`c07ea11b1`) and never previously
recorded as assessed. **Proposed:** `INFORMATIONAL_NO_ACTION`; this report is
the assessment of record.

### S6 — Notice-ledger instrument gap (structural)

The `notice-not-in-ledger` scan class is structurally unbounded: the only
ledger is the one-off 2026-07-28 remediation CSV, so every notice since is
by construction "not in a ledger" (29 raw at the prior harvest → 45 now).
An instrument-design question, not a defect in any cited source.
**Proposed:** `INFORMATIONAL_NO_ACTION` unless the owner initiates an
instrument decision.

## 5. Existing-row maintenance and staleness observations — not promotion candidates

No edit is authorized by this report; each line is separately ruled.

| # | Row(s) | Observation | Proposed if separately ruled | Evidence |
|---|---|---|---|---|
| M1 | `TM-ROOT-105`, `TM-ROOT-109` (DEFERRED) | Recorded trigger has FIRED: the Piping runtime-surface response landed (commit `c394365ca`) and reciprocally cites both row IDs; it supplies the generic-primitive set (§4) and comparison-basis identity boundary (§6) the rows await. No Root surface records receipt. Downstream: App D-APP-90 lane, TM-APP-027/-028 wait on this workstream | DEFERRED→OPEN with the response as trigger evidence; optional routed acknowledgment to Piping | `projects/chirality-piping/execution/_Coordination/COORDINATION_RESPONSE_2026-08-02_PIPING_RUNTIME_SURFACE_NEEDS.md`, SHA-256 `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7` |
| M2 | `TM-ROOT-110` (OPEN) | Closure evidence now exists on committed main: PR #491 merged (`d7acbbff8` in ancestry) and the diff-mode G4 check runs in CI at `.github/workflows/governance-harness.yml:100-110` (verified on HEAD); Receipt 87 records the hosted pass | `RESOLVED_WITH_CHANGE` citing the workflow lines + Receipt 87 | workflow bytes at basis; `execution/_Coordination/LOOP_RECEIPTS.md` SHA-256 `8c72645cc01f4c9c1a51dd3a48e27b45fd3b3e49c3f81fc5a2591ef58bac5500` |
| M3 | `TM-ROOT-108` (OPEN, empty `Trigger`) | Its routed DEL-02-06 lane is owner-deferred with a named trigger (Receipt 88: "a dedicated owner selection session against committed main after PR #491 merges"); the row's Trigger field is empty | Row maintenance: adopt the owner's exact trigger text (interacts with CH-20260803-11 alternative) | Receipt 88, same LOOP_RECEIPTS SHA |
| M4 | `TM-ROOT-107` (OPEN) | SCA-003 closed `CLOSED_ZERO_ACTION_NO_DECOMPOSITION_CHANGE` — it did NOT assess the D-APP-84 / product-delivery impact this row names; its ScaRef must not be auto-populated with SCA-003 | No action (guard against false closure) | `execution/_ScopeChange/SCA-003_2026-08-02_2212/CLOSURE_RECORD_2026-08-03_ZERO_ACTION_NO_CHANGE.md` |
| M5 | 20 packet-question rows (`TM-ROOT-055..075` block + `-101`) | All 21 federation `REMOTE_CLOSED_LOCAL_OPEN` pairs are App↔Root; 20 share one gating condition — TM-ROOT-098 closure + App packet-residue review — which is fully satisfied (TM-ROOT-098 CLOSED; every App counterpart dispositioned). Prepared vehicle exists: `DRAFT_HANDOFF_2026-08-02_APP_PACKET_RESIDUE_DEFERRAL_REVIEW.md` | Step-3 deferral review classifies each (expected `TRIGGER_FIRED` → mostly `DUPLICATE`-to-survivor or `RESOLVED_BY_DECISION`) | App register SHA-256 `bd863e1a873b5e8bafc83f0ae8aa06569d89a1100650ee43e57fcfc30581c1de`; federation projection |
| M6 | (surface, not a row) | `execution/_Coordination/HANDOFF_STATE.md` §1 register counts are stale (says 36 live / 4 OPEN; actual 37 / 5 after TM-ROOT-111) | Ordinary next handoff refresh by the loop — outside TM write scope | register bytes at basis |

## 6. Routed-response draft preparation and gate

No routed draft is written in this tranche; none can truthfully carry a Root
`ActionItemID` before promotion rulings exist. Preplanned drafts, written only
inside the Root closeout tranche on the owner's ruling:

| Triggering ruling | Addressee / destination | Required reciprocal citations |
|---|---|---|
| CH-20260803-01 promoted | App loop — `projects/chirality-app-dev/execution/_Coordination/` | inbound notice SHA-256 `4f52ed…656`; new `TM-ROOT-*` ID; Root reproduction/disproof plan or evidence refs |
| CH-20260803-02 dispositioned | Piping loop — `projects/chirality-piping/execution/_Coordination/` | inbound notice SHA-256 `712949…a9c`; new `TM-ROOT-*` ID (the notice awaits it); repair/decline evidence |
| CH-20260803-06 ruled (either way) | App loop | SESSION_RECON SHA-256 `05e6ee…901`; App register SHA-256 `bd863e…1de`; the named Root row App should re-cite |
| S1/S2 routed as ruled | Piping loop | SESSION_RECON SHA-256; marker quotes; no Root row ID required (informational routing) |
| M1 acknowledgment (optional) | Piping loop | response SHA-256 `e38c56…5e7`; TM-ROOT-105/-109 status change evidence |

## 7. Owner ruling requested

1. Promote or decline **CH-20260803-01 … -13** (each independently; -11
   offers a no-new-row alternative via M3; -12/-13 offer fold-into-106
   alternatives).
2. Accept or amend the no-new-row screenings **S1 … S6** (S1 carries a
   contested-ownership choice; S2 carries an optional Piping routing).
3. Separately authorize any of **M1 … M5** maintenance dispositions; none is
   implied by a promotion ruling.
4. Authorize the closeout drafts per §6 after new row IDs exist. Shipping
   remains under the owner's closeout gate.
