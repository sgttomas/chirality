# Retained-source recovery design return

**Ready for ROOT selection and WORKING_ITEMS implementation; not implemented or independently qualified.** [DESIGN.md](DESIGN.md) defines the minimum complete-source, <=2-free-block recovery tranche, its exact affine-functional derivation, source/API ownership, route integration and required controls.

The selected technical direction is to solve from retained contributions and evaluate member end forces, station actions, signed spring device actions and constrained equilibrium reactions against the exact response before projecting each final scalar. In a 2x2 block, combine the functional numerator over the shared exact positive determinant. Replacing published displacement alone does not repair member torque.

The design keeps these distinctions explicit:

- Exact declared binary64 source operands versus exact physical geometry/material/pi claims; observed N05 product coefficient `...e26` versus NP-A's independently frozen `...e22`.
- Spring-on-pipe action `-k*(u-g)` versus total equilibrium `K*u-f`; the latter is zero on a free spring DOF and cannot report N05 root spring torque.
- Requested dense/sparse mode, actual ordinary attempt and the separately selected exact-source method. N06 recovery cannot require ordinary rounded-system success first.
- Exact connected free-block eligibility and local/global recovery-source closure versus a fixture-specific admission. Signed-permutation source transforms can qualify; larger coupled blocks, unproved rotated-source closure and unsupported recovery families remain explicit.
- Private retained method/projection evidence versus consumer admission. ROOT owns minimal combined carrier semantics; current freeze05 containment is unchanged, and a label alone cannot bypass it.

Five grouped [lightweight rational design checks](_run_records/REFERENCE_PROBE.json) passed, using [a standalone Fraction/Gauss script](_run_records/reference_probe.py) with no production imports. The N05 illustrative source calculation shows approximately 3.38e-7 relative torque error after projecting correct rotations first. The N06-scale illustrative calculation loses the twist entirely; direct exact functional evaluation returns the declared torque. Other checks cover nonzero prescribed values, constrained load subtraction, fixed-end affine offsets, multiple blocks, wholly prescribed states, signed permutations and a tiny coupling that correctly connects a forbidden three-DOF block. These are design evidence, not actual product or Rust observations.

The minimum handoff is: bounded functional engine and retained companion; source-complete straight-frame/ground-spring adapter with supported nodal loads and source closure; both-mode actual N05/N06 member/spring/reaction recovery; ROOT-owned method/consumer admission after fresh independent review and required tests. Protected 1e-9, contact/count/cap/affine criteria and ordinary DEC-050/053 observations remain unchanged. Arbitrary rotations, broader nonlinear/load families and precision2 persistence remain outside this tranche, without being declared complete.

Full Root/Piping/LOOP_INIT/HELPS_HUMANS instruction origins and hashes, source readset, actual harness-native parentage and execution limits are retained in [_run_records/PROVENANCE.json](_run_records/PROVENANCE.json) and [_run_records/INPUT_MANIFEST.json](_run_records/INPUT_MANIFEST.json). No delegation by this author, production/source edit, Git command, build, native/browser run or larger-successor write occurred. Only this design folder was written. Evidence hashes and unchanged-input verification are in [_run_records/OUTPUT_MANIFEST.json](_run_records/OUTPUT_MANIFEST.json) and [_run_records/INPUT_RECHECK.json](_run_records/INPUT_RECHECK.json).
