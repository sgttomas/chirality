# DEC: decision-effect audit notes (RUN_D128 R2 EXT, item 3)

Ledger: `DEC_claims.csv`, 46 rows, sealed at SHA-256
`7601ffe7e243261671dd8224020eb094de4f5a89aa2fff5dd65dcbcfcf94f912`. Validator: `RESULT PASS errors=0 warnings=0`.
There is no errata file.

## 1. Census

- **Units.** All 38 `Item = 3` units are covered (D-APP-86..115 and 120..127; D-APP-116..119 are not units). Together
  they produce 41 unit rows and 5 run-local `DEC:REGISTER-n` rows. No `DEC:STATE-n` rows were needed.
- **Split rate.** 3 of 38 units (7.9%) were split, each by numbered ruling items that disposition differently:
  - D-APP-112: `.1` is item A, `.2` is item B.
  - D-APP-114: `.1` covers items 1, 2, 3 and 5; `.2` is item 4.
  - D-APP-125: `.1` covers items 1, 2, 4 and 5; `.2` is item 3.
- **SEE rows.** None.

| ClaimType | Disposition | Rows |
|---|---|---|
| REQUIREMENT | ALIGNED | 25 |
| REQUIREMENT | RETIRED_BY_RULING | 8 (88, 92, 94, 100, 104, 107, 125.2, 126) |
| REQUIREMENT | ACCEPTED_DIVERGENCE | 3 (96, 112.2, 114.2) |
| REQUIREMENT | PARTIALLY_IMPLEMENTED | 3 (99, 101, 127) |
| REQUIREMENT | DOCUMENTED_UNIMPLEMENTED | 2 (121, 125.1) |
| REGISTER_DEFECT | REMAINING_STATE_MISMATCH | 4 (REGISTER-1, 2, 4, 5) |
| REGISTER_DEFECT | STALE_SPECIFICATION | 1 (REGISTER-3) |

Confidence: 30 rows HIGH, 13 MEDIUM, 3 LOW. HumanDecisionNeeded is `R4` on one row (D-APP-112.2) and `NO` on
all the others.

**`EFFECT_NOT_LANDED` rows, for the manager.** These are rows where the ruled effect never landed or only partly
landed: 88, 92, 99, 101, 121, 125.1, 125.2, 126 and 127.

- Of these, 88, 92, 125.2 and 126 never landed and were then retired. The retiring ruling is D-APP-127 for 88,
  125.2 and 126, and the 2026-08-13 disposition for 92.
- The rows still owed at the frozen basis are 99, 101, 121, 125.1 and 127.

**`EFFECT_LANDED_THEN_SUPERSEDED` rows.** These use a separate Notes token of my own for effects that landed and
were later superseded by a governing ruling or an owner direction: 94, 96, 100, 104, 107, 112.2 and 114.2. They do
not carry `EFFECT_NOT_LANDED`.

**Flagged rows (RUN_BASIS §5 "GOVERNING, flagged").** For each: the recorded flag, whether that flag is accurate
at the frozen basis, and the disposition.

| Row | Recorded flag | Flag accurate? | Disposition |
|---|---|---|---|
| D-APP-104 | "Git closeout pending" | No. Applied in 06068dfb8, then expired and retired. | RETIRED_BY_RULING (D-APP-127); flag defect in REGISTER-1 |
| D-APP-107 | "integration pending" | No. Integrated in e079cbc39; ScopeOfWork created in be243fdf6. | RETIRED_BY_RULING (D-APP-127); flag defect in REGISTER-1 |
| D-APP-121 | Carrier application and implementation HELD | Yes. Carriers are unamended and `preload.ts:77 inlinePdfPreview: false`. | DOCUMENTED_UNIMPLEMENTED |
| D-APP-122 | "effect HELD until fetched main" | No. PR745 merged; V3-05 removed. Daemon-target parts superseded by D-APP-127. | ALIGNED (LatestDecision D-APP-127); flag defect in REGISTER-2 |
| D-APP-123 | "effect HELD until fetched main" | No. The caller is live at `woven-dialogue-shell.tsx:1062`. | ALIGNED; flag defect in REGISTER-2 |
| D-APP-125 | Design routing active; implementation held | Yes, as far as App surfaces show. Item 3 is superseded. | 125.1 DOCUMENTED_UNIMPLEMENTED (LOW); 125.2 RETIRED_BY_RULING |
| D-APP-126 | Owning Root/Runtime amendments unapplied | Was accurate until superseded; now moot. | RETIRED_BY_RULING (D-APP-127) |

The D-APP-127 application map was summarized, not re-derived:

- 270 rows in total.
- `_STATUS.md` is `Revised = YES` for the 11 named carriers.
- `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md` and `Dependencies.csv` are `NO` for every deliverable.
- 2 `Dependencies.csv` entries are `ABSENT`.

## 2. Least-confident rows

- **D-APP-112.2 (LOW, R4).** Item B (one PR at the run's terminus) landed on 2026-09-05. The owner-directed
  2026-09-19 session-work-graph amendment then displaced it. That amendment is recorded only in
  `AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md` and a notice, has no register row, and
  does not name D-APP-112.
  - I treated the owner's verbatim direction as GOVERNING and dispositioned the row `ACCEPTED_DIVERGENCE`.
  - Alternative: `AUTHORITY_CONFLICT` (R4), if an unregistered owner direction held only in AgentRuns counts as
    CONTEXT under RUN_BASIS §5.
- **D-APP-125.1 (LOW).** No App carrier or governing document transcribes the finalized contracts for items 1, 4
  and 5. Item 2 (a whole-turn Stop) and item 4 (no-folder stays blocked) match live code.
  - Alternative: `UNKNOWN`, because the finalization may exist in Root or Runtime execution records outside this
    worker's read boundary.
- **REGISTER-5 (LOW).** This flags the missing register row for the 2026-09-19 loop amendment.
  - Alternative: not a defect, if owner-direction notices are an accepted home for loop-instruction changes.
- **D-APP-92 and D-APP-94 (MEDIUM, RETIRED_BY_RULING via D-APP-93).**
  - Alternative: `ALIGNED`, if each ruling's effect is read as authorization only. D-APP-92 opened its tranche but
    never executed it; D-APP-94 did adopt its planning baseline.
- **D-APP-96 (MEDIUM, ACCEPTED_DIVERGENCE).** The corpus effect landed. The "All sessions (N)" label was removed
  by 03e61f38f (the SCA-APP-010 dialogue shell).
  - Alternative: `ALIGNED`, if the ruling's effect is read as the corpus removal only.
- **D-APP-99 (MEDIUM).** Four DEL-09-06 secret-scan summaries run to 7,515–9,922 lines with no stated reason. The
  ~2,000-line figure is only a "guideline".
- **D-APP-106, D-APP-108, D-APP-120 (MEDIUM or HIGH).** Part of each ruling's effect lies in Root (the validator,
  the routed notices), which this worker may not read. For those parts the evidence is a commit subject or a run
  REVIEW.
- **D-APP-91 (MEDIUM).** The planning baseline was recorded and never consumed. Nothing downstream was owed.

## 3. Register-defect summary

1. **REGISTER-1.** The State cells of D-APP-104 ("Git closeout pending") and D-APP-107 ("integration pending")
   lag the completed acts. Disposition: `REMAINING_STATE_MISMATCH`.
2. **REGISTER-2.** D-APP-120, 122 and 123 still say their effect is HELD until fetched main, but all three effects
   are on main. Disposition: `REMAINING_STATE_MISMATCH`.
3. **REGISTER-3.** The D-APP-124 row says "PR #739 (open; not merged)", but 2c75eb4bf merged it. Disposition:
   `STALE_SPECIFICATION`.
4. **REGISTER-4.** Blank lines inside the register table (lines 131–151) break the Markdown table from D-APP-118
   onward. Disposition: `REMAINING_STATE_MISMATCH`. Discovery is not affected.
5. **REGISTER-5.** There is no row for the 2026-09-19 loop amendment. Disposition: `REMAINING_STATE_MISMATCH`, LOW.

These do not count as defects:

- D-APP-106 has no ruling record of its own; the register openly points to D-APP-105 §Residual.
- The ruled rows superseded by D-APP-127 are not annotated, but under the register's convention a ruled row is
  history and the D-APP-127 row records the supersessions.

## 4. Direction and cause

- **CauseTags used:**
  - `A2_TOPOLOGY` ×5: 88, 100, 104, 107, 114.2.
  - `DOC_HYGIENE` ×5: the REGISTER rows.
  - `LIFECYCLE_GATE_PENDING` ×3: 101, 121, 125.1.
  - `PRE_V3_DRIFT` ×2: 92, 94. The 2026-08-13 supersession predates 2026-08-22 and no v3 mechanism applies.
  - `CREDENTIAL_CUSTODY` ×2: 125.2, 126.
  - `SHELL_REDESIGN` ×1: 96.
  - `CARRIER_PROPAGATION` ×1: 127.
  - `UNRECORDED_JUDGMENT` ×1: 99.
  - `OTHER:LOOP_WORKGRAPH_TRANSITION` ×1: 112.2. This is the only `OTHER:` token. It names the owner-directed
    2026-09-19 replacement of the session workplan and D-APP-112 item B by the session work graph and "scoped PRs
    at meaningful integration boundaries" rule.
- **Secondary causes:** `CAUSE2:CARRIER_PROPAGATION` on 112.2 and `CAUSE2:A2_TOPOLOGY` on 127.
- **GOVERNING direction cited:** D-APP-127 on 88, 100, 104, 107, 114.2, 125.2 and 126; D-APP-93 (the 2026-08-13
  disposition) on 92 and 94; D-APP-108 on 96; D-APP-114 on 101; the rulings themselves on 121 and 125.1.
- **CONTEXT records used:**
  - `NOTICE_2026-09-12_STANDING_GIT_AUTHORIZATION.md`.
  - `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md`.
  - `AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md`. This is owner words, which I treated as
    GOVERNING on 112.2, flagged LOW.
- **Searches behind each `NONE_FOUND` DirectionEvidence:**
  - D-APP-99: grep of `_REGISTER.md` for D-APP-99; grep of DEL-09-06 run records and Evidence for `2,000`,
    `D-APP-99` and `secret-scan-summary`; the AgentRuns APP_V3_* names. None records a reason.
  - D-APP-127: grep of `_REGISTER.md`, plus `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/{HANDOFF,RUN_LOG,...}.md`
    for ScopeOfWork/_CONTEXT revision. None records why the SoW-level carriers were left unrevised.
  - REGISTER-4: grep of the register and CONTEXT for any rationale for the blank lines. None found.
- **R4-Q1.** No row cites it. The only code evidence that is not LIVE is TEST_ONLY on D-APP-89, a module-level
  claim met as intended by the rollback probe. No LEGACY_ONLY code meets any claim.
- **Cross-ledger observations, not dispositioned here:**
  - DEL-02-02 `_STATUS.md:21-23` and DEL-08-02 `_STATUS.md:24-28` still gate a parity rerun on an accepted
    D-APP-88 helper, which D-APP-127 retired.
  - The Checks lines of DEL-09-04-V3-01, DEL-02-02-V3-01 and DEL-09-06-V3-07 still require the A1 re-stage
    declaration, which D-APP-127 superseded.
  - DEL-02-02 `_STATUS.md:18-19` says the "current" All-sessions presentation is accepted, but the label is gone.
  - DEL-02-03 `_STATUS.md:16` says the D121 addition takes effect "only after owner ruling", but the ruling exists.
  - `execution/_Scripts/app_hold.py:51` keeps a dormant `BOOTSTRAP_AUTHORITY = "D-APP-104"`.
  - Instruction roots when packaged: `main.ts:414-415` gives the App `resourcesPath`, while `main.ts:441-444`
    gives the service `resourcesPath/instruction-root`. D-APP-127 says the service resolves "the same way the App
    does"; this is unverified and low confidence.
  - The done-declaration questions Q-01..Q-13 were not consulted.

## 5. Method friction

- **Superseded-after-landing has no dedicated token.** `EFFECT_NOT_LANDED` does not separate "never landed" from
  "landed, then superseded". I added `EFFECT_LANDED_THEN_SUPERSEDED` in Notes. Proposal: make it a recognised
  token for DEC ledgers.
- **Planning-only and authorization-only rulings.** For rulings such as D-APP-87, 90, 91, 94, 102 and 103, "did
  the effect land" reduces to "was the authorized act performed or recorded". Proposal: say so explicitly for
  item 3.
- **RETIRED_BY_RULING versus ACCEPTED_DIVERGENCE** is under-specified for superseded rulings. I used
  `RETIRED_BY_RULING` when the later ruling names the earlier record or item as superseded, and
  `ACCEPTED_DIVERGENCE` when it replaces behaviour without naming it (96, 114.2) or when the displacing act is an
  owner direction (112.2).
- **The read boundary hides Root-side effects.** The Root validator (D-APP-106), the routed Root notices
  (D-APP-108, 120, 101) and the Root/Runtime owning instruments (D-APP-125, 126) all lie outside it. Proposal:
  either grant read access to named Root paths for DEC work, or accept `UNKNOWN` for Root-side effects.
- **Paths that are not product code still need REACH tags.** The validator's code-path regex requires a REACH tag
  on `frontend/package.json` and `frontend/tsconfig.electron.json`. I tagged them `REACH=LIVE` and explained
  in Notes. Governance scripts (`app_hold.py`) were cited only in Notes, to avoid a spurious `LEGACY_ONLY`/R4-Q1
  tag.

## 6. Effort

- **Read:** about 45 ruling and packet sections, the 38 register rows, about 25 deliverable `_STATUS.md` excerpts,
  about 15 code files (in excerpts), the three evidence-pack CSVs, and about 10 read-only `git log`/`git show`
  lookups against the frozen tree.
- **Context budget:** tight but sufficient. I read the rulings' effect sections in full; for large carriers I read
  grep hits only.
