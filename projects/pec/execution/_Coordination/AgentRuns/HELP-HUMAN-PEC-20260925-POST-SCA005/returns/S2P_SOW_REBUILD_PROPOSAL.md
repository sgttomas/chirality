# Return — S2P: S2 Scope of Work rebuild packet (provisional D-PEC-100)

Role: WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, graph node S2. Brief `briefs/S2P_SOW_REBUILD_PROPOSAL.md`, SHA-256 `31313b8fafc7fd25ea351eb2826a9e3c64cd5c5f9541f169a5f451a2cb6692d3` (verified before starting). Date 2026-09-26. Host: Claude Code; the host reports the serving model as Opus 5.5 (`claude-opus-5-5`); role and `high` effort are instruction-asserted.

**Result:** the packet is prepared and published as PR #964. It is **not merged**. No production file was written.

## Brief amendment received (recorded as evidence)

HELP_HUMAN relayed a replacement for the brief's "Method choice as an owner option" bullet. The Root notice says the owner defers action in PEC and "no adoption … is expected in this loop now". So adoption of `scope-of-work` `MODE=REVISE` is **not** put to the owner. The packet follows PEC's current practice (the `D-PEC-98` precedent) and mentions the new mode only as a one-line disclosure. A later relay asked me to resume after a host-forced handback, finish steps 1–5, confirm nothing pinned changed at the new `origin/main`, and state add-on M's exact files and rows. All of this is done.

## Publication

- **PR:** https://github.com/sgttomas/chirality/pull/964 — branch `claude/pec-s2-sow-rebuild-proposal`, base `main`.
- **Head at the last check run:** `541090b00ebcbc97c5d0bbc08c6eec6e83ce5af7`. The commit that updates this return follows it (see the PR).
- **Worktree:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s2-sow-rebuild`. It was created from fresh `origin/main` `aca930622`, and `origin/main` was merged in as it moved; the last merge was `121900105` (PR #966). The caller's checkout was not modified. A PreToolUse hook blocked Write tool calls into a second worktree, so I entered the new worktree with `EnterWorktree`.
- **"Update the PR base" failures:** none seen.

## Draft

- **Path:** `projects/pec/execution/_Coordination/PEC_SOW_REBUILD_S2_PREP_2026-09-26/DRAFT_D-PEC-100_s2_sow_rebuild_proposal.md`.
- **SHA-256:** `a6d9abe861ea76a7d87ce5c14d3c49ac71ad4e30d487b73d7fd3219aa16afe8e` (352 lines).
- **Suggested filing name:** `_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md`.
- **Register:** HELP_HUMAN adds the register row. At `121900105` there is no D-PEC-100 row.

## Candidate hashes

Paths are under `projects/pec/execution/`. Each postimage is also at `PREP/candidates/<same path>`.

| Deliverable | Lifecycle | Preimage (current) | Postimage |
|---|---|---|---|
| DEL-01-01 | INITIALIZED | `43f1f57a13bb96b3235bbbb460342bd03518c503f23cb8b0560914f27a2f0170` | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| DEL-01-06 | INITIALIZED | `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| DEL-02-03 | INITIALIZED | `c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872` | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| DEL-02-04 | INITIALIZED | `bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87` | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| DEL-02-05 | INITIALIZED | `192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e` | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| DEL-02-06 | INITIALIZED | `c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8` | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| DEL-02-07 | INITIALIZED | `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559` | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |

- **Bound act script:** `PREP/apply_s2p.py`, SHA-256 `42dc95532fdb39a308f59cf86e2bee73f8cf4f17808e403f42adcb308fc03d20`. It carries 7 TARGETS and 23 PINNED files.

## Recommended option and method

- **Recommended: option A.** One run of `apply_s2p.py` replaces the seven contracts with the tabled bytes. There is no lifecycle change, and add-on M is separate.
- **Scope check.** None of the seven deliverables is in S4, and SCA-006 IA §7.1 classes all seven `NOT_AFFECTED`. The eighth §B4 rebuild contract, DEL-04-01, stays in S4.
- **Method.** The candidates were authored under `scope-of-work` `MODE=INIT` discipline, the D-PEC-98 practice. The act is an owner-ruled exact-bytes **replacement**, and `MODE=VERIFY` is the independent check.
  - This departs from D-PEC-98, which created new files. The recorded edition's INIT precondition ("no production contract exists") is not met literally, so the draft discloses the departure.
  - `REVISE` appears only as the one-line disclosure. It is not an owner question.
- **Split options.** A per-deliverable split is not offered with these bytes, because the candidates cite each other's postimages. A split would need re-drafting.

## Lifecycle answer

- All seven deliverables are `INITIALIZED` at `aca930622` and at `121900105`. The brief expected five, and I checked each one.
- None is CHECKING or ISSUED.
- The method does nothing to `_STATUS.md` (WORKFLOW "Do not modify `_STATUS.md` …"; checks item 3). Standard §8's `INITIALIZED` condition still holds after the act.
- **No transition is proposed.** The act pins all seven `_STATUS.md` files and refuses to run if any has changed.

## Part B landing (DEL-02-07 postimage)

Each carry-forward and Gate line is verbatim, in a blockquote with the carve-out sentence. CLM-016's introduction (L135–137) and AX-011 (L268) state that the gates still bind.

| Item | Lines (carry-forward / Gate / mapping) | Local IDs |
|---|---|---|
| DEL-02-07-REM-001 | L141 / L143 / L145 | OUT-001, REQ-002, REQ-007, REQ-009, REQ-011, AC-001, AC-005, AC-009, AC-011, VER-001, VER-005, VER-008, VER-010, TBD-002, TBD-004 |
| DEL-02-07-REM-002 | L149 / L151 (with the CON-002 gate) / L153 | CON-002, TBD-003, REQ-003, REQ-013, AC-002, AC-013, VER-002, VER-012, CLM-006, CLM-007 |
| DEL-02-07-REM-003 | L157 / L159 / L161 | REQ-004..007, AC-003..006, VER-003..006 |
| DEL-02-07-REM-004 | L165 / L167 / L169 | OUT-002, REQ-008, REQ-016, AC-007, AC-016, VER-007, VER-015 |

## Check results

Final `run_s2p_checks.sh` at `origin/main` `121900105` (`PREP/evidence/run_main/SUMMARY.out`), run on `git archive` exports: **OVERALL PASS**.

- act: check-only 0, apply 0, rerun refuses 1
- containment: exactly the 7 `ScopeOfWork.md` files
- `PASS format=SOW_V1` ×7; checklists rerun byte-identical; boundary check shows no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`
- quotes 460/460, both sides; this includes the 7 raw dependency `EvidenceQuote` spans
- state claims 1280/1280
- sibling IDs 92/92
- strict registers, harness self-check and receipts validator produce identical output before and after, with the export root normalized. Strict exits 1 with 28 pre-existing warnings (26 XRG-013, 2 DRB-008).
- whitespace clean
- fault injection 9/9

Other evidence:
- **Negative controls** (`evidence/negative_controls.out`): each control fails as designed. Control 2b replaced the tree-side control 2 after the exhibit quotes were pinned to `aca930622`.
- **Reliance preflight:** `exact-correction-preparation` on all 21 possible targets gives `ALLOW` ×21. The holds register has no rows.
- **`SHA256SUMS`:** lists tracked files only; `shasum -c` passes on a `git archive` of the head.

## Verifier verdicts

Each verdict was given by a fresh read-only `pec-reviewer`. Each is saved verbatim in PREP with the manager's dispositions.

| Verdict | Head | Result | Main points |
|---|---|---|---|
| `VERIFIER_VERDICT_01.md` | `c0919e261` | PASS WITH NOTES | 8 non-blocking notes, all repaired. One candidate wording fix: DEL-02-07 `"this contract"`. |
| `VERIFIER_VERDICT_02.md` | `c7719559b` | FAIL | One mechanical blocker: `SHA256SUMS` listed an untracked `.pyc`. Repaired, with 5 further notes. |
| `VERIFIER_VERDICT_03.md` | `3be700545` | PASS WITH NOTES | Nothing blocking. The changed-ID disclosure and the run-root guard were repaired after it. |
| `VERIFIER_VERDICT_04.md` | `dafce6d7e` | PASS WITH NOTES | Nothing blocking. The run-root guard held against bypass probes. Four wording notes were repaired afterwards; those repairs were not re-reviewed. |

## Owner questions (in the draft)

1. A, amend or defer. The recommendation is **A**.
2. **Part B reading.** Confirm that the ruling places DEL-02-07-REM-001..004 verbatim, with gates **still binding**, and discharges only the exhibit's carry. The recommendation is to confirm. Without an answer, the text is applied and every gate stays binding.
3. **Add-on M, with exact files and rows.**
   - Create `MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`) in DEL-01-01, DEL-02-03, DEL-02-04, DEL-02-05, DEL-02-06 and DEL-02-07. Each gets one `## Runs` row.
   - Append the same row to DEL-01-06's existing `MEMORY.md` (`035ecb86…0a3f`), after the D-PEC-96 add-on row.
   - The row, with `{D}`, `{PR}` and the link slots fixed at closeout:
     `| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | Scope of Work rebuilt under D-PEC-100 (graph node S2). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-100 ruling record> |`
   - Or record the run only in the graph and receipt.
4. Model steer.

No question concerns CHECKING or REVISE adoption.

## What the caller must resolve or know

- **Publication.** Publish the draft in `_DECISIONS/` with its register row. The number D-PEC-100 is provisional.
- **Ordering.** Rule S2 before the S1 and S4 packets are finalized. The act makes verbatim quotations of the prior S2 contracts stale in 15 contracts outside S2, flagged by `scan_external_quotes.py`: DEL-02-01, 02-02, 03-01, 03-02, 03-03, 03-06, 04-01, 04-02, 04-05, 08-04, 10-02, 10-03 and 10-10, plus DEL-02-08 and 02-09, whose quotations are anchored to the old hash. Separately, DEL-02-01's own REQ-002 still names DEL-02-07 as the feed-manifest supplier.
- **D-PEC-101 draft (K4/K1, PR #962).** It shares no path with this act, and either may land first. The draft explains how each ordering is absorbed.
- **Open CON items worth owner attention.** Each is carried in its contract and none is resolved:
  - D-GOV-45 archived run evidence (DEL-02-04 CON-005, DEL-02-05 CON-004);
  - DEL-02-06's workplan grammar has no declared surface under the ruled vocabulary (CON-004), which is also the envelope evidence toward S (CON-007);
  - whether historical workplan gate tokens are emitted (DEL-02-06 CON-009);
  - gate state from scope-change pointers that no feed covers (DEL-01-01 CON-007);
  - DriftFinding fit for a harness-configuration divergence (DEL-01-01 CON-008, DEL-02-07 CON-006);
  - the loop-to-project relation (DEL-02-07 CON-002);
  - register wording left for a later scope change: SOW-013 "live for PEC", SOW-014 "current-by-own-practice for PEC", SOW-094/§9 `remaining-loop` (COV-083), and OI-012 still "undecided" after D-PEC-72 O-B.
- **Kept IDs whose rule changed.** These are listed in the draft's Method section. DEL-01-01 REQ-006 is the only one cited from outside S2 (by DEL-02-09).
- **Drafter returns are not tracked.** They were delivered to this session only; their substance is in the candidates, the verdicts and this return.
- **Disk.** The scratch volume ran near full, at about 98%, from large scratch folders of other runs (`k14p`, `rr1`, `rev.*`, `u1_verifier`). I deleted only my own exports.
- **Graph S2 row.** Marking S2 as packet-prepared, and any receipt entry, are HELP_HUMAN's; I did not edit the graph.

## Execution record

- **Delegation mechanism:** the Claude Code Agent tool, as background subagents under this WORKING_ITEMS session.
  - Seven `pec-task` TASK drafters (opus; model steer `claude-opus-5-5` high), one per deliverable, run in three rounds: authoring, cross-candidate reconciliation, then targeted fixes to DEL-01-01, DEL-02-06 and DEL-02-07. Their shared brief is `briefs/S2P_DRAFTER_BRIEF.md` (`ab7fdc29…43fd`).
  - Four fresh read-only `pec-reviewer` TASKs, one per verdict. None of them authored anything.
  - Children wrote only their three prep files each. The reviewers wrote nothing.
- **Instruction and authority sources relied on** (SHA-256 at `2b5389a97` unless noted):
  - Root `AGENTS.md` `c8ce87ef…1dffd`
  - `projects/pec/AGENTS.md` `df9196d1…5eb8`
  - `agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`
  - `workflows/index.json` `2bfa2c5f…dafb3`, with `scope-of-work` `WORKFLOW.md` `84dadde4…bc2b`, `execution.json` `4ad8b7eb…a26d`, `brief.md` `1696cd9a…92bc`, `checks.md` `44ab41ac…f188` and `tools.md` `fbd07771…6cc5`
  - Standard `26c8254a…433c`
  - Work graph `5cee83f9…6788` (the S2 row is identical at `aca930622`)
  - D-PEC-94 `b6814e90…5a6b`; D-PEC-96 ruling `852057f0…399e`; D-PEC-98 ruling `039dc7e2…8361`; D-PEC-99 exhibit `69b646f8…f45e`
  - SCA-005 `Propagation_Plan.md` `50cd0b1d…1350`; SCA-006 IA `93253b7d…b691`
  - Project-setup incremental notice `8829ac84…64af`
  - Decomposition revision 1.6 and PRD v2.4 at the draft's basis hashes
- **SHA256SUMS:** `shasum -a 256 -c` on a `git archive` of `541090b00`: exit 0, 87 entries, all tracked.
- **Wider consultation:** none beyond the WORKING_ITEMS role. `agents/AGENT_TASK.md` was read only by the TASK children.
