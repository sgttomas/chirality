# CAEPIPE correlation pilot

This Design governs the first external-prover correlation loop (PRD §22.5): SWBPIPE
models are written as CAEPIPE input, solved by the owner's CAEPIPE installation, and
CAEPIPE's results are kept as private reference data and compared with SWBPIPE and an
independent hand calculation. It records how DEL-17-05's open placeholders and its
invocation `TBD` are settled for the pilot, and what stays open.

## 1. Activation and purpose

PRD §22.5 makes activation "owner-gated on lawful access to the external tool". The
owner activated it on 2026-10-26:

- Request: "Could we start making validation cases using a CAEPIPE solver in my
  Parallels Windows virtual desktop and have validation cases made as input files that
  can be given to CAEPIPE and solved and then take the outputs as the validation data
  for SWBPIPE to later use?"
- Rulings on Agent 0's questions: "1. Start that 5th lane now 2. Yes the license I just
  read allows such use and I take full responsibility. 3. Automate as much as possible,
  even the first time if that could be done right. 4. Make the shared folder in a place
  you recommend so that it's going to work well for our needs." And: "I have just
  installed an evaluation version of CAEPIPE and it is currently running through
  Parallels."
- Purpose of the pilot: "The pilot using the trial version of CAEPIPE is just to prove
  the basic concept for how I want to do validation will work. Once that's assured, I
  will pay for the full license allowing us to do more extensive validation work."

The pilot is a proof of concept supporting that licence decision. It exercises each
part of the loop once on a small case set; breadth of coverage and governed
tolerances wait for the full licence. CAEPIPE results are a reference, not ground
truth: the hand-calculation witnesses remain the primary verification anchor, and
neither CAEPIPE agreement nor a completed run is professional acceptance, validation
of engineering use, or compatibility proof (DEL-17-05-REQ-008, F-PIP-3).

## 2. Target tool and environment

| Item | Pilot value |
|---|---|
| Target | CAEPIPE 15.10, evaluation ("Trial") build, owner-licensed, MBF `VERSION 15.10` |
| Environment | The owner's Windows virtual machine under Parallels on the development Mac; commands run as the logged-in Windows user (`prlctl exec <vm> --current-user`) |
| Trial window | 30 days from first launch (2026-10-26), per the vendor release notes; the private case manifests record the date |
| Evaluation limits observed | Import refuses a model of more than 20 layout rows; printouts carry the evaluation product name and version (DEL-17-01 CQ-17-01-009) |

The evaluation limit shapes the pilot corpus: every case stays within 20 layout rows.
A licensed build is expected to lift it; the writer reports the row count and warns
above 20, but does not refuse.

## 3. Invocation profile (settles DEL-17-05-REQ-003 for the pilot)

The project selects the documented batch pattern (`CAEPIPE-BATCH`, archived copy in
DEL-17-01 `Source_Basis_Register.md`):

```text
<CAEPIPE executable> "<model>.mbf";batchmode=yes
```

It imports the MBF, writes `<model>.mod` and `<model>.res`, and is documented to write
`<model>.csv` beside the MBF. The harness always runs this route first and uses its CSV
whenever one appears.

**Trial-build workaround (labelled, not hardened).** In the 15.10 evaluation build the
batch run stops at a modal "Access violation" dialog after writing `.res` and never
writes the CSV, on every model tried, including the manual's own example
(DEL-17-01 CQ-17-01-008). Until a build fixes that, the guest script stops the process
it started, opens the solved `.res` in a fresh CAEPIPE instance it starts itself, and
prints the results to CSV through the documented Print > To File command
(`CAEPIPE-PRINT-TO-FILE`), finding menu items and buttons by their visible captions. It
reads no binary result file and stops only processes it started. The run record states
which route produced the CSV (`csv_from_batch` or `csv_from_gui_print`). This fallback
exists only for the trial build and gets no further investment; the full licence
should be checked for batch CSV output first.

## 4. Configuration surface (DEL-17-05-PH-001)

The harness is disabled unless the user configures it (REQ-001, REQ-016):

- `SWBPIPE_CAEPIPE_EXCHANGE` names the private exchange folder;
- that folder holds `harness_config.json` with the virtual machine name, the guest path
  of the user's CAEPIPE executable, the guest path of the shared exchange folder, a
  guest-local work folder, and `license_and_environment_responsibility_acknowledged:
  true`.

Without both, every live step skips with a stated reason, and public CI never has
either. The harness refuses an exchange folder that lies inside a Git work tree or
lacks a `.gitignore` of `*`. Because the guest paths enter guest shell commands, each
must be an absolute Windows path (`X:\…`) of letters, digits, space and `\ . - _ ( )`
only, without `.` or `..` segments; any other value skips the harness naming the
field. No executable is discovered, bundled or installed.

## 5. Exchange folder and run directory (DEL-17-05-PH-002)

The exchange folder is outside every repository, mode 700, with a `.gitignore` of `*`.
The owner's VM sees it as a shared folder. Per case:

```text
cases/<case_id>/
  case_manifest.json         case id, model and MBF hashes, tool and version, trial first-launch date, route used, per-layer privacy
  swbpipe/                   solve request and SWBPIPE result envelope
  caepipe_in/                model.mbf, id_map.json, mbf_render.json (diagnostics, loss report, mapping assumptions)
  caepipe_out/               CSV, guest run log, .mod/.res as CAEPIPE wrote them        PRIVATE
  parsed/                    normalized CAEPIPE results                                  PRIVATE
  comparison/                three-way comparison record                                 PRIVATE
```

`caepipe_in/` holds only SWBPIPE-derived content. Every layer from `caepipe_out/` on
is CAEPIPE output or derived from it and stays private (§8). Every directory and
file the pilot creates, writes or deletes must lie inside the resolved exchange
folder with no symbolic link on the way; otherwise the case stops as
`containment_violation`. Live runs solve on a guest-local copy of the case folder
and copy the outputs back. A failed preparation step (the guest copy of the MBF)
stops the run as `prepare_failed` before solving. The guest script reports the
SHA-256 of the MBF it solved; the run record holds it beside the host MBF's hash, and
when they differ the run is `input_hash_mismatch` and nothing is collected. A CSV is
compared only when its run record binds it to the current MBF (both hashes equal);
an offline re-run reports `stale` when the solved MBF differs from the current one
and `unbound_output` when no valid run record binds the CSV. Each guest step is
idempotent and is retried when the `prlctl` client itself fails (exit 255 with a
`PrlJob_` message), which happens intermittently on this host.

## 6. Writer, parser and comparison

- **MBF writer (DEL-17-04).** `core/handoff/caepipe_mbf/si_writer.py` writes SI MBF
  (`OPTIONS SI`, lengths in mm, E in N/mm², weight density in kgf/m³) from the headless
  runner's preview model. A project or quantity in another unit system is refused by
  name, not converted. Unsupported constructs are refused by name and listed in the
  loss report. Rotational partial restraints are refused: the 15.10 build rejects
  `FIXR` at import ("FIXR is not available"); translational `FIXD` is accepted. A
  curved bend is written at its tangent intersection (`KI`, radius `B`, the user
  flexibility factor as `FF`); CAEPIPE reports its near and far tangent points as
  nodes `<n>A` and `<n>B`, which the writer's node map uses for SWBPIPE's
  tangent-point nodes. A bend without a user flexibility factor is refused. SWBPIPE's
  curved bend includes arc bending and axial flexibility but no transverse shear.
  Weight per length maps to a weight density using standard gravity
  (9.80665 m/s²); CAEPIPE applies its own gravitational constant, a documented
  difference. Poisson's ratio is taken as given or derived as E/(2G) − 1.
- **Parser (PH-003).** `core/handoff/caepipe_external/print_csv.py` reads the
  Print > To File CSV. Its coverage register lists each recognized section (global
  displacements, anchor loads in global and local axes, restraint loads, element
  forces in local and global axes), checks each section's header and unit rows, treats
  a blank numeric cell as zero, skips Min/Max blocks and unknown sections with a
  diagnostic, and pairs element-force rows in from/to order (a weak, row-order
  correlation per REQ-010, bound back to SWBPIPE ids through the writer's id map). Its
  public test fixture is invented and labelled.
- **Comparison record.** Each case produces one record naming what PRD §22.5 lists:
  internal model hash, exported MBF hash, target tool and version, import/export
  assumptions, manual changes (none), load-case mapping, support mapping, comparison
  basis, tolerance basis and discrepancy disposition. Each compared quantity carries
  three values (analytic, SWBPIPE, CAEPIPE) and three pairwise checks.
  - Outcome: `matched_within_tolerance`, `delta_exceeds_tolerance`,
    `row_unmatched_internal_only`, `row_unmatched_external_only`, `tolerance_tbd`.
  - Cause hypothesis for a non-matching outcome (an `ASSUMPTION` until evidenced):
    `solver_defect_candidate`, `export_mapping_issue`, `parser_mapping_issue`,
    `unit_or_axis_mismatch`, `support_semantics_mismatch`, `load_case_mismatch`,
    `missing_model_parameter`, `documented_behavior_difference`,
    `caepipe_profile_unknown`. It is derived from which pairs disagree: if the analytic
    and SWBPIPE values agree and CAEPIPE differs, the CAEPIPE side (export mapping,
    profile or a documented behaviour difference the case declares) is suspected; if
    SWBPIPE alone differs, `solver_defect_candidate`; if the analytic value alone
    differs, the case inputs are suspected; if all three disagree,
    `solver_defect_candidate` with the alternatives listed. A declared
    behaviour difference counts as `documented_behavior_difference` only when the
    analytic and SWBPIPE values agree and the observed CAEPIPE − SWBPIPE difference
    is within 10 % of the case's predicted difference (or the case gives no
    prediction, recorded as `declared_only`). When the analytic check fails or has
    no verdict, the triangle rule names the cause and a fitting declaration is kept
    only as further evidence. No axis is silently defaulted.
  - Disposition: `no_action`, `assumption_recorded`, `bug_report`,
    `dossier_question`, `proposed_code_fix`, `requires_professional_review`.

Sign and unit mappings applied before comparison: CAEPIPE reports anchor loads as the
load of the pipe on the anchor, SWBPIPE reports the reaction on the pipe (sign flip);
CAEPIPE rotations are in degrees, SWBPIPE's in radians; CAEPIPE forces in a
mechanical case also appear in its Empty Weight case, so the pilot compares the
`Sustained (W+P)` case with empty pipes and zero pressure.

## 7. Cases and tolerances

The public case definitions live in `validation/caepipe_correlation/cases/`: invented
inputs, the SWBPIPE model, the hand-calculation formulas and values, the quantities
compared, and per-case tolerances labelled `ASSUMPTION`. The governed external-oracle
tolerance class stays `TBD` until the owner rules values; tolerances are never
loosened, nor SWBPIPE tuned, to match CAEPIPE. The pilot cases cover, once each, a
force load, thermal expansion, self-weight, a bend, a branch and an imposed
displacement on a support, plus one case with a deliberately injected input fault to
show that a real difference is caught and classified.

A difference indicating a wrong SWBPIPE output goes to Agent 0 with its evidence and
is not fixed in this deliverable.

## 8. Data boundary

CAEPIPE's outputs and everything derived from them (parsed values, differences,
agreement counts, tolerances measured from them) stay in the exchange folder and are
never committed, pushed, or written into PR, issue or other GitHub text. Public
material is limited to invented models, SWBPIPE-generated MBF, code, this Design, and
invented parser fixtures. Vendor files in the CAEPIPE install folder are read locally
only and never copied. No public text claims agreement with CAEPIPE. The pilot
command's standard output carries operational status only (case, route, the record's
path in the exchange folder or the reason none was written); outcome and cause counts
stay in the private record. A guard test checks that no tracked file sits under an
exchange-style path, carries the CAEPIPE CSV header of a real run, or is a parsed,
comparison or run-record artefact (by document kind or private-layer file name)
unless a provenance sidecar declares it invented, and that the harness refuses an
exchange folder inside a Git work tree.

## 9. Regression check

`tests/test_caepipe_private_correlation.py` reads the private corpus through
`SWBPIPE_CAEPIPE_EXCHANGE`. When it is unset or empty the test skips with that reason;
otherwise it re-parses each stored CAEPIPE CSV, re-solves the case in SWBPIPE and
re-runs the comparison, failing if any quantity's outcome moves out of its recorded
classification. It never prints CAEPIPE values outside the local run.

## 10. Remaining items

- Batch-route CSV on a licensed build; retire the GUI-print fallback once batch output
  works (CQ-17-01-008).
- A governed tolerance class for external-oracle comparisons (owner ruling).
- Writer breadth: springs, guides, hangers, nonlinear supports, pressure, rigid and
  valve components, temperature-dependent materials, imperial-unit projects
  (conversion), multiple thermal cases.
- The desktop `.mbf` export (`CaepipeMbfExportPanel.tsx`) still writes the placeholder
  smoke text; it should use the SI writer's record subset.
- Wider correlation corpus once the full licence lifts the 20-row limit.
- Non-unit bend flexibility factors are untested: the bend case uses k = 1.
