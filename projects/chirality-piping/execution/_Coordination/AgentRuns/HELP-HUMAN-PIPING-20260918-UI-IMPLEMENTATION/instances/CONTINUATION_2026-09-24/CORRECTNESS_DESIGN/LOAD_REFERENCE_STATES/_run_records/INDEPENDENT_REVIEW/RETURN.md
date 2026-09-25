# Independent load/reference-state design review

**Result: clear after three design repairs.** This review qualifies the bounded
design and analytical examples, not a production implementation or finding-group
closure. The actual reviewed seven-file packet is identified in
[FINAL_HASHES.json](FINAL_HASHES.json).

Reviewer `/root/load_state_design/reference_review` acted as TASK (Type 2),
delegated by `/root/load_state_design` through native `collaboration.spawn_agent`.
No further delegation occurred. Root/project instructions and the full TASK role
were read; their origins/hashes are in [BASIS_START.json](BASIS_START.json).
The caller remained the sole author of design repairs. Reviewer writes are
confined to this directory. No product, Git, work-graph, instruction, library or
code-rule change, build, native check or production qualification occurred.

## Findings and disposition

| ID | Severity | Finding | Repair and backcheck |
|---|---|---|---|
| LR-R1 | P2 | Calling the rigid-replacement reaction the force in the lock could overstate internal pin load. In example 8 the total support action is 1000 N, but a retained 100 N spring action would leave 900 N for the pin. | DESIGN §5, INTERFACE support records, VERIFICATION example 8 and the author calculation now explicitly report total locked-support assembly action. Internal force partition is unavailable without its own device model. Reviewer independently checked both zero-position and predecessor-position locking. Clear. |
| LR-R2 | P2 | The first concrete interface had only `selected_temperature_K`, and actual operating temperature existed only in the free-length thermal branch. A direct-strain case could not faithfully carry known physical temperature separately from an overridden E/nu selection temperature. | INTERFACE now owns optional actual `operating_temperature` per element, requires it when consumed, and retains separate `operating_temperature_K` and `material_selection_temperature_K`. DESIGN matches. Direct interval/fixed-data cases need not invent absolute T. Duplicate adapter temperatures must agree after normalization. Clear. |
| LR-R3 | P2; supplied by ROOT during review | Uniform pressure and full fluid weight needed a tighter admitted-geometry boundary. In a vertical closed fluid column, true cap-force imbalance already carries fluid weight in a wall-force model. Reapplying full axial contents weight doubles the reaction; a uniform-pressure approximation can hide local force errors even when reaction and end extension match. | Independently confirmed the root-supplied counterexample, including the stronger average-pressure control. DESIGN, INTERFACE and VERIFICATION now restrict the first uniform/full-fluid route to zero axial gravity projection and require a coherent pressure-field/weight formulation otherwise. HYDROSTATIC_CONTROL documents wall/effective-force ownership and station checks. Clear as a bounded design; the successor remains implementation work. |

LR-R1 was reported against the draft read before the first hash capture; that
capture already contains its repair, and is not presented as a hash of the old
wording. The first interface capture in
[INTERFACE_INITIAL_HASH.json](INTERFACE_INITIAL_HASH.json) predates LR-R2's repair.
The caller also clarified ordinary-load inclusion and imposed-boundary migration
during review; the final text explicitly prevents applying the primitive array
again or treating support movement as a scalable force. These were read and
included in the final review.

LR-R3 arrived after an initial return/hash packet had been written but before
handoff. [BEFORE_HYDROSTATIC_HASHES.json](BEFORE_HYDROSTATIC_HASHES.json) preserves
that intermediate packet. Final review supersedes its coverage and includes the
hydrostatic amendment and the final eleven-group calculation.

## Independent checks

[independent_check.py](independent_check.py) uses only Python standard-library
Fraction/Decimal arithmetic. It imports neither the product nor the author's
calculation. The actual run passed all **11 independent analytical groups**;
[NUMERICAL_REVIEW.json](NUMERICAL_REVIEW.json) retains values and script hash.
Command, run result and Python identity are in
[CHECK_RUN.json](CHECK_RUN.json).

- Axial support motion: independently assembled bar equilibrium reproduces
  middle displacement 1/15000 m and reactions ±20000/3 N. Omitting prescribed
  coupling leaves a 20000 N free-equation residual.
- Rotation: cubic beam interpolation and boundary derivatives, rather than the
  author's stiffness-row formula, yield [3, 4, -3, 2] N/N*m and balanced total
  moment. A free tip follows the rigid small rotation without strain.
- Per-element properties: compatibility plus equilibrium for two members sharing
  a material identity reproduces 1/3000 m and equal/opposite 200000/3 N actions.
- Thermal data: direct physical lengths give 43/25009 engineering strain and
  datum invariance. Differential-per-datum integration gives 0.0015; logarithmic
  current-length integration gives exp(0.0015)-1. Split/reversed integration
  identities pass. These are distinct declared data meanings.
- Fit mismatch: the stated assembly-reference, small-strain law produces cold
  tension 40000 N and hot force -89976 N. An independently computed law using
  natural length in its denominator differs, as expected; the design explicitly
  avoids claiming exact finite-deformation mechanics. The reference-ratio input
  transformation does not remove the frame approximation.
- Hydrotest: direct annular-area integration and cantilever balance confirm all
  symbolic-pi mass, weight, wall-pressure and root-action values. Uniform pressure
  plus full-fluid weight is a stated beam-level scenario; this does not verify a
  spatial hydrostatic field, partial fill, or unspecified closure mechanics.
- Support/source/history: active spring equilibrium, total locked assembly
  action, conditional internal pin partition, one-time persistent preload and
  explicit stick/slip branch history all reproduce the proposed examples.
- Hydrostatic formulation: cap-traction balance independently gives a 1000 N
  top reaction and constant 3000 N wall tension for the final column inputs.
  Adding axial contents weight again gives 2000 N reaction. Uniform average
  pressure instead gives incorrect wall forces [2500, 3000, 3500] N while still
  matching the 1000 N reaction, effective forces and 75 micrometre extension.
  Explicit integration of the strain's affine coefficients confirms this
  stronger counterexample. A second 100 kPa top-pressure case confirms the same
  balance distinction independently of the final witness's pressure offset.

The verification document also lists future mutation, migration, native,
persistence and coverage checks. Those are implementation obligations, not
additional tests purportedly executed by this review.

## Reference assessment

The inspected primary sources support the distinctions they are used for:

- [Abaqus 2025 Thermal Expansion](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEMATRefMap/simamat-c-thermalexpan.htm)
  distinguishes coefficient datum from initial temperature and total from
  differential data. Its small-strain secant equation subtracts reference
  dilations; the design correctly does not attribute its exact length ratio to
  that equation.
- [COMSOL 6.4 Thermal Expansion](https://doc.comsol.com/6.4/doc/com.comsol.help.sme/sme_ug_modeling.05.168.html)
  separates the measured-data datum from the stress-free reference and supplies
  a reference-length correction. The final reference packet replaces the
  initially used 6.3 page with 6.4 and limits its freshness claim. Some equation
  image fetches returned a cache miss; the textual explanation, reference
  correction expression, and independent derivation were available. This review
  does not pretend to have read unavailable images.
- [Abaqus boundary conditions](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEKEYRefMap/simakey-r-boundary.htm)
  distinguish prescribed values from fixing values at a step's start.
  [Initial condition types](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEPRCRefMap/simaprc-c-initialcond-t-SpecifyingTheTypeOfInitialConditionBeingDefined-sma-topic1.htm)
  distinguish initial geometry and stress-free state. These are conceptual
  corroboration, not sources of the numerical examples.
- [Connector friction](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEELMRefMap/simaelm-c-connfrictionbehav.htm)
  and [FRIC_COEF](https://docs.software.vt.edu/abaqusv2025/English/SIMACAESUBRefMap/simasub-c-fric_coef.htm)
  carry slip and committed state between increments. They substantiate retaining
  physical history separately from a numerical iteration seed.
- [CAEPIPE Hydrotest](https://www.sstusa.com/docs/tech_manual/hydrotest.htm)
  and [Cold Spring](https://www.sstusa.com/docs/tech_manual/cold_spring__cut_pipe_.htm)
  identify relevant physical inputs and product-specific conventions. The
  design correctly declines to import automatic pinning, fluid defaults or code
  treatment as SWBPIPE mechanics or operational data.
- [Ansys 2026 R1 PIPE288](https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_elem/Hlp_E_PIPE288.html)
  couples internal fluid free-surface input to pressure and mass effects and
  exposes effective tension. [Abaqus distributed loads](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEPRCRefMap/simaprc-c-loaddistributed.htm)
  distinguishes uniform/hydrostatic pipe pressure and includes closed-end
  effects. These corroborate formulation ownership; the column arithmetic is
  independently derived rather than taken from vendor output.

Modern sources retain the equilibrium/reference distinctions at issue. The
review found no conflict requiring a different first-tranche formulation.
This is not an exhaustive search for the newest nonlinear formulation. Finite
rotation, plasticity/creep, arbitrary installation stages and stateful friction
are explicit successors, not capabilities established by these linear examples.

## Implementation return

The proposed resolver is implementable around existing assembly, prescribed
reduction and result owners. Per-element property keys, one physical-source
ledger, explicit boundary/device references, and recovery from the same resolved
object address the substantive failure modes. A bounded read of the joined
working source confirmed the existing prescribed-displacement kernel primitive,
the product's zero-only reduction path, and the hydrotest-pressure block at the
time of inspection; it was not a frozen implementation review.

Carry the three corrected distinctions into typed fields, result labels and tests.
Preserve the design's limits: uniform member temperatures, global small
prescriptions, straight axial fit mismatch, explicit full/drained mass state,
equivalent locked-support totals, zero axial gravity projection for the first
uniform/full-fluid route, and authentic history only where its physical
state method is implemented. Final version allocation, actual connected
implementation, source-recovery eligibility, native witnesses and candidate
qualification remain with ROOT and the implementation managers.
