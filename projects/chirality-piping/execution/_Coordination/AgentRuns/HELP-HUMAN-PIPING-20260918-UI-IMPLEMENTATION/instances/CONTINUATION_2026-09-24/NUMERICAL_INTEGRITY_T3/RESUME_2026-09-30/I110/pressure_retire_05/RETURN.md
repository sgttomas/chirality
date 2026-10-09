# I110 round 5: ROOT's rulings on the round-4 stop

I110 is a TASK for WORKING_ITEMS (T3). The round-5 instructions came in a WORKING_ITEMS message that carried ROOT's rulings.

Branch `codex/piping-t3-pressure-retire-20261008` in `WT/t3-pret`. Head: **`70e7f49ced`**, 2 commits on `5bc6f269da`. Product files only; not pushed.

## Stop

**STOP on item 1 (T2) only. The text is not changed, and nothing is re-pinned.**

ROOT's condition for the re-pins was: "only the declared string may differ, in every re-pinned byte". That condition cannot hold for the source-block carriers. Each source-block document binds its publication bytes with two digests, which the readers verify:
- `source_block_recovery.body.publication_sha256`;
- `source_block_recovery.receipt_sha256`.

The readers that verify them include:
- `sourceBlockRecovery.ts:162`;
- `analysisRunCompatibility.ts:233`;
- `loadReferenceSourceEvidence.ts`.

So a consistent re-pin necessarily changes those two digests along with the string. A string-only edit would break the readers' verification.

`_run_records/t2_per_file_check.txt` has the per-file check, made with the head's own output with T2 applied (not committed):

| Carrier | Does the head reproduce it today? | Leaves that would change |
|---|---|---|
| 12 source-block raws (6 main, 6 `ui/`) | yes, as JSON | 3 each: the declared string and the two receipt digests |
| `f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes`, whose 2 SHA constants pin the full envelope | — | the same 3 |
| `source_blocks/generation.json` | — | all 12 of its raw-file `sha256` entries |
| 2 `rejected_stress_range` raws | no: they are historical pre-repair captures ("maintained negative reader fixtures") | any re-pin would edit a captured artifact; `ORACLE.json` holds their `raw_sha256` |
| 2 precision UI fixtures | no: captured precision-1 documents | a string-only edit would be declared-only (no digests) |

**For ROOT, one of:**
- **(a)** Accept an extended check. Each re-pinned source-block file and the Rust pin may differ in the declared string and in the two receipt digests that bind it, which the product recomputes and the readers verify. `generation.json`'s 12 hashes change. The two historical captures and `ORACLE.json` stay as captured. The precision UI pair gets a string-only edit.
- **(b)** Defer T2 with T4 to the next scheduled corpus generation.

## Commits (`5bc6f269da..70e7f49ced`)

| Commit | What |
|---|---|
| `5dc62d764c` | Item 3, the two joint validation messages (below) |
| `70e7f49ced` | Item 5: the DEL-10-05 regeneration procedure passes the local-private intent (below) |

**`5dc62d764c`, the two joint messages.**
- `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (`validation.rs:1159`) loses "pressure thrust remains load-side input evidence".
- `EXPANSION_JOINT_GEOMETRY_INPUT_INVALID` (`:1350`) loses "before load-side pressure-thrust evidence can be generated".
- Both now say no joint pressure thrust is generated.
- Both are published warnings that described the retired treatment, and the radius is small:
  - 4 corpus rows, all from contract-corpus case 67 (its base and applied models, both modes). They change in the ordinary and runner mechanics envelopes, and in the declared string only.
  - No committed fixture or test carries either message.

**`70e7f49ced`, the DEL-10-05 procedure.** The procedure is in `P/docs/validation_manual/headless_runner_reproduction.md`. The five bound-path commands now pass `--explicit-local-private-intent`. The text says the runner wraps its output in the local-private control, and that each output's `payload` equals the committed witness. I checked all five:
- exit codes are 0, 0, 0, 1, 1;
- every payload equals its committed file as JSON (`_run_records/del1005_witness_check.txt`).

The frozen-E1 procedure in Part 1 is historical and is unchanged.

## Re-pins

None. T2 is stopped (above).

The two joint messages needed no re-pin: no committed file carries them. Their corpus rows are confined to the declared string under the mechanical check.

## Evidence

B is main `7eae707bb7`; its B-side records are reused from round 2. The candidate is `70e7f49ced`.

**Per-test outcomes.** The changes equal, name for name, the source `#[test]` changes since B (58).

| Suite | B | Candidate | Changes |
|---|---|---|---|
| 40 manifests | 2776 pass / 3 fail / 80 ignored | 2755 / 3 / 80 | 57, all planned; none new in round 5 |
| src-tauri | 116 | 117 | |
| pytest | 4426 passed, 32 skipped | unchanged | |
| vitest | 4245 | 4248 | |

- The 3 manifest failures are the known Mac ones at both B and candidate.
- **vitest:** the full run inside the chain had one failure, `App.deadControls.test.tsx` "every button is either responsive or disabled…". The file passed in two isolated reruns, and a second full run passed all 4248. Round 5 changes no TypeScript. See `vitest_flake_note.txt`; the comparison uses the second full run.

**Bytes** (`declared_text_check.txt`):

| Set | Result |
|---|---|
| E (exact) | 96/96 equal |
| F (pressure-free) | 358 equal; 6 differ only in declared strings |
| B1 | 64/64 equal |
| W1 | 64/64 equal |

The 6 declared-only F rows are:
- T1: `result_export_v0_2.json` producer case 1, 2 rows;
- the joint interface message: case 67, 4 rows.

There are no other differences.

## Notes

- **T4** (`PP/src/preview_physics.rs:75`, `LIMITATIONS[1]`) is unchanged, per ROOT. Its text ("Nonzero pressure is refused…") is true, only narrower than the refusal. The wider wording waits for the next scheduled corpus generation.
  - Its radius (round 4) is the whole retained-precision and reader corpus:
    - B1 64/64;
    - W1 64/64;
    - 07n, all 26 cases;
    - 8 successor fixtures;
    - the `results.v0.3` schema `const`s;
    - 28 Rust pins.
- **MECH-TP-PHYS-008's id** keeps its name, per ROOT.
- **I114's fixtures** are untouched.

Records: `RETURN.md`, `_run_records/`, `SHA256SUMS`. Placeholder paths only.
