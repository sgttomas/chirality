"""Hosted routing must receive PR changes and retain an honest result gate."""
from pathlib import Path
import json

import yaml
from select_affected_checks import select_checks

ROOT = Path(__file__).resolve().parents[2]


def workflow(name):
    return yaml.load((ROOT / ".github/workflows" / name).read_text(), Loader=yaml.BaseLoader)


def test_changes_to_hosted_workflows_select_their_structural_tests():
    profile = json.loads((ROOT / "tools/tools-test-routing.json").read_text())
    for name in ["harness-premerge.yml", "pec-tests.yml"]:
        selection = select_checks(profile, [f".github/workflows/{name}"])
        assert "software_workflow" in selection["checks"]


def test_every_pr_change_reaches_selection_and_full_dispatch_is_available():
    for name in ["harness-premerge.yml", "pec-tests.yml"]:
        config = workflow(name)
        trigger = config["on"]["pull_request"]
        assert set(trigger["types"]) >= {"opened", "synchronize", "reopened"}
        # Instruction/doc/record changes must reach the selector, even when no
        # product job is required. Outer path/branch filters would hide them.
        assert not set(trigger) & {"paths", "paths-ignore", "branches", "branches-ignore"}
        assert "workflow_dispatch" in config["on"]
        assert "if" not in config["jobs"]["selection"]


def test_stable_result_waits_for_all_routes_even_when_a_required_route_fails():
    for name, products in [("harness-premerge.yml", {"instructions", "harness-premerge"}),
                           ("pec-tests.yml", {"pec"})]:
        jobs = workflow(name)["jobs"]
        result = jobs["result"]
        assert set(result["needs"]) == {"selection", *products}
        assert result["if"] == "always()"
        for product in products:
            assert jobs[product]["needs"] == "selection"
            assert "needs.selection.outputs.mode" in jobs[product]["if"]


def test_runner_context_is_not_evaluated_in_job_level_environment():
    # Runner context is available in step env, but not in jobs.<id>.env.
    # The old whole-file substring ban rejected valid step-level usage too.
    for name in ["harness-premerge.yml", "pec-tests.yml"]:
        for job in workflow(name)["jobs"].values():
            assert all("${{ runner." not in str(value) for value in job.get("env", {}).values())
