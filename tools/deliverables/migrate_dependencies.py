#!/usr/bin/env python3
"""Migrate current dependency sources without inferring fulfilment or new gates.

Dry-run by default. --apply writes only deliverable.yaml in existing deliverable
folders. --source-ref reads legacy inputs from Git after their working copies
have been removed. JSON accounting goes to stdout, never into the project.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import io
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml

ID = re.compile(r"DEL-\d{2,3}-\d{2,3}")
SOURCE = re.compile(r"/execution/PKG[^/]+/(?:1_Working/)?DEL[^/]+/(Dependencies\.csv|_DEPENDENCIES\.md)$")
EMPTY = {"", "TBD", "UNKNOWN", "NOT_APPLICABLE", "N/A"}


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True)


class Sources:
    def __init__(self, root, project, ref=None):
        self.root = Path(root).resolve()
        self.project = Path(project).as_posix().rstrip("/")
        self.ref = git(self.root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").strip() if ref else None
        if self.ref:
            self.paths = git(self.root, "ls-tree", "-r", "--name-only", self.ref, "--", self.project).splitlines()
        else:
            self.paths = [p.relative_to(self.root).as_posix() for p in (self.root / self.project / "execution").glob("PKG*/**/*") if p.is_file()]

    def read(self, path):
        if self.ref:
            return git(self.root, "show", f"{self.ref}:{path}")
        return (self.root / path).read_text(encoding="utf-8-sig")

    def exists(self, path):
        return path in self.paths if self.ref else (self.root / path).is_file()


def parse_csv(text, source):
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")))
    rows = list(reader)
    if any(None in r or None in r.values() for r in rows):
        raise ValueError(f"Ragged CSV: {source}")
    return rows


def pair(row):
    a, b = row["FromDeliverableID"], row.get("TargetDeliverableID", "")
    return (a, b) if row["Direction"] == "UPSTREAM" else (b, a)


def meaningful(value):
    return value.strip() if value.strip().upper() not in EMPTY else ""


def target(row):
    kind = row.get("TargetType", "UNKNOWN")
    if kind == "DELIVERABLE":
        return row.get("TargetDeliverableID") or "unknown"
    if kind == "UNKNOWN":
        return "unknown"
    if kind == "PACKAGE":
        value = meaningful(row.get("TargetPackageID", "")) or meaningful(row.get("TargetRefID", ""))
        return "package:" + (value or "unknown")
    if kind == "DOCUMENT":
        value = meaningful(row.get("TargetLocation", "")) or meaningful(row.get("TargetRefID", "")) or meaningful(row.get("TargetName", ""))
        return "doc:" + (value or "unknown")
    if kind == "EXTERNAL":
        value = meaningful(row.get("TargetRefID", "")) or meaningful(row.get("TargetName", ""))
        return "external:" + (value or "unknown")
    return "unknown"


def condition(row):
    """Preserve prose, including restrictions outside Statement; never reinterpret it."""
    parts = [row.get("Statement", "").strip()]
    for key in ("Constraint", "Constraints", "Notes"):
        value = meaningful(row.get(key, ""))
        if value:
            parts.append(f"{key}: {value}")
    # Maturity is an input condition in the old source, not a lifecycle verdict.
    maturity = meaningful(row.get("RequiredMaturity", ""))
    if maturity:
        parts.append(f"Required input maturity in source: {maturity}; this is not a fulfilment or completion claim.")
    if row.get("TargetType") != "DELIVERABLE":
        details = [f"{k}: {v}" for k in ("TargetName", "TargetRefID", "TargetLocation") if (v := meaningful(row.get(k, "")))]
        if details:
            parts.append("Target description — " + "; ".join(details))
    if not parts[0]:
        raise ValueError(f"Missing condition: {row.get('DependencyID')}")
    return "\n\n".join(parts)


def declared_lines(text):
    section = None
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            section = "UPSTREAM" if line.startswith("## Declared Upstream") else "DOWNSTREAM" if line.startswith("## Declared Downstream") else None
            continue
        stripped = line.strip()
        if not section or not stripped or stripped == "---" or stripped.startswith("<!--"):
            continue
        if re.match(r"^[-*]?\s*(?:None declared|None\.?$|No (?:human[- ]|individual )?(?:declared |declarations|dependencies))", stripped, re.I):
            continue
        yield number, section, stripped


def destination_folders(root, project):
    result = {}
    for p in sorted((root / project / "execution").glob("PKG*/**/DEL*")):
        if not p.is_dir() or not ID.fullmatch(p.name.split("_", 1)[0]):
            continue
        identifier = p.name.split("_", 1)[0]
        if identifier in result:
            raise ValueError(f"Duplicate deliverable folder: {identifier}")
        result[identifier] = p
    return result


def migrate(source, dag="_DAG/DAG-004"):
    rows, identities, per_file = [], {}, {}
    report = {"source_revision": source.ref or "working-tree", "accounting": [], "flags": [], "per_deliverable": {}, "dag": {}}
    csv_paths = sorted(p for p in source.paths if SOURCE.search("/" + p) and p.endswith("Dependencies.csv"))
    if not csv_paths:
        raise ValueError("No canonical dependency CSVs found; use --source-ref after migration")
    for path in csv_paths:
        parsed = parse_csv(source.read(path), path)
        folder_id = Path(path).parent.name.split("_", 1)[0]
        if not ID.fullmatch(folder_id):
            raise ValueError(f"Malformed folder identity: {path}")
        counts = Counter(total=len(parsed))
        seen = set()
        for line, row in enumerate(parsed, 2):
            depid = row.get("DependencyID", "")
            if not depid or depid in seen:
                raise ValueError(f"Missing or duplicate DependencyID: {path}:{line}")
            seen.add(depid)
            if row.get("FromDeliverableID") != folder_id:
                raise ValueError(f"Source identity mismatch: {path}:{line}")
            identities.setdefault(folder_id, row.get("FromDeliverableName", ""))
            row = dict(row, _source=path, _line=line)
            if row.get("Status") == "RETIRED":
                counts["retired"] += 1
                report["accounting"].append({"source": f"{path}:{line}", "id": depid, "disposition": "excluded", "reason": "retired"})
            elif row.get("DependencyClass") == "ANCHOR":
                counts["anchors"] += 1
                report["accounting"].append({"source": f"{path}:{line}", "id": depid, "disposition": "excluded", "reason": "anchor; retained sources belong in ScopeOfWork"})
            elif row.get("Status") == "ACTIVE" and row.get("DependencyClass") == "EXECUTION":
                if row.get("Direction") not in ("UPSTREAM", "DOWNSTREAM"):
                    raise ValueError(f"Invalid direction: {path}:{line}")
                rows.append(row)
                counts["active_execution"] += 1
            else:
                raise ValueError(f"Unsupported row status/class: {path}:{line}")
        identities.setdefault(folder_id, "")
        per_file[folder_id] = counts
    layers = {}
    for filename, gating in (("DependencyEdges.csv", True), ("CandidateEdges.csv", False)):
        path = f"{source.project}/execution/{dag}/{filename}"
        if not source.exists(path):
            raise ValueError(f"Missing DAG layer: {path}; specify --dag for this project")
        for row in parse_csv(source.read(path), path):
            arc = pair(row)
            if arc in layers:
                raise ValueError(f"DAG pair appears twice: {arc}")
            layers[arc] = gating
    docs = {identifier: {"id": identifier, **({"name": name} if name else {}), "needs": []} for identifier, name in sorted(identities.items())}
    exact, migrated_pairs = {}, set()
    groups = defaultdict(list)
    for row in sorted(rows, key=lambda r: (r["Direction"] != "UPSTREAM", r["_source"], r["DependencyID"])):
        owner = row["FromDeliverableID"]
        endpoint = target(row)
        if endpoint.startswith("doc:" + source.project + "/"):
            endpoint = "doc:" + endpoint[len("doc:" + source.project + "/"):]
        need = {"from": endpoint, "condition": condition(row)}
        arc = None
        if row["TargetType"] == "DELIVERABLE":
            if not ID.fullmatch(endpoint):
                raise ValueError(f"Malformed target identity: {row['_source']}:{row['_line']}")
            arc = pair(row)
            if row["Direction"] == "DOWNSTREAM" and endpoint in docs:
                owner, need["from"] = endpoint, row["FromDeliverableID"]
            elif row["Direction"] == "DOWNSTREAM":
                need["direction"] = "downstream"
            if arc[0] in docs and arc[1] in docs:
                migrated_pairs.add(arc)
                if arc in layers:
                    need["gating"] = layers[arc]
                else:
                    report["flags"].append({"id": row["DependencyID"], "kind": "pair_not_in_baseline", "pair": list(arc)})
            else:
                report["flags"].append({"id": row["DependencyID"], "kind": "unresolved_deliverable", "target": endpoint})
        elif row["Direction"] == "DOWNSTREAM":
            need.update(direction="downstream", gating=False)
            report["flags"].append({"id": row["DependencyID"], "kind": "nonlocal_downstream_preserved", "target": endpoint})
        if endpoint == "unknown":
            report["flags"].append({"id": row["DependencyID"], "kind": "unknown_target"})
        timing = [f"{k}: {row[k].strip()}" for k in ("When", "Timing", "PointOfNeed") if meaningful(row.get(k, ""))]
        if timing:
            need["when"] = "; ".join(timing)
        # Evidence belongs to the original declarer even after downstream inversion.
        evidence = meaningful(row.get("EvidenceFile", ""))
        if evidence:
            original = Path(row["_source"]).parent
            if not evidence.startswith(("/", "projects/")):
                evidence = (original / evidence).as_posix()
            if evidence.startswith(source.project + "/"):
                evidence = evidence[len(source.project) + 1:]
            need["evidence"] = evidence
        signature = (owner, json.dumps(need, sort_keys=True))
        account = {"source": f"{row['_source']}:{row['_line']}", "id": row["DependencyID"], "consumer": owner}
        if signature in exact:
            account.update(disposition="consolidated", partner=exact[signature]["id"], need=exact[signature]["need"])
            per_file[row["FromDeliverableID"]]["consolidated"] += 1
        else:
            index = len(docs[owner]["needs"])
            docs[owner]["needs"].append(need)
            account.update(disposition="preserved", need=index)
            exact[signature] = account
            per_file[row["FromDeliverableID"]]["preserved"] += 1
        report["accounting"].append(account)
        if arc:
            groups[arc].append(row)
    # Differing maturity/restrictions remain intact, and are visible for judgment.
    for arc, members in groups.items():
        maturities = {r.get("RequiredMaturity", "") for r in members}
        if len(maturities) > 1:
            report["flags"].append({"kind": "maturity_difference", "pair": list(arc), "ids": [r["DependencyID"] for r in members], "values": sorted(maturities)})
    for path in sorted(p for p in source.paths if SOURCE.search("/" + p) and p.endswith("_DEPENDENCIES.md")):
        for line, direction, text in declared_lines(source.read(path)):
            # Only a direct row-ID citation or identical statement establishes coverage.
            local = [r for r in rows if Path(r["_source"]).parent == Path(path).parent and r["Direction"] == direction]
            if not any(re.search(rf"(?<![\w-]){re.escape(r['DependencyID'])}(?![\w-])", text) or text.lstrip("-* ") == r.get("Statement", "") for r in local):
                report["flags"].append({"kind": "markdown_declaration", "source": f"{path}:{line}", "direction": direction, "text": text})
    report["per_deliverable"] = {k: dict(v) for k, v in sorted(per_file.items())}
    report["dag"] = {"baseline": dag, "admitted_pairs": sum(layers.values()), "held_pairs": sum(not v for v in layers.values()), "migrated_pairs": len(migrated_pairs), "missing_pairs": [list(p) for p in sorted(set(layers) - migrated_pairs)], "new_pairs": [list(p) for p in sorted(migrated_pairs - set(layers))], "non_gating_preserved": sum(layers[p] is False for p in migrated_pairs & layers.keys()), "rule": "ACTIVE EXECUTION deliverable pairs, UPSTREAM consumer or inverted DOWNSTREAM, topology deduplicated only; accepted admitted/held classification preserved"}
    counts = Counter()
    for c in per_file.values():
        counts.update(c)
    report["summary"] = {**dict(counts), "deliverables": len(docs), "needs": sum(len(d["needs"]) for d in docs.values()), "flags": dict(Counter(f["kind"] for f in report["flags"]))}
    return docs, report


def write_documents(root, project, docs, apply=False):
    folders = destination_folders(root, project)
    missing = sorted(set(docs) - folders.keys())
    if missing:
        raise ValueError(f"No existing destination folder for {missing}")
    changes = []
    planned = []
    for identifier, migrated in docs.items():
        destination = folders[identifier] / "deliverable.yaml"
        if not destination.resolve().is_relative_to((root / project).resolve()):
            raise ValueError(f"Destination escapes project: {destination}")
        existing = yaml.safe_load(destination.read_text()) if destination.exists() else {}
        if existing and (not isinstance(existing, dict) or existing.get("id") != identifier):
            raise ValueError(f"Existing YAML identity mismatch: {destination}")
        # Metadata seeded by the caller is preserved on reruns; migration owns needs.
        document = {**(existing or {}), **migrated}
        # Rewrite legacy evidence paths through the current destination mapping.
        for need in document["needs"]:
            evidence = need.get("evidence", "")
            match = re.search(r"(?:^|/)(DEL-\d{2,3}-\d{2,3})(?:_[^/]*)?/", evidence)
            if match and match[1] in folders:
                suffix = evidence[match.end():]
                need["evidence"] = (folders[match[1]].relative_to(root / project) / suffix).as_posix()
        text = yaml.safe_dump(document, allow_unicode=True, sort_keys=False, width=100)
        if not destination.exists() or destination.read_text() != text:
            changes.append(destination.relative_to(root).as_posix())
            planned.append((destination, text))
    # Validate every destination before the first write.
    if apply:
        for destination, text in planned:
            destination.write_text(text)
    return changes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default="projects/chirality-app-v4")
    parser.add_argument("--source-ref")
    parser.add_argument("--dag", default="_DAG/DAG-004", help="DAG path relative to execution")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--summary", action="store_true", help="Print counts and flags only; default includes full accounting")
    args = parser.parse_args(argv)
    try:
        root = Path(git(Path.cwd(), "rev-parse", "--show-toplevel").strip())
        project = Path(args.project)
        if project.is_absolute() or not (root / project).resolve().is_relative_to(root):
            raise ValueError("Project must be a repository-relative contained path")
        source = Sources(root, project, args.source_ref)
        docs, report = migrate(source, args.dag)
        report["changed_files"] = write_documents(root, project, docs, args.apply)
        report["applied"] = args.apply
        if args.summary:
            report.pop("accounting")
            report.pop("per_deliverable")
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError, yaml.YAMLError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
