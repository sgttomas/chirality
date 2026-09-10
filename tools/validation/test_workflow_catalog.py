import json
from pathlib import Path

import pytest

from build_workflow_index import CENTRAL, parse_yaml_mapping, validate_and_build
from validate_skill_metadata import validate_skill_dir
from validate_workflow_metadata import validate_workflow_dir


ROOT = Path(__file__).resolve().parents[2]


def _fixture_root(tmp_path: Path) -> Path:
    workflows = tmp_path / "workflows"
    workflows.mkdir()
    (workflows / "catalog.yaml").write_text(json.dumps({
        "schema": "chirality-workflow-catalog/v1",
        "library": {"source": "bundled", "sourceRootId": "fixture-bundle"},
        "centralWorkflowNames": list(CENTRAL),
    }))
    (workflows / "legacy-agents.json").write_text(json.dumps({"schema_version": 1, "aliases": {}}))
    (workflows / "legacy-methods.json").write_text(json.dumps({
        "schema": "chirality-legacy-methods/v1", "convertedWorkflowAliases": {},
        "historicalOnly": [], "unknownLegacyBehavior": "error",
    }))
    for name in CENTRAL:
        package = workflows / name
        package.mkdir()
        (package / "WORKFLOW.md").write_text(f"---\nname: {name}\ndescription: Fixture {name}\n---\n\n# {name}\n")
        (package / "execution.json").write_text(json.dumps({"schema_version": 1, "compatible_roles": ["WORKING_ITEMS"]}))
    return tmp_path


def test_root_index_is_fresh_and_classification_is_bounded():
    index = validate_and_build(ROOT)
    assert (ROOT / "workflows/index.json").read_text() == json.dumps(index, indent=2, sort_keys=False) + "\n"
    workflows = [item for item in index["methods"] if item["kind"] == "workflow"]
    skills = [item for item in index["methods"] if item["kind"] == "skill"]
    assert {item["name"] for item in workflows if item["compatibility"] == "canonical"} == set(CENTRAL)
    assert len(skills) == 8 and {item["compatibility"] for item in skills} == {"canonical"}
    assert all(item["compatibility"] == "legacy" for item in workflows if item["name"] not in CENTRAL)
    assert index["legacy"]["convertedWorkflowAliases"]["deliverable-consistency"] == {"kind": "skill", "name": "deliverable-consistency"}


def test_canonical_skill_execution_policies_and_catalog_projection():
    # Current policy expectations belong here, not in the one-time conversion
    # evidence or retired workflow packages. Role order has no policy meaning.
    expected_tools = {
        "chirality-change": None,
        "preparation": {"capabilities": ["read", "write", "bash", "report_coordination_notice", "ack_agent_update"]},
        "researcher": {"capabilities": ["read", "write", "bash", "report_coordination_notice", "ack_agent_update"]},
        "deliverable-consistency": {"commands": ["python3 tools/validation/scan_deliverable_consistency.py:*"]},
        "drawing-titleblock-page": {"commands": []},
        "proposal-format": {"commands": []},
        "software-code-review": {"commands": [
            "python3 tools/software_workflow/select_affected_checks.py:*",
            "python3 tools/software_workflow/validate_change_scope.py:*",
            "python3 tools/software_workflow/compare_structured.py:*",
            "python3 tools/software_workflow/verify_generated_manifest.py:*",
        ]},
        "software-defect-diagnosis": {"commands": [
            "python3 tools/software_workflow/discover_repository.py:*",
            "python3 tools/software_workflow/select_affected_checks.py:*",
            "python3 tools/software_workflow/run_registered_checks.py:*",
        ]},
    }
    index = validate_and_build(ROOT)
    by_name = {(item["kind"], item["name"]): item for item in index["methods"]}
    for skill_name, tools in expected_tools.items():
        target = json.loads((ROOT / ".agents/skills" / skill_name / "execution.json").read_text())
        assert set(target["compatible_roles"]) == {"HELPS_HUMANS", "WORKING_ITEMS", "TASK"}
        assert target.get("tools") == tools
        descriptor = by_name[("skill", skill_name)]
        assert descriptor["executionRoleIds"] == target["compatible_roles"]
        assert descriptor["execution"]["compatibleRoles"] == target["compatible_roles"]
        assert descriptor["execution"].get("tools") == tools


def test_absent_skill_execution_inherits_and_empty_roles_deny_all(tmp_path):
    root = _fixture_root(tmp_path)
    skill = root / ".agents/skills/portable"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: portable\ndescription: Portable\n---\n")
    method = next(item for item in validate_and_build(root)["methods"] if item["kind"] == "skill")
    assert method["executionRoleIds"] == ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"]
    assert "execution" not in method
    (skill / "execution.json").write_text(json.dumps({"schema_version": 1, "compatible_roles": []}))
    method = next(item for item in validate_and_build(root)["methods"] if item["kind"] == "skill")
    assert method["executionRoleIds"] == []
    assert method["execution"]["compatibleRoles"] == []


def test_malformed_frontmatter_and_optional_workflow_execution(tmp_path):
    root = _fixture_root(tmp_path)
    target = root / "workflows" / CENTRAL[0]
    (target / "WORKFLOW.md").write_text("# no metadata\n")
    with pytest.raises(ValueError, match="frontmatter"):
        validate_and_build(root)
    (target / "WORKFLOW.md").write_text(f"---\nname: {CENTRAL[0]}\ndescription: fixed\n---\n")
    (target / "execution.json").unlink()
    method = next(item for item in validate_and_build(root)["methods"] if item["name"] == CENTRAL[0])
    assert method["executionRoleIds"] == ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"]
    assert "execution" not in method
    (target / "execution.json").write_text(json.dumps({"schema_version": 1, "compatible_roles": []}))
    method = next(item for item in validate_and_build(root)["methods"] if item["name"] == CENTRAL[0])
    assert method["executionRoleIds"] == []
    assert method["execution"]["compatibleRoles"] == []
    (target / "execution.json").write_text(json.dumps({"schema_version": 1, "compatible_roles": "TASK"}))
    with pytest.raises(ValueError, match="malformed execution"):
        validate_and_build(root)


def test_resource_symlink_escape_fails(tmp_path):
    root = _fixture_root(tmp_path)
    outside = tmp_path / "outside.txt"
    outside.write_text("outside")
    (root / "workflows" / CENTRAL[0] / "escape.txt").symlink_to(outside)
    with pytest.raises(ValueError, match="escaping resource"):
        validate_and_build(root)


def test_skill_package_symlink_escape_fails(tmp_path):
    root = _fixture_root(tmp_path)
    outside = tmp_path / "outside-skill"
    outside.mkdir()
    (outside / "SKILL.md").write_text("---\nname: escape\ndescription: Outside\n---\n")
    skills = root / ".agents/skills"
    skills.mkdir(parents=True)
    (skills / "escape").symlink_to(outside, target_is_directory=True)
    with pytest.raises(ValueError, match="escaping skill package"):
        validate_and_build(root)


def test_skill_collection_symlink_escape_fails(tmp_path):
    root = _fixture_root(tmp_path)
    outside = tmp_path.parent / f"{tmp_path.name}-outside-skills"
    skill = outside / "portable"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: portable\ndescription: Outside\n---\n")
    (root / ".agents").mkdir()
    (root / ".agents/skills").symlink_to(outside, target_is_directory=True)
    with pytest.raises(ValueError, match="skill collection escapes"):
        validate_and_build(root)


def test_frontmatter_delimiters_are_complete_lines(tmp_path):
    root = _fixture_root(tmp_path)
    target = root / "workflows" / CENTRAL[0] / "WORKFLOW.md"
    target.write_text(f"---\nname: {CENTRAL[0]}\ndescription: before---after\n---\n\n# Body\n")
    method = next(item for item in validate_and_build(root)["methods"] if item["name"] == CENTRAL[0])
    assert method["description"] == "before---after"


def test_method_name_rejects_empty_hyphen_segment(tmp_path):
    root = _fixture_root(tmp_path)
    target = root / "workflows" / CENTRAL[0]
    bad = root / "workflows/a--b"
    target.rename(bad)
    (bad / "WORKFLOW.md").write_text("---\nname: a--b\ndescription: Invalid name\n---\n")
    with pytest.raises(ValueError, match="invalid bundled workflow identity"):
        validate_and_build(root)


def test_method_name_fixture_enforces_length_and_segments():
    from build_workflow_index import NAME_RE
    fixture = json.loads((ROOT / "tools/validation/fixtures/method_discovery_v1.json").read_text())
    for case in fixture["methodNameCases"]:
        assert bool(NAME_RE.fullmatch(case["name"])) is case["valid"]


def test_standalone_validators_share_name_and_deny_all_contract(tmp_path):
    fixture = json.loads((ROOT / "tools/validation/fixtures/method_discovery_v1.json").read_text())
    for case in fixture["methodNameCases"]:
        skill = tmp_path / case["name"]
        skill.mkdir()
        (skill / "SKILL.md").write_text(f"---\nname: {case['name']}\ndescription: Fixture\n---\n")
        assert validate_skill_dir(skill, tmp_path)["valid"] is case["valid"]
    workflow = tmp_path / "deny-all"
    workflow.mkdir()
    (workflow / "WORKFLOW.md").write_text("---\nname: deny-all\ndescription: Fixture\n---\n")
    (workflow / "execution.json").write_text(json.dumps({"schema_version": 1, "compatible_roles": []}))
    assert validate_workflow_dir(workflow, tmp_path)["valid"]


def test_exact_central_refs_and_public_export_exclusion():
    registry = json.loads((ROOT / "agents/registry.json").read_text())
    assert registry["workflow_catalog"] == {
        "schema": "chirality-method-index/v1",
        "catalog": "workflows/catalog.yaml",
        "index": "workflows/index.json",
    }
    index = validate_and_build(ROOT)
    assert index["centralWorkflowNames"] == list(CENTRAL)
    exported = validate_and_build(ROOT, public_export=True)
    assert len(index["methods"]) == 79
    assert len(exported["methods"]) == 78
    assert not any(item["kind"] == "skill" and item["name"] == "chirality-change" for item in exported["methods"])
    assert not any("chirality-change" in str(item) for item in exported.get("diagnostics", []))


def test_shared_discovery_fixture_contract():
    fixture = json.loads((ROOT / "tools/validation/fixtures/method_discovery_v1.json").read_text())
    assert fixture["precedence"] == ["project", "user", "bundled"]
    collision = next(case for case in fixture["cases"] if case["id"] == "qualified-collision-precedence")
    assert collision["expected"]["selected"]["source"] == "project"
    assert len({candidate["sourceRootId"] for candidate in collision["candidates"]}) == 3
    malformed = next(case for case in fixture["cases"] if case["id"] == "malformed-higher-source-blocks")
    assert malformed["expected"]["selected"] is None
    assert malformed["expected"]["error"] == "MALFORMED_HIGHER_PRECEDENCE"
    for case in fixture["packageYamlCases"]:
        if "expectedError" in case:
            with pytest.raises(Exception, match="duplicate key"):
                parse_yaml_mapping(case["yaml"], case["id"])
        else:
            assert parse_yaml_mapping(case["yaml"], case["id"]) == case["expected"]
    assert next(case for case in fixture["frontmatterDocumentCases"] if case["id"] == "delimiter-substring-preserved")["expectedDescription"] == "before---after"
    assert next(case for case in fixture["methodNameCases"] if case["name"] == "a--b")["valid"] is False
    assert next(case for case in fixture["packageContainmentCases"] if case["id"] == "skill-package-symlink-escape")["expectedError"] == "PACKAGE_OUTSIDE_LIBRARY_ROOT"
    workflow_absent = next(case for case in fixture["workflowExecutionCases"] if case["id"] == "absent-companion-inherits")
    assert workflow_absent["expectedExecutionRoleIds"] == ["HELP_HUMAN", "HELPS_HUMANS", "WORKING_ITEMS", "TASK"]


def test_canonical_skill_has_no_task_specific_companions(tmp_path):
    skill = tmp_path / "skills" / "portable"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: portable\ndescription: Portable skill\n---\n")
    assert validate_skill_dir(skill, tmp_path)["valid"]
    legacy = validate_skill_dir(skill, tmp_path, legacy_task_contract=True)
    assert not legacy["valid"]
    assert any("legacy TASK skill contract" in issue for issue in legacy["issues"])
    (skill / "SKILL.md").write_text(
        "---\nname: portable\ndescription: Portable skill\nmetadata:\n"
        "  chirality-skill-version: '1'\n  chirality-task-profile: NONE\n---\n"
    )
    for name in ("BRIEF_SCHEMA.md", "TOOL_POLICY.md", "QA_CHECKS.md"):
        (skill / name).write_text(f"# {name}\n")
    assert validate_skill_dir(skill, tmp_path, legacy_task_contract=True)["valid"]


def test_grouped_checkpoint_boundaries_use_accepted_snapshots():
    standard = (ROOT / "docs/DECOMPOSITION_STANDARD.md").read_text()
    assert "After every required human checkpoint is accepted" in standard
    assert "consumes that accepted snapshot" in standard

    for name in ("project-decomp", "software-decomp"):
        method = (ROOT / "workflows" / name / "resources/method.md").read_text()
        assert "_LATEST_GROUP1.md" in method
        assert "_LATEST_GROUP2.md" in method
        assert "_LATEST_ACCEPTED.md" in method
        assert "Resolve and consume the accepted group-1 snapshot" in method
        assert "Resolve and consume the accepted group-2 snapshot" in method

    domain = (ROOT / "workflows/domain-decomp/resources/method.md").read_text()
    for pointer in ("_LATEST_SOURCE.md", "_LATEST_GROUP1.md", "_LATEST_GROUP2.md", "_LATEST_ACCEPTED.md"):
        assert pointer in domain

    scope_change = (ROOT / "workflows/scope-change/resources/method.md").read_text()
    assert "Group-1 and\ngroup-2 snapshots live under `_ScopeChange/checkpoint_snapshots/`" in scope_change
    assert "Do not update `_LATEST.md` before checkpoint group 3 acceptance" in scope_change


def test_research_uses_grouped_domain_acceptance_with_legacy_fallback():
    contract = (ROOT / "workflows/research-orchestration/resources/contract.md").read_text()
    method = (ROOT / "workflows/research-orchestration/resources/method.md").read_text()
    assert "checkpoint_snapshots/_LATEST_ACCEPTED.md" in contract
    assert "checkpoint_snapshots/_LATEST_ACCEPTED.md" in method
    assert "LEGACY_ACCEPTED_GATE_POINTER" in contract
    assert "Gate6_Publication_Manifest.csv" in contract
    assert "clearly label that compatibility basis" in method
