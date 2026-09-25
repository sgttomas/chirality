# Piping solver benchmark research and coding-agent implementation plan

**Research date:** 24 September 2026  
**Document status:** Research report and proposed implementation specification; not a completed test report.  
**Audience:** Project owner and coding agent responsible for integrating numerical qualification into an existing repository.  
**Repository status:** No repository or application executable was supplied or inspected for this report.

## Executive decision

Build a versioned, publicly reproducible **numerical qualification suite** around three complementary sources of evidence:

1. Analytical reference problems and executable open-source tests, initially drawn from EDF's Code_Aster piping test families.
2. Published system-level piping benchmarks, especially NUREG/CR-1677 Volumes 1 and 2, with NUREG/CR-6414 and NUREG/CR-6645 where the implemented dynamic capabilities warrant them.
3. Equivalent-model comparisons against explicitly identified releases of established piping solvers, with separate tests of the application's export path.

There are direct industry precedents for this approach: ANSYS publishes NRC piping implementations, Bentley documents a feature-based reference-test matrix, and MetaPiping documents an automated comparison/reporting tool using NRC cases and PIPESTRESS references. [R04] [R19] [R20]

Use NASA-STD-7009B as a freely accessible framework for organizing evidence. ASME V&V 10 is an applicable solid-mechanics framework, but it is a commercially published standard, not an open-source test corpus. No single freely available, piping-specific pass/fail standard establishing whole-product equivalence was identified in this research. [R15] [R18]

**The intended outcome is a scoped claim of demonstrated numerical performance, not a claim that one test suite establishes every aspect of another product's capability or quality-assurance program.** Scope can expand as evidence accumulates. Lack of a completed profile need not prevent publication of experimental source code; it prevents presenting that profile as passed.

This plan does not require a bundled production materials database, component catalog, or piping-code compliance module. Test cases supply their own explicit numerical properties. It also does not assume a human will inspect the solver source or equations. Record the actual review and execution history; do not describe agent-generated work as human review.

## Contents

- [1. Scope and terminology](#1-scope-and-terminology)
- [2. Research findings: available benchmarks](#2-research-findings-available-benchmarks)
- [3. Standards, methods, and commercial precedents](#3-standards-methods-and-commercial-precedents)
- [4. What has and has not been established](#4-what-has-and-has-not-been-established)
- [5. Instructions to the coding agent](#5-instructions-to-the-coding-agent)
- [6. Qualification profiles and coverage matrix](#6-qualification-profiles-and-coverage-matrix)
- [7. Analytical and derived test specifications](#7-analytical-and-derived-test-specifications)
- [8. Source acquisition and benchmark transcription](#8-source-acquisition-and-benchmark-transcription)
- [9. Repository architecture and data contracts](#9-repository-architecture-and-data-contracts)
- [10. Comparison and acceptance rules](#10-comparison-and-acceptance-rules)
- [11. Reference-solver adapters and interoperability](#11-reference-solver-adapters-and-interoperability)
- [12. UI, agent, and optimization testing](#12-ui-agent-and-optimization-testing)
- [13. CI, release gates, and evidence retention](#13-ci-release-gates-and-evidence-retention)
- [14. Implementation backlog and completion criteria](#14-implementation-backlog-and-completion-criteria)
- [15. Publication and claim templates](#15-publication-and-claim-templates)
- [16. Open decisions and blocked work](#16-open-decisions-and-blocked-work)
- [17. Coding-agent handoff prompt](#17-coding-agent-handoff-prompt)
- [18. Annotated reference register](#18-annotated-reference-register)

## 1. Scope and terminology

### 1.1 Product scope assumed for planning

The application is an open-source piping analysis/design environment with a numerical solver, a modern UI, user-supplied material/component inputs, agent-accessible operations, and export to established analysis programs. Piping-code compliance checking and a production property catalog are outside the requested scope. The agent must confirm the actual implemented scope from the repository rather than infer features from this description.

In particular, do not assume that “comprehensive” means the application supports plasticity, shell ovalization, soil interaction, large deformation, response spectra, or fluid transients. Make those individual capability records. A test that requires unimplemented physics belongs in a future profile, not in a silently simplified current test.

### 1.2 Working labels

| Label | Meaning in this plan |
|---|---|
| Analytical reference | A specified mathematical problem with an independently evaluated closed-form or otherwise exact mathematical reference. Applicability depends on its assumptions. |
| Published numerical reference | Results from a documented numerical calculation, possibly including a stated reference accuracy or uncertainty. |
| Cross-solver comparison | Equivalent-model evaluation by another identified solver/version. |
| Regression baseline | A stored prior result from the application or reference implementation. It detects change; it is not automatically an independent target. |
| Experimental reference | Measurements from a documented physical test, with sufficient setup and uncertainty information. |
| Qualification profile | A project-defined, versioned set of capabilities, cases, comparisons, and acceptance rules. This is not an external certification designation. |
| Numerical parity | Comparable performance on a disclosed common modeling domain, output set, and test suite. It does not mean identical implementations or every product feature. |
| Reference readiness | Whether a reference is documented, acquired, transcribed, reproducible, and ready to be used. This is separate from whether the application passes it. |

“Known solution” must not collapse these categories. Preserve the source of every expected value. Tests based only on the application's previous output must not inflate the independent-reference count.

## 2. Research findings: available benchmarks

### 2.1 NRC piping collections

| Collection | Verified content and usefulness | Acquisition and implementation note |
|---|---|---|
| **NUREG/CR-1677, Volume 1** | Linear-elastic piping problems using uniform-support-motion response-spectrum analysis. Reference outputs include frequencies, participation factors, nodal displacements, and internal forces/moments. Associated anchor-motion static solutions are explicitly excluded. [R01] | Public archival record and report access through the repository. Start with the simplest applicable problem, then cover the remainder required by the selected profile. |
| **NUREG/CR-1677, Volume 2** | Four independent-support-motion response-spectrum problems, including reference natural frequencies, participation factors, displacements, and element forces. Associated anchor-motion pseudo-static displacements are excluded. [R02] | NTIS record inspected; complete input/output transcription remains implementation work. ANSYS provides a directly accessible implementation route for Problem 1. |
| **NUREG/CR-6414** | Three representative piping-system problems developed for the Westinghouse AP600 analysis program. These are system-level dynamic numerical benchmarks. [R03] | Public archival record inspected. Acquire the original report, identify its analysis settings, and transcribe the applicable cases before claiming them as implemented. |
| **NUREG/CR-6645** | Modal-response-combination reference material. ANSYS publishes a piping case with missing-mass and rigid-response treatments. [R06] | Implement only the response-combination features actually claimed. Do not label the ANSYS output as an exact analytical answer or confuse it with the original report's tables. |

**Why this family matters:** the ANSYS Mechanical APDL Verification Manual includes NRC piping cases, with input listings, model descriptions, and output tables. Its overview identifies EPIPE, a piping-oriented modification of SAP IV, as the source of the NRC solutions discussed there. These are therefore recognizable numerical benchmarks used in a commercial verification context. [R04]

**Important implementation distinction:** ANSYS separates archived-element implementations from newer pipe/elbow-element implementations. For example, the inspected Volume 2 Problem 1 page lists `PIPE289`, `ELBOW290`, and `COMBIN14`, and links three input listings. Treat element formulation, mass formulation, support stiffness, and response-combination options as part of the benchmark identity. [R05]

The inspected ANSYS pages identify themselves as **2026 R1**. That is the documented version inspected, not a claim that it is the latest release or the version the project must adopt. [R04]

### 2.2 Code_Aster: open-source executable references

Code_Aster provides a particularly practical starting point because the documentation describes problems and reference solutions, while the source tree contains runnable test assets. The inspected `ssll106a.comm` file carries a **GPL-3.0-or-later** notice. Its paired `.export` file identifies both the command file and the required `ssll106a.mmed` mesh. Obtain all dependencies, not just the command script. [R08] [R09]

| Identifier | Subject and outputs | Reference type and scope |
|---|---|---|
| **SSLL106 / V3.01.106** | Straight pipe under axial force, transverse forces, bending moments, torsion, internal pressure, distributed loading, and thermal expansion. Displacements, nodal resultants, stresses, and strains are tested. | Analytical strength-of-materials references. Multiple enriched pipe-element variants are documented. [R07] |
| **SSLL101 / V3.01.101** | Noncoplanar three-dimensional Hovgaard piping system with bends, gravity, thermal loading, and nodal loading. | Published numerical comparisons. Beam variants reference POUX/ADL/TITUS; pipe variants reference ABAQUS. The source distinguishes the formulations and reports 2% reference uncertainty. [R10] [R11] |
| **SSLX102 / V3.05.102** | Bent piping under bending, including flexibility changes associated with ovalization and adjacent straight segments. | Shell/solid numerical references; the reference-solution page estimates 2% accuracy. This is not automatically equivalent to a simple beam-with-flexibility-factors model. [R12] [R13] |
| **SDLX02 / V2.05.002** | Hovgaard modal and spectral analysis, including static modes and spectrum interpolation. | Compilation of other-program results. Useful for assembled-system dynamics and post-processing. [R14] |
| **SDLL14 / V2.02.014** | Thin piping-elbow natural frequencies and mode shapes. | Analytical references for specified variants, and published/PIPESTRESS comparisons for other variants. Preserve the variant-specific provenance. [R23] |
| **SSNL503 / V6.02.503** | Thin elbow with in-plane bending, internal pressure, and end-cap effects in material-nonlinear quasi-static analysis. | ABAQUS numerical reference. Relevant only to a profile that includes material nonlinearity and the necessary pipe representation. [R24] |

The pipe-element usage guide identifies further tests, including **SSNL106**, **HSNV100**, and **ELSA**. Treat these as discoverable extensions; this report did not audit their complete input sets or all numerical reference values. [R25]

#### What the executable assertions give you

The inspected `ssll106a.comm` differentiates analytical reference values (`VALE_REFE`) from stored calculated values (`VALE_CALC`) and supplies comparison precision on individual assertions. Preserve that distinction in the new harness. Do not import a regression number and relabel it as an analytical target. [R08]

The project should implement its own independent oracle for a basic formula when appropriate, while recording the published problem from which a fixture was adapted. Copying upstream executable code requires handling its actual licence. Reimplementing a problem from documented inputs and importing upstream code are different acquisition paths; do not merge them into a single undifferentiated “open data” category.

### 2.3 A concrete numerical-reference example

For **SSLX102**, the reference page specifies an applied bending moment of **17,000 N·m**, an in-plane end displacement reference of **0.02 m**, and an out-of-plane reference of **−0.015657 m**, with stated reference accuracy of approximately **2%**. These values are useful checks on transcription, not complete fixtures: geometry, boundary conditions, material inputs, formulation, and output location must also be captured. [R13]

This illustrates why a blanket “all results must match to 0.1%” policy is inappropriate. A close match to a finite-accuracy numerical reference and accuracy relative to an analytical solution are different tests.

### 2.4 Supplementary benchmark sources

**NAFEMS:** the publicly readable Benchmark Challenge index links problems and solutions. These can supplement general structural-mechanics coverage, but the challenge is not a comprehensive piping qualification suite. [R21]

For the nonlinear-restraint gap, **NAFEMS R0081, _Benchmark Tests for Finite Element Modelling of Contact, Gapping and Sliding_**, is a useful optional acquisition. Its public description identifies ten problems, including a sliding wedge with springs and a cantilever contacting a surface. The complete publication is offered through purchase/subscription, not as an identified open-source corpus. Applicability still depends on matching its contact model to the application's restraint model. [R26]

**Method of manufactured solutions:** Sandia's SAND2000-1444 supplies a publicly accessible methodological reference for constructing additional exact-solution verification cases. It is a method, not an external certificate or a piping test library. [R22]

**Physical-test extension:** NRC's public abstract for NUREG/CR-6983 describes analyses of JNES/NUPEC large-scale seismic piping experiments. This is a possible later source of physical-reference evidence. The complete report and machine-readable measurements were not acquired in this research; do not make that extension a dependency of the initial elastic qualification suite. [R29]

## 3. Standards, methods, and commercial precedents

### 3.1 Publicly accessible is not the same as open-source

| Resource | Access classification | Recommended use |
|---|---|---|
| Code_Aster test source | Inspected source file explicitly licensed GPL-3.0-or-later. Other assets require their own recorded terms. | Executable test acquisition or separately implemented benchmark fixtures. [R08] |
| NRC benchmark reports | Public archival/government report access; redistribution permission must be recorded for the actual acquired asset. | Documented problem definitions and numerical references. [R01] [R02] [R03] |
| ANSYS verification documentation | Publicly readable vendor documentation and input listings; not identified as open-source. | Model interpretation and published commercial comparisons. [R04] [R05] [R06] |
| NASA-STD-7009B | Publicly accessible standard, approved 5 March 2024. | Evidence organization and a traceable requirements-adoption matrix. [R15] |
| NASA-HDBK-7009B | Public handbook, official page and cover identifying approval on 3 February 2026. | Implementation guidance. [R16] [R17] |
| ASME V&V 10-2019 (R2025) | Commercially published solid-mechanics standard. | Optional purchased methodology reference; do not claim clauses were audited from a product page. [R18] |
| AutoPIPE Acceptance Test Set | Vendor-supplied subset associated with its QA & Reporting releases. | Optional, access-controlled comparison evidence; not an open corpus. [R19] |
| NAFEMS Challenge / R0081 | Public challenge pages versus separately purchased/subscribed benchmark publication. | Supplementary tests, keeping the access categories distinct. [R21] [R26] |

Repository policy: **when redistribution permission is unresolved, store the source pointer and acquisition metadata rather than committing the asset.** This is a conservative project rule, not a legal determination that every public document is restricted.

### 3.2 Applying NASA without overclaiming compliance

Use a compact adoption matrix mapping source sections to repository evidence. Useful anchors in NASA-STD-7009B include §4.2.1.3 for units/frames, §4.2.3–4.2.4 for verification records, §4.2.5–4.2.6 for validation records, and §4.3.8 for reporting. The standard leaves acceptance criteria to the relevant program/project rather than supplying a universal piping error percentage. [R15]

The matrix should state `adopted`, `partially_addressed`, `not_addressed`, or `not_applicable`, with a rationale. Do not generate “NASA-compliant” from a partial mapping.

**Source-control note:** the linked NASA-HDBK-7009B has an approved cover, but an inspected interior page retains a “DRAFT” running header. Preserve the acquired file and hash, cite the official catalog entry and cover, and seek clarification before treating that file as a controlled contractual reference. This report does not infer withdrawal or lack of approval from that inconsistency. [R16] [R17]

### 3.3 Commercial evidence practices you can emulate

**AutoPIPE:** Bentley describes pre-release Alpha Tests as a feature-based matrix evaluated against prepared expectations, including hand calculations and established programs. The ATS is a sample, not complete functional coverage; Bentley also states that the installed version must match the ATS version. The practical pattern is a feature matrix, documented expected results, and version-specific execution. [R19]

**MetaPiping:** its quality documentation names PIPESTRESS 4.2 and NRC collections among the references, and describes running reference projects and saving a current-version conformity report. The practical pattern is an automated, repeatable benchmark/reporting command. This report inspected the documentation, not its private case corpus. [R20]

**CAEPIPE:** its technical manual points to a Verification Manual for inter-program comparisons. Vendor release material also identifies that manual. A complete current verification corpus was not obtained here; its cases and permissions remain an optional acquisition task. [R27] [R28]

**CAESAR II / Aspect Pipe Stress:** the vendor currently uses the latter name and describes a broader quality-assurance program, including NQA-1-related claims. Treat these as the vendor's stated program, not evidence that this proposed project has equivalent QA arrangements. A numerical-performance comparison can be scoped separately. [R30]

## 4. What has and has not been established

### 4.1 Established by this research

Public source pages were inspected for the benchmark families, reference types, access categories, and vendor practices described above. Representative Code_Aster command and dependency files were read. ANSYS problem pages and linked input listings were accessible. Selected NASA PDF pages were visually inspected in addition to reading extracted text. Source pointers are collected in §18.

### 4.2 Not established

No benchmark was run against the user's solver. No commercial solver was executed. No repository was inspected. No complete NRC corpus was digitized. Not every Code_Aster variant was acquired or executed. No publication-rights audit of a proposed redistributed corpus was completed. No external certification, independent human review, or whole-product equivalence was established.

This document contains **original implementation proposals** from §5 onward. Proposed thresholds, directory layouts, schemas, gates, and work packages are project recommendations, not assertions that NASA, ASME, NRC, EDF, or a vendor mandates those exact details.

### 4.3 Important refinements to the earlier discussion

The Code_Aster pipe cases include formulations richer than ordinary beam elements. NRC dynamic cases do not fill the nonlinear-restraint or imposed-anchor-motion gaps. Free documentation does not imply unrestricted code/data reuse. A quality-assurance framework does not supply the missing numerical test targets. Keep each distinction visible in the implementation rather than burying it in a general disclaimer.

## 5. Instructions to the coding agent

### 5.1 First action: inspect the repository, not the marketing description

Create a short `verification/repo-assessment.md` before implementation. Identify the language and build system, numerical libraries, solver entry points, model schema, result schema, units, coordinate systems, element formulations, load-case model, supported analysis modes, UI command layer, agent/API entry points, and exporters.

Run the existing test suite and record its actual baseline. Do not overwrite unexplained failures. Find whether the solver can already run deterministically without the UI. If it cannot, introduce the smallest headless entry point consistent with the architecture; do not rewrite the solver to accommodate this plan.

Classify every feature as `implemented`, `partial`, `advertised_only`, `unsupported`, or `unknown`, with code locations and limitations. Separately classify its numerical evidence. Implementation presence is not a passing test result.

### 5.2 Non-negotiable project rules

| Rule | Required behavior |
|---|---|
| Preserve independent expectations | The application under test must never write the accepted analytical or external-reference target as a side effect of a normal test run. |
| Separate oracle and production code | Analytical oracles must not import production stiffness, geometry-property, load-assembly, or stress-recovery functions being tested. Small explicit duplication is intentional. |
| No hidden fixture repair | Never modify geometry, loads, boundary conditions, or source targets just to make a benchmark pass. Record and version justified corrections. |
| Freeze tolerances | Tolerance changes require a separate recorded rationale and comparison of old/new outcomes. Do not silently relax them after observing errors. |
| Fail closed | A missing target, missing result, unsupported required option, nonfinite value, timeout, empty case set, or zero-assertion run is not a pass. |
| Respect formulation differences | Reject an inapplicable comparison or create a separately named modeling variant. Do not force unrelated theories to share a target. |
| Preserve source rights | Unknown redistribution status blocks vendoring, not independent testing from authorized local inputs. Never bypass licensing or access controls. |
| Keep the application data-free | Test material values and section dimensions are fixture data, not a production material catalog. Do not import vendor databases. |
| No fictitious evidence | Never populate an external-run record with invented solver versions, hashes, results, approvals, or human review. |
| Preserve workflow scope | Do not add piping-code allowable-stress checks or agent-supplied material libraries as incidental work. |

An unavailable source or licensed program should produce a precise blocked-work record while unblocked work continues. It must not cause the agent to declare the whole plan complete or to abandon the open-source lane.

### 5.3 Initial implementation boundary

Use the repository's existing language and test runner unless there is a concrete reason not to. A small external harness is acceptable when needed for isolation, but avoid introducing a second application framework.

All paths and commands below are **proposed interfaces to implement or map to existing equivalents**. They are not claims that those files or commands already exist in the user's repository.

## 6. Qualification profiles and coverage matrix

### 6.1 Modular profiles

| Profile ID | Intended scope | Required evidence before marking the profile passed |
|---|---|---|
| `Q0-HARNESS` | Reliability of the test machinery | Schema tests, comparator boundary cases, corrupted-artifact tests, missing-output tests, and seeded-fault detection. Not counted as solver accuracy evidence. |
| `Q1-STRAIGHT-STATIC` | Linear straight-pipe/frame behavior | Analytical axial, bending, torsion, thermal, support-movement, reaction, and load-recovery tests in multiple orientations/units. |
| `Q2-PIPING-STATIC` | Assembled three-dimensional elastic piping | Applicable Hovgaard and elbow cases; gravity/thermal/nodal loads; elbows, rigid offsets, linear supports; applicable network interactions. |
| `Q3-RESTRAINT-NONLINEAR` | Gaps, one-way supports, lift-off, friction, and sequencing | Analytical piecewise cases, small independently solved support networks, transition tests, and an appropriate external comparison suite. Separate each supported law. |
| `Q4-MODAL` | Modal analysis | Analytical oscillators/beams, matched piping mode shapes/subspaces, mass and participation tests, and mesh/mode-count convergence. |
| `Q5A-RS-UNIFORM` | Uniform-support response spectra | Applicable NUREG/CR-1677 Volume 1 cases and independently tested modal/directional combination operations. |
| `Q5B-RS-MULTISUPPORT` | Independent-support response spectra | Applicable Volume 2 cases, excitation-group mapping, support correlation/combination assumptions, and separate imposed-support-motion tests where claimed. |
| `Q5C-RS-CORRECTIONS` | Missing-mass/rigid-response corrections | Applicable NUREG/CR-6645 implementation and isolated correction tests. |
| `Q6-HARMONIC-TRANSIENT` | Harmonic/time-history analysis | Analytical response cases, damping/phase tests, time-step studies, initial-condition and applied-load-history tests. Split this profile if only one mode exists. |
| `Q7-INTERCHANGE` | Specific export/import target and version | Semantic model checks, loss reports, target-solver runs, output equivalence, and negative tests for unsupported transfers. One subprofile per target format/version. |
| `Q8-AUTOMATION` | UI/API/agent operational parity | Model-state, command-sequence, save/reload, results-version, and permission tests through the actual supported interfaces. |
| `Q9-ADVANCED` | Additional implemented physics | Separate subprofiles for plasticity, large deformation, soil, expansion joints, or other special features; no implied blanket pass. |

For a release advertised as an elastic, static piping design tool with nonlinear supports and a particular export target, a reasonable proposed release boundary is `Q0 + Q1 + Q2 + Q3 + target-specific Q7`, plus `Q8` if agentic operation is advertised. Dynamics should not delay a static-only claim, but must not be included in it by implication.

### 6.2 Capability matrix fields

Each capability entry must identify its production code paths, governing assumptions, supported input ranges, analysis modes, applicable profiles, tests, required output quantities, reference types, and open discrepancies. Include interaction coverage, not only single-feature tests.

Useful domain descriptors include dimensionless geometry ratios such as length/diameter and bend-radius/diameter; thickness/diameter; support stiffness relative to member stiffness; prescribed thermal strain; load ratios; normalized gap; friction coefficient; and, for dynamics, time-step/frequency and frequency-cutoff ratios.

A handful of sampled values does not establish every point in the bounding box. Report the sampled domain and test design explicitly. Agent-selected parameter sweeps must store the generator version and seed.

### 6.3 Interaction tests that deserve explicit rows

| Interaction | Why it needs its own test obligation |
|---|---|
| Thermal loading + elbow flexibility + anchor movement | Exercises different sources of imposed strain/displacement in one assembled system. |
| Gravity + lift-off + friction | Changes normal forces and therefore tangential restraint capacity. |
| Pressure effects + bend flexibility + restraints | Exposes double counting, missing effects, and inconsistent pressure conventions. |
| Rigid offset + nodal force + local axes | Exercises lever arms, end-force signs, and coordinate transformations. |
| User stiffness matrix + rotated support | Exercises coupled translational/rotational stiffness and units. |
| Added mass + piping modes + response spectrum | Connects mass construction, modal extraction, participation, and spectral response. |
| Load-history edit + cached nonlinear result | Tests whether the application reruns the correct history instead of reusing stale state. |
| Exported material function + reference temperature | Tests property interpretation as well as file syntax. |

## 7. Analytical and derived test specifications

These are proposed project-authored tests. Implement them independently and document the assumptions beside the equations. They are not presented as new NRC or Code_Aster benchmark identifiers.

### 7.1 Common conventions

Use a right-handed local axis system with the straight member along local `x`. State whether an end force is the force **on the element**, **by the element on the joint**, or a signed section resultant. Distinguish force from mass and temperature from temperature difference.

For a circular annulus with outer diameter `D`, wall thickness `t`, and inner diameter `d = D - 2t`:

```text
A = pi * (D^2 - d^2) / 4
I_y = I_z = pi * (D^4 - d^4) / 64
J = I_y + I_z
G = E / (2 * (1 + nu))       [isotropic linear elasticity only]
```

Validate `D > 0`, `0 < t < D/2`, and the constitutive assumptions. Compute these in the oracle independently of the application's section-property implementation.

### 7.2 Initial analytical catalog

Here `F` is an axial or transverse point force as stated, `M` a bending moment, `T` a torque, `q` a force per unit length, `L` the span, and `E`, `G`, `A`, `I`, `J` the usual stiffness quantities. Equations below give magnitudes except where a sign is explicitly stated. The actual fixture must specify signed axes and reactions.

| Case ID | Setup | Required reference assertions |
|---|---|---|
| `AN-AXIAL-01` | Uniform member fixed at one end, axial tip force | `u = F L/(E A)`; axial force `F`; stress `F/A`; support reaction `-F`. |
| `AN-AXIAL-02` | Prescribed relative axial end displacement `delta` | `N = E A delta/L`; consistent equal/opposite reactions. |
| `AN-TORSION-01` | Circular member, fixed root, tip torque | `theta = T L/(G J)`; torque recovery; shear stress `T r/J` at a specified radius where that stress output is implemented. |
| `AN-BEND-01` | Euler–Bernoulli cantilever, transverse tip force | `v_tip = F L^3/(3 E I)`; `theta_tip = F L^2/(2 E I)`; root moment magnitude `F L`. |
| `AN-BEND-02` | Euler–Bernoulli cantilever, tip bending moment | `v_tip = M L^2/(2 E I)`; `theta_tip = M L/(E I)`; constant bending moment. |
| `AN-BEND-03` | Euler–Bernoulli cantilever, uniform transverse load | `v_tip = q L^4/(8 E I)`; root shear `q L`; root moment `q L^2/2`; field values at declared stations. |
| `AN-BEND-04` | Simply supported Euler–Bernoulli beam, uniform load | Reactions `q L/2`; midspan moment `q L^2/8`; midspan displacement `5 q L^4/(384 E I)`. |
| `AN-SHEAR-01` | Timoshenko cantilever with specified shear coefficient `kappa` | Tip-force displacement `F L^3/(3 E I) + F L/(kappa G A)`. Match the precise shear convention; do not compare to the Euler–Bernoulli target. |
| `AN-THERMAL-01` | Uniform temperature change, one end axially free | `u = alpha delta_T L`; zero axial thermal force for unconstrained expansion. |
| `AN-THERMAL-02` | Uniform temperature change, both ends axially fixed | `N = -E A alpha delta_T` in the small-strain, constant-property model; zero axial displacement. |
| `AN-THERMAL-03` | Tangent expansion coefficient prescribed as a temperature function | Independently integrate `epsilon_th = integral(alpha(T), T0, T1)`; test free and restrained cases. Do not apply this integral to a secant-coefficient definition. |
| `AN-MOTION-01` | Same prescribed translation at all restrained points, no other load | Compatible rigid translation with no induced strain/resultants. Also test unequal prescribed motion using `AN-AXIAL-02`. |
| `AN-SPRING-01` | Member and axial support spring in series | Under force `F`, total motion `F L/(E A) + F/k`; identical transmitted axial force. |
| `AN-SPRING-02` | Two ground springs in parallel at one degree of freedom | `u = F/(k1 + k2)`; individual reactions proportional to stiffness. |
| `AN-OFFSET-01` | Force transferred through a rigid offset vector `r` | Equivalent moment `r cross F`, force balance, and compatible rigid-link kinematics. |
| `AN-MASS-01` | Uniform straight pipe with separately specified added mass | Mass, center of mass, and inertial quantities from the explicit geometry/mass distribution; gravity load generated once. |
| `AN-MODAL-01` | One-degree-of-freedom mass/spring system | `omega_n = sqrt(k/m)`; `f_n = omega_n/(2 pi)`; applicable mode normalization and participation. |
| `AN-MODAL-02` | Uniform Euler–Bernoulli cantilever | `omega_1 = beta_1^2 sqrt(E I/(rho A))/L^2`, `beta_1 = 1.875104068711961`; refine the mesh and compare shapes at common stations. Exclude rotary inertia/shear from this reference variant. |
| `AN-HARMONIC-01` | Linear oscillator, force `Re(F0 exp(i omega t))` | Complex steady response `X = F0/(k - m omega^2 + i c omega)` under the same phasor convention. |
| `AN-TRANSIENT-01` | Undamped oscillator, `x(0)=x0`, `v(0)=0`, no applied force | `x(t)=x0 cos(omega_n t)`; displacement/velocity histories and time-step convergence. |

Also create separate tests for any implemented pressure stress, pressure-induced strain, effective axial force, or automatic end-cap loading. Define the physical/mechanical convention first. Do not make the identity `pressure × internal area` an indiscriminate expectation for every vendor's reported anchor force. The CAEPIPE manual, for example, explicitly documents its own end-cap-force reporting convention. [R27]

Basic elastic stress recovery, where supported, should be tested at specified section positions using independently combined axial/bending/torsional effects. Keep raw elastic stresses distinct from code stresses, stress intensification, and allowable-stress utilization. A code-compliance module is not part of this plan.

### 7.3 Nonlinear-restraint cases with tractable answers

**Unilateral elastic stop.** One degree of freedom has baseline stiffness `k > 0`, applied positive-direction force `F`, and a stop with gap `g >= 0` and contact stiffness `ks > 0`. Its restoring force is `ks max(u - g, 0)`. The exact piecewise displacement is:

```text
u = F/k                         when F <= k*g
u = (F + ks*g)/(k + ks)          when F > k*g
stop_force_magnitude = ks * max(u - g, 0)
```

Test below, exactly at, and above the transition, followed by unload/reload. A rigid-stop implementation uses the appropriate limiting problem, not an arbitrary finite `ks` without a penalty-error budget.

**Thermal expansion against a rigid stop.** An axial bar has stiffness `K = EA/L`, free thermal expansion `delta_th >= 0`, root fixed, and a rigid stop at tip displacement `g >= 0`. For this one-dimensional small-strain model:

```text
u_tip = min(delta_th, g)
N = -K * max(delta_th - g, 0)
```

Use this to test contact activation, reaction sign, and thermal-load assembly together.

**Monotonic friction slider.** A tangential spring of stiffness `kt` is pulled by prescribed displacement `d >= 0`; the slider has constant normal load `Nn > 0` and ideal Coulomb coefficient `mu`. Starting unstressed and sticking:

```text
slider_displacement = max(d - mu*Nn/kt, 0)
friction_force_magnitude = min(kt*d, mu*Nn)
```

This formula covers the stated monotonic path only. Reverse loading requires a separate incremental reference and state history. Distinguish constant-normal-load tests from piping cases in which lift-off or vertical deflection changes the normal load.

For small multi-support networks, independently enumerate admissible contact states or use a separately implemented analytical/convex formulation when applicable. Do not make the production nonlinear solver its own oracle.

Check contact admissibility in addition to final displacement: penetration bounds, permitted reaction sign, complementarity where appropriate, stick/slip bounds, and dissipation for the chosen law. At a mathematically exact transition, admissible forces and motion may be more meaningful than requiring a unique textual state label.

### 7.4 Manufactured-solution extension

Use SAND2000-1444 as a methodological starting point. [R22] Select a smooth displacement field, independently derive loads and boundary conditions from the governing continuous equations, and verify convergence of the implemented approximation.

A simple clamped Euler–Bernoulli beam example is:

```text
w(x) = C * x^2 * (L-x)^2
w(0) = w'(0) = w(L) = w'(L) = 0
q(x) = E I * w''''(x) = 24 E I C
```

Document the load/displacement sign convention. Add nonuniform fields where the application's load representation supports them.

Do not call `f = K_production @ u_chosen` independent element verification. That construction can test a linear solve, but shares the production matrix and can preserve its assembly or formulation errors.

### 7.5 Metamorphic and parameter-sweep tests

Transform a valid seed case and assert a relationship, rather than treating each transformed case as a new external benchmark. Required transformations should include equivalent unit systems; node/element renumbering; global rigid rotations of all appropriate geometry, loads, supports, and outputs; element subdivision; and, in applicable linear cases, load scaling and superposition.

Do not apply linear superposition to frictional or contact-history problems. Do not expect identical element-by-element results after remeshing; compare physical stations or conserved quantities. Do not rotate the geometry without rotating directional supports, gravity, and prescribed motion.

Add finite-difference checks of tangent stiffness where a tangent is exposed, and step-size studies of derivatives used by optimization. Test singular and nearly singular models separately: returning a controlled diagnostic is the correct result for a genuinely underconstrained case.

### 7.6 Oracle fault detection

Deliberately inject or simulate faults such as swapped local axes, reversed moment sign, missing factor of `1000`, omitted thermal load, doubled gravity, wrong section inertia, suppressed contact, dropped support motion, and incorrect `Hz`/`rad/s` conversion. Verify that relevant tests fail.

An oracle that cannot detect representative faults should not be counted as meaningful feature coverage. Keep mutation/fault-injection results separate from numerical benchmark counts.

## 8. Source acquisition and benchmark transcription

### 8.1 Source registry

Create `verification/sources/registry.yaml` and `verification/sources/lock.json`. Every acquired source must have a stable internal ID, title, publisher, original URL, resolved URL, acquisition timestamp, version/commit when applicable, content hash, access category, redistribution decision, and local-storage policy.

Use `null` for unknown values and make relevant gates reject unresolved required fields. Never insert a fake SHA-256 or an assumed upstream revision. The live Code_Aster `main` URLs in this report are discovery pointers; the executed suite must pin a real commit/tag and required binary assets.

Record reference-to-reference dependencies. An ANSYS result and its underlying NRC target are not two independent physical experiments. A Code_Aster result based on an ABAQUS reference must retain that lineage.

### 8.2 Acquisition sequence

| Stage | Agent action | Completion evidence |
|---|---|---|
| A | Acquire the SSLL106 documentation and the pinned `.comm`, `.export`, and declared mesh dependencies. | Verified hashes, dependency completeness, licence records, and a parsed acquisition manifest. |
| B | Acquire relevant SSLL101, SSLX102, SDLL14, and SDLX02 variants. | Explicit formulation-selection notes and source sections for every imported target. |
| C | Obtain NRC source reports and associated ANSYS problem/listing pages. | Case/page/table inventory and separate identities for original-reference and ANSYS-reference datasets. |
| D | Arrange authorized commercial reference execution or controlled result import. | Exact executable/version/settings and proof of actual run; no fabricated “reference passed” status. |
| E | Add optional NAFEMS/advanced/experimental sources. | Access and applicability decisions before fixtures are counted in a release profile. |

External test files are executable content. Parse dependency manifests as data, use a restricted work directory, and execute reference software in an appropriately isolated environment without repository secrets. Do not download-and-execute arbitrary scripts from a floating branch in CI.

### 8.3 Numerical transcription rules

Use authoritative machine-readable data where available. For report tables, capture table/section identifiers, units, signs, point IDs, and printed precision. If a source is scanned, unresolved visual transcription must remain an explicit blocker rather than a guessed value. Any OCR-derived value needs a verification record; do not bulk-promote OCR output to reference truth.

For every numerical fixture, produce `source-map.md`: each geometry/material/load item and each expected quantity points to its source location or to a project-authored derivation. Preserve original numerical strings when rounding matters. Record errata and ambiguities without silently correcting the source.

Independent extraction routes can help detect mistakes, but two agents using the same already-transcribed table are not two independent transcriptions. Record the actual acquisition and checking path.

### 8.4 Original versus adapted benchmarks

Retain an unmodified original-case identity whenever its complete intended formulation is reproduced. A changed mesh, altered restraint stiffness, substituted material, simplified elbow, omitted pressure effect, or different spectral-combination rule creates a named variant unless the source explicitly permits that variation.

A derived case may be valuable; it simply must not be reported as passing the untouched original benchmark. Report why an adaptation was necessary and which reference assertions remain applicable.

## 9. Repository architecture and data contracts

### 9.1 Suggested layout

Map this structure onto the existing repository rather than duplicating equivalent infrastructure.

```text
verification/
  README.md
  repo-assessment.md
  capability-matrix.yaml
  sources/
    registry.yaml
    lock.json
    permissions.md
  profiles/
    q1-straight-static.yaml
    q2-piping-static.yaml
    ...
  schemas/
    case.schema.json
    model.schema.json
    reference.schema.json
    result.schema.json
    run.schema.json
    profile.schema.json
  cases/
    analytical/
      an-axial-01/
        case.yaml
        model.yaml
        expected.yaml
        derivation.md
        source-map.md
      ...
    code-aster/
    nrc/
    cross-solver/
    interchange/
    automation/
    derived/
  oracles/
  adapters/
    application/
    code-aster/
    reference-file-import/
    commercial-targets/
  harness/
  self-tests/
  generators/
  discrepancies/
  docs/
    methodology.md
    conventions.md
    tolerance-policy.md
    standards-adoption.md
    benchmark-authoring.md
    claims-policy.md
    reference-execution.md
    qualification-report-template.md
  results/                  # generated; normally ignored in Git
  private-reference-cache/   # ignored; no credentials or restricted assets committed
  source-cache/             # content-addressed, with policy-controlled publication
  evidence-index.json       # links/hashes of published release evidence

tools/
  verify                    # proposed entry point, or existing project equivalent
```

Use JSON Schema or the repository's equivalent typed validation. Do not create a new general-purpose piping model format merely to run tests. A small benchmark contract and a normalized semantic snapshot are sufficient if the production format already represents the required information.

### 9.2 Required case contract

| Field group | Required information |
|---|---|
| Identity | Stable case ID, revision, title, original/adapted/derived classification, capability tags, profile membership. |
| Problem definition | Geometry, topology, dimensions, material values/functions, temperature convention, supports, rigid offsets, releases, loads, analysis sequence. |
| Formulation | Beam/pipe theory, bend representation, shear/rotary-inertia options, mass treatment, pressure effects, geometric/material nonlinearity settings. |
| Numerics | Mesh or subdivision rule, solver tolerances, load/time increments, damping, mode range, convergence requirements, random seed if used. |
| References | Reference kind, source ID/version/hash, source location, oracle revision or external-run ID, precision/uncertainty description. |
| Outputs | Exact physical locations, component IDs, units, coordinate frames, sign/end conventions, and quantity definition. |
| Acceptance | Per-output absolute/relative budgets or specialized metric; required diagnostics; applicability and exclusions. |
| Provenance | Authoring/checking actor types, execution history, actual human-review status, adaptation notes, licence/storage policy. |

For coupled support stiffness, record the full matrix, degree-of-freedom ordering, reference point, axes, and the dimensions of each block. A mixed translation/rotation matrix cannot be treated as a single unitless array.

### 9.3 Example synthetic benchmark

The following is an **original simple fixture**, not a transcription of SSLL106. Its expected values were evaluated for this report from the stated annular area and axial-bar equations. The user's application has not been run on it.

`case.yaml`:

```yaml
schema_version: 1
id: AN-AXIAL-01
revision: 1
title: Synthetic straight pipe under axial tip load
case_origin: project_authored
capabilities: [linear_static, axial_stiffness, section_properties, reactions]
profiles: [Q1-STRAIGHT-STATIC]
model_file: model.yaml
reference_file: expected.yaml
reference_kind: analytical
reference_readiness: transcribed
execution_status: not_run
assumptions:
  - isotropic_linear_elastic
  - small_strain_small_displacement
  - uniform_straight_annular_member
  - no_pressure_no_thermal_load_no_gravity
review:
  derivation_author_type: agent
  human_review_performed: false
required_result_status: converged
```

`model.yaml`:

```yaml
schema_version: 1
units:
  length: m
  force: N
  stress: Pa
  rotation: rad
coordinate_system:
  handedness: right
  frame: global
nodes:
  A: [0.0, 0.0, 0.0]
  B: [2.0, 0.0, 0.0]
materials:
  synthetic_elastic:
    E: 200000000000.0
    nu: 0.3
sections:
  annulus:
    outer_diameter: 0.1
    wall_thickness: 0.005
elements:
  - id: E1
    type: straight_pipe
    nodes: [A, B]
    material: synthetic_elastic
    section: annulus
    local_y: [0.0, 1.0, 0.0]
constraints:
  - node: A
    dofs: [UX, UY, UZ, RX, RY, RZ]
    values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
loadcases:
  - id: AXIAL
    type: linear_static
    nodal_loads:
      - node: B
        frame: global
        force: [10000.0, 0.0, 0.0]
        moment: [0.0, 0.0, 0.0]
```

`expected.yaml`:

```yaml
schema_version: 1
reference_kind: analytical
source_id: PROJECT-AN-AXIAL-01
source_location: derivation.md
loadcase: AXIAL
quantities:
  - id: node.B.displacement.x
    frame: global
    unit: m
    value: 0.00006701260761764011
    atol: 1.0e-11
    rtol: 1.0e-7
  - id: node.A.reaction.x
    definition: support_force_on_structure
    frame: global
    unit: N
    value: -10000.0
    atol: 1.0e-4
    rtol: 1.0e-7
  - id: element.E1.section.axial_force
    definition: tension_positive
    frame: local
    unit: N
    value: 10000.0
    atol: 1.0e-4
    rtol: 1.0e-7
  - id: element.E1.section.axial_stress
    definition: direct_elastic_axial_stress
    unit: Pa
    value: 6701260.761764012
    atol: 1.0
    rtol: 1.0e-7
checks:
  - finite_required_outputs
  - required_output_ids_present
  - converged
  - independently_reconstructed_force_balance
```

These example tolerances are proposed for this simple, well-conditioned axial case, not universal industrial acceptance criteria. The final fixture should also assert expected zero transverse responses/rotations with explicit absolute budgets, and test section area and strain energy where those outputs are supported. Register `PROJECT-AN-AXIAL-01` as a project-authored derivation, not as an external publication.

Reference quantities:

```text
A = 0.0014922565104551523 m^2
u_Bx = F L/(E A) = 0.00006701260761764011 m
sigma_axial = F/A = 6701260.761764012 Pa
strain_energy = F^2 L/(2 E A) = 0.3350630380882006 J
```

The numerical values are rounded evaluations, not new measured material data. Keep the symbolic equations and full-precision generation path in `derivation.md` and the oracle.

### 9.4 Normalized results

Store one record per quantity or an equivalent typed structure. Keys must include case, loadcase/step, physical location, quantity, component, frame, units, and definition. Dynamic records additionally need mode/frequency/time and normalization or phasor convention.

Raw vendor reports remain immutable evidence. A normalized record must point back to its raw source location. Preserve missing/unsupported values as explicit states; never convert blank output, overflow markers, failed parses, or `NaN` to zero.

Keep member-end nodal actions distinct from section forces. Keep nominal elastic stress distinct from stress-intensified output. Keep absolute and relative seismic displacement distinct. Keep signed time-history results distinct from unsigned spectral envelopes.

### 9.5 Run manifest

Every run must record the application commit and build identifier, executable/artifact hash, dirty-tree status, harness/adapters/oracles/profile revisions, input and reference hashes, OS/architecture, numerical-library/compiler versions when relevant, thread settings, seeds, actual command, exit status, convergence diagnostics, timestamps, elapsed time, and artifact locations.

Include `run_purpose: development | release_qualification | installation_check | reference_acquisition`. A failed or interrupted run is still evidence and must retain its diagnostics. A release-qualification report must not silently reuse results from a different build or input hash.

### 9.6 State handling

Keep **readiness** (`discovered`, `acquired`, `transcribed`, `reference_reproduced`, `ready`) separate from **outcome** (`not_run`, `pass`, `fail`, `blocked`, `not_applicable`, `error`).

`not_applicable` needs a documented formulation/scope reason. It is not a pass and does not cover a required capability. `blocked` and expected failures may exist during development, but cannot satisfy required release assertions.

## 10. Comparison and acceptance rules

### 10.1 Scalar quantities

After explicit unit and convention conversion, use:

```text
absolute_error = abs(actual - reference)
allowed_error = atol + rtol * abs(reference)
pass = absolute_error <= allowed_error
```

Require finite values, nonnegative tolerances, matching quantity definitions, and the complete required output set before evaluating this condition. A wrong sign on a meaningful signed result is a failure, even if a magnitude-only plot looks correct.

For near-zero reference values, the absolute budget is controlling. Set it from an independently chosen quantity scale and the purpose of that assertion. Do not enlarge it based on the observed candidate error or normalize it by the largest unrelated output.

### 10.2 Tolerance policy

| Test class | Proposed policy |
|---|---|
| Exact algebraic identities / schema / units | Exact equality when appropriate; otherwise a documented floating-point budget. |
| Exactly representable, well-conditioned analytical cases | Start with strict case-specific budgets, typically relative targets around `1e-6` or tighter where justified. This is a project starting target, not a sourced universal threshold. |
| Discretized analytical cases | Require convergence and an error target for the stated discretization; do not conceal discretization error inside arbitrary loose comparison tolerance. |
| Published numerical references | Record reference precision/accuracy and select justified per-quantity acceptance budgets. A cited 2% accuracy statement is not automatically a 95% confidence interval or a universal 2% pass rule. |
| Cross-solver cases | Predefine the common modeling assumptions and comparison budget. Unexplained disagreements require investigation, not averaging. |
| Contact/friction | Combine output-error budgets with admissibility, equilibrium, path, and increment-refinement requirements. |
| Export semantics | Exact semantic preservation where required; permitted numerical rounding gets its own budget; approximations require explicit declared loss. |

Before making a parity claim, each required assertion's tolerance must have `rationale`, `units`, `reference_basis`, and a recorded policy revision. Initial suggested values in this report are not automatic approval of every future tolerance.

### 10.3 Vectors, fields, extrema, and frames

Compare signed components in a declared common frame and add norms as supplementary metrics. A vector norm alone can hide swapped axes or wrong directions.

For different meshes, map to specified physical locations using a documented interpolation/projection method. Keep the mapping independent of the error being measured. Compare fields or multiple stations as well as extrema. When multiple near-equal maxima exist, define an admissible location set rather than requiring an arbitrary node number.

### 10.4 Modal comparison

Match modes using both frequency and shape information, not index alone. A mode shape may change sign without changing the physical mode. Cluster repeated or nearly repeated eigenvalues and compare the corresponding subspaces instead of demanding identical basis vectors.

A useful shape metric is a weighted modal assurance criterion:

```text
MAC(phi, psi; W) = |phi^T W psi|^2 /
                   ((phi^T W phi) * (psi^T W psi))
```

Use a documented common coordinate map and weight matrix `W`. Avoid mixing translations and rotations without a defined scaling/metric. For clustered modes, use principal angles or projection/subspace metrics on the matched cluster. Predefine frequency-clustering and acceptance rules.

Also test eigenproblem residuals, applicable orthogonality, effective modal mass, participation, and selected-mode coverage. An apparently close frequency does not qualify an incorrect mass model.

### 10.5 Response spectra

Record the damping, spectral quantity and units, interpolation convention, excitation direction/group mapping, frequency truncation, modal combination, directional combination, support combination, rigid-response option, and missing-mass treatment.

First test the individual combination operations with small constructed inputs; then test full piping networks. Do not check static equilibrium by summing independently combined envelope maxima as though they occur simultaneously. Apply equilibrium/residual checks to appropriate signed constituent solutions, not an incompatible collection of envelope components.

### 10.6 Harmonic and transient results

Harmonic comparisons should include complex response or amplitude and phase under the same convention. Do not compare only amplitude if phase affects the intended use.

For transients, compare physical time histories, peak values/times, and convergence under time-step refinement. Do not silently shift time histories to maximize agreement. Initial state, load interpolation, damping, and nonlinear restart behavior are part of the model.

### 10.7 Residual, equilibrium, and energy checks

Reconstruct net forces and moments from normalized applied loads and reactions where meaningful. For linear solves, inspect a suitably scaled residual on unconstrained degrees of freedom, accounting for prescribed displacement terms. For nonlinear solves, check the residual and constraint/contact conditions at required load steps.

Use energy identities only under their stated assumptions. For example, the familiar `U = 0.5 * f^T u` is not an indiscriminate check for every combination of thermal strain, prescribed motion, preload, and nonlinear history.

### 10.8 Convergence studies

For relevant spatial, temporal, load-step, and modal-truncation discretizations, run a refinement sequence and publish error/stability measures. With a known reference and uniform refinement, observed order can be estimated from successive errors, but flag cases near roundoff, zero error, or outside an asymptotic regime.

A numerical result that stops changing is not thereby the correct result. Require the appropriate reference comparisons as well as convergence. Conversely, a known formulation difference must not be “fixed” merely by refining a fundamentally different model.

### 10.9 Comparator self-tests

Test exact-boundary passes, just-outside-budget failures, near-zero references, wrong units, wrong frames, missing IDs, duplicate IDs, unexpected loadcases, nonfinite/overflow values, malformed numeric strings, shuffled rows, eigenvector sign changes, repeated-mode basis rotations, and interrupted files.

Reporting must preserve the full assertion denominator. A parser that drops an unrecognized result row must produce a failed or blocked required assertion, not a smaller set of successful comparisons.

## 11. Reference-solver adapters and interoperability

### 11.1 Adapter contract

Each adapter should expose the equivalent of `describe_capabilities`, `prepare_model`, `run`, `collect_raw_artifacts`, `normalize_results`, and `describe_model_semantics`. Unsupported capabilities must produce structured diagnostic output before a comparison can be marked ready.

For commercial engines without suitable automation access, support controlled import of real native input files, raw result reports, and an execution manifest. Do not invent command-line flags or APIs; discover the installed version's supported interface and document it.

### 11.2 Two independent comparison routes

| Route | Purpose |
|---|---|
| Benchmark specification → application adapter; separately → reference adapter | Tests numerical agreement while reducing dependence on the application's production exporter. |
| Application model → production export → target import/run | Tests the actual handoff workflow that users will rely on. |

Use both. Sharing a normalized benchmark definition is reasonable; sharing the very production conversion routine being tested defeats the independence of that particular check.

### 11.3 Semantic transfer inventory

The target's reconstructed model must be compared with the intended benchmark for geometry/topology, node/element identities, local axes, section dimensions, effective thickness, material values/functions, reference/operating temperatures, stiffness/flexibility factors, supports/gaps/friction, releases, rigid links/offsets, imposed movements, mass/weight distribution, pressure effects, load directions, load histories, damping, spectra, and analysis options.

Not every file format can be assumed to carry every item. Maintain a format/version capability map and a **loss report** with `preserved`, `transformed_exactly`, `approximated`, `omitted`, and `unsupported` entries. A required omitted feature blocks a claim of faithful export.

Where possible, read the target program's own model listing rather than only parsing the file produced by the application. Round-trip identity alone can preserve a shared mistake.

### 11.4 Reference acquisition and updates

Pin each reference executable and its options. Store actual raw outputs plus normalized data and hashes. A solver upgrade, parser change, default-setting change, or reference-data correction creates a new reference revision.

Frozen authorized reference outputs can keep ordinary CI independent of commercial licence availability. For a release, rerun references when an input, formulation, target setting, or relevant target version changes; never claim a fresh external execution merely because stored outputs were compared again.

Do not publish restricted vendor decks/reports automatically. Keep the public open-reference lane usable independently, and clearly label comparisons that require authorized external assets to reproduce.

### 11.5 Disagreement workflow

On a discrepancy, preserve all artifacts and investigate in order: transcription and units; geometry/topology; formulation/settings; load/support sequencing; output definitions and signs; discretization/convergence; then suspected implementation errors.

Do not select the majority answer as correct. Record whether the discrepancy is explained by a model difference, an input defect, a parser defect, a source ambiguity, a candidate-solver defect, or remains unresolved. Only resolved issues may change the relevant reference or acceptance specification, and those changes must be versioned.

## 12. UI, agent, and optimization testing

### 12.1 Same model, different entry paths

Create representative cases through the headless API, UI command layer, actual UI controls where feasible, and agent tool interface. Compare the resulting canonical semantic snapshots and numerical results. A command-layer test alone does not cover field widgets, unit selectors, selection state, or display-to-model conversion.

Test save/reload, undo/redo, model revision changes, cache invalidation, cancellation, failed solves, and export of the current versus an outdated model. Every displayed or exported result must identify the model and solver revision that produced it.

### 12.2 User data and knowledge-base behavior

Supply material and component values through the same user-input path as normal use. Test missing required properties, conflicting units, tabular interpolation, reference temperature, out-of-range evaluation, and provenance.

The knowledge base should cite test/profile evidence when describing supported behavior. It must not turn a missing material value into an invented “approved” property. Agent-generated assumptions should remain explicitly marked and distinguishable from benchmark inputs.

### 12.3 Semantic parity is an executable requirement

For a defined task, compare the actual command sequence, final model state, units, loadcases, options, diagnostics, and results—not the wording of an agent's explanation. The agent API must receive unsupported-feature and qualification-domain information, not just the UI.

Separate permissible design variables from fixed problem assumptions. An optimizer should not improve an objective by deleting a required load, weakening an externally imposed constraint, changing material properties, or changing an acceptance threshold outside its authorized task.

### 12.4 Optimization-specific numerical tests

Store search seeds, objectives, fixed assumptions, permitted variables, and evaluation histories. For representative tasks, compare selected candidates and finalists with an external reference, including nearby perturbations and active-set transitions where relevant.

Test whether candidate rankings and claimed improvements survive those comparisons. Keep optimization performance claims separate from basic per-case numerical agreement. Nondeterministic agent behavior requires repeated task-level evaluation; a single successful demonstration is not a reproducibility claim.

## 13. CI, release gates, and evidence retention

### 13.1 Execution lanes

| Lane | Typical trigger | Required behavior |
|---|---|---|
| Fast deterministic | Every change | Schema/oracle/comparator self-tests, core analytical tests, unit/axis checks, representative API and export tests. |
| Extended open-reference | Scheduled and release candidate | Broader Code_Aster/NRC-derived coverage, parameter sweeps, convergence studies, applicable independently runnable references. |
| Authorized external reference | Manual authorized trigger or controlled scheduled runner | Execute licensed targets or verify controlled imported artifacts without exposing licences, credentials, or restricted files. |
| Packaged-build acceptance | Every release candidate | Run the selected suite against the actual distributed application artifact, not only a developer build. |
| Installation/environment check | User/local installation | Run a portable disclosed subset and report platform-specific outcomes without claiming it covers every application feature. |

Choose execution budgets from observed repository performance. Do not invent a runtime promise before the suite exists. Pin dependency versions and numerical execution settings where feasible, and record legitimate platform differences.

### 13.2 Proposed command contract

These commands are implementation targets; map them to existing project tooling where appropriate.

```sh
./tools/verify doctor
./tools/verify validate-schemas
./tools/verify list --profile Q1-STRAIGHT-STATIC
./tools/verify sources-check
./tools/verify run --profile Q1-STRAIGHT-STATIC --adapter application
./tools/verify run --profile Q2-PIPING-STATIC --adapter code-aster
./tools/verify compare --run <candidate-run-id> --reference <reference-run-id>
./tools/verify report --run <run-id> --format markdown,json,junit
./tools/verify gate --profile <profile-id> --run <run-id>
```

`doctor` should report actual dependency/adapter availability. `sources-check` verifies hashes and required assets without inventing missing references. `run` must not mutate expectations. `gate` should return nonzero for missing mandatory evidence, not only numerical mismatches.

Keep reference acquisition/update a separate command with an explicit audit record, such as `reference-import` or `reference-refresh`; normal CI must not auto-bless new expected outputs.

### 13.3 Release gate definition

A profile can be marked passed only when its declared scope is fixed, all mandatory cases and assertions are present, required sources are ready, all required outcomes pass on the selected build, and no blocking discrepancy remains in scope.

The gate must also verify convention compatibility, reference provenance, justified tolerances, required convergence/diagnostic tests, applicable interaction coverage, relevant supported-platform checks, and production-export tests when export is included in the claim.

**Zero required tests passing out of zero tests is not a passing qualification.** Neither `skip`, `xfail`, `not_applicable`, `blocked`, nor a missing licensed run can satisfy a mandatory assertion. A development run may contain such states, but its report must remain visibly incomplete.

A failure outside the claimed scope can be documented without blocking a narrower release. A failure inside the scope requires repair or an explicit reduction of the profile and corresponding claim. Do not hide it in an overall pass percentage.

### 13.4 Report content

Produce a machine-readable report and a human-readable Markdown report from the same data. Include:

| Report section | Contents |
|---|---|
| Identification | Application/build/profile/harness/reference versions and hashes; execution environment. |
| Scope | Capabilities, sampled ranges, formulations, output types, and exclusions. |
| Evidence summary | Counts by case family, reference type, profile, and outcome; separate original cases from generated variants and individual assertions. |
| Results | Reference/actual values, signed and absolute differences, budgets, pass/fail status, and source locations. |
| Numerical studies | Mesh, time-step, iteration, penalty, and mode-count studies where applicable. |
| Transfer evidence | Target format/version, model-semantic comparison, loss report, and actual target-run provenance. |
| Defects and limitations | All unresolved discrepancies and their affected scopes; unavailable references and unperformed activities. |
| Review history | Actual automated/manual activities and actor types; no implied human examination. |
| Reproduction | Commands, inputs, dependencies, permissions, and publicly available or restricted artifact locations. |

Do not expose private paths, user models, licence-server information, or credentials in public reports. Distinguish a fully public reproducible result from a disclosed result whose raw evidence has access restrictions.

### 13.5 Retention and regression policy

Keep immutable evidence for each public qualified release: application artifact identity, case/profile/reference locks, normalized results, raw output or authorized archival pointer, comparison results, and discrepancy history.

Add a regression test for each fixed numerical, parser, modeling, or exporter defect. A failed reference comparison discovered after release should generate a documented affected-version/profile notice and a targeted rerun, not just a silent baseline update.

## 14. Implementation backlog and completion criteria

Implement as small reviewable changes, even when the reviewer is another automated process. The table gives a dependency sequence, not a calendar estimate.

| Work package | Dependencies | Deliverables | Completion criterion |
|---|---|---|---|
| **WP0 — Repository assessment** | None | Assessment, existing-test baseline, feature inventory, headless-run decision. | Every advertised solver/transfer capability mapped to implemented code or a documented unknown; existing failures retained. |
| **WP1 — Contracts and provenance** | WP0 | Schemas, source registry/lock, profile format, conventions, discrepancy format. | Valid fixtures accepted; missing references, unknown units, duplicate output IDs, and incompatible conventions rejected. |
| **WP2 — Harness and comparator** | WP1 | Runner, artifact capture, normalization interface, scalar/specialized comparators, reporting skeleton. | Seeded parsing/comparison failures cannot produce a passing report; zero-assertion and missing-output gates tested. |
| **WP3 — Analytical core** | WP2 | Independent oracles and applicable §7 fixtures, including rotations/units and prescribed motion. | `Q1` evidence produced against the actual application; any failures localized and documented; relevant injected faults detected. |
| **WP4 — Code_Aster static acquisition** | WP1–WP3 | Pinned SSLL106, SSLL101, SSLX102 variants and dependencies; formulation notes; source maps. | At least the selected upstream cases can be independently executed where supported; candidate comparisons use correctly typed targets. |
| **WP5 — Nonlinear restraints** | WP3 | Gap, thermal stop, friction, lift-off, sequence, and small-network tests; increment/penalty studies. | Each claimed law passes its analytical/independent checks, including transitions and relevant interactions; external evidence added before a cross-solver parity claim for this profile. |
| **WP6 — Modal and spectral coverage** | WP3–WP4, applicable dynamics | Modal metrics; SDLL14/SDLX02; applicable NRC cases; separate combination/correction tests. | No index-only modal matching; required frequencies/shapes/participation/response quantities pass with settings and reference origins documented. |
| **WP7 — Reference and exporter adapters** | WP1–WP3 | Independent reference-generation route, production-export route, target model listing parser, loss reports. | Equivalent model semantics established for each claimed target; required omissions and corrupt exports fail; real reference outputs preserved. |
| **WP8 — UI and agent workflow** | WP3, WP7 | Actual-interface tests, command/task fixtures, state snapshots, cache/version checks, input-provenance tests. | Same intended task produces matching models/results; forbidden assumption changes and stale-result exports are detected. |
| **WP9 — Release evidence and gates** | Applicable prior packages | Profile reports, CI lanes, packaged-build checks, public evidence index, claims template. | Fresh execution on the distributed artifact produces a reproducible report; a deliberately failed required assertion blocks qualification. |
| **WP10 — Extended robustness** | Initial profiles | Held-out cases, seeded sweeps, larger networks, optimizer-neighborhood tests, optional advanced/physical references. | Additional covered domain is explicitly reported; new failures enter the discrepancy and regression process. |

### 14.1 Suggested first milestone

The first useful milestone is **not** the entire NRC suite. It is a working harness, a source/units convention, the synthetic axial case, basic bending/torsion/thermal cases, and a report that honestly fails when an injected numerical error is introduced.

Then reproduce a selected SSLL106 reference run and one applicable Hovgaard static case. Add production-export semantic tests early. For a mainly static design product, nonlinear restraints and thermal/support interactions generally deserve implementation attention before optional advanced dynamic profiles.

### 14.2 Capability-specific minimum evidence policy

For each claimed capability, require at least an isolating test with a justified target, a system/interaction test, a suitable orientation or unit transformation where applicable, a numerical-refinement/robustness check when relevant, and a representative seeded-fault detection test.

This is a **coverage obligation**, not a magic case count. Some capabilities require several formulations, load paths, or limit states. Hundreds of variations of the same easy axial case do not substitute for one missing friction or elbow test.

### 14.3 Handling changes while implementation proceeds

Separate solver fixes from changes to benchmark definitions, references, and tolerances whenever possible. Every numerical behavior change should identify which test exposed it and which profiles need rerunning.

Maintain a previously withheld assessment set for major releases. Once a case has been used repeatedly to tune the implementation, retain it as a regression case but record that history. Add fresh independently specified cases rather than describing the tuned set as an untouched assessment.

## 15. Publication and claim templates

### 15.1 Evidence-qualified numerical claim

Use only after the named profiles and comparisons have actually passed:

> Release `<version/build>` meets the published acceptance criteria of Benchmark Profile `<profile/revision>` for `<capabilities and sampled domain>`. The suite includes `<analytical families>`, `<published piping cases>`, and equivalent-model comparisons with `<products, versions, settings>`. Inputs, reference provenance, tolerances, results, exclusions, and unresolved discrepancies are provided in `<evidence location>`.

A stronger comparative statement requires actual supporting comparisons:

> Within the disclosed common modeling domain and output set, this release demonstrates comparable numerical performance to `<identified reference implementations>` under the published comparison criteria.

### 15.2 Claim when only published vendor outputs were compared

> This release reproduces the specified published numerical values in `<manual/version/case IDs>` within the disclosed tolerances under the documented modeling assumptions. The referenced commercial program was not executed as part of this assessment.

Do not convert that statement into “tested against the current installed version” or a vendor endorsement.

### 15.3 Experimental or partially qualified release

> The application is published as an experimental design and analysis tool. Profiles `<list>` have completed the disclosed numerical test program; profiles `<list>` remain untested, blocked, or incomplete. No independent human review of the solver source or equations has been performed. Results and transfer limitations are documented per profile.

Populate this from actual metadata. Do not pre-fill completed profiles merely because their test files exist.

### 15.4 Claims the evidence package should prevent

Do not automatically generate “fully validated,” “certified by NASA/ASME/NRC,” “equivalent to all established piping software,” “passes all NRC benchmarks,” or “human-verified hand calculations.” Those statements require facts not supplied by this report and, in several cases, substantially broader evidence than the proposed initial profiles.

A project-generated profile badge should identify scope and build. It should not resemble or imply external certification. Keep code-compliance checking, material-database accuracy, site-specific engineering acceptance, and vendor QA-program equivalence outside the numerical claim unless separately established.

## 16. Open decisions and blocked work

The agent should resolve repository-discoverable issues itself. Only genuinely external decisions need escalation.

| Decision or dependency | Default implementation stance | Escalate when |
|---|---|---|
| Actual solver formulations and feature scope | Inspect implementation and create explicit capability records. | Code and advertised behavior materially conflict or governing assumptions cannot be established. |
| Initial public claim | Start with completed narrow profiles; do not assume whole-product parity. | Owner must choose the intended public scope. |
| Property conventions | Make units, expansion definition, reference temperature, and interpolation explicit. | Existing behavior is ambiguous or incompatible with required export semantics. |
| Reference engines | Build the open lane first and generic adapters next. | A specific licensed installation, supported automation interface, or external run is needed. |
| Asset redistribution | Use pointers and local caches until permission is established. | Vendoring or publishing licensed/reference assets is proposed. |
| Per-quantity tolerances | Implement policy and record provisional versus finalized status. | A budget is justified only by observed disagreement or the intended accuracy target has not been specified. |
| Missing/scanned report information | Record exact source/table blockers and continue unrelated work. | Reliable input or target transcription cannot be established. |
| Unsupported dynamics/advanced physics | Exclude from current profile and preserve backlog entries. | The proposed public claim includes that feature. |
| Deployment environments | Inspect current build targets and test the actual distributed artifact. | Platform support is promised without available execution evidence. |
| Human review | Record `not_performed` unless it actually occurs. | A claim or external program requires a review activity not provided by the project. |

Recommended discrepancy record fields: issue ID, affected cases/profiles/builds, expected/actual quantities, source and input hashes, reproduction command, classification, numerical impact, current hypothesis, disposition, resolution evidence, and regression test added.

## 17. Coding-agent handoff prompt

The owner can give the agent this section together with the full document and repository access.

> Integrate the numerical qualification program described in this document into the existing repository. Begin by inspecting the repository and writing an implementation/capability assessment. Reuse existing tooling and do not assume a programming language, solver formulation, headless API, external licence, or complete feature set.
>
> Implement the contracts, provenance registry, immutable reference handling, runner, comparators, self-tests, analytical fixtures, and reports before importing a large benchmark corpus. Then integrate compatible Code_Aster cases and applicable NRC problems with pinned sources, complete dependencies, explicit modeling assumptions, and source maps for every target.
>
> Keep the independent benchmark-to-reference route separate from tests of the production exporter. Include units, local frames, property interpretation, support/load sequencing, mass, pressure conventions, and target model semantics in the comparison. Add actual UI/API/agent workflow tests and preserve model/result version identities.
>
> Do not copy expected outputs from the application under test, silently relax tolerances, omit failed assertions, guess missing reference values, invent human review, or report unexecuted external comparisons as completed. Unknown source permissions must block redistribution, not cause hidden licence assumptions. No code-compliance module or production material database is requested.
>
> Work in small changes following WP0 through the applicable work packages. Continue unblocked tasks when an external asset or decision is unavailable. After each work package, report changed files, tests actually run, exact outcomes, remaining discrepancies, and the next dependency. The final deliverable is a reproducible evidence package and profile-specific release gate, not merely a directory of example models.
>
> The published claim must be generated from completed evidence. A narrow passing profile is acceptable; unsupported, blocked, or failed capabilities must remain outside that claim.

## 18. Annotated reference register

All access observations below are from **24 September 2026**. Links are source pointers, not promises that an upstream URL or floating branch will remain unchanged. The agent must acquire and hash the actual assets used. “Inspected” does not mean the corresponding benchmark was executed.

### 18.1 NRC and published commercial implementations

| ID | Reference | Inspection and next action |
|---|---|---|
| R01 | [NUREG/CR-1677 Volume 1 — Piping benchmark problems: uniform support motion][R01] | UNT archival metadata/abstract inspected; includes persistent identifier and report access. Acquire complete report and preserve page/table provenance. |
| R02 | [NUREG/CR-1677 Volume 2 — Independent support motion][R02] | NTIS record/abstract inspected. Obtain complete source before transcribing all four cases. |
| R03 | [NUREG/CR-6414 — AP600 piping benchmark problems][R03] | UNT archival metadata/abstract inspected. Acquire original numerical definitions and settings. |
| R04 | [ANSYS NRC Piping Benchmarks Overview, 2026 R1][R04] | Overview inspected; useful entry point to archived/new-element variants and source provenance. |
| R05 | [ANSYS VM-NR1677-02-1][R05] | Problem page, element choices, result tables, and input links inspected. |
| R06 | [ANSYS VM-NR6645-01-1][R06] | Problem page, correction cases, results, and input links inspected. |
| R31 | [ANSYS vm-nr1677-02-1a input listing][R31] | Linked input listing accessible and inspected. Public readability is not an open-source licence. |
| R32 | [ANSYS vm-nr6645-01-1a input listing][R32] | Linked input listing accessible and inspected. Keep vendor and original-report targets distinct. |

### 18.2 Code_Aster documentation and executable assets

| ID | Reference | Inspection and next action |
|---|---|---|
| R07 | [SSLL106 / V3.01.106 — Straight pipe][R07] | Test overview inspected; follow its problem, solution, and formulation pages. |
| R08 | [Code_Aster `ssll106a.comm`][R08] | Actual command/assertion source read; floating `main` pointer. Pin a revision before execution or reuse. |
| R09 | [Code_Aster `ssll106a.export`][R09] | Dependency file read; identifies `.comm` and `.mmed` inputs. |
| R10 | [SSLL101 / V3.01.101 — Hovgaard static piping][R10] | Overview and formulation choices inspected. |
| R11 | [SSLL101 reference solutions][R11] | Beam/pipe reference distinctions and uncertainty statement inspected. |
| R12 | [SSLX102 / V3.05.102 — Bent piping in bending][R12] | Overview and ovalization-related formulation scope inspected. |
| R13 | [SSLX102 reference solutions][R13] | Reference displacement values and accuracy statement inspected. |
| R14 | [SDLX02 / V2.05.002 — Hovgaard spectral analysis][R14] | Overview and stated numerical-reference basis inspected. |
| R23 | [SDLL14 / V2.02.014 — Thin elbow vibration modes][R23] | Overview and variant-dependent reference types inspected. |
| R24 | [SSNL503 / V6.02.503 — Elastoplastic elbow collapse][R24] | Overview and ABAQUS reference identification inspected. |
| R25 | [Code_Aster pipe-element usage guide: examples][R25] | Further test identifiers located; not a complete audit of those extended cases. |

### 18.3 Methodology and additional evidence sources

| ID | Reference | Inspection and next action |
|---|---|---|
| R15 | [NASA-STD-7009B — Standard for Models and Simulations][R15] | Official PDF inspected, including the verification section. Use a project adoption matrix, not an assumed certificate. |
| R16 | [NASA-HDBK-7009B official catalog entry][R16] | Official revision/date/access information inspected. |
| R17 | [NASA-HDBK-7009B linked PDF][R17] | Cover and selected interior pages inspected; note the interior-header inconsistency described in §3.2. |
| R18 | [ASME V&V 10-2019 (R2025)][R18] | Official scope/product information inspected; full purchased standard not audited. |
| R21 | [NAFEMS Benchmark Challenge][R21] | Public problem/solution index inspected. Select formulation-compatible supplementary cases. |
| R22 | [Sandia SAND2000-1444 — Method of Manufactured Solutions][R22] | Official publication record inspected; contains DOI/OSTI routes to the report. |
| R26 | [NAFEMS R0081 — Contact, Gapping and Sliding][R26] | Public contents and access information inspected; full publication not acquired. |
| R29 | [NUREG/CR-6983 — JNES/NUPEC large-scale piping tests][R29] | Official abstract surfaced in search; subsequent direct retrieval returned access denied. Supplementary lead only; full report/data not inspected. |

### 18.4 Vendor descriptions of testing and QA

| ID | Reference | Inspection and next action |
|---|---|---|
| R19 | [Bentley AutoPIPE Acceptance Test Set][R19] | Official description inspected; ATS is a version-specific subset, with separate access arrangements. |
| R20 | [MetaPiping Quality Assurance][R20] | Official reference list and validation-tool/reporting description inspected; underlying private test projects not audited. |
| R27 | [CAEPIPE Technical Reference Manual — Anchor][R27] | Official manual page inspected, including reference-manual pointer and pressure-force convention. |
| R28 | [CAEPIPE announcement identifying updated Verification Manual][R28] | Vendor evidence that the manual exists; not the manual itself and not a current case-count assertion. |
| R30 | [Octave Aspect Pipe Stress, formerly CAESAR II][R30] | Official product/QA statements inspected. Attribute the claims to the vendor; do not transfer them to this project. |

### 18.5 Source links

[R01]: https://digital.library.unt.edu/ark:/67531/metadc1211143/ "NUREG/CR-1677 Volume 1 archival record"
[R02]: https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/NUREGCR1677V2.xhtml "NUREG/CR-1677 Volume 2 NTIS record"
[R03]: https://digital.library.unt.edu/ark:/67531/metadc684063/ "NUREG/CR-6414 archival record"
[R04]: https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_vm/Hlp_V_ch5_1.html "ANSYS NRC Piping Benchmarks Overview"
[R05]: https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_vm/Hlp_V_vmnr02-1.html "ANSYS VM-NR1677-02-1"
[R06]: https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_vm/Hlp_V_vmnr03-1.html "ANSYS VM-NR6645-01-1"
[R07]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v3/v3.01.106/index.html "Code_Aster SSLL106"
[R08]: https://gitlab.com/codeaster/src/-/raw/main/astest/ssll106a.comm "Code_Aster SSLL106A command source; pin a commit"
[R09]: https://gitlab.com/codeaster/src/-/raw/main/astest/ssll106a.export "Code_Aster SSLL106A dependency declaration; pin a commit"
[R10]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v3/v3.01.101/index.html "Code_Aster SSLL101"
[R11]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v3/v3.01.101/Solution_de_r_f_rence.html "SSLL101 reference solution"
[R12]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v3/v3.05.102/index.html "Code_Aster SSLX102"
[R13]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v3/v3.05.102/Solution_de_r_f_rence.html "SSLX102 reference solution"
[R14]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v2/v2.05.002/index.html "Code_Aster SDLX02"
[R15]: https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf "NASA-STD-7009B official PDF"
[R16]: https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009 "NASA-HDBK-7009 official catalog entry"
[R17]: https://standards.nasa.gov/system/files/tmp/NASA-HDBK-7009B_Final%2002-03-2026.pdf "NASA-HDBK-7009B linked PDF"
[R18]: https://www.asme.org/codes-standards/find-codes-standards/standard-for-verification-and-validation-in-computational-solid-mechanics "ASME V&V 10 official product information"
[R19]: https://bentleysystems.service-now.com/community?id=kb_article_view&sysparm_article=KB0116379 "AutoPIPE Acceptance Test Set"
[R20]: https://documentation.metapiping.com/Quality/ "MetaPiping quality assurance"
[R21]: https://www.nafems.org/community/working-groups/education-and-training/nafems_benchmark_challenge/ "NAFEMS Benchmark Challenge"
[R22]: https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/ "Sandia SAND2000-1444"
[R23]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v2/v2.02.014/index.html "Code_Aster SDLL14"
[R24]: https://codeaster.gitlab.io/doc/docaster/manuals/man_v/v6/v6.02.503/index.html "Code_Aster SSNL503"
[R25]: https://codeaster.gitlab.io/doc/docaster/manuals/man_u/u2/u2.02.02/Exemples.html "Code_Aster pipe-element examples"
[R26]: https://www.nafems.org/publications/resource_center/r0081/ "NAFEMS R0081"
[R27]: https://docs.sstcae.com/tech_manual/anchor.htm "CAEPIPE anchor technical reference"
[R28]: https://www.sstcae.com/piping-news/caepipe-v1000-and-updated-verification-manual-are-released "CAEPIPE Verification Manual announcement"
[R29]: https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/cr6983 "NUREG/CR-6983 supplementary experimental lead"
[R30]: https://www.octave.com/products/engineering-analysis/aspect/pipe-stress "Aspect Pipe Stress, formerly CAESAR II"
[R31]: https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_vm/vm-nr1677-2-1a-btxt.html "ANSYS vm-nr1677-02-1a input listing"
[R32]: https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/ans_vm/vm-nr6645-1-1a-btxt.html "ANSYS vm-nr6645-01-1a input listing"

---

**Completion condition for this handoff:** the repository contains an executable, versioned qualification system with independent targets, traceable sources, failure-sensitive comparisons, capability-specific reports, and gates that prevent unsupported claims. Creating test files without executing and assessing them does not satisfy that condition.
