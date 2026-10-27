---
doc_id: OPS-RELEASE-NOTES-V0-1-0-DRAFT
doc_kind: engineering.release_notes_draft
status: draft
created: 2026-10-22
deliverable_id: DEL-10-04
refs:
  - rel: instance_of
    to: OPS-RELEASE-NOTES-TEMPLATE
  - rel: governed_by
    to: OPS-RELEASE-QUALITY-GATES
---

# SWBPIPE 0.1.0 Release Notes (Draft)

This is a draft prepared from `docs/RELEASE_NOTES_TEMPLATE.md` ahead of a
release candidate. It is not a release and authorizes none: release,
publication, risk acceptance and the public repository's name and location are
the owner's. Bracketed `[OWNER: …]` and `[CANDIDATE: …]` fields are filled when
the owner selects a candidate.

## Release Identity

| Field | Value |
|---|---|
| Product | SWBPIPE |
| Version | `0.1.0` (`apps/desktop/src-tauri/tauri.conf.json`) |
| Release label | `[OWNER: release label]` |
| Source revision | `[CANDIDATE: commit hash]` |
| Release date | `[OWNER: date]` |
| Release authority | `[OWNER: release acceptance record]` (DEC-027: sole maintainer and release authority) |
| Published at | `[OWNER: public repository name and location (DEC-057)]` |
| Artifact set | `SWBPIPE_0.1.0_aarch64-apple-darwin.app.zip` and `SWBPIPE_0.1.0_aarch64-apple-darwin.app.zip.sha256` |
| Artifact SHA-256 | `[CANDIDATE: digest from the .sha256 file]` |
| Release artifact record | `[CANDIDATE: validation/evidence/release_artifacts/RELEASE_ARTIFACT_<utc>_<commit12>.json]` |
| Evidence sweep | `[CANDIDATE: commit-bound sweep artifact named in the record]` |

## Summary

SWBPIPE is local, decision-support software for piping design and stress-model
authoring. It builds a 3D centerline model, solves its mechanics with an
in-repository engine, evaluates user-supplied rule packs, and assembles
auditable reports and export packages. Competent human review remains required
before any reliance. Version 0.1.0 is the first packaged build: one macOS Apple
Silicon application.

## Product scope as built

What the SWBPIPE 0.1.0 desktop application does in this source tree. It describes software behaviour only. SWBPIPE is decision-support software; competent human review remains required.

### Model authoring

- Projects: New Local Project, New Blank Project, Open, Save and List Local Projects, and Open Model Document… for a model JSON file (model schema 0.7.0; other versions are refused by name). An invented demo model is bundled.
- 3D centerline viewport: place nodes by coordinates, connect pipes between explicit endpoints (automatic node creation while routing is not provided), box and filtered selection, labels, load arrows, grid and view cube.
- Model tree with a table view for browsing and inline editing, and a property inspector for the selected entity.
- Every edit is a model operation: validated by the operation engine, shown as a diff, applied explicitly and recorded in an operation ledger. Undo and redo cover up to 25 edits.
- Geometry tools: split a pipe at a new node; reconnect one end of a pipe to another existing node; copy, rotate and mirror selected pipes.
  - Reconnect refuses a pipe that a component names (bend span, tee leg, rigid component, expansion joint or connector span), a pipe with a component other than a terminal marker at either of its ends or at the node it joins, a pipe in a pressure region, and a move onto a pressure region's internal node. The refusal names the blocking component or region; re-author it around the reconnect.
  - Deleting a pipe is refused while any record still names it; the refusal lists each dependent.
- Materials with explicit elastic, shear and thermal properties, temperature tables and expansion-law definitions. Shared sections can be assigned to pipes or detached.
- Components: bend, tee, reducer, valve, flange and expansion joint, with geometry and provenance. A bend can be inserted at a corner with exact tangent points and realized as a curved element carrying the user's flexibility factor and optional directional SIF pair. No factor is suggested or defaulted.
- Expansion joints are authored as objective connectors (6×6 stiffness, frame, offsets, optional explicit tie rods).
- Supports: anchor, guide, line stop, vertical support, spring, variable spring hanger, constant-effort and nonlinear supports, each with explicit DOFs and provenance. Equipment and nozzle boundaries take an explicit rigid, free or spring choice per DOF.
- Load cases: concentrated force and moment, distributed force, thermal temperature change and imposed support displacement; wind fields with whole or partial exposed spans; seismic static-g fields; self-weight generated from pipe metal, contents and insulation mass under an explicit gravity.
- Pressure authoring: per-case pressure regions, E/ν materials, section corrosion allowance and a shear model (Timoshenko by default, Euler–Bernoulli selectable). Load/reference states carry installation and case temperatures, fit strain and prescribed support motion.
- Combinations: factored linear ("mechanics"), result-state subtraction and range envelope.
- User-imported material, section, component and hanger libraries pass a provenance check and are stored locally. Imported hanger records can be selected onto supports.
- Offline agent proposals: import a proposal file, validate it, preview the diff and apply it explicitly. No live provider is connected.
- Project units are chosen when a blank project is created (SI, US customary or a custom unit per key) and can be changed later on the Project page; the length unit is fixed once nodes exist, and no stored value is converted. New entries take their default units from the project units. A model document, stored project or saved state without project units is refused by name at open.
- Readouts in Entered, SI or US units; editing stays in entered units. Missing or incompatible units are diagnostics, not defaults.
- Missing-data and project-validation panels separate solve-blocking from rule-check-blocking findings.

### Analysis

- Linear-static, small-displacement 3D frame analysis with six DOFs per node. The solve runs natively in a capped local worker process with progress, cancellation and a memory pool.
- Two solver modes: Sparse interactive (default; in-repository skyline LDLᵀ factorization) and Dense scrutiny.
- The model's declared pressure contract selects one of two routes:
  - Pressure-free route: Euler–Bernoulli straight pipes; realized curved bends; anchors, guides, line stops, vertical supports and linear springs; variable spring hangers as linear springs from the entered stiffness; constant-effort supports as a constant force when one translational DOF and a constant load are entered; nonlinear one-way, gap, lift-off and friction supports, iterated to a converged active set. Loads: weight and distributed force, concentrated force and moment, element temperature change, wind and seismic static-equivalent loads generated from user inputs, and an imposed displacement or rotation on a rigid support DOF. Pressure is refused on this route, and so is an imposed support displacement in a model with nonlinear supports.
  - Exact pressure route (`3.0.0/exact_pressure_v3`): straight circular pipes (Euler–Bernoulli or Timoshenko), realized curved bends, objective-connector expansion joints with optional tie rods, linear restraints and springs, and valves, flanges, rigid and specialty components (reducers only outside pressure regions). Loads: internal pressure as a signed differential per explicit region, force, moment and line loads, and load/reference states for thermal and fit strain and prescribed support motion. Tees, reducers in a pressure region, nonlinear and constant-effort supports, combinations, wind or seismic generation and the support-targeted imposed-displacement load are refused by name.
- Material moduli come from the entered base material properties. A load case may instead select a named temperature point, or linear interpolation between two entered points; there is no extrapolation.
- Valves, flanges, reducers, tees and rigid or specialty components carry user data, and user SIFs feed review rows. A valve, flange, reducer, rigid or specialty component's mapped member takes the user's stiffness scale (DEC-045) on both routes, and its stress rows are those of the mapped reference section, not a body stress. When self-weight is generated, a component with an entered weight and centre of gravity contributes a nodal force and moment at its node in place of the member's distributed pipe weight. Reducer eccentricity is not modelled. A tee's span is analysed as pipe; no branch flexibility is assembled.
- Documents with legacy pressure primitives or legacy four-rate expansion joints are refused by name and must be re-authored. Nothing is converted.
- Missing, invalid or unsupported inputs that the solve needs block it with named diagnostics; nothing is defaulted. Some records the solve does not consume (for example a constant-effort support it cannot apply) contribute nothing and are reported with a warning, while the solve proceeds.

### Results and stress recovery

- Nodal displacements and rotations; element-local axial force, shears, torsion and bending moments at member ends and stations; signed support reactions.
- Mechanics stresses: axial, bending and torsional shear components, and a per-member maximum elastic normal stress |N/A| + hypot(My, Mz)/Z. The exact route adds pressure hoop (Lamé) and longitudinal stresses, each on the nominal and the reduced section.
- Where the user supplied a SIF, an intensified bending measure labelled as not a code stress.
- Combinations are evaluated on the pressure-free route. Factored-linear ("mechanics") combinations are withheld where superposition is not a solved state: nonlinear supports, constant effort with a factor sum other than 1, or mixed moduli. Result-state subtraction and range envelopes operate on the solved results and are not gated this way.
- Results table, deformed shape and rotation glyphs in the viewport, with optional member colouring by a result quantity and support reaction arrows. Each result shows its numerical-integrity standing and diagnostics.
- A numerical health indicator for each load case, from the solver's existing residual and conditioning checks: checks passed, sensitive, quality unresolved, solve failed or not assessed. Each state comes with an estimated conditioning figure where available, the cause where the solver names one, and a link to the solver diagnostic. These checks look for numerical trouble; they do not measure the error.

### User rule packs

- Rule-pack manager: create, open, save, delete, validate and checksum packs in the local store.
- Expressions are built in a structured composer for the typed-AST grammar (DEC-022), including table interpolation and lookup. There is no writable text syntax (DEC-037).
- Run Rule Checks binds solver result rows, library values and entered values. Each check reports RULE_INPUTS_INCOMPLETE, USER_RULE_CHECKED or USER_RULE_FAILED with a worst-of aggregate; missing inputs block pass/fail.
- A bundled invented demonstration pack carries no code data.

### Reports and exports

- Rendered HTML calculation report from the Rust renderer, with its canonical SHA-256 and a derived Print/PDF view, for pressure-free results and for eligible exact-route (`pressure-2` and `pressure-source-1`) results. A report is rendered only as a local private document, when the user states local-private intent; a public render is refused for every session, because session data is classified private. An exact-route report carries no numerical-health lines.
- The report carries rule-pack references, user-rule check outcomes, software and solver versions, run settings, coordinate systems, and provenance records for materials, sections, components, supports and library references. A record whose review status is quarantined or rejected, or whose redistribution status is suspected protected, blocks the report.
- Report record JSON and report-lint JSON, for pressure-free results.
- Save Report Package… (`.opsproj`) saves a local private package for a current pressure-free or eligible exact-route result.
- Result JSON and stress-neutral JSON exports, offered when the result's standing admits them. For exact-route results these, rule checks, the rendered report and the report package are the open outputs.
- For pressure-free results also: native JSON package, handoff package JSON, conservative PCF (straight-pipe records; supports and components go to a loss report), a `.mbf` model batch file package (nodes, elements, supports and load cases; components omitted; target version and record subset `TBD`) and a local FEA handoff JSON packet. PCF and `.mbf` lengths convert exactly from m, mm, in and ft; other units, and a missing project unit, are refused by name.
- Outputs that must be byte-exact for a downstream tool (stress-neutral CSV, glTF review geometry, PCF text and `.mbf` text) are built but not offered for download while session values are classified private. The `.mbf` text is a placeholder record subset that its target tool does not import.
- `openpipestress-runner` command-line runner, built from source and not bundled in the app: `solve`, `validate-input`, `export-results`, `run-benchmark`, `run-regression` and `read`; JSON in and out; exit codes 0, 1 and 2; `--solver-mode`. The desktop exports a matching runner envelope JSON.

### Privacy and local operation

- The project store is a local SQLite file in the app's Application Support folder; saved rule packs and libraries are kept there too.
- No telemetry is sent: telemetry attempts are dropped before any payload is built, and the app has no network upload path.
- Export downloads pass a redaction control for their context (public report, downstream tool, local private). Private values are redacted or blocked unless the user states explicit local-private intent.
- Library imports suspected of carrying protected content are quarantined and not stored.

### Platform and packaging

- macOS on Apple silicon (`aarch64-apple-darwin`) only: Tauri `.app` bundle `SWBPIPE`, version 0.1.0, identifier `com.chirality.swbpipe`.
- Distributed as a zip with a SHA-256 checksum file. The app is signed with the developer's Developer ID certificate (hardened runtime) and notarized by Apple with the ticket stapled (D-06b, owner, 2026-10-23); see the install note.

### States, runs, comparison and model export

Owner ruling, 2026-10-23 ("I approve OD-1 through OD-5 as you recommended."; `docs/COMPLETENESS_MAP.md` §4.2) places these in v0.1:

- Named immutable model states: save, open, label and delete, kept in the local store (OD-1).
- Analysis runs recorded against a saved state, with the model's rule-pack references resolved at solve, and a History panel to browse them (OD-1).
- Comparison of two saved states, of two recorded runs, and of load cases and combinations within one run; view-only, with automatic mapping and no unit conversion or tolerance classification (OD-1).
- File › Save Model Document… writes the canonical model document, independent of a solve; File › Save Handoff… writes a verified handoff directory package with its manifest for a saved state. Runs are not referenced in the handoff package (OD-1, OD-4).

An entity-mapping editor, tolerance profiles, graphical comparison overlays and comparison export are not provided; the states-and-comparison design places them in v0.2 R3. History export is not provided.

### Not in v0.1

- Design-knowledge authoring, constraint checks (clearance, no-go volumes, slope) and candidate generation; deferred to v0.2 by the same ruling (OD-1, OD-3). The Design Knowledge panel shows a bundled document.
- Further agent-proposal work (PKG-16) and further export formats (PKG-17); deferred to v0.2 (OD-1). The offline proposal intake and the export panels described above are unchanged.
- Principal, von Mises and Tresca stresses.
- Reducer eccentricity.
- Hydrotest cases; rotational gap and friction supports; rigid strut and sliding-support families; hanger preload from installed, cold or hot loads.
- Flow momentum, Bourdon effect, ovalization and external-pressure collapse.
- Verified result bounds (retained precision) on any product surface.
- A shareable (not local private) report; final report layout and PDF policy (`TBD`).
- A live agent provider; public API transport, plugin loading and the local FEA package format (`TBD`).
- Windows, Linux and Intel Mac builds.

## Platform, Packaging And Installation

- **Platform:** macOS on Apple silicon (`aarch64-apple-darwin`) only (DEC-057).
  No Intel, Windows or Linux build.
- **Package:** the Tauri `.app` bundle in a deterministic zip, with a SHA-256
  checksum file in `shasum` format beside it.
- **Install:** see the user guide, `docs/user_guide/index.md` §3.1: verify the
  checksum, unzip, then open the app.
- **Project data:** kept in a local SQLite project store under
  `~/Library/Application Support/com.chirality.swbpipe/` (user guide §3.2).

### Install note

> This build is signed with a Developer ID Application certificate and
> notarized by Apple, with the notarization ticket stapled (D-06b owner
> decision of 2026-10-23). Before opening it, verify the artifact's SHA-256
> checksum against the published .sha256 file; the release artifact record
> binds that digest to the source commit and its commit-bound DEC-025
> evidence-sweep artifact. macOS Gatekeeper then opens it as an identified,
> notarized app.

(Verbatim from `docs/BUILD_AND_RELEASE.md` §8.2, as the packaging record
carries it.)

## Validation Evidence

`[CANDIDATE: the release-candidate evidence for the selected commit: the
evidence sweep, release gate records and packaged-app smoke, with their
results. Prepared with the release-candidate rehearsal; not restated here.]`

## Known Limitations And Open Risks

`[CANDIDATE: open-risks list from the release-candidate rehearsal, inserted
here as produced.]`

Risk acceptance is the owner's: `[OWNER: disposition of each listed risk]`.
This draft does not accept, waive or rank any risk.

## Data, IP And Privacy Boundary

- The product runs locally. It has no cloud, network or telemetry features,
  and it does not write private data to repository paths by default.
- Bundled examples and fixtures are invented. The release carries no protected
  standards text or tables, proprietary commercial data, private project data,
  private rule packs or private libraries.
- Code-specific rules, allowables, stress intensification and flexibility
  factors are user-supplied through private rule packs and library data.

## Professional Boundary Notice

SWBPIPE is decision-support software. It may compute mechanics, evaluate
user-supplied rule packs, record diagnostics, and assemble auditable reports.
Competent human review remains required.

Standard claim fence applies (claims taxonomy per DEC-081).

## Reproducibility Manifest

| Field | Value |
|---|---|
| Git revision | `[CANDIDATE: commit hash]` |
| Working tree state | `[CANDIDATE: clean, per the release artifact record]` |
| Build command | `python3 tools/release/build_signed_app.py --execute`, then `python3 tools/release/notarize_app.py --execute --keychain-profile swbpipe-notary`, then `python3 tools/release/package_release_artifact.py --execute --sweep-artifact <sweep>` |
| Runtime versions | `[CANDIDATE: from the release artifact record]` |
| Artifact checksum | `[CANDIDATE: SHA-256]` |

## Upgrade And Compatibility Notes

- First packaged release; nothing to migrate from a published version.
- A project store left by an earlier preview build under the former identifier
  `org.openpipestress.technical-preview` is copied forward once on first launch
  (DEC-101 persistence compatibility). An existing store is never overwritten.

## Human Review Record

| Review item | Disposition |
|---|---|
| Release authority | `[OWNER]` |
| Data-boundary review (D-20 scan) | `[OWNER]` |
| Professional-boundary review | `[OWNER]` |
| Known-risk acceptance | `[OWNER]` |
