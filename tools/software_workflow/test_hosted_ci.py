"""Real-diff routing and aggregate failures for hosted App/PEC coverage."""
import json
from pathlib import Path
import subprocess
import tempfile
import sys
import unittest

from hosted_ci import aggregate, make_plan, select_paths, SUITES

PROFILE = json.loads((Path(__file__).resolve().parents[1] / "hosted-ci-routing.json").read_text())


def modes(**overrides):
    return {**dict.fromkeys(SUITES, "not-applicable"), **overrides}


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
        self.assertEqual(self.plan()["modes"], modes(app="instructions", **{"app-v4": "full"}))

    def test_project_records_including_json_do_not_run_product_suites(self):
        paths = [f"projects/{project}/{folder}/{filename}" for project in
                 ["chirality-app-dev", "chirality-runtime", "pec"] for folder in
                 ["docs", "execution", "loop", "plans"] for filename in ["note.md", "state.json"]]
        self.assertEqual(select_paths(paths, PROFILE)["modes"], modes(app="not-applicable", pec="not-applicable"))

    def test_app_v4_records_and_prose_do_not_run_product_suites(self):
        paths = [f"projects/chirality-app-v4/{folder}/{filename}" for folder in
                 ["execution/_Coordination/AgentRuns/RUN", "docs", "conceptual", "foundation", "reference", "loop", "init"]
                 for filename in ["note.md", "state.json"]]
        paths += ["projects/chirality-app-v4/AGENTS.md", "projects/chirality-app-v4/README.md"]
        self.assertEqual(select_paths(paths, PROFILE)["modes"], modes(app="not-applicable", pec="not-applicable"))
        # Its application source selects App v4, not unrelated legacy products.
        self.assertEqual(select_paths(["projects/chirality-app-v4/app/src/main.rs"], PROFILE)["modes"],
                         modes(**{"app-v4": "full"}))

    def test_hash_bound_scope_selects_app_v4(self):
        self.assertEqual(select_paths([
            "projects/chirality-app-v4/execution/PKG-02/DEL-02-04/ScopeOfWork.md"
        ], PROFILE)["modes"], modes(**{"app-v4": "full"}))

    def test_owned_product_and_shared_runtime_dependencies_select_consumers(self):
        for path, expected_modes in [
            ("projects/chirality-app-dev/frontend/src/a.tsx", modes(app="full", pec="not-applicable")),
            ("projects/pec/server/src/a.ts", modes(app="not-applicable", pec="full")),
            ("projects/chirality-runtime/packages/client/src/a.ts", modes(app="full", pec="full")),
            ("projects/chirality-runtime/package-lock.json", modes(app="full", pec="full")),
            ("projects/chirality-app-dev/instructions/AGENTS.md", modes(app="instructions", pec="not-applicable")),
        ]:
            with self.subTest(path=path):
                self.assertEqual(select_paths([path], PROFILE)["modes"], expected_modes)

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
            ("projects/chirality-app-dev/new-input.bin", modes(app="full", pec="not-applicable")),
            ("projects/chirality-app-dev/new-runtime/docs/input.json", modes(app="full", pec="not-applicable")),
            ("projects/pec/new-input.bin", modes(app="not-applicable", pec="full")),
            ("unknown-root-input.bin", dict.fromkeys(SUITES, "full")),
            ("projects/chirality-app-v4/unmapped/new-code.bin", modes(**{"app-v4": "full"})),
            ("projects/chirality-piping/new-code.bin", modes(piping="full", **{"piping-numerical": "full"})),
        ]:
            selection = select_paths([path], PROFILE)
            self.assertEqual(selection["unmatched_paths"], [path])
            self.assertEqual(selection["modes"], expected)

    def test_policy_changes_require_full_consumer_checks(self):
        selection = select_paths(["tools/hosted-ci-routing.json"], PROFILE)
        self.assertEqual(selection["modes"], dict.fromkeys(SUITES, "full"))

    def test_missing_base_and_manual_dispatch_request_full_coverage(self):
        for plan in [self.plan(base="missing-ref"), self.plan(event="workflow_dispatch")]:
            self.assertEqual(plan["modes"], dict.fromkeys(SUITES, "full"))

    def test_product_paths_and_consumed_design_select_without_deliverable_mappings(self):
        for path in ('projects/chirality-app-v4/app/src-tauri/src/workflow_catalog.rs',
                     'projects/chirality-app-v4/execution/PKG-04/DEL-04-03/Design/RS_RECORD.schema.json'):
            self.assertEqual(select_paths([path], PROFILE)['modes'], modes(**{'app-v4':'full'}))
        selection = select_paths(['projects/chirality-piping/core/solver/src/lib.rs'], PROFILE)
        self.assertEqual(selection['modes'], modes(piping='full', **{'piping-numerical':'full'}))
        self.assertEqual(select_paths(['projects/chirality-piping/docs/note.md'], PROFILE)['modes'], modes())

    def test_piping_python_implementation_and_tests_select_python_lane(self):
        for path in ('projects/chirality-piping/tools/product_preview/validate.py',
                     'projects/chirality-piping/tests/product_preview/test_contract.py',
                     'projects/chirality-piping/tests/security/test_permissions.py'):
            selection = select_paths([path], PROFILE)
            self.assertEqual(selection['modes']['piping-numerical'], 'full')
            self.assertEqual(selection['modes']['piping'], 'full')

    def test_new_required_results_never_launder_missing_failed_or_cancelled_checks(self):
        for suite in ('app-v4','piping','piping-numerical'):
            for state in ('failure','cancelled','skipped',''):
                self.assertFalse(aggregate(suite,'full','success',state))
            self.assertFalse(aggregate(suite,'not-applicable','failure','skipped'))
            self.assertTrue(aggregate(suite,'not-applicable','success','skipped'))
            self.assertTrue(aggregate(suite,'full','success','success'))

    def test_aggregate_cli_failure_returns_failure_without_traceback(self):
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name('hosted_ci.py')),
            'aggregate', '--suite', 'app-v4', '--mode', 'full', '--selection', 'success',
            '--product', 'skipped'], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 1)
        self.assertIn('did not complete', completed.stdout)
        self.assertNotIn('Traceback', completed.stderr)

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
