# Specification — DEL-043-01 Scope of Work

## Scope

This specification establishes the normative content of the EPC Integrator Scope of Work (SOW) for PKG-043 "Instrumentation (outside of Mechanical Packages only)" (Workbook row 45; CoA tracking 26020-01-32-002; WBS 01; Discipline = Instrumentation).

**In scope (per PACKAGE_REGISTER.csv row PKG-043):**

- Instrumentation that is **not** carried within a Mechanical vendor package.
- Physical interfaces of types: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network.
- Inclusion criterion: equipment/work assigned to Workbook row 45, Discipline Instrumentation, WBS 01.

**Out of scope:**

- Instrumentation that is integral to a Mechanical vendor package and ships within that package (excluded by package name itself).
- Per PACKAGE_REGISTER.csv: "no package-specific exclusions stated in source materials" beyond the package-name exclusion. Other exclusions are TBD.

**Covers scope items:** `SOW-0044` (DELIVERABLE_REGISTER.csv).

## Requirements

| ID | Requirement | Authority | Source |
|---|---|---|---|
| REQ-043-01-01 | The SOW shall identify the EPC Integrator (or assigned discipline subcontractor) as responsible for delivery of the instrumentation scope outside of Mechanical packages. | NORMATIVE | _CONTEXT.md; PACKAGE_REGISTER.csv ResponsibilityModel |
| REQ-043-01-02 | The SOW shall enumerate tagged equipment and the package identity list for PKG-043. | NORMATIVE | _CONTEXT.md Anticipated Artifacts |
| REQ-043-01-03 | The SOW shall provide a package function and integration narrative describing how PKG-043 integrates with the whole facility. | NORMATIVE | _CONTEXT.md Anticipated Artifacts; DELIVERABLE_REGISTER.csv ("whole-facility integration narrative") |
| REQ-043-01-04 | The SOW shall provide a responsibility assignment record covering the package scope. | NORMATIVE | _CONTEXT.md Anticipated Artifacts |
| REQ-043-01-05 | The SOW shall declare the package boundary as "Instrumentation outside of Mechanical packages only" and shall not include instrumentation owned by Mechanical vendor packages. | NORMATIVE | PACKAGE_REGISTER.csv row PKG-043 (Name; ResponsibilityModel) |
| REQ-043-01-06 | The SOW shall record the interface types in effect for the package: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | NORMATIVE | PACKAGE_REGISTER.csv row PKG-043 InterfaceTypes |
| REQ-043-01-07 | The SOW shall identify the source basis as Workbook Packages row 45 (CoA 26020-01-32-002) and the Gate 7 PROJECT_DECOMP snapshot. | NORMATIVE | _CONTEXT.md Source Reference; _REFERENCES.md |
| REQ-043-01-08 | The SOW shall cite the project Electrical & Instrumentation specification set, including ELC-QAS-000014-001 "Instrumentation General", as governing for instrumentation design. (ASSUMPTION: applicable to PKG-043; confirm during detailed engineering.) | NORMATIVE | DBM-Deepcut/4-25_Deepcut_DBM.md L2870, L2887 |
| REQ-043-01-09 | The SOW shall declare relationship to the consolidated 04-25 Instrument Air package and any shared 03-25/04-25 instrumentation context (see Conflict Table in Guidance). | NORMATIVE | DBM-Deepcut/4-25_Deepcut_DBM.md L1822, L1906-1925 |
| REQ-043-01-10 | The SOW shall identify the responsible party for installation of shipped-loose instruments, valves, and components within the PKG-043 boundary. (Field-construction allocation per DBM L115 is an ASSUMPTION until confirmed for this package.) | NORMATIVE | DBM-Deepcut/4-25_Deepcut_DBM.md L115 |

## Standards

| Standard / Specification | Applicability | Location |
|---|---|---|
| ELC-QAS-000014-001 — Instrumentation General | Project instrumentation specification (governing) | DBM-Deepcut/4-25_Deepcut_DBM.md L2887 |
| Project Electrical and Instrumentation specifications (full set) | Govern electrical distribution and equipment procurement; full list location TBD | DBM-Deepcut/4-25_Deepcut_DBM.md L2870 |
| Workbook 26020 Package Requirements | Source basis for package inclusion criteria | _Sources/26020-Package_Requirements.docx (clause-level location TBD) |
| Site/jurisdictional codes (e.g., CSA, CEC for electrical area classification supporting instrumentation) | ASSUMPTION: likely applicable; clause-level location TBD | TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-043-01-01 | Inspection of SOW for named responsible party (EPC Integrator or assigned subcontractor). |
| REQ-043-01-02 | Inspection of SOW for a tagged-equipment list and package identity list traceable to Workbook row 45. |
| REQ-043-01-03 | Inspection of SOW for an integration narrative describing PKG-043's role in the facility. |
| REQ-043-01-04 | Inspection of SOW for a responsibility assignment record (e.g., RACI or equivalent). |
| REQ-043-01-05 | Cross-check tagged-equipment list against Mechanical package equipment lists to confirm no overlap. |
| REQ-043-01-06 | Inspection of SOW interface section against PACKAGE_REGISTER.csv InterfaceTypes. |
| REQ-043-01-07 | Inspection of SOW source-basis citations. |
| REQ-043-01-08 | Inspection of SOW for citation of governing instrumentation specifications. |
| REQ-043-01-09 | Inspection of SOW for boundary statement relative to the 04-25 Instrument Air package and any shared 03-25/04-25 scope. |
| REQ-043-01-10 | Inspection of SOW for installation responsibility statement covering shipped-loose instruments. |

## Documentation

The deliverable produces the following artifacts (from `_CONTEXT.md` Anticipated Artifacts):

- Package scope of work (this document set: Datasheet, Specification, Guidance, Procedure).
- Tagged equipment and package identity list.
- Package function and integration narrative.
- Responsibility assignment record.

Records produced by execution of this SOW shall include the items in `Procedure.md` § Records.
