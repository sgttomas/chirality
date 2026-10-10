"""Behavioral preservation checks for the one-time dependency migration."""
import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml

spec = importlib.util.spec_from_file_location("migration", Path(__file__).with_name("migrate_dependencies.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

FIELDS = ["DependencyID", "FromDeliverableID", "FromDeliverableName", "DependencyClass", "Status", "Direction", "TargetType", "TargetDeliverableID", "TargetRefID", "TargetName", "TargetLocation", "TargetPackageID", "Statement", "Notes", "RequiredMaturity", "EvidenceFile", "Constraint", "When"]


def row(identifier, owner="DEL-01-01", target="DEL-01-02", **kwargs):
    result = {k: "" for k in FIELDS}
    result.update(DependencyID=identifier, FromDeliverableID=owner, FromDeliverableName=owner, DependencyClass="EXECUTION", Status="ACTIVE", Direction="UPSTREAM", TargetType="DELIVERABLE", TargetDeliverableID=target, Statement="Supply the stable interface.")
    result.update(kwargs)
    return result


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.project = "projects/example"
        self.execution = self.root / self.project / "execution"
        self.dag = self.execution / "_DAG/DAG-004"
        self.dag.mkdir(parents=True)
        self.folders = {}
        for id_ in ("DEL-01-01", "DEL-01-02"):
            p = self.execution / "PKG-01" / id_
            p.mkdir(parents=True)
            self.folders[id_] = p
            (p / "ScopeOfWork.md").write_text("Contract")
        self.csv(self.dag / "DependencyEdges.csv", [])
        self.csv(self.dag / "CandidateEdges.csv", [])
        self.csv(self.folders["DEL-01-01"] / "Dependencies.csv", [])
        self.csv(self.folders["DEL-01-02"] / "Dependencies.csv", [])

    def tearDown(self):
        self.tmp.cleanup()

    def csv(self, path, rows):
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def run_migration(self, ref=None):
        return m.migrate(m.Sources(self.root, self.project, ref))

    def test_distinct_conditions_and_supplier_restrictions_survive(self):
        a = row("a", Notes="Only before qualification", RequiredMaturity="INITIALIZED")
        b = row("b", Statement="Supply the installed interface.", Constraint="Offline only")
        c = row("c", owner="DEL-01-02", target="DEL-01-01", Direction="DOWNSTREAM", Notes="Never transfer credentials")
        self.csv(self.folders["DEL-01-01"] / "Dependencies.csv", [a, b])
        self.csv(self.folders["DEL-01-02"] / "Dependencies.csv", [c])
        self.csv(self.dag / "CandidateEdges.csv", [a])
        docs, report = self.run_migration()
        needs = docs["DEL-01-01"]["needs"]
        self.assertEqual(len(needs), 3)
        self.assertTrue(all(n["from"] == "DEL-01-02" and n["gating"] is False for n in needs))
        combined = str(needs)
        for text in ("Only before qualification", "INITIALIZED", "Offline only", "Never transfer credentials"):
            self.assertIn(text, combined)
        self.assertEqual(report["dag"]["migrated_pairs"], 1)
        self.assertEqual(report["dag"]["missing_pairs"], [])

    def test_equivalent_only_consolidation_with_named_partner(self):
        self.csv(self.folders["DEL-01-01"] / "Dependencies.csv", [row("a"), row("b"), row("c", Statement="A different need")])
        docs, report = self.run_migration()
        self.assertEqual(len(docs["DEL-01-01"]["needs"]), 2)
        account = {x["id"]: x for x in report["accounting"]}
        self.assertEqual(account["b"]["partner"], "a")
        self.assertEqual(account["c"]["disposition"], "preserved")

    def test_non_deliverable_outgoing_unknown_retired_anchor_accounting(self):
        rows = [row("external", TargetType="EXTERNAL", TargetRefID="PEC"), row("document", TargetType="DOCUMENT", TargetLocation="docs/input.md"), row("package", TargetType="PACKAGE", TargetPackageID="PKG-02"), row("unknown", TargetType="UNKNOWN"), row("outgoing", TargetType="EXTERNAL", TargetRefID="SWBPIPE", Direction="DOWNSTREAM"), row("retired", Status="RETIRED"), row("anchor", DependencyClass="ANCHOR")]
        self.csv(self.folders["DEL-01-01"] / "Dependencies.csv", rows)
        docs, report = self.run_migration()
        needs = docs["DEL-01-01"]["needs"]
        self.assertEqual({n["from"] for n in needs}, {"external:PEC", "doc:docs/input.md", "package:PKG-02", "unknown", "external:SWBPIPE"})
        outgoing = next(n for n in needs if n["from"] == "external:SWBPIPE")
        self.assertEqual(outgoing["direction"], "downstream")
        self.assertFalse(outgoing["gating"])
        self.assertEqual(len(report["accounting"]), 7)
        self.assertEqual(report["summary"]["retired"], 1)
        self.assertEqual(report["summary"]["anchors"], 1)
        self.assertFalse((self.root / "projects/SWBPIPE").exists())

    def test_markdown_only_declaration_flagged_not_imported(self):
        (self.folders["DEL-01-01"] / "_DEPENDENCIES.md").write_text("## Declared Upstream\n- Need DEL-01-02 after the owner selects the interface.\n## Declared Downstream\n- None declared at initial setup.\n## Run Notes\nDo not import me\n")
        docs, report = self.run_migration()
        self.assertEqual(docs["DEL-01-01"]["needs"], [])
        self.assertEqual(len(report["flags"]), 1)
        self.assertEqual(report["flags"][0]["kind"], "markdown_declaration")

    def test_source_ref_rerun_after_csv_removal_preserves_metadata(self):
        self.csv(self.folders["DEL-01-01"] / "Dependencies.csv", [row("a", EvidenceFile="ScopeOfWork.md")])
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "source"], check=True)
        docs, _ = self.run_migration("HEAD")
        dry = m.write_documents(self.root, self.project, docs)
        self.assertEqual(len(dry), 2)
        self.assertFalse((self.folders["DEL-01-01"] / "deliverable.yaml").exists())
        m.write_documents(self.root, self.project, docs, True)
        for folder in self.folders.values():
            (folder / "Dependencies.csv").unlink()
        path = self.folders["DEL-01-01"] / "deliverable.yaml"
        data = yaml.safe_load(path.read_text())
        data["code_paths"] = ["src/**"]
        path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100))
        docs, _ = self.run_migration("HEAD")
        self.assertEqual(m.write_documents(self.root, self.project, docs, True), [])
        self.assertEqual(yaml.safe_load(path.read_text())["code_paths"], ["src/**"])

    def test_downstream_only_inversion_and_new_pair_not_assumed_gating(self):
        self.csv(self.folders["DEL-01-02"] / "Dependencies.csv", [row("out", owner="DEL-01-02", target="DEL-01-01", Direction="DOWNSTREAM", When="after interface choice")])
        docs, report = self.run_migration()
        need = docs["DEL-01-01"]["needs"][0]
        self.assertEqual(need["from"], "DEL-01-02")
        self.assertNotIn("gating", need)
        self.assertEqual(need["when"], "When: after interface choice")
        self.assertEqual(report["dag"]["new_pairs"], [["DEL-01-01", "DEL-01-02"]])

    def test_document_suppliers_relocate_and_preserve_section_in_condition(self):
        old = 'execution/PKG-01_Old/1_Working/DEL-01-01_Old/Design/contract.md §10 (draft)'
        self.csv(self.folders['DEL-01-01'] / 'Dependencies.csv', [row('doc', TargetType='DOCUMENT', TargetLocation=old)])
        docs, _ = self.run_migration()
        m.write_documents(self.root, self.project, docs, True)
        path = self.folders['DEL-01-01'] / 'deliverable.yaml'
        need = yaml.safe_load(path.read_text())['needs'][0]
        self.assertEqual(need['from'], 'doc:execution/PKG-01/DEL-01-01/Design/contract.md')
        self.assertIn('§10 (draft)', need['condition'])
        docs, _ = self.run_migration()
        self.assertEqual(m.write_documents(self.root, self.project, docs, True), [])

    def test_symlink_destination_cannot_escape(self):
        docs, _ = self.run_migration()
        outside = self.root / "elsewhere"
        outside.mkdir()
        (self.folders["DEL-01-01"] / "deliverable.yaml").symlink_to(outside / "data.yaml")
        with self.assertRaisesRegex(ValueError, "escapes project"):
            m.write_documents(self.root, self.project, docs, True)


if __name__ == "__main__":
    unittest.main()
