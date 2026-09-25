# PHYS-R4 independent successor backcheck

Disposition: **PHYS-R4 closed for the bounded two-file source repair and manager-observed public red/green control. Suitable for manager fan-in; no unresolved actionable finding in this delta.** This does not establish full-suite, native, consumer, merge, engineering or lifecycle acceptance.

## Assignment and actual execution

Independent TASK `/root/physics_resume/membrane_backcheck`, actual harness parent `/root/physics_resume`, created through the delegated harness. The supplied brief includes the complete TASK role. Read the actual temporary checkout's Root/Piping AGENTS, Piping `loop/LOOP_INIT.md`, and `.agents/skills/software-code-review/SKILL.md`; their exact origins and SHA-256 values are in `verification.json`. Prior complete F03 review at `INDEPENDENT_REVIEW/FREEZE_03_BACKCHECK/RETURN.md` is the inherited source-review basis, not a newly executed complete review by this successor.

Writes are confined to `MEMBRANE_BACKCHECK`. This reviewer performed source/evidence inspection and the retained Python file/hash/patch/Fraction probe only. No Git, Cargo, Rust or public-product execution, native/browser work, implementation mutation or delegation occurred. The manager's red/green executions remain attributed to `/root/physics_resume`; inspecting their logs does not make them independent runtime executions.

## Finding closure and consequences

At `core/product_physics/src/lib.rs:8177`, the exact-pressure membrane row now publishes the `membrane` already returned by `SourceAnnulus::recover_wall_effective_membrane`. It no longer divides the rounded published wall force by the rounded wall area.

At `lib.rs:2053–2065` and `6780–6848`, the exact straight maximum receives the retained mechanical/thermal end actions plus the same optional member pressure state. At each statics interval start, `straight_section_resultants` recovers the same signed mechanical force used by the row path, and the same SourceAnnulus helper produces the constant axial stress before wall-force projection. Both row and maximum therefore use the same source geometry, material, pressure and constitutive recovery. The helper and its scalar arithmetic bytes are unchanged from F03.

Pressure correction at `lib.rs:1726–1743` changes only axial end-action components after retaining the original vector. Consequently the change of vector used by the maximum does not alter its transverse forces, torsion or bending moments. Uniform member pressure adds a constant wall force; it does not change the axial distributed-load slope. The unchanged j-side equilibrium coefficients `N'=-wx`, `My'=Vz`, `Mz'=-Vy`, `My''=-wz`, `Mz''=wy` and the bending Bernstein controls remain appropriate. Independent Fraction checks cover 36 tensile/compressive/zero-force and distributed axial-load polynomial evaluations, including pressure-free identities. These checks establish algebraic consistency, not general floating-point forward accuracy.

For an exact-mode member with no pressure state, no mechanical-action copy is created; the caller still selects the original corrected forces, and the helper takes the unchanged `r[0]/section.area` branch. Legacy mode does not enter this maximum path. No stress tolerance, old oracle, geometry helper, solver, load assembly, nonaxial statics or other result publication is changed by this patch. Existing `pressure_section_geometry` controls cover pressurized bending and an unpressurized thin member; `elastic_extrema_runtime` covers the pressure-free X1 maximum and torque. Their F03 evidence is inherited, and successor affected-test reruns remain an integration gate.

## Public proof and independent arithmetic

The original `red-01` fixture used length `1e-77 m` and failed at `PIPE_ELEMENT_INPUT_INVALID` with a degenerate element axis. It remains failed-admission evidence. The retained successor test uses length `1 m`, fixes all degrees of freedom at both ends and has no mechanical/thermal primitive load. Hence mechanical/thermal force is zero and the independent membrane ratio has no length term; changing length does not change the frozen stress reference.

The public test invokes `run_linear_static_preview_with_mode` in both SparseInteractive and DenseScrutiny, first requires `MECHANICS_SOLVED`, checks finite result rows and no accepted-state mutation, locates unique case/entity/component/unit rows, and checks the membrane row, per-member governing maximum and complete-case maximum. It checks that the published wall force has binary64 bits `1`. Its nonzero reference tolerance remains `1e-9 * abs(reference)`.

Independent exact represented-input Fraction algebra gives:

- Source OD `4e-77 m`, wall `1e-77 m`, pressure `4.7e-170 Pa`, nu `0.1`; with `Nm=0`, membrane `2*nu*p*(OD/2-wall)^2 / (wall*(OD-wall)) = 3.1333333333333337e-171 Pa`. Pi cancels from this ratio.
- Projected wall force is the minimum positive binary64 subnormal. Re-dividing this projected force by projected area yields `5.242199316501608e-171 Pa`, relative error `0.6730423350537045`.
- Bound manager `red-02` logs report both modes reaching solved mechanics and exactly that incorrect old membrane and member maximum. Exit code 101 records both assertion failures. This is actual observed public reachability, beyond the predecessor expression-only premise.
- Bound manager `green-01` logs report both modes passing all test assertions with membrane/member maximum `3.13333333333333325e-171 Pa`; exit code 0, 2/2 tests pass. Relative error from the independent reference is `-1.4669863914547882e-16`, within the unchanged `1e-9` criterion. Successful assertions also cover the complete-case summary value, although that value is not separately printed.

These are arithmetic-range controls. They establish neither material fitness nor source-load/subnormal force/solver-conditioning forward-error qualification.

## Exact inspected bindings

`verification.json` records the complete inspected input hash map and successful in-memory application of every patch hunk. No Git reconstruction or runtime execution was used. The two-path patch reconstructs the exact current source/test bytes from the F03 source snapshot. All 19 F03 snapshot hashes verify; the 18 unchanged paths still match current bytes, while lib.rs matches the declared successor.

| Item | SHA-256 |
|---|---|
| F03 content identity | `18dc3fea2b087f00aeecbb92c321ce42e0e23812b5c541921e813c034d7fd7fb` |
| F03 SOURCE_MANIFEST.json | `ed5dc0ef77c69c5ab9e9aefcd59128217d87330ca7e9c78069ca8f49f139430a` |
| lib.rs before | `322c7f8b9a4040d77c3ccc0a5ba336715b1575e87267cc5100ae8125588390f8` |
| lib.rs after | `0c5a275a82a4cdd244b613cb1028bd2a4639312126cff64e0965ad9afed71417` |
| new pressure_membrane_range.rs | `53b461e708f092cd9b35717f9aa242ddfd288e2f742c61456fbf46fa0ec620ea` |
| PHYS_R4.delta.patch | `177ef090e35d501efbc82685866d0ae2a23fb20dfca4cbe70d6d82e77db61aee` |
| independent Fraction reference JSON | `23db606adf7fe61f4df6031ac6b11b8285b88b12d6dfe381a04faaabd13c349c` |
| manager red-02.log | `618e937089db6aeadbca224dc0dbbb0916cca9e43b0c856bc62e6ea55cfd93c3` |
| manager green-01.log | `4086f6863bef956dce8916ed7a7ce4f305ff21f1532e152bda0cf19576ca0a8c` |

One evidence defect was raised during this backcheck: `REFERENCE_BINDING.json` contained a test hash matching neither retained test. The manager preserved that record and added `REFERENCE_BINDING_02.json`, explicitly recording the supersession, matching final test hash, source basis and length-only admission correction. `REPAIR_BINDING.json` now points to that successor. This reviewer verified the corrected chain against the actual test, independent reference and red/green execution records. The binding defect is closed; the old record is historical, not the operative reference binding.

Reproduction: from the checkout root, run Python 3 on this directory's `verify_bindings_and_arithmetic.py`. It writes only this directory's `verification.json`. Actual run exit 0: 2 patch sections, all 19 F03 paths verified, reference/test/log binding checks passed, exact Fraction reference and 36 polynomial identities passed. Its own source and output hashes are retained in `OUTPUT_HASHES.json`.

## Remaining gates

The parent must still integrate and independently check the regression dispositions, obtain the ROOT build slot, run affected public controls/full suites on the actual assembled candidate, complete NUM/physics-1 producer/consumer checks, perform applicable native authoring/solve/result/save/reopen/export witnesses, and satisfy the registered evidence sweep, independent final-candidate review and CI/merge gates. Prior F03 review limits remain applicable. This return closes PHYS-R4 only and does not claim those gates have passed or authorize a product release.
