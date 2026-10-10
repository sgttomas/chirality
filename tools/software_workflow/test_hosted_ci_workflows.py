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
    for name in ["app-v4.yml", "piping-desktop-e2e.yml"]:
        selection = select_checks(profile, [f".github/workflows/{name}"])
        assert "software_workflow" in selection["checks"]


def test_every_pr_reaches_single_required_aggregate_and_reusable_products():
    root = workflow('governance-harness.yml')
    assert 'pull_request' in root['on']
    assert not root['on']['pull_request']
    assert 'schedule' not in root['on']
    assert 'push' not in root['on']  # no duplicate post-merge product run
    jobs = root['jobs']
    assert jobs['harness']['if'] == 'always()'
    assert set(jobs['harness']['needs']) == {'repository-checks', 'app-v4', 'piping'}
    for job, name in [('app-v4', 'app-v4.yml'), ('piping', 'piping-desktop-e2e.yml')]:
        config = workflow(name)
        assert 'workflow_call' in config['on']
        assert 'workflow_dispatch' in config['on']
        assert 'pull_request' not in config['on']
        assert 'schedule' not in config['on']
        assert jobs[job]['uses'] == f'./.github/workflows/{name}'
        assert 'if' not in config['jobs']['selection']


def test_single_required_result_fails_for_any_unsuccessful_child(tmp_path):
    import os
    import subprocess
    step = workflow('governance-harness.yml')['jobs']['harness']['steps'][0]
    for state in ['success', 'failure', 'cancelled', 'skipped']:
        results = {name: {'result': 'success'} for name in ['repository-checks', 'app-v4', 'piping']}
        results['piping']['result'] = state
        process = subprocess.run(['bash', '-c', step['run']], env={**os.environ, 'RESULTS': json.dumps(results)}, capture_output=True)
        assert (process.returncode == 0) == (state == 'success')


def test_retired_products_have_no_workflows():
    for name in ('harness-premerge.yml', 'pec-tests.yml', 'desktop-release-template.yml'):
        assert not (ROOT / '.github/workflows' / name).exists()


def test_runner_context_is_not_evaluated_in_job_level_environment():
    # Runner context is available in step env, but not in jobs.<id>.env.
    # The old whole-file substring ban rejected valid step-level usage too.
    for name in ["app-v4.yml", "piping-desktop-e2e.yml"]:
        for job in workflow(name)["jobs"].values():
            assert all("${{ runner." not in str(value) for value in job.get("env", {}).values())
