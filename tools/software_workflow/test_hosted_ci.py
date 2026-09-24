"""Real-diff routing and aggregate failures for hosted App/PEC coverage."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from hosted_ci import aggregate, make_plan, select_paths

PROFILE = json.loads((Path(__file__).resolve().parents[1] / "hosted-ci-routing.json").read_text())


class HostedCITests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "ci-test@example.invalid")
        self.git("config", "user.name", "CI routing fixture")
        self.write("README.md")
        self.base = self.commit()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.PIPE).decode().strip()

    def write(self, path, content="fixture"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def plan(self, base=None, event="pull_request"):
        return make_plan(self.root, PROFILE, event, base or self.base, "HEAD")

    def test_evergreen_instruction_pr_uses_only_bundle_and_governance(self):
        paths = ["AGENTS.md", "docs/SPEC.md", "projects/chirality-app-dev/AGENTS.md",
                 "projects/chirality-app-dev/loop/LOOP_INIT.md", "projects/chirality-piping/AGENTS.md",
                 "projects/chirality-piping/loop/LOOP_INIT.md",
                 "workflows/construct-local-work-graph/WORKFLOW.md",
                 "workflows/construct-local-work-graph/resources/work-graph-template.md"]
        paths += [f"projects/{p}/execution/_Coordination/NOTICE.md" for p in
                  ["chirality-app-dev", "chirality-piping", "chirality-runtime", "pec"]]
        for path in paths:
            self.write(path)
        self.commit()
        self.assertEqual(self.plan()["modes"], {"app": "instructions", "pec": "not-applicable"})

    def test_project_records_including_json_do_not_run_product_suites(self):
        paths = [f"projects/{project}/{folder}/{filename}" for project in
                 ["chirality-app-dev", "chirality-runtime", "pec"] for folder in
                 ["docs", "execution", "loop", "plans"] for filename in ["note.md", "state.json"]]
        self.assertEqual(select_paths(paths, PROFILE)["modes"], {"app": "not-applicable", "pec": "not-applicable"})

    def test_owned_product_and_shared_runtime_dependencies_select_consumers(self):
        for path, modes in [
            ("projects/chirality-app-dev/frontend/src/a.tsx", {"app": "full", "pec": "not-applicable"}),
            ("projects/pec/server/src/a.ts", {"app": "not-applicable", "pec": "full"}),
            ("projects/chirality-runtime/packages/client/src/a.ts", {"app": "full", "pec": "full"}),
            ("projects/chirality-runtime/package-lock.json", {"app": "full", "pec": "full"}),
            ("projects/chirality-app-dev/instructions/AGENTS.md", {"app": "instructions", "pec": "not-applicable"}),
        ]:
            with self.subTest(path=path):
                self.assertEqual(select_paths([path], PROFILE)["modes"], modes)

    def test_earlier_source_commit_is_not_hidden_by_later_docs(self):
        self.write("projects/chirality-app-dev/frontend/src/a.tsx")
        self.commit()
        self.write("docs/notes.md")
        self.commit()
        plan = self.plan()
        self.assertEqual(plan["modes"]["app"], "full")
        self.assertEqual(len(plan["paths"]), 2)

    def test_consumed_doc_deletion_keeps_its_executable_app_checks(self):
        path = "projects/chirality-app-dev/docs/harness/reliance_boundary_register.md"
        self.write(path)
        base = self.commit()
        (self.root / path).unlink()
        self.commit()
        self.assertEqual(self.plan(base)["modes"]["app"], "full")

    def test_move_from_product_to_records_still_checks_removed_product(self):
        original = "projects/pec/server/src/a.ts"
        self.write(original)
        base = self.commit()
        self.write("projects/pec/docs/a.ts")
        (self.root / original).unlink()
        self.commit()
        plan = self.plan(base)
        self.assertIn(original, plan["paths"])
        self.assertEqual(plan["modes"]["pec"], "full")

    def test_newline_in_filename_cannot_hide_product_path(self):
        path = "projects/chirality-app-dev/frontend/src/odd\nname.ts"
        self.write(path)
        self.commit()
        self.assertIn(path, self.plan()["paths"])
        self.assertEqual(self.plan()["modes"]["app"], "full")

    def test_unknown_inputs_fall_back_to_owner_or_both_products(self):
        for path, expected in [
            ("projects/chirality-app-dev/new-input.bin", {"app": "full", "pec": "not-applicable"}),
            ("projects/chirality-app-dev/new-runtime/docs/input.json", {"app": "full", "pec": "not-applicable"}),
            ("projects/pec/new-input.bin", {"app": "not-applicable", "pec": "full"}),
            ("unknown-root-input.bin", {"app": "full", "pec": "full"}),
        ]:
            selection = select_paths([path], PROFILE)
            self.assertEqual(selection["unmatched_paths"], [path])
            self.assertEqual(selection["modes"], expected)

    def test_policy_changes_require_full_consumer_checks(self):
        selection = select_paths(["tools/hosted-ci-routing.json"], PROFILE)
        self.assertEqual(selection["modes"], {"app": "full", "pec": "full"})

    def test_missing_base_and_manual_dispatch_request_full_coverage(self):
        for plan in [self.plan(base="missing-ref"), self.plan(event="workflow_dispatch")]:
            self.assertEqual(plan["modes"], {"app": "full", "pec": "full"})

    def test_required_selected_job_failure_cancellation_or_skip_blocks_result(self):
        for state in ["failure", "cancelled", "skipped", ""]:
            self.assertFalse(aggregate("app", "full", "success", state))
            self.assertFalse(aggregate("app", "instructions", "success", "skipped", state))
        self.assertFalse(aggregate("pec", "not-applicable", "failure", "skipped"))
        self.assertFalse(aggregate("app", "typo", "success", "skipped"))
        self.assertTrue(aggregate("app", "instructions", "success", "skipped", "success"))
        self.assertTrue(aggregate("pec", "not-applicable", "success", "skipped"))
        self.assertTrue(aggregate("app", "full", "success", "success"))


if __name__ == "__main__":
    unittest.main()
