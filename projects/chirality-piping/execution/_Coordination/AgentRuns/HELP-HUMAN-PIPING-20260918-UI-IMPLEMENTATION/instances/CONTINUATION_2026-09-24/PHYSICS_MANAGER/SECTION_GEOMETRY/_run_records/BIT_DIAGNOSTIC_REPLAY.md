# Narrow bit/cancellation diagnostic replay

This is an ad hoc run record, not a workflow or a new acceptance test.

The executable was compiled with rustc 1.97.1 from geometry_bit_diagnostic.rs, using the product and serde_json rlibs named and SHA-256 bound in BIT_DIAGNOSTIC_INPUTS.json. The source test was copied without changing its fixture/helper/expectation contents; include paths were rebased to the original frozen JSON files and a printing main was appended. No original test or product source was edited.

On the recorded host the operation was:

    rustc --edition=2021 -L dependency=<PHYSICS_MANAGER/PRESSURE_REGIONS/target/debug/deps> --extern open_pipe_stress_product_physics=<recorded product rlib> --extern serde_json=<recorded serde_json rlib> geometry_bit_diagnostic.rs -o geometry_bit_diagnostic.bin
    ./geometry_bit_diagnostic.bin > geometry_bit_trace.jsonl

Compile output is geometry_bit_compile.log. BIT_DIAGNOSTIC_RESULT.json records executable, source, compiler and trace identities. The executable was removed after recording its hash; no build binary belongs in the source PR.

For replay in another checkout, rebase the two include_str paths to this packet's SOURCE_ODWALL_EXPECTATIONS.json and NEAR_INCOMPRESSIBLE_EXPECTATIONS.json, leaving their bytes unchanged. Use the corresponding frozen producer source/dependency profile from GEOMETRY_RUN1_INPUTS.json and parent source snapshot to rebuild the rlibs. Verify the rlib identities before claiming byte-identical replay; a rebuilt or repaired source is a new observation and must have a new output record. Do not relabel the old failure trace as a repaired-source result.

The printing main reports ordinary decoded source values/bits, public geometry and both-mode near-incompressible responses. It retains the same explicit nu-bit input selection already in the frozen original test. SOURCE_INPUT_BITS.json is diagnostic reference data only and was not substituted into the fixture.
