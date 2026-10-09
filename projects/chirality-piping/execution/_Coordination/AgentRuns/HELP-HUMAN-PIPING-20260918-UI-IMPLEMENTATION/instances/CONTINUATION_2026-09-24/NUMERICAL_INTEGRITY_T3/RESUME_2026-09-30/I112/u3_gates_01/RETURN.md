# I112 round 2 RETURN: the U3 PR's T9 and both-entry gate (parts 1 and 2)

**Verdict: T9 PASS. Part 1 PASS. Part 2 PASS. No stop.**

Every difference between B and C falls in a class the brief allows:
- a declared text correction (T2), with its two binding digests recomputed by the product's rule;
- a designed refusal, a legacy pressure primitive now refused with the documented code and text.

No removed case occurs in these corpora. The only other change is the added demo model, whose outputs equal the committed demo results byte for byte. gate_check passes on both sides with 0 trusted breach triples.

**Who and when:** I112 (TASK, Type 2), continued by WORKING_ITEMS for T3 (Agent 1). The brief is `R/BRIEFS/U3_GATES.md` (sha256 `3e907f06…`, verified). Round 1's brief `PR_N_GATES.md`, its grant and its method (I61's) apply. I worked on 2026-10-09 from 02:06Z to about 02:35Z.

**Revisions:**
- **Base B** = `ba500defa498a454be182ed46db795fc3e04d627` (main; PR-B1 and PR-N merged).
- **Candidate C** = `8a12de28db5ede85d3df09d5307e795ff39e4373`, the code commit of U3 PR #1168 (`codex/piping-t3-pressure-retire-pr-20261009`, worktree `WT/u3-pr`). Its parent is B.
- The PR head `98733368f9` adds only the evidence package under `execution/`, which is outside every gate input.

**The branch moved during this run** (an observation; the carry-over is WORKING_ITEMS' ruling). The worktree is now at `3bfcceb4c0`. After C, the only change outside `execution/` is `ed012c7ccf`, which deletes three bundled result documents (G10, D-3): `fixtures/product_preview/invented_mechanics_result.json` and `invented_mechanics_result_precision_1_{dense,sparse}.json`.
- They are `mechanics_result` documents, not requests or models. The T9 harness produced no output for them on either side, and no gate request reads them.
- No file under `core/` names them.

These gates ran on C as briefed.

**Host:**
- The memory guard ran throughout (PID 78827; no KILLED line).
- rustc 1.97.1; python 3.13.14 (`WT/venv/bin/python`).
- **Every cargo** went through `t3_cargo.sh`: the T9 harnesses, the probes and the digest helper.
- **Each part-1 driver** ran as one `t3_slot.sh` job.
- **Part 2** ran only under `t3_exclusive.sh`, one execution, 02:21:17Z–02:29:36Z.
- One heavy job of mine at a time; no other job signalled. My lock-log lines are in `gate/host_jobs_i112_u3.txt`.
- No Git writes; no DEC-025; no installs.
- Targets are under `WT/targets/i112-u3-t9/`, `i112-u3-gate/` and `i112-u3-digest/`; scratch is `WT/scratch/i112_u3/`.

**Trees** (`trees_check.txt`): `git archive` of `projects/chirality-piping` with `execution/` excluded.
- 2,973 files each side (C deletes 6 and adds 6).
- 0 blob mismatches at extraction and after the builds.
- **PP's lock** is the same blob in B and C (`833cbda4…`) and unchanged after every build. Cargo added only the harness or probe package.

**Scripts** (`gate/script_provenance.txt`):
- The preserved method scripts and inputs are unchanged and equal round 1's.
- Round 1's rebuilt scripts were reused, changed only in paths, worktree and revisions.
- New: `u3diff.py` (the U3 classifier), `t9_u3_compare.py`, `part1_u3_compare.py` (round 1's record and stdout checks with `u3diff`), and the digest helper (`digest_helper/`).
- **Requests:** round 1's `gen_out` was reused. Its 223 files equal the calibration list, and gen.py's inputs are unchanged in B and C.

**The binding-digest recomputation** (the brief's 2): the scratch helper `i112_receipt_digests` applies PP `source_receipt::hash`'s rule through the product's own `canonical_json` crate (`canonical_json_checked_v1_text`). The crate is identical in B and C. The rule is:
- publication = the envelope without `source_block_recovery`, domain `source_blocks_publication_v1`;
- receipt = `body` with that publication digest, domain `source_blocks_receipt_v1`.

**Self-check:** the helper reproduces the embedded digests of all 100 receipt-carrying T9 outputs (50 base, 50 candidate).

The export-document digests (RE `derivative::digest`, `derivative_hash`) do not arise: these gates publish envelopes, not export documents.

## 1. T9 (`t9/`): PASS

**Method:** S11-K's `fixdiff_main.rs` (`ec089c1d…`), unchanged, built `--release --offline`, run over `core`, `fixtures`, `validation` and F1b's extra corpus.

**Output sets** (`t9_u3_compare.txt`, `.json`):
- Base 114 outputs, candidate 116; every rc 0.
- 86 identical, 28 differing, 0 removed, 2 added.
- Extra corpus: 16/16 identical.
- Every differing output's input is byte-identical in B and C.

**The differences, classified:**

| Outputs | Class | Detail |
|---|---|---|
| `fixtures/product_preview/invented_preview_model.json`, both modes (2) | **1, designed refusal** | The input (0.1.0, no contract) carries 4 legacy pressure primitives: `load:L-100-P`, `L-100-P-EJ`, `L-200-P` and `L-200-P-EJ`. B already refused it (`MODEL_INCOMPLETE`, 0 results, the same 4 `PRESSURE_MODEL_REAUTHOR_REQUIRED`) with the old text. C's 4 diagnostics carry the documented text: "legacy pressure primitives are retired, zero values included; remove the primitive, or re-author the model to 2.0.0/exact_straight_pressure_v2 …". Their refs name each primitive. Only those 4 messages differ. |
| `fixtures/product_preview/source_blocks/{,ui/}{multicase,n05,n06}-{dense_scrutiny,sparse_interactive}.request.json`, both modes (24) | **2, declared T2** | Only T2's string and its two digests differ. C's digests equal the rule over C's content. B's bytes equal C with T2 restored to its old text and both digests recomputed by the rule. |
| `fixtures/product_preview/numerical_sensitive_torsion_model.json`, both modes (2) | **2, declared T2** | the same check |

**Added outputs** (2). The input `fixtures/product_preview/invented_demo_model.json` is new in C (I114's demo model, CHANGE_RECORD §5).
- Both modes give `MECHANICS_SOLVED`, `checks_passed`, with 625 results (sparse) and 627 (dense).
- **Each output plus a final newline equals the committed `invented_demo_result_preview_physics_1_{sparse,dense}.json` byte for byte.**

**Committed raw fixtures beside requests:** 42.
- 12 of them are the source-block raws C re-pinned for T2.
- **B reproduces all 42 of B's tree; C reproduces all 42 of C's tree:** 32 byte for byte and 10 as the same JSON document. Those 10 are the sorted-key serializations I110 noted.

## 2. Both-entry gate, part 1 (`gate/part1/`): PASS

The probes are `7bda41f5…` (B) and `430c4005…` (C). Each side ran 884 runs.

| Check | Result |
|---|---|
| gate_check, B and C | **PASS**, 764 evaluated, 332 trusted, **0 trusted breach triples**. The 764 rows are identical. |
| Outcomes, both sides | solved 676, refused_blocked 142, refused_capture 64, refused_error 2. 0 heap-cap aborts, 0 timeouts, every exit 0. |
| `compare_gate_kf2.py` (identity) | 16 differences, all `full_envelope_sha256`. No outcome, ok, exit, error-text or summary difference. |
| stderr; summary envelopes | 884/884 identical; 818/818 identical |
| runs.jsonl and stdout | No residue beyond the timing fields and `run.envelope_sha256` |
| **The U3 rule** | **884/884 within the rule.** Full envelopes: 802 identical, 66 none, **16 declared T2**. |

**The 16 differences** are the captured entry, both modes, of FX-N05, FX-N06 and FX-NP-A-ulp-{.25, .5, .75, 1, 1.5, 2}. Each is **class 2, declared T2**, with C's digests equal to the rule and B equal to C normalized and re-digested. The typed entry, which has no source-block recovery, is identical.

There are no refusals or removed cases: no gate request carries a legacy pressure input or a joint.

B's 818 full and summary envelopes equal round 1's PR-N candidate (lists `0b478a78…`, `c3113bff…`).

## 3. Both-entry gate, part 2 (`gate/part2_run1/`): PASS

- **The runs:** the four dense 1,000-member runs on B and C, using I13's `gate_part2.py`, unchanged, with I61's fixed quiet wait and watcher.
- **One execution, under `t3_exclusive.sh`.** 0 of 75 watcher samples saw a foreign job, so no rerun was needed.
- **Timings:** every run ended in 46.4–47.5 s, with exit 0 and no timeout.
- **Outcomes:** all are `refused_blocked`, `NUMERICAL_INTEGRITY_UNRESOLVED`.
- **Full envelopes:** base and candidate are byte-identical per run (`68cf1929…`, `cb611210…`, `7a3d32b4…`, `9384c225…`). These equal round 1's, I61's and KF2's.
- **RESULT PASS.**

## 4. Not exercised here

These gates' corpora contain:
- no input with the legacy label;
- no new joint refusal (`JOINT_ELEMENT_STIFFNESS_INCOMPLETE`, `JOINT_ELEMENT_MAPPING_UNRESOLVED`);
- no T1, T3 or V1 carrier as a standalone input;
- no removed case from CHANGE_RECORD §4.

The T1 and V1 rows I110 measured are embedded models inside `result_export_v0_2.json` and contract case 67, and T9 does not walk embedded models. The classifier handles those classes, but no output here needed them.

## 5. Records

All paths are relative to this folder. Bulk outputs are uncommitted, with their hashes in `gate/uncommitted_sha256.txt`: `WT/scratch/i112_u3/` (trees, T9 outputs, `gen_out`, `part1_{base,cand}/` at about 606 MB of runs.jsonl each, and `part2_run1/`).
- **`t9/`:** scripts, manifests, lock diffs, build and run logs, sha lists, binary hashes and the classification.
- **`gate/`:** scripts and provenance, probe manifests, lock diffs, build logs, binary hashes, the request hashes and the host job lines.
  - **`part1/`:** SUMMARY, drivers, gate_check, schedules, host samples, indexes, the identity comparison, the U3 classification and the gate_check-row comparison.
  - **`part2_run1/`** and `part2_combined.tsv`.
- **`digest_helper/`:** the helper's source, manifest, lock diff, build log and binary hash.
- **Top level:** `u3diff.py`, `normdiff.py` (its lexer serves the refusal leaf list), `screen_files.py`, `trees_check.txt` and SHA256SUMS.
- **The host screen** (`WT/tools/t3_host_screen.py`'s patterns over every record file) gives 0 hits.
