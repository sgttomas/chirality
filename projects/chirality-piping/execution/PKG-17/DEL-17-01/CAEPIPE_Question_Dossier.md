# CAEPIPE Developer-Team Question Dossier: DEL-17-01

## Purpose

This dossier records clarification questions for the CAEPIPE developer/support team or equivalent public support channels. It is designed to close target-behavior gaps without asking for proprietary internals, protected standards data, commercial examples, or license-bypass guidance.

## Question Register

All open questions are TBD/gated items. Until answered by a public-citable source, an explicit project profile decision, or private support response with a recorded public-use boundary, downstream deliverables must carry the relevant TBD forward and avoid proprietary-format or target-coverage inference.

| Question ID | Linked TBD | Question | Current Public Basis and Location | Affected Deliverables | Gating Impact | Status |
|---|---|---|---|---|---|---|
| CQ-17-01-001 | TBD-17-01-001 | Which CAEPIPE version should OpenPipeStress target first for a documented MBF export/import smoke profile? | CAEPIPE public MBF export page documents latest-version MBF plus a 6.xx option (`EXPORT MBF`); batch page notes a path-length change starting Version 15.00 (`RUNNING CAEPIPE/CAEPIPE 3D+ IN BATCH MODE`, `Note`). | DEL-17-04, DEL-17-05 | Blocks version-specific support claims. | TBD |
| CQ-17-01-002 | TBD-17-01-002 | Which MBF record families are recommended for a minimal straight-pipe/support/load-case smoke model? | CAEPIPE public import page lists MBF section keywords and section descriptions (`IMPORT MBF`, `Format of .MBF`), but the first OpenPipeStress subset is not selected. | DEL-17-04 | Blocks first writer subset acceptance and any claim of broad MBF coverage. | TBD |
| CQ-17-01-003 | TBD-17-01-003 | Are comments or user fields in MBF appropriate for preserving stable external IDs, or should stable IDs be sidecar-only? | PKG-17 requires stable ID maps; admitted public MBF pages do not yet provide a confirmed stable external-ID carrier for OpenPipeStress identity mapping. | DEL-17-02, DEL-17-04 | Blocks ID-map placement claims. | TBD |
| CQ-17-01-004 | TBD-17-01-004 | Which command-line invocation pattern is recommended for a user-owned, licensed local executable smoke run? | CAEPIPE public pages describe command-line/import behavior (`IMPORT MBF`, `Command line operation`) and batch arguments (`RUNNING CAEPIPE/CAEPIPE 3D+ IN BATCH MODE`, `Run the Analysis and Output Results in CSV Format`, `Note`). | DEL-17-05 | Blocks harness profile wording beyond user-owned local execution. | TBD |
| CQ-17-01-005 | TBD-17-01-004 | Which CSV output sections are stable enough for automated regression parsing in a first harness? | CAEPIPE public export-data page lists CSV/TEXT and time-history CSV export surfaces (`Export data from CAEPIPE`), and batch documentation describes CSV output from MBF execution; stable parser subset is not selected. | DEL-17-05, DEL-17-06 | Blocks parser coverage claims. | TBD |
| CQ-17-01-006 | TBD-17-01-005 | Which PCF translation defaults should OpenPipeStress warn about or avoid in a conservative PCF subset? | CAEPIPE PCF translator PDF documents translator defaults, external mapping database dependencies, support/material mapping behavior, and component mappings (`Reference`; `PCF to CAEPIPE component Mapping`). | DEL-17-07 | Blocks PCF subset acceptance and warning-policy claims. | TBD |
| CQ-17-01-007 | TBD-17-01-001 | Are there public documentation pages preferred for citation in open-source handoff documentation? | Current admitted URLs are public and official; preferred citation targets may vary by CAEPIPE version/profile. Since at least 2026-10-26 the `www.sstusa.com` manual URLs redirect to the `www.sstcae.com` root and the same paths there return 404; archived copies are the working basis (`Source_Basis_Register.md`, `Archived copies`). Where are the manual pages published now? | Relevant downstream PKG-17 exporters and harnesses | Blocks documentation citation hardening only. | TBD |
| CQ-17-01-008 | TBD-17-01-004 | In CAEPIPE 15.10 (evaluation "Trial" build), running `CaepipeD.exe "<model>.mbf";batchmode=yes` (and the plain `CaepipeD.exe <model>.mbf` form) imports the model, writes `<model>.mod` and `<model>.res`, then stops at a modal "Caepipe: Error / Access violation" dialog and writes no `<model>.csv`. Is batch-mode CSV output supported in the evaluation build, and is this a known defect with a fix or workaround? | Public basis: `CAEPIPE-BATCH` and `CAEPIPE-IMPORT-MBF` (`Command line operation`) state that the run produces `<model>.csv` beside the MBF. Project observation 2026-10-26 on the owner's licensed evaluation install, recorded in DEL-17-05 `Design/caepipe-correlation-pilot.md` §3: the same dialog on every model tried, including the public manual's own example. The correlation pilot works around it by printing the solved results to CSV through the documented Print > To File command (`CAEPIPE-PRINT-TO-FILE`). | DEL-17-05 | The pilot depends on a labelled UI-automation workaround until batch CSV output works; the harness prefers batch output whenever it appears. | TBD |
| CQ-17-01-009 | TBD-17-01-001 | Which limits apply to the CAEPIPE evaluation build: model size, run period, printed stamps, and output types? | No public basis found. Observed on the owner's install 2026-10-26: import refuses a model with more than 20 layout rows ("Evaluation version cannot import model with more than 20 rows"); the release notes state evaluation use lasts 30 days from first launch and that printouts carry the product name and version. | DEL-17-05, DEL-09 correlation corpus | Shapes the pilot corpus (cases of 20 layout rows or fewer) and its schedule; licensed builds may differ. | TBD |

## Question Boundary

Questions must not ask for:

- proprietary solver algorithms;
- protected standards content;
- commercial example files;
- copied report templates;
- hidden binary format behavior;
- license-bypass procedures;
- code-compliance calculations or professional acceptance criteria.

If an answer is private/support-only, record that boundary and do not copy private text, examples, proprietary mappings, protected standards content, or commercial fixtures into the public repository.

## Closure Rule

When a question is answered, record:

- answer source and date;
- whether the answer is public-citable or private/support-only;
- affected TBD IDs;
- affected downstream deliverables;
- any boundary that prevents public repository use.

Do not close a linked TBD merely because a question was asked. Closure requires a recorded answer source, its public/private status, and a downstream decision on whether the answer is admissible for public artifacts.
