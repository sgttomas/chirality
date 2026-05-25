#!/usr/bin/env python3
"""Build the West Doe Combined PROJECT_DECOMP working package.

This generator is intentionally deterministic: it treats the package workbook as
the authoritative package register, extracts package scope and vendor-document
groups from the Word requirements document, and writes the modular working
surface plus authoritative companion registers required by PROJECT_DECOMP.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import openpyxl
from docx import Document
from docx.document import Document as DocumentType
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


PROJECT_ROOT = Path("/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined")
SOURCE_ROOT = PROJECT_ROOT / "_Sources"
OUTPUT_ROOT = PROJECT_ROOT / "_Decomposition" / "PROJECT_DECOMP"

WORKBOOK_PATH = SOURCE_ROOT / "26020-Packages_Interfaces_4_export.xlsx"
DOCX_PATH = SOURCE_ROOT / "26020-Package_Requirements.docx"
DBM_COMP_PATH = SOURCE_ROOT / "DBM-Comp_and_Liquids" / "3-25_Comp_and_Liquids_DBM.md"
DBM_DEEPCUT_PATH = SOURCE_ROOT / "DBM-Deepcut" / "4-25_Deepcut_DBM.md"

REVISION = "1.0"
GENERATED_ON = date.today().isoformat()
GATE1_APPROVAL_DATE = "2026-05-24"
GATE1_SNAPSHOT_DIRNAME = f"GATE-01_Intake_Approved_{GATE1_APPROVAL_DATE}"
GATE2_APPROVAL_DATE = "2026-05-24"
GATE2_SNAPSHOT_DIRNAME = f"GATE-02_SSOW_Vocabulary_Approved_{GATE2_APPROVAL_DATE}"
GATE3_APPROVAL_DATE = "2026-05-24"
GATE3_SNAPSHOT_DIRNAME = f"GATE-03_Objectives_Approved_{GATE3_APPROVAL_DATE}"
GATE4_APPROVAL_DATE = "2026-05-24"
GATE4_SNAPSHOT_DIRNAME = f"GATE-04_Packages_Approved_{GATE4_APPROVAL_DATE}"
GATE5_APPROVAL_DATE = "2026-05-24"
GATE5_SNAPSHOT_DIRNAME = f"GATE-05_Deliverables_Approved_{GATE5_APPROVAL_DATE}"
GATE6_APPROVAL_DATE = "2026-05-24"
GATE6_SNAPSHOT_DIRNAME = f"GATE-06_Coverage_Approved_{GATE6_APPROVAL_DATE}"
GATE7_APPROVAL_DATE = "2026-05-24"
GATE7_SNAPSHOT_DIRNAME = f"GATE-07_Final_Published_{GATE7_APPROVAL_DATE}"

CORE_INTERFACE_COLUMNS = [
    "Process Piping",
    "Utility Piping",
    "Relief / Flare / Vent",
    "Drain / Containment",
    "Electrical Power",
    "EHT",
    "Grounding / Bonding",
    "Area / Exterior Lighting",
    "Cathodic Protection",
    "I&C / Control Cabling",
    "Communications / Network",
    "Building HVAC / Services",
    "Fire & Gas / Safety Systems",
    "Maintenance Access",
    "Grading / Site Drainage / Spill Containment",
    "Structural / Foundations / Supports",
    "Product Loading",
    "Pipeline / Pigging",
]

MANUAL_DOC_MATCH_BY_PACKAGE_ID = {
    "PKG-060": "26020-01-PT-18-002",
    "PKG-061": "26020-01-PT-18-004",
    "PKG-075": "26020-01-PT-28-001",
    "PKG-091": "26020-03-PT-18-002",
}

PACKAGE_SOURCE_DISPOSITIONS = {
    "PKG-069": "Gate 6 disposition: Gas Mole Sieve scope is included with the Cryogenic Unit package scope; NGL Mole Sieve remains a distinct package.",
    "PKG-077": "Gate 6 disposition: Methanol Injection scope is included with the Cryogenic Unit package scope.",
}

OBJECTIVES = [
    {
        "ObjectiveID": "OBJ-001",
        "Statement": "Provide the 04-25 Deepcut facility scope required to process sour raw gas through inlet separation and stabilization, compression, amine treating, gas dehydration, cryogenic C3+ recovery, product handling, acid-gas handling, and supporting systems.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md sections Project Objectives, SEC-04 through SEC-08, SEC-10 through SEC-15; workbook WBS 01 rows",
        "DerivedSourceIntent": "The 04-25 DBM defines a 300 MMSCFD deep cut sour gas processing expansion and supporting facility systems.",
        "TestCriteria": "The 04-25 package set preserves process and support-system scope, interfaces, source references, deliverables, and open issues for the Deepcut design basis.",
        "ExpectedEvidence": "WBS 01 package rows, 04-25 mechanical package scope, electrical/controls/instrument/civil/structural support packages, DBM source references, and package deliverables.",
        "MappingBasis": "Packages with workbook WBS 01 or CoA tracking facility code 01.",
        "Notes": "This replaces the former umbrella integrated-facility objective with a source-specific 04-25 success condition.",
        "ReviewFocus": "Confirm this objective captures the 04-25 facility outcome at the right level for package/deliverable mapping.",
    },
    {
        "ObjectiveID": "OBJ-002",
        "Statement": "Provide the 03-25 compressor station and liquids hub scope required for Doe field inlet receipt and separation, inlet compression, sour-gas dehydration and export, condensate storage and treating, produced-water handling, vapour recovery, product loading, utilities, and construction support.",
        "SourceRef": "DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md sections Facility Overview, Scope Inclusions, Commercial and Facility Interfaces, SEC-04 through SEC-08, SEC-10 through SEC-15; workbook WBS 02 and WBS 03 rows",
        "DerivedSourceIntent": "The 03-25 DBM defines the compressor station, liquids hub, produced-water, VRU, product-handling, and supporting facility scope.",
        "TestCriteria": "The 03-25 package set preserves process and support-system scope, interfaces, source references, deliverables, and open issues for the compression and liquids design basis.",
        "ExpectedEvidence": "WBS 02 and WBS 03 package rows, 3-25 mechanical package scope, support-discipline package rows, DBM source references, and package deliverables.",
        "MappingBasis": "Packages with workbook WBS 02 or WBS 03 or CoA tracking facility code 02 or 03.",
        "Notes": "This objective carries the 03-25 outcome separately from 04-25 so repeated package names are not collapsed.",
        "ReviewFocus": "Confirm this objective captures the 03-25 facility outcome at the right level for package/deliverable mapping.",
    },
    {
        "ObjectiveID": "OBJ-003",
        "Statement": "Preserve commercial stream disposition, metering accountability, and facility boundary interfaces for sales gas, NGL, condensate, acid gas, produced water, LACT/tie-in limits, truck loading, and cross-facility 03-25/04-25 exchanges.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md Project Objectives and Process and Commercial Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md Commercial and Facility Interfaces; workbook interface columns Product Loading and Pipeline / Pigging",
        "DerivedSourceIntent": "Both DBMs define product, third-party, metering, and inter-facility boundaries that must remain explicit in downstream package execution.",
        "TestCriteria": "Stream-handling and boundary packages expose product/disposition interfaces, tie-in limits, metering/control implications, and open boundary issues.",
        "ExpectedEvidence": "Product loading, pigging, tank, compressor, treating, metering/control, acid-gas, condensate, produced-water, NGL, and tie-in related package deliverables and interface facts.",
        "MappingBasis": "Packages with stream/product keywords, Product Loading or Pipeline / Pigging interfaces, or controls/instrumentation responsibility for metering/accountability.",
        "Notes": "This is a source-derived objective rather than a generic traceability rule.",
        "ReviewFocus": "Confirm commercial and stream-boundary accountability should be a distinct decomposition objective.",
    },
    {
        "ObjectiveID": "OBJ-004",
        "Statement": "Execute each electrical and mechanical equipment package as a vendor-owned package with vendor engineering, package design, vendor documentation, physical equipment supply, and EPC integration review preserved as separate responsibilities.",
        "SourceRef": "Accepted Gate 1 responsibility clarification; accepted Gate 2 SSOW; workbook Electrical and Mechanical discipline rows; 26020-Package_Requirements.docx vendor-document tables",
        "DerivedSourceIntent": "The user clarified that electrical and mechanical packages are developed by vendors while the EPC integrates them into the facility.",
        "TestCriteria": "Electrical and mechanical package deliverables assign package engineering/design/equipment/documentation to the Package Vendor and integration/interface review to the EPC Integrator.",
        "ExpectedEvidence": "Electrical and mechanical package register rows, EPC Scope of Work, Package Datasheet, Construction Work Package, vendor-equipment deliverables, vendor-document turnover deliverables, responsibility model text, and EPC interface artifacts.",
        "MappingBasis": "Workbook packages with Electrical or Mechanical discipline.",
        "Notes": "This remains a valid objective because it controls responsibility and deliverable ownership, not just formatting.",
        "ReviewFocus": "Confirm the vendor/EPC split is stated strongly enough and does not assign vendor design work to the EPC Integrator.",
    },
    {
        "ObjectiveID": "OBJ-005",
        "Statement": "Provide and integrate the facility electrical power basis, electrical buildings, transformers, switchgear, MCC/VFD/UPS equipment, standby power, grounding and bonding, lighting, EHT, cathodic protection, and electrical interfaces to vendor packages.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-12 Electrical Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 Electrical Basis; workbook Electrical discipline rows and electrical interface columns",
        "DerivedSourceIntent": "Both DBMs define electrical infrastructure and package power/interface requirements as facility success conditions.",
        "TestCriteria": "Electrical packages and electrical interface facts identify power, grounding, lighting, EHT, cathodic protection, building-service, and vendor-load responsibilities.",
        "ExpectedEvidence": "Electrical package deliverables, electrical interface register facts, vendor load/interface documentation, and source references to electrical DBM sections.",
        "MappingBasis": "Electrical discipline packages and packages carrying electrical power, EHT, grounding/bonding, lighting, or cathodic-protection interfaces.",
        "Notes": "This separates electrical facility success from generic interface coordination.",
        "ReviewFocus": "Confirm electrical infrastructure and vendor-load integration should be a separate objective.",
    },
    {
        "ObjectiveID": "OBJ-006",
        "Statement": "Provide and integrate controls, instrumentation, communications, package control interfaces, fire and gas detection, alarm and shutdown interfaces, and operating data pathways across EPC and vendor package boundaries.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-13 Controls System Basis and SEC-14 Instrumented Protection Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-13 Control System Basis and SEC-14 Instrumentation, Fire and Gas Detection, and Shutdown Interfaces; workbook Controls and Instrumentation rows plus I&C/communications/fire-gas interface columns",
        "DerivedSourceIntent": "The DBMs define controls topology, package interfaces, instrumentation, fire/gas detection, alarms, shutdowns, and operating-data integration.",
        "TestCriteria": "Controls, instrumentation, and package interface deliverables expose I&C, communications, fire/gas, shutdown, metering, and vendor control-system requirements.",
        "ExpectedEvidence": "Controls and instrumentation packages, I&C/communications/fire-gas interface facts, vendor cause-and-effect/control input artifacts, and source references to controls/instrumentation DBM sections.",
        "MappingBasis": "Controls or Instrumentation discipline packages and packages carrying I&C/control cabling, communications/network, or fire and gas/safety-system interfaces.",
        "Notes": "This objective gives controls and instrumentation a direct success condition instead of burying them in an EPC catch-all.",
        "ReviewFocus": "Confirm controls, instrumentation, communications, and shutdown integration are covered at the correct level.",
    },
    {
        "ObjectiveID": "OBJ-007",
        "Statement": "Provide and integrate shared utilities and ancillary support systems including fuel gas, instrument air, drains, flare/blowdown/vent systems, heat medium, HVAC/building services, emergency power interfaces, methanol, lube oil, analyzers, and utility tie-ins.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-08 Utilities and Support Systems Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-07 Utilities and Ancillary Services; workbook utility, relief/flare/vent, drain/containment, HVAC, and related package rows",
        "DerivedSourceIntent": "The DBMs define utilities and ancillary systems as cross-facility and cross-package supports required for operation.",
        "TestCriteria": "Utility and support-system packages expose utility service boundaries, tie-ins, source dependencies, package loads, relief/drain/vent routing, and open service-allocation issues.",
        "ExpectedEvidence": "Fuel gas, instrument air, flare, drain, heat medium, methanol, lube oil, analyzer, HVAC/building-service, utility-interface, and support-system deliverables.",
        "MappingBasis": "Packages with utility, relief/flare/vent, drain/containment, building HVAC/services interfaces or utility/support keywords in the package name.",
        "Notes": "This objective is separate because utility interfaces are a core integration risk across 03-25 and 04-25.",
        "ReviewFocus": "Confirm the utilities/support-system scope is neither too broad nor missing key DBM utility systems.",
    },
    {
        "ObjectiveID": "OBJ-008",
        "Statement": "Provide civil, structural, site, buildings, foundations, grading, containment, access, pipe rack, platform, and construction-support scope needed to install, support, access, and maintain the facility and vendor packages.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md Construction Scope Summary and SEC-11 Plant Layout, Spacing, Civil, and Buildings; workbook Civil and Structural rows plus structural/grading/access interface columns",
        "DerivedSourceIntent": "The DBMs and workbook define civil/structural/construction support as required facility scope for modules, packages, buildings, and site systems.",
        "TestCriteria": "Civil/structural/site packages and interface facts preserve foundation, support, access, grading, drainage, containment, construction, building, pipe-rack, and platform requirements.",
        "ExpectedEvidence": "Civil and structural package deliverables, structural/foundation/grading/access interface facts, building/electrical-building interfaces, and construction-support open issues.",
        "MappingBasis": "Civil or Structural discipline packages and packages carrying structural/foundation/support, grading/site drainage/spill containment, or maintenance-access interfaces.",
        "Notes": "This objective replaces the former broad EPC-led support objective with a concrete civil/structural/site outcome.",
        "ReviewFocus": "Confirm civil/structural/site/construction support is scoped correctly for package integration.",
    },
    {
        "ObjectiveID": "OBJ-009",
        "Statement": "Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, and standards requirements into package scopes and interfaces.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-09 Energy, Prime Movers, and Emissions Basis, SEC-14 Instrumented Protection Basis, SEC-15 Regulatory, Codes, and Standards Basis; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-08 Prime Movers and Emissions, SEC-14 Instrumentation/Fire and Gas/Shutdown Interfaces, SEC-15 Environmental/Regulatory/Specifications/Codes/Standards; workbook safety-related interface columns",
        "DerivedSourceIntent": "The DBMs define sour-service, safety, emissions, environmental, regulatory, and protection constraints that must be visible in package execution.",
        "TestCriteria": "Safety and regulatory package mappings expose fire/gas, shutdown, relief/flare, drain/containment, emissions, environmental, sour-service, and code/standard responsibilities or open issues.",
        "ExpectedEvidence": "Relief/flare/vent, drain/containment, fire/gas, shutdown, sour-service, environmental/regulatory, and safety-interface deliverables and open issue records.",
        "MappingBasis": "Packages with safety-related interfaces or names tied to sour service, acid gas, flare, incineration, caustic, produced water, tanks, methanol, or protection functions.",
        "Notes": "This objective is testable through safety/interface deliverables and explicit open issues.",
        "ReviewFocus": "Confirm this objective captures safety and compliance without becoming a generic quality objective.",
    },
    {
        "ObjectiveID": "OBJ-010",
        "Statement": "Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and controlled open-item closure evidence for package procurement and downstream facility handoff.",
        "SourceRef": "DBM-Deepcut/4-25_Deepcut_DBM.md SEC-10 Plant Design Philosophy and Mechanical Requirements plus assumptions/TBD sections; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-09 Plant Design Requirements and Mechanical Package Structure plus assumptions/TBD sections; 26020-Package_Requirements.docx vendor-document tables",
        "DerivedSourceIntent": "The DBMs and package requirements document define sparing, isolation, maintenance access, vendor document registers, package deliverables, and open design-development items as closure conditions.",
        "TestCriteria": "Package deliverables and open issues show vendor documents, package engineering basis, sparing/isolation/access/winterization assumptions, commissioning/turnover needs, and unresolved DBM/package TBDs.",
        "ExpectedEvidence": "Vendor document turnover deliverables, EPC Scope of Work, Package Datasheet, Construction Work Package, interface evidence artifacts, maintenance-access interfaces, open issue register rows, and coverage telemetry.",
        "MappingBasis": "Vendor packages, packages with maintenance-access interfaces, packages with detailed Word requirements, and packages with source-limited detail/open issues.",
        "Notes": "This is retained as an objective because it is a handoff success condition with deliverable evidence, not just register hygiene.",
        "ReviewFocus": "Confirm open-item and handoff readiness evidence should remain a Gate 3 objective.",
    },
]

VOCABULARY = [
    ("Package", "Work package; equipment package; package row", "Flat PROJECT_DECOMP partition. Workbook rows are authoritative."),
    ("PackageID", "PKG-XXX", "Derived from workbook ID # where present. Missing workbook IDs remain blockers."),
    ("CoA Tracking Number", "Tracking number; package number", "Workbook tracking reference. Repeated values do not merge packages."),
    ("WBS", "Facility code; work breakdown", "Workbook WBS value, used for source grouping and DBM objective mapping."),
    ("4-25 Deepcut", "Deepcut; WBS 01", "Design-basis source represented by DBM-Deepcut and many WBS 01 package rows."),
    ("3-25 Comp and Liquids", "3-25; compression and liquids; WBS 02/03", "Design-basis source represented by DBM-Comp_and_Liquids and WBS 02/03 rows."),
    ("Process Mechanical Equipment Package", "Mechanical package; vendor package", "Mechanical package rows that have detailed scope in the package requirements Word document."),
    ("Electrical Package", "Electrical equipment package; electrical vendor package", "Electrical package rows are treated as vendor-owned engineering/design/equipment packages unless later source authority says otherwise."),
    ("Package Vendor", "Vendor; supplier; equipment vendor", "Entity responsible for engineering, design, vendor documentation, and physical equipment package for each electrical or mechanical package."),
    ("EPC Integrator", "Main EPC company; central EPC; integration contractor", "Entity responsible for integrating vendor packages into a functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration."),
    ("Scope of Work", "SOW; package scope of work", "Mandatory EPC Integrator package deliverable that identifies tagged equipment where source-supported, states package function, and explains whole-facility integration."),
    ("Package Datasheet", "Package data sheet; vendor handoff datasheet", "Mandatory EPC Integrator technical handoff deliverable containing the data required for third-party vendor or discipline package engineering and design."),
    ("Construction Work Package", "CWP; construction package", "Mandatory EPC Integrator package deliverable describing physical installation, construction, tie-ins, inspection, and turnover."),
    ("Vendor Document Turnover", "Vendor document package; vendor submittal package", "Single package-level vendor deliverable that groups source vendor-document rows as artifacts/evidence."),
    ("Vendor Engineering Deliverable", "Vendor document; document requirement", "Word-document deliverable rows carried as artifacts/evidence under Vendor Document Turnover Package deliverables."),
    ("Interface Type", "Interface column; package interface", "Workbook X columns captured as interface facts, not packages."),
    ("DBM", "Design Basis Memorandum; design basis", "Integral source for objectives, boundaries, and source context."),
    ("TBD", "To be determined; unresolved", "Allowed when source truth is missing; must be surfaced in OPEN_ISSUES.csv."),
]


@dataclass
class PackageRow:
    row: int
    workbook_id: str
    package_id: str
    wbs: str
    tracking: str
    name: str
    discipline: str
    interfaces: list[str]
    interface_notes: str
    source_ref: str
    normalized_tracking: str
    source_package_key: str


@dataclass
class DocPackage:
    sequence: int
    heading: str
    tracking: str
    normalized_tracking: str
    name: str
    source_ref: str
    location_status: str = ""
    source_basis: str = ""
    basic_scope: str = ""
    major_equipment: str = ""
    scope_notes: str = ""
    interface_rows: list[dict[str, str]] = field(default_factory=list)
    deliverable_groups: list[dict[str, Any]] = field(default_factory=list)
    interface_coordination_notes: str = ""


def normalize_spaces(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def safe_desc(value: str, fallback: str = "deliverable") -> str:
    value = normalize_spaces(value).lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-+", "-", value)
    return value[:64].strip("-") or fallback


def digest_id(prefix: str, *parts: str, width: int = 10) -> str:
    raw = "|".join(parts)
    return f"{prefix}-{hashlib.sha1(raw.encode('utf-8')).hexdigest()[:width].upper()}"


def normalize_tracking(tracking: str) -> str:
    tracking = normalize_spaces(tracking)
    return tracking.replace("-PT-", "-")


def source_package_key(tracking: str, name: str) -> str:
    return f"{normalize_tracking(tracking)}::{safe_desc(name)}"


def read_workbook() -> list[PackageRow]:
    workbook = openpyxl.load_workbook(WORKBOOK_PATH, data_only=True)
    worksheet = workbook["Packages"]
    rows = list(worksheet.iter_rows(values_only=True))
    headers = [normalize_spaces(cell) for cell in rows[0]]
    header_index = {name: index for index, name in enumerate(headers)}
    packages: list[PackageRow] = []

    for row_number, raw_row in enumerate(rows[1:], start=2):
        if not any(cell not in (None, "") for cell in raw_row):
            continue
        record = {
            header: raw_row[index] if index < len(raw_row) else None
            for header, index in header_index.items()
        }
        raw_id = normalize_spaces(record.get("ID #"))
        package_id = f"PKG-{int(raw_id):03d}" if raw_id.isdigit() else "TBD_PENDING_ID"
        wbs_raw = normalize_spaces(record.get("WBS"))
        wbs = wbs_raw.zfill(2) if wbs_raw.isdigit() else wbs_raw
        tracking = normalize_spaces(record.get("CoA Tracking Number"))
        name = normalize_spaces(record.get("Packages"))
        discipline = normalize_spaces(record.get("Discipline"))
        interfaces = [
            column
            for column in CORE_INTERFACE_COLUMNS
            if normalize_spaces(record.get(column)).upper() == "X"
        ]
        packages.append(
            PackageRow(
                row=row_number,
                workbook_id=raw_id,
                package_id=package_id,
                wbs=wbs,
                tracking=tracking,
                name=name,
                discipline=discipline,
                interfaces=interfaces,
                interface_notes=normalize_spaces(record.get("Interface Review Notes")),
                source_ref=f"Workbook Packages row {row_number}",
                normalized_tracking=normalize_tracking(tracking),
                source_package_key=source_package_key(tracking, name),
            )
        )
    return packages


def iter_blocks(document: DocumentType) -> Iterable[Paragraph | Table]:
    for child in document.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def table_rows(table: Table) -> list[list[str]]:
    return [[normalize_spaces(cell.text) for cell in row.cells] for row in table.rows]


def parse_docx_packages() -> list[DocPackage]:
    document = Document(DOCX_PATH)
    heading_re = re.compile(r"^(26020-\d{2}-PT-\d{2}-\d{3})\s+-\s+(.+)$")
    packages: list[DocPackage] = []
    current: DocPackage | None = None
    active_text_section: str | None = None
    section_buffers: dict[str, list[str]] = defaultdict(list)

    def close_current() -> None:
        nonlocal current, active_text_section, section_buffers
        if current is None:
            return
        current.basic_scope = " ".join(section_buffers.get("Basic Scope", [])).strip()
        current.major_equipment = " ".join(section_buffers.get("Major Included Equipment", [])).strip()
        current.interface_coordination_notes = " ".join(section_buffers.get("Interface Coordination Notes", [])).strip()
        packages.append(current)
        current = None
        active_text_section = None
        section_buffers = defaultdict(list)

    for block in iter_blocks(document):
        if isinstance(block, Paragraph):
            text = normalize_spaces(block.text)
            if not text:
                continue
            match = heading_re.match(text)
            if match:
                close_current()
                current = DocPackage(
                    sequence=len(packages) + 1,
                    heading=text,
                    tracking=match.group(1),
                    normalized_tracking=normalize_tracking(match.group(1)),
                    name=normalize_spaces(match.group(2)),
                    source_ref=f"26020-Package_Requirements.docx package heading {len(packages) + 1}",
                )
                continue
            if current is None:
                continue
            if text in {"Basic Scope", "Major Included Equipment", "Physical Interface Summary", "Vendor Engineering Deliverables", "Interface Coordination Notes"}:
                active_text_section = text
                continue
            if text.startswith("Interface source:"):
                continue
            if active_text_section in {"Basic Scope", "Major Included Equipment", "Interface Coordination Notes"}:
                section_buffers[active_text_section].append(text)
        else:
            if current is None:
                continue
            rows = table_rows(block)
            if not rows:
                continue
            first = rows[0]
            if len(first) == 2 and first[0] == "Location / Status":
                for key, value in rows:
                    if key == "Location / Status":
                        current.location_status = value
                    elif key == "Source Basis":
                        current.source_basis = value
            elif len(first) == 1 and first[0].startswith("Scope Notes / Open Items:"):
                current.scope_notes = first[0].replace("Scope Notes / Open Items:", "", 1).strip()
            elif first[:3] == ["Interface Type", "Applicability", "PE Notes / Questions"]:
                for interface_type, applicability, notes, *_ in rows[1:]:
                    if interface_type:
                        current.interface_rows.append(
                            {
                                "InterfaceType": interface_type,
                                "Applicability": applicability,
                                "Notes": notes,
                            }
                        )
            elif first[:3] == ["Deliverable ID", "Deliverable Name", "Notes"]:
                current.deliverable_groups = parse_deliverable_groups(rows[1:])

    close_current()
    return packages


def parse_deliverable_groups(rows: list[list[str]]) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for row in rows:
        cells = (row + ["", "", ""])[:3]
        deliverable_id, deliverable_name, notes = [normalize_spaces(cell) for cell in cells]
        if not any(cells):
            continue
        if re.match(r"^[A-Z]{3}-\d{3}$", deliverable_id):
            if current is None:
                current = {"Category": "Ungrouped vendor deliverables", "Items": []}
                groups.append(current)
            current["Items"].append(
                {
                    "SourceDeliverableID": deliverable_id,
                    "DeliverableName": deliverable_name,
                    "Notes": notes,
                }
            )
        else:
            category = deliverable_name or deliverable_id
            if category and (deliverable_id == deliverable_name or not re.match(r"^[A-Z]{3}-", deliverable_id)):
                current = {"Category": category, "Items": []}
                groups.append(current)
    return [group for group in groups if group["Items"]]


def dbm_section_refs() -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for label, path in [
        ("DBM-Comp_and_Liquids", DBM_COMP_PATH),
        ("DBM-Deepcut", DBM_DEEPCUT_PATH),
    ]:
        headings: list[str] = []
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                headings.append(line[2:].strip())
        refs[label] = headings
    return refs


def objective_ids_for_package(package: PackageRow, has_doc_scope: bool) -> list[str]:
    ids: set[str] = set()
    facility_codes = package_facility_codes(package)

    if "01" in facility_codes:
        ids.add("OBJ-001")
    if facility_codes & {"02", "03"}:
        ids.add("OBJ-002")
    if supports_stream_disposition_objective(package):
        ids.add("OBJ-003")
    if is_vendor_package(package):
        ids.add("OBJ-004")
    if supports_electrical_objective(package):
        ids.add("OBJ-005")
    if supports_controls_objective(package):
        ids.add("OBJ-006")
    if supports_utilities_objective(package):
        ids.add("OBJ-007")
    if supports_civil_structural_objective(package):
        ids.add("OBJ-008")
    if supports_safety_regulatory_objective(package):
        ids.add("OBJ-009")
    if supports_handoff_objective(package, has_doc_scope):
        ids.add("OBJ-010")

    if not ids:
        ids.add("OBJ-010")
    return sorted(ids)


def package_facility_codes(package: PackageRow) -> set[str]:
    codes: set[str] = set()
    if package.wbs:
        codes.add(package.wbs)
        return codes
    match = re.match(r"^26020-(\d{2})-", package.tracking)
    if match:
        codes.add(match.group(1))
    return codes


def package_has_interface(package: PackageRow, *interfaces: str) -> bool:
    return bool(set(package.interfaces) & set(interfaces))


def package_text_contains(package: PackageRow, keywords: Iterable[str]) -> bool:
    text = f"{package.name} {package.tracking} {package.interface_notes}".lower()
    return any(keyword.lower() in text for keyword in keywords)


def supports_stream_disposition_objective(package: PackageRow) -> bool:
    return (
        package.discipline in {"Controls", "Instrumentation"}
        or package_has_interface(package, "Product Loading", "Pipeline / Pigging")
        or package_text_contains(
            package,
            [
                "sales",
                "ngl",
                "condensate",
                "product",
                "loading",
                "acid gas",
                "produced",
                "sour water",
                "sour condensate",
                "pig receiver",
                "inlet",
                "meter",
                "tank",
                "storage",
                "vapour",
                "vapor",
                "caustic",
                "stabilizer",
                "amine",
                "teg",
                "cryogenic",
                "deepcut",
                "mole sieve",
                "dehy",
                "compressor",
                "truck",
                "lact",
            ],
        )
    )


def supports_electrical_objective(package: PackageRow) -> bool:
    return package.discipline == "Electrical" or package_has_interface(
        package,
        "Electrical Power",
        "EHT",
        "Grounding / Bonding",
        "Area / Exterior Lighting",
        "Cathodic Protection",
    )


def supports_controls_objective(package: PackageRow) -> bool:
    return package.discipline in {"Controls", "Instrumentation"} or package_has_interface(
        package,
        "I&C / Control Cabling",
        "Communications / Network",
        "Fire & Gas / Safety Systems",
    )


def supports_utilities_objective(package: PackageRow) -> bool:
    return (
        package_has_interface(
            package,
            "Utility Piping",
            "Relief / Flare / Vent",
            "Drain / Containment",
            "Building HVAC / Services",
        )
        or package_text_contains(
            package,
            [
                "fuel gas",
                "instrument air",
                "flare",
                "drain",
                "heat medium",
                "lube oil",
                "methanol",
                "vapour recovery",
                "vapor recovery",
                "emergency",
                "analyzer",
                "hvac",
                "building",
                "incinerator",
            ],
        )
    )


def supports_civil_structural_objective(package: PackageRow) -> bool:
    return (
        package.discipline in {"Civil", "Structural"}
        or package_has_interface(
            package,
            "Structural / Foundations / Supports",
            "Grading / Site Drainage / Spill Containment",
            "Maintenance Access",
        )
        or package_text_contains(
            package,
            [
                "building",
                "foundation",
                "grading",
                "berm",
                "pond",
                "pipe rack",
                "platform",
                "road",
                "containment",
            ],
        )
    )


def supports_safety_regulatory_objective(package: PackageRow) -> bool:
    return (
        package_has_interface(
            package,
            "Relief / Flare / Vent",
            "Drain / Containment",
            "Fire & Gas / Safety Systems",
            "Grounding / Bonding",
            "Cathodic Protection",
        )
        or package_text_contains(
            package,
            [
                "sour",
                "acid gas",
                "flare",
                "incinerator",
                "caustic",
                "hydrogen peroxide",
                "produced water",
                "tank",
                "methanol",
                "amine",
                "teg",
                "cryogenic",
                "mole sieve",
                "shutdown",
            ],
        )
    )


def supports_handoff_objective(package: PackageRow, has_doc_scope: bool) -> bool:
    return (
        is_vendor_package(package)
        or has_doc_scope
        or package_has_interface(package, "Maintenance Access")
        or bool(package.interface_notes)
    )


def is_vendor_package(package: PackageRow) -> bool:
    return package.discipline in {"Electrical", "Mechanical"}


def responsibility_model(package: PackageRow) -> str:
    if is_vendor_package(package):
        return (
            "Package Vendor owns package engineering, package design, vendor documentation, "
            "and the physical equipment package. EPC Integrator owns integration into the "
            "functional process facility, including interfaces, tie-ins, constructability, "
            "procurement/construction coordination, and facility-level integration."
        )
    return (
        "EPC Integrator or discipline subcontractor responsibility is source-dependent; "
        "no separate vendor-package ownership model is inferred from the current sources."
    )


def interface_disposition_note(package: PackageRow) -> str:
    if not package.interface_notes:
        return ""
    if package.discipline == "Controls":
        return (
            f"{package.interface_notes} Gate 6 disposition: controls power-panel interfaces remain interface "
            "facts/artifacts under the package datasheet; no separate package or deliverable is created."
        )
    if package.discipline == "Instrumentation":
        return (
            f"{package.interface_notes} Gate 6 disposition: instrumentation field supports, power, and "
            "communications are included in each package scope as appropriate under the plug-n-play package philosophy."
        )
    if package.package_id == "PKG-103":
        return (
            f"{package.interface_notes} Gate 6 disposition: pipe racks and pipe rack modules are designed "
            "exclusively by the EPC Integrator."
        )
    if package.package_id == "PKG-105":
        return (
            f"{package.interface_notes} Gate 6 disposition: platform-to-equipment tie-ins are the EPC "
            "Integrator's responsibility through the overall 3D model and integrated P&ID set."
        )
    return f"{package.interface_notes} Gate 6 disposition recorded."


def base_deliverable_responsible_party(package: PackageRow, deliverable_type: str) -> str:
    if is_vendor_package(package):
        if deliverable_type == "Interface Coordination":
            return "EPC Integrator (lead) with Package Vendor input"
        return "Package Vendor (engineering/design/equipment) with EPC Integrator integration review"
    if deliverable_type == "Interface Coordination":
        return "EPC Integrator (lead); discipline support TBD"
    return "TBD; EPC Integrator or discipline subcontractor as assigned"


def source_refs_for_package(package: PackageRow, doc_pkg: DocPackage | None) -> str:
    refs = [package.source_ref]
    if doc_pkg:
        refs.append(doc_pkg.source_ref)
        if doc_pkg.source_basis:
            refs.append(f"Word Source Basis: {doc_pkg.source_basis}")
    if package.package_id in PACKAGE_SOURCE_DISPOSITIONS:
        refs.append(PACKAGE_SOURCE_DISPOSITIONS[package.package_id])
    if package.wbs == "01":
        refs.append("DBM-Deepcut/4-25_Deepcut_DBM.md")
    elif package.wbs in {"02", "03"}:
        refs.append("DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md")
    return "; ".join(refs)


def build_doc_package_match(packages: list[PackageRow], doc_packages: list[DocPackage]) -> dict[str, DocPackage]:
    by_key: dict[str, list[DocPackage]] = defaultdict(list)
    by_tracking: dict[str, list[DocPackage]] = defaultdict(list)
    by_raw_tracking: dict[str, list[DocPackage]] = defaultdict(list)
    for doc_pkg in doc_packages:
        by_key[source_package_key(doc_pkg.tracking, doc_pkg.name)].append(doc_pkg)
        by_tracking[doc_pkg.normalized_tracking].append(doc_pkg)
        by_raw_tracking[doc_pkg.tracking].append(doc_pkg)

    matched: dict[str, DocPackage] = {}
    used_doc_ids: set[int] = set()
    for package in packages:
        manual_doc_tracking = MANUAL_DOC_MATCH_BY_PACKAGE_ID.get(package.package_id)
        if manual_doc_tracking:
            manual_candidates = by_raw_tracking.get(manual_doc_tracking, [])
            if len(manual_candidates) == 1:
                matched[package.source_package_key] = manual_candidates[0]
                used_doc_ids.add(id(manual_candidates[0]))
                continue

        candidates = by_key.get(package.source_package_key, [])
        candidates = [candidate for candidate in candidates if id(candidate) not in used_doc_ids]
        if len(candidates) == 1:
            matched[package.source_package_key] = candidates[0]
            used_doc_ids.add(id(candidates[0]))
            continue

        candidates = [candidate for candidate in by_tracking.get(package.normalized_tracking, []) if id(candidate) not in used_doc_ids]
        if len(candidates) == 1:
            matched[package.source_package_key] = candidates[0]
            used_doc_ids.add(id(candidates[0]))
            continue

        if len(candidates) > 1:
            package_name_key = safe_desc(package.name)
            ranked = sorted(
                candidates,
                key=lambda candidate: text_similarity_score(package_name_key, safe_desc(candidate.name)),
                reverse=True,
            )
            if ranked and text_similarity_score(package_name_key, safe_desc(ranked[0].name)) > 0:
                matched[package.source_package_key] = ranked[0]
                used_doc_ids.add(id(ranked[0]))
    return matched


def text_similarity_score(left: str, right: str) -> int:
    left_terms = {term for term in left.split("-") if term}
    right_terms = {term for term in right.split("-") if term}
    return len(left_terms & right_terms)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: serialize_cell(row.get(field, "")) for field in fieldnames})


def serialize_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def list_count(value: Any) -> int:
    if isinstance(value, list):
        return len(value)
    return len([item for item in serialize_cell(value).split("; ") if item])


def build_outputs() -> None:
    packages = read_workbook()
    doc_packages = parse_docx_packages()
    doc_match = build_doc_package_match(packages, doc_packages)
    dbm_refs = dbm_section_refs()

    package_rows: list[dict[str, Any]] = []
    interface_rows: list[dict[str, Any]] = []
    scope_rows: list[dict[str, Any]] = []
    deliverable_rows: list[dict[str, Any]] = []
    artifact_rows: list[dict[str, Any]] = []
    open_issues: list[dict[str, Any]] = []
    objective_rows: list[dict[str, Any]] = []
    objective_scope_map_rows: list[dict[str, Any]] = []
    objective_package_map_rows: list[dict[str, Any]] = []
    objective_deliverable_map_rows: list[dict[str, Any]] = []

    deliverables_by_package: dict[str, list[str]] = defaultdict(list)
    scope_by_package: dict[str, list[str]] = defaultdict(list)
    doc_scope_items_by_package: dict[str, list[str]] = defaultdict(list)

    issue_seq = 1
    scope_seq = 1

    matched_doc_object_ids = {id(doc_pkg) for doc_pkg in doc_match.values()}

    for package in packages:
        doc_pkg = doc_match.get(package.source_package_key)
        has_doc_scope = doc_pkg is not None
        package_objectives = objective_ids_for_package(package, has_doc_scope)
        package_rows.append(
            {
                "PackageID": package.package_id,
                "WorkbookID": package.workbook_id,
                "WorkbookRow": package.row,
                "WBS": package.wbs,
                "CoATrackingNumber": package.tracking,
                "NormalizedTrackingNumber": package.normalized_tracking,
                "Name": package.name,
                "Discipline": package.discipline,
                "ResponsibilityModel": responsibility_model(package),
                "ScopeDescription": build_package_scope_description(package, doc_pkg),
                "InclusionCriteria": build_inclusion_criteria(package, doc_pkg),
                "Exclusions": "TBD; no package-specific exclusions stated in source materials.",
                "InterfaceTypes": package.interfaces,
                "InterfaceReviewNotes": package.interface_notes,
                "SourceRefs": source_refs_for_package(package, doc_pkg),
                "DocxPackageMatched": "TRUE" if doc_pkg else "FALSE",
                "DocxPackageHeading": doc_pkg.heading if doc_pkg else "",
                "SupportsObjectives": package_objectives,
                "OpenIssue": "TRUE" if package.package_id == "TBD_PENDING_ID" else "FALSE",
                "PackageRole": "authoritative companion register row",
            }
        )

        if package.package_id == "TBD_PENDING_ID":
            open_issues.append(
                issue(
                    issue_seq,
                    "BLOCKER",
                    "MISSING_PACKAGE_ID",
                    "Gate 4",
                    "TBD_PENDING_ID",
                    "Yard Lighting has no workbook ID #, so a compliant PKG-XXX identifier cannot be assigned without human resolution.",
                    package.source_ref,
                    "Assign an authoritative workbook ID # or confirm a controlled ID amendment.",
                )
            )
            issue_seq += 1

        for interface_type in package.interfaces:
            interface_rows.append(
                {
                    "InterfaceID": digest_id("IFC", package.source_ref, interface_type),
                    "PackageID": package.package_id,
                    "WorkbookID": package.workbook_id,
                    "WorkbookRow": package.row,
                    "PackageName": package.name,
                    "Discipline": package.discipline,
                    "InterfaceType": interface_type,
                    "Applicability": "YES",
                    "SourceRef": package.source_ref,
                    "Notes": interface_disposition_note(package),
                }
            )

        package_scope_id = f"SOW-{scope_seq:04d}"
        scope_seq += 1
        scope_by_package[package.package_id].append(package_scope_id)
        scope_rows.append(
            {
                "ScopeItemID": package_scope_id,
                "InOutStatus": "IN",
                "ScopeItemStatement": build_package_scope_item_statement(package),
                "SourceRef": package.source_ref,
                "PackageID": package.package_id,
                "DeliverableID(s)": "",
                "ObjectiveID(s)": package_objectives,
                "DecisionRef": "DEC-001",
                "OpenIssue": "TRUE" if package.package_id == "TBD_PENDING_ID" else "FALSE",
                "Notes": "Workbook package row is authoritative. Duplicate tracking numbers are not merged.",
            }
        )

        if doc_pkg:
            for label, statement in [
                ("Basic scope", doc_pkg.basic_scope),
                ("Major included equipment", doc_pkg.major_equipment),
                ("Scope notes and open items", doc_pkg.scope_notes),
            ]:
                if not statement:
                    continue
                scope_id = f"SOW-{scope_seq:04d}"
                scope_seq += 1
                scope_by_package[package.package_id].append(scope_id)
                doc_scope_items_by_package[package.package_id].append(scope_id)
                scope_rows.append(
                    {
                        "ScopeItemID": scope_id,
                        "InOutStatus": "IN",
                        "ScopeItemStatement": f"{package.name}: {label}: {statement}",
                        "SourceRef": f"{doc_pkg.source_ref}; {label}",
                        "PackageID": package.package_id,
                        "DeliverableID(s)": "",
                        "ObjectiveID(s)": package_objectives,
                        "DecisionRef": "",
                        "OpenIssue": "FALSE",
                        "Notes": "Extracted from process mechanical package requirements document.",
                    }
                )

        next_deliverable_seq = 1
        next_deliverable_seq = append_base_deliverables(
            package,
            doc_pkg,
            package_objectives,
            scope_by_package[package.package_id],
            deliverable_rows,
            artifact_rows,
            deliverables_by_package,
            next_deliverable_seq,
        )

    assign_scope_deliverables(scope_rows, deliverables_by_package)

    unmatched_doc_packages = [doc_pkg for doc_pkg in doc_packages if id(doc_pkg) not in matched_doc_object_ids]
    for doc_pkg in unmatched_doc_packages:
        open_issues.append(
            issue(
                issue_seq,
                "ACTION",
                "UNMATCHED_WORD_PACKAGE_SECTION",
                "Gate 6",
                "TBD",
                f"Word package section '{doc_pkg.heading}' did not match a workbook package row by tracking/name.",
                doc_pkg.source_ref,
                "Confirm whether this section is superseded, renamed, or should be mapped manually.",
            )
        )
        issue_seq += 1

    objective_support = build_objective_support(deliverable_rows)
    objective_scope_support = build_objective_scope_support(scope_rows)
    scope_lookup = {row["ScopeItemID"]: row for row in scope_rows}
    package_lookup = {row["PackageID"]: row for row in package_rows}
    deliverable_lookup = {row["DeliverableID"]: row for row in deliverable_rows}
    for objective in OBJECTIVES:
        objective_id = objective["ObjectiveID"]
        scope_support = objective_scope_support.get(objective["ObjectiveID"], {"ScopeItems": [], "Packages": []})
        mapped_scope_items = scope_support["ScopeItems"]
        mapped_packages = scope_support["Packages"]
        mapped_deliverables = objective_support.get(objective_id, [])
        objective_rows.append(
            {
                "ObjectiveID": objective_id,
                "Statement": objective["Statement"],
                "SourceRef": objective["SourceRef"],
                "DerivedSourceIntent": objective["DerivedSourceIntent"],
                "TestCriteria": objective["TestCriteria"],
                "ExpectedEvidence": objective["ExpectedEvidence"],
                "MappingBasis": objective["MappingBasis"],
                "Notes": objective["Notes"],
                "ReviewFocus": objective["ReviewFocus"],
                "MappedScopeItemCount": len(mapped_scope_items),
                "MappedPackageCount": len(mapped_packages),
                "MappedDeliverableCount": len(mapped_deliverables),
                "OpenIssue": "FALSE" if mapped_deliverables else "TRUE",
            }
        )
        for scope_item_id in mapped_scope_items:
            scope_row = scope_lookup.get(scope_item_id, {})
            objective_scope_map_rows.append(
                {
                    "ObjectiveID": objective_id,
                    "ScopeItemID": scope_item_id,
                    "PackageID": scope_row.get("PackageID", ""),
                    "SourceRef": scope_row.get("SourceRef", ""),
                    "OpenIssue": scope_row.get("OpenIssue", ""),
                }
            )
        for package_id in mapped_packages:
            package_row = package_lookup.get(package_id, {})
            objective_package_map_rows.append(
                {
                    "ObjectiveID": objective_id,
                    "PackageID": package_id,
                    "WorkbookID": package_row.get("WorkbookID", ""),
                    "WorkbookRow": package_row.get("WorkbookRow", ""),
                    "PackageName": package_row.get("Name", ""),
                    "Discipline": package_row.get("Discipline", ""),
                    "WBS": package_row.get("WBS", ""),
                    "SourceRefs": package_row.get("SourceRefs", ""),
                }
            )
        for deliverable_id in mapped_deliverables:
            deliverable_row = deliverable_lookup.get(deliverable_id, {})
            objective_deliverable_map_rows.append(
                {
                    "ObjectiveID": objective_id,
                    "DeliverableID": deliverable_id,
                    "ParentPackageID": deliverable_row.get("ParentPackageID", ""),
                    "PackageName": deliverable_row.get("PackageName", ""),
                    "DeliverableName": deliverable_row.get("Name", ""),
                    "Type": deliverable_row.get("Type", ""),
                    "ResponsibleParty": deliverable_row.get("ResponsibleParty", ""),
                    "SourceRef": deliverable_row.get("SourceRef", ""),
                }
            )

    vocabulary_rows = [
        {"CanonicalTerm": term, "Synonyms": synonyms, "Notes": notes}
        for term, synonyms, notes in VOCABULARY
    ]

    telemetry = build_telemetry(
        packages,
        doc_packages,
        doc_match,
        package_rows,
        scope_rows,
        deliverable_rows,
        artifact_rows,
        open_issues,
        objective_rows,
        objective_scope_map_rows,
        objective_package_map_rows,
        objective_deliverable_map_rows,
    )

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    write_registers(
        package_rows,
        scope_rows,
        deliverable_rows,
        artifact_rows,
        interface_rows,
        objective_rows,
        objective_scope_map_rows,
        objective_package_map_rows,
        objective_deliverable_map_rows,
        vocabulary_rows,
        open_issues,
        telemetry,
    )
    write_main_doc(package_rows, deliverable_rows, scope_rows, open_issues, objective_rows, telemetry, dbm_refs)
    write_validation_report(telemetry, open_issues)


def build_package_scope_description(package: PackageRow, doc_pkg: DocPackage | None) -> str:
    if doc_pkg and doc_pkg.basic_scope:
        if is_vendor_package(package):
            return (
                f"{doc_pkg.basic_scope} Package vendor is responsible for the package engineering, "
                "design, vendor documentation, and physical equipment package; the EPC Integrator "
                "is responsible for integrating this package into the whole process facility."
            )
        return doc_pkg.basic_scope
    if is_vendor_package(package):
        return (
            f"Workbook-defined vendor-owned {package.discipline} package for '{package.name}' "
            f"under WBS {package.wbs or 'TBD'} with package engineering/design/equipment by the "
            "Package Vendor and facility integration by the EPC Integrator."
        )
    return (
        f"Workbook-defined {package.discipline} package for '{package.name}'"
        f" under WBS {package.wbs or 'TBD'} with recorded physical interfaces."
    )


def build_inclusion_criteria(package: PackageRow, doc_pkg: DocPackage | None) -> str:
    criteria = [f"Workbook row {package.row}; discipline {package.discipline}; WBS {package.wbs or 'TBD'}."]
    if is_vendor_package(package):
        criteria.append(
            "Electrical/mechanical package vendor owns package engineering, package design, "
            "vendor documentation, and physical equipment package; EPC Integrator owns "
            "facility-level integration and interfaces."
        )
    if package.interfaces:
        criteria.append(f"Applicable interface types: {'; '.join(package.interfaces)}.")
    if doc_pkg:
        criteria.append("Detailed process mechanical scope and vendor documentation requirements from the Word package section.")
    return " ".join(criteria)


def build_package_scope_item_statement(package: PackageRow) -> str:
    if is_vendor_package(package):
        return (
            f"Carry the workbook-defined vendor-responsible {package.discipline} package "
            f"'{package.name}' as a distinct flat project package for WBS {package.wbs or 'TBD'}; "
            "the Package Vendor owns engineering/design/equipment and the EPC Integrator owns "
            "facility integration."
        )
    return (
        f"Carry the workbook-defined {package.discipline} package '{package.name}' "
        f"as a distinct flat project package for WBS {package.wbs or 'TBD'}."
    )


def issue(
    seq: int,
    severity: str,
    issue_type: str,
    gate: str,
    related_id: str,
    statement: str,
    source_ref: str,
    required_action: str,
) -> dict[str, Any]:
    return {
        "IssueID": f"ISS-{seq:03d}",
        "Severity": severity,
        "IssueType": issue_type,
        "Gate": gate,
        "RelatedID": related_id,
        "Statement": statement,
        "SourceRef": source_ref,
        "RequiredAction": required_action,
        "Status": "OPEN",
    }


def append_base_deliverables(
    package: PackageRow,
    doc_pkg: DocPackage | None,
    objective_ids: list[str],
    scope_ids: list[str],
    deliverable_rows: list[dict[str, Any]],
    artifact_rows: list[dict[str, Any]],
    deliverables_by_package: dict[str, list[str]],
    next_seq: int,
) -> int:
    source_ref = package.source_ref if not doc_pkg else f"{package.source_ref}; {doc_pkg.source_ref}"
    sow_artifacts = [
        {
            "Name": "Package scope of work",
            "Type": "EPC Scope of Work",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Integrator-authored package scope, function, tagged-equipment basis, source rows, WBS, discipline, and boundaries.",
        },
        {
            "Name": "Tagged equipment and package identity list",
            "Type": "Tagged Equipment Evidence",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Package name, workbook ID, CoA tracking number, WBS, and detailed major-equipment text where source-supported.",
        },
        {
            "Name": "Package function and whole-facility integration narrative",
            "Type": "EPC Integration Narrative",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Explains what the package does and how it integrates into the process facility.",
        },
        {
            "Name": "Package responsibility assignment record",
            "Type": "Responsibility Evidence",
            "SourceArtifactID": "",
            "SourceRef": package.source_ref,
            "Notes": responsibility_model(package),
        },
    ]
    if doc_pkg:
        sow_artifacts.append(
            {
                "Name": "Detailed mechanical package scope extraction evidence",
                "Type": "Source Scope Evidence",
                "SourceArtifactID": "",
                "SourceRef": doc_pkg.source_ref,
                "Notes": "Detailed scope text from the package requirements document supports this package basis.",
            }
        )
    next_seq = append_deliverable(
        package,
        objective_ids,
        scope_ids,
        deliverable_rows,
        artifact_rows,
        deliverables_by_package,
        next_seq,
        "Scope of Work",
        "scope-of-work",
        "EPC Scope of Work",
        "Mandatory EPC Integrator deliverable for the full package scope, including tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative.",
        "EPC Integrator",
        "Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record",
        source_ref,
        "FALSE",
        "Mandatory Gate 5 EPC anchor deliverable defined by user instruction.",
        sow_artifacts,
    )

    datasheet_artifacts = [
        {
            "Name": "Package technical datasheet",
            "Type": "EPC Package Datasheet",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Integrator-authored technical handoff data required for third-party package engineering and design.",
        },
        {
            "Name": "Vendor engineering handoff basis",
            "Type": "Vendor Handoff Evidence",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Technical basis, battery limits, design expectations, and source-supported requirements to be handed to the package delivery entity.",
        },
        {
            "Name": "Package interface requirements matrix",
            "Type": "EPC Interface Requirements Evidence",
            "SourceArtifactID": "",
            "SourceRef": package.source_ref,
            "Notes": "Workbook interface facts are carried as datasheet evidence for third-party engineering/design handoff.",
        },
    ]
    for interface_type in package.interfaces:
        datasheet_artifacts.append(
            {
                "Name": f"Interface fact - {interface_type}",
                "Type": "Interface Fact Evidence",
                "SourceArtifactID": digest_id("IFC", package.source_ref, interface_type),
                "SourceRef": package.source_ref,
                "Notes": interface_disposition_note(package) or "Workbook interface X-column fact carried as evidence, not as a separate deliverable.",
            }
        )
    if package.interface_notes:
        datasheet_artifacts.append(
            {
                "Name": "Interface note disposition record",
                "Type": "Interface Issue Evidence",
                "SourceArtifactID": "",
                "SourceRef": package.source_ref,
                "Notes": interface_disposition_note(package),
            }
        )
    if doc_pkg and doc_pkg.major_equipment:
        datasheet_artifacts.append(
            {
                "Name": "Major included equipment evidence",
                "Type": "Tagged Equipment Evidence",
                "SourceArtifactID": "",
                "SourceRef": f"{doc_pkg.source_ref}; Major Included Equipment",
                "Notes": doc_pkg.major_equipment,
            }
        )
    next_seq = append_deliverable(
        package,
        sorted(set(objective_ids + ["OBJ-004", "OBJ-010"])) if is_vendor_package(package) else objective_ids,
        scope_ids,
        deliverable_rows,
        artifact_rows,
        deliverables_by_package,
        next_seq,
        "Package Datasheet",
        "package-datasheet",
        "EPC Package Datasheet",
        "Mandatory EPC Integrator technical handoff deliverable containing the package data required for third-party vendor or discipline package engineering and design.",
        "EPC Integrator",
        "Package technical datasheet; vendor engineering handoff basis; package interface requirements matrix; source-supported equipment and design criteria",
        source_ref,
        "FALSE",
        "Mandatory Gate 5 EPC anchor deliverable; interface facts are intentionally carried here as evidence rather than standalone deliverables.",
        datasheet_artifacts,
    )

    cwp_artifacts = [
        {
            "Name": "Construction work package",
            "Type": "EPC Construction Work Package",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems.",
        },
        {
            "Name": "Installation and tie-in workface plan",
            "Type": "Construction Tie-In Evidence",
            "SourceArtifactID": "",
            "SourceRef": source_ref,
            "Notes": "Workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable.",
        },
        {
            "Name": "Construction interface and turnover checklist",
            "Type": "Construction Interface Evidence",
            "SourceArtifactID": "",
            "SourceRef": package.source_ref,
            "Notes": "Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package.",
        },
    ]
    next_seq = append_deliverable(
        package,
        sorted(set(objective_ids + ["OBJ-008", "OBJ-010"])),
        scope_ids,
        deliverable_rows,
        artifact_rows,
        deliverables_by_package,
        next_seq,
        "Construction Work Package",
        "construction-work-package",
        "EPC Construction Work Package",
        "Mandatory EPC Integrator deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.",
        "EPC Integrator",
        "Construction work package; installation and tie-in workface plan; construction interface and turnover checklist",
        source_ref,
        "FALSE",
        "Mandatory Gate 5 EPC anchor deliverable defined by user instruction.",
        cwp_artifacts,
    )

    if is_vendor_package(package):
        vendor_equipment_artifacts = [
            {
                "Name": "Vendor engineered physical equipment package",
                "Type": "Vendor Equipment Package",
                "SourceArtifactID": "",
                "SourceRef": source_ref,
                "Notes": "Vendor-owned engineering, design, fabrication/supply, and physical package evidence.",
            },
            {
                "Name": "Vendor package design basis and datasheet set",
                "Type": "Vendor Design Evidence",
                "SourceArtifactID": "",
                "SourceRef": source_ref,
                "Notes": "Expected vendor package design basis and datasheet evidence; detailed rows are source-specific where available.",
            },
        ]
        if doc_pkg and doc_pkg.major_equipment:
            vendor_equipment_artifacts.append(
                {
                    "Name": "Major included equipment evidence",
                    "Type": "Source Scope Evidence",
                    "SourceArtifactID": "",
                    "SourceRef": f"{doc_pkg.source_ref}; Major Included Equipment",
                    "Notes": doc_pkg.major_equipment,
                }
            )
        next_seq = append_deliverable(
            package,
            objective_ids,
            scope_ids,
            deliverable_rows,
            artifact_rows,
            deliverables_by_package,
            next_seq,
            "Vendor Engineered Equipment Package",
            "vendor-engineered-equipment-package",
            "Vendor Package Production Unit",
            "Package Vendor production unit for engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work and Package Datasheet.",
            "Package Vendor (engineering/design/equipment) with EPC Integrator integration review",
            "Vendor engineered physical equipment package; vendor package design basis and datasheet set",
            source_ref,
            "FALSE",
            "Additional Gate 5 deliverable framed as a vendor package production unit anchored by the EPC Scope of Work and Package Datasheet.",
            vendor_equipment_artifacts,
        )

        vendor_doc_artifacts = build_vendor_document_artifacts(package, doc_pkg)
        next_seq = append_deliverable(
            package,
            sorted(set(objective_ids + ["OBJ-004", "OBJ-010"])),
            scope_ids,
            deliverable_rows,
            artifact_rows,
            deliverables_by_package,
            next_seq,
            "Vendor Document Turnover Package",
            "vendor-document-turnover-package",
            "Vendor Document Turnover",
            "Single Package Vendor deliverable for the vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review.",
            "Package Vendor (vendor documentation) with EPC Integrator interface/integration review",
            "Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records",
            source_ref,
            "FALSE" if doc_pkg else "TRUE",
            "Additional Gate 5 deliverable; individual source document rows remain artifacts/evidence, not separate deliverables.",
            vendor_doc_artifacts,
        )

        acceptance_artifacts = [
            {
                "Name": "Vendor document review and comment log",
                "Type": "EPC Vendor Review Evidence",
                "SourceArtifactID": "",
                "SourceRef": source_ref,
                "Notes": "EPC review evidence for vendor documentation and integration requirements.",
            },
            {
                "Name": "Vendor package acceptance and turnover checklist",
                "Type": "EPC Acceptance Evidence",
                "SourceArtifactID": "",
                "SourceRef": source_ref,
                "Notes": "Acceptance and turnover evidence for integration into the facility.",
            },
            {
                "Name": "Factory/shop test and inspection evidence",
                "Type": "Vendor Test Evidence",
                "SourceArtifactID": "",
                "SourceRef": source_ref,
                "Notes": "Expected package test/inspection evidence; detailed requirements are source-specific where available.",
            },
        ]
        next_seq = append_deliverable(
            package,
            sorted(set(objective_ids + ["OBJ-010"])),
            scope_ids,
            deliverable_rows,
            artifact_rows,
            deliverables_by_package,
            next_seq,
            "EPC Vendor Package Review and Acceptance",
            "epc-vendor-package-review-and-acceptance",
            "EPC Vendor Package Acceptance",
            "EPC Integrator deliverable for vendor package review, integration acceptance, and handoff readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package.",
            "EPC Integrator (lead) with Package Vendor input",
            "Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence",
            source_ref,
            "FALSE" if doc_pkg else "TRUE",
            "Additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence.",
            acceptance_artifacts,
        )
    else:
        next_seq = append_deliverable(
            package,
            objective_ids,
            scope_ids,
            deliverable_rows,
            artifact_rows,
            deliverables_by_package,
            next_seq,
            f"EPC / {package.discipline} Discipline Production Package",
            f"epc-{package.discipline.lower()}-discipline-production-package",
            "EPC/Discipline Production Unit",
            "EPC Integrator or discipline subcontractor production unit for the non-vendor package scope, carried conservatively from workbook and DBM support.",
            "TBD; EPC Integrator or discipline subcontractor as assigned",
            "Discipline production package basis; TBD discipline deliverable register; source-limited requirements closure record",
            source_ref,
            "TRUE",
            "Detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition.",
            [
                {
                    "Name": "Discipline production package basis",
                    "Type": "EPC/Discipline Production Evidence",
                    "SourceArtifactID": "",
                    "SourceRef": source_ref,
                    "Notes": "Workbook and DBM-supported production package evidence.",
                },
                {
                    "Name": "Source-limited requirements closure record",
                    "Type": "Source Gap Evidence",
                    "SourceArtifactID": "",
                    "SourceRef": source_ref,
                    "Notes": "Detailed discipline requirements are not present in the current source set and remain open.",
                },
            ],
        )
    return next_seq


def append_deliverable(
    package: PackageRow,
    objective_ids: list[str],
    scope_ids: list[str],
    deliverable_rows: list[dict[str, Any]],
    artifact_rows: list[dict[str, Any]],
    deliverables_by_package: dict[str, list[str]],
    next_seq: int,
    name: str,
    desc: str,
    deliverable_type: str,
    description: str,
    responsible_party: str,
    anticipated_artifacts: str,
    source_ref: str,
    _open_issue: str,
    notes: str,
    artifacts: list[dict[str, str]],
) -> int:
    deliverable_id = make_deliverable_id(package.package_id, next_seq, desc)
    deliverables_by_package[package.package_id].append(deliverable_id)
    deliverable_rows.append(
        {
            "DeliverableID": deliverable_id,
            "Name": name,
            "ParentPackageID": package.package_id,
            "ParentWorkbookID": package.workbook_id,
            "PackageName": package.name,
            "Description": description,
            "ResponsibleParty": responsible_party,
            "Type": deliverable_type,
            "AnticipatedArtifacts": anticipated_artifacts,
            "CoversScopeItems": scope_ids,
            "SupportsObjectives": objective_ids,
            "SourceRef": source_ref,
            "Notes": notes,
        }
    )
    for artifact in artifacts:
        artifact_rows.append(
            {
                "ArtifactID": digest_id("ART", deliverable_id, artifact.get("Name", ""), artifact.get("SourceArtifactID", "")),
                "Name": artifact.get("Name", ""),
                "ParentDeliverableID": deliverable_id,
                "ParentPackageID": package.package_id,
                "Type": artifact.get("Type", deliverable_type),
                "SourceArtifactID": artifact.get("SourceArtifactID", ""),
                "SourceRef": artifact.get("SourceRef", source_ref),
                "Notes": artifact.get("Notes", ""),
            }
        )
    return next_seq + 1


def build_vendor_document_artifacts(package: PackageRow, doc_pkg: DocPackage | None) -> list[dict[str, str]]:
    if not doc_pkg:
        return [
            {
                "Name": "TBD vendor document register",
                "Type": "Vendor Documentation Gap Evidence",
                "SourceArtifactID": "",
                "SourceRef": package.source_ref,
                "Notes": "Detailed vendor-document requirements are not present in current source material for this package.",
            }
        ]
    artifacts: list[dict[str, str]] = [
        {
            "Name": "Vendor document register",
            "Type": "Vendor Documentation Register",
            "SourceArtifactID": "",
            "SourceRef": f"{doc_pkg.source_ref}; Vendor Engineering Deliverables table",
            "Notes": "Register-level evidence for source vendor-document rows.",
        }
    ]
    for group in doc_pkg.deliverable_groups:
        category = group["Category"]
        artifacts.append(
            {
                "Name": f"Vendor document category - {category}",
                "Type": "Vendor Documentation Category Evidence",
                "SourceArtifactID": "",
                "SourceRef": f"{doc_pkg.source_ref}; Vendor Engineering Deliverables table",
                "Notes": "Source vendor-document category carried as evidence under the vendor documentation production unit.",
            }
        )
        for item in group["Items"]:
            artifacts.append(
                {
                    "Name": item["DeliverableName"],
                    "Type": f"Vendor Documentation Evidence - {category}",
                    "SourceArtifactID": item["SourceDeliverableID"],
                    "SourceRef": f"{doc_pkg.source_ref}; Vendor Engineering Deliverables table",
                    "Notes": item["Notes"],
                }
            )
    return artifacts


def make_deliverable_id(package_id: str, seq: int, desc: str) -> str:
    if re.match(r"^PKG-\d{3}$", package_id):
        package_num = package_id.split("-")[1]
    else:
        package_num = "TBD"
    return f"DEL-{package_num}-{seq:02d}_{safe_desc(desc)}"


def append_vendor_deliverables(
    package: PackageRow,
    doc_pkg: DocPackage,
    objective_ids: list[str],
    scope_ids: list[str],
    deliverable_rows: list[dict[str, Any]],
    artifact_rows: list[dict[str, Any]],
    deliverables_by_package: dict[str, list[str]],
    next_seq: int,
) -> int:
    for group in doc_pkg.deliverable_groups:
        category = group["Category"]
        items = group["Items"]
        deliverable_id = make_deliverable_id(package.package_id, next_seq, category)
        next_seq += 1
        artifacts = [f"{item['SourceDeliverableID']} {item['DeliverableName']}" for item in items]
        deliverables_by_package[package.package_id].append(deliverable_id)
        deliverable_rows.append(
            {
                "DeliverableID": deliverable_id,
                "Name": category,
                "ParentPackageID": package.package_id,
                "ParentWorkbookID": package.workbook_id,
                "PackageName": package.name,
                "Description": f"Vendor documentation group '{category}' for {package.name}.",
                "ResponsibleParty": "Package Vendor (engineering/design/equipment and vendor documentation) with EPC Integrator interface/integration review",
                "Type": f"Vendor Documentation - {category}",
                "AnticipatedArtifacts": artifacts,
                "CoversScopeItems": scope_ids,
                "SupportsObjectives": sorted(set(objective_ids + ["OBJ-004"])),
                "SourceRef": f"{doc_pkg.source_ref}; Vendor Engineering Deliverables table",
                "Notes": "Generated by grouping Word-document vendor deliverable rows by category.",
            }
        )
        for item in items:
            artifact_rows.append(
                {
                    "ArtifactID": digest_id("ART", deliverable_id, item["SourceDeliverableID"], item["DeliverableName"]),
                    "Name": item["DeliverableName"],
                    "ParentDeliverableID": deliverable_id,
                    "ParentPackageID": package.package_id,
                    "Type": f"Vendor Documentation - {category}",
                    "SourceArtifactID": item["SourceDeliverableID"],
                    "SourceRef": f"{doc_pkg.source_ref}; Vendor Engineering Deliverables table",
                    "Notes": item["Notes"],
                }
            )
    return next_seq


def assign_scope_deliverables(scope_rows: list[dict[str, Any]], deliverables_by_package: dict[str, list[str]]) -> None:
    for row in scope_rows:
        package_id = row["PackageID"]
        row["DeliverableID(s)"] = deliverables_by_package.get(package_id, [])
        if not row["DeliverableID(s)"]:
            row["OpenIssue"] = "TRUE"


def build_objective_support(deliverable_rows: list[dict[str, Any]]) -> dict[str, list[str]]:
    support: dict[str, list[str]] = defaultdict(list)
    for row in deliverable_rows:
        for objective_id in row["SupportsObjectives"]:
            support[objective_id].append(row["DeliverableID"])
    return {key: sorted(set(value)) for key, value in support.items()}


def build_objective_scope_support(scope_rows: list[dict[str, Any]]) -> dict[str, dict[str, list[str]]]:
    support: dict[str, dict[str, set[str]]] = defaultdict(lambda: {"ScopeItems": set(), "Packages": set()})
    for row in scope_rows:
        objective_ids = [
            objective_id.strip()
            for objective_id in serialize_cell(row.get("ObjectiveID(s)", "")).split(";")
            if objective_id.strip()
        ]
        for objective_id in objective_ids:
            support[objective_id]["ScopeItems"].add(row["ScopeItemID"])
            support[objective_id]["Packages"].add(row["PackageID"])
    return {
        objective_id: {
            "ScopeItems": sorted(values["ScopeItems"]),
            "Packages": sorted(values["Packages"]),
        }
        for objective_id, values in support.items()
    }


def build_telemetry(
    packages: list[PackageRow],
    doc_packages: list[DocPackage],
    doc_match: dict[str, DocPackage],
    package_rows: list[dict[str, Any]],
    scope_rows: list[dict[str, Any]],
    deliverable_rows: list[dict[str, Any]],
    artifact_rows: list[dict[str, Any]],
    open_issues: list[dict[str, Any]],
    objective_rows: list[dict[str, Any]],
    objective_scope_map_rows: list[dict[str, Any]],
    objective_package_map_rows: list[dict[str, Any]],
    objective_deliverable_map_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    issue_counts = Counter(row["IssueType"] for row in open_issues)
    discipline_counts = Counter(package.discipline for package in packages)
    deliverable_type_counts = Counter(row["Type"] for row in deliverable_rows)
    artifact_type_counts = Counter(row["Type"] for row in artifact_rows)
    vendor_package_rows = [row for row in package_rows if row["Discipline"] in {"Electrical", "Mechanical"}]
    accepted_package_ids = [package.package_id for package in packages if re.match(r"^PKG-\d{3}$", package.package_id)]
    missing_package_ids = [package for package in packages if package.package_id == "TBD_PENDING_ID"]
    invalid_deliverable_ids = [
        row["DeliverableID"]
        for row in deliverable_rows
        if not valid_deliverable_id(row["DeliverableID"], row["ParentPackageID"])
    ]
    unassigned_scope = [
        row["ScopeItemID"]
        for row in scope_rows
        if row["InOutStatus"] == "IN" and not re.match(r"^PKG-\d{3}$", row["PackageID"])
    ]
    scope_without_deliverables = [
        row["ScopeItemID"]
        for row in scope_rows
        if row["InOutStatus"] == "IN" and not row["DeliverableID(s)"]
    ]
    unmapped_objectives = [
        row["ObjectiveID"]
        for row in objective_rows
        if row["OpenIssue"] == "TRUE"
    ]
    workbook_duplicate_tracking = {
        tracking: len(rows)
        for tracking, rows in group_by([package for package in packages if package.tracking], lambda package: package.tracking).items()
        if len(rows) > 1
    }
    mandatory_epc_anchor_names = {"Scope of Work", "Package Datasheet", "Construction Work Package"}
    deliverable_names_by_package: dict[str, set[str]] = defaultdict(set)
    for row in deliverable_rows:
        deliverable_names_by_package[row["ParentPackageID"]].add(row["Name"])
    mandatory_epc_anchors_present = all(
        mandatory_epc_anchor_names <= deliverable_names_by_package[package.package_id]
        for package in packages
    )
    mandatory_epc_anchor_counts = {
        anchor_name: sum(1 for row in deliverable_rows if row["Name"] == anchor_name)
        for anchor_name in sorted(mandatory_epc_anchor_names)
    }
    return {
        "Revision": REVISION,
        "GeneratedOn": GENERATED_ON,
        "Status": "FINAL_PUBLISHED"
        if not any(row["Severity"] == "BLOCKER" for row in open_issues)
        else "DRAFT_WITH_BLOCKERS",
        "GateStatus": {
            "Gate1Intake": f"APPROVED {GATE1_APPROVAL_DATE}",
            "Gate2SSOWVocabulary": f"APPROVED {GATE2_APPROVAL_DATE}",
            "Gate3Objectives": f"APPROVED {GATE3_APPROVAL_DATE}",
            "Gate4Packages": f"APPROVED {GATE4_APPROVAL_DATE}",
            "Gate5Deliverables": f"APPROVED {GATE5_APPROVAL_DATE}",
            "Gate6Coverage": f"APPROVED {GATE6_APPROVAL_DATE}",
            "Gate7Publish": f"APPROVED {GATE7_APPROVAL_DATE}",
        },
        "AcceptedGateSnapshots": [
            f"_GateSnapshots/{GATE1_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE2_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE3_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE4_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE5_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE6_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
            f"_GateSnapshots/{GATE7_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md",
        ],
        "PackageRole": "coverage telemetry",
        "ScopeItemCount": len(scope_rows),
        "PackageCount": len(package_rows),
        "AcceptedPackageIDCount": len(accepted_package_ids),
        "DeliverableCount": len(deliverable_rows),
        "ArtifactCount": len(artifact_rows),
        "DeliverableTypeCounts": dict(sorted(deliverable_type_counts.items())),
        "MandatoryEPCAnchorDeliverableCounts": mandatory_epc_anchor_counts,
        "ArtifactTypeCounts": dict(sorted(artifact_type_counts.items())),
        "ObjectiveCount": len(OBJECTIVES),
        "ObjectiveScopeMapRowCount": len(objective_scope_map_rows),
        "ObjectivePackageMapRowCount": len(objective_package_map_rows),
        "ObjectiveDeliverableMapRowCount": len(objective_deliverable_map_rows),
        "WorkbookPackageRowCount": len(packages),
        "ElectricalMechanicalVendorPackageCount": len(vendor_package_rows),
        "WorkbookDisciplineCounts": dict(sorted(discipline_counts.items())),
        "WorkbookMissingIDRows": [
            {"WorkbookRow": package.row, "PackageName": package.name, "Tracking": package.tracking}
            for package in missing_package_ids
        ],
        "WorkbookDuplicateTrackingNumbers": workbook_duplicate_tracking,
        "DocxPackageSectionCount": len(doc_packages),
        "DocxMatchedPackageSectionCount": len(doc_match),
        "DocxUnmatchedPackageSectionCount": len(doc_packages) - len(doc_match),
        "UnassignedScopeItems": len(unassigned_scope),
        "UnassignedScopeItemIDs": unassigned_scope,
        "ScopeItemsWithoutDeliverableMapping": len(scope_without_deliverables),
        "ScopeItemsWithoutDeliverableMappingIDs": scope_without_deliverables,
        "InvalidDeliverableIDs": invalid_deliverable_ids,
        "UnmappedObjectives": len(unmapped_objectives),
        "UnmappedObjectiveIDs": unmapped_objectives,
        "OpenIssueCount": len(open_issues),
        "BlockingOpenIssueCount": sum(1 for row in open_issues if row["Severity"] == "BLOCKER"),
        "OpenIssuesByType": dict(sorted(issue_counts.items())),
        "Validation": {
            "WorkbookRowCountIs105": len(packages) == 105,
            "DisciplineCountsMatchPlan": dict(sorted(discipline_counts.items()))
            == {
                "Civil": 7,
                "Controls": 3,
                "Electrical": 33,
                "Instrumentation": 3,
                "Mechanical": 54,
                "Structural": 5,
            },
            "NoMissingPackageIDs": not missing_package_ids,
            "AcceptedPackageIDsValid": len(accepted_package_ids) == len(packages),
            "ElectricalMechanicalResponsibilityModelRecorded": all(
                "Package Vendor owns package engineering" in row["ResponsibilityModel"]
                and "EPC Integrator owns integration" in row["ResponsibilityModel"]
                for row in vendor_package_rows
            ),
            "DeliverableIDsValidExceptBlockedTBD": not invalid_deliverable_ids,
            "MandatoryEPCAnchorsPresent": mandatory_epc_anchors_present
            and all(count == len(packages) for count in mandatory_epc_anchor_counts.values()),
            "DeliverablesReframedAsProductionUnits": set(deliverable_type_counts)
            <= {
                "EPC Scope of Work",
                "EPC Package Datasheet",
                "EPC Construction Work Package",
                "Vendor Package Production Unit",
                "Vendor Document Turnover",
                "EPC Vendor Package Acceptance",
                "EPC/Discipline Production Unit",
            },
            "InterfaceFactsCarriedAsArtifacts": any(row["Type"] == "Interface Fact Evidence" for row in artifact_rows)
            and not any(row["Type"] == "EPC Interface Control" for row in deliverable_rows),
            "VendorDocumentsGroupedAsTurnoverDeliverables": deliverable_type_counts["Vendor Document Turnover"]
            == len(vendor_package_rows)
            and not any(row["Type"].startswith("Vendor Documentation - ") for row in deliverable_rows),
            "ObjectiveRegisterRowsConcise": all(
                "MappedScopeItems" not in row
                and "MappedPackages" not in row
                and "MappedDeliverables" not in row
                for row in objective_rows
            ),
            "ObjectiveScopeMappingsPresent": all(int(row.get("MappedScopeItemCount", 0)) > 0 for row in objective_rows),
            "ObjectivePackageMappingsPresent": all(int(row.get("MappedPackageCount", 0)) > 0 for row in objective_rows),
            "ObjectiveDeliverableMappingsPresent": all(int(row.get("MappedDeliverableCount", 0)) > 0 for row in objective_rows),
            "ObjectiveMappingRowsPresent": bool(
                objective_scope_map_rows and objective_package_map_rows and objective_deliverable_map_rows
            ),
            "ObjectiveCountsMatchMappingRows": sum(int(row.get("MappedScopeItemCount", 0)) for row in objective_rows)
            == len(objective_scope_map_rows)
            and sum(int(row.get("MappedPackageCount", 0)) for row in objective_rows) == len(objective_package_map_rows)
            and sum(int(row.get("MappedDeliverableCount", 0)) for row in objective_rows)
            == len(objective_deliverable_map_rows),
            "ObjectiveReviewFieldsPresent": all(row.get("ReviewFocus") for row in objective_rows),
            "ObjectiveDefinitionFieldsPresent": all(
                row.get("DerivedSourceIntent")
                and row.get("TestCriteria")
                and row.get("ExpectedEvidence")
                and row.get("MappingBasis")
                for row in objective_rows
            ),
            "AllScopeHasObjectiveMapping": all(row.get("ObjectiveID(s)") for row in scope_rows),
            "AllScopeHasPackageOrOpenIssue": all(
                re.match(r"^PKG-\d{3}$", row["PackageID"]) or row["OpenIssue"] == "TRUE"
                for row in scope_rows
                if row["InOutStatus"] == "IN"
            ),
            "AllScopeHasDeliverableMapping": not scope_without_deliverables,
            "AllObjectivesMapped": not unmapped_objectives,
            "BothDBMsCited": DBM_COMP_PATH.exists() and DBM_DEEPCUT_PATH.exists(),
            "DocxSectionsAccountedFor": len(doc_packages) == 52,
        },
    }


def valid_deliverable_id(deliverable_id: str, package_id: str) -> bool:
    if not re.match(r"^PKG-\d{3}$", package_id):
        return deliverable_id.startswith("DEL-TBD-")
    package_num = package_id.split("-")[1]
    return bool(re.match(rf"^DEL-{package_num}-\d{{2}}_[a-z0-9][a-z0-9-]*$", deliverable_id))


def group_by(items: list[Any], key_func: Any) -> dict[str, list[Any]]:
    grouped: dict[str, list[Any]] = defaultdict(list)
    for item in items:
        grouped[key_func(item)].append(item)
    return grouped


def write_registers(
    package_rows: list[dict[str, Any]],
    scope_rows: list[dict[str, Any]],
    deliverable_rows: list[dict[str, Any]],
    artifact_rows: list[dict[str, Any]],
    interface_rows: list[dict[str, Any]],
    objective_rows: list[dict[str, Any]],
    objective_scope_map_rows: list[dict[str, Any]],
    objective_package_map_rows: list[dict[str, Any]],
    objective_deliverable_map_rows: list[dict[str, Any]],
    vocabulary_rows: list[dict[str, Any]],
    open_issues: list[dict[str, Any]],
    telemetry: dict[str, Any],
) -> None:
    write_csv(
        OUTPUT_ROOT / "PACKAGE_REGISTER.csv",
        [
            "PackageID",
            "WorkbookID",
            "WorkbookRow",
            "WBS",
            "CoATrackingNumber",
            "NormalizedTrackingNumber",
            "Name",
            "Discipline",
            "ResponsibilityModel",
            "ScopeDescription",
            "InclusionCriteria",
            "Exclusions",
            "InterfaceTypes",
            "InterfaceReviewNotes",
            "SourceRefs",
            "DocxPackageMatched",
            "DocxPackageHeading",
            "SupportsObjectives",
            "OpenIssue",
            "PackageRole",
        ],
        package_rows,
    )
    write_csv(
        OUTPUT_ROOT / "SCOPE_LEDGER.csv",
        [
            "ScopeItemID",
            "InOutStatus",
            "ScopeItemStatement",
            "SourceRef",
            "PackageID",
            "DeliverableID(s)",
            "ObjectiveID(s)",
            "DecisionRef",
            "OpenIssue",
            "Notes",
        ],
        scope_rows,
    )
    write_csv(
        OUTPUT_ROOT / "DELIVERABLE_REGISTER.csv",
        [
            "DeliverableID",
            "Name",
            "ParentPackageID",
            "ParentWorkbookID",
            "PackageName",
            "Description",
            "ResponsibleParty",
            "Type",
            "AnticipatedArtifacts",
            "CoversScopeItems",
            "SupportsObjectives",
            "SourceRef",
            "Notes",
        ],
        deliverable_rows,
    )
    write_csv(
        OUTPUT_ROOT / "ARTIFACT_REGISTER.csv",
        [
            "ArtifactID",
            "Name",
            "ParentDeliverableID",
            "ParentPackageID",
            "Type",
            "SourceArtifactID",
            "SourceRef",
            "Notes",
        ],
        artifact_rows,
    )
    write_csv(
        OUTPUT_ROOT / "INTERFACE_REGISTER.csv",
        [
            "InterfaceID",
            "PackageID",
            "WorkbookID",
            "WorkbookRow",
            "PackageName",
            "Discipline",
            "InterfaceType",
            "Applicability",
            "SourceRef",
            "Notes",
        ],
        interface_rows,
    )
    write_csv(
        OUTPUT_ROOT / "OBJECTIVE_REGISTER.csv",
        [
            "ObjectiveID",
            "Statement",
            "SourceRef",
            "DerivedSourceIntent",
            "TestCriteria",
            "ExpectedEvidence",
            "MappingBasis",
            "Notes",
            "ReviewFocus",
            "MappedScopeItemCount",
            "MappedPackageCount",
            "MappedDeliverableCount",
            "OpenIssue",
        ],
        objective_rows,
    )
    write_csv(
        OUTPUT_ROOT / "OBJECTIVE_SCOPE_MAP.csv",
        ["ObjectiveID", "ScopeItemID", "PackageID", "SourceRef", "OpenIssue"],
        objective_scope_map_rows,
    )
    write_csv(
        OUTPUT_ROOT / "OBJECTIVE_PACKAGE_MAP.csv",
        ["ObjectiveID", "PackageID", "WorkbookID", "WorkbookRow", "PackageName", "Discipline", "WBS", "SourceRefs"],
        objective_package_map_rows,
    )
    write_csv(
        OUTPUT_ROOT / "OBJECTIVE_DELIVERABLE_MAP.csv",
        [
            "ObjectiveID",
            "DeliverableID",
            "ParentPackageID",
            "PackageName",
            "DeliverableName",
            "Type",
            "ResponsibleParty",
            "SourceRef",
        ],
        objective_deliverable_map_rows,
    )
    write_csv(
        OUTPUT_ROOT / "VOCABULARY_MAP.csv",
        ["CanonicalTerm", "Synonyms", "Notes"],
        vocabulary_rows,
    )
    write_csv(
        OUTPUT_ROOT / "OPEN_ISSUES.csv",
        ["IssueID", "Severity", "IssueType", "Gate", "RelatedID", "Statement", "SourceRef", "RequiredAction", "Status"],
        open_issues,
    )
    (OUTPUT_ROOT / "COVERAGE_TELEMETRY.json").write_text(
        json.dumps(telemetry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def write_main_doc(
    package_rows: list[dict[str, Any]],
    deliverable_rows: list[dict[str, Any]],
    scope_rows: list[dict[str, Any]],
    open_issues: list[dict[str, Any]],
    objective_rows: list[dict[str, Any]],
    telemetry: dict[str, Any],
    dbm_refs: dict[str, list[str]],
) -> None:
    discipline_counts = telemetry["WorkbookDisciplineCounts"]
    open_issue_counts = telemetry["OpenIssuesByType"]
    blocker_count = telemetry["BlockingOpenIssueCount"]
    lines: list[str] = [
        "---",
        "doc_id: WEST-DOE-COMBINED-PROJECT-DECOMP",
        "package_role: working_surface",
        "doc_kind: decomposition.project",
        "status: gate4_approved_pending_gate5_review",
        f"revision: {REVISION}",
        f"created: {GENERATED_ON}",
        "governed_by:",
        "  - AGENT_PROJECT_DECOMP.md",
        "  - AGENT_DECOMP_BASE.md",
        "---",
        "",
        "# PROJECT_DECOMP — West Doe Combined",
        "",
        "## 1. Intake Summary",
        "",
        "This PROJECT_DECOMP working package decomposes the West Doe Combined source corpus into a flat package register, scope ledger, deliverable register, artifact register, interface register, objective register, vocabulary map, open issue register, and coverage telemetry.",
        "",
        "The workbook `26020-Packages_Interfaces_4_export.xlsx` is the authoritative package breakdown. Package rows are not merged when package names or CoA tracking numbers repeat. The Word package requirements document supplies detailed process mechanical equipment scope and vendor-documentation requirements where its package sections can be matched to workbook rows. The two DBM folders are integral design-basis sources for objectives, boundaries, and source context.",
        "",
        "Responsibility model clarified before Gate 1 acceptance: each electrical and mechanical package is treated as a vendor-owned package. The Package Vendor is responsible for that package's engineering, design, vendor documentation, and physical equipment package. The central EPC company is treated as the EPC Integrator responsible for integrating all vendor packages into a functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.",
        "",
        "## 2. Gate Status",
        "",
        "| Gate | Status | Notes |",
        "|---|---|---|",
        f"| Gate 1 — Intake | APPROVED ({GATE1_APPROVAL_DATE}) | User approved intake understanding, source authority order, vendor/EPC responsibility split, and Yard Lighting ID resolution. |",
        f"| Gate 2 — SSOW + Vocabulary | APPROVED ({GATE2_APPROVAL_DATE}) | User approved the generated scope ledger and vocabulary map as-is. |",
        f"| Gate 3 — Objectives | APPROVED ({GATE3_APPROVAL_DATE}) | User approved the EPC-integrator-centric objective set as the Gate 3 basis. |",
        f"| Gate 4 — Packages | APPROVED ({GATE4_APPROVAL_DATE}) | User approved the workbook-locked flat package partition. |",
        f"| Gate 5 — Deliverables | APPROVED ({GATE5_APPROVAL_DATE}) | User approved the deliverable basis with mandatory EPC anchors, vendor production units, vendor document turnover grouping, and interface facts carried as artifacts/evidence. |",
        f"| Gate 6 — Coverage | APPROVED ({GATE6_APPROVAL_DATE}) | User approved coverage after Gate 6 source dispositions closed the prior non-blocking open issues. |",
        f"| Gate 7 — Publish | APPROVED ({GATE7_APPROVAL_DATE}) | Final decomposition package accepted and published as downstream basis. |",
        "",
        "## 3. Companion Inventory",
        "",
        "| Artifact | Role | Authority |",
        "|---|---|---|",
        "| `PROJECT_DECOMP.md` | working surface | Human-facing control surface. |",
        "| `PACKAGE_REGISTER.csv` | authoritative companion register | Authoritative package rows derived from the workbook. |",
        "| `SCOPE_LEDGER.csv` | authoritative companion register | Authoritative scope-item mapping and coverage ledger. |",
        "| `DELIVERABLE_REGISTER.csv` | authoritative companion register | Authoritative deliverable rows. |",
        "| `ARTIFACT_REGISTER.csv` | authoritative companion register | Anticipated artifact instances under deliverables. |",
        "| `INTERFACE_REGISTER.csv` | authoritative companion register | Workbook interface facts. |",
        "| `OBJECTIVE_REGISTER.csv` | authoritative companion register | Approved objective statements, review focus, evidence basis, and traceability counts. |",
        "| `OBJECTIVE_SCOPE_MAP.csv` | authoritative companion register | Objective-to-scope traceability rows. |",
        "| `OBJECTIVE_PACKAGE_MAP.csv` | authoritative companion register | Objective-to-package traceability rows. |",
        "| `OBJECTIVE_DELIVERABLE_MAP.csv` | authoritative companion register | Objective-to-deliverable traceability rows. |",
        "| `VOCABULARY_MAP.csv` | authoritative companion register | Canonical term map. |",
        "| `OPEN_ISSUES.csv` | authoritative companion register | Open issue register. |",
        "| `COVERAGE_TELEMETRY.json` | authoritative companion register | Machine-readable coverage and validation summary. |",
        "| `VALIDATION_REPORT.md` | snapshot / handoff artifact | Generated validation summary for this run. |",
        f"| `_GateSnapshots/{GATE1_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 1 approval snapshot. |",
        f"| `_GateSnapshots/{GATE2_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 2 approval snapshot. |",
        f"| `_GateSnapshots/{GATE3_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 3 approval snapshot. |",
        f"| `_GateSnapshots/{GATE4_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 4 approval snapshot. |",
        f"| `_GateSnapshots/{GATE5_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 5 approval snapshot. |",
        f"| `_GateSnapshots/{GATE6_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 6 approval snapshot. |",
        f"| `_GateSnapshots/{GATE7_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` | snapshot / handoff artifact | Immutable Gate 7 final published snapshot. |",
        "",
        "## 4. References",
        "",
        "| RefID | Source | Role | Notes |",
        "|---|---|---|---|",
        "| SRC-001 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` | Authoritative package register | One `Packages` sheet; package rows and interface `X` columns are authoritative. |",
        "| SRC-002 | `_Sources/26020-Package_Requirements.docx` | Detailed process mechanical package scope | 52 package sections and vendor-documentation tables. |",
        "| SRC-003 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Integral DBM source | 3-25 compression and liquids design basis. |",
        "| SRC-004 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Integral DBM source | 4-25 Deepcut design basis. |",
        "",
        "## 5. Gate 3 Accepted Basis — Objectives",
        "",
        f"Gate 3 was approved on {GATE3_APPROVAL_DATE}. The accepted objective set is EPC-integrator-centric: it uses facility/process outcomes, vendor package obligations, and EPC integration controls as decomposition success criteria. The objective set below is derived from the accepted Gate 2 scope ledger, the workbook package breakdown, the DBMs, the package requirements document, and the accepted vendor/EPC responsibility clarification.",
        "",
        "| ObjectiveID | Success Criterion | Derived Source Intent | Test Criteria | Scope Items | Packages | Deliverables | Gate 3 Review Focus |",
        "|---|---|---|---|---:|---:|---:|---|",
    ]
    for objective in objective_rows:
        scope_count = objective["MappedScopeItemCount"]
        package_count = objective["MappedPackageCount"]
        deliverable_count = objective["MappedDeliverableCount"]
        lines.append(
            f"| {objective['ObjectiveID']} | {objective['Statement']} | {objective['DerivedSourceIntent']} | "
            f"{objective['TestCriteria']} | {scope_count} | {package_count} | {deliverable_count} | "
            f"{objective['ReviewFocus']} |"
        )
    lines.extend(
        [
            "",
            "Objective source references, expected downstream evidence, and mapping basis live in `OBJECTIVE_REGISTER.csv`. Row-level traceability lives in `OBJECTIVE_SCOPE_MAP.csv`, `OBJECTIVE_PACKAGE_MAP.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.",
            "",
            "Not included as standalone objectives: package-ID hygiene, workbook-authority policy, duplicate-row preservation, open-issue bookkeeping, and register maintenance. Those remain required decisions, invariants, or telemetry controls, but they are not Gate 3 success criteria.",
        ]
    )

    lines.extend(
        [
            "",
            "## 6. Gate 4 Accepted Basis — Package Partition",
            "",
            f"Gate 4 was approved on {GATE4_APPROVAL_DATE}. The accepted flat package partition is not inferred: it is locked to the `26020-Packages_Interfaces_4_export.xlsx` workbook package rows.",
            "",
            "The approved Gate 4 basis confirms:",
            "",
            "- the 105 workbook package rows remain the authoritative flat package list;",
            "- package IDs use workbook `ID #` as `PKG-XXX`, including `Yard Lighting` as `PKG-106`;",
            "- duplicate package names and repeated CoA tracking numbers remain separate where the workbook gives separate rows;",
            "- design package assignments remain discipline-exclusive according to the workbook discipline column;",
            "- workbook interface `X` columns remain interface facts, not separate packages;",
            "- each `IN` scope item maps to exactly one `PackageID` in `SCOPE_LEDGER.csv`;",
            "- package responsibility text preserves vendor ownership for electrical/mechanical package engineering, design, vendor documentation, and physical equipment, with EPC Integrator responsibility for facility integration.",
            "",
            "The full package list is authoritative in `PACKAGE_REGISTER.csv`; it is summarized here to keep the main document usable as a control surface.",
            "",
            f"- Package rows: {telemetry['WorkbookPackageRowCount']}",
            f"- Accepted `PKG-XXX` IDs: {telemetry['AcceptedPackageIDCount']}",
            f"- Missing package IDs: {len(telemetry['WorkbookMissingIDRows'])}",
            f"- Electrical/mechanical vendor-owned package rows: {telemetry['ElectricalMechanicalVendorPackageCount']}",
            f"- Discipline counts: {', '.join(f'{key} {value}' for key, value in discipline_counts.items())}",
            "- Package register authority: `PACKAGE_REGISTER.csv`.",
            "",
            "The package list is intentionally not duplicated in full here. `PACKAGE_REGISTER.csv` is the authoritative companion register for package identity, source rows, discipline, WBS, scope description, interface types, and source references.",
            "",
            "## 7. Gate 5 Accepted Basis — Deliverables",
            "",
            f"Gate 5 was approved on {GATE5_APPROVAL_DATE}. The accepted deliverable basis makes the EPC Integrator anchor set mandatory for every approved package: `Scope of Work`, `Package Datasheet`, and `Construction Work Package`. Additional deliverables are then added where needed as vendor package production units, vendor document turnover, EPC acceptance, or source-limited discipline production units. Interface facts and source vendor-document rows are carried mostly as artifacts/evidence.",
            "",
            "The accepted Gate 5 basis confirms:",
            "",
            "- every deliverable belongs to exactly one approved `PackageID`;",
            "- every deliverable ID is mechanically coupled to its parent package as `DEL-XXX-YY_{shortDescription}`;",
            "- every package includes the three mandatory EPC Integrator deliverables: `Scope of Work`, `Package Datasheet`, and `Construction Work Package`;",
            "- package `Scope of Work` deliverables identify tagged equipment where source-supported, explain package function, and describe whole-facility integration;",
            "- package `Package Datasheet` deliverables carry the technical handoff basis required for third-party vendor or discipline package engineering and design;",
            "- package `Construction Work Package` deliverables describe physical installation, construction, tie-in, inspection, and turnover into larger systems;",
            "- electrical and mechanical vendor production units assign package engineering, design, vendor documentation, and physical equipment responsibility to the Package Vendor, with EPC Integrator integration review;",
            "- vendor-document turnover is a single deliverable where needed; Word-document vendor-document rows are artifacts under `Vendor Document Turnover Package`, not separate deliverables;",
            "- workbook interface `X` facts are artifacts/evidence under the package `Package Datasheet`, not separate deliverables;",
            "- non-mechanical detailed requirements are not invented; source-limited deliverables remain `TBD` and open issues identify what must be resolved;",
            "- `CoversScopeItems` and `SupportsObjectives` mappings are acceptable as best-effort Gate 5 mappings.",
            "",
            f"- Deliverables: {telemetry['DeliverableCount']}",
            f"- Artifacts: {telemetry['ArtifactCount']}",
            "- Mandatory EPC anchor counts: "
            + ", ".join(f"{key}={value}" for key, value in telemetry["MandatoryEPCAnchorDeliverableCounts"].items())
            + ".",
            "- Deliverable type counts: "
            + ", ".join(f"{key}={value}" for key, value in telemetry["DeliverableTypeCounts"].items())
            + ".",
            "- Artifact type counts are in `COVERAGE_TELEMETRY.json`; major artifact groups include package scope evidence, datasheet handoff evidence, construction/tie-in evidence, interface fact evidence, vendor-document evidence, EPC review evidence, and source-gap evidence.",
            "- Non-mechanical package detail is carried conservatively from workbook and DBM sources, with open issues where discipline-specific detailed source material is absent.",
            "",
            "## 8. Gate 6 Accepted Basis — Coverage & Telemetry",
            "",
            f"Gate 6 was approved on {GATE6_APPROVAL_DATE}. The accepted coverage basis confirms package, scope, objective, deliverable, artifact, and source coverage is complete enough to serve as downstream basis, with the prior non-blocking issue set resolved by source dispositions.",
            "",
            "The accepted Gate 6 basis confirms:",
            "",
            "- every `IN` scope item maps to exactly one approved package and at least one approved deliverable;",
            "- every approved objective maps to downstream deliverables or is explicitly carried as an open issue;",
            "- every deliverable belongs to exactly one approved package and uses a valid mechanically coupled `DEL-XXX-YY_{shortDescription}` ID;",
            "- mandatory EPC anchor deliverables are present for all 105 packages;",
            "- interface facts are preserved as artifacts/evidence and not promoted to packages or standalone deliverables;",
            "- vendor-document rows are grouped as artifacts/evidence under package-level vendor document turnover deliverables;",
            "- Gate 6 issue dispositions are correctly recorded in package source references, interface evidence, and Word-section mappings.",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| ScopeItemCount | {telemetry['ScopeItemCount']} |",
            f"| PackageCount | {telemetry['PackageCount']} |",
            f"| DeliverableCount | {telemetry['DeliverableCount']} |",
            f"| ObjectiveCount | {telemetry['ObjectiveCount']} |",
            f"| UnassignedScopeItems | {telemetry['UnassignedScopeItems']} |",
            f"| ScopeItemsWithoutDeliverableMapping | {telemetry['ScopeItemsWithoutDeliverableMapping']} |",
            f"| UnmappedObjectives | {telemetry['UnmappedObjectives']} |",
            f"| OpenIssueCount | {telemetry['OpenIssueCount']} |",
            f"| BlockingOpenIssueCount | {blocker_count} |",
            "",
            "Open issue counts by type: "
            + (", ".join(f"{key}={value}" for key, value in open_issue_counts.items()) or "none")
            + ".",
            "",
            "## 9. Open Issues",
            "",
            "Gate 6 source review resolved the prior non-blocking issue set. Non-mechanical detailed-package warnings are accepted as source-limited package basis supported by workbook and DBM discipline sections. Instrumentation support/power/comms notes, pipe-rack responsibility, platform tie-ins, and the mechanical package remappings are recorded as Gate 6 dispositions. The live open issue register is now empty unless new source changes introduce new blockers.",
            "",
            "| Issue Type | Count | Gate Focus | Review Note |",
            "|---|---:|---|---|",
        ]
    )
    issue_focus = {
        "INTERFACE_NOTE_CONFIRMATION": ("Gate 6 / Gate 7", "Confirm workbook interface notes before final coverage acceptance or carry as explicit handoff conditions."),
        "MISSING_DETAILED_PACKAGE_REQUIREMENTS": ("Gate 6 / Gate 7", "Non-mechanical and unmatched package details remain source-limited; accept as handoff conditions or provide additional source material."),
        "UNMATCHED_WORD_PACKAGE_SECTION": ("Gate 6 / Gate 7", "Resolve whether Word package sections are superseded, renamed, manually mapped, or accepted as handoff conditions."),
    }
    for issue_type, count in open_issue_counts.items():
        gate_focus, note = issue_focus.get(issue_type, ("TBD", "See `OPEN_ISSUES.csv`."))
        lines.append(f"| {issue_type} | {count} | {gate_focus} | {note} |")
    lines.append(f"| All open issues | {len(open_issues)} | See register | Full details are authoritative in `OPEN_ISSUES.csv`. |")

    lines.extend(
        [
            "",
            "## 10. Gate 7 Accepted Basis — Final Publication",
            "",
            f"Gate 7 was accepted on {GATE7_APPROVAL_DATE}. The PROJECT_DECOMP package is final-published as downstream basis for subsequent project workflows.",
            "",
            "The final published basis confirms:",
            "",
            "- Gates 1 through 6 have immutable accepted snapshots;",
            "- package partition, scope ledger, objectives, deliverables, artifacts, interfaces, vocabulary, open issues, coverage telemetry, and validation are published together as one governed decomposition package;",
            "- validation passes with zero blocking issues and zero open issues;",
            "- downstream agents should consume the Gate 7 final published snapshot as the accepted decomposition truth, not mutable working state alone;",
            "- source documents remain upstream source truth and this package remains the accepted decomposition-state derivative of those sources.",
        ]
    )

    lines.extend(
        [
            "",
            "## 11. Decision Log",
            "",
            "| DecisionRef | Decision | Source |",
            "|---|---|---|",
            "| DEC-001 | Workbook package rows are authoritative and are not merged by name or repeated CoA tracking number. | User instruction; `26020-Packages_Interfaces_4_export.xlsx` |",
            "| DEC-002 | Workbook `ID #` is used as `PKG-XXX`; the initially missing Yard Lighting ID was resolved as workbook ID 106 / `PKG-106`. | User-selected implementation policy and source workbook update |",
            "| DEC-003 | Interface `X` columns are represented as interface facts in `INTERFACE_REGISTER.csv`, not as separate packages. | User instruction; PROJECT_DECOMP flat-package invariant |",
            "| DEC-004 | Word vendor-document rows are represented as artifacts under a package-level vendor document turnover deliverable rather than as standalone deliverables. | PROJECT_DECOMP design-deliverable granularity rule; Gate 5 user direction |",
            "| DEC-005 | Non-mechanical detail is not invented; where detailed source material is absent, deliverables are marked TBD and open issues are recorded. | No-invention invariant |",
            "| DEC-006 | Electrical and mechanical packages are vendor-owned for package engineering, design, vendor documentation, and physical equipment; the central EPC company owns integration into the full process facility. | Human Gate 1 clarification |",
            f"| DEC-007 | Gate 1 intake understanding is approved; proceed to Gate 2 SSOW and Vocabulary review. | Human Gate 1 approval on {GATE1_APPROVAL_DATE} |",
            f"| DEC-008 | Gate 2 SSOW and Vocabulary are approved as-is; proceed to Gate 3 Objectives review. | Human Gate 2 approval on {GATE2_APPROVAL_DATE} |",
            "| DEC-009 | Gate 3 objectives were rebuilt before Gate 3 approval to function as source-derived, testable decomposition success criteria rather than broad umbrella labels or internal register controls. | PROJECT_DECOMP reassessment before Gate 3 acceptance |",
            f"| DEC-010 | Gate 3 objectives are approved; proceed to Gate 4 package partition review using the workbook package breakdown as the authoritative flat package list. | Human Gate 3 approval on {GATE3_APPROVAL_DATE} |",
            f"| DEC-011 | Gate 4 package partition is approved; proceed to Gate 5 deliverable review using the approved workbook-locked package list as the parent partition basis. | Human Gate 4 approval on {GATE4_APPROVAL_DATE} |",
            "| DEC-012 | Gate 5 deliverables were reframed so deliverable rows represent EPC-integrator production units or vendor package production units; interface facts and source vendor-document rows are carried primarily as artifacts/evidence. | Gate 5 second review pass |",
            "| DEC-013 | Every approved package must include EPC Integrator `Scope of Work`, `Package Datasheet`, and `Construction Work Package` deliverables before additional vendor or discipline production deliverables are added. | Human Gate 5 direction on 2026-05-24 |",
            f"| DEC-014 | Gate 5 deliverables are approved; proceed to Gate 6 coverage review using the accepted package and deliverable basis. | Human Gate 5 approval on {GATE5_APPROVAL_DATE} |",
            "| DEC-015 | Gate 6 issue dispositions close the prior 67 non-blocking open issues: non-Word disciplines are accepted as source-limited workbook/DBM basis; instrumentation plug-n-play interfaces are included by package as appropriate; pipe-rack design and platform-to-equipment tie-ins are EPC Integrator responsibilities; Cryogenic Deep Cut, LPG Booster, and Tank Farm Pump Word sections are manually mapped; Methanol Injection and Gas Mole Sieve scope are included with the Cryogenic Unit while NGL Mole Sieve remains distinct. | Human Gate 6 direction on 2026-05-24 plus source cross-check |",
            f"| DEC-016 | Gate 6 coverage is approved; proceed to Gate 7 final publish review using the accepted Gate 1 through Gate 6 snapshots as upstream basis. | Human Gate 6 approval on {GATE6_APPROVAL_DATE} |",
            f"| DEC-017 | Gate 7 final publish is accepted; PROJECT_DECOMP is final-published as downstream basis. | Human Gate 7 approval on {GATE7_APPROVAL_DATE} |",
            "",
            "## 12. DBM Section Coverage Notes",
            "",
            "The DBMs were ingested as design-basis sources and cited by WBS grouping. Representative top-level sections discovered:",
            "",
            "| DBM | Top-level section count | First sections |",
            "|---|---:|---|",
        ]
    )
    for label, headings in dbm_refs.items():
        preview = "; ".join(headings[:5])
        lines.append(f"| {label} | {len(headings)} | {preview} |")

    lines.extend(
        [
            "",
            "## 13. Handoff State",
            "",
            f"- Accepted upstream snapshots: `_GateSnapshots/{GATE1_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, `_GateSnapshots/{GATE2_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, `_GateSnapshots/{GATE3_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, `_GateSnapshots/{GATE4_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, `_GateSnapshots/{GATE5_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, `_GateSnapshots/{GATE6_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md`, and `_GateSnapshots/{GATE7_SNAPSHOT_DIRNAME}/Snapshot_Manifest.md` record the accepted Gate 1 through Gate 7 basis.",
            "- Derivative-package status: Gate 1 through Gate 7 snapshots are accepted decomposition-state records. The source documents remain upstream source truth.",
            "- Closure verdict: Gates 1-7 closed; PROJECT_DECOMP is final-published.",
            "- Rerun requirements: rerun `scripts/build_project_decomp.py` after workbook ID correction, package source additions, or human disposition of open issues.",
            f"- Remaining blockers: {first_blocker_id(open_issues)}.",
            "",
        ]
    )
    (OUTPUT_ROOT / "PROJECT_DECOMP.md").write_text("\n".join(lines), encoding="utf-8")


def first_blocker_id(open_issues: list[dict[str, Any]]) -> str:
    for issue_row in open_issues:
        if issue_row["Severity"] == "BLOCKER":
            return issue_row["IssueID"]
    return "none"


def write_validation_report(telemetry: dict[str, Any], open_issues: list[dict[str, Any]]) -> None:
    validations = telemetry["Validation"]
    lines = [
        "# PROJECT_DECOMP Validation Report — West Doe Combined",
        "",
        f"Generated: {GENERATED_ON}",
        "",
        "## Result",
        "",
        "PASS_WITH_BLOCKERS" if all(validations.values()) and telemetry["BlockingOpenIssueCount"] else "PASS" if all(validations.values()) else "FAIL",
        "",
        "## Checks",
        "",
        "| Check | Result |",
        "|---|---|",
    ]
    for key, value in validations.items():
        lines.append(f"| {key} | {'PASS' if value else 'FAIL'} |")
    lines.extend(
        [
            "",
            "## Blocking Issues",
            "",
            "| IssueID | Type | RelatedID | Statement |",
            "|---|---|---|---|",
        ]
    )
    blockers = [issue for issue in open_issues if issue["Severity"] == "BLOCKER"]
    if blockers:
        for issue_row in blockers:
            lines.append(f"| {issue_row['IssueID']} | {issue_row['IssueType']} | {issue_row['RelatedID']} | {issue_row['Statement']} |")
    else:
        lines.append("| none | none | none | none |")
    lines.append("")
    (OUTPUT_ROOT / "VALIDATION_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    build_outputs()
