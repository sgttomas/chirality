# DEL-01-03 concordance notes (R2 Wave-5, PKG-01)

Deliverable: DEL-01-03 Product Identity and Professional Boundary Copy (Type DOC_UPDATE).
Source state: frontend/ at `fac46e33f` (byte-identical through current HEAD `242900ae9` = main per W5 dispatch; last frontend commit `d2f1cb7ff`).
Verification binding: `GATE-TRANSCRIPT(W1@fac46e33f)` where behavioral (typecheck exit 0; Vitest 667 passed/4 skipped); `RUN-INSPECTION@fac46e33f` for this wave's copy sweeps; MR-10 vocabulary elsewhere.

## Census

- Total rows: 21 (10 REQUIREMENT, 4 EXCLUSION, 5 ACCEPTANCE, 1 REGISTER_DEFECT, 1 REMAINING_WORK).
- By Disposition: ALIGNED 15, STALE_SPECIFICATION 3 (EXC-02, ACC-02, ACC-03), STALE_ASSESSMENT 1 (ACC-01), PARTIALLY_IMPLEMENTED 1 (ACC-05), REMAINING_STATE_MISMATCH 1 (REGISTER-1). (ACC-02 flipped STALE_ASSESSMENT -> STALE_SPECIFICATION at fan-in; see the fan-in record below.)
- AssessmentEvidence tokens: STILL CURRENT 14, OVERTAKEN 3 (EXC-02, ACC-01, ACC-02), NOT APPLICABLE 4 (EXC-04, ACC-03, REGISTER-1, REMAINING-1).
- IMPLEMENTED_UNMAPPED rows: 0 (see below).
- HumanDecisionNeeded: NEW-PACKET 1 (ACC-04, the CT-001 ruling), NO on all other rows.
- SelectableUnderCurrentLoop: YES only on REMAINING-1 (MR-2).

## How the enforcement-truth distinction was applied (PKG-01 note)

DEL-01-03 is a copy-rules deliverable, but each MUST/MUST NOT was checked against the
live frontend, not just the kit:

- Identity present: `frontend/src/app/layout.tsx:9`, `frontend/src/components/shell/shell-frame.tsx:72-78`, `frontend/package.json:8-9,63-64` (productName `Chirality`, appId `com.chirality.app`).
- Violating copy absent: repo-wide grep at the source state finds ZERO `Claude Code` strings in `frontend/src`, `frontend/public`, `frontend/electron`, `frontend/package.json`; the only Anthropic strings are provider detail (`api-key-settings.tsx:175,180,238`; `electron/api-key-storage.ts:4`; SDK asarUnpack entries).
- Boundary copy live in runtime messages: `persona-manager.ts:108` (agents propose / humans approve preface) and `:186` (allowedTools not a security boundary); `domain-proposal-tools.ts:101-102` (no domain verdict; dry-run is NOT acceptance; human acts behind admin-only RBAC), attached at lines 235/497/561/620 and test-asserted (`domain-proposal-tools.test.ts:376,575`; `chirality-read-mcp.test.ts:324,451`).
- Human-gate copy consistent: `permission-requests.tsx:81-121` approval cards are operator acts; `pipeline-surface.tsx:441-450,1014-1051` force actor HUMAN + approvalSha for CHECKING/ISSUED.

No register row of this deliverable asserts an enforced product behavior that the
implementation does not carry; the defect rows found are documentation/assessment
staleness, not enforcement gaps.

## Least-confident rows (self-flagged; alternative readings)

- **DEL-01-03-REQ-01 (ALIGNED, MEDIUM).** Identity is live everywhere, but no rendered UI
  copy affirmatively "describes Chirality's governed-work posture" (subtitles are operational;
  posture copy lives in docs and the composed system prompt). **Alternative that would flip it:**
  read the requirement as demanding posture description on rendered user-facing surfaces →
  PARTIALLY_IMPLEMENTED. I kept ALIGNED because the requirement is a copy rule over copy that
  exists, the deliverable's verification approach is a review (not a rendered-surface mandate),
  and no live copy contradicts the posture.
- **DEL-01-03-REQ-04 (ALIGNED, MEDIUM).** Same shape: draft/decision-support posture is stated
  in the persona composer preface (`persona-manager.ts:108`) and nothing contradicts it, but no
  rendered chat/output surface displays a draft-assistance notice. **Alternative:** read
  "copy MUST state" as requiring a visible end-user notice → PARTIALLY_IMPLEMENTED (or
  DOCUMENTED_UNIMPLEMENTED on the UI slice). I kept ALIGNED on the disjunctive "state or
  preserve" wording plus the checklist's own "starting points, not mandatory UI strings" framing
  (BOUNDARY_REVIEW_CHECKLISTS.md line 57). Test nuance recorded in-row: persona-manager.test.ts:85
  asserts the phrase but the fixture also injects it (line 37), so the assertion does not isolate
  the composer's hardcoded preface line.
- **DEL-01-03-ACC-02 (now STALE_SPECIFICATION, HIGH — refutation accepted at fan-in).** My
  original STALE_ASSESSMENT reading rested on a wrong factual premise: I took the kit's "MATCH
  under D-APP-38 corpus v1" as hash-true because `_REFERENCES.md` reproduces live shasums. The
  verifier's evidence is correct and I re-verified it directly before editing:
  AUTHORITY_CORPUS.json's v1 entry (binding commit 8da930ae0) records docs/PRD.md = 33e00c82…,
  which does NOT match the live file (ac35fba4…, v6-era) — the match holds under v6, not v1, so
  the kit surfaces (Spec line 45, Datasheet line 68, Procedure lines 18/30/102-103, Guidance
  lines 85-86) flatly assert a now-false state → MR-8 first branch, STALE_SPECIFICATION. This
  also makes the class consistent with DEL-01-01 ACC-001, DEL-01-02 RBR-021, DEL-01-04 ACC-004.
  The INSP-03 stale-caveat leg stays recorded via the row's OVERTAKEN token.
- **DEL-01-03-ACC-04 (ALIGNED, MEDIUM; HumanDecisionNeeded NEW-PACKET).** CT-001 (dispatch-path
  label vs on-disk folder) is open with a kit PROPOSAL and no register row; declared state matches
  reality, so ALIGNED with NEW-PACKET. **Alternative:** treat CT-001 as an ignorable historical
  dispatch artifact needing no decision → HumanDecisionNeeded NO. I kept NEW-PACKET because the
  Specification's own closure evidence (line 63) requires the ruling to be recorded or explicitly
  deferred by a human.
- **DEL-01-03-ACC-05 (PARTIALLY_IMPLEMENTED, MEDIUM).** The checklist/template package exists and
  this wave's sweep found no violating copy, but no completed human-attributed release review
  record exists. **Alternative:** closure criteria bind only at the issuance gate, and the kit
  correctly declares TBD while IN_PROGRESS → ALIGNED. I kept PARTIALLY_IMPLEMENTED per the
  DEL-09-03 REQ-012 closure-criterion precedent (templates exist, evidence capture outstanding).
  Note the residual is declared in the kit but not recorded on this deliverable's `## Remaining`;
  I did not emit a separate REMAINING_STATE_MISMATCH row for that omission (precedent: earlier
  waves carried declared closure residuals in-row rather than as mismatch rows).
- **REGISTER-1 (REMAINING_STATE_MISMATCH, LOW).** DEP-01-03-011's Notes cell still says
  "dependency satisfaction remains TBD" ahead of the appended dated D-APP-53 sentence, while the
  row's SatisfactionStatus is SATISFIED. **Alternative:** the Notes cell is layered dated history
  and the later 2026-07-10 sentence supersedes the earlier clause → no defect. I emitted the row
  at LOW confidence because MR-5 targets exactly this kind of metadata lag and the other 11 rows
  carry no such contradiction.

## Register-defect summary

- 1 row: REGISTER-1 (DEP-01-03-011 Notes internal wording lag vs SATISFIED status; LOW).
- Checked and clean: Dependencies.csv schema v3.1, 12/12 ACTIVE+SATISFIED rows consistent with
  `_DEPENDENCIES.md` summary tables and Evidence_D53A; `_REFERENCES.md` all seven rows MATCH,
  re-verified by direct SHA-256 recomputation this wave (DIRECTIVE 14c77480…, CONTRACT 2f52a24c…,
  SPEC cbca612e…, TYPES bb4af418…, PLAN 6f0baacc…, PRD ac35fba4…, AGENT_SOFTWARE_DECOMP 4f2c0a66…).
- Not defects, noted only: (a) Evidence_D53A quotes REF-003/REF-004 recompute prefixes
  (2a63277a…, aed33a0f…) that no longer match the live/`_REFERENCES.md` hashes — expected drift:
  the 2026-07-11 lifecycle-semantics amendments to docs/SPEC.md and docs/TYPES.md (corpus v6)
  postdate that dated evidence record; `_REFERENCES.md` was updated by the D-APP-38 v6 apply and
  is current. (b) `_DEPENDENCIES.md` Declared Upstream/Downstream are terse pointer sections, not
  bare TBDs — no Declared-TBD observation applies. (c) REF-007 uses an absolute machine-local
  path (`/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md`); the file exists
  and hash-matches, but the path is not repo-relative — portability wart shared with the original
  extraction convention, left to R3 if it recurs across deliverables.

## Other observations

- REQUIREMENT_INDEX.csv parsed all ten DEL-01-03 REQ IDs — no parser gap for this deliverable;
  the claim set was still re-derived from Specification.md (IDs REQ-01..REQ-10, lines 25-34).
- MR-9: the Specification was NOT rewritten after INSP-03 in a way that renumbers requirements
  (REQ IDs stable at the same lines); post-assessment kit changes were the ADQ-01 REF-006 wording
  reconciliation and the ADQ-03 Construction/Documentation materialization paragraphs, both
  handled per-row (ACC-01, ACC-02, EXC-02).
- IMPLEMENTED_UNMAPPED: none emitted. The candidate live copy surfaces (shell identity strings,
  API-key provider labels, persona composer preface, domain proposal result semantics) are all
  owned by sibling deliverables under decomposition v3.2 (PKG-02 shell, PKG-04/05 provider/session
  spine, PKG-08 persona/runtime, PKG-10 domain boundary) — an accepted mapping elsewhere in the
  corpus, so per the Wave-5 rule they are cited as cross-deliverable evidence rather than
  unmapped rows. DEL-01-03's own product is the copy-rules package, which is fully mapped
  (Datasheet Construction table → docs/BOUNDARY_REVIEW_CHECKLISTS.md).
- "No test asserts X" claims in rows REQ-01 and REQ-07 were verified by real greps of
  frontend/src (including `src/__tests__`) at the source state: no test references
  'Chirality Workflow Shell', the brand tile, or the persona-manager line-186 security-boundary
  string.
- Method deviations: none. No tests executed; no dependency installs; write scope limited to the
  two Wave-5 files; F-APP-3 respected (no other project's execution tree read; `_DomainEngines/**`
  not judged).

## Fan-in verification record (accepted verdicts)

- **ACC-02 refutation accepted** (STALE_ASSESSMENT -> STALE_SPECIFICATION; MEDIUM -> HIGH): see
  the updated self-flag entry above. Beyond the disposition token, I corrected the row's
  ImplementationEvidence on my own judgment — its original "remaining hash-true" clause embedded
  the refuted premise and could not stand; it now states the corpus-v1 PRD hash fact
  (33e00c82… vs live ac35fba4…), independently re-verified against AUTHORITY_CORPUS.json.
- **MR-10 evidence recasts accepted** (dispositions unchanged): the free-text
  "Document/scope claim …" VerificationEvidence cells on EXC-01, EXC-03, and ACC-04 were recast
  to `RUN-INSPECTION@242900ae9` with the same content parenthesized. On my own initiative I also
  recast REGISTER-1's VerificationEvidence lead ("Live register read this wave …") to the same
  form — it was the same nonconformant class, merely unflagged.
