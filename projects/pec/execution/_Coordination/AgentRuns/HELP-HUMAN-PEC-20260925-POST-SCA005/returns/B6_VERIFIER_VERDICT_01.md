# B6 verifier verdict 01 (saved verbatim)

The verifier was a fresh `pec-reviewer` instance (Claude Code Agent tool, `model: opus`, which the host maps to Opus 5.5), with no write tools, that authored nothing in this candidate. It was dispatched by the WORKING_ITEMS manager for brief B6. It reviewed candidate head `9a8b7150d3f4e8b6422cde759638e419e47fe5aa`.

The manager saved the report as returned; only the harness indentation was removed. The manager's repairs are listed at the end.

---

# B6 independent verifier verdict 01: SCA-006 checkpoint-3 preparation (PR #943, candidate head `9a8b7150d3f4e8b6422cde759638e419e47fe5aa`)

**Verdict: BLOCKING.** There is one blocking finding. It sits in the checkpoint-3 question set and the A6 instructions. The applied Lane A bytes are not affected: the decomposition, registers, PRD, contexts, `AGENTS.md`, manifest and notices all verify, and so do C1 through C5. The repair touches records only. I also have one MINOR finding and seven NOTEs.

I worked read-only as a fresh TASK verifier and authored nothing in this candidate. I made no writes in the repository; scratch output is under `/private/tmp/claude-501/.../978bf4ac-.../scratchpad/`. I make no CHECKING, ISSUED or acceptance claim.

## Basis read (SHA-256 recomputed)

- Root `AGENTS.md`: `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/pec/AGENTS.md` at `94e9255b6`, read as my instructions: `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`
- Brief B6 at `94e9255b6`: `8bdc718105f05dd2f72378e50fea246eb99a38a937938da72afa221bb8872df4`. This matches the required value.

**Method.** I reviewed committed bytes only:
- `git archive 9a8b7150d` and `git archive f90320c1d` into scratch;
- basis preimages from `git archive 94e9255b6`.

The worktree HEAD is `9a8b7150d` and it is clean (`git status --short` is empty before and after my runs). The candidate diff is `git diff --name-status f90320c1d 9a8b7150d`, which lists 46 paths.

## Findings

### 1. BLOCKING: the A6 instructions and the post-A6 hash leave out the `accepted:` acceptance-date slot

**What the accepted instruments say:**
- `Amendment_Preview.md` (accepted `737af0e6…`) §"Acceptance-bound tokens", L39–44, lists **four** decomposition slots that take the checkpoint-3 acceptance date:
  - `date:`
  - front matter `accepted:` (L42)
  - the §7 Revision row
  - the DL-21 cell
- Its hash rule is at L37.
- `Propagation_Plan.md` (`f95d00d1…`) L249, §A6, says: "The decomposition front-matter lines return to their accepted postimage values". Those values include the `accepted:` slot.

**What the package says:**
- `RUN_SUMMARY.md` L81 treats `accepted:` (L8) as having no slot ("accepted values").
- The A6 note (L98), the §9 A6 bullet (L268) and `Handoff_State.md` A6 steps 2–3 substitute the acceptance date at "exactly these three loci" only. They say to "restore the accepted `accepted:` line" unchanged.

**The hash handed to the owner is inconsistent.** `RUN_SUMMARY.md` L94 and L257 (Q-CP3-A) and `Handoff_State.md` A6 step 3 give the post-A6 file as `86de50c3b56812dec9537210c0202ec9efc98aac7b328a8736cac8a6c688ecb3`. I reproduced that hash. It mixes two dates:
- `date:`, the Revision row and DL-21 at 2026-09-26;
- `accepted: 2026-09-25 (…revision 1.6 successor accepted through SCA-006…)`.

Revision 1.5's line shows that this date token is the latest acceptance date: `accepted: 2026-09-25 (…revision 1.5 successor accepted through SCA-005…)`.

**Consequence.** If HELP_HUMAN follows these instructions, the decomposition will state that revision 1.6 was accepted on 2026-09-25, a date on which it was not accepted. The owner would also be accepting a derived hash that the preview's slot rule does not produce.

**Correct value.** For acceptance on 2026-09-26, fill all four slots. I computed:
- restore candidate L5 and L8 on the live file;
- set L8 to `accepted: 2026-09-26 …`;
- SHA-256 = `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`.

The C4.3 review (note 3) also named only three loci.

**Repair (records only; no Lane A byte changes):**
- In `RUN_SUMMARY.md`, add `accepted:` as the fourth acceptance-date slot:
  - §3.1 row L81;
  - slot proofs L94;
  - A6 note L98;
  - §9 L257 and L268.
- In `Handoff_State.md` A6 steps 2–3, do the same.
- Replace `86de50c3…` with `9374c21f…` (for 2026-09-26), or state the rule for other dates.
- Update the `RUN_SUMMARY.md` hash in `Decision_Log.md` §"SCA006-CP3 — package prepared".
- Correct C4.3 disposition 3.

### 2. MINOR: the hunk is faithful, but the record overstates what it keeps

**The hunk is faithful and bounded.** It covers every amendment-1 bullet:
- no new sections or entries;
- no feed profile reads them;
- new open scope goes to the graph;
- status quo until a retirement ruling;
- gate markers still bind;
- updates only under the packet that opens the `_STATUS.md`;
- retirement remains a separate owner-directed undertaking.

It decides no retirement.

**On the dropped clause** ("its graph accounts for the Remaining items it touches"): dropping it is acceptable. It fits "There must not be any of those going forward", and the owner approved after being shown the clause.

**Where the record overstates.** The stated rationale, that the clause "implies each undertaking's graph looks for Remaining items", is a stretch: the clause only applies to items an undertaking already touches. The record also says (`AGENTS_MD_AMENDMENT1_DIFF.md` §2, and `RUN_SUMMARY.md` L136) that the touched-item duty "is kept". That is only partly true:
- the candidate's positive duty, "When an undertaking completes or changes an item, update it under the packet…", is now a restriction, "Update an item only under the packet…" (applied L269);
- "changes" became "affects".

With the graph clause also gone, an undertaking that holds a grant has no explicit duty left to update an item it completes.

**Repair.** No byte change is needed, since the owner approved `4400c4e9…`. Add one disclosure sentence in `AGENTS_MD_AMENDMENT1_DIFF.md` §2 and in `RUN_SUMMARY.md` §3.2, or treat this verdict as that disclosure.

### 3. NOTE: the approval record is attributed correctly and names the exact bytes

These three records all carry "approve hunk", 2026-09-26, name `projects/pec/AGENTS.md` `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`, and attribute the act to HELP_HUMAN's K-AUTH-1 relay:
- `Decision_Log.md` row SCA006-G2-A1 and its section (L136–152);
- manifest `group2_amendment_1.owner_hunk_approval`;
- `RUN_SUMMARY.md` §3.2.

On `origin/main`, `D-PEC-96_RULING_2026-09-26.md` (`852057f0…399e`) independently records that the same owner message "also carried 'approve hunk', which answers SCA-006 group-2 amendment 1". That record does not name the bytes.

"Gate satisfied" is the manager's conclusion from the relay, which is acceptable. At merge, HELP_HUMAN should confirm that the paragraph it presented equals applied L261–272.

### 4. NOTE: Q-CP3-A cites the hunk and the closure fields by reference

Q-CP3-A cites the hunk as "quoted verbatim in §3.2" and the closure state as "the §7 fields", rather than inline. This is acceptable within one file. Inlining them is optional.

The open choices are:
- Q-CP3-1: COV-083; option (a) is sound.
- Q-CP3-2: the audit pointer. `D-PEC-97` does not open `_Evaluation/DecompCoverage/_LATEST.md`, so this is a genuine choice.

Each has a recommendation. Nothing asks about CHECKING.

### 5. NOTE: the rollback note names more notices than it should

The rollback note (`RUN_SUMMARY.md` L270; `Handoff_State.md` A6 step 5) refers to "the notices' present-tense 'revision 1.6 adds …'". Only the Runtime notice (L38) has that wording.

### 6. NOTE: C4.3 disposition 6 has a wrong locator

The disposition says the R-rerun method is in `RUN_SUMMARY.md` §4. It is actually in §8 (L241) and in `AGENTS_MD_AMENDMENT1_DIFF.md` §4.

### 7. NOTE: the interim return has a typo and a superseded claim

The interim return (`850ad9e0…66ac`) quotes the group-2 `DECISION.md` as `30aebd16…a989`. The actual hash is `30aebd162e98…87abf989`. Its "diff --check clean" claim is already disclosed as superseded. The final return should use the correct hash.

### 8. NOTE: C1 wording in `RUN_SUMMARY.md` §4

The C1 text reads "14 planned postimages, the manifest …". The manifest is one of the 14; the count is 14 + 20 frozen = 34 checks.

## Confirmations by brief item

**1. Live poststate.**
- Decomposition:
  - `3ef0412a…9b29` differs from candidate `4eed1247…` only at L5, L7, L8, L574 and L700;
  - reversing the three 2026-09-26 slots gives `3ad0de686616…8a8b`, and restoring L5 and L8 as well gives `4eed1247…2d62`.
- Registers and PRD: `cmp` shows each is equal to its CP2_CANDIDATE file:
  - `1d24a4b8…`
  - `94ee5d18…`
  - `93b0bb07…`
  - `1597ceec…`
  - `ae49b806…7fbe`
- A2 contexts: `b28ada46…7b22`, `74b12e73…2d22` and `95fa815a…37b5`, each equal to its plan postimage.
- `AGENTS.md`:
  - the candidate with L6 filled gives `6f6f2ed1…64e6`;
  - candidate L1–260 equal applied L1–260, and candidate L271 onward equals applied L273 onward;
  - L260 and L271 are blank;
  - the only other change is the hunk.
- Every group-2 `ACCEPTED_MANIFEST.csv` artifact matches its hash, apart from the two living logs.

**2. Hunk.** See finding 2.

**3. Approval record.** See finding 3.

**4. Containment.**
- All 46 paths are inside the Lane A allowlist, the snapshot folder, the COV folder or the B6 return.
- The SCA-006 folder shows only A, except `Decision_Log.md` and `Handoff_State.md`.
- There are no writes to `checkpoint_snapshots/**`, `_LATEST.md`, `_STATUS.md`, any SOW, `Dependencies.csv`, `v2/**`, `pec.yaml`, `docs/STATUS.md` or `_DECISIONS/**`.
- Checkpoint-1 artifacts match the group-1 manifest.
- Both pointers are unchanged: `626feaaf…`, `e92b3b16…`.

**5. C1–C5 reruns (cwd is the worktree, Python 3.13.7):**
- `c1_containment.py` over `git diff --name-status f90320c1d 9a8b7150d`: exit 0; 46 paths, 34 hash checks, 0 fails.
- `validate_decomposition_registers.py projects/pec/execution --strict`: exit 1 by design.
  - 0 ERROR.
  - 2 DRB-008: DEL-08-06, DEL-10-13.
  - 26 XRG-013. They are exactly the 26 revision-1.5 OUT/TBD items with no PackageID (the same IDs at 1.5 and 1.6). SOW-097..100 are IN with packages PKG-04/08/08/10.
- `analyze_dep_closure.py`: exit 0; 111 edges, 66 nodes, 0 SCCs.
- `c3_assert.py <preimages from 94e9255b6>`: exit 0, 31/31. The output is byte-identical to the committed `c3_result.json`.
- `c5_completeness.py`: exit 0. The output is identical to `c5_result.json`.
- Accumulator rerun reproduces `Supersession_Map.csv`: `010ce5c4…ab92`, 45 rows, 0 findings.
- `Post_Change_Coverage.json` equals the audit's `coverage_summary.json`.

**6. Audit reading.**
- COV-068/069/072 are attributed to `D-PEC-95` N2/N3.
- COV-073 is PARTIAL: N1 covers the pointers, and the residual is carried as COV-086 INFO.
- All 12 EXPECTED_CONSEQUENCE rows cite `D-PEC-97` plus a plan section (§B1/B2/B3/B7/A2/A5/A6).
- Severity counts from the IssueLog are 0 BLOCKER / 3 WARNING / 71 INFO / 12 EXPECTED_CONSEQUENCE. They match `RUN_SUMMARY.md` §5.
- The COV-083 cited loci are correct: `SOFTWARE_DECOMP.md` L259 and L652, `ScopeLedger.csv` L72, `Deliverables.csv` L10.
- `v2/config/loops.json` declares no `feed_profiles`.
- The account of `D-PEC-96` is accurate: PEC's row is migrated with profiles `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, and the decomposition text is routed to S2 and a later scope change.

**7. Manifest and notices.**
- My own extraction of the §6.1 and §6.3 drafts gives:
  - manifest `852b1d5b…`
  - Root `43cfa318…`
  - App `eb927e1f…`
  - Runtime `385e5e2f…`
- `diff` shows only slot fills plus one named amendment-1 addition in each file.
- `verify_manifest.py` reports MATCH.
- `authorization_date` stays 2026-09-25.
- The notices grant nothing.
- G4 CI mode: exit 0 (126 manifests).
- G4 `--base f90320c1d --head 9a8b7150d --added-manifests-only`: exit 0 (46 paths, 1 on the instruction surface, covered by 1 manifest).
- `validate_instruction_entrypoints.py .`: exit 0.
- `validate_pec_loop_receipts.py --repo-root .`: exit 0.
- `pec_reliance_hold.py --target AGENTS.md --operation candidate-validation`: ALLOW. The hold register has a header and no rows.

**8. C4.3 review.** Its dispositions 1, 2, 8 and 9 are carried out as stated. Disposition 3 is incomplete (finding 1), and disposition 6 has a wrong locator (finding 6). I cannot prove the review is verbatim without the original return. Internally it is consistent.

**9. Question set and A6.** See findings 1 and 4.

**`git diff --check`.** Only `Supersession_Map.csv` is reported, with 46 lines. It is CRLF, as SCA-005's map is (30/30 lines). Every other changed path is clean. This is not blocking.

## Recomputed hashes (head `9a8b7150d`)

| File | SHA-256 |
|---|---|
| `projects/pec/AGENTS.md` | `4400c4e9…139c` |
| `SOFTWARE_DECOMP.md` | `3ef0412a…9b29` |
| PRD | `ae49b806…7fbe` |
| Manifest | `2b29af18…ee74` |
| Root notice | `b3c60bf4…c601` |
| App notice | `af4f6342…68ef` |
| Runtime notice | `e883efac…bb93` |
| SCA `RUN_SUMMARY.md` | `fd0f8a73…4ca2` |
| `Decision_Log.md` | `9558a099…9d8a` |
| `Handoff_State.md` | `eef22a0c…d3b` |
| `AGENTS_MD_AMENDMENT1_DIFF.md` | `0202158b…c111` |
| `C4_3_REVIEW.md` | `3caacea4…402d` |
| Audit `RUN_SUMMARY.md` | `f97bde4e…6499` |
| Amendment-1 `DECISION.md` | `15720eb1…777e` |
| Group-2 `DECISION.md` | `30aebd16…f989` |
| B6 interim return | `850ad9e0…66ac` |

Every hash cited in the `Decision_Log.md` CP3 table matches. The one exception is the derived post-A6 decomposition hash `86de50c3…` (finding 1).

---

## Manager repairs after verdict 01

| # | Repair |
|---|---|
| 1 | The manager confirmed the finding and recomputed `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`. `accepted:` is now the fourth acceptance-date slot in `RUN_SUMMARY.md` §3.1, the slot proofs, the A6 note and §9, and in `Handoff_State.md` A6 steps 2–3. `86de50c3…` is replaced by `9374c21f…` (acceptance on 2026-09-26), with the rule for other dates. C4.3 disposition 3 is corrected. The `Decision_Log.md` CP3 hash for `RUN_SUMMARY.md` is updated. No Lane A byte changed |
| 2 | Disclosure sentences added in `AGENTS_MD_AMENDMENT1_DIFF.md` §2 and `RUN_SUMMARY.md` §3.2: the rationale is softened, and the loss of the explicit positive update duty and the change from "changes" to "affects" are stated. The hunk bytes are unchanged, as approved |
| 5 | Rollback note narrowed to the Runtime notice |
| 6 | C4.3 disposition 6 locator corrected to `RUN_SUMMARY.md` §8 and `AGENTS_MD_AMENDMENT1_DIFF.md` §4 |
| 7 | The final return uses the full group-2 `DECISION.md` hash `30aebd162e98cdc91923468852af6833feda84c3a3d9d3efe252dc8a87abf989` |
| 8 | C1 wording corrected to "14 planned postimages (the manifest among them) + 20 frozen = 34" |
| 3, 4 | No change needed |
