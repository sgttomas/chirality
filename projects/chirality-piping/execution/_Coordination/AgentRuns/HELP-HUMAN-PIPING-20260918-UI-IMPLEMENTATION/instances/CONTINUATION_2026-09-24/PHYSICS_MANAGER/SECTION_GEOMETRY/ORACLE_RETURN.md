# Independent source-section oracle — final return

Date: 2026-09-24. TASK /root/numerical_policy_review, actual harness parent /root; issuer/integrator /root/physics_manager. No delegation. Only this evidence directory and the new core/product_physics/tests/pressure_section_geometry.rs were written by this TASK.

**Final public result: 9 geometry/source-cancellation tests passed, 0 failed. The pre-existing pressure14 suite passed unchanged.** Final execution was performed by physics_manager; this oracle author independently read the raw combined log and bound the held source/test identities. This is not a claim that this TASK executed that final combined run.

Test SHA-256: b81b1600adf62c711779ca1d06e908954fc2531b8545f37925b150cdbf7301f7. Pressure14 remains 9493488af21d2459d47cb2f18f3b5e2f4c5da43351bf9a210387067e7839e272.

## Reference and geometry definition

SOURCE_REFERENCE_RETURN.md and SOURCE_ODWALL_EXPECTATIONS.json are the selected source-faithful reference: normalized source OD D and effective wall t define ro=D/2, ri=ro-t mathematically, A=pi*t*(D-t), Ai=pi*(ro-t)^2, I=A*[ro²+(ro-t)²]/4, J=2I and Z=I/ro. The independently frozen properties/responses were generated with exact Fraction arithmetic and bounded Machin pi before the new source implementation was read.

Earlier REFERENCE_RETURN.md / FROZEN_SECTION_EXPECTATIONS.json remain unchanged as the represented-radii comparison, not the runtime acceptance target. Their thin extension differs from the source target by +1.3050401129e-6 relative. The final tests reject substituting that alternative for source-wall accuracy.

The selected thin source extension is 3.59999999990999998e-7 m, with A=3.76991118427633574e-13 m² and I=6.78584013158430650e-16 m⁴. Runtime checks use the unchanged nonzero relative 1e-9 criterion for source A/Ai/I/J/Z, pressure extension, bending displacement/rotation, torsional rotation and normal stress. Rounded radii remain explicitly derived observations. Source and pressure evidence must agree with the same built section, including unpressurized members without fabricated pressure regions.

## What the nine public tests establish

1. Ordinary source annulus properties and pressure/bending/torsion/normal-stress response.
2. Thin source wall drives those same quantities, rather than rounded-radius geometry.
3. An unpressurized thin member uses the source section and all-member evidence without a fake region.
4. Representable I/J survive a nonrepresentable naive intermediate in the fully fixed range control.
5. Collapsed rounded-radius gap and genuinely unrepresentable final area/property cases block.
6. Free near-incompressible source pressure loading retains its nonzero extension, including the last admissible binary64 nu below .5; nu=.5 stays invalid.
7. Two exactly equal-bore spans with distinct comparable near-limit nu values preserve each extension in both modes and all member/terminal reversals.
8. Fixed near-limit effective force and signed support reactions preserve the small nonzero source difference independently of the much larger wall force.
9. Near-limit extension transforms as a vector under a proper three-dimensional rotation in both modes.

The two-span control uses exact dyadic OD/wall/bore inputs and increments with ratio 1.8. It does not rely on subtracting a 1e-20 increment from a 1e-10 displacement. The fixed control compares its tiny nonzero effective force/reactions against their own 1e-9 references, not a wall-force-sized allowance. The rotated control compares all three nonzero components and the magnitude.

These are real run_linear_static_preview_with_mode calls after DTO construction/deserialization. No product section/pressure/stress helper produced an expected value; no synthetic result rows stand in for runtime output.

## Failure evidence and subsequent repair verification

The initial six-test run passed four and failed two. Its original test hash 6fff5e055fee05956b5f286c5859ffc4a2cc0d1cd064cd02bf65dbdb51c471ba and all 49 participating source hashes were retained; post-run hashes were unchanged.

- Ordinary/thin source geometry and responses, unpressurized thin geometry, and invalid final-range controls already passed.
- The large-range test exposed input decoding: source JSON wall=5e76 became bits ending 5c instead of the frozen source bits ending 5b. Product geometry faithfully used that changed input. The evidence-only diagnostic links exact old product/serde_json artifacts and records the input/emitted bits.
- With nu/OD/wall bits verified, both modes showed near-limit source-load cancellation: relative extension error +1.7902493e-8 at nu=.4999999999 and +.043037835047 at the last valid nu. The latter produced extension1.5790972091241894e-20 m versus reference1.51394048812521335e-20 m. The original 1e-9 criterion remained failed.

DIAGNOSIS_BEFORE_PARSER_AND_LOAD_REPAIR.md and _run_records/geometry_bit_trace.jsonl preserve those distinctions. The diagnostic's RHS values are explicitly response-inferred, not directly captured assembly vectors.

ROOT directed the actual M34 float_roundtrip feature fix; the frozen original input/test route was rerun unchanged. SOURCE_INPUT_BITS.json was diagnostic custody only and was not substituted to obtain a pass. Parent separately repaired source coefficient grouping, pressure assembly and effective-force recovery. This TASK made no production changes.

New controls were appended through recorded deltas: the original six remain a byte-for-byte prefix of the eight-test source, and those eight remain a byte-for-byte prefix of the final nine. TWO_APPENDED_TESTS.json/.patch and ROTATION_APPEND.json/.patch bind each delta and reference. No original numerical value, tolerance or fixture was edited for the later pass.

Parent's grouped eight-test log first recorded 8/8. The final public log records all nine passing, pressure14 passing and separate parent-owned stress/reaction/coverage/grouping-limit suites passing. This return claims only the bounded geometry/source-cancellation and unchanged pressure14 results.

## Execution, source custody and rerun

This TASK executed the independent Python freezes, the first six-test Cargo run, and the narrow evidence-only Rust bit/response diagnostic under coordinated slots. Original pressure14 source was never changed. No Git mutation, native/browser operation or configuration edit was performed by this TASK.

Final raw log: public-final-source-01.log, SHA-256 0c3f8fef249a7af32c3c000f81c99807eeda46589fff182b858125479f0c4668. _run_records/FINAL_PUBLIC_OBSERVATION.json identifies physics_manager as execution actor and records the 50-file held source capture after the completed run, plus test/log identities.

Bounded rerun from the qualified source checkout, after obtaining the shared Cargo slot:

    CARGO_BUILD_JOBS=2 CARGO_TARGET_DIR=<PHYSICS_MANAGER/PRESSURE_REGIONS/target> cargo test --offline --locked -j2 --manifest-path projects/chirality-piping/core/product_physics/Cargo.toml --test pressure_section_geometry -- --test-threads=2

This is a reproducer for the nine-test target, not a claim that it is the parent's full multi-target command. Parent owns the combined-run/source-freeze record and actual-candidate integration.

## Limits and return

The reference is for the selected homogeneous-isotropic, small-strain straight-annulus model. Thin/extreme and near-incompressible examples are arithmetic/source-parameter controls, not manufactured-pipe, shell/collapse, local end/interface, stability or professional fitness evidence. Source arithmetic fidelity is distinct from input/material accuracy in the world.

The coefficient grouping method is qualified only within its actual supported grouping and source-condition envelope. The parent-owned grouping-limit test records explicit nonqualification of strong cancellation across distinct pressure factors; this return makes no universal forward-error or formal IEEE certificate claim.

A nine-test public pass is not full-library, legacy-oracle disposition, native/persistence/export, protected-sweep or complete-candidate review acceptance. Those remain with ROOT and the integration owner. Later source or consumer changes need their affected checks and review coverage.

The frozen source test, independent references, first failures, bit trace, append deltas and final passing observation are returned to ROOT and physics_manager. No earlier instruction/checkpoint or pressure14 file was modified.
