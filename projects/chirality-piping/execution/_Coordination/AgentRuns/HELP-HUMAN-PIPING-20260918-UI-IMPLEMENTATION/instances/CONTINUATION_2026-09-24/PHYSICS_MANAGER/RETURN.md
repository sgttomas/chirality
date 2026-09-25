# Initial bounded core pressure/stress return

The real exact-pressure runtime is implemented in the isolated physics checkout. It uses the existing exact-annulus kernel unchanged in arithmetic, explicit case-scoped pressure regions and closure paths, a common selected E/nu material basis with derived G, and separate mechanical/eigen/cap assembly. Wall recovery excludes cap subtraction. New raw0.2 rows retain wall force, effective force, membrane/Lamé stresses and signed six-component linear support actions. Exact unpressurized members retain material evidence without fabricated regions.

The new circular normal-stress maximum uses the correct |Nw/As|+hypot(My,Mz)/Z objective over direct piecewise quadratic section statics. Bernstein interval bounds identify an approximate witness and bound the global objective of the supplied binary64 coefficients; they do not claim exact/unique station coordinates or bound solver/coefficient-formation error. An unresolved maximum is explicitly unavailable. Pure torque retains signed torsional shear and zero normal maximum.

Fresh nonzero legacy pressure blocks with PRESSURE_MODEL_REAUTHOR_REQUIRED. Existing historical model/result bytes and old physics expectations are not rewritten. Exact first-composition exclusions and unsupported combination handling remain explicit.

## Checks and source freeze

- Corrected independent public pressure suite: **14/14 pass**, including both solver modes, six realistic SI states, rotation/units, unequal-wall/E two-span reversal, mixed closures, distributed axial loading, selected material/alpha and identity controls.
- Actual-entrypoint X1 missed-peak and pure-torque cases: **2/2 pass**.
- Full stress crate: **48/48 pass**.
- Full product library inventory: **195 tests; 145 pass, 50 fail**. This includes **11/11 region-module tests passing**. Failures and proposed per-purpose classes are retained in PRODUCT_LIB_FAILURE_INVENTORY.json and PRODUCT_LIB_FAILURE_CLASSIFICATION.json; no old fixture/assertion/criterion has been changed to clear them.
- Integrated compilation passed. No native, headless consumer, export/persistence, registered sweep/CI or merge check is claimed.

FREEZE_01 contains the ten-file source whitelist, base/current hashes, complete patch, recoverable source copies and evidence bindings. Review it together with TEST_WIRE_DELTA.json/.patch and pressure_runtime.corrected.rs: one independent test helper used the wrong moment direction token, causing 2/14 exploratory failures; correcting global_x to rotation_x produced 14/14 without changing numbers or tolerances. The original failure source/log remain preserved. Nine other source files are unchanged from the initial freeze. INTERFACE_SCHEMA.md records the exact prospective row/evidence meanings and limits.

ROOT selected case-bound basis_ref and separate pressure result_ids mapping, case-scoped region IDs and the prospective physics-1 allocation. Numerical integration, schema/consumer qualification and authoring/native routing remain ROOT/NUM/AUTHORING-owned. The branch has no local commit and is **not merge-ready**: independent whole-source/oracle review and individually warranted disposition of the 50 regression failures remain required.

Actual delegation, full role briefs, original input hashes and enforcement limits are retained under PHYSICS_MANAGER. ROOT-nominated retained TASKs preserve harness parent /root; assignment issuer/integrator is /root/physics_manager. A rejected first spawn was never represented as executed. This return is not a new central receipt, engineering acceptance or release.

## Independent-review repair update

FREEZE_02 supersedes the initial source as the repair candidate while preserving FREEZE_01. Independent review found incomplete maximum coverage and input-order tie selection. Four real public controls failed before repair and pass after it; overall summaries now require complete requested case/member coverage, while valid individual rows remain. Added public nonzero six-component reaction/rotation and explicit two-spring attribution controls, plus ambiguity/duplicate rejection. All 24 public tests pass on repaired executable source; full product library remains 145/195 with the same 50 retained fixture failures. Stress 48 remains passed on unchanged stress source. A subsequent comment-only TEST_HEADER_DELTA corrects copied attribution text in two new tests; no executable expectation changed. Backcheck is pending.

All 50 failures have concrete proposals in REGRESSION_DISPOSITION/DISPOSITIONS.json and PARENT_12_DISPOSITIONS.json. An observational diagnostic clone (no production edits/condition changes) reproduced the same195/145/50 and directly observed the legacy-pressure refusal before every failure. These causal records and proposals do not clear any failed acceptance check.

## Successor source geometry and cancellation closure

FREEZE_03 is the current core candidate, with 19 source/test/manifest files and an explicit delta from FREEZE_02. Actual checks are now 34/34 public, 156/206 library (same 50 preserved legacy fixture failures), canonical JSON 8+2, unchanged stress 48. Independent source OD/wall and near-incompressible references were frozen before repair; exact coefficient summation received 7707 independent bit/Fraction checks. The pure area helper is the same owned source delivered to M35, with no material dependency or pressure admission guard added to mass. See FREEZE_03/RETURN.md, INTERFACE_SCHEMA.md and CHECKS_AND_REFERENCES.json. Independent successor backcheck remains pending; merge/consumer/native qualification remains open.

## Resumed PHYS-R4 and test-policy work

WORKING_ITEMS `/root/physics_resume` resumed under actual harness parent ROOT `/root`; predecessor records remain `/root/physics_manager`. Full role/basis and actual instruction hashes are in RESUMPTION_2026-09-24.json. F03 is preserved. A real public admitted-length arithmetic-range case reproduced the reviewer’s67.304% membrane/headline error in both modes. The publisher now consumes the retained prepublication membrane, and exact-pressure extrema form their constant axial stress from retained mechanical/thermal state through the same source annulus. Shared area/helper bytes remain unchanged. Two red controls become green at original relative1e-9; all36 affected public controls pass. MEMBRANE_PUBLICATION binds the narrow delta and actual logs; independent MEMBRANE_BACKCHECK supplies bounded closure.

The50 test-disposition candidate is still preserved and unintegrated. Independent TEST_DISPOSITION_REVIEW held it for thermal-only current-route restoration, nonzero exact-region kPa coverage, and a composite derived-normal nonlinear/friction/reversal counterpart. The original13 historical numerical bodies and36 constructor-only current edits passed static preservation review, with individual50 causal/proposal bindings. TEST_DISPOSITION_REPAIR holds pending successor deltas; NONLINEAR_CURRENT_REFERENCE is deriving the original composite state independently before expected public output is examined. The full product suite remains pending this reviewed integration; no merge, consumer/native join, governed acceptance or release is claimed.

## Integrated successor check

The pending test-policy findings above are now corrected, independently backchecked, and integrated on the PHYS-R4 source. Actual product library213/213 and public36/36 pass with no ignored cases. The composite reference is independently frozen and exercises both cases, original/Z-reversed/all-reversed inputs and both solver modes; exact kPa and current thermal routing also pass. FREEZE_04 candidate `6bb99354fa9591032f672a7c3bd488edd8d4cdb6df9135e211cff3a10556b546` binds21 actual files equal to the run’s input hashes. Original F03,50 failures, held test-policy patch/reviews and prior oracles remain preserved. Final independent composition/log backcheck is pending; next required joins remain ROOT/NUM semantic-consumer union, native/persistence/authoring evidence and registered checks/CI.

Final independent composition/log backcheck passed (TEST_DISPOSITION_REVIEW/BACKCHECK_02), with no unresolved bounded source/test-policy finding. ROOT authorized local checkpoint only; no push/PR/main join. CONNECTED_INTEGRATION_HANDOFF.md identifies concrete model, semantic reader and native/authoring joins. Selected source is frozen, passing and independently reviewed; full programme/engineering/consumer qualification remains open.
