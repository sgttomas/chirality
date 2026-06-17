# Source Pack: SRC-CODE-TOOLS

Grouping: `GROUPED_CODE`  RepoGlob: `tools/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: tools/REGISTRY.md

### Tool Registry

| Name | Category | Language | Purpose | Inputs | Outputs |
|------|----------|----------|---------|--------|---------|
| `list_deliverable_status` | coordination | Python 3 | Read-only discovery of deliverable-local `_STATUS.md` lifecycle values with optional DAG node context | `execution/PKG-*/1_Working/DEL-*/_STATUS.md`, `DeliverableNodes.csv`; `--dag`, `--repo-root`, `--format`, optional `--status` | stdout table, CSV, or Markdown; no repo-tracked writes |
| `dependency_type_rectification` | coordination | Python 3 | Canonicalize dependency registers, move candidate rows to non-authoritative worklists, build proposed `DAG-007` from refreshed local registers, consolidate duplicate aggregate edges, and emit after-drift evidence | `--local`, `--dag007`, `--after-drift`, optional `--working-root`, `--today` | Updated local dependency artifacts, `execution/_DAG/DAG-007/`, rectification evidence CSVs |
| `dependency_semantic_refresh_fanin` | coordination | Python 3 | Inventory and validate deliverable-local dependency registers during ORCHESTRATOR semantic refresh fan-in | `--working-root`, `--output-dir`, optional `--label`, `--validate` | Fan-in register inventories, validation results, summary JSON |
| `validate_dependencies_schema` | validation | Python 3 | Validate `Dependencies.csv`/`DependencyEdges.csv` v3.1 shape plus canonical enum and row-rule semantics; `--schema-only` is reserved for historical legacy snapshots | CSV path, optional `--schema-only` | VALID/INVALID report and exit code |

#### Examples

```bash
python3 tools/coordination/list_deliverable_status.py --dag DAG-006 --format table --summary
python3 tools/coordination/list_deliverable_status.py --dag DAG-006 --status IN_PROGRESS --format csv
```

## Component: tools/coordination/dependency_semantic_refresh_fanin.py

    #!/usr/bin/env python3
    """Fan-in helpers for the dependency semantic refresh tranche."""

    from __future__ import annotations

    import argparse
    import csv
    import json
    import subprocess
    from pathlib import Path


    def dependency_registers(working_root: Path) -> list[Path]:
        return sorted(
            path
            for path in (working_root / "execution").rglob("Dependencies.csv")
            if "_run_records" not in path.parts
        )


    def read_rows(path: Path) -> list[dict[str, str]]:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return list(csv.DictReader(handle))


    def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)


    def inventory(working_root: Path, output_dir: Path, label: str) -> dict[str, object]:
        register_rows: list[dict[str, object]] = []
        total_rows = 0
        active_rows = 0
        retired_rows = 0
        candidate_rows = 0
        active_del00_targets = 0

        for path in dependency_registers(working_root):
            rows = read_rows(path)
            counts = {
                "file": str(path.relative_to(working_root)),
                "rows": len(rows),
                "active": 0,
                "retired": 0,
                "candidate": 0,
                "active_del00_targets": 0,
            }
            for row in rows:
                total_rows += 1
                status = row.get("Status", "").strip()
                if status == "ACTIVE":
                    active_rows += 1
                    counts["active"] += 1
                if status == "RETIRED":
                    retired_rows += 1
                    counts["retired"] += 1
                if status == "CANDIDATE":
                    candidate_rows += 1
                    counts["candidate"] += 1
                if status == "ACTIVE" and row.get("TargetDeliverableID", "").startswith("DEL-00-"):
                    active_del00_targets += 1
                    counts["active_del00_targets"] += 1
            register_rows.append(counts)

        write_csv(
            output_dir / f"register_inventory_{label}.csv",
            register_rows,
            ["file", "rows", "active", "retired", "candidate", "active_del00_targets"],
        )

        summary = {
            "dependency_registers": len(register_rows),
            "rows": total_rows,
            "active": active_rows,
            "retired": retired_rows,
            "candidate_status_rows": candidate_rows,
            "active_del00_target_rows": active_del00_targets,
        }
        (output_dir / f"summary_{label}.json").write_text(json.dumps(summary, indent=2) + "\n")
        return summary


    def validate_all(working_root: Path, output_dir: Path) -> int:
        rows: list[dict[str, object]] = []
        failures = 0
        validator = working_root / "tools/validation/validate_dependencies_schema.py"
        for path in dependency_registers(working_root):
            result = subprocess.run(
                ["python3", str(validator), str(path)],
                cwd=working_root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            ok = result.returncode == 0
            if not ok:
                failures += 1
            rows.append(
                {
                    "file": str(path.relative_to(working_root)),
                    "valid": str(ok),
                    "returncode": result.returncode,
                    "output": result.stdout.strip().replace("\n", "\\n"),
                }
            )
        write_csv(output_dir / "validation_results.csv", rows, ["file", "valid", "returncode", "output"])
        return failures


    def main() -> int:
        parser = argparse.ArgumentParser()
        parser.add_argument("--working-root", required=True)
        parser.add_argument("--output-dir", required=True)
        parser.add_argument("--label", default="after")
        parser.add_argument("--validate", action="store_true")
        args = parser.parse_args()

        working_root = Path(args.working_root).resolve()
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        summary = inventory(working_root, output_dir, args.label)
        failures = validate_all(working_root, output_dir) if args.validate else 0
        summary["validation_failures"] = failures
        print(json.dumps(summary, indent=2))
        return 1 if failures else 0


    if __name__ == "__main__":
        raise SystemExit(main())

## Component: tools/coordination/dependency_type_rectification.py

    #!/usr/bin/env python3
    """Canonicalize OpenPipeStress dependency registers and build DAG-007.

    This tool performs deterministic migration work only. It does not decide graph
    topology, promote candidate edges, or update the approved DAG pointer.
    """

    from __future__ import annotations

    import argparse
    import csv
    import json
    import subprocess
    from collections import Counter, defaultdict, deque
    from datetime import date
    from pathlib import Path
    from typing import Iterable


    REQUIRED_COLUMNS = [
        "RegisterSchemaVersion",
        "DependencyID",
        "FromPackageID",
        "FromDeliverableID",
        "FromDeliverableName",
        "DependencyClass",
        "AnchorType",
        "Direction",
        "DependencyType",
        "TargetType",
        "TargetPackageID",
        "TargetDeliverableID",
        "TargetRefID",
        "TargetName",
        "TargetLocation",
        "Statement",
        "EvidenceFile",
        "SourceRef",
        "EvidenceQuote",
        "Explicitness",
        "RequiredMaturity",
        "ProposedMaturity",
        "SatisfactionStatus",
        "Confidence",
        "Origin",
        "FirstSeen",
        "LastSeen",
        "Status",
        "Notes",
    ]

    CANONICAL_DEPENDENCY_TYPES = {
        "PREREQUISITE",
        "INTERFACE",
        "HANDOVER",
        "CONSTRAINT",
        "ENABLES",
        "OTHER",
    }

    BASIS_TYPES = {
        "ARCHITECTURE_BASIS",
        "SOURCE_BASIS",
        "IDENTITY_BASIS",
        "EXPORT_SOURCE_BASIS",
    }

    PREREQUISITE_TYPES = {
        "DOMAIN_MODEL",
        "RESULT_RECORD_MODEL",
        "SOLVER_PREDECESSOR",
        "GOVERNANCE_PREDECESSOR",
        "GUI_PREDECESSOR",
        "INTEROP_PREDECESSOR",
        "LOAD_STRESS_PREDECESSOR",
        "REPORTING_PREDECESSOR",
        "RULE_PACK_PREDECESSOR",
        "SECURITY_PREDECESSOR",
        "VALIDATION_PREDECESSOR",
        "DOCS_PREDECESSOR",
    }

    INTERFACE_TYPES = {
        "ADAPTER_FRAMEWORK",
        "COMPARISON_EXPORT_CONTRACT",
        "COMPONENT_LIBRARY_SCHEMA",
        "DIAGNOSTICS_CONTRACT",
        "EXPORT_CONTRACT",
        "EXPORT_PROFILE",
        "HANDOFF_PACKAGE_CONTRACT",
        "PERSISTENCE_CONTRACT",
        "PHYSICAL_TRANSFORM_CONTRACT",
        "PLUGIN_CONTRACT",
        "RESULT_EXPORT_CONTRACT",
        "RUNNER_CONTRACT",
        "SCHEMA_CONTRACT",
        "SERVICE_API",
        "TARGET_MAPPING_CONTRACT",
        "UNIT_CONTRACT",
    }

    CONSTRAINT_TYPES = {
        "API_PLUGIN_BOUNDARY",
        "BOUNDARY",
        "DATA_BOUNDARY",
        "GUI_GEOMETRY_CONTEXT",
    }

    HANDOVER_TYPES = {
        "CONSUMED_BY",
        "REPORT_INTEGRATION",
    }

    TARGET_TYPE_MAP = {
        "REFERENCE": "DOCUMENT",
        "SCOPE_ITEM": "REQUIREMENT",
    }


    def clean(value: object) -> str:
        return str(value or "").strip()


    def repo_root(start: Path) -> Path:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            text=True,
            capture_output=True,
            check=True,
        )
        return Path(result.stdout.strip())


    def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            return list(reader.fieldnames or []), list(reader)


    def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
            writer.writeheader()
            for row in rows:
                writer.writerow({field: row.get(field, "") for field in fieldnames})


    def append_note(notes: str, *parts: str) -> str:
        existing = clean(notes)
        additions = [part for part in parts if part and part not in existing]
        if not additions:
            return existing
        return "; ".join([item for item in [existing, *additions] if item])


    def canonical_dependency_type(row: dict[str, str]) -> str:
        value = clean(row.get("DependencyType"))
        if clean(row.get("DependencyClass")) == "ANCHOR":
            return "OTHER"
        if value in CANONICAL_DEPENDENCY_TYPES:
            return value
        if value in BASIS_TYPES or value in PREREQUISITE_TYPES or value.endswith("_PREDECESSOR"):
            return "PREREQUISITE"
        if value in INTERFACE_TYPES or value.endswith("_CONTRACT") or value.endswith("_FRAMEWORK") or value.endswith("_PROFILE"):
            return "INTERFACE"
        if value in CONSTRAINT_TYPES:
            return "CONSTRAINT"
        if value in HANDOVER_TYPES:
            return "HANDOVER"
        if value == "TRACEABILITY":
            return "OTHER"
        return "OTHER"


    def canonicalize_row(
        row: dict[str, str],
        *,
        source_file: Path,
        today: str,
        candidate_rows: list[dict[str, str]],
    ) -> dict[str, str]:
        original = {column: clean(row.get(column)) for column in row}
        output = {column: row.get(column, "") for column in row}

        for column in REQUIRED_COLUMNS:
            output.setdefault(column, "")
        output["RegisterSchemaVersion"] = "v3.1"

        legacy_notes: list[str] = []
        for field in [
            "AnchorType",
            "Direction",
            "DependencyType",
            "TargetType",
            "Explicitness",
            "SatisfactionStatus",
            "Origin",
            "Status",
        ]:
            value = clean(original.get(field))
            if value:
                legacy_notes.append(f"legacy_{field.lower()}={value}")

        dependency_class = clean(output.get("DependencyClass"))
        if dependency_class not in {"ANCHOR", "EXECUTION"}:
            dependency_class = "EXECUTION"
            output["DependencyClass"] = dependency_class

        if dependency_class == "ANCHOR":
            output["AnchorType"] = "TRACES_TO_REQUIREMENT" if clean(output.get("AnchorType")) not in {"IMPLEMENTS_NODE", "TRACES_TO_REQUIREMENT"} else clean(output.get("AnchorType"))
            output["DependencyType"] = "OTHER"
            output["Direction"] = "UPSTREAM"
        else:
            output["AnchorType"] = "NOT_APPLICABLE"
            output["DependencyType"] = canonical_dependency_type(output)
            if clean(output.get("Direction")) not in {"UPSTREAM", "DOWNSTREAM"}:
                output["Direction"] = "UPSTREAM"

        output["TargetType"] = TARGET_TYPE_MAP.get(clean(output.get("TargetType")), clean(output.get("TargetType")))
        if clean(output.get("TargetType")) not in {"DELIVERABLE", "PACKAGE", "WBS_NODE", "REQUIREMENT", "DOCUMENT", "EQUIPMENT", "EXTERNAL", "UNKNOWN"}:
            output["TargetType"] = "UNKNOWN"

        if output["TargetType"] != "DELIVERABLE":
            if clean(output.get("TargetDeliverableID")) and not clean(output.get("TargetRefID")):
                output["TargetRefID"] = clean(output.get("TargetDeliverableID"))
            output["TargetDeliverableID"] = ""
        elif not clean(output.get("TargetDeliverableID")) and clean(output.get("TargetRefID")).startswith("DEL-"):
            output["TargetDeliverableID"] = clean(output.get("TargetRefID"))

        explicitness = clean(output.get("Explicitness"))
        output["Explicitness"] = explicitness if explicitness in {"EXPLICIT", "IMPLICIT"} else "IMPLICIT"

        satisfaction = clean(output.get("SatisfactionStatus"))
        output["SatisfactionStatus"] = satisfaction if satisfaction in {"TBD", "PENDING", "IN_PROGRESS", "SATISFIED", "WAIVED", "NOT_APPLICABLE"} else "TBD"

        confidence = clean(output.get("Confidence"))
        output["Confidence"] = confidence if confidence in {"HIGH", "MEDIUM", "LOW"} else "LOW"

        output["Origin"] = clean(output.get("Origin")) if clean(output.get("Origin")) == "DECLARED" else "EXTRACTED"

        if clean(output.get("Status")) == "CANDIDATE":
            candidate_rows.append(candidate_record(source_file, original, output))
            output["Status"] = "RETIRED"
            legacy_notes.append("candidate_disposition=moved_to_non_authoritative_worklist")
        elif clean(output.get("Status")) not in {"ACTIVE", "RETIRED"}:
            output["Status"] = "ACTIVE"

        if not clean(output.get("FirstSeen")):
            output["FirstSeen"] = today
        output["LastSeen"] = today
        output["Notes"] = append_note(clean(output.get("Notes")), *legacy_notes)
        return output


    def candidate_record(source_file: Path, original: dict[str, str], canonical: dict[str, str]) -> dict[str, str]:
        return {
            "SourceFile": str(source_file),
            "DependencyID": clean(original.get("DependencyID")),
            "FromPackageID": clean(original.get("FromPackageID")),
            "FromDeliverableID": clean(original.get("FromDeliverableID")),
            "OriginalDependencyType": clean(original.get("DependencyType")),
            "CanonicalDependencyType": clean(canonical.get("DependencyType")),
            "TargetPackageID": clean(original.get("TargetPackageID")),
            "TargetDeliverableID": clean(original.get("TargetDeliverableID")),
            "Statement": clean(original.get("Statement")),
            "Disposition": "NON_AUTHORITATIVE_CANDIDATE_WORKLIST",
            "Notes": clean(original.get("Notes")),
        }


    def declared_section(existing: str, heading: str) -> list[str]:
        lines = existing.splitlines()
        start = None
        for index, line in enumerate(lines):
            if line.strip() == heading:
                start = index
                break
        if start is None:
            return ["- None recorded."]
        collected: list[str] = []
        for line in lines[start + 1 :]:
            if line.startswith("## "):
                break
            if line.strip():
                collected.append(line)
        return collected or ["- None recorded."]


    def render_dependencies_md(path: Path, rows: list[dict[str, str]], candidate_count: int, today: str) -> str:
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        deliverable_id = clean(rows[0].get("FromDeliverableID")) if rows else path.parent.name.split("_", 1)[0]
        deliverable_name = clean(rows[0].get("FromDeliverableName")) if rows else path.parent.name
        upstream = declared_section(existing, "## Declared Upstream Dependencies")
        downstream = declared_section(existing, "## Declared Downstream Dependencies")
        status_counts = Counter(clean(row.get("Status")) or "BLANK" for row in rows)
        class_counts = Counter(clean(row.get("DependencyClass")) or "BLANK" for row in rows)
        type_counts = Counter(clean(row.get("DependencyType")) or "BLANK" for row in rows)

        type_lines = [f"- `{key}`: {type_counts[key]}" for key in sorted(type_counts)]
        return "\n".join(
            [
                f"# Dependencies: {deliverable_id} {deliverable_name}",
                "",
                "## Coordination Mode",
                "- **Mode:** FULL_GRAPH",
                "- **Graph Authority:** `execution/_DAG/DAG-006/` is the approved legacy graph pending `DAG-007` canonical approval.",
                "- **Authority Boundary:** Candidate/non-gating edges are not represented through `Status=CANDIDATE` in current canonical registers.",
                "",
                "## Declared Upstream Dependencies",
                *upstream,
                "",
                "## Declared Downstream Dependencies",
                *downstream,
                "",
                "## Extracted Dependency Register",
                "- **Local Register:** `Dependencies.csv`",
                "- **Register schema version:** `v3.1`",
                f"- **Canonicalized:** {today}",
                f"- **Rows:** {len(rows)} total; {status_counts.get('ACTIVE', 0)} ACTIVE; {status_counts.get('RETIRED', 0)} RETIRED.",
                f"- **Classes:** ANCHOR={class_counts.get('ANCHOR', 0)}; EXECUTION={class_counts.get('EXECUTION', 0)}.",
                f"- **Candidate rows moved to worklist:** {candidate_count}.",
                "",
                "## Canonical Dependency Types",
                *(type_lines or ["- None"]),
                "",
                "## Run Notes",
                "- Core enum fields conform to the canonical Chirality dependency model.",
                "- Legacy project-specific labels are preserved in `Notes` as `legacy_*` fields.",
                "- Candidate rows remain non-gating in the candidate worklist and require explicit human approval plus graph revalidation before promotion.",
                "- This dependency refresh does not authorize implementation, lifecycle promotion, release claims, professional approval, certification, sealing, authentication, or code-compliance claims.",
                "",
            ]
        )


    def local_dependency_paths(working_root: Path) -> list[Path]:
        return sorted(working_root.glob("execution/PKG-*/1_Working/DEL-*/Dependencies.csv"))


    def canonicalize_local(working_root: Path, today: str) -> dict[str, object]:
        candidate_rows: list[dict[str, str]] = []
        touched: list[dict[str, object]] = []
        worklist_path = working_root / "execution/_Reconciliation/DependencyTypeSystem/TYPE_RECTIFICATION_2026-06-16/CandidateDependencyEdges.csv"

        for csv_path in local_dependency_paths(working_root):
            header, rows = read_csv(csv_path)
            fieldnames = REQUIRED_COLUMNS + [column for column in header if column not in REQUIRED_COLUMNS]
            before = [dict(row) for row in rows]
            local_candidates_before = len(candidate_rows)
            canonical_rows = [
                canonicalize_row(row, source_file=csv_path.relative_to(working_root), today=today, candidate_rows=candidate_rows)
                for row in rows
            ]
            write_csv(csv_path, fieldnames, canonical_rows)
            md_path = csv_path.with_name("_DEPENDENCIES.md")
            md_path.write_text(
                render_dependencies_md(
                    md_path,
                    canonical_rows,
                    len(candidate_rows) - local_candidates_before,
                    today,
                ),
                encoding="utf-8",
            )
            touched.append({
                "path": str(csv_path.relative_to(working_root)),
                "rows": len(canonical_rows),
                "changed": before != canonical_rows,
                "candidate_rows_moved": len(candidate_rows) - local_candidates_before,
            })

        write_csv(
            worklist_path,
            [
                "SourceFile",
                "DependencyID",
                "FromPackageID",
                "FromDeliverableID",
                "OriginalDependencyType",
                "CanonicalDependencyType",
                "TargetPackageID",
                "TargetDeliverableID",
                "Statement",
                "Disposition",
                "Notes",
            ],
            candidate_rows,
        )
        return {"touched": touched, "candidate_worklist": str(worklist_path), "candidate_rows": len(candidate_rows)}


    def normalized_edge(row: dict[str, str]) -> tuple[str, str] | None:
        from_id = clean(row.get("FromDeliverableID"))
        target_id = clean(row.get("TargetDeliverableID"))
        if not from_id or not target_id:
            return None
        if clean(row.get("Direction")) == "DOWNSTREAM":
            return target_id, from_id
        return from_id, target_id


    def active_execution_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
        return [
            row
            for row in rows
            if clean(row.get("Status")) == "ACTIVE"
            and clean(row.get("DependencyClass")) == "EXECUTION"
            and clean(row.get("TargetType")) == "DELIVERABLE"
            and normalized_edge(row) is not None
        ]


    def topological_waves(nodes: list[str], rows: list[dict[str, str]]) -> list[list[str]]:
        graph: dict[str, set[str]] = defaultdict(set)
        indegree: dict[str, int] = {node: 0 for node in nodes}
        for row in rows:
            edge = normalized_edge(row)
            if edge is None:
                continue
            source, target = edge
            if target not in graph[source]:
                graph[source].add(target)
                indegree[target] = indegree.get(target, 0) + 1
                indegree.setdefault(source, 0)

        queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
        waves: list[list[str]] = []
        while queue:
            wave = list(queue)
            waves.append(wave)
            queue.clear()
            next_nodes: list[str] = []
            for node in wave:
                for target in sorted(graph.get(node, set())):
                    indegree[target] -= 1
                    if indegree[target] == 0:
                        next_nodes.append(target)
            queue.extend(sorted(next_nodes))
        return waves


    def render_topological_waves(waves: list[list[str]], today: str, source_basis: str) -> str:
        lines = [
            "---",
            "doc_id: DAG-007-TOPOLOGICAL-WAVES",
            "doc_kind: coordination.topological_waves",
            "status: proposed_pending_approval",
            f"created: {today}",
            "---",
            "",
            "# DAG-007 Topological Waves",
            "",
            f"These waves are computed from {source_basis}.",
            "Candidate rows are excluded from the active graph and remain in the non-authoritative candidate worklist.",
            "",
            "| Wave | Node count | Deliverables |",
            "|---|---:|---|",
        ]
        for index, wave in enumerate(waves, start=1):
            nodes = ", ".join(f"`{node}`" for node in wave)
            lines.append(f"| {index} | {len(wave)} | {nodes} |")
        lines.append("")
        return "\n".join(lines)


    def render_cycle_report(active_count: int, node_count: int, wave_count: int, active_scc_count: int, today: str, source_basis: str) -> str:
        status = "ACYCLIC" if active_scc_count == 0 else "CYCLES_REQUIRING_RECONCILIATION"
        return "\n".join(
            [
                "# DAG-007 Cycle Report",
                "",
                f"- Active graph status: {status}",
                f"- Node count: {node_count}",
                f"- Active edge count: {active_count}",
                f"- Active SCCs with more than one node: {active_scc_count}",
                "- Candidate rows: excluded from canonical active edge register",
                f"- Topological waves: {wave_count}",
                f"- Generated: {today}",
                "",
                f"DAG-007 is proposed from {source_basis}.",
                "Candidate SCCs remain non-gating worklist items pending explicit human resolution.",
                "",
            ]
        )


    def render_review_packet(summary: dict[str, object], today: str) -> str:
        return "\n".join(
            [
                "---",
                "doc_id: DAG-007-APPROVAL-REVIEW-PACKET",
                "doc_kind: coordination.approval_review_packet",
                "status: proposed_pending_human_approval",
                f"created: {today}",
                "---",
                "",
                "# DAG-007 Approval Review Packet",
                "",
                "## Proposal Summary",
                "",
                "`DAG-007` is a proposed canonical successor built from refreshed deliverable-local dependency registers.",
                "It removes candidate rows from the v3.1 edge register and normalizes core dependency enum fields",
                "to the canonical Chirality model.",
                "",
                "## Graph Facts",
                "",
                "| Fact | Value |",
                "|---|---:|",
                f"| Deliverable nodes | {summary['node_count']} |",
                f"| Edge rows | {summary['edge_row_count']} |",
                f"| Active edges | {summary['active_edge_count']} |",
                f"| Retired rows | {summary['retired_edge_count']} |",
                f"| Candidate worklist rows | {summary['candidate_edge_count']} |",
                f"| Active SCCs | {summary['active_scc_count']} |",
                f"| Topological waves | {summary['wave_count']} |",
                "",
                "## Approval Boundary",
                "",
                "Human approval, if granted, approves only the canonical graph-authority successor.",
                "It does not promote candidate rows, dispatch Type 2 work, change lifecycle states,",
                "make release-readiness claims, or create professional/code-compliance acceptance.",
                "",
            ]
        )


    def render_approval_record_template(summary: dict[str, object], today: str) -> str:
        return "\n".join(
            [
                "---",
                "doc_id: DAG-007-APPROVAL-RECORD",
                "doc_kind: coordination.approval_record",
                "status: proposed_pending_human_approval",
                f"created: {today}",
                "approved: TBD",
                "approved_by: TBD",
                "approved_decomposition: execution/_Decomposition/SOFTWARE_DECOMP.md",
                'approved_revision: "0.7"',
                "dag_path: execution/_DAG/DAG-007/",
                "approval_scope: canonical_dependency_type_system_rectification",
                "candidate_treatment: separate_non_authoritative_worklist",
                "topology_basis: refreshed_deliverable_local_dependency_registers",
                "type2_dispatch: not_authorized_by_approval_record",
                "lifecycle_changes: not_authorized",
                "---",
                "",
                "# DAG-007 Approval Record Template",
                "",
                "`DAG-007` is not approved at creation time. Replace this template only after explicit human approval.",
                "",
                "## Proposed Decision",
                "",
                "Approve `DAG-007` as the canonical dependency successor built from refreshed local registers,",
                "with candidate rows held outside the canonical active edge register.",
                "",
                "## Proposed Graph Facts",
                "",
                f"- Nodes: {summary['node_count']}",
                f"- Edge rows in canonical register: {summary['edge_row_count']}",
                f"- Active edges: {summary['active_edge_count']}",
                f"- Candidate worklist rows: {summary['candidate_edge_count']}",
                "",
                "## Required Human Approval",
                "",
                "Approval text must explicitly approve this `DAG-007` package before `_DAG/_LATEST.md` is updated.",
                "",
            ]
        )


    def build_dag_json(nodes: list[dict[str, str]], rows: list[dict[str, str]], summary: dict[str, object], today: str) -> dict[str, object]:
        active_rows = active_execution_rows(rows)
        return {
            "metadata": {
                "dag_id": "DAG-007",
                "created": today,
                "decomposition_revision": "0.7",
                "node_count": summary["node_count"],
                "package_count": summary["package_count"],
                "edge_row_count": summary["edge_row_count"],
                "active_edge_count": summary["active_edge_count"],
                "candidate_edge_count": summary["candidate_edge_count"],
                "retired_edge_count": summary["retired_edge_count"],
                "approval_status": "PROPOSED_PENDING_HUMAN_APPROVAL",
                "node_baseline_graph": "execution/_DAG/DAG-006/",
                "edge_basis": "refreshed deliverable-local Dependencies.csv registers",
                "candidate_treatment": "SEPARATE_NON_AUTHORITATIVE_WORKLIST",
                "active_cycle_status": "ACYCLIC" if summary["active_scc_count"] == 0 else "CYCLES_REQUIRING_RECONCILIATION",
                "edge_direction": "FromDeliverableID depends on TargetDeliverableID for UPSTREAM rows; DOWNSTREAM rows normalize inverse",
                "approval_record": "execution/_DAG/DAG-007/APPROVAL_RECORD.md",
            },
            "nodes": [
                {
                    "id": clean(node.get("DeliverableID")),
                    "package_id": clean(node.get("PackageID")),
                    "name": clean(node.get("DeliverableName")),
                    "type": clean(node.get("DeliverableType")),
                    "path": clean(node.get("ExecutionPath")),
                }
                for node in nodes
            ],
            "edges": [
                {
                    "id": clean(row.get("DependencyID")),
                    "from": clean(row.get("FromDeliverableID")),
                    "to": clean(row.get("TargetDeliverableID")),
                    "direction": clean(row.get("Direction")),
                    "dependency_type": clean(row.get("DependencyType")),
                    "status": clean(row.get("Status")),
                    "source": normalized_edge(row)[0] if normalized_edge(row) else "",
                    "target": normalized_edge(row)[1] if normalized_edge(row) else "",
                }
                for row in active_rows
            ],
        }


    def local_dependency_rows(working_root: Path, today: str) -> tuple[list[str], list[dict[str, str]], list[dict[str, str]]]:
        fieldnames = list(REQUIRED_COLUMNS)
        rows: list[dict[str, str]] = []
        candidate_rows: list[dict[str, str]] = []
        for csv_path in local_dependency_paths(working_root):
            header, source_rows = read_csv(csv_path)
            for column in header:
                if column not in fieldnames:
                    fieldnames.append(column)
            for row in source_rows:
                normalized = canonicalize_row(
                    row,
                    source_file=csv_path.relative_to(working_root),
                    today=today,
                    candidate_rows=candidate_rows,
                )
                if clean(row.get("Status")) == "CANDIDATE":
                    continue
                rows.append(normalized)
        return fieldnames, rows, candidate_rows


    def active_sccs(rows: list[dict[str, str]]) -> list[list[str]]:
        graph: dict[str, set[str]] = defaultdict(set)
        nodes: set[str] = set()
        for row in active_execution_rows(rows):
            edge = normalized_edge(row)
            if edge is None:
                continue
            source, target = edge
            graph[source].add(target)
            nodes.add(source)
            nodes.add(target)

        index = 0
        stack: list[str] = []
        indices: dict[str, int] = {}
        lowlink: dict[str, int] = {}
        on_stack: set[str] = set()
        components: list[list[str]] = []

        def visit(node: str) -> None:
            nonlocal index
            indices[node] = index
            lowlink[node] = index
            index += 1
            stack.append(node)
            on_stack.add(node)

            for target in sorted(graph.get(node, set())):
                if target not in indices:
                    visit(target)
                    lowlink[node] = min(lowlink[node], lowlink[target])
                elif target in on_stack:
                    lowlink[node] = min(lowlink[node], indices[target])

            if lowlink[node] == indices[node]:
                component: list[str] = []
                while True:
                    item = stack.pop()
                    on_stack.remove(item)
                    component.append(item)
                    if item == node:
                        break
                if len(component) > 1:
                    components.append(sorted(component))

        for node in sorted(nodes):
            if node not in indices:
                visit(node)
        return sorted(components, key=lambda item: (len(item), item))


    def duplicate_retention_key(row: dict[str, str]) -> tuple[int, str, str]:
        origin_rank = 0 if clean(row.get("Origin")) == "DECLARED" else 1
        return (origin_rank, clean(row.get("FirstSeen")), clean(row.get("DependencyID")))


    def retire_duplicate_active_edges(rows: list[dict[str, str]], today: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
        by_edge: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            if clean(row.get("Status")) != "ACTIVE":
                continue
            if clean(row.get("DependencyClass")) != "EXECUTION":
                continue
            if clean(row.get("TargetType")) != "DELIVERABLE":
                continue
            edge = normalized_edge(row)
            if edge is not None:
                by_edge[edge].append(row)

        keep_ids: set[int] = set()
        duplicate_records: list[dict[str, str]] = []
        for (source, target), edge_rows in sorted(by_edge.items()):
            if len(edge_rows) <= 1:
                continue
            ranked = sorted(edge_rows, key=duplicate_retention_key)
            kept = ranked[0]
            keep_ids.add(id(kept))
            kept_id = clean(kept.get("DependencyID"))
            for duplicate in ranked[1:]:
                duplicate_id = clean(duplicate.get("DependencyID"))
                duplicate_records.append(
                    {
                        "Source": source,
                        "Target": target,
                        "KeptDependencyID": kept_id,
                        "RetiredDependencyID": duplicate_id,
                        "FromDeliverableID": clean(duplicate.get("FromDeliverableID")),
                        "TargetDeliverableID": clean(duplicate.get("TargetDeliverableID")),
                        "DependencyType": clean(duplicate.get("DependencyType")),
                        "Statement": clean(duplicate.get("Statement")),
                        "Disposition": "RETIRED_IN_DAG007_AGGREGATE_ONLY_DUPLICATE_DIRECTED_EDGE",
                    }
                )

        if not duplicate_records:
            return rows, []

        duplicate_ids = {record["RetiredDependencyID"] for record in duplicate_records}
        output: list[dict[str, str]] = []
        for row in rows:
            if clean(row.get("DependencyID")) in duplicate_ids:
                updated = dict(row)
                updated["Status"] = "RETIRED"
                updated["LastSeen"] = today
                kept_id = next(record["KeptDependencyID"] for record in duplicate_records if record["RetiredDependencyID"] == clean(row.get("DependencyID")))
                updated["Notes"] = append_note(
                    clean(updated.get("Notes")),
                    "dag007_duplicate_directed_edge_retired=true",
                    f"duplicate_kept_id={kept_id}",
                    "aggregate_only_local_register_unchanged=true",
                )
                output.append(updated)
            else:
                output.append(row)
        return output, duplicate_records


    def build_dag007(working_root: Path, repo: Path, today: str) -> dict[str, object]:
        dag006 = working_root / "execution/_DAG/DAG-006"
        dag007 = working_root / "execution/_DAG/DAG-007"
        dag007.mkdir(parents=True, exist_ok=True)

        node_header, node_rows = read_csv(dag006 / "DeliverableNodes.csv")
        fieldnames, canonical_edge_rows, candidate_rows = local_dependency_rows(working_root, today)
        canonical_edge_rows, duplicate_rows = retire_duplicate_active_edges(canonical_edge_rows, today)
        write_csv(dag007 / "DependencyEdges.csv", fieldnames, canonical_edge_rows)
        write_csv(dag007 / "DeliverableNodes.csv", node_header, node_rows)
        write_csv(
            dag007 / "DAG-007_CandidateEdgeWorklist.csv",
            [
                "SourceFile",
                "DependencyID",
                "FromPackageID",
                "FromDeliverableID",
                "OriginalDependencyType",
                "CanonicalDependencyType",
                "TargetPackageID",
                "TargetDeliverableID",
                "Statement",
                "Disposition",
                "Notes",
            ],
            candidate_rows,
        )
        write_csv(
            dag007 / "DAG-007_DuplicateEdgeWorklist.csv",
            [
                "Source",
                "Target",
                "KeptDependencyID",
                "RetiredDependencyID",
                "FromDeliverableID",
                "TargetDeliverableID",
                "DependencyType",
                "Statement",
                "Disposition",
            ],
            duplicate_rows,
        )

        active_rows = active_execution_rows(canonical_edge_rows)
        node_ids = [clean(row.get("DeliverableID")) for row in node_rows if clean(row.get("DeliverableID"))]
        waves = topological_waves(node_ids, active_rows)
        sccs = active_sccs(canonical_edge_rows)
        summary = {
            "node_count": len(node_ids),
            "package_count": len({clean(row.get("PackageID")) for row in node_rows if clean(row.get("PackageID"))}),
            "edge_row_count": len(canonical_edge_rows),
            "active_edge_count": len(active_rows),
            "retired_edge_count": sum(1 for row in canonical_edge_rows if clean(row.get("Status")) == "RETIRED"),
            "candidate_edge_count": len(candidate_rows),
            "duplicate_edge_rows_retired": len(duplicate_rows),
            "active_scc_count": len(sccs),
            "wave_count": len(waves),
        }
        (dag007 / "dag.json").write_text(json.dumps(build_dag_json(node_rows, canonical_edge_rows, summary, today), indent=2) + "\n", encoding="utf-8")
        source_basis = "the refreshed deliverable-local `Dependencies.csv` registers; `DAG-006` supplies the node/path baseline only"
        (dag007 / "TopologicalWaves.md").write_text(render_topological_waves(waves, today, source_basis), encoding="utf-8")
        (dag007 / "Cycle_Report.md").write_text(render_cycle_report(len(active_rows), len(node_ids), len(waves), len(sccs), today, source_basis), encoding="utf-8")
        (dag007 / "DAG-007_APPROVAL_REVIEW_PACKET.md").write_text(render_review_packet(summary, today), encoding="utf-8")
        (dag007 / "APPROVAL_RECORD.md").write_text(render_approval_record_template(summary, today), encoding="utf-8")
        (dag007 / "PROPOSAL_RECORD.md").write_text(
            "\n".join(
                [
                    "---",
                    "doc_id: DAG-007-PROPOSAL-RECORD",
                    "doc_kind: coordination.proposal_record",
                    "status: proposed_pending_human_approval",
                    f"created: {today}",
                    "---",
                    "",
                    "# DAG-007 Proposal Record",
                    "",
                    "DAG-007 is proposed after the all-register dependency semantic refresh.",
                    "It is built from refreshed deliverable-local dependency registers and holds candidate rows outside the canonical edge register.",
                    "`DAG-006` supplies the node/path baseline only; root `_DAG/_LATEST.md` remains unchanged pending human approval.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (dag007 / "_LATEST.md").write_text(
            "\n".join(
                [
                    "# DAG-007 Local Pointer",
                    "",
                    "- DAG artifact: `DAG-007`",
                    "- Status: proposed_pending_human_approval",
                    "- Approved graph authority: not yet; root `_DAG/_LATEST.md` remains on `DAG-006` until approval.",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        audit_json = dag007 / "DAG_Audit.json"
        audit_md = dag007 / "DAG_Audit.md"
        subprocess.run(
            [
                "python3",
                str(repo / "tools/coordination/audit_dag.py"),
                "--dag-dir",
                str(dag007.relative_to(working_root)),
                "--canonical",
                "--json-out",
                str(audit_json.relative_to(working_root)),
                "--markdown-out",
                str(audit_md.relative_to(working_root)),
            ],
            cwd=working_root,
            check=True,
        )
        return {"dag007": str(dag007), **summary}


    def drift_summary(working_root: Path, output_path: Path) -> None:
        fields = [
            "DependencyClass",
            "AnchorType",
            "Direction",
            "DependencyType",
            "TargetType",
            "Explicitness",
            "SatisfactionStatus",
            "Confidence",
            "Origin",
            "Status",
        ]
        allowed = {
            "DependencyClass": {"ANCHOR", "EXECUTION"},
            "AnchorType": {"IMPLEMENTS_NODE", "TRACES_TO_REQUIREMENT", "NOT_APPLICABLE"},
            "Direction": {"UPSTREAM", "DOWNSTREAM"},
            "DependencyType": {"PREREQUISITE", "INTERFACE", "HANDOVER", "CONSTRAINT", "ENABLES", "OTHER"},
            "TargetType": {"DELIVERABLE", "PACKAGE", "WBS_NODE", "REQUIREMENT", "DOCUMENT", "EQUIPMENT", "EXTERNAL", "UNKNOWN"},
            "Explicitness": {"EXPLICIT", "IMPLICIT"},
            "SatisfactionStatus": {"TBD", "PENDING", "IN_PROGRESS", "SATISFIED", "WAIVED", "NOT_APPLICABLE"},
            "Confidence": {"HIGH", "MEDIUM", "LOW"},
            "Origin": {"DECLARED", "EXTRACTED"},
            "Status": {"ACTIVE", "RETIRED"},
        }
        rows: list[dict[str, str]] = []
        paths = local_dependency_paths(working_root) + [working_root / "execution/_DAG/DAG-007/DependencyEdges.csv"]
        for path in paths:
            _header, data = read_csv(path)
            for line, row in enumerate(data, start=2):
                for field in fields:
                    value = clean(row.get(field))
                    if value not in allowed[field]:
                        rows.append({"File": str(path.relative_to(working_root)), "Line": str(line), "DependencyID": clean(row.get("DependencyID")), "Field": field, "Value": value})
        write_csv(output_path, ["File", "Line", "DependencyID", "Field", "Value"], rows)


    def main() -> int:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--working-root", type=Path, default=Path.cwd())
        parser.add_argument("--today", default=date.today().isoformat())
        parser.add_argument("--local", action="store_true", help="Canonicalize local deliverable registers.")
        parser.add_argument("--dag007", action="store_true", help="Build DAG-007 from refreshed local dependency registers.")
        parser.add_argument("--after-drift", action="store_true", help="Write after_enum_drift.csv evidence.")
        args = parser.parse_args()

        working_root = args.working_root.resolve()
        repo = repo_root(working_root)
        result: dict[str, object] = {}
        if args.local:
            result["local"] = canonicalize_local(working_root, args.today)
        if args.dag007:
            result["dag007"] = build_dag007(working_root, repo, args.today)
        if args.after_drift:
            evidence = working_root / "execution/_Reconciliation/DependencyTypeSystem/TYPE_RECTIFICATION_2026-06-16/Evidence/after_enum_drift.csv"
            drift_summary(working_root, evidence)
            result["after_drift"] = str(evidence)

        print(json.dumps(result, indent=2))
        return 0


    if __name__ == "__main__":
        raise SystemExit(main())

## Component: tools/coordination/list_deliverable_status.py

    #!/usr/bin/env python3
    """List deliverable-local lifecycle status with optional DAG node context.

    This is a read-only coordination helper. It discovers deliverables from local
    `_STATUS.md` files and joins to the selected DAG's `DeliverableNodes.csv` for
    node presence and path context when available. Local `_STATUS.md` values are
    the lifecycle source of truth for work selection.
    """

    from __future__ import annotations

    import argparse
    import csv
    import re
    import sys
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Iterable


    ROOT = Path(__file__).resolve().parents[2]
    CANONICAL_STATES = {"OPEN", "INITIALIZED", "IN_PROGRESS", "CHECKING", "ISSUED"}
    TOLERATED_NONSTANDARD_STATES = {"SEMANTIC_READY"}
    STATUS_RE = re.compile(r"^\*\*Current State:\*\*\s*(?P<status>\S+)\s*$")
    UPDATED_RE = re.compile(r"^\*\*Last Updated:\*\*\s*(?P<date>.+?)\s*$")
    PACKAGE_RE = re.compile(r"^(?P<package_id>PKG-\d+)")
    DELIVERABLE_RE = re.compile(r"^(?P<deliverable_id>DEL-\d+-\d+)(?:_(?P<name>.*))?$")


    HEADER = [
        "DeliverableID",
        "PackageID",
        "DeliverableName",
        "LocalStatus",
        "LastUpdated",
        "StatusVocabulary",
        "DeliverablePath",
        "StatusPath",
        "DAG",
        "DAGNodePresent",
        "DAGExecutionPath",
    ]


    @dataclass(frozen=True)
    class LocalStatus:
        deliverable_id: str
        package_id: str
        deliverable_name: str
        status: str
        last_updated: str
        deliverable_path: Path
        status_path: Path


    def latest_dag(root: Path) -> str:
        latest = root / "execution/_DAG/_LATEST.md"
        for line in latest.read_text(encoding="utf-8").splitlines():
            if line.startswith("- Approved graph authority:"):
                value = line.split(":", maxsplit=1)[1].strip().strip("`").strip("/")
                return Path(value).name
        raise ValueError(f"approved graph authority not found in {latest}")


    def rel(path: Path, root: Path) -> str:
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            return path.as_posix()


    def package_id_from_path(path: Path) -> str:
        for part in path.parts:
            match = PACKAGE_RE.match(part)
            if match:
                return match.group("package_id")
        return ""


    def deliverable_parts_from_path(path: Path) -> tuple[str, str]:
        for part in path.parts:
            match = DELIVERABLE_RE.match(part)
            if match:
                name = (match.group("name") or "").replace("_", " ").strip()
                return match.group("deliverable_id"), name
        return "", ""


    def parse_status_file(path: Path) -> LocalStatus:
        status = ""
        last_updated = ""
        for line in path.read_text(encoding="utf-8").splitlines():
            status_match = STATUS_RE.match(line)
            if status_match:
                status = status_match.group("status").strip()
                continue
            updated_match = UPDATED_RE.match(line)
            if updated_match:
                last_updated = updated_match.group("date").strip()

        deliverable_path = path.parent
        package_id = package_id_from_path(deliverable_path)
        deliverable_id, deliverable_name = deliverable_parts_from_path(deliverable_path)
        return LocalStatus(
            deliverable_id=deliverable_id,
            package_id=package_id,
            deliverable_name=deliverable_name,
            status=status,
            last_updated=last_updated,
            deliverable_path=deliverable_path,
            status_path=path,
        )


    def discover_statuses(root: Path) -> list[LocalStatus]:
        paths = sorted(root.glob("execution/PKG-*/1_Working/DEL-*/_STATUS.md"))
        return [parse_status_file(path) for path in paths]


    def read_dag_nodes(root: Path, dag: str) -> dict[str, dict[str, str]]:
        path = root / "execution" / "_DAG" / dag / "DeliverableNodes.csv"
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise ValueError(f"empty DAG node CSV: {path}")
            return {row.get("DeliverableID", ""): row for row in reader}


    def status_vocabulary(status: str) -> str:
        if not status:
            return "MISSING"
        if status in CANONICAL_STATES:
            return "CANONICAL"
        if status in TOLERATED_NONSTANDARD_STATES:
            return "NONSTANDARD_TOLERATED"
        return "NONSTANDARD"


    def rows(root: Path, dag: str, statuses: Iterable[LocalStatus]) -> list[dict[str, str]]:
        dag_nodes = read_dag_nodes(root, dag)
        output_rows: list[dict[str, str]] = []
        for item in sorted(statuses, key=lambda row: (row.package_id, row.deliverable_id)):
            node = dag_nodes.get(item.deliverable_id, {})
            output_rows.append(
                {
                    "DeliverableID": item.deliverable_id,
                    "PackageID": item.package_id,
                    "DeliverableName": item.deliverable_name
                    or node.get("DeliverableName", ""),
                    "LocalStatus": item.status,
                    "LastUpdated": item.last_updated,
                    "StatusVocabulary": status_vocabulary(item.status),
                    "DeliverablePath": rel(item.deliverable_path, root),
                    "StatusPath": rel(item.status_path, root),
                    "DAG": dag,
                    "DAGNodePresent": "TRUE" if node else "FALSE",
                    "DAGExecutionPath": node.get("ExecutionPath", ""),
                }
            )
        return output_rows


    def filter_rows(
        output_rows: Iterable[dict[str, str]],
        statuses: set[str],
        exclude_issued: bool,
    ) -> list[dict[str, str]]:
        filtered = []
        for row in output_rows:
            status = row["LocalStatus"]
            if statuses and status not in statuses:
                continue
            if exclude_issued and status == "ISSUED":
                continue
            filtered.append(row)
        return filtered


    def write_csv(output_rows: list[dict[str, str]]) -> None:
        writer = csv.DictWriter(sys.stdout, fieldnames=HEADER, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)


    def write_table(output_rows: list[dict[str, str]]) -> None:
        columns = [
            "DeliverableID",
            "PackageID",
            "LocalStatus",
            "StatusVocabulary",
            "DAGNodePresent",
            "DeliverablePath",
        ]
        widths = {
            column: max(len(column), *(len(row[column]) for row in output_rows))
            if output_rows
            else len(column)
            for column in columns
        }
        print("  ".join(column.ljust(widths[column]) for column in columns))
        print("  ".join("-" * widths[column] for column in columns))
        for row in output_rows:
            print("  ".join(row[column].ljust(widths[column]) for column in columns))


    def write_markdown(output_rows: list[dict[str, str]]) -> None:
        columns = [
            "DeliverableID",
            "PackageID",
            "LocalStatus",
            "StatusVocabulary",
            "DAGNodePresent",
            "DeliverablePath",
        ]
        print("| " + " | ".join(columns) + " |")
        print("| " + " | ".join("---" for _ in columns) + " |")
        for row in output_rows:
            print("| " + " | ".join(row[column] for column in columns) + " |")


    def print_summary(output_rows: list[dict[str, str]]) -> None:
        counts: dict[str, int] = {}
        for row in output_rows:
            counts[row["LocalStatus"]] = counts.get(row["LocalStatus"], 0) + 1
        status_counts = ", ".join(f"{key}={counts[key]}" for key in sorted(counts))
        print(f"Rows: {len(output_rows)}", file=sys.stderr)
        print(f"Status counts: {status_counts}", file=sys.stderr)


    def parse_args(argv: list[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="List deliverable-local _STATUS.md values with DAG context."
        )
        parser.add_argument("--repo-root", default=str(ROOT), help="Repository root.")
        parser.add_argument("--dag", default=None, help="DAG folder name, for example DAG-006.")
        parser.add_argument(
            "--format",
            choices=("table", "csv", "markdown"),
            default="table",
            help="Output format.",
        )
        parser.add_argument(
            "--status",
            action="append",
            default=[],
            help="Filter by local status. Repeatable.",
        )
        parser.add_argument(
            "--exclude-issued",
            action="store_true",
            help="Exclude ISSUED deliverables from the report.",
        )
        parser.add_argument(
            "--summary",
            action="store_true",
            help="Print row count and local status counts to stderr.",
        )
        return parser.parse_args(argv)


    def main(argv: list[str]) -> int:
        args = parse_args(argv)
        root = Path(args.repo_root).resolve()
        dag = args.dag or latest_dag(root)
        output_rows = rows(root, dag, discover_statuses(root))
        output_rows = filter_rows(output_rows, set(args.status), args.exclude_issued)

        if args.format == "csv":
            write_csv(output_rows)
        elif args.format == "markdown":
            write_markdown(output_rows)
        else:
            write_table(output_rows)

        if args.summary:
            print_summary(output_rows)
        return 0


    if __name__ == "__main__":
        raise SystemExit(main(sys.argv[1:]))

## Component: tools/release/check_release_readiness.py

    #!/usr/bin/env python3
    """Provider-neutral local release-readiness checks for OpenPipeStress."""

    from __future__ import annotations

    import argparse
    import shutil
    import subprocess
    import sys
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Iterable


    ROOT = Path(__file__).resolve().parents[2]

    REQUIRED_PATHS = (
        "docs/BUILD_AND_RELEASE.md",
        "docs/RELEASE_NOTES_TEMPLATE.md",
        "docs/RELEASE_QUALITY_GATES.md",
        "docs/VALIDATION_STRATEGY.md",
        "docs/IP_AND_DATA_BOUNDARY.md",
        "docs/PROFESSIONAL_BOUNDARY.md",
        "execution/_DAG/_LATEST.md",
    )

    CARGO_SEARCH_ROOTS = (
        "core",
        "validation/benchmarks",
    )


    @dataclass(frozen=True)
    class CheckStep:
        name: str
        command: tuple[str, ...]
        description: str


    def check_required_paths(root: Path = ROOT) -> list[str]:
        return [path for path in REQUIRED_PATHS if not (root / path).exists()]


    def latest_dag_dependency_edges(root: Path = ROOT) -> Path:
        latest_path = root / "execution" / "_DAG" / "_LATEST.md"
        try:
            lines = latest_path.read_text(encoding="utf-8").splitlines()
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"missing latest DAG pointer: {latest_path}") from exc

        dag_dir: str | None = None
        for line in lines:
            if line.startswith("- Approved graph authority:"):
                _, value = line.split(":", maxsplit=1)
                dag_dir = value.strip().strip("`")
                break

        if dag_dir is None:
            raise ValueError(f"approved graph authority not found in {latest_path}")

        dependency_edges = Path(dag_dir) / "DependencyEdges.csv"
        if not (root / dependency_edges).exists():
            raise FileNotFoundError(
                f"approved graph dependency file not found: {dependency_edges}"
            )
        return dependency_edges


    def discover_cargo_manifests(root: Path = ROOT) -> list[Path]:
        manifests: list[Path] = []
        for search_root in CARGO_SEARCH_ROOTS:
            base = root / search_root
            if not base.exists():
                continue
            for manifest in sorted(base.rglob("Cargo.toml")):
                relative = manifest.relative_to(root)
                if "target" in relative.parts:
                    continue
                manifests.append(relative)
        return manifests


    def python_cmd(*args: str) -> tuple[str, ...]:
        return (sys.executable, *args)


    def build_plan(profile: str, root: Path = ROOT) -> list[CheckStep]:
        steps: list[CheckStep] = []

        if profile in {"skeleton", "python", "all"}:
            dag_dependency_edges = latest_dag_dependency_edges(root)
            steps.append(
                CheckStep(
                    name="dag dependency schema",
                    command=python_cmd(
                        "tools/validation/validate_dependencies_schema.py",
                        dag_dependency_edges.as_posix(),
                    ),
                    description="Validate the approved latest DAG dependency register schema.",
                )
            )
            steps.append(
                CheckStep(
                    name="release readiness script tests",
                    command=python_cmd(
                        "-m",
                        "pytest",
                        "-q",
                        "tests/test_release_readiness_script.py",
                    ),
                    description="Run focused tests for the provider-neutral readiness script.",
                )
            )

        if profile in {"python", "all"}:
            steps.append(
                CheckStep(
                    name="python contract tests",
                    command=python_cmd("-m", "pytest", "-q", "tests"),
                    description="Run repository Python contract tests.",
                )
            )
            steps.append(
                CheckStep(
                    name="coordination tool tests",
                    command=python_cmd(
                        "-m",
                        "pytest",
                        "-q",
                        "tests/test_coordination_maintenance.py",
                    ),
                    description="Run coordination tool regression tests.",
                )
            )

        if profile in {"security", "all"}:
            steps.append(
                CheckStep(
                    name="security and privacy tests",
                    command=python_cmd("-m", "pytest", "-q", "tests/security"),
                    description="Run local-first storage, telemetry, and redaction checks.",
                )
            )

        if profile in {"cargo", "all"}:
            for manifest in discover_cargo_manifests(root):
                steps.append(
                    CheckStep(
                        name=f"cargo test {manifest.parent.as_posix()}",
                        command=("cargo", "test", "--manifest-path", manifest.as_posix()),
                        description="Run crate-local Rust tests without assuming a root workspace.",
                    )
                )

        return steps


    def missing_tools(steps: Iterable[CheckStep]) -> list[str]:
        missing: list[str] = []
        for step in steps:
            executable = step.command[0]
            if Path(executable).exists():
                continue
            if shutil.which(executable) is None and executable not in missing:
                missing.append(executable)
        return missing


    def print_plan(steps: list[CheckStep], root: Path, execute: bool) -> None:
        mode = "execute" if execute else "dry-run"
        print(f"OpenPipeStress release readiness profile ({mode})")
        print(f"repo: {root}")
        print("")

        manifests = discover_cargo_manifests(root)
        print(f"discovered cargo manifests: {len(manifests)}")
        for manifest in manifests:
            print(f"  - {manifest.as_posix()}")
        print("")

        print(f"planned checks: {len(steps)}")
        for index, step in enumerate(steps, start=1):
            print(f"{index}. {step.name}")
            print(f"   {step.description}")
            print(f"   command: {' '.join(step.command)}")


    def run_steps(steps: list[CheckStep], root: Path) -> int:
        for step in steps:
            print(f"running: {step.name}", flush=True)
            completed = subprocess.run(step.command, cwd=root, check=False)
            if completed.returncode != 0:
                print(f"failed: {step.name} exited {completed.returncode}", file=sys.stderr)
                return completed.returncode
        return 0


    def parse_args(argv: list[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="Run or dry-run provider-neutral OpenPipeStress release checks."
        )
        parser.add_argument(
            "--profile",
            choices=("skeleton", "python", "security", "cargo", "all"),
            default="skeleton",
            help="Local check profile to plan or execute.",
        )
        parser.add_argument(
            "--execute",
            action="store_true",
            help="Run the selected local checks. Without this flag, only dry-run.",
        )
        parser.add_argument(
            "--list-cargo-manifests",
            action="store_true",
            help="Print discovered Cargo manifests and exit.",
        )
        parser.add_argument(
            "--repo-root",
            default=str(ROOT),
            help="Repository root. Defaults to the root containing this script.",
        )
        return parser.parse_args(argv)


    def main(argv: list[str] | None = None) -> int:
        args = parse_args(sys.argv[1:] if argv is None else argv)
        root = Path(args.repo_root).resolve()

        if not root.exists():
            print(f"missing repository root: {root}", file=sys.stderr)
            return 2

        if args.list_cargo_manifests:
            for manifest in discover_cargo_manifests(root):
                print(manifest.as_posix())
            return 0

        missing_paths = check_required_paths(root)
        if missing_paths:
            print("missing required release paths:", file=sys.stderr)
            for path in missing_paths:
                print(f"  - {path}", file=sys.stderr)
            return 1

        steps = build_plan(args.profile, root)
        print_plan(steps, root, args.execute)
        sys.stdout.flush()

        if not args.execute:
            return 0

        tools = missing_tools(steps)
        if tools:
            print("missing required local tools:", file=sys.stderr)
            for tool in tools:
                print(f"  - {tool}", file=sys.stderr)
            return 1

        return run_steps(steps, root)


    if __name__ == "__main__":
        raise SystemExit(main())

## Component: tools/release/run_evidence_sweep.py

    #!/usr/bin/env python3
    """DEC-025 five-surface evidence sweep — the deterministic local merge gate.

    Runs the five evidence surfaces sequentially in F-4-safe order (cargo crate
    sweep, Python pytest, desktop Vitest with the wasm engine built first,
    Playwright e2e, desktop production build) and writes a machine-readable
    summary artifact bound to the current commit hash. This sweep is the required
    pre-push/fan-in evidence for every parallel agent development branch
    (`DEC-025`, recorded in `execution/_Decomposition/SOFTWARE_DECOMP.md` §12;
    basis `execution/_Coordination/_DECISIONS/D-05_ci_provider_workflow.md`
    Option D).

    The sweep is local-only: no network services, no signing, no publication
    credentials. A green sweep is development evidence, not a release claim,
    professional approval, certification, sealing, authentication, or
    code-compliance determination.
    """

    from __future__ import annotations

    import argparse
    import json
    import os
    import platform
    import shutil
    import subprocess
    import sys
    import time
    from dataclasses import dataclass
    from datetime import datetime, timezone
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[2]

    SCHEMA_VERSION = 2
    ARTIFACT_KIND = "openpipestress.evidence_sweep_summary"
    DECISION_BASIS = "DEC-025"
    DEFAULT_OUTPUT_DIR = "validation/evidence/sweeps"

    BOUNDARY_NOTE = (
        "Local-only development evidence. Not a release claim, professional "
        "approval, certification, sealing, authentication, or code-compliance "
        "determination."
    )


    @dataclass(frozen=True)
    class Surface:
        """One evidence surface: an ordered list of commands run sequentially."""

        surface_id: str
        description: str
        commands: tuple[tuple[str, ...], ...]


    def build_sweep_plan() -> list[Surface]:
        """The five surfaces in the DEC-025 / F-4-safe sequential order.

        The wasm engine build precedes Vitest because the Vitest setup pre-warms
        the engine and fails loudly when the generated artifact is absent. The
        Playwright root script rebuilds the wasm artifact itself
        (`test:e2e` = `build:wasm && playwright test`), which is safe because the
        sweep is strictly sequential and the build swaps atomically (F-4).
        """
        return [
            Surface(
                surface_id="cargo_crate_sweep",
                description="Rust crate tests across all discovered crate manifests.",
                commands=(
                    (
                        sys.executable,
                        "tools/release/check_release_readiness.py",
                        "--profile",
                        "cargo",
                        "--execute",
                    ),
                ),
            ),
            Surface(
                surface_id="python_pytest",
                description="Repository Python contract, governance, and validation tests.",
                commands=((sys.executable, "-m", "pytest", "-q", "tests"),),
            ),
            Surface(
                surface_id="desktop_vitest",
                description="Desktop unit/contract tests; wasm engine built first.",
                commands=(
                    ("npm", "run", "build:wasm:desktop"),
                    ("npm", "run", "test:desktop"),
                ),
            ),
            Surface(
                surface_id="desktop_playwright_e2e",
                description=(
                    "Playwright end-to-end smoke in a real Chrome browser: dev-server "
                    "lane, then production-dist lane via vite preview "
                    "(TP-APP-R2-WASMPKG-001)."
                ),
                commands=(
                    ("npm", "run", "test:e2e:desktop"),
                    ("npm", "run", "test:e2e:dist:desktop"),
                ),
            ),
            Surface(
                surface_id="desktop_production_build",
                description="Desktop production build (tsc -b && vite build).",
                commands=(("npm", "run", "build:desktop"),),
            ),
        ]


    def _capture(
        command: tuple[str, ...], root: Path, *, strip: bool = True
    ) -> str | None:
        try:
            completed = subprocess.run(
                command, cwd=root, capture_output=True, text=True, check=False
            )
        except OSError:
            return None
        if completed.returncode != 0:
            return None
        return completed.stdout.strip() if strip else completed.stdout


    def parse_porcelain_status(porcelain: str) -> list[str]:
        """Parse `git status --porcelain -z` output into the affected paths.

        Records are `XY <path>` terminated by NUL; rename/copy records carry the
        original path as a second NUL-terminated token. The X status character is
        a significant leading space for worktree-only changes (` M <path>`), so
        the captured output must never be whitespace-stripped before parsing.
        """
        paths: list[str] = []
        tokens = porcelain.split("\0")
        index = 0
        while index < len(tokens):
            record = tokens[index]
            index += 1
            if not record:
                continue
            status = record[:2]
            paths.append(record[3:])
            if "R" in status or "C" in status:
                if index < len(tokens) and tokens[index]:
                    paths.append(tokens[index])
                index += 1
        return sorted(paths)


    def collect_git_state(root: Path = ROOT) -> dict:
        """Bind the summary to the commit hash and record working-tree deltas.

        A failed git capture is recorded explicitly and must never read as a
        clean working tree: the DEC-025 gate binds evidence to the commit hash,
        so a summary that cannot verify its git state has to say so out loud
        (`working_tree_dirty` becomes null, never false).
        """
        commit = _capture(("git", "rev-parse", "HEAD"), root)
        branch = _capture(("git", "rev-parse", "--abbrev-ref", "HEAD"), root)
        porcelain = _capture(
            ("git", "status", "--porcelain", "-z"), root, strip=False
        )
        status_capture_failed = porcelain is None
        dirty_paths = parse_porcelain_status(porcelain or "")
        return {
            "commit_hash": commit,
            "branch": branch,
            "status_capture_failed": status_capture_failed,
            "working_tree_dirty": None if status_capture_failed else bool(dirty_paths),
            "dirty_paths": dirty_paths,
        }


    def git_state_unverified(git_state: dict) -> bool:
        """True when the summary cannot honestly bind to a verified git state."""
        return bool(git_state.get("status_capture_failed")) or not git_state.get(
            "commit_hash"
        )


    def collect_runtime_versions(root: Path = ROOT) -> dict:
        versions = {"platform": platform.platform(), "python": platform.python_version()}
        for name, command in (
            ("node", ("node", "--version")),
            ("npm", ("npm", "--version")),
            ("cargo", ("cargo", "--version")),
            ("rustc", ("rustc", "--version")),
        ):
            versions[name] = _capture(command, root)
        return versions


    def run_command(command: tuple[str, ...], root: Path) -> int:
        """Run one evidence command streaming output to the console."""
        completed = subprocess.run(command, cwd=root, check=False)
        return completed.returncode


    def run_sweep(surfaces: list[Surface], root: Path, runner=None) -> dict:
        """Execute surfaces sequentially, fail-fast, and return the summary body.

        A failing command fails its surface; later surfaces are recorded as
        `not_run` so the artifact states exactly which evidence exists for the
        bound commit.
        """
        if runner is None:
            runner = run_command
        started = datetime.now(timezone.utc)
        results: list[dict] = []
        failed = False

        for order, surface in enumerate(surfaces, start=1):
            entry: dict = {
                "order": order,
                "surface_id": surface.surface_id,
                "description": surface.description,
                "commands": [],
                "status": "not_run",
            }
            if failed:
                results.append(entry)
                continue

            surface_failed = False
            for command in surface.commands:
                print(f"[evidence-sweep] {surface.surface_id}: {' '.join(command)}", flush=True)
                start = time.monotonic()
                exit_code = runner(command, root)
                entry["commands"].append(
                    {
                        "argv": list(command),
                        "exit_code": exit_code,
                        "duration_seconds": round(time.monotonic() - start, 3),
                    }
                )
                if exit_code != 0:
                    surface_failed = True
                    break

            entry["status"] = "fail" if surface_failed else "pass"
            if surface_failed:
                failed = True
                print(
                    f"[evidence-sweep] FAILED at surface {surface.surface_id}; "
                    "remaining surfaces recorded as not_run",
                    file=sys.stderr,
                    flush=True,
                )
            results.append(entry)

        finished = datetime.now(timezone.utc)
        return {
            "artifact": ARTIFACT_KIND,
            "schema_version": SCHEMA_VERSION,
            "decision_basis": DECISION_BASIS,
            "boundary_note": BOUNDARY_NOTE,
            "git": collect_git_state(root),
            "runtime": collect_runtime_versions(root),
            "started_utc": started.isoformat(timespec="seconds"),
            "finished_utc": finished.isoformat(timespec="seconds"),
            "duration_seconds": round((finished - started).total_seconds(), 3),
            "surfaces": results,
            "overall_status": "fail" if failed else "pass",
        }


    def summary_filename(summary: dict) -> str:
        commit = (summary["git"]["commit_hash"] or "nocommit")[:12]
        if git_state_unverified(summary["git"]):
            dirty = "-gitunverified"
        elif summary["git"]["working_tree_dirty"]:
            dirty = "-dirty"
        else:
            dirty = ""
        stamp = summary["started_utc"].replace("-", "").replace(":", "")
        stamp = stamp.split("+")[0] + "Z"
        return f"SWEEP_{stamp}_{commit}{dirty}.json"


    def write_summary(summary: dict, output_dir: Path) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / summary_filename(summary)
        output_path.write_text(
            json.dumps(summary, indent=2, sort_keys=False) + "\n", encoding="utf-8"
        )
        return output_path


    def print_plan(surfaces: list[Surface], root: Path, execute: bool) -> None:
        mode = "execute" if execute else "dry-run"
        print(f"OpenPipeStress five-surface evidence sweep ({mode}) — {DECISION_BASIS}")
        print(f"repo: {root}")
        print("")
        print(f"surfaces (sequential, F-4-safe order): {len(surfaces)}")
        for order, surface in enumerate(surfaces, start=1):
            print(f"{order}. {surface.surface_id}")
            print(f"   {surface.description}")
            for command in surface.commands:
                print(f"   command: {' '.join(command)}")


    def missing_tools(surfaces: list[Surface]) -> list[str]:
        missing: list[str] = []
        for surface in surfaces:
            for command in surface.commands:
                executable = command[0]
                if Path(executable).exists():
                    continue
                if shutil.which(executable) is None and executable not in missing:
                    missing.append(executable)
        return missing


    def parse_args(argv: list[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Run the DEC-025 five-surface evidence sweep and write a "
                "commit-bound machine-readable summary."
            )
        )
        parser.add_argument(
            "--execute",
            action="store_true",
            help="Run the sweep. Without this flag, only print the plan.",
        )
        parser.add_argument(
            "--output-dir",
            default=DEFAULT_OUTPUT_DIR,
            help=f"Summary artifact directory relative to the repo root "
            f"(default: {DEFAULT_OUTPUT_DIR}).",
        )
        parser.add_argument(
            "--repo-root",
            default=str(ROOT),
            help="Repository root. Defaults to the root containing this script.",
        )
        return parser.parse_args(argv)


    def main(argv: list[str] | None = None) -> int:
        args = parse_args(sys.argv[1:] if argv is None else argv)
        root = Path(args.repo_root).resolve()
        if not root.exists():
            print(f"missing repository root: {root}", file=sys.stderr)
            return 2

        surfaces = build_sweep_plan()
        print_plan(surfaces, root, args.execute)
        sys.stdout.flush()

        if not args.execute:
            return 0

        tools = missing_tools(surfaces)
        if tools:
            print("missing required local tools:", file=sys.stderr)
            for tool in tools:
                print(f"  - {tool}", file=sys.stderr)
            return 1

        # The Playwright surface runs last, after the cargo + wasm + vitest surfaces
        # have loaded the machine. At Playwright's default worker count (~half the
        # cores) the extra Chromium workers are slow to reap under that load and
        # trip the internal 300s worker-stop grace ("worker process did not exit
        # within 300000ms after stop, force-killed it"), failing an otherwise
        # all-green run. Run the e2e workers serially for the gate; the configs read
        # PLAYWRIGHT_WORKERS and `setdefault` lets an explicit caller value win.
        os.environ.setdefault("PLAYWRIGHT_WORKERS", "1")

        summary = run_sweep(surfaces, root)
        output_path = write_summary(summary, root / args.output_dir)

        print("")
        print(f"[evidence-sweep] overall: {summary['overall_status']}")
        print(f"[evidence-sweep] commit: {summary['git']['commit_hash']}")
        if summary["git"]["working_tree_dirty"]:
            print(
                "[evidence-sweep] working tree dirty — summary records the deltas; "
                "the merge gate binds to a clean committed HEAD"
            )
        try:
            summary_ref = output_path.relative_to(root).as_posix()
        except ValueError:
            summary_ref = str(output_path)
        print(f"[evidence-sweep] summary: {summary_ref}")
        if git_state_unverified(summary["git"]):
            print(
                "[evidence-sweep] git state could not be verified — the summary "
                "is not commit-bound and does not satisfy the DEC-025 gate",
                file=sys.stderr,
            )
            return 1
        return 0 if summary["overall_status"] == "pass" else 1


    if __name__ == "__main__":
        raise SystemExit(main())

## Component: tools/validation/validate_dependencies_schema.py

    #!/usr/bin/env python3
    """Validate a dependency CSV file against the canonical v3.1 contract."""

    import argparse
    import csv
    import sys

    REQUIRED_COLUMNS = [
        "RegisterSchemaVersion", "DependencyID", "FromPackageID", "FromDeliverableID",
        "FromDeliverableName", "DependencyClass", "AnchorType", "Direction",
        "DependencyType", "TargetType", "TargetPackageID", "TargetDeliverableID",
        "TargetRefID", "TargetName", "TargetLocation", "Statement",
        "EvidenceFile", "SourceRef", "EvidenceQuote", "Explicitness",
        "RequiredMaturity", "ProposedMaturity", "SatisfactionStatus", "Confidence",
        "Origin", "FirstSeen", "LastSeen", "Status", "Notes"
    ]

    KNOWN_EXTENSIONS = ["EstimateImpactClass", "ConsumerHint"]

    CANONICAL_ENUMS = {
        "DependencyClass": {"ANCHOR", "EXECUTION"},
        "AnchorType": {"IMPLEMENTS_NODE", "TRACES_TO_REQUIREMENT", "NOT_APPLICABLE"},
        "Direction": {"UPSTREAM", "DOWNSTREAM"},
        "DependencyType": {"PREREQUISITE", "INTERFACE", "HANDOVER", "CONSTRAINT", "ENABLES", "OTHER"},
        "TargetType": {"DELIVERABLE", "PACKAGE", "WBS_NODE", "REQUIREMENT", "DOCUMENT", "EQUIPMENT", "EXTERNAL", "UNKNOWN"},
        "Explicitness": {"EXPLICIT", "IMPLICIT"},
        "SatisfactionStatus": {"TBD", "PENDING", "IN_PROGRESS", "SATISFIED", "WAIVED", "NOT_APPLICABLE"},
        "Confidence": {"HIGH", "MEDIUM", "LOW"},
        "Origin": {"DECLARED", "EXTRACTED"},
        "Status": {"ACTIVE", "RETIRED"},
    }


    def dependency_id(row: dict[str, str], fallback: str = "<missing>") -> str:
        return row.get("DependencyID", "").strip() or fallback


    def validate_row_semantics(rows: list[dict[str, str]]) -> list[str]:
        findings: list[str] = []
        for line_number, row in enumerate(rows, start=2):
            dep_id = dependency_id(row)

            for field, allowed in CANONICAL_ENUMS.items():
                value = row.get(field, "").strip()
                if value not in allowed:
                    findings.append(
                        f"Row {line_number} invalid {field}: {value!r} "
                        f"(DependencyID={dep_id}; allowed={', '.join(sorted(allowed))})"
                    )

            dependency_class = row.get("DependencyClass", "").strip()
            anchor_type = row.get("AnchorType", "").strip()
            dependency_type = row.get("DependencyType", "").strip()
            target_type = row.get("TargetType", "").strip()
            target_deliverable_id = row.get("TargetDeliverableID", "").strip()

            if dependency_class == "ANCHOR":
                if dependency_type != "OTHER":
                    findings.append(
                        f"Row {line_number} ANCHOR row must use DependencyType=OTHER "
                        f"(DependencyID={dep_id}; found {dependency_type!r})"
                    )
                if anchor_type == "NOT_APPLICABLE":
                    findings.append(
                        f"Row {line_number} ANCHOR row must not use AnchorType=NOT_APPLICABLE "
                        f"(DependencyID={dep_id})"
                    )

            if dependency_class == "EXECUTION" and anchor_type != "NOT_APPLICABLE":
                findings.append(
                    f"Row {line_number} EXECUTION row must use AnchorType=NOT_APPLICABLE "
                    f"(DependencyID={dep_id}; found {anchor_type!r})"
                )

            if target_type == "DELIVERABLE" and not target_deliverable_id:
                findings.append(
                    f"Row {line_number} TargetType=DELIVERABLE requires TargetDeliverableID "
                    f"(DependencyID={dep_id})"
                )
            if target_type and target_type != "DELIVERABLE" and target_deliverable_id:
                findings.append(
                    f"Row {line_number} non-deliverable TargetType must leave TargetDeliverableID blank "
                    f"(DependencyID={dep_id}; TargetType={target_type!r}; "
                    f"TargetDeliverableID={target_deliverable_id!r})"
                )

        return findings


    def validate(csv_path, schema_only=False):
        try:
            with open(csv_path, 'r', newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                header = next(reader)
                raw_rows = list(reader)
        except FileNotFoundError:
            return False, [f"ERROR: File not found: {csv_path}"], [], 0, []
        except StopIteration:
            return False, [f"ERROR: Empty file: {csv_path}"], [], 0, []
        except csv.Error as exc:
            return False, [f"ERROR: CSV parse error in {csv_path}: {exc}"], [], 0, []

        # Strip whitespace and BOM.
        header = [col.strip().lstrip('\ufeff') for col in header]
        missing = [col for col in REQUIRED_COLUMNS if col not in header]
        extensions = [col for col in header if col not in REQUIRED_COLUMNS]
        row_count = len(raw_rows)
        findings = []
        dict_rows: list[dict[str, str]] = []

        expected_width = len(header)
        for index, row in enumerate(raw_rows, start=2):
            if len(row) != expected_width:
                dependency_id = row[1] if len(row) > 1 else "<missing>"
                findings.append(
                    f"Row {index} field count mismatch: expected {expected_width}, "
                    f"found {len(row)} (DependencyID={dependency_id})"
                )
            padded = row + [""] * max(0, expected_width - len(row))
            dict_rows.append({name: padded[column_index] for column_index, name in enumerate(header)})

        if "RegisterSchemaVersion" in header:
            version_index = header.index("RegisterSchemaVersion")
            for index, row in enumerate(raw_rows, start=2):
                if len(row) <= version_index:
                    continue
                if row[version_index].strip() != "v3.1":
                    dependency_id = row[1] if len(row) > 1 else "<missing>"
                    findings.append(
                        f"Row {index} invalid RegisterSchemaVersion: "
                        f"{row[version_index]!r} (DependencyID={dependency_id})"
                    )

        if missing:
            findings.append(f"Missing columns ({len(missing)}): {', '.join(missing)}")

        if not schema_only and not missing:
            findings.extend(validate_row_semantics(dict_rows))

        return not findings, findings, extensions, row_count, header


    def parse_args(argv):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("csv_path")
        parser.add_argument(
            "--schema-only",
            action="store_true",
            help="Validate only CSV shape/version. Use only for historical legacy snapshots.",
        )
        return parser.parse_args(argv)


    if __name__ == '__main__':
        args = parse_args(sys.argv[1:])
        valid, findings, extensions, row_count, header = validate(args.csv_path, schema_only=args.schema_only)

        if not valid:
            print(f"INVALID: {args.csv_path}")
            for finding in findings:
                print(f"  {finding}")
            print(f"  Data rows: {row_count}")
            sys.exit(1)

        print(f"VALID: {args.csv_path}")
        print(f"  Columns: {len(header)} ({len(REQUIRED_COLUMNS)} required + {len(extensions)} extension)")
        print(f"  Data rows: {row_count}")
        if extensions:
            print(f"  Extensions: {', '.join(extensions)}")
        sys.exit(0)
