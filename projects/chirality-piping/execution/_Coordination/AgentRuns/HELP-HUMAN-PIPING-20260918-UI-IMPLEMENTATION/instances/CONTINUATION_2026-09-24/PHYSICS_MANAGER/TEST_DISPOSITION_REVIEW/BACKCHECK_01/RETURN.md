# Successor test-disposition backcheck

**TD-R1, TD-R2 and TD-V1 are closed as source/test-disposition findings on the bound successor. No new actionable static finding.** The original pending patch plus these exact repairs is suitable for manager integration and actual-candidate execution. This is not a product test pass, final merge clearance, engineering acceptance or acceptance of other outstanding core/consumer work.

Exact identities:

- Original retained patch: `f7ee34f04a74e474a2f6fc97f2faeedfaa0476e54b2b1ee2082df1c3825678c3`.
- Policy successor delta: `db1f66527f093c68e6e068378e298703d2df7530d093d3db2e85b76e55cce53b`.
- Exact kPa delta: `aaa11cab61ea2cb4a89e69feafb0976b79394bdbfcbca511fb4fc9f7da72190f`.
- Reconstructed successor `lib.rs`: `61d7316246bc51983606c1bda006727b62c0e159d62c39b37b190d27d3e08568`.
- Reconstructed successor public pressure test: `ad501226fb01868d3f831f5b72b2ce1703c8a23703ee7a006166590bbbc168e3`.
- Independent frozen expectations: `0f2d6fea59033500f68d443fa2a0518a7c0fbf08582e684fdd1eca6f344a07c2`.

## Closure evidence

**TD-R1:** The current companion now preserves the composite geometry, materials, parallel EJ springs and named nonlinear/source supports, applies precisely Z4 plus the existing spring-removal/qL/2 nodal premise, and exercises both primitive cases in both solver modes. Original, Z-reversed and all-load-reversed variants check independent displacement/reaction values, stop active/released states, sliding state, convergence/iteration criteria, opposing slip and friction, and source-reference/DOF metadata. All-load reversal changes the normal magnitude to 350/125 N and releases the one-way stop, so coverage no longer consists solely of unchanged-magnitude reversal. It also compares normal evidence against the actual S-130 resultant. This is correctly a magnitude-only comparison: only UY belongs to that source support, and the existing facade masks reactions by each support's actual DOFs. No signed source-UY publication is inferred. The original historical constants and assertions remain unchanged.

The independent reference was inspected in full. Its cubic-Hermite strain-energy assembly has the correct axial/torsional and two bending contributions, global projection, fixture section properties and six relative-DOF EJ springs. Its nonlinear enumeration solves both one-way states and sticking/sliding sign branches. With `R_s=a+b*p`, Coulomb equilibrium gives `p=c*a/(1-c*b)`; the nonzero feedback `b≈0.117249080152111878` matters and is retained. This qualifies the stated legacy frame/EJ premise, not a new physical expansion-joint formulation.

My bounded Python probe independently reconstructs the exact fixture transformation, including binary64-generated nodal-load values, then reexecutes only the inspected reference definitions with the output-writing tail excluded. Separate checks establish positive constrained stiffness by Cholesky for both stop states, matrix symmetry, affine Coulomb consistency, global Y balance and unique admissible branches. All six case/variant results match the frozen Decimal packet. The actual binary64 literals and `round6` expectation expressions in the Rust test produce the same six-decimal values. This is a mathematical reference check, not product execution or a claim of a wholly separate second oracle. Algorithm-specific iteration count 2 remains an execution obligation; a mismatch requires diagnosis, not retuning.

**TD-R2:** Only `kind == "pressure"` enters the historical adapter. Fixed/free thermal calls now use the current public entrypoint in both modes, preserving every existing station comparison and compression assertion. The retained mixed test name still explains its historical pressure branch; that name does not alter the now-current thermal execution.

**TD-V1:** The existing public orientation/unit control now includes 2000 kPa alongside 2e6 Pa and 2 MPa. The entire solve/assertion tail and protected tolerances are unchanged. Both fixed/free states and both modes still verify the qualified nonzero pressure, wall/surface stresses, displacement and support responses. `2000*1000 = 2e6` independently checks the intended encoding.

## Binding and limits

`binding_probe.py` strictly applies all five hunks to their declared original-candidate/F03 preimages and verifies the successor hashes. It separately proves the only policy changes are the named helper-purpose addition, the exact new companion function and thermal branch routing. The historical adapter, original 50-test assertions and shared fixture remain otherwise as previously reviewed. `STATIC_BINDING.json`, `REFERENCE_PROBE.json` and the input hash manifests retain the checks and exact consulted sources.

The parent's PHYS-R4 runtime delta is expressly outside these reconstructed source hashes and needs its own review plus a faithful combined integration. Actual library/public tests, full suite, required checks and downstream/native evidence remain outstanding. Earlier all50 static conclusions remain bounded by those execution obligations. No observed product output supplied the new expected values.

Same independent TASK `/root/physics_resume/test_policy_review`, actual parent `/root/physics_resume`, delegated-harness-native. Continued under the full role/Root/Piping/LOOP_INIT/software-code-review basis preserved in the parent review input manifest. Assignment and final-freeze messages came from that parent. Writes for this backcheck are confined to `TEST_DISPOSITION_REVIEW/BACKCHECK_01`. No product source edit, Cargo/Rust build, product run, Git operation, native/network action or delegation occurred.
