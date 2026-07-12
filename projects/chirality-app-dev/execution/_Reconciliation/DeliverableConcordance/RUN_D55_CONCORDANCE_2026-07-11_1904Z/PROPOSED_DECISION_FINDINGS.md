# PROPOSED_DECISION_FINDINGS — R4 draft decision packets

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, method pinned at plan revision `551f84ef6`).
Author: R3 synthesis agent R3-B (fable). Source state: frontend/ @ `fac46e33f` (byte-identical through main `60db8de85` at R3 dispatch); behavioral evidence bound to GATE-TRANSCRIPT(W1@fac46e33f) — typecheck 0, Vitest 667 passed / 4 skipped.

> **Epistemic status: every packet in this file is a DRAFT PROPOSAL awaiting the R4 human
> decision gate.** Nothing here is a ruling; no disposition is re-adjudicated; no lifecycle
> transition is proposed for execution; recommended options are minimal-change proposals only
> (plan §8 R4). Unruled items remain explicit and do not block unrelated repairs. All
> dispositions cited are settled R2 agent judgments from the wave ledgers
> (`CLAIM_CONCORDANCE.csv`, fan-in verified per `R2_WAVES/PKG-*/_VERIFICATION.md`).

Packets are grouped by the six plan §8 R4 decision types. Companion artifact:
`PROPOSED_DELIVERABLE_UPDATES.csv` (proposal-only repair rows, each `GatedBy` a packet below).
NEW-PACKET sweep reconciliation: §7 at the end of this file.

---

## 1. Scope adoption or retirement

### R4-P01 — Adopt or record: API-key remove/reveal management UI
- **Decision type:** scope adoption or retirement.
- **Question:** the settings surface implements remove-stored-key and reveal/hide controls no DEL-02-05 requirement names.
- **Evidence:** `frontend/src/components/settings/api-key-settings.tsx` lines 110-129 (handleRemove → bridge.remove), 224-232 (Remove Stored Key rendered only for source==='ui'), 145-147/193-214 (reveal/hide); ledger DEL-02-05 DEL-02-05-UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED); NormativeSource NONE_FOUND.
- **Options:** (A) adopt the controls into a new DEL-02-05 requirement (with test obligation per the D-APP-36 bar); (B) record them as deliberate unrequired convenience UI in the kit's exclusions; (C) do nothing (row stays IMPLEMENTED_UNDOCUMENTED).
- **Affected claims/deliverables:** DEL-02-05 DEL-02-05-UNMAPPED-1.
- **Downstream:** A adds a verification obligation; B closes the row with a kit-text note; C leaves a standing unmapped surface in every future concordance pass.
- **Recommended (minimal change):** B — record as deliberate convenience UI; no code change, one kit-text note.

### R4-P02 — Adopt or record: whole-product secret-scan proof command
- **Decision type:** scope adoption or retirement.
- **Evidence:** `frontend/scripts/scan-secret-evidence.mjs`; `frontend/package.json` line 30 wiring; ledger DEL-05-03 UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED); scans broader secret shapes than the configured-API-key runtime contract.
- **Options:** (A) adopt into a DEL-05-03 requirement; (B) adopt into a PKG-09 validation requirement (it is a proof command, not runtime redaction); (C) record as deliberate unrequired defense-in-depth; (D) do nothing.
- **Affected claims/deliverables:** DEL-05-03 UNMAPPED-2; interacts with R4-P46 (the gated configured-secret registry item DEL-05-03 REMAINING-1).
- **Downstream:** A/B create a maintenance obligation for the scanner's secret-shape list; C leaves the broader-than-contract scan un-owned but documented.
- **Recommended (minimal change):** C — record as defense-in-depth in the DEL-05-03 kit, cross-referencing PKG-09 validation as the surface where a future owner could formalize it.

### R4-P03 — Adopt or record: `desktop:pack` app-directory packaging path
- **Decision type:** scope adoption or retirement.
- **Evidence:** `frontend/package.json` scripts.desktop:pack line 32; documented in `docs/BUILD_AND_RELEASE.md` lines 62, 117, 129 as a live packaging-review command (W4 fan-in enrichment, `R2_WAVES/PKG-09/_VERIFICATION.md` §6.4); ledger DEL-09-04 UNMAPPED-1; DEL-09-04 Specification names only `desktop:dist` (REQ-002).
- **Options:** (A) adopt `desktop:pack --dir` into DEL-09-04 requirements (it is the layout the packaged probes and the D-APP-18 live proof exercise); (B) record as deliberate unrequired tooling; (C) do nothing.
- **Affected claims/deliverables:** DEL-09-04 UNMAPPED-1; feeds R4-P49 (packaging evidence).
- **Downstream:** A makes the packaged-probe layout an owned requirement, strengthening the R4-P49 evidence story; B leaves the probes exercising an unrequired path.
- **Recommended (minimal change):** A — adopt; the gap is deliverable/requirement ownership, not documentation (W4 finding), and the surface is already documented and probe-exercised.

### R4-P04 — Adopt or record: `hook.progress` event category
- **Decision type:** scope adoption or retirement.
- **Evidence:** `frontend/packages/harness-contract/src/event-schema.ts` line 26 (hook.progress registered); `frontend/src/lib/harness/sdk-message-mapper.ts` lines 986-1001 (adapter mapping); DEL-06-06 Specification REQ-004 names only hook.started/hook.completed; verifier-confirmed ZERO test coverage for hook.progress (PKG-06 fan-in). Ledger DEL-06-06 UNMAPPED-1.
- **Options:** (A) extend Specification.md REQ-004's hook-category list to include hook.progress plus a coverage obligation; (B) record it as a deliberate unrequired mirror category; (C) do nothing.
- **Affected claims/deliverables:** DEL-06-06 UNMAPPED-1.
- **Downstream:** A creates a test-coverage obligation (currently zero); B leaves an emitted-but-unrequired event category.
- **Recommended (minimal change):** A — one kit line plus one test; the category is already registered and emitted, and zero coverage on an emitted event is the riskier resting state.

### R4-P05 — Retire or adapt: repo-root `desktop-release-template.yml` build-windows job
- **Decision type:** scope adoption or retirement (retirement candidate).
- **Evidence:** W4 cross-package finding (`R2_WAVES/PKG-09/_VERIFICATION.md` §6.3): the template is a live executable surface (`on: push tags v*` + `workflow_dispatch`) containing a `build-windows` job producing Windows NSIS artifacts — in tension with K-RELEASE-1's macOS-only posture, DEL-09-04-REQ-010, and DEL-09-05-EXC-005; additionally its paths cannot succeed against this tree (`working-directory: frontend` at repo root; `frontend/dist-electron/*` vs actual `dist`) — an unadapted template, not an operating release path.
- **Options:** (A) retire/remove the template from the repo root; (B) adapt it to the ruled macOS-only posture and this repo's layout; (C) neutralize the triggers (disable `push tags`/`workflow_dispatch`) and keep it as reference text; (D) do nothing (live executable surface claiming a non-macOS target remains).
- **Affected claims/deliverables:** DEL-09-04 (REQ-010 posture), DEL-09-05 (EXC-005; CI ownership); no ledger row carries it (cross-package fan-in finding).
- **Downstream:** A/C remove a misfiring release trigger risk; B expands release scope only if the owner separately rules Windows in — otherwise B without a Windows ruling contradicts K-RELEASE-1. Ownership of the fix (DEL-09-04 packaging vs DEL-09-05 CI) rides with the chosen option.
- **Recommended (minimal change):** C — neutralize triggers, keep text; no scope ruling implied either way, and the K-RELEASE-1 tension is removed.

---

## 2. Product-behavior ruling

### R4-P06 — Corpus-amendment packet family (ONE governed D-APP-38 bump/apply)
- **Decision type:** product-behavior ruling (transcription of already-ruled postures into the authority corpus; two sub-items carry genuine either-way choices).
- **Consolidation:** per PKG-10 escalation §4.1, the DEL-08-02 six (W3), the W1 PKG-02 shared corpus packet (flag 4), and escalation-queue item 6. All sub-items ride ONE governed authority-doc amendment + corpus version bump; kit-text refreshes that transcribe these lines are separate update rows gated by this packet. MR-11 governs the interim: rulings stand over untranscribed corpus wording.
- **Sub-items:**
  - **(a) Loop-first routing wording** — docs/PRD.md §7.2 (lines 303/306/312), FR-001 (line 473), FR-005 (line 477: three-pane), FR-008 (line 485); docs/TYPES.md §4.1 (lines 141/143 NORMATIVE/EVALUATIVE "open WORKBENCH") — superseded by ruled D-APP-28/30/31/32. Claims: DEL-02-01 REQ-002/REQ-007/REQ-008, DEL-02-02 REQ-002, DEL-08-02 REQ-008/REQ-009. Recommended: amend to the ruled loop-first posture (transcription only).
  - **(b) Persona alias/matrix vocabulary** — docs/TYPES.md §3.4 (lines 123-131) and §4.3 (lines 154-160); docs/PRD.md FR-026 (line 513). AGGREGATE→AGGREGATION removal (DEL-08-02 REQ-003, ruled D-APP-28/24); DEPENDENCIES→EVALUATION alias addition (DEL-08-02 ACC-001, live at persona-resolution.ts line 38 citing D-APP-23); the three-cell roster divergence (DEL-02-01 UNMAPPED-1: NORMATIVE/REVIEWING=REVIEW, EVALUATIVE/REVIEWING=RESEARCH vs TYPES AGGREGATE/RECONCILING). Recommended: amend TYPES/PRD to the live ruled roster.
  - **(c) RECONCILING→RESEARCH re-pointing (either-way)** — DEL-08-02 REQ-004 (IMPLEMENTED_DIFFERENTLY, W3 owner-resolved contest): the RATIFIED corpus requires RECONCILING→RECONCILIATION and RECONCILIATION is a valid Type-1 persona (`agents/AGENT_RECONCILIATION.md` Type-1 since repo origin), yet the live cell/alias were re-pointed to RESEARCH by the ADQ-12 kit rewrite with no bridging register ruling. Option 1: amend corpus to adopt the re-pointing. Option 2: restore the RECONCILING→RECONCILIATION alias in code. Option 3: do nothing (corpus and code stay divergent). Recommended (minimal change): Option 1 — adopt the live behavior into the corpus; also correct the false Datasheet line 26 rationale (kit repair, same gate). Deciding facts recorded in `R2_WAVES/PKG-08/_VERIFICATION.md` §2 and the DEL-08-02 notes.
  - **(d) Persona default (either-way)** — DEL-08-02 REQ-014: docs/SPEC.md §13.1 line 715 says fallback "HELP_HUMAN or configured default"; live default is the hardcoded WORKING_ITEMS (`persona-resolution.ts` line 12), neither configured nor HELP_HUMAN. Option 1: amend SPEC line 715 to the hardcoded WORKING_ITEMS default. Option 2: implement a configured default / HELP_HUMAN fallback. Option 3: do nothing. Recommended (minimal change): Option 1; Datasheet line 31 transcription refresh rides in the same tranche.
  - **(e) Domain staged-live posture** — docs/SPEC.md §18 (lines 875-889), docs/TYPES.md §11 forward note ("domain_* stays reserved"), docs/PLAN.md R7 (lines 277-300), docs/PRD.md KG-016 (line 1514) and §8.17 still flatly assert domain surfaces must not be implemented — superseded for the staged read/propose/validate subset by ruled D-APP-49/50/51/52 (four independent NEW-PACKET routes in PKG-10, merged here per `R2_WAVES/PKG-10/_VERIFICATION.md` §4.1). Claims: DEL-10-01 REQ-002/ACC-001, DEL-10-04 REQ-001, DEL-10-05 REQ-007 (+ DEL-10-03 EXC-002 kit side). Recommended: transcribe the ruled staged-live posture (read/propose/validate live; apply, endpoints, path hooks remain future/gated).
  - **(f) Provider-expansion BR wording** — DEL-01-04 ACC-003: the proposed provider-expansion boundary-register row must be worded against the post-D-APP-44 F1 posture; interacts with DEL-04-02 ownership (W5 escalation §6.6). Recommended: word the BR row per D-APP-44 F1 in the same amendment.
  - **(g) SPEC §10.2 TurnInput enumeration** — corpus wording vs implemented port shape (PKG-03 flag §3.3, pairs with DEL-03-01 REQ-005). Recommended: align §10.2's enumeration with the implemented TurnInput shape (transcription; if the owner prefers the spec shape, route to R4-P24 instead).
- **Options (family-level):** (A) one governed D-APP-38 corpus bump applying sub-items a-g with the per-item recommendations; (B) apply the pure transcriptions (a, b, e, f, g) and rule c/d separately; (C) do nothing — corpus stays stale, MR-11 keeps rulings operative but every future concordance re-detects these rows.
- **Affected claims:** DEL-02-01 REQ-002/REQ-007/REQ-008/UNMAPPED-1; DEL-02-02 REQ-002; DEL-08-02 REQ-003/REQ-004/REQ-008/REQ-009/REQ-014/ACC-001; DEL-10-01 REQ-002/ACC-001; DEL-10-04 REQ-001; DEL-10-05 REQ-007; DEL-01-04 ACC-003; DEL-03-01 REQ-005 (pairing). Affected deliverables: DEL-01-04, DEL-02-01, DEL-02-02, DEL-03-01, DEL-08-02, DEL-10-01, DEL-10-03, DEL-10-04, DEL-10-05.
- **Downstream:** gates the largest kit-refresh tranche in `PROPOSED_DELIVERABLE_UPDATES.csv`; until ruled, all dependent kit texts stay frozen (MR-11 interim).
- **Recommended (minimal change):** A — one bump, per-item minimal options as stated (c→Option 1, d→Option 1).

### R4-P07 — Toolkit mode/persona controls (one underlying gap)
- **Decision type:** product-behavior ruling.
- **Evidence:** DEL-02-04 REQ-003 + REQ-009 (both PARTIALLY_IMPLEMENTED; W1 fan-in: "one underlying gap … one product decision, not two"); `operator-toolkit-panel.tsx` lines 64-143 exposes model/tools/maxTurns/subagentGovernance but NO mode or persona control; `sdk-options-builder.ts` lines 40-52, 111-119 (mode→permission-posture enforcement already implemented); PRD FR-041 requirement-vs-acceptance wording split at docs/PRD.md line 543 is the exact fact to adjudicate.
- **Options:** (A) require Toolkit-surfaced mode and persona controls (implement UI); (B) amend Specification.md line 29 (REQ-003) and line 35 (REQ-009) to state mode/persona are supplied by the persona picker and session controls; (C) do nothing.
- **Affected claims/deliverables:** DEL-02-04 REQ-003, REQ-009.
- **Downstream:** A is a product feature tranche; B is kit repair plus possibly a PRD FR-041/FR-044 acceptance-text touch (joins R4-P06 if the PRD line changes).
- **Recommended (minimal change):** B — the enforcement substance exists; only the control's location diverges.

### R4-P08 — Medium-band tool-result preview policy
- **Decision type:** product-behavior ruling.
- **Evidence:** DEL-05-05 REQ-004 (PARTIALLY_IMPLEMENTED): `tool-evidence.ts` lines 92-107 classify within-inline / requires-artifact-overflow / exceeds-artifact-budget with no distinct medium band; D-APP-42 left thresholds/preview length unchanged (Option C logged as "a deferred future enhancement — not a correctness gap"); cross-referenced verification-side row DEL-05-03 R13 (PKG-05 fan-in §3.2: one underlying gap, DEL-05-05 owns the packet).
- **Options:** (A) require a distinct bounded medium-band preview (implement); (B) amend REQ-004 to ratify current inline-to-artifact behavior as the accepted policy; (C) do nothing (defer again, explicitly).
- **Affected claims/deliverables:** DEL-05-05 REQ-004 (with REQ-010/014 context rows), DEL-05-03 R13.
- **Downstream:** A is product work with output-budget policy implications; B/C close or park the PARTIAL.
- **Recommended (minimal change):** C — record an explicit continued deferral anchored to D-APP-42's own "deferred future enhancement" language; revisit under an output-budget policy decision.

### R4-P09 — Bash timeout numeric policy ratification
- **Decision type:** product-behavior ruling.
- **Evidence:** DEL-06-05 UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED): `tool-shell-policy.ts` lines 8-9 (DEFAULT_BASH_TIMEOUT_MS=120000, MAX_BASH_TIMEOUT_MS=600000), enforced lines 194-218 and 346-352; NO accessible source sets a Bash-specific numeric limit (Specification REQ-006 line 34 says TBD); Guidance conflict DEL-06-05-TIMEOUT-001 open.
- **Options:** (A) ratify 120000/600000 ms as accepted policy (amend REQ-006, resolve TIMEOUT-001); (B) record the values as deliberate unadopted implementation defaults; (C) rule different values (product change); (D) do nothing.
- **Affected claims/deliverables:** DEL-06-05 UNMAPPED-1.
- **Downstream:** A makes the numbers normative (future changes need rulings); B keeps them free implementation detail.
- **Recommended (minimal change):** A — the values are live, enforced, and test-pinned; ratification closes the Guidance conflict with one kit edit.

### R4-P10 — Stub-adapter terminal-persistence parity (single packet; do not double-count)
- **Decision type:** product-behavior ruling.
- **Evidence:** DEL-03-02 REQ-009 + DEL-03-04 REQ-006 (both PARTIALLY_IMPLEMENTED; PKG-03 fan-in §3.1 mandates ONE packet): agentSdk and anthropic adapters persist terminal HarnessEvents; the stub adapter's terminal outcomes are UI-visible but not persisted (grep appendHarnessEvent absent in `frontend/src/lib/harness/agent-sdk-manager.ts` at 4c8ed8907); K-EVENT-3, PRD FR-022, D-APP-40.
- **Options:** (A) add stub terminal-persistence parity (small product change); (B) document the stub as a deterministic UI-only test adapter exclusion (kit edit in both deliverables); (C) do nothing.
- **Affected claims/deliverables:** DEL-03-02 REQ-009; DEL-03-04 REQ-006.
- **Downstream:** A makes event-stream evidence uniform across adapters; B narrows K-EVENT-3's applicability wording for the stub.
- **Recommended (minimal change):** B — the stub is a test adapter; a documented exclusion resolves both rows without product change. (If the owner values replay-evidence uniformity, A is small and bounded.)

---

## 3. Acceptance-criteria ruling

### R4-P11 — Ratify method rule 1a: superseding-note test for stale assessments
- **Decision type:** acceptance-criteria ruling (run-method ratification).
- **Rule as applied:** an assessment whose conclusions are overtaken is STALE_ASSESSMENT only when NO superseding note recasts the stale conclusion as historical; where a superseding note exists (exactly two corpus-wide: DEL-07-02 ADQ-06, DEL-07-03 ADQ-07 — owner-verified grep), rows are ALIGNED with AssessmentEvidence=OVERTAKEN.
- **Evidence:** W3 DEL-07-03 8-row class flip (`R2_WAVES/PKG-07/_VERIFICATION.md` §2/§3.1); applied consistently through W5/W6/W7 (W7 DEL-00-02 REQ-005/REQ-010 refutations harmonized to it, `R2_WAVES/PKG-00/_VERIFICATION.md` §2); noteless precedents R0 DEL-02-01, W2 DEL-04-03.
- **Options:** (A) ratify run-wide (the test becomes the acceptance bar for assessment-staleness rows and gates tranche R4-P43); (B) reject (would reopen the W3/W7 flips — NOT recommended; those are settled agent judgments this packet does not re-adjudicate, only the forward rule is at issue); (C) do nothing (rule stays run-local convention).
- **Affected claims:** all STALE_ASSESSMENT rows (23 run-wide) and the ALIGNED+OVERTAKEN family. **Downstream:** gates R4-P43.
- **Recommended (minimal change):** A.

### R4-P12 — Ratify method rule 1b: STALE_ASSESSMENT vs STALE_SPECIFICATION split
- **Decision type:** acceptance-criteria ruling (run-method ratification).
- **Rule as applied:** assessment-only staleness → STALE_ASSESSMENT; any kit or register surface carrying the stale wording as current → STALE_SPECIFICATION.
- **Evidence:** W5 escalation §6.2 (would have mechanically decided DEL-01-02 RBR-014; consistent with all W5 outcomes); applied W5/W6/W7-consistently.
- **Options:** (A) ratify run-wide; (B) reject; (C) do nothing.
- **Affected claims:** the disposition boundary across the 94 STALE_SPECIFICATION / 23 STALE_ASSESSMENT rows. **Downstream:** stabilizes classification for R6 backcheck and future runs.
- **Recommended (minimal change):** A.

### R4-P13 — Ratify method rule 1c: dated-note discipline
- **Decision type:** acceptance-criteria ruling (run-method ratification).
- **Rule as applied:** prose in dated register notes that was true when written (e.g. D53A-era "remains CHECKING", pre-v6 SHAs inside dated self-qualified notes) is NOT a defect; lagging machine fields ARE (MR-5). Contrast pair: DEL-10-02 DEP-10-02-003 note correctly uncoded vs DEL-10-04 REGISTER-2 correctly coded (`R2_WAVES/PKG-10/_VERIFICATION.md` §2, §4.2); DEL-09-03's dated D-APP-53 correction note cited as the model practice (W4 §4).
- **Options:** (A) ratify run-wide; (B) reject (dated notes would need annotation sweeps — large, low-value churn); (C) do nothing.
- **Affected claims:** register-defect rows run-wide (53 REMAINING_STATE_MISMATCH). **Downstream:** bounds tranches R4-P40/P41/P45 to machine-field repairs.
- **Recommended (minimal change):** A.

### R4-P14 — Ratify method rule: corpus-wide accepted-mapping test (fold: decomposition-of-record + TYPES §6.2 question)
- **Decision type:** acceptance-criteria ruling (run-method ratification).
- **Fold rationale:** two escalations are the same rule seen from two sources. (i) W2 PKG-04 flag §3.1: treat decomposition-of-record assignments as accepted mappings when sweeping IMPLEMENTED_UNDOCUMENTED rows (all three W2 refutations failed by testing only deliverable-local mapping); applied at W3 (DEL-07-02 UNMAPPED-1, DEL-08-01 UNMAPPED-1) and W4 (DEL-09-01 UNMAPPED-1). (ii) W3 DEL-07-05 UNMAPPED-001 classification question: does descriptive-normative vocabulary-table wording in docs/TYPES.md (§6.2 line 211 "IMPLEMENTS_NODE … normally one per deliverable") count as an "accepted mapping" under the same test? (`R2_WAVES/PKG-07/_VERIFICATION.md` §2/§4d.)
- **Options:** (A) ratify both prongs (decomposition rows and TYPES vocabulary-table wording are accepted mappings); (B) ratify prong (i) only, requiring explicit requirement/decomposition rows and leaving TYPES tables descriptive; (C) do nothing.
- **Affected claims:** DEL-07-05 UNMAPPED-001 (ALIGNED, owner-adopted Reading B, standing classification question); the IMPLEMENTED_UNDOCUMENTED sweep discipline generally.
- **Downstream:** determines how future concordance passes and packets R4-P27..P34 treat decomposition/TYPES-sourced ownership.
- **Recommended (minimal change):** A — matches the run's actual settled practice, including the owner-adopted DEL-07-05 resolution.

### R4-P15 — Declared-TBD register-defect class harmonization (+ register de-minimis bar)
- **Decision type:** acceptance-criteria ruling.
- **Question:** are "Declared Upstream/Downstream: TBD…" narrative rows register defects, given docs/SPEC.md §5.2 (Declared sections are human-owned declarations, distinct from the extracted register; TBD-by-design — orchestrator-verified)?
- **Evidence:** class-level inter-verifier conflict, full statement `R2_WAVES/PKG-03/_VERIFICATION.md` §3.5 and `R2_WAVES/PKG-06/_VERIFICATION.md` §3.1. PKG-06's two class rows dropped (owners accepted); standing same-class rows NOT reopened mid-wave: DEL-03-02 REGISTER-2, DEL-03-03 REGISTER-1, DEL-04-01 REGISTER-1, DEL-04-02 REGISTER-1, DEL-04-03 REGISTER-1, DEL-05-02 REGISTER-1, plus merged W1 rows DEL-02-02 REGISTER-1 and DEL-02-03 REGISTER-1 (narrowed). Related fold: PKG-05 §3.6 register-defect de-minimis bar inconsistency (DEL-05-01 treated cosmetic label lag as non-defect; DEL-05-05 emitted REGISTER-1 for a comparable lag) — same underlying bar question, folded here.
- **Options:** (A) adopt the SPEC §5.2 reading: pure Declared-TBD rows are NOT defects — the eight standing rows resolve to non-defect at repair time (annotate ledger interpretation via R5 notes, rows themselves stay immutable evidence) and the "no … edges have been extracted yet" placeholder wording is at most cosmetic; set the de-minimis bar to "machine-field falsity or present-tense false prose" (aligns with R4-P13). (B) reject §5.2 reading: keep the eight rows as defects and sweep the placeholder wording corpus-wide. (C) do nothing (class stays split across packages).
- **Affected claims:** the eight standing rows above; DEL-05-05 REGISTER-1 (bar question).
- **Downstream:** determines whether eight register repairs in `PROPOSED_DELIVERABLE_UPDATES.csv` execute or are recorded as no-repair-needed.
- **Recommended (minimal change):** A — §5.2 is the pinned authority text and PKG-06's owners already accepted it; one bar, applied corpus-wide.

### R4-P16 — REF-006 register-lag class harmonization (ledgered-defect vs historical-run-note)
- **Decision type:** acceptance-criteria ruling.
- **Question:** stale, unannotated REF-006 (docs/PRD.md) HASH_MISMATCH-era warnings carried in `_DEPENDENCIES.md`/register surfaces — ledgered defect (PKG-09 treatment: DEL-09-01 REGISTER-2, DEL-09-02 register rows, DEL-09-05 REGISTER-1, DEL-09-06 REGISTER-1, each recording the alternative dated-run-note no-defect reading as a self-flag) vs historical-run-note non-defect (readings preserved in W4 §4; PKG-07 coded its six register rows as REMAINING_STATE_MISMATCH).
- **Evidence:** `R2_WAVES/PKG-09/_VERIFICATION.md` §4 (class found in five of six PKG-09 registers; live shasum `ac35fba4…` = REF-006 MATCH everywhere); `R2_WAVES/PKG-07/_VERIFICATION.md` §3.2; escalation-queue item 3.
- **Options:** (A) harmonize as annotate-only defects: the warnings are repaired by dating/annotating them as resolved history (consistent with R4-P13's machine-field line — a present-tense unannotated warning IS a lagging field); (B) harmonize as non-defects (drop from repair scope; ledger rows stay as evidence); (C) do nothing (two treatments persist).
- **Affected claims:** PKG-07 six REGISTER-1 rows (DEL-07-01..06); PKG-09 REGISTER rows (DEL-09-01 REGISTER-2, DEL-09-02 REGISTER-1, DEL-09-04 REGISTER-1, DEL-09-05 REGISTER-1, DEL-09-06 REGISTER-1); PKG-10 sightings (DEL-10-02 ACC-001, DEL-10-04 REQ-009, DEL-10-05 ACC-001 kit side).
- **Downstream:** gates tranche R4-P40's register half; the kit-text half (STALE_SPECIFICATION rows) is independent and rides D-APP-35's existing refresh authorization.
- **Recommended (minimal change):** A — annotate-only, preserving history; matches the majority treatment and R4-P13.

### R4-P17 — Standing contest: DEL-04-05 RQ-011 (per-class verification bar)
- **Decision type:** acceptance-criteria ruling. **Both readings presented; no winner picked.**
- **Reading A (owner, recorded disposition ALIGNED):** error-classification is a source-level property, fully present in the taxonomy; test-coverage shortfall is RemainingWork, not a disposition change.
- **Reading B (verifier):** the plan §6 behavioral-verification bar applies per error class; 4 of 7 error classes are not test-asserted by name and INSP-03 says PARTIAL → PARTIALLY_IMPLEMENTED.
- **Deciding fact:** whether the §6 behavioral-verification bar applies per-class or per-requirement. (`R2_WAVES/PKG-04/_VERIFICATION.md` §2.)
- **Options:** (A) rule per-requirement (Reading A stands; coverage residual stays in RemainingWork); (B) rule per-class (row's disposition would be revisited in R6 backcheck; adds 4 named-class test obligations); (C) do nothing (contest stands recorded).
- **Affected claims/deliverables:** DEL-04-05 RQ-011; the per-class bar generalizes to any enumerated-class requirement.
- **Recommended (minimal-change option, not a winner):** A is the minimal-change option because it requires no disposition revisit and keeps the coverage gap visible as recorded RemainingWork; the owner should note Reading B's bar question is generic and may deserve a standing method rule either way.

### R4-P18 — Standing contest: DEL-06-02 REGISTER-2 (single-row satisfaction advance)
- **Decision type:** acceptance-criteria ruling. **Both readings presented; no winner picked.**
- **Reading A (discovery agent, recorded disposition REMAINING_STATE_MISMATCH, LOW):** advancing DEP-06-02-011 (REF-006) to SATISFIED while four equally-MATCH sibling rows (DEP-06-02-005..010) stay TBD is internally inconsistent — a defect.
- **Reading B (verifier alternative, per DEL-06-05 sibling treatment):** TBD satisfaction is a legitimate open acceptance state for an IN_PROGRESS deliverable; the single advance is by-design incrementalism.
- **Deciding fact:** whether ADQ-11/D-APP-43 reconciliation scope obligated sibling-row review. (`R2_WAVES/PKG-06/_VERIFICATION.md` §2.)
- **Options:** (A) Reading B ruled → row drops to NOT_A_DEFECT, no repair implied; (B) Reading A ruled → advance the four sibling rows (or revert the one) in a register fix; (C) do nothing.
- **Affected claims/deliverables:** DEL-06-02 REGISTER-2.
- **Recommended (minimal-change option, not a winner):** A is minimal-change (no repair); if the owner holds that D-APP-43 scope obligated sibling review, B is a one-register bounded fix.

### R4-P19 — Standing contest: DEL-07-04 REQ-017 (HUMAN-prefix actor mapping)
- **Decision type:** acceptance-criteria ruling. **Both readings presented; no winner picked.**
- **Reading A (verifier):** the SHALL clause (explicit actor mapping + fail-closed) is met; the requirement's own "exact enum … remains TBD" defers enumeration → ALIGNED.
- **Reading B (owner, recorded disposition PARTIALLY_IMPLEMENTED):** the live mechanism is a prefix wildcard — `normalized.startsWith('HUMAN')` at `frontend/src/lib/lifecycle/transition.ts:69` — so ANY HUMAN*-prefixed actor authorizes human-gate transitions; heuristic prefix matching independently falls short of "explicit" mapping regardless of the enum question.
- **Deciding facts:** recorded in the DEL-07-04 owner notes (`R2_WAVES/PKG-07/`); contest record W3 §2.
- **Options:** (A) rule the prefix mechanism acceptable pending the enum ruling (Reading A; kit notes the TBD); (B) rule "explicit mapping" requires an enumerated actor set (Reading B; bounded code change to an allowlist); (C) do nothing.
- **Affected claims/deliverables:** DEL-07-04 REQ-017; touches K-AUTH-2 fail-closed posture.
- **Recommended (minimal-change option, not a winner):** A is minimal-change; note that B is a small, security-flavored hardening (an actor allowlist) the owner may prefer given the human-gate is the product's core authority boundary.

### R4-P20 — Standing contest: DEL-09-05 REQ-008 (K-VALIDATE-1 packaging enforcement)
- **Decision type:** acceptance-criteria ruling. **Both readings presented; no winner picked.**
- **Reading A (owner, recorded disposition ALIGNED, MEDIUM):** SPEC §19.1 structurally separates the four required checks from a distinct "Packaging:" block; RUNBOOK §6 keeps packaging evidence separate; the deliverable's own Spec mirrors the split.
- **Reading B (verifier):** docs/CONTRACT.md K-VALIDATE-1 line 128 lists `desktop:dist` among required checks for release-significant changes, and no packaging evidence passes at the source state → PARTIALLY_IMPLEMENTED.
- **Deciding question (routed verbatim from W4 §3):** does K-VALIDATE-1's Enforcement list bind packaging into EVERY release-significant acceptance, or only packaging-significant ones?
- **Options:** (A) rule packaging binds only packaging-significant acceptances (Reading A stands; clarify CONTRACT/SPEC wording via a small corpus touch riding R4-P06); (B) rule packaging binds every release-significant acceptance (Reading B; packaging evidence becomes a standing gate — see R4-P49); (C) do nothing.
- **Affected claims/deliverables:** DEL-09-05 REQ-008; interacts with R4-P49 and R4-P23.
- **Recommended (minimal-change option, not a winner):** A is minimal-change; B materially raises the release bar and should be chosen only with R4-P49's evidence plan funded.

### R4-P21 — DEL-08-03 REQ-010: pipeline scan endpoint naming
- **Decision type:** acceptance-criteria ruling.
- **Evidence:** DEL-08-03 REQ-010 (IMPLEMENTED_DIFFERENTLY, W3-upheld): pipeline scan consumes `/api/project/deliverables` (docs/SPEC.md line 868), not the spec-named `/api/working-root/scope` (line 867); both are SPEC §17.2 active-root surfaces — the substantive anti-hard-coding intent holds.
- **Options:** (A) update Specification.md line 36 and Datasheet.md line 44 to name `/api/project/deliverables` (kit repair); (B) route the pipeline scan through `/api/working-root/scope` (code change); (C) do nothing.
- **Affected claims/deliverables:** DEL-08-03 REQ-010.
- **Recommended (minimal change):** A.

### R4-P22 — DEL-01-04 REQ-011: boundary-register human rulings
- **Decision type:** acceptance-criteria ruling (owner act).
- **Evidence:** DEL-01-04 REQ-011 (ALIGNED): Datasheet.md lines 53-67 carry BR-001..BR-005 with all six required fields; Human Ruling fields deliberately TBD per Guidance; INSP-03 forward recommendation asks for rulings or explicit deferrals; DIRECTIVE §7, CONTRACT §1.7 K-INVENT-1.
- **Options:** (A) record a ruling or explicit deferral per BR row (five micro-decisions, recorded in the register); (B) blanket-defer all five with one dated note; (C) do nothing.
- **Affected claims/deliverables:** DEL-01-04 REQ-011; BR-005 also touches R4-P25/R4-P06(f).
- **Recommended (minimal change):** B for any row the owner is not ready to rule, A for BR-005 (already forced by the DEL-01-04 ACC-002/ACC-003 area).

### R4-P23 — DEL-09-02 RQ-014: Section 9 status enum + gate policy
- **Decision type:** acceptance-criteria ruling.
- **Evidence:** DEL-09-02 RQ-014 (PARTIALLY_IMPLEMENTED): (1) status enum is pass/fail only — pending/skipped/blocked/gated distinction unimplemented (currently moot: all 16 IDs have landed phases); (2) whether Section 9 stays report-only or becomes release-blocking is an unruled validation-policy question (INSP-03 G6 + forward recommendation 1); `validate-harness-section9.mjs` lines 157-212.
- **Options:** (A) keep Section 9 report-only and amend the requirement to say so; enum extension deferred until a non-landed phase exists; (B) make Section 9 release-blocking and implement the full enum; (C) do nothing.
- **Affected claims/deliverables:** DEL-09-02 RQ-014; interacts with R4-P20/R4-P49.
- **Recommended (minimal change):** A.

### R4-P24 — DEL-03-02 TurnEngine architecture acceptance (INSP-03 Gaps 1+2)
- **Decision type:** acceptance-criteria ruling.
- **Evidence:** DEL-03-02 REQ-002 (PARTIALLY_IMPLEMENTED — named-port binding: TurnEngine depends on local IAgentSdkManager, `turn-engine.ts:45-56/68-77`, while packages/harness-contract exports the named AgentEnginePort/RuntimeEngineContract) and REQ-008 (ALIGNED — accepted-turn/terminal persistence split between TurnEngine `turn-engine.ts:301-312` and the SDK adapter; requirement "persist before execution" satisfied either way). SPEC §10.1-10.3, K-ENGINE-1/4, K-EVENT-2.
- **Options:** (A) reconcile PKG-03 docs to accept IAgentSdkManager as the product-owned port and adapter-side persistence as acceptable (kit/doc edits only); (B) refactor TurnEngine to the named AgentEnginePort and move persistence into TurnEngine (code change); (C) split: accept persistence placement (REQ-008) but refactor the port binding (REQ-002); (D) do nothing.
- **Affected claims/deliverables:** DEL-03-02 REQ-002, REQ-008.
- **Recommended (minimal change):** A — both gaps are Medium doc/architecture-naming questions; behavior is verified correct.

### R4-P25 — Minority reading preserved: DEL-01-04 ACC-002 (BR-005 carve-in)
- **Decision type:** acceptance-criteria ruling. **Both readings presented; no winner picked.**
- **Recorded disposition:** STALE_SPECIFICATION (W5 refutation accepted — strict affirmative-permission test: D-APP-50/52 permit the tool surface but contain no text accepting the BR-005 register-wording divergence).
- **Minority reading (preserved per W5 §6.1):** ALIGNED — BR-005's statement carve-in arguably covers the ruled propose/validate/read surface. **Pivot fact:** whether the staged loopback tools count as "domain-engine integration as a shipping feature".
- **Options:** (A) ratify the recorded STALE_SPECIFICATION reading → BR-005 wording repair rides R4-P06(f)/R4-P22; (B) ratify the minority ALIGNED reading → no repair, dated note records the interpretation; (C) do nothing.
- **Affected claims/deliverables:** DEL-01-04 ACC-002.
- **Recommended (minimal-change option, not a winner):** A — it is the fan-in-settled row and its repair is already consolidated in the corpus family; B would leave register wording that the strict permission test found unsupported.

### R4-P26 — Minority reading preserved: DEL-10-03 REMAINING-2 Selectable UNKNOWN→NO
- **Decision type:** acceptance-criteria ruling.
- **Evidence:** the run's only UNKNOWN cell (SelectableUnderCurrentLoop on DEL-10-03 REMAINING-2), justified and fence-compliant (F-APP-3); verifier observation (`R2_WAVES/PKG-10/_VERIFICATION.md` §3/§4.5): the registry's own pinned transportStatus (`domain-profile-registry.ts` lines 70-71) arguably yields NO instead — practically equivalent.
- **Options:** (A) prefer NO on the own-pinned-surface basis (ledger annotation at R5; row stays immutable, note records the preference); (B) keep UNKNOWN as the fence-conservative reading; (C) do nothing.
- **Affected claims/deliverables:** DEL-10-03 REMAINING-2.
- **Recommended (minimal change):** B/C — no correction was required at fan-in; adopt A only if the owner wants zero UNKNOWN cells in the QA report.

---

## 4. Deliverable ownership / mapping

### R4-P27 — Domain staged-surface ownership (ONE packet; four-way partition + two overlap resolutions)
- **Decision type:** deliverable ownership/mapping.
- **Consolidation (per PKG-10 §3/§4.3 and escalation item 5):** the W6 IMPLEMENTED_UNDOCUMENTED rows cleanly partition the unowned ruled staged surface; four rows → ONE packet, not four. Folded in (rationale: same unowned ruled-domain-surface family, single coherent ownership map): DEL-06-02 UNMAPPED-1 (registry roster wording, ruled D-APP-50/52) and DEL-05-03 UNMAPPED-1 (domain-proposal transport credential/cookie hygiene, D-APP-52 lane).
- **The four-way partition:**
  1. **domain-profile.ts type mirror** (+ operation-proposal.ts twin, correctly row-less via DEL-10-03 REQ-001/002/006) — DEL-10-01 UNMAPPED-1. Candidate owner: DEL-10-01.
  2. **profile registry** (`domain-profile-registry.ts`, registration IS the gate) — DEL-10-01 UNMAPPED-2 (dedupe note: same packet as UNMAPPED-1). Candidate owners: DEL-10-01 (identity/registration) vs DEL-10-04 (validation/fixture).
  3. **proposal-tool surface** (`domain-proposal-tools.ts` live propose/refresh/validate) — DEL-10-03 UNMAPPED-1 (its register rows DEP-10-03-007/-008 and Remaining item 2 already lean on it).
  4. **pec fixture profile + v1 validation records** (`_DomainEngines/profiles/pec.yaml`, `_validation/pec.validation.json`) — DEL-10-04 UNMAPPED-1 (pec engine status itself F-APP-3-fenced, not judged).
- **Evidence-overlap partitions (proposed resolutions, as required):**
  - `domain-profile-registry.ts` lines 75-100 (pec entry) appears in both (2) and (4). **Proposed partition:** the registry mechanism and its gate belong to (2); the pec ENTRY (the fixture registration content) belongs to (4). Split on mechanism-vs-content.
  - `domain-proposal-tools.ts` appears in both (3) and (4). **Proposed partition:** the tool surface (registration, envelope, gating) belongs to (3); only its pec-profile-scoped fixture interaction (engineKind http-api gate exercising the pec profile) is evidence for (4). Split on surface-vs-fixture-use.
- **Options:** (A) adopt the partition into deliverable scope: (1)→DEL-10-01, (2)→DEL-10-01 (registration) with fixture-validation content to DEL-10-04, (3)→DEL-10-03, (4)→DEL-10-04, DEL-06-02 kit reconciles its "unsupported/TBD" wording (Guidance line 83) to the ruled roster with PKG-10 as roster owner, DEL-05-03 adds the transport-hygiene clause to its redaction scope; (B) record the whole staged surface as ruled-program work with no deliverable owner (deliberate, documented); (C) mixed per-item adoption; (D) do nothing.
- **Affected claims:** DEL-10-01 UNMAPPED-1/UNMAPPED-2; DEL-10-03 UNMAPPED-1; DEL-10-04 UNMAPPED-1; DEL-06-02 UNMAPPED-1 (ACCEPTED_DIVERGENCE row — mapping side only); DEL-05-03 UNMAPPED-1. Affected deliverables: DEL-05-03, DEL-06-02, DEL-10-01, DEL-10-03, DEL-10-04.
- **Downstream:** A gives every ruled-live domain surface a concordance owner before any R7/domain-engine successor work; B leaves the surfaces permanently deliverable-less (each future run re-detects).
- **Recommended (minimal change):** A — the partition already exists in the evidence; adoption is kit-text only (no code).

### R4-P28 — Pipeline shared-panel ownership (de-duplicated claim)
- **Decision type:** deliverable ownership/mapping.
- **Consolidation:** DEL-02-02 UNMAPPED-1 (scaffold UI), DEL-02-02 UNMAPPED-2 (PIPELINE contract/lifecycle-transition panel), DEL-08-03 UNMAPPED-1 (same panels seen from PKG-08) — the W3-flagged known double-count (`R2_WAVES/PKG-08/_VERIFICATION.md` §3.4); one shared-surface claim, one packet.
- **Evidence:** `frontend/src/components/pipeline/pipeline-surface.tsx` lines 166-172/745-875 (Execution Root Scaffold form → scaffoldHarnessExecutionRoot / POST /api/harness/scaffold), lines 152-164/269-299/877-1066 (deliverable-contract + lifecycle-transition panels); DEL-07-02 Specification.md line 17 explicitly excludes "UI presentation beyond the scaffold API result surface" (the UI layer is currently unowned); candidates: DEL-07-02 (scaffold), DEL-07-04 (transition), DEL-02-02 (parallel to its WORKBENCH REQ-003/004).
- **Options:** (A) map scaffold UI → DEL-07-02 (amending its UI exclusion) and contract/transition panel → DEL-07-04; (B) map both panels to DEL-02-02 as PIPELINE requirements (parallel to WORKBENCH REQ-003/004, with a PIPELINE transition render test per the D-APP-36 bar); (C) record both as deliberate co-resident convenience UI; (D) do nothing.
- **Affected claims:** DEL-02-02 UNMAPPED-1, UNMAPPED-2; DEL-08-03 UNMAPPED-1. Affected deliverables: DEL-02-02, DEL-07-02, DEL-07-04, DEL-08-03.
- **Downstream:** B adds one render test; A amends a DEL-07-02 exclusion (spec edit).
- **Recommended (minimal change):** B — the panels live on DEL-02-02's surface and mirror its existing WORKBENCH requirements; one kit amendment + one test, no exclusion rewrites in PKG-07.

### R4-P29 — Shell/persona surface ownership (/chat, persona picker, deliverable-rows launcher)
- **Decision type:** deliverable ownership/mapping.
- **Consolidation:** DEL-02-01 UNMAPPED-2 (/chat direct-chat shell surface), UNMAPPED-3 (portal deliverable-rows launcher), UNMAPPED-4 (portal persona-picker bar) — the ledger itself marks 2/3/4 as one packet. Handle noted (HDN=NO row, no cell mapped here): DEL-08-02 UNMAPPED-001 `isMatrixLaunchBlockedByStreaming` UI guard, flagged W3 §3.6 with no decomposition assignment — same shell/persona ownership map should name its owner in passing.
- **Evidence:** `shell-frame.tsx` line 9 (ShellSection includes CHAT), `loop-first.ts` (CHAT_ROUTE, buildDirectChatHref), `frontend/src/app/chat/**`; `agent-matrix.tsx` lines 127-161/229-251 (deliverable-rows launcher); `portal-loop-shell.tsx` lines 28-36 + `persona-picker.tsx`; Guidance assigns persona-alias ownership to DEL-08-02. W1 flag: `agent-matrix.tsx` OPERATIVE Deliverable Rows also claimed by DEL-02-03 REQ-009 (likely benign DEL-02-03 ownership — adjudicate in the same map).
- **Options:** (A) adopt all three surfaces into DEL-02-01's shell scope (kit amendment; launcher possibly to DEL-02-03 per its REQ-009 claim); (B) map persona-facing surfaces (/chat, persona bar) to a PKG-08 persona deliverable (DEL-08-02/08-03) and keep the launcher in DEL-02-01/02-03; (C) record as convenience UI; (D) do nothing.
- **Affected claims:** DEL-02-01 UNMAPPED-2/UNMAPPED-3/UNMAPPED-4 (+ DEL-02-03 REQ-009 and DEL-08-02 UNMAPPED-001 as context). Affected deliverables: DEL-02-01, DEL-02-03, DEL-08-02.
- **Recommended (minimal change):** A with the launcher confirmed under DEL-02-03 REQ-009 (already-claimed) — shell surfaces live in the shell deliverable; persona-ALIAS ownership stays with DEL-08-02 unchanged.

### R4-P30 — /api/harness/* route-catalog ownership
- **Decision type:** deliverable ownership/mapping.
- **Evidence:** DEL-03-03 UNMAPPED-1: three live routes beyond the cataloged seven (SPEC §17.1 lines 851-857 / PRD §9.1): `api/harness/session/[id]/events` (JSONL replay — DEL-05-02 owns the replay library and declined the HTTP route, W2), `api/harness/permission…`, `api/harness/agents…`. Candidates: DEL-05-02 (events), PKG-06 permission spine, PKG-08 agent roster; or extend DEL-03-03's route-shape compatibility coverage.
- **Options:** (A) assign each route to the deliverable owning its backing capability (events→DEL-05-02, permission→PKG-06 owner, agents→PKG-08 owner) and add the three to the SPEC §17.1 catalog via R4-P06; (B) extend DEL-03-03 to cover route-shape compatibility for all /api/harness/* routes generically; (C) do nothing.
- **Affected claims:** DEL-03-03 UNMAPPED-1 (+ DEL-03-03 REQ-008 doc residual rides R4-P48). Affected deliverables: DEL-03-03, DEL-05-02, PKG-06/PKG-08 owners.
- **Recommended (minimal change):** A — capability-owner mapping matches the run's decomposition-of-record practice (R4-P14).

### R4-P31 — Session-manager guard surfaces (adoption + ownership, one packet)
- **Decision type:** deliverable ownership/mapping (folds one scope-adoption question — same file, same decision sitting).
- **Evidence:** DEL-05-01 UNMAPPED-1: `session-manager.ts` assertSafeSessionId lines 70-82 (path-traversal guard, no owning requirement, no dedicated test); DEL-05-01 UNMAPPED-2: assertProjectRootAccessible lines 34-45 (instruction-root/working-root containment guard, likely PKG-03 working-root territory; partially covered by DEL-05-01 R005).
- **Options:** (A) adopt both guards into DEL-05-01 requirements (security hardening; add the missing sessionId guard test); (B) adopt the sessionId guard into DEL-05-01 and map the containment guard to the PKG-03 working-root owner; (C) record both as deliberate unrequired hardening; (D) do nothing.
- **Affected claims:** DEL-05-01 UNMAPPED-1, UNMAPPED-2. Affected deliverables: DEL-05-01, PKG-03 working-root owner.
- **Recommended (minimal change):** A — both guards execute on DEL-05-01's owned surface; one kit amendment + one test, no cross-package spec edits.

### R4-P32 — Child-output artifact thresholds and ownership (W2↔W3 handle, resolved partition)
- **Decision type:** deliverable ownership/mapping.
- **Evidence:** DEL-08-05 UNMAPPED-1 (W3-upheld: hardcoded CHILD_OUTPUT_INLINE_BYTE_LIMIT=16KB / CHILD_OUTPUT_ARTIFACT_BYTE_LIMIT=512KB, `tool-result-artifacts.ts` lines 38-39, gating at 177/181 — genuinely unmapped threshold VALUES, cleanly distinct from DEL-05-05's descriptor.resultBudget); DEL-05-05 UNMAPPED-1 (subagent child-output artifact storage `artifacts/subagents/` unowned between DEL-05-05 and a PKG-08 subagent deliverable). REQ-007 requires artifact storage "too large for inline" but names no threshold.
- **Options:** (A) assign subagent child-output artifact storage to DEL-08-05 (the child-run record owner) and adopt the two byte limits into its REQ-007/REQ-008 wording; (B) assign storage to DEL-05-05 as a scope extension; (C) record the constants as deliberate unrequired implementation values; (D) do nothing.
- **Affected claims:** DEL-05-05 UNMAPPED-1; DEL-08-05 UNMAPPED-1. Affected deliverables: DEL-05-05, DEL-08-05.
- **Recommended (minimal change):** A — matches the W3 partition already verified (child-output path belongs to DEL-08-05).

### R4-P33 — Subagent permission-class ownership
- **Decision type:** deliverable ownership/mapping.
- **Evidence:** DEL-06-01 UNMAPPED-1: `permission-overlay.ts` lines 195-221 (subagent class: evaluateSubagentPreflight — allow only in workspaceWrite for delegated children, else hard-deny; cites D-APP-10); DEL-06-01 Specification REQ-005 enumerates tool classes but names no subagent/Agent class; W3 verified DEL-08-04 CONSUMES the class compatibly (declaration vs consumption split, no double-mapping).
- **Options:** (A) adopt the subagent permission class into DEL-06-01 REQ-005's class enumeration (declaration owner) with DEL-08-04 as consumer; (B) map the class to the D-APP-10 executable-subagent-bridge deliverable (DEL-08-04); (C) do nothing.
- **Affected claims:** DEL-06-01 UNMAPPED-1 (context: DEL-08-04 rows). Affected deliverables: DEL-06-01, DEL-08-04.
- **Recommended (minimal change):** A — the class lives in DEL-06-01's owned overlay file and the behavior is already ruling-governed (D-APP-10); one kit line.

### R4-P34 — message.* / queue.* event-lane mapping
- **Decision type:** deliverable ownership/mapping.
- **Evidence:** DEL-04-03 UNMAPPED-1: `sdk-message-mapper.ts` emits message.delta/message.completed/queue.enqueued in parallel with the model.* lane; DEL-04-03 REQ006 enumerates session/turn/model categories only; PKG-04 fan-in kept this as the package's one surviving genuine coverage query.
- **Options:** (A) enumerate the message.*/queue.* lane in DEL-04-03 REQ006 (kit amendment); (B) attribute the lane to the owning HarnessEvent-type/TYPES deliverable; (C) record as accepted canonical-type emission; (D) do nothing.
- **Affected claims:** DEL-04-03 UNMAPPED-1. Affected deliverables: DEL-04-03 (candidate: event-schema owner).
- **Recommended (minimal change):** A — the mapper is DEL-04-03's surface; enumeration is one kit-table row.

### R4-P35 — Ratify the open kit conflict-table scope splits (CT-001, CT002, CONFLICT-003)
- **Decision type:** deliverable ownership/mapping (three recorded TBD rulings, one sitting; folded because each is an open Guidance conflict-table row whose live state already matches the kit's proposed authority — same decision shape, minimal-change identical).
- **Items:**
  1. **DEL-01-03 ACC-04 / CT-001** — dispatch path label vs on-disk `PKG-01_Product_Governance_and_Reliance_Boundaries` folder name (Guidance.md line 83; Specification closure evidence line 63 requires the ruling recorded or explicitly deferred). Kit's own PROPOSAL is the minimal-change option.
  2. **DEL-02-05 EXC-002 / CT002** (HDN cell `D-APP-CT002-open` — NO register row exists; verified absent from DECISION_INDEX.csv, so this packet is its decision vehicle) — SOW-019 scope split DEL-02-05 (UI feedback only) vs DEL-04-05/DEL-09-06 (provider wrapper); live split matches the proposed authority (`anthropic-agent-sdk-manager.ts` owned by DEL-04-05 per decomposition line 312).
  3. **DEL-02-02 EXC-003 / CONFLICT-003** — SOW-007 ownership overlap DEL-02-02 (UI selector) vs PKG-08/DEL-08-03 (dispatch); `_CONTEXT` lists SOW-007 under DEL-02-02 while the decomposition ledger marks PKG-08 primary; Dependencies.csv DEP-02-02-003/009. Resolve or explicitly defer before any CHECKING entry.
- **Options (per item):** (A) ratify the kit-proposed split as recorded ruling; (B) rule the alternative assignment; (C) explicit deferral with dated note; (D) do nothing (closure evidence stays incomplete).
- **Affected claims:** DEL-01-03 ACC-04; DEL-02-05 EXC-002; DEL-02-02 EXC-003. Affected deliverables: DEL-01-03, DEL-02-02, DEL-02-05, DEL-04-05, DEL-08-03, DEL-09-06.
- **Downstream:** all three block their deliverables' closure-evidence completeness; none blocks unrelated repairs.
- **Recommended (minimal change):** A for all three — live state already matches each proposed authority; ratification is a register/kit note per item.

### R4-P36 — DEP-02-05-005 dependency-mapping refresh (error-taxonomy target)
- **Decision type:** deliverable ownership/mapping (dependency-row ruling).
- **Evidence:** DEL-02-05 REGISTER-2 (REMAINING_STATE_MISMATCH; HDN cell `D-APP-taxonomy-mapping-open` — NO register row exists; verified absent from DECISION_INDEX.csv, so this packet is its decision vehicle): Dependencies.csv DEP-02-05-005 TargetType UNKNOWN / SatisfactionStatus TBD vs Evidence_ORN-08 (2026-07-10) resolving the taxonomy to product-owned `@chirality/harness-contract`; ORN-08 declined to mutate the row absent a directing ruling.
- **Options:** (A) direct the Dependencies.csv update (Target → `@chirality/harness-contract` typed error taxonomy; SatisfactionStatus per evidence); (B) keep UNKNOWN/TBD deliberately (dated note); (C) do nothing.
- **Affected claims:** DEL-02-05 REGISTER-2. Affected deliverables: DEL-02-05.
- **Recommended (minimal change):** A — the evidence already exists; one register row update.

### R4-P37 — DEL-09-01 CI-requirement ownership (hand-off to DEL-09-05)
- **Decision type:** deliverable ownership/mapping.
- **Evidence:** DEL-09-01 REQ-007 (IMPLEMENTED_DIFFERENTLY; HDN cell cites `D-APP-55` — i.e., this run is the decision vehicle; no separate register row): live CI is repo-root `.github/workflows/harness-premerge.yml` (ORN-01 reshape) — the kit's workflow path, direct wrapper step, `harness-section8-summary` upload name, projectRoot=/tmp poll, and `secrets.ANTHROPIC_API_KEY` wording are all stale; W4 verified CI ownership sits with DEL-09-05 per decomposition line 364 (DEL-09-01 defers; handles compatible, `R2_WAVES/PKG-09/_VERIFICATION.md` §5).
- **Options:** (A) hand the CI-workflow requirement entirely to DEL-09-05 and reduce DEL-09-01 REQ-007 to a cross-reference (kit repair both sides); (B) retain a narrowed DEL-09-01 CI requirement (validation-wrapper invocation only) with DEL-09-05 owning the workflow; (C) do nothing.
- **Affected claims:** DEL-09-01 REQ-007 (+ REGISTER-1 artifact-name lag rides tranche R4-P45). Affected deliverables: DEL-09-01, DEL-09-05.
- **Recommended (minimal change):** B — preserves DEL-09-01's genuine interest in its own wrapper's CI invocation while matching the decomposition's ownership line.

---

## 5. Residual work acceptance or deferral (R5 tranche definitions — all owner-gated)

Each tranche below is a bounded repair set; member rows are enumerated in
`PROPOSED_DELIVERABLE_UPDATES.csv` (GatedBy = the tranche packet). Options for every tranche
packet are: (A) authorize the tranche as bounded; (B) authorize a subset (owner strikes rows);
(C) defer entirely; (D) do nothing. Recommended is (A) unless stated. Per plan §8, unruled
sibling packets do not block a tranche's unrelated rows.

### R4-P38 — Tranche A: corpus v1→v6 label pins
- Four-way-consistent class (W5 §5): kit/register lines pinning "corpus v1"/"MATCH at v1" while the live corpus is v6; substantive MATCH claims true everywhere (hashes verified by recompute).
- **Members:** DEL-01-01 ACC-001 + REGISTER-1; DEL-01-02 RBR-021 (lines 9/112/122); DEL-01-03 ACC-02 + DEP-01-03-011 register note (REGISTER-1); DEL-01-04 ACC-004; PKG-00/PKG-10 sightings folded where rows exist.
- **Repair shape:** replace v1 pins with the current corpus version reference or a version-neutral pointer; no judgment changes. **Recommended:** A.

### R4-P39 — Tranche B: CHECKING-lifecycle wording under D-APP-54
- Every package carries kit lines saying the deliverable "is CHECKING" / CHECKING-era acceptance wording, superseded by the D-APP-54 rebaseline (all 53 → IN_PROGRESS).
- **Members (ledgered rows):** DEL-00-01 ACC-001, DEL-00-02 ACC-001, DEL-01-01 REQ-009, DEL-01-02 ACC-001, DEL-01-03 ACC-03, DEL-01-04 ACC-001, DEL-10-01 ACC-004 (+ analogous rows swept per-deliverable in the CSV).
- **Repair shape:** lifecycle-neutral wording reading state from `_STATUS.md` (W5 §5 pattern). NO lifecycle transitions ride this tranche. **Recommended:** A.

### R4-P40 — Tranche C: REF-006 resolved hash-mismatch sweep (kit half + register half)
- **Kit half (independent; existing D-APP-35 refresh authorization):** kit texts asserting a docs/PRD.md HASH_MISMATCH that is resolved (live shasum `ac35fba4…` = MATCH). Members: PKG-04 (DEL-04-01/02/05 ACC-001, DEL-04-04 PC-ACC-001), PKG-06 (six kits — DEL-06-01 ACC-001, DEL-06-02 ACC-001, DEL-06-03 ACC-06-03-001, DEL-06-04 REQ-016, DEL-06-05 REQ-009/REQ-016/ACC-001, DEL-06-06 REQ-014/REQ-015), PKG-07 (six ACC/REQ rows), PKG-09 (DEL-09-01 REQ-010, DEL-09-02 ACC-001, DEL-09-03 ACC-001, DEL-09-04 ACC-001, DEL-09-05 ACC-001, DEL-09-06 ACC-001), PKG-10 (DEL-10-02 ACC-001, DEL-10-04 REQ-009, DEL-10-05 ACC-001), PKG-02 (DEL-02-05 ACC-001).
- **Register half (gated additionally by R4-P16):** the stale unannotated warnings in `_DEPENDENCIES.md`/register surfaces (PKG-07 six REGISTER-1 rows; PKG-09 DEL-09-01 REGISTER-2, DEL-09-02 REGISTER-1, DEL-09-04 REGISTER-1, DEL-09-05 REGISTER-1, DEL-09-06 REGISTER-1) — annotate-as-resolved-history, no erasure.
- **Recommended:** A for the kit half now; register half executes under whichever R4-P16 option rules.

### R4-P41 — Tranche D: REF-007/REF-008 machine-absolute reference paths
- Machine-absolute paths (e.g. `/Users/ryan/…`) in `_REFERENCES.md` rows, recurring in all four PKG-01 registers (W5 §6.4) and all five PKG-10 registers (W6 §7: five REGISTER rows), with every register audited run-wide.
- **Repair shape:** re-anchor to repo-relative paths; metadata-only. **Recommended:** A.

### R4-P42 — Tranche E: superseded DepClosure snapshot pointer
- Kits pin `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` as "current accepted DepClosure snapshot" while live `_LATEST.md` names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`; substantive closure verdicts INTACT (both snapshots scc_count=0, W7-verified).
- **Members:** DEL-00-01 REQ-001 + REGISTER-1; DEL-00-02 REQ-002 + REGISTER-1; DEL-10-04 notes sighting (rides its kit row). Complementary spec-view and register-view repairs, one tranche (W7 §6.1). Also carries the DEL-00-01 REQ-003 SCC-002 descriptor-row fixes (DEP-10-03-006 PENDING→SATISFIED; DEP-10-02-004 →RETIRED/NOT_APPLICABLE) already scoped at W7 §4. **Recommended:** A.

### R4-P43 — Tranche F: noteless-INSP-03 supersede/annotate (gated by R4-P11)
- Add superseding notes to assessments whose conclusions are overtaken but carry no note, preserving historical evidence (plan R5 "supersede or annotate … without erasing").
- **Members:** all 5 PKG-10 assessments (W6 §4.4 — cut as ONE tranche, resolving the per-deliverable-vs-one question in favor of one); DEL-00-02 INSP-03 (W7); the run's STALE_ASSESSMENT rows per deliverable (DEL-01-01/01-02/01-03, DEL-02-01, DEL-04-03, DEL-10-01/02/03/05 — see CSV); DEL-07-03's retained matrix-annotation repair (W3 precedent: note exists, only the FAIL/PARTIAL matrix cells need the historical annotation). **Recommended:** A, one run-wide tranche.

### R4-P44 — Tranche G: relocated-evidence-pointer refresh (D-APP-48 / D-APP-46)
- Evidence pointers referencing pre-relocation paths: PKG-05's D-APP-48 path references (DEL-05-04 REQ-013 kit-normative path — STALE_SPECIFICATION; DEL-05-05 citation note; DEL-05-01/02 assessment pointers — one sweep, W2 PKG-05 §3.4); D-APP-46 relocated tool-descriptor assessment pointers (PKG-04 §3.4); DEL-03-03's `runtime_engine_contract.md` citations of pre-D-APP-48 paths (`event-schema.ts`, `agent-engine-port.ts`); DEL-01-02 RBR-001's four stale enforcement-surface paths (live at `frontend/packages/harness-contract/src/`) plus RBR-025's sound proposal to add a cited-path-existence assertion to `reliance-boundary-register.test.ts` (verified absent — the only code item in this tranche; owner may strike it to keep the tranche doc-only). **Recommended:** A.

### R4-P45 — Tranche H: residual kit/register metadata corrections (catch-all, bounded by ledger rows)
- Every remaining defect row not claimed by Tranches A-G or a specific packet: per-row register machine-field lags (e.g. DEL-04-04 REGISTER-1 retirement mirror; DEL-04-05 REGISTER-1 discharged constraint still ACTIVE/TBD; DEL-05-02 REGISTER-2 retired-row count; DEL-06-05 REGISTER-1 narrowed present-tense cell DEP-06-05-008; DEL-09-01 REGISTER-1 artifact-name lag `harness-section8-summary`→`harness-validation-summaries`; DEL-10-04 REGISTER-2 DEP-10-04-008 machine-field lag), kit-text one-offs (DEL-08-05 REQ-001 Datasheet ChildRunRecord field table lines 49-60 + Guidance example lines 43-58; DEL-08-02 Datasheet line 26 false rationale — gated also by R4-P06(c); DEL-09-02 RQ-015 Specification line 31 now-false sentence), and STALE_VERIFICATION pointer repairs (DEL-02-01 REQ-003, DEL-02-04 REQ-002, DEL-09-01 REQ-003/REQ-005). Exact member set = the CSV rows with GatedBy R4-P45. Each repair executes only per its ledger row's RemainingWork; no judgment changes. **Recommended:** A.

### R4-P46 — D-APP-53 Option-C-gated open items: accept continued gating or mint successor packets
- **Decision type:** residual work acceptance or deferral.
- **Evidence:** D-APP-53 ruled Option A only ("No Option C" — register row 68); four deliverables carry accurately-recorded, correctly-gated open items that are NOT selectable under the current loop: DEL-07-04 REQ-014 + REMAINING-1 (content-change SHA revalidation on the transition surface); DEL-08-04 REMAINING-1 (per-attempt subagent decision-replay artifact — currently console-only, `subagent-governance.ts` lines 66-81); DEL-05-03 REMAINING-1 (arbitrary configured-secret registry); DEL-10-03 REMAINING-1 (DEP-10-03-004 amendment question, still PENDING with the D-APP-53 annotate-only note).
- **Options:** (A) accept continued gating (explicit re-affirmation; items stay open and unselectable — pure status quo, zero work); (B) mint a successor owner decision packet unlocking one or more items (each would become its own bounded tranche); (C) retire any item the owner no longer wants (scope retirement, recorded).
- **Affected claims:** DEL-05-03 REMAINING-1; DEL-07-04 REQ-014, REMAINING-1; DEL-08-04 REMAINING-1; DEL-10-03 REMAINING-1.
- **Recommended (minimal change):** A — all four are concordant as recorded; unlocking is a fresh owner queue decision outside this run's need.

### R4-P47 — ResponsibleParty / owner-role assignments (human-owned fields)
- **Decision type:** residual work acceptance or deferral (owner act, not agent work).
- **Evidence:** DEL-00-02 REMAINING-1 (ResponsibleParty TBD persists across the kit: `_CONTEXT.md` line 14, Datasheet line 12, Guidance lines 56-57; gated on an owner ruling, D-APP-53 Option A only); DEL-04-01 ACC-002 (assign the approving role for the adoption verdict; `_CONTEXT.md` requires preserving TBD until a human assigns ownership); DEL-01-01 Guidance open item R003 (ResponsibleParty; rides the DEL-01-01 ACC-002 row's residual list).
- **Options:** (A) assign the roles now (one owner act per field); (B) explicit deferral with dated note per field; (C) do nothing.
- **Affected claims:** DEL-00-02 REMAINING-1; DEL-04-01 ACC-002; DEL-01-01 ACC-002 (R003 component). Affected deliverables: DEL-00-02, DEL-01-01, DEL-04-01.
- **Recommended (minimal change):** B — explicit dated deferrals keep the fields honestly TBD without forcing role decisions inside a reconciliation gate.

### R4-P48 — Missing documentation artifacts: produce or governed deferral
- **Decision type:** residual work acceptance or deferral. (Fold: two same-shaped produce-or-defer items, independent options inside.)
- **Items:** (1) DEL-01-01 ACC-002 (DOCUMENTED_UNIMPLEMENTED): checklist artifacts named by Specification Documentation lines 54-64 / Datasheet line 29 do not exist as standalone artifacts (owner ruling DEL-01-01-R004 defines filenames/destinations); also resolve Guidance R002 (stale dispatch label). (2) DEL-03-03 REQ-008 (PARTIALLY_IMPLEMENTED): route adapter test index and SSE compatibility fixture README not produced (route tests and contract doc substantially exist); residual not recorded in `_STATUS.md ## Remaining` — recording correction rides this packet's CSV rows.
- **Options (per item):** (A) produce the artifacts (bounded doc work); (B) record a governed deferral in the kit + `## Remaining` with gate metadata; (C) do nothing.
- **Affected claims:** DEL-01-01 ACC-002; DEL-03-03 REQ-008. Affected deliverables: DEL-01-01, DEL-03-03.
- **Recommended (minimal change):** B for both — the substantive content exists elsewhere; a recorded deferral makes the `## Remaining` truthful (the current omission is itself a defect the CSV rows repair).

### R4-P49 — Packaging-evidence absence family (all 15 PKG-09 PARTIALs + packaged-SDK proof)
- **Decision type:** residual work acceptance or deferral.
- **Evidence:** the 15 PKG-09 PARTIALLY_IMPLEMENTED rows share one root state: no packaging outputs exist at the source state (`frontend/dist/`, `frontend/artifacts/` absent, gitignored — e.g. DEL-09-05 REQ-003's accepted refutation basis, W4 §2); DEL-09-04 REQ-008 needs the packaged SDK resolver proof and live read-tool proof run against a produced app bundle with command/package-path/expected/observed recorded (assessment Recommendation 3; probe mechanism complete and unit-tested; historical D-APP-18 app-directory proof passed; Guidance CONF-004 — whether a full packaged SDK-backed turn start blocks closure — unresolved and ruled inside this packet).
- **Options:** (A) authorize one bounded packaging-evidence tranche: run `desktop:pack` (per R4-P03) / `desktop:dist`, execute the packaged probes, record evidence artifacts; rule CONF-004 in passing; (B) defer all packaging evidence to a release-preparation phase (explicit, dated; the 15 PARTIALs remain open-by-design); (C) do nothing.
- **Affected claims:** DEL-09-04 REQ-008 + the PKG-09 PARTIAL family (15 rows incl. DEL-09-05 REQ-003). Affected deliverables: DEL-09-01..06.
- **Downstream:** interacts with R4-P20 (if packaging binds every release-significant acceptance, B becomes untenable) and R4-P05.
- **Recommended (minimal change):** B — packaging evidence is naturally produced at release time; record the deferral once, family-wide.

---

## 6. Lifecycle recommendation

### R4-P50 — Run-level lifecycle recommendation: no transitions; all 53 stay IN_PROGRESS
- **Decision type:** lifecycle recommendation.
- **Evidence:** D-APP-54 rebaselined all 53 deliverables CHECKING→IN_PROGRESS (register row 69); this run recorded zero AUTHORITY_CONFLICT, zero UNKNOWN dispositions (one UNKNOWN cell, R4-P26), 833/1,115 rows ALIGNED, and 282 defect rows now mapped to gated repair tranches; F-APP-4 (no CHECKING→ISSUED) binding throughout.
- **Recommendation (proposal only):** (i) no deliverable transitions lifecycle as part of R4/R5 — every repair tranche is lifecycle-neutral (R4-P39 explicitly rewords kits to read state from `_STATUS.md`); (ii) no deliverable is proposed for CHECKING entry until its gating packets rule and its R5 rows land — checking-entry readiness should then be assessed per the D-APP-34 evidence-profile pattern one gate earlier (plan §8: profiles emerge from checking experience, not predetermined); (iii) the deliverables whose ledgers are already defect-free (no STALE_*/REMAINING_STATE_MISMATCH rows: DEL-03-04 aside its REQ-014 corpus row — see CSV; none are fully clean of gated questions) illustrate that no candidate currently satisfies an evidence profile without at least one open packet — supporting (ii).
- **Options:** (A) adopt i-iii as the run's lifecycle posture; (B) direct early CHECKING-entry evaluation for named deliverables after their packets rule; (C) do nothing (same effect as A, undocumented).
- **Affected deliverables:** all 53. **Recommended (minimal change):** A.

---

## 7. NEW-PACKET sweep reconciliation (CLAIM_CONCORDANCE.csv, complete)

Sweep basis: 1,115 rows; `HumanDecisionNeeded` non-NO in 66 cells — 63 `NEW-PACKET` cells plus 3
pseudo-decision citations (`D-APP-CT002-open`, `D-APP-taxonomy-mapping-open`, `D-APP-55`) that name
NO existing register row (verified against `R1_INVENTORY/DECISION_INDEX.csv` and
`_DECISIONS/_REGISTER.md`; the register's only relevant rows are D-APP-53/54/55 themselves), so all
66 cells require packet placement. Every cell lands in EXACTLY ONE packet:

| Cell (DEL / ClaimID) | Packet |
|---|---|
| DEL-00-02 REMAINING-1 | R4-P47 |
| DEL-01-01 ACC-002 | R4-P48 |
| DEL-01-03 ACC-04 | R4-P35 |
| DEL-01-04 REQ-011 | R4-P22 |
| DEL-02-01 REQ-002 / REQ-007 / REQ-008 | R4-P06(a) |
| DEL-02-01 UNMAPPED-1 | R4-P06(b) |
| DEL-02-01 UNMAPPED-2 / UNMAPPED-3 / UNMAPPED-4 | R4-P29 |
| DEL-02-02 REQ-002 | R4-P06(a) |
| DEL-02-02 EXC-003 | R4-P35 |
| DEL-02-02 UNMAPPED-1 / UNMAPPED-2 | R4-P28 |
| DEL-02-04 REQ-003 / REQ-009 | R4-P07 |
| DEL-02-05 EXC-002 (`D-APP-CT002-open`) | R4-P35 |
| DEL-02-05 DEL-02-05-UNMAPPED-1 | R4-P01 |
| DEL-02-05 REGISTER-2 (`D-APP-taxonomy-mapping-open`) | R4-P36 |
| DEL-03-02 REQ-002 / REQ-008 | R4-P24 |
| DEL-03-02 REQ-009 | R4-P10 |
| DEL-03-03 REQ-008 | R4-P48 |
| DEL-03-03 UNMAPPED-1 | R4-P30 |
| DEL-03-04 REQ-006 | R4-P10 |
| DEL-04-01 ACC-002 | R4-P47 |
| DEL-04-03 UNMAPPED-1 | R4-P34 |
| DEL-05-01 UNMAPPED-1 / UNMAPPED-2 | R4-P31 |
| DEL-05-03 UNMAPPED-1 | R4-P27 |
| DEL-05-03 UNMAPPED-2 | R4-P02 |
| DEL-05-03 REMAINING-1 | R4-P46 |
| DEL-05-05 REQ-004 | R4-P08 |
| DEL-05-05 UNMAPPED-1 | R4-P32 |
| DEL-06-01 UNMAPPED-1 | R4-P33 |
| DEL-06-02 UNMAPPED-1 | R4-P27 |
| DEL-06-02 REGISTER-2 | R4-P18 |
| DEL-06-05 UNMAPPED-1 | R4-P09 |
| DEL-06-06 UNMAPPED-1 | R4-P04 |
| DEL-07-04 REQ-014 / REMAINING-1 | R4-P46 |
| DEL-08-02 REQ-003 / ACC-001 | R4-P06(b) |
| DEL-08-02 REQ-004 | R4-P06(c) |
| DEL-08-02 REQ-008 / REQ-009 | R4-P06(a) |
| DEL-08-02 REQ-014 | R4-P06(d) |
| DEL-08-03 REQ-010 | R4-P21 |
| DEL-08-03 DEL-08-03-UNMAPPED-1 | R4-P28 |
| DEL-08-04 REMAINING-1 | R4-P46 |
| DEL-08-05 REQ-001 | R4-P45 |
| DEL-08-05 UNMAPPED-1 | R4-P32 |
| DEL-09-01 REQ-007 (`D-APP-55`) | R4-P37 |
| DEL-09-02 RQ-014 | R4-P23 |
| DEL-09-04 REQ-008 | R4-P49 |
| DEL-09-04 UNMAPPED-1 | R4-P03 |
| DEL-10-01 REQ-002 / ACC-001 | R4-P06(e) |
| DEL-10-01 UNMAPPED-1 / UNMAPPED-2 | R4-P27 |
| DEL-10-03 UNMAPPED-1 | R4-P27 |
| DEL-10-03 REMAINING-1 | R4-P46 |
| DEL-10-04 REQ-001 | R4-P06(e) |
| DEL-10-04 UNMAPPED-1 | R4-P27 |
| DEL-10-05 REQ-007 | R4-P06(e) |

**Tally: 66 cells → 30 distinct packets.** Deliberate folds (multi-cell packets): R4-P06 (16 cells
— the ONE corpus family per the escalation queue), R4-P27 (6 — the ONE domain-ownership packet plus
two same-family folds), R4-P46 (5 — one D-APP-53 gate family), R4-P28 (3), R4-P29 (3), R4-P35 (3 —
same conflict-table decision shape), R4-P07/P10/P22-as-pairs, R4-P47 (2), R4-P48 (2), R4-P31 (2),
R4-P32 (2), R4-P24 (2). Standing-contest packets R4-P17/P19/P20, minority-reading packet R4-P26,
method packets R4-P11..P14, class packets R4-P15/P16, tranches R4-P38..P44, CI packet R4-P05, and
lifecycle packet R4-P50 carry no NEW-PACKET cell (their rows are HDN=NO or non-ledger escalations)
but are mandated by the wave records and escalation queue.

**Existing-decision citations verified (no packet needed):** all other non-NO-adjacent references in
RemainingWork cells cite ruled register rows (D-APP-53 row 68, D-APP-54 row 69, D-APP-55 row 70 —
verified present in `_DECISIONS/_REGISTER.md`); the three pseudo-IDs above were the only citation-shaped
values without register rows, and each received a packet (R4-P35, R4-P36, R4-P37).

**Packet census: 50 packets** — scope adoption/retirement 5 (P01-P05); product-behavior 5 (P06-P10);
acceptance-criteria 16 (P11-P26); ownership/mapping 11 (P27-P37); residual work 12 (P38-P49);
lifecycle 1 (P50).
