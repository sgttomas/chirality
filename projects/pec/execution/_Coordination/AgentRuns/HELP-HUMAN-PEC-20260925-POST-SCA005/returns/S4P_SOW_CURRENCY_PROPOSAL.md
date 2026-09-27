# Return — S4P: S4 Scope of Work currency packet preparation (D-PEC-102, reserved)

WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S4. Brief `briefs/S4P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `d00a739afc1f4bc03bd5bd9862fb104d880c22ccce6859dbe85c7e588802dc67`, verified). Resume directions from HELP_HUMAN were relayed after two host-forced interim handbacks. Model: `claude-opus-5-5` (host-reported), at `high` (instruction-asserted), for the manager and every child.

## Result

- **PR:** https://github.com/sgttomas/chirality/pull/990, branch `claude/pec-s4-sow-currency-proposal`, base `main`. Not merged. The head is the commit that adds this return. The preparation content is final at `0ba771eac`; see the PR for the head SHA.
- **Draft:** `projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/DRAFT_D-PEC-102_s4_sow_currency_proposal.md`, SHA-256 `cc01a5fdea02b2883c5afae91212662cbddc0d078ddd207b44824bc75623b1ba`.
- **Recommended option:** **A**. One run of the bound `apply_s4p.py` (SHA-256 `2b6792fee7b69266ad28f517734f89f9c01b60c6e6d4489118fd14375f364869`) replaces eight existing contracts with exact postimages. There is no lifecycle change. Add-on M is separate.
- **Number:** PR #989 reserved D-PEC-102 in the register (`NOT_PREPARED`). It becomes final on publication.
- **Worktree:** isolated at `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-s4-sow-currency`, created from fresh `origin/main` `125cfacc1`. The host's write hook refused writes to it from the parent's worktree, so I switched into it with the EnterWorktree tool. The parent checkout was not modified.

## Candidates (paths under `projects/pec/execution/`)

| Deliverable | Preimage | Postimage |
|---|---|---|
| DEL-04-01 | `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` | `98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0` |
| DEL-04-02 | `a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a` | `bcd69f503acf308e2ef7e73cc722efd61b59710877a5561624260aad71736b11` |
| DEL-08-01 | `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` | `b8c021f581448d1ff5413938563d40b015672aefede15ed97da9dd9b92865e01` |
| DEL-08-03 | `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` | `d4bb8ffa475a7165a00f4d383a210f3d232dd16af3a971b87d9c1bad77cf81bf` |
| DEL-08-04 | `6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b` | `16d731a51556cb644220c2c532696d8d0144972e20576db29495e200a775404c` |
| DEL-04-03 | `6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d` | `10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18` |
| DEL-03-04 | `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02` | `5f7bd434694c8a87bba512ba74a8b8f2dee4f5e2a0ab10e5a50c234e432b196f` |
| DEL-10-03 | `cbcabbde6882baf5330e90cdd6e1cf4a9d9aa1da076643a27f84ff4cb7696ff8` | `e0df75bdcbdeaa2ecd0c320a3c36082c7c47551f2f514392856c761a96b99865` |

No ID is retired in any of the eight. New IDs follow the highest existing number for each prefix. Each contract has a rebuild-provenance `AX-*`.

## Lifecycle answer

- All eight are `INITIALIZED` at `125cfacc1` and at `d385b6a19`. None is `CHECKING` or `ISSUED`.
- The method (`NO_STATUS_TOUCH`) implies no transition, so no add-on S is offered. The act pins every `_STATUS.md`.
- **Disclosed:** DEL-04-01's `_REVIEW.md` records the owner's 2026-08-09 `ACCEPT_EXACT_BYTES` for the preimage `6f4e8c66…30ae`. It also says "Any SOW byte change invalidates this acceptance and requires a new checklist derivation and REVIEW rerun." Ruling A therefore lets that acceptance lapse. The postimage stands `INITIALIZED` with no artifact acceptance.
- No review is opened or prompted, and nothing asks about CHECKING.
- Among the eight, only DEL-04-01 has such a record.

## Part B landing (D-PEC-99 exhibit `69b646f8…f45e`)

| Item | Landing in the postimage | Gate |
|---|---|---|
| DEL-04-01-REM-001 | subsection L273; statement that the gates still bind L277; clause L281 and Gate L283 verbatim; mapping L285; trace table L297–344 (all 46 prior REQ/AC/VER) | still binds (separate owner-ruled DEL-04-01 production packet, WORKING_ITEMS activation, reliance preflight) |
| DEL-04-01-REM-002 | clause L289 and Gate L291 verbatim; mapping L293; the three verification sentences verbatim at L421–425 | still binds |
| DEL-04-02-REM-002 (5 parts) | L19 (qualifying sentences L20–24), L172, L174, L381, L307 and L446; Gate quoted at L389 | met only for the tabled wording if the owner rules A |
| DEL-04-03-REM-002 (3 parts) | L20 (qualifying sentences L21–25), L213, L383; E-P34 block unchanged at L215–223; Gate quoted at L388 | met only for the tabled wording if the owner rules A |

Owner question 2 asks the owner to confirm this reading.

## Downstream and anchor accounts

- **Dependency quotes.** DEP-08-04-004, DEP-08-04-006 and DEP-08-05-005 stay raw substrings of the postimages. Corpus-wide quote currency is 127/127, identical before and after. No register is written.
- **External qualified citations resolve** (57/57 across sibling and external citations). The external ones:
  - DEL-04-05 → DEL-04-01 REQ-001 and REQ-006, and DEL-04-03 REQ-001, REQ-008 and CON-003;
  - DEL-01-01 and DEL-02-07 → DEL-03-04 CON-004, which is byte-identical.
- **Anchors that go stale** (listed, not changed):
  - **DEL-04-05** (S1):
    - `CLM-013` quotes DEL-04-01 `REQ-001`, which now has seven components ("no eighth"), and `CON-004` ("seven stated absences"). DEL-04-05's own "six components, no seventh added" and its `CON-003` go stale with them.
    - `CLM-012` quotes DEL-04-03 `CON-003`, which is re-derived from PEC-RCN-002 v2.4.
    - DEL-04-05's `CON-003` premise may go partly stale because of DEL-04-03 `REQ-018`.
  - **DEL-10-11** (no current node): `CLM-014` quotes DEL-03-04 `CON-001` and `CON-005`. I suggest the graph record this for a later DEL-10-11 currency pass.
- **Kept anchors:** DEL-04-01 `REQ-006`; DEL-04-03 `REQ-001`, `REQ-005` and `REQ-008`; DEL-10-03 `OUT-001` and `REQ-007` (quoted by DEL-10-02); DEL-03-04 `REQ-003`, `REQ-007`, `REQ-013`, `CON-004` and `TBD-005`.
- **S2 quotation currency.** The four S4 members among D-PEC-100's fifteen are brought current. The scan on the postimages finds stale=0.
- **Recommended ordering:** rule S4 before S1 is finalized, so S1 absorbs the DEL-04-05 anchors at its own basis.
- **K2 (`D-PEC-103`, ruled):** K2 cites no S4 local ID, and its act writes none of this act's targets or pins, so either act may land first.
- **Stale text found in passing**, reported and not repaired:
  - DEL-01-05 `CLM-009` (old PEC-API-001 text) and `CON-001` (old SOW-083 text);
  - DEL-01-03 (old §12 P1 row);
  - DEL-08-02 (`CHECKING`): an abridged revision-1.2 OBJ-001 row;
  - DEL-10-02: renders DEL-10-03 `OUT-001`'s double quotes as single quotes;
  - DEL-04-02 `_DEPENDENCIES.md` has no `D-PEC-65` note.

## Checks

All checks ran on `git archive` exports, never on a checkout. Python 3.13.7.

- **`run_s4p_checks.sh` at `origin/main` `d385b6a19` (observation `125cfacc1`): OVERALL PASS** (`evidence/run_main/`):
  - act: check-only 0, apply 0, second run refused;
  - containment: exactly 8 `ScopeOfWork.md`;
  - `PASS format=SOW_V1` ×8; checklists byte-identical on rerun; no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM`;
  - quotes 740/740; state claims 1144/1144; IDs 57/57; S2 scan stale=0;
  - strict (0 errors, 26 XRG-013), harness and receipts identical before and after; quote currency 127/127;
  - whitespace clean; fault injection 9/9.
- **Negative controls:** 6/6 tripped.
- **Reliance preflight:** `exact-correction-preparation` ALLOW ×24 (the register has a header and no rows).
- **Pins:** all 19 pinned files and 8 preimages are unchanged from `125cfacc1` through `d385b6a19`.

## Verdicts (fresh read-only `pec-reviewer`, one per verdict, in the preparation folder)

| Verdict | Head | Scope | Result |
|---|---|---|---|
| 01 | `396c6f744` | DEL-04-01, DEL-04-02, DEL-04-03 | FAIL: DEL-04-02 said "six" components; repaired |
| 02 | `396c6f744` | DEL-08-01, DEL-08-03, DEL-08-04 | FAIL: DEL-08-03 `CON-007` routed an owner-reserved question to production; repaired |
| 03 | `396c6f744` | DEL-03-04, DEL-10-03, packet | PASS WITH NOTES |
| 04 | `cf23df7df` | re-verification of DEL-04-0x and DEL-10-03, plus the draft | PASS WITH NOTES |
| 05 | `cf23df7df` | re-verification of DEL-08-0x | PASS WITH NOTES |
| 06 | `7da048c83` | final bytes and packet | PASS WITH NOTES: the DEL-04-01 acceptance-lapse disclosure was added |
| 07 | `e09b25efa` | final draft delta | PASS WITH NOTES: record and re-anchoring notes applied as text only |

Nothing blocks at the final bytes. Every note is dispositioned in its verdict file.

## Owner questions (in the draft)

1. A, amend or defer. Recommend A. This question includes the note that DEL-04-01's exact-byte acceptance lapses.
2. The Part B reading. Recommend confirm.
3. Two readings. Recommend confirm both:
   - (a) DEL-04-01 has **seven** components (terminal completion);
   - (b) DEL-04-03's reliance envelope sits beside the stamp and is not a stamp field.
4. Add-on M: eight new `MEMORY.md` files at closeout. Recommended.
5. Models: keep the defaults.

## For HELP_HUMAN to resolve

- **Publication.** Publish the draft in `_DECISIONS/` and move the D-PEC-102 row to `AWAITING_RULING`. Consider refreshing the check commit (`d385b6a19`) at publication.
- **Work graph.** Record the DEL-10-11 stale-quotation item and the DEL-04-05 anchors for S1.
- **A point outside this packet.** Verdict 06 notes that the D-PEC-100 act replaced DEL-02-07, whose `_REVIEW.md` also records an owner `ACCEPT_EXACT_BYTES`, and D-PEC-100 did not disclose it. Whether to record that lapse is for HELP_HUMAN.
- **Scratchpad.** Verdict 07's reviewer left a stray file, `scratchpad/k2draft.txt`, outside its mktemp directory. I did not delete it because I did not create it. My own scratch is under `scratchpad/s4p_mgr/`: the stage, exports and notes. Only I use it.
- **Git state.** No merge. The branch has no merge from `origin/main`: its base is `125cfacc1`, and the checks ran on exports of current main.

## Sources relied on (at `125cfacc1` unless stated)

- **Instructions:** root `AGENTS.md` `c8ce87ef…1dffd`; `projects/pec/AGENTS.md` `df9196d1…5eb8`; `agents/AGENT_WORKING_ITEMS.md` `9ae4bea2…9665`; `agents/AGENT_TASK.md` `1a13a5b0…8fb7`.
- **Method:** `workflows/scope-of-work/WORKFLOW.md` `84dadde4…bc2b` (with `execution.json`, `resources/brief.md`, `checks.md`, `tools.md` `fbd07771…5cc7`); `workflows/index.json` `2bfa2c5f…fb3`; the standard `26c8254a…433c`.
- **Basis:** decomposition revision 1.6 (the four files, identical at the pin `189f205ff`); PRD v2.4 `ae49b806…3fbe`.
- **Scope-change records:** SCA-006 `Propagation_Plan.md` `f95d00d1…d7d8` and `Impact_Assessment.md` `93253b7d…b691`; SCA-005 `Propagation_Plan.md` `50cd0b1d…1350`.
- **Rulings:** D-PEC-90, 94, 96, 98, 99, 100 and 101 (hashes in the draft's basis table); D-PEC-99 exhibit `69b646f8…f45e`.
- **Work graph and register:** `8296ad0c…b148`; `_REGISTER.md` `33b43ae8…5a2f` (at `125cfacc1`; the D-PEC-102 reservation was added later in PR #989).
- **Drafters' shared brief:** `DRAFTER_BRIEF.md` `d795dbca…fb70d` (in the preparation folder).
- **Children dispatched:** eight `pec-task` drafters and seven `pec-reviewer` verdicts, all `claude-opus-5-5` through the host's Agent tool with `subagent_type` set. The drafters ran in the background and the reviewers in the foreground. Their returns are transcribed or summarized in the preparation folder.
