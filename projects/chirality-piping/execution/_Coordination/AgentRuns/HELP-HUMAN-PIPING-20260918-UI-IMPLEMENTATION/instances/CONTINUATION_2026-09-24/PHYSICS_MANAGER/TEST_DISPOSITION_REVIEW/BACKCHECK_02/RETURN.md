# Final integrated core composition and execution backcheck

**No unresolved actionable source/test-policy finding in the exact bounded F04 candidate. Suitable for ROOT/manager core fan-in.** Candidate content SHA-256 is `6bb99354fa9591032f672a7c3bd488edd8d4cdb6df9135e211cff3a10556b546`. This closes the integration backcheck for the previously reviewed core, PHYS-R4 and individual test dispositions. Consumer/native/CI/merge and engineering acceptance gates remain open.

## Exact composition

Independent `composition_probe.py` reconstructs F04 from the 19 preserved F03 sources and the five-path F04 delta. It separately reconstructs the original pending test patch, its reviewed policy/kPa successor, and the reviewed PHYS-R4 patch. The test and membrane edits compose without overlap in original F03 coordinates; their result equals the F04 reconstruction byte for byte. No fuzzy hunk application or live-source substitution was used.

All 21 live file hashes, byte counts, declared F03 preimages, source whitelist and sorted candidate digest match. The five changed paths are `product_physics/src/lib.rs`, `src/pressure_runtime.rs`, new `src/historical_pressure_reference.rs`, `tests/pressure_runtime.rs`, and new `tests/pressure_membrane_range.rs`. The other 16 selected paths remain identical to F03. The final facade hash is `0965164e6b6b8107a1b9563354ddbf5226ccc23e30516bd23cdea9789b0932c9`; the F04 delta hash is `d83f0f93192e9c2366754e7bc52b5900a08a8bdd011ea1158e7f87a1f31243c7`.

The inherited whole-F03 review, `MEMBRANE_BACKCHECK/RETURN.md` and this review's `BACKCHECK_01/RETURN.md` retain their exact inspected identities. All hashes in F04 `CHECKS_AND_REFERENCES.json` verify, including the corrected PHYS-R4 reference chain, original red evidence, green runs and independently frozen nonlinear expectations. No changed or missing reviewed basis was found among these selected source/evidence records. Earlier failed and held records remain intact as history.

## Actual recorded execution

The manager's `integrated-product-01-execution.json` records Cargo/Rust 1.97.1, actual checkout cwd, `--offline --locked -j 2`, the library and all seven named public test binaries, and two test threads. It exited 0 at `2026-09-25T03:15:03.700615+00:00`. All 21 F04 files are included in its before/after unchanged input hashes and still match live bytes. Its raw log SHA-256 is `99b12efa0b3b5911a388c8b1d1a91d940bce97120e707a47173d2a7f7dc1315c`.

The log independently parses to **213/213 library tests and 36/36 public tests passed, zero failed, ignored or filtered**. Public breakdown: pressure 14, source geometry 9, membrane range 2, elastic extrema 2, coverage/ties 4, support reactions 4 and grouping refusal 1. The two private-scope panic messages are expected caught-panic controls; both named tests subsequently report `ok` and the process succeeds.

`ALL50_PASS_MAPPING.json` maps each original failure to exactly one passing integrated function: 36 current-purpose tests, 13 explicitly historical pressure tests, and the current hydrotest/refusal test. Original assertions and the thermal-only current branch have the previously reviewed composition. All five added current companions and both scope-safety controls also have passing rows. The new composite test exercises both cases/modes and three independently derived load variants; the kPa and membrane controls execute through the normal library boundary. A green suite is not being used to excuse changed criteria: byte composition first establishes that the executed checks are the reviewed ones.

## Disposition and limits

TD-R1, TD-R2, TD-V1 and the separately reviewed PHYS-R4 remain closed for this exact integrated scope. No additional source or test-policy repair is requested by this backcheck. The changed normal stress publication, historical adapter restriction, local fixture treatment and prospective physical counterparts are faithfully integrated.

Execution inspection is attributed to the manager's actual run, not an independent product run by this reviewer. The run manifest hashes all 21 selected core files plus evidence records; it does not exhaustively hash Cargo.lock or every transitive workspace dependency. This is a provenance boundary for the selected-core result, not a claim of an immutable complete build environment. The inherited stress 48 and canonical JSON 8+2 checks remain inherited evidence rather than new executions.

ROOT/NUM physics-1 producer/consumer integration, actual native authoring/solve/inspection/save/reopen/export, registered evidence sweep and CI on the joined candidate, broader pressure/nonlinear/combination/stress programme obligations and merge gates remain open. Historical recalculation is not byte replay, Current qualification, engineering fitness, lifecycle acceptance or release authority.

Same independent delegated-harness-native TASK `/root/physics_resume/test_policy_review`, parent `/root/physics_resume`, continuing under the preserved full TASK/Root/Piping/LOOP_INIT/software-code-review basis. Writes were confined to `BACKCHECK_02`; this reviewer ran only the bounded Python composition/hash/log probe. No source edit, Git, Cargo/Rust build, product execution, native/network action or delegation occurred. `INSPECTED_INPUTS.json`, `COMPOSITION_AND_EXECUTION.json`, `ALL50_PASS_MAPPING.json` and `OUTPUT_HASHES.json` retain the exact evidence.
