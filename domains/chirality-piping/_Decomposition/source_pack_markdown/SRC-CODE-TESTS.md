# Source Pack: SRC-CODE-TESTS

Grouping: `GROUPED_CODE`  RepoGlob: `tests/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: tests/product_preview/test_product_preview_service.py

    #!/usr/bin/env python3
    """Tests for the TP-MAC-01 product-preview service slice."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[2]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.product_preview import (  # noqa: E402
        build_analysis_run_preview,
        build_agent_proposal_preview,
        build_model_tree,
        build_report_packet_preview,
        load_design_knowledge,
        load_preview_model,
        run_preview_mechanics,
        validate_preview_model,
    )
    from core.product_preview.service import canonical_json  # noqa: E402


    def test_preview_model_fixture_is_valid_and_invented():
        model = load_preview_model()
        validation = validate_preview_model(model)

        assert model["document_kind"] == "openpipestress.product_preview.model"
        assert validation["status"] == "passed"
        assert model["data_boundary"]["public_examples_policy"] == "invented_or_cleared_data_only"
        assert "protected_owner_or_standards_data" in model["data_boundary"]["protected_source_policy"]
        assert "code compliant" not in canonical_json(model).lower()


    def test_model_tree_preserves_stable_entity_ids():
        tree = build_model_tree()
        entity_ids = {item["id"] for item in tree["entities"]}

        assert {"node:N-100", "pipe:P-120", "support:S-130", "component:C-140"} <= entity_ids
        assert all(item["properties"] for item in tree["entities"])


    def test_design_knowledge_has_visible_provenance_and_diagnostics():
        knowledge = load_design_knowledge()

        assert knowledge["records"]
        assert all(record["provenance"] == "invented_example" for record in knowledge["records"])
        assert {item["code"] for item in knowledge["diagnostics"]} == {
            "RULE_CHECK_NOT_PERFORMED",
            "SUPPORT_STIFFNESS_UNRESOLVED",
        }


    def test_mechanics_result_keeps_status_boundaries_separate():
        result = run_preview_mechanics()
        result_ids = {item["id"] for item in result["results"]}

        assert result["status"]["mechanics"] == "MECHANICS_SOLVED"
        assert result["status"]["rule_check"] == "RULE_INPUTS_INCOMPLETE"
        assert result["status"]["professional_acceptance"] == "NOT_PROVIDED"
        assert result["accepted_model_state_mutated"] is False
        assert "RULE_CHECK_INPUTS_MISSING" in {item["code"] for item in result["diagnostics"]}
        assert "COMBINATION_STRESS_SUMMARY_SKIPPED" in {item["code"] for item in result["diagnostics"]}
        assert result["summary"]["load_case_count"] == 2
        assert result["summary"]["max_displacement"]["result_ref"] == "result:disp:node-N-140"
        assert "result:force:pipe-P-120:axial" in result_ids
        assert "result:force:pipe-P-120:axial:end-j" in result_ids
        assert "result:force:pipe-P-120:shear-y" in result_ids
        assert "result:force:pipe-P-120:shear-y:end-j" in result_ids
        assert "result:force:pipe-P-120:quarter-1:shear-y" in result_ids
        assert "result:force:pipe-P-120:midspan:axial" in result_ids
        assert "result:force:pipe-P-120:midspan:shear-z" in result_ids
        assert "result:force:pipe-P-120:quarter-3:shear-z" in result_ids
        assert "result:loadcase:load-L-200:force:pipe-P-120:axial" in result_ids
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial" in result_ids
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y" in result_ids
        assert "result:moment:pipe-P-120:bending-z" in result_ids
        assert "result:moment:pipe-P-120:bending-z:end-j" in result_ids
        assert "result:moment:pipe-P-120:quarter-1:bending-z" in result_ids
        assert "result:moment:pipe-P-120:midspan:bending-z" in result_ids
        assert "result:stress:pipe-P-120" in result_ids
        assert "result:stress:pipe-P-120:end-i:axial-normal" in result_ids
        assert "result:stress:pipe-P-120:end-j:torsional-shear" in result_ids
        assert "result:stress:pipe-P-120:quarter-1:torsional-shear" in result_ids
        assert "result:stress:pipe-P-120:midspan:torsional-shear" in result_ids
        assert "result:stress:pipe-P-120:end-i:pressure-hoop" in result_ids
        assert "result:stress:pipe-P-120:quarter-1:pressure-hoop" in result_ids
        assert "result:stress:pipe-P-120:quarter-1:pressure-longitudinal" not in result_ids
        assert "result:stress:pipe-P-120:quarter-1:shear-y" not in result_ids
        axial = next(item for item in result["results"] if item["id"] == "result:force:pipe-P-120:axial")
        axial_end_j = next(item for item in result["results"] if item["id"] == "result:force:pipe-P-120:axial:end-j")
        shear_quarter = next(
            item
            for item in result["results"]
            if item["id"] == "result:force:pipe-P-120:quarter-1:shear-y"
        )
        torsional_stress_end_j = next(
            item
            for item in result["results"]
            if item["id"] == "result:stress:pipe-P-120:end-j:torsional-shear"
        )
        pressure_hoop = next(
            item
            for item in result["results"]
            if item["id"] == "result:stress:pipe-P-120:end-i:pressure-hoop"
        )
        combination_axial = next(
            item
            for item in result["results"]
            if item["id"] == "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial"
        )
        assert axial["metadata"]["coordinate_system"] == "element_local"
        assert axial["metadata"]["location"] == "end_i"
        assert axial["metadata"]["component"] == "axial_force"
        assert axial["basis_ref"] == {"ref_type": "load_case", "ref_id": "load:L-100"}
        assert axial_end_j["metadata"]["coordinate_system"] == "element_local"
        assert axial_end_j["metadata"]["location"] == "end_j"
        assert axial_end_j["metadata"]["component"] == "axial_force"
        assert shear_quarter["metadata"]["coordinate_system"] == "element_local"
        assert shear_quarter["metadata"]["location"] == "quarter_1"
        assert shear_quarter["metadata"]["component"] == "shear_force_y"
        assert shear_quarter["metadata"]["basis"] == "interpolated_from_endpoint_resultants"
        assert torsional_stress_end_j["unit"] == "MPa"
        assert torsional_stress_end_j["metadata"]["coordinate_system"] == "element_local"
        assert torsional_stress_end_j["metadata"]["location"] == "end_j"
        assert torsional_stress_end_j["metadata"]["component"] == "torsional_shear_stress"
        assert (
            torsional_stress_end_j["metadata"]["basis"]
            == "recovered_from_open_mechanics_stress_components"
        )
        assert pressure_hoop["metadata"]["coordinate_system"] == "pipe_section"
        assert pressure_hoop["metadata"]["component"] == "pressure_hoop_stress"
        assert combination_axial["basis_ref"] == {
            "ref_type": "combination",
            "ref_id": "combination:C-OPER-ALT",
        }
        assert combination_axial["source_result_refs"] == [
            "result:force:pipe-P-120:axial",
            "result:loadcase:load-L-200:force:pipe-P-120:axial",
        ]
        assert combination_axial["metadata"]["basis"] == "explicit_user_linear_combination"


    def test_analysis_run_preview_binds_mechanics_results_to_immutable_run_record():
        preview = build_analysis_run_preview()
        run = preview["analysis_run"]
        result_refs = {item["result_ref"]["ref"]: item for item in run["result_refs"]}
        load_basis_refs = {(item["object_type"], item["ref"]) for item in run["load_basis_refs"]}

        assert preview["deliverable_id"] == "DEL-14-02"
        assert run["run_id"] == "run:preview-linear-static-001"
        assert run["immutability_policy"]["run_record_is_read_only"] is True
        assert "HUMAN_REVIEW_REQUIRED" in run["analysis_status"]
        assert "result:force:pipe-P-120:axial" in result_refs
        assert "result:force:pipe-P-120:axial:end-j" in result_refs
        assert "result:force:pipe-P-120:midspan:axial" in result_refs
        assert "result:force:pipe-P-120:quarter-1:shear-y" in result_refs
        assert "result:force:pipe-P-120:shear-y" in result_refs
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial" in result_refs
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y" in result_refs
        assert "result:stress:pipe-P-120:end-j:torsional-shear" in result_refs
        assert "result:stress:pipe-P-120:quarter-1:torsional-shear" in result_refs
        assert result_refs["result:force:pipe-P-120:axial"]["result_family"] == "force"
        assert result_refs["result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial"]["result_family"] == "force"
        assert result_refs["result:force:pipe-P-120:axial"]["hash_refs"][0]["payload_scope"] == "result_value"
        assert (
            result_refs["result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial"]["hash_refs"][0][
                "payload_scope"
            ]
            == "result_value"
        )
        assert result_refs["result:force:pipe-P-120:axial:end-j"]["result_family"] == "force"
        assert result_refs["result:stress:pipe-P-120:end-j:torsional-shear"]["result_family"] == "stress"
        assert {
            ("LoadCase", "load:L-100"),
            ("LoadCase", "load:L-200"),
            ("Combination", "combination:C-OPER-ALT"),
        } <= load_basis_refs
        assert run["professional_boundary"]["software_makes_compliance_claim"] is False


    def test_report_packet_preview_materializes_read_only_audit_context():
        packet = build_report_packet_preview()

        assert packet["document_kind"] == "openpipestress.product_preview.report_packet"
        assert packet["packet_id"] == "report-packet:run:preview-linear-static-001"
        assert packet["source_run_ref"] == {
            "object_type": "AnalysisRun",
            "ref": "run:preview-linear-static-001",
        }
        assert "result:disp:node-N-140" in packet["selected_result_refs"]
        assert "result:force:pipe-P-120:axial" in packet["selected_result_refs"]
        assert "result:force:pipe-P-120:axial:end-j" in packet["selected_result_refs"]
        assert "result:force:pipe-P-120:midspan:axial" in packet["selected_result_refs"]
        assert "result:force:pipe-P-120:quarter-1:shear-y" in packet["selected_result_refs"]
        assert "result:force:pipe-P-120:shear-y" in packet["selected_result_refs"]
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial" in packet["selected_result_refs"]
        assert (
            "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y"
            in packet["selected_result_refs"]
        )
        assert "result:stress:pipe-P-120:end-j:torsional-shear" in packet["selected_result_refs"]
        assert "result:stress:pipe-P-120:quarter-1:torsional-shear" in packet["selected_result_refs"]
        assert packet["analysis_run_context"]["deliverable_id"] == "DEL-14-02"
        assert packet["analysis_run_context"]["immutability_policy"]["run_record_is_read_only"] is True
        assert packet["analysis_run_context"]["result_value_hash_count"] >= 1
        assert packet["analysis_run_context"]["result_envelope_hash_refs"][0]["payload_scope"] == "result_envelope"
        assert packet["proposal_context"]["application_status"] == "not_applied"
        assert packet["proposal_context"]["accepted_model_state_mutated"] is False
        assert packet["report_packet_status"] == {
            "materialization": "read_only_context_packet",
            "rendered_calculation_report": False,
            "result_export_payload": False,
            "external_handoff_payload": False,
            "professional_acceptance_record": False,
        }
        assert packet["professional_boundary"]["software_makes_compliance_claim"] is False
        assert packet["privacy_boundary"]["private_payload_embedded"] is False
        assert packet["privacy_boundary"]["protected_payload_embedded"] is False
        assert any(item["payload_scope"] == "report_packet_context" for item in packet["hash_refs"])
        assert any(
            item["payload_ref"] == {
                "object_type": "Result",
                "ref": "result:force:pipe-P-120:axial",
            }
            for item in packet["hash_refs"]
        )
        assert any(
            item["payload_ref"] == {
                "object_type": "Result",
                "ref": "result:force:pipe-P-120:axial:end-j",
            }
            for item in packet["hash_refs"]
        )
        assert any(
            item["payload_ref"] == {
                "object_type": "Result",
                "ref": "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial",
            }
            for item in packet["hash_refs"]
        )
        assert any(
            item["payload_ref"] == {
                "object_type": "Result",
                "ref": "result:stress:pipe-P-120:end-j:torsional-shear",
            }
            for item in packet["hash_refs"]
        )
        assert "code compliant" not in canonical_json(packet).lower()
        assert "professional approval" not in canonical_json(packet).lower()


    def test_preview_validation_blocks_empty_ids_and_missing_provenance():
        model = load_preview_model()
        model["nodes"][0]["id"] = ""
        del model["pipe_segments"][0]["provenance"]

        validation = validate_preview_model(model)
        codes = {item["code"] for item in validation["diagnostics"]}

        assert validation["status"] == "blocked"
        assert "PREVIEW_ID_MISSING" in codes
        assert "PREVIEW_PROVENANCE_MISSING" in codes


    def test_preview_validation_blocks_invalid_explicit_combinations():
        model = load_preview_model()
        model["combinations"] = [
            {
                "id": "combination:C-BAD",
                "basis": "code",
                "terms": [{"load_case": "load:missing", "factor": float("inf")}],
                "provenance": "invented_example_invalid_combination",
            },
            {
                "id": "combination:C-EMPTY",
                "basis": "mechanics",
                "terms": [],
                "provenance": "invented_example_invalid_combination",
            },
        ]

        validation = validate_preview_model(model)
        codes = {item["code"] for item in validation["diagnostics"]}

        assert validation["status"] == "blocked"
        assert "PREVIEW_COMBINATION_BASIS_UNSUPPORTED" in codes
        assert "PREVIEW_COMBINATION_FACTOR_INVALID" in codes
        assert "PREVIEW_COMBINATION_LOAD_CASE_UNKNOWN" in codes
        assert "PREVIEW_COMBINATION_TERMS_EMPTY" in codes


    def test_agent_proposal_is_review_only_and_non_mutating():
        preview = build_agent_proposal_preview()

        assert preview["application_status"] == "not_applied"
        assert preview["accepted_model_state_mutated"] is False
        assert preview["proposal"]["audit_boundary"]["requires_user_acceptance"] is True
        assert preview["proposal"]["audit_boundary"]["mutates_accepted_model_state"] is False
        assert "certified" not in canonical_json(preview).lower()

## Component: tests/schema_validation.py

    """Shared JSON Schema validation helpers for PKG-02 contract tests."""

    from __future__ import annotations

    from copy import deepcopy


    INSTALL_MESSAGE = (
        "jsonschema>=4,<5 is required for full PKG-02 JSON Schema validation; "
        "install with: python3 -m pip install -r requirements-dev.txt"
    )


    class JsonSchemaDependencyMissing(RuntimeError):
        """Raised when optional JSON Schema validation tooling is unavailable."""


    def _draft202012_validator():
        try:
            from jsonschema import Draft202012Validator
        except ModuleNotFoundError as exc:
            raise JsonSchemaDependencyMissing(INSTALL_MESSAGE) from exc
        return Draft202012Validator


    def validate_schema_document(schema, *, schema_label="schema"):
        """Validate a schema document with Draft 2020-12."""
        validator_class = _draft202012_validator()
        try:
            validator_class.check_schema(schema)
        except Exception as exc:  # jsonschema raises SchemaError subclasses.
            raise AssertionError(f"{schema_label} is not a valid Draft 2020-12 schema: {exc}") from exc
        return True


    def schema_for_definition(root_schema, definition_name):
        """Build a small root schema that validates one definition from a larger schema."""
        schema = {
            "$schema": root_schema.get("$schema", "https://json-schema.org/draft/2020-12/schema"),
            "$defs": deepcopy(root_schema["$defs"]),
            "$ref": f"#/$defs/{definition_name}",
        }
        return schema


    def validate_instance(schema, instance, *, schema_label="schema", instance_label="instance"):
        """Validate an instance and raise an assertion with compact error paths."""
        validate_schema_document(schema, schema_label=schema_label)
        validator_class = _draft202012_validator()
        validator = validator_class(schema)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if errors:
            formatted = "\n".join(_format_error(error) for error in errors[:10])
            remaining = len(errors) - 10
            suffix = f"\n... {remaining} more validation errors" if remaining > 0 else ""
            raise AssertionError(f"{instance_label} failed JSON Schema validation:\n{formatted}{suffix}")
        return True


    def _format_error(error):
        path = "$"
        for part in error.path:
            if isinstance(part, int):
                path += f"[{part}]"
            else:
                path += f".{part}"
        return f"{path}: {error.message}"

## Component: tests/security/test_local_first_storage_policy.py

    #!/usr/bin/env python3
    """Policy checks for the local-first storage contract."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(ROOT))

    from core.security.local_first_storage import (  # noqa: E402
        classify_storage_record,
        guard_storage_records,
        storage_record,
    )

    POLICY_PATH = ROOT / "docs" / "security" / "local_first_storage_policy.md"

    TRACEABILITY = {
        "deliverable_id: DEL-12-01",
        "package_id: PKG-12",
        "SOW-029",
        "OBJ-010",
    }

    LOCAL_FIRST_PRIVATE_CLASSES = {
        "Private project models",
        "private rule packs",
        "private material and component libraries",
        "owner standards",
        "company design bases",
        "credentials",
        "secrets",
        "diagnostics",
        "reports",
        "generated outputs",
        "user controlled",
    }

    SYMBOLIC_PATH_CLASSES = {
        "PUBLIC_REPOSITORY_CONTENT",
        "PUBLIC_EXAMPLE_CONTENT",
        "USER_CHOSEN_PROJECT_PACKAGE",
        "USER_PRIVATE_LIBRARY_ROOT",
        "USER_PRIVATE_RULE_PACK_ROOT",
        "USER_REPORT_OUTPUT_ROOT",
        "USER_DIAGNOSTIC_BUNDLE_ROOT",
        "USER_IMPORT_STAGING_ROOT",
        "USER_EXPORT_STAGING_ROOT",
        "LOCAL_CACHE_ROOT",
        "USER_SECRET_REFERENCE",
    }

    PERSISTENCE_BASELINE = {
        "versioned persistence",
        "schema-governed payloads",
        "unit-aware data",
        "provenance-preserving records",
        "migration-aware status",
        "deterministic round-trip serialization",
        "canonical JSON/JCS-compatible hashes",
        "local SQLite storage as a payload/index substrate",
        "rebuildable, hash-neutral SQLite FTS5/BM25 retrieval sidecars",
    }

    OPEN_DECISIONS = {
        "Operating-system roots and application data directories",
        "DB migration and product schema migration framework",
        "Encryption, secret storage, and key management",
        "Redaction workflow and export staging behavior",
        "Private-library registry and secret/private-library handling",
        "Import/export formats and adapter behavior",
        "Cloud exception workflow",
    }

    NO_BYPASS_SURFACES = {
        "plugins",
        "adapters",
        "import/export paths",
        "reports",
        "telemetry",
        "CLI runners",
        "diagnostics",
        "tests",
        "application services",
    }

    REAL_PATH_MARKERS = {
        "/Users/",
        "/home/",
        "C:\\",
        "file://",
        "s3://",
        "gs://",
        "https://",
        "http://",
    }

    DISALLOWED_COMMITMENTS = {
        "cloud storage is enabled",
        "cloud sync is enabled",
        "hosted database is enabled",
        "network is required",
        "encryption is provided",
        "secrets are stored in",
        "default path is",
        "storage root is",
    }


    def decision_codes(result):
        return {decision.reason_code for decision in result.decisions}


    def diagnostic_codes(result):
        return {diagnostic.code for diagnostic in result.diagnostics}


    def invented_project_storage_record():
        return storage_record(
            record_id="invented.project.metadata",
            record_kind="project_model",
            label="Invented project metadata reference",
            checksum="sha256:0000000000000000000000000000000000000000000000000000000000000000",
            checksum_status="placeholder_checksum_recorded",
            source_note="invented local placeholder source note",
            redistribution_status="private_only",
            review_status="pending",
        )


    def policy_text():
        return POLICY_PATH.read_text(encoding="utf-8")


    def lower_policy_text():
        return policy_text().lower()


    def test_storage_record_classification_is_deterministic_and_metadata_only():
        first = classify_storage_record(invented_project_storage_record())
        second = classify_storage_record(invented_project_storage_record())

        assert first == second
        assert first.decision_id.startswith("LFS-CLS-")
        assert first.reason_code == "PRIVATE_METADATA_LOCAL_FIRST"
        assert first.default_posture == "local_private_metadata_requires_explicit_intent"
        assert first.metadata["storage_locality"] == "USER_CHOSEN_PROJECT_PACKAGE"
        assert first.metadata["contains_payload"] is False
        assert first.metadata["secret_material_present"] is False
        assert first.metadata["direct_sql_access"] is False


    def test_public_repository_blocks_private_storage_payloads_without_leaking_values():
        unsafe_records = [
            {
                "record_id": "invented.project.payload",
                "record_kind": "project_model",
                "label": "Invented project payload",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "project_payload": {"invented": "PROJECT_PAYLOAD_SHOULD_NOT_SURVIVE"},
            },
            {
                "record_id": "invented.rule.payload",
                "record_kind": "private_rule_pack",
                "label": "Invented rule payload",
                "privacy_classification": "private_rule_pack_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "rule_payload": "RULE_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.material.payload",
                "record_kind": "private_material_library",
                "label": "Invented material payload",
                "privacy_classification": "private_material_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "material_values": {"invented": "MATERIAL_PAYLOAD_SHOULD_NOT_SURVIVE"},
            },
            {
                "record_id": "invented.component.payload",
                "record_kind": "private_component_library",
                "label": "Invented component payload",
                "privacy_classification": "private_component_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "component_values": {"invented": "COMPONENT_PAYLOAD_SHOULD_NOT_SURVIVE"},
            },
            {
                "record_id": "invented.report.payload",
                "record_kind": "private_report",
                "label": "Invented report payload",
                "privacy_classification": "private_report_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "report_payload": "REPORT_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.diagnostic.payload",
                "record_kind": "private_diagnostic",
                "label": "Invented diagnostic payload",
                "privacy_classification": "private_diagnostic_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "diagnostic_payload": "DIAGNOSTIC_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.cache.payload",
                "record_kind": "private_cache",
                "label": "Invented cache payload",
                "privacy_classification": "private_cache_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "cache_payload": "CACHE_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.secret.payload",
                "record_kind": "secret_reference",
                "label": "Invented secret payload",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "credential_reference",
                "secret_value": "SECRET_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
        ]

        result = guard_storage_records(
            unsafe_records,
            target_context="public_repository",
        )
        serialized = json.dumps(result.as_schema_dict(), sort_keys=True)

        assert result.blocked is True
        assert result.summary()["metadata_only"] is True
        assert decision_codes(result) == {
            "STORAGE_PAYLOAD_METADATA_ONLY_REQUIRED",
            "SECRET_MATERIAL_METADATA_ONLY_REQUIRED",
        }
        assert "STORAGE_PAYLOAD_METADATA_ONLY_REQUIRED" in diagnostic_codes(result)
        for leaked in {
            "PROJECT_PAYLOAD_SHOULD_NOT_SURVIVE",
            "RULE_PAYLOAD_SHOULD_NOT_SURVIVE",
            "MATERIAL_PAYLOAD_SHOULD_NOT_SURVIVE",
            "COMPONENT_PAYLOAD_SHOULD_NOT_SURVIVE",
            "REPORT_PAYLOAD_SHOULD_NOT_SURVIVE",
            "DIAGNOSTIC_PAYLOAD_SHOULD_NOT_SURVIVE",
            "CACHE_PAYLOAD_SHOULD_NOT_SURVIVE",
            "SECRET_PAYLOAD_SHOULD_NOT_SURVIVE",
        }:
            assert leaked not in serialized


    def test_local_private_storage_requires_explicit_user_intent_for_private_metadata():
        blocked = guard_storage_records(
            [invented_project_storage_record()],
            target_context="local_private",
            explicit_user_intent=False,
        )
        allowed = guard_storage_records(
            [invented_project_storage_record()],
            target_context="local_private",
            explicit_user_intent=True,
        )

        assert blocked.blocked is True
        assert "LOCAL_PRIVATE_INTENT_REQUIRED" in decision_codes(blocked)
        assert allowed.blocked is False
        assert "PRIVATE_LOCAL_METADATA_ALLOWED" in decision_codes(allowed)
        assert allowed.safe_manifest[0]["record_id"] == "invented.project.metadata"
        assert allowed.safe_manifest[0]["contains_payload"] is False


    def test_public_repository_locality_blocks_even_with_local_private_intent():
        result = guard_storage_records(
            [
                storage_record(
                    record_id="invented.public.repo.private.target",
                    record_kind="project_model",
                    label="Invented public repository private target",
                    storage_locality="PUBLIC_REPOSITORY_CONTENT",
                    redistribution_status="private_only",
                    review_status="pending",
                    source_note="invented local placeholder source note",
                )
            ],
            target_context="local_private",
            explicit_user_intent=True,
        )

        assert result.blocked is True
        assert result.decisions[0].blocked is True
        assert "PUBLIC_REPOSITORY_PRIVATE_STORAGE_BLOCKED" in diagnostic_codes(result)


    def test_cloud_network_direct_sql_secret_and_concrete_path_details_are_sanitized():
        records = [
            {
                "record_id": "invented.cloud.reference",
                "record_kind": "project_model",
                "label": "Invented cloud reference",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "cloud_or_network_reference": True,
                "cloud_sync_target": "CLOUD_SYNC_TARGET_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.direct.sql",
                "record_kind": "project_store",
                "label": "Invented direct SQL reference",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "table_name": "SQL_TABLE_DETAIL_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.secret.material",
                "record_kind": "secret_reference",
                "label": "Invented secret material",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "credential_reference",
                "api_key": "SECRET_MATERIAL_SHOULD_NOT_SURVIVE",
            },
            {
                "record_id": "invented.concrete.path",
                "record_kind": "private_report",
                "label": "Invented concrete path reference",
                "privacy_classification": "private_report_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "file_path": "FAKE_CONCRETE_PRIVATE_PATH_SHOULD_NOT_SURVIVE",
            },
        ]

        result = guard_storage_records(
            records,
            target_context="local_private",
            explicit_user_intent=True,
        )
        serialized = json.dumps(result.as_schema_dict(), sort_keys=True)

        assert result.blocked is True
        assert "CLOUD_OR_NETWORK_STORAGE_BLOCKED" in decision_codes(result)
        assert "DIRECT_SQL_ACCESS_BLOCKED" in decision_codes(result)
        assert "SECRET_MATERIAL_METADATA_ONLY_REQUIRED" in decision_codes(result)
        assert "CONCRETE_PATH_REDUCED_TO_SAFE_METADATA" in decision_codes(result)
        assert any(
            decision.record_id == "invented.concrete.path"
            and decision.action == "include_metadata_only"
            for decision in result.decisions
        )
        for leaked in {
            "CLOUD_SYNC_TARGET_SHOULD_NOT_SURVIVE",
            "SQL_TABLE_DETAIL_SHOULD_NOT_SURVIVE",
            "SECRET_MATERIAL_SHOULD_NOT_SURVIVE",
            "FAKE_CONCRETE_PRIVATE_PATH_SHOULD_NOT_SURVIVE",
        }:
            assert leaked not in serialized


    def test_policy_is_traceable_to_deliverable_scope():
        text = policy_text()
        for required in TRACEABILITY:
            assert required in text


    def test_local_first_user_control_default_is_explicit():
        text = policy_text()
        assert "OpenPipeStress is local-first by default." in text
        for required in LOCAL_FIRST_PRIVATE_CLASSES:
            assert required in text


    def test_repository_is_not_default_private_storage():
        text = policy_text()
        assert "The public repository is not a default durable storage location" in text
        assert "Public repository paths must not be used as default durable storage" in text


    def test_symbolic_path_classes_are_defined_without_real_paths():
        text = policy_text()
        for path_class in SYMBOLIC_PATH_CLASSES:
            assert path_class in text
        assert "These names are planning classes, not filesystem paths." in text
        for marker in REAL_PATH_MARKERS:
            assert marker not in text


    def test_unresolved_storage_choices_remain_tbd_or_findings():
        text = policy_text()
        assert "remain explicit warning, finding, or unsupported" in text
        for decision in OPEN_DECISIONS:
            assert decision in text


    def test_persistence_baseline_is_preserved():
        text = policy_text()
        for required in PERSISTENCE_BASELINE:
            assert required in text
        assert "SCA-003 local SQLite-backed project store/index" in text
        assert "Canonical JSON/JCS-compatible payload bytes remain the domain and interchange" in text
        assert "SQLite tables are storage/projection details, not public contracts." in text
        assert "must not be copied" in text
        assert "explicit export/review workflow" in text


    def test_no_bypass_surfaces_are_listed():
        text = policy_text()
        for surface in NO_BYPASS_SURFACES:
            assert surface in text
        assert "No plugin manifest, adapter declaration, CLI option" in text
        assert "can bypass" in text
        assert "direct SQL, raw SQLite handles, table-name dependencies" in text


    def test_no_cloud_encryption_or_runtime_storage_commitment():
        lowered = lower_policy_text()
        assert "hosted database" in lowered
        assert "required network" in lowered
        assert "cloud sync" in lowered
        assert "no encryption or secret-storage claim is made here" in lowered
        assert "free to use" in lowered
        assert "usable offline" in lowered
        for disallowed in DISALLOWED_COMMITMENTS:
            assert disallowed not in lowered


    def test_no_runtime_storage_code_or_schema_was_added():
        assert not (ROOT / "core" / "storage").exists()
        assert not (ROOT / "apps" / "storage").exists()
        assert not (ROOT / "schemas" / "storage.schema.yaml").exists()

## Component: tests/security/test_redaction_export_controls.py

    #!/usr/bin/env python3
    """Checks for DEL-12-02 redaction/export controls using invented fixtures."""

    import copy
    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(ROOT))

    from core.security.redaction import (  # noqa: E402
        REDACTED_VALUE,
        classify_export_item,
        redact_export_payload,
    )


    SCHEMA_PATH = ROOT / "schemas" / "redaction_export_controls.schema.yaml"
    DOC_PATH = ROOT / "docs" / "security" / "redaction_export_controls.md"
    MEMORY_PATH = (
        ROOT
        / "execution"
        / "PKG-12_Security, Privacy, and Private Data Handling"
        / "1_Working"
        / "DEL-12-02_Private data redaction and export controls"
        / "MEMORY.md"
    )

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "control_profile",
        "field_policies",
        "export_run",
    }

    REQUIRED_DEFS = {
        "ControlProfile",
        "ExportContext",
        "ExportRun",
        "FieldClass",
        "FieldPolicy",
        "FindingClass",
        "FindingSeverity",
        "InputSummary",
        "PrivacyClassification",
        "ReasonCode",
        "RedactionAction",
        "RedactionDecision",
        "RedactionFinding",
        "RedactionSummary",
        "RedistributionStatus",
        "ReviewStatus",
    }

    PRIVATE_CLASSES = {
        "private_project_data",
        "private_material_data",
        "private_component_data",
        "private_rule_pack_data",
        "owner_standard_data",
        "company_design_basis_data",
        "path_data",
        "secret_like_data",
    }

    POLICY_ACTIONS = {
        "warning_only",
        "redact_value",
        "redact_field",
        "omit_field",
        "block_export",
    }

    FORBIDDEN_CHANGED_FILE_TERMS = {
        "AS" + "ME",
        "B" + "31",
        "B" + "31J",
        "allowable stress " + "table",
        "stress intensification factor " + "table",
        "vendor catalog " + "value",
        "real " + "secret",
        "private key " + "fixture",
        "cert" + "ified by " + "OpenPipeStress",
        "se" + "aled by " + "OpenPipeStress",
        "code " + "compliant",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def decision_codes(result):
        return {decision.reason_code for decision in result.decisions}


    def finding_codes(result):
        return {finding.code for finding in result.findings}


    def invented_payload():
        return {
            "report_id": "invented-redaction-report",
            "project": {
                "name": {
                    "field_id": "project.name",
                    "field_class": "project",
                    "privacy_classification": "private_project_data",
                    "redistribution_status": "private_only",
                    "review_status": "accepted",
                    "value": "Invented Local Project A",
                },
                "status": {
                    "field_id": "project.status",
                    "field_class": "public_metadata",
                    "privacy_classification": "public_metadata",
                    "redistribution_status": "public_permissive",
                    "review_status": "accepted",
                    "value": "MECHANICS_SOLVED",
                },
                "path": {
                    "field_id": "project.path",
                    "field_class": "path",
                    "privacy_classification": "path_data",
                    "redistribution_status": "private_only",
                    "review_status": "accepted",
                    "value": "SYMBOLIC_USER_PROJECT_PACKAGE/invented-project.ops",
                },
            },
            "rule_pack": {
                "identity": {
                    "field_id": "rule.identity",
                    "field_class": "rule_pack",
                    "privacy_classification": "public_metadata",
                    "redistribution_status": "public_permissive",
                    "review_status": "accepted",
                    "value": {
                        "id": "invented-rule-pack",
                        "version": "0.1.0",
                        "checksum": "sha256:invented",
                    },
                },
                "private_value": {
                    "field_id": "rule.private_value",
                    "field_class": "rule_pack",
                    "privacy_classification": "private_rule_pack_data",
                    "redistribution_status": "private_only",
                    "review_status": "accepted",
                    "value": 123.45,
                },
            },
            "material": {
                "unknown_source": {
                    "field_id": "material.unknown_source",
                    "field_class": "material",
                    "privacy_classification": "unknown",
                    "redistribution_status": "unknown",
                    "review_status": "pending",
                    "value": "Invented material placeholder",
                }
            },
            "component": {
                "private_component_value": {
                    "field_id": "component.private_value",
                    "field_class": "component",
                    "privacy_classification": "private_component_data",
                    "redistribution_status": "private_only",
                    "review_status": "accepted",
                    "value": 9.87,
                }
            },
            "secret_reference": {
                "field_id": "secret.reference",
                "field_class": "secret_like",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "accepted",
                "value": "SYNTHETIC_SECRET_REFERENCE_ONLY",
            },
        }


    def test_schema_is_strict_and_traceable():
        schema = load_json(SCHEMA_PATH)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(schema["$defs"])
        assert schema["properties"]["deliverable_id"]["const"] == "DEL-12-02"
        assert schema["properties"]["package_id"]["const"] == "PKG-12"
        assert schema["properties"]["scope_item"]["const"] == "SOW-040"
        assert {"OBJ-010"} == set(schema["properties"]["objectives"]["items"]["enum"])


    def test_schema_vocabularies_cover_required_controls():
        schema = load_json(SCHEMA_PATH)
        assert PRIVATE_CLASSES <= enum_at(schema, "PrivacyClassification")
        assert POLICY_ACTIONS <= enum_at(schema, "RedactionAction")
        assert {
            "public_report",
            "public_example",
            "shared_model",
            "downstream_tool",
            "local_private",
        } <= enum_at(schema, "ExportContext")
        assert {
            "UNKNOWN_PROVENANCE_WARNING",
            "REDISTRIBUTION_STATUS_UNKNOWN",
            "PROTECTED_CONTENT_BLOCKED",
            "MISSING_METADATA_REDACTED",
            "LOCAL_PRIVATE_INTENT_REQUIRED",
            "PROFESSIONAL_BOUNDARY_BLOCKED",
            "PAYLOAD_METADATA_ONLY_REQUIRED",
            "SECRET_MATERIAL_BLOCKED",
            "CLOUD_OR_NETWORK_REFERENCE_BLOCKED",
            "DIRECT_SQL_ACCESS_BLOCKED",
            "STORAGE_BYPASS_BLOCKED",
            "CONCRETE_PATH_REDACTED",
        } <= enum_at(schema, "ReasonCode")

        profile = schema["$defs"]["ControlProfile"]["properties"]
        assert profile["local_first"]["const"] is True
        assert profile["source_mutation_allowed"]["const"] is False
        assert profile["cloud_transmission_allowed"]["const"] is False
        assert profile["local_private_requires_explicit_intent"]["const"] is True
        assert profile["professional_claims_allowed"]["const"] is False
        assert profile["classification_basis"]["const"] == "explicit_metadata_only"


    def test_public_report_redacts_private_and_unknown_values_without_mutating_source():
        source = invented_payload()
        original = copy.deepcopy(source)
        result = redact_export_payload(source, export_context="public_report")

        assert source == original
        assert result.blocked is False
        assert result.payload["project"]["name"]["value"] == REDACTED_VALUE
        assert result.payload["project"]["path"]["value"] == REDACTED_VALUE
        assert result.payload["rule_pack"]["private_value"]["value"] == REDACTED_VALUE
        assert result.payload["component"]["private_component_value"]["value"] == REDACTED_VALUE
        assert result.payload["secret_reference"]["value"] == REDACTED_VALUE
        assert result.payload["material"]["unknown_source"]["value"] == REDACTED_VALUE
        assert result.payload["rule_pack"]["identity"]["value"]["checksum"] == "sha256:invented"
        assert "PRIVATE_DATA_REDACTED" in decision_codes(result)
        assert "REDISTRIBUTION_STATUS_UNKNOWN" in decision_codes(result)
        assert "PRIVATE_DATA_WARNING" in {finding.class_ for finding in result.findings}
        assert "PROVENANCE_WARNING" in {finding.class_ for finding in result.findings}


    def test_local_private_export_requires_explicit_intent_then_retains_with_warning():
        blocked = redact_export_payload(
            invented_payload(),
            export_context="local_private",
            explicit_local_private_intent=False,
        )
        assert blocked.blocked is True
        assert "LOCAL_PRIVATE_INTENT_REQUIRED" in finding_codes(blocked)

        allowed = redact_export_payload(
            invented_payload(),
            export_context="local_private",
            explicit_local_private_intent=True,
        )
        assert allowed.blocked is False
        assert allowed.payload["project"]["name"]["value"] == "Invented Local Project A"
        assert allowed.payload["rule_pack"]["private_value"]["value"] == 123.45
        assert allowed.payload["secret_reference"]["value"] == "SYNTHETIC_SECRET_REFERENCE_ONLY"
        assert "PRIVATE_LOCAL_ALLOWED_WITH_WARNING" in finding_codes(allowed)
        assert allowed.summary()["warning_count"] >= 1
        assert allowed.summary()["cloud_transmission_attempted"] is False


    def test_storage_privacy_metadata_blocks_or_redacts_unsafe_export_details():
        payload = {
            "payload_marker": {
                "field_id": "storage.payload",
                "field_class": "export_manifest",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "accepted",
                "contains_payload": True,
                "payload": "PAYLOAD_DETAIL_SHOULD_NOT_SURVIVE",
                "value": "PAYLOAD_VALUE_SHOULD_NOT_SURVIVE",
            },
            "secret_material": {
                "field_id": "storage.secret",
                "field_class": "secret_like",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "accepted",
                "secret_material_present": True,
                "secret_value": "SECRET_DETAIL_SHOULD_NOT_SURVIVE",
                "value": "SECRET_VALUE_SHOULD_NOT_SURVIVE",
            },
            "cloud_reference": {
                "field_id": "storage.cloud",
                "field_class": "export_manifest",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "cloud_or_network_reference": True,
                "cloud_sync_target": "CLOUD_TARGET_SHOULD_NOT_SURVIVE",
                "value": "CLOUD_VALUE_SHOULD_NOT_SURVIVE",
            },
            "direct_sql": {
                "field_id": "storage.sql",
                "field_class": "export_manifest",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "direct_sql_access": True,
                "table_name": "SQL_TABLE_DETAIL_SHOULD_NOT_SURVIVE",
                "value": "SQL_VALUE_SHOULD_NOT_SURVIVE",
            },
            "storage_bypass": {
                "field_id": "storage.bypass",
                "field_class": "export_manifest",
                "privacy_classification": "private_project_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "storage_bypass_requested": True,
                "value": "BYPASS_VALUE_SHOULD_NOT_SURVIVE",
            },
            "concrete_path": {
                "field_id": "storage.path",
                "field_class": "path",
                "privacy_classification": "path_data",
                "redistribution_status": "private_only",
                "review_status": "accepted",
                "concrete_path_present": True,
                "file_path": "FAKE_CONCRETE_PATH_SHOULD_NOT_SURVIVE",
                "value": "PATH_VALUE_SHOULD_NOT_SURVIVE",
            },
        }

        result = redact_export_payload(payload, export_context="public_report")
        serialized_payload = json.dumps(result.payload, sort_keys=True)

        assert result.blocked is True
        assert {
            "PAYLOAD_METADATA_ONLY_REQUIRED",
            "SECRET_MATERIAL_BLOCKED",
            "CLOUD_OR_NETWORK_REFERENCE_BLOCKED",
            "DIRECT_SQL_ACCESS_BLOCKED",
            "STORAGE_BYPASS_BLOCKED",
            "CONCRETE_PATH_REDACTED",
        } <= finding_codes(result)
        assert result.payload["concrete_path"]["value"] == REDACTED_VALUE
        assert "file_path" not in result.payload["concrete_path"]
        for leaked in {
            "PAYLOAD_DETAIL_SHOULD_NOT_SURVIVE",
            "PAYLOAD_VALUE_SHOULD_NOT_SURVIVE",
            "SECRET_DETAIL_SHOULD_NOT_SURVIVE",
            "SECRET_VALUE_SHOULD_NOT_SURVIVE",
            "CLOUD_TARGET_SHOULD_NOT_SURVIVE",
            "CLOUD_VALUE_SHOULD_NOT_SURVIVE",
            "SQL_TABLE_DETAIL_SHOULD_NOT_SURVIVE",
            "SQL_VALUE_SHOULD_NOT_SURVIVE",
            "BYPASS_VALUE_SHOULD_NOT_SURVIVE",
            "FAKE_CONCRETE_PATH_SHOULD_NOT_SURVIVE",
            "PATH_VALUE_SHOULD_NOT_SURVIVE",
        }:
            assert leaked not in serialized_payload


    def test_local_private_intent_metadata_allows_private_value_with_warning():
        item = {
            "field_id": "project.intent",
            "field_class": "project",
            "privacy_classification": "private_project_data",
            "redistribution_status": "private_only",
            "review_status": "accepted",
            "local_private_intent": True,
            "value": "Invented local-only value",
        }

        result = redact_export_payload({"item": item}, export_context="local_private")
        decision = classify_export_item(item, export_context="local_private")

        assert result.blocked is False
        assert result.payload["item"]["value"] == "Invented local-only value"
        assert "PRIVATE_LOCAL_ALLOWED_WITH_WARNING" in finding_codes(result)
        assert decision.action == "warning_only"
        assert decision.reason_code == "PRIVATE_LOCAL_ALLOWED_WITH_WARNING"


    def test_protected_or_professional_boundary_metadata_blocks_export():
        payload = invented_payload()
        payload["protected"] = {
            "field_id": "protected.synthetic",
            "field_class": "report_body",
            "privacy_classification": "protected_suspected",
            "redistribution_status": "protected_suspected",
            "review_status": "quarantined",
            "value": "OPS_SYNTHETIC_PROTECTED_MARKER",
        }
        payload["claim"] = {
            "field_id": "claim.synthetic",
            "field_class": "report_body",
            "privacy_classification": "public_metadata",
            "redistribution_status": "public_permissive",
            "review_status": "accepted",
            "professional_claim": True,
            "value": "OPS_SYNTHETIC_PROFESSIONAL_CLAIM_MARKER",
        }

        result = redact_export_payload(payload, export_context="shared_model")

        assert result.blocked is True
        assert "PROTECTED_CONTENT_BLOCKED" in finding_codes(result)
        assert "PROFESSIONAL_BOUNDARY_BLOCKED" in finding_codes(result)
        assert all(
            finding.severity == "BLOCKING"
            for finding in result.findings
            if finding.code in {"PROTECTED_CONTENT_BLOCKED", "PROFESSIONAL_BOUNDARY_BLOCKED"}
        )


    def test_missing_metadata_does_not_silently_export_value_bearing_record():
        payload = {"unclassified": {"field_id": "missing.metadata", "value": "Invented value"}}
        result = redact_export_payload(payload, export_context="downstream_tool")

        assert result.payload["unclassified"]["value"] == REDACTED_VALUE
        assert "MISSING_METADATA_REDACTED" in finding_codes(result)


    def test_documentation_and_memory_record_scope_boundaries():
        doc = DOC_PATH.read_text(encoding="utf-8")
        memory = MEMORY_PATH.read_text(encoding="utf-8")
        for required in {
            "deliverable_id: DEL-12-02",
            "package_id: PKG-12",
            "SOW-040",
            "OBJ-010",
            "explicit metadata only",
            "local-first",
            "does not mutate source project data",
        }:
            assert required in doc
        assert "DEL-12-02" in memory
        assert "invented fixtures only" in memory


    def test_changed_files_do_not_embed_disallowed_example_content():
        changed_files = [
            SCHEMA_PATH,
            DOC_PATH,
            MEMORY_PATH,
            ROOT / "core" / "security" / "redaction" / "__init__.py",
            ROOT / "core" / "security" / "redaction" / "controls.py",
            Path(__file__),
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in changed_files)
        for forbidden in FORBIDDEN_CHANGED_FILE_TERMS:
            assert forbidden not in combined


    if __name__ == "__main__":
        test_schema_is_strict_and_traceable()
        test_schema_vocabularies_cover_required_controls()
        test_public_report_redacts_private_and_unknown_values_without_mutating_source()
        test_local_private_export_requires_explicit_intent_then_retains_with_warning()
        test_protected_or_professional_boundary_metadata_blocks_export()
        test_missing_metadata_does_not_silently_export_value_bearing_record()
        test_documentation_and_memory_record_scope_boundaries()
        test_changed_files_do_not_embed_disallowed_example_content()

## Component: tests/security/test_secret_private_library_handling.py

    #!/usr/bin/env python3
    """Checks for DEL-12-04 secret/private-library reference handling."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(ROOT))

    from core.security.secret_private_library import (  # noqa: E402
        classify_reference,
        credential_placeholder,
        guard_reference_release,
        private_library_reference,
        private_path_reference,
    )


    DOC_PATH = ROOT / "docs" / "security" / "secret_private_library_handling.md"
    MEMORY_PATH = (
        ROOT
        / "execution"
        / "PKG-12_Security, Privacy, and Private Data Handling"
        / "1_Working"
        / "DEL-12-04_Secret and private-library handling"
        / "MEMORY.md"
    )

    FORBIDDEN_CHANGED_FILE_TERMS = {
        "AS" + "ME",
        "B" + "31",
        "B" + "31J",
        "allowable stress " + "table",
        "stress intensification factor " + "table",
        "vendor catalog " + "value",
        "real " + "secret",
        "private key " + "fixture",
        "cert" + "ified by " + "OpenPipeStress",
        "se" + "aled by " + "OpenPipeStress",
        "code " + "compliant",
    }


    def diagnostic_codes(result):
        return {diagnostic.code for diagnostic in result.diagnostics}


    def decision_codes(result):
        return {decision.reason_code for decision in result.decisions}


    def invented_private_library():
        return private_library_reference(
            reference_id="invented.private.materials",
            library_kind="material",
            label="Invented Private Material Library Reference",
            version="0.0-placeholder",
            checksum="sha256:0000000000000000000000000000000000000000000000000000000000000000",
            checksum_status="placeholder_checksum_recorded",
            source_note="invented local placeholder source note",
            redistribution_status="private_only",
            review_status="pending",
        )


    def test_private_library_classification_is_deterministic_and_metadata_only():
        first = classify_reference(invented_private_library())
        second = classify_reference(invented_private_library())

        assert first == second
        assert first.classification_id.startswith("SPL-CLS-")
        assert first.default_posture == "local_private_metadata_only"
        assert first.metadata["checksum"].startswith("sha256:0000")
        assert first.metadata["source_note"] == "invented local placeholder source note"
        assert first.metadata["contains_payload"] is False
        assert first.metadata["secret_material_present"] is False


    def test_public_report_keeps_private_reference_metadata_with_warning_only():
        result = guard_reference_release(
            [invented_private_library()],
            release_context="public_report",
        )

        assert result.blocked is False
        assert result.summary()["metadata_only"] is True
        assert "PRIVATE_REFERENCE_METADATA_ONLY" in decision_codes(result)
        assert result.safe_manifest[0]["reference_id"] == "invented.private.materials"
        assert result.safe_manifest[0]["checksum"].startswith("sha256:0000")


    def test_public_fixture_rejects_private_payloads_secret_values_and_unknown_rights():
        unsafe_records = [
            {
                "record_kind": "secret_field_reference",
                "reference_id": "invented.secret.value",
                "label": "api token field",
                "storage_locality": "USER_SECRET_REFERENCE",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "credential_reference",
                "value": "SYNTHETIC_SECRET_VALUE_SHOULD_NOT_SURVIVE",
            },
            {
                "record_kind": "private_material_library",
                "reference_id": "invented.private.library.payload",
                "label": "Private Library Payload Fixture",
                "storage_locality": "USER_PRIVATE_LIBRARY_ROOT",
                "privacy_classification": "private_material_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "library_payload": {"invented": "payload blocked"},
            },
            {
                "record_kind": "private_path_reference",
                "reference_id": "invented.private.path.payload",
                "label": "Private Path Payload Fixture",
                "storage_locality": "local_private",
                "privacy_classification": "path_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "path_payload": "FAKE_USER_PRIVATE_LIBRARY_ROOT/invented.ops",
            },
            {
                "record_kind": "private_component_library",
                "reference_id": "invented.unknown.redistribution",
                "label": "Unknown Redistribution Fixture",
                "storage_locality": "USER_PRIVATE_LIBRARY_ROOT",
                "privacy_classification": "private_component_data",
                "redistribution_status": "TBD",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "source_note": "TBD",
            },
        ]

        result = guard_reference_release(
            unsafe_records,
            release_context="public_fixture",
        )
        serialized = json.dumps(result.as_schema_dict(), sort_keys=True)

        assert result.blocked is True
        assert "SECRET_MATERIAL_REFERENCE_ONLY_REQUIRED" in decision_codes(result)
        assert "PRIVATE_LIBRARY_PAYLOAD_REFERENCE_ONLY_REQUIRED" in decision_codes(result)
        assert "PRIVATE_PATH_PAYLOAD_REFERENCE_ONLY_REQUIRED" in decision_codes(result)
        assert "UNKNOWN_REDIS_PRIVATE_DATA_BLOCKED" in decision_codes(result)
        assert "SYNTHETIC_SECRET_VALUE_SHOULD_NOT_SURVIVE" not in serialized
        assert "payload blocked" not in serialized
        assert "FAKE_USER_PRIVATE_LIBRARY_ROOT/invented.ops" not in serialized


    def test_public_shared_downstream_release_blocks_storage_boundary_markers():
        unsafe_records = [
            {
                "record_kind": "public_metadata",
                "reference_id": "invented.payload.marker",
                "label": "Invented payload marker",
                "storage_locality": "PUBLIC_REPOSITORY_CONTENT",
                "privacy_classification": "public_metadata",
                "redistribution_status": "public_permissive",
                "review_status": "accepted",
                "source_state": "invented_public",
                "payload_present": True,
                "raw_value": "SYNTHETIC_PAYLOAD_SHOULD_NOT_SURVIVE",
            },
            {
                "record_kind": "private_path_reference",
                "reference_id": "invented.concrete.path",
                "label": "Invented concrete path marker",
                "privacy_classification": "path_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "absolute_path": "/tmp/open-pipe-stress/invented-private-library.ops",
                "concrete_path_present": True,
            },
            {
                "record_kind": "private_library_reference",
                "reference_id": "invented.cloud.marker",
                "label": "Invented cloud marker",
                "privacy_classification": "private_library_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "cloud_or_network_reference": True,
                "cloud_url": "https://example.invalid/invented-private-library",
            },
            {
                "record_kind": "private_rule_pack",
                "reference_id": "invented.sql.marker",
                "label": "Invented SQL marker",
                "privacy_classification": "private_rule_pack_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "direct_sql_access": True,
                "sql": "SELECT invented_secret FROM private_rule_pack",
            },
            {
                "record_kind": "private_component_library",
                "reference_id": "invented.bypass.marker",
                "label": "Invented storage bypass marker",
                "privacy_classification": "private_component_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "private_user_supplied",
                "storage_bypass_requested": True,
            },
            {
                "record_kind": "secret_field_reference",
                "reference_id": "invented.external.secret.manager",
                "label": "Invented external secret manager marker",
                "privacy_classification": "secret_like_data",
                "redistribution_status": "private_only",
                "review_status": "pending",
                "source_state": "credential_reference",
                "external_secret_manager_reference": True,
                "secret_manager": "invented external vault",
            },
        ]

        for context in ("public_report", "shared_model", "downstream_tool"):
            result = guard_reference_release(unsafe_records, release_context=context)
            serialized = json.dumps(result.as_schema_dict(), sort_keys=True)

            assert result.blocked is True
            assert "REFERENCE_PAYLOAD_METADATA_ONLY_REQUIRED" in decision_codes(result)
            assert "CLOUD_OR_NETWORK_REFERENCE_BLOCKED" in decision_codes(result)
            assert "DIRECT_SQL_ACCESS_BLOCKED" in decision_codes(result)
            assert "STORAGE_BYPASS_BLOCKED" in decision_codes(result)
            assert "EXTERNAL_SECRET_MANAGER_BLOCKED" in decision_codes(result)
            assert "CONCRETE_PATH_REDUCED_TO_SAFE_METADATA" in diagnostic_codes(result)
            assert "SYNTHETIC_PAYLOAD_SHOULD_NOT_SURVIVE" not in serialized
            assert "/tmp/open-pipe-stress/invented-private-library.ops" not in serialized
            assert "https://example.invalid/invented-private-library" not in serialized
            assert "SELECT invented_secret FROM private_rule_pack" not in serialized
            assert "invented external vault" not in serialized
            assert result.summary()["cloud_or_network_block_count"] == 1
            assert result.summary()["direct_sql_block_count"] == 1
            assert result.summary()["storage_bypass_block_count"] == 1
            assert result.summary()["concrete_paths_emitted"] is False


    def test_concrete_private_path_helper_withholds_path_detail():
        record = private_path_reference(
            reference_id="invented.direct.path.helper",
            path_class="/tmp/open-pipe-stress/direct-private-library.ops",
            label="Invented direct path helper",
            source_note="invented direct path descriptor only",
        )
        result = guard_reference_release([record], release_context="public_report")
        serialized = json.dumps(result.as_schema_dict(), sort_keys=True)

        assert result.safe_manifest[0]["value_descriptor"] == "concrete path detail withheld"
        assert result.safe_manifest[0]["concrete_path_present"] is True
        assert "CONCRETE_PATH_REDUCED_TO_SAFE_METADATA" in diagnostic_codes(result)
        assert "/tmp/open-pipe-stress/direct-private-library.ops" not in serialized


    def test_local_private_intent_required_and_payloads_remain_blocked():
        private_ref = invented_private_library()
        blocked = guard_reference_release(
            [private_ref],
            release_context="local_private",
            explicit_local_private_intent=False,
        )
        allowed = guard_reference_release(
            [private_ref],
            release_context="local_private",
            explicit_local_private_intent=True,
        )
        payload_blocked = guard_reference_release(
            [
                private_path_reference(
                    reference_id="invented.private.path",
                    path_class="USER_PRIVATE_LIBRARY_ROOT",
                    label="Invented private path placeholder",
                    source_note="invented path descriptor only",
                    contains_payload=True,
                )
            ],
            release_context="local_private",
            explicit_local_private_intent=True,
        )

        assert blocked.blocked is True
        assert "LOCAL_PRIVATE_INTENT_REQUIRED" in decision_codes(blocked)
        assert allowed.blocked is False
        assert "PRIVATE_LOCAL_METADATA_ALLOWED" in decision_codes(allowed)
        assert payload_blocked.blocked is True
        assert "PRIVATE_PATH_PAYLOAD_REFERENCE_ONLY_REQUIRED" in decision_codes(payload_blocked)


    def test_credential_placeholder_uses_fake_key_id_and_descriptor_only():
        placeholder = credential_placeholder(
            reference_id="invented.credential.placeholder",
            placeholder_key_id="fake-key-id:del-12-04-placeholder",
            credential_descriptor="placeholder:license-token-reference",
            review_status="pending",
        )
        classification = classify_reference(placeholder)

        assert classification.privacy_classification == "secret_like_data"
        assert classification.metadata["storage_locality"] == "USER_SECRET_REFERENCE"
        assert "fake-key-id:del-12-04-placeholder" in classification.metadata["value_descriptor"]
        assert classification.metadata["contains_payload"] is False
        assert classification.metadata["secret_material_present"] is False


    def test_documentation_and_memory_record_scope_boundaries():
        doc = DOC_PATH.read_text(encoding="utf-8")
        memory = MEMORY_PATH.read_text(encoding="utf-8")
        for required in {
            "deliverable_id: DEL-12-04",
            "package_id: PKG-12",
            "SOW-040",
            "SOW-029",
            "OBJ-010",
            "metadata-only",
            "local-first",
            "invented fixtures only",
        }:
            assert required in doc
        assert "DEL-12-04" in memory
        assert "invented fixtures only" in memory


    def test_changed_files_do_not_embed_disallowed_example_content():
        changed_files = [
            DOC_PATH,
            MEMORY_PATH,
            ROOT / "core" / "security" / "secret_private_library" / "__init__.py",
            ROOT / "core" / "security" / "secret_private_library" / "controls.py",
            Path(__file__),
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in changed_files)
        for forbidden in FORBIDDEN_CHANGED_FILE_TERMS:
            assert forbidden not in combined


    if __name__ == "__main__":
        test_private_library_classification_is_deterministic_and_metadata_only()
        test_public_report_keeps_private_reference_metadata_with_warning_only()
        test_public_fixture_rejects_private_payloads_secret_values_and_unknown_rights()
        test_public_shared_downstream_release_blocks_storage_boundary_markers()
        test_concrete_private_path_helper_withholds_path_detail()
        test_local_private_intent_required_and_payloads_remain_blocked()
        test_credential_placeholder_uses_fake_key_id_and_descriptor_only()
        test_documentation_and_memory_record_scope_boundaries()
        test_changed_files_do_not_embed_disallowed_example_content()

## Component: tests/security/test_telemetry_policy.py

    #!/usr/bin/env python3
    """Policy checks for the telemetry-off-by-default contract."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(ROOT))

    from core.security.telemetry_policy import (  # noqa: E402
        TelemetryConfig,
        TelemetryEventAttempt,
        guard_telemetry_event,
        resolve_telemetry_config,
    )

    POLICY_PATH = ROOT / "docs" / "security" / "telemetry_policy.md"

    TRACEABILITY = {
        "deliverable_id: DEL-12-03",
        "package_id: PKG-12",
        "SOW-037",
        "OBJ-010",
    }

    DEFAULT_OFF_TERMS = {
        "Telemetry is disabled by default.",
        "Absent",
        "unset",
        "unknown",
        "unsupported",
        "malformed",
        "resolves to disabled",
        "Fail-closed behavior is required",
    }

    INITIALIZATION_BANS = {
        "network transport",
        "background upload jobs",
        "upload queues",
        "local telemetry persistence",
        "endpoints",
        "vendors",
        "external service clients",
    }

    ALLOWLIST_TERMS = {
        "human-approved event allowlist",
        "No event is collectable until it appears in a human-approved allowlist.",
        "Unknown events",
        "fields not listed on the allowlist",
        "rejected before payload construction",
    }

    FORBIDDEN_FIELD_CLASSES = {
        "Private project models",
        "Code-specific rule data",
        "Private rule packs",
        "Private material or component libraries",
        "Generated reports and exports",
        "Model hashes",
        "Local file paths",
        "Secrets and credentials",
        "Protected standards content",
        "Professional or code-compliance claims",
    }

    TBD_DECISIONS = {
        "Product configuration schema",
        "Consent UI or CLI surface",
        "Endpoint, vendor, transport, and retention policy",
        "Concrete event schema and event allowlist",
    }

    HELPER_DOC_TERMS = {
        "metadata-only telemetry guard helper",
        "does not authorize endpoint, vendor, transport, queue, upload, persistence, or telemetry payload construction",
        "returns diagnostics and a decision before payload construction",
    }

    DISALLOWED_IMPLEMENTATION_COMMITMENTS = {
        "https://",
        "http://",
        "segment",
        "amplitude",
        "posthog",
        "sentry",
        "telemetry endpoint is",
        "vendor is",
    }


    def approved_metadata_config():
        return {
            "enabled": True,
            "explicit_opt_in": True,
            "consent_surface": "approved.settings.telemetry",
            "approved_consent_surfaces": ["approved.settings.telemetry"],
            "allowlist_approved": True,
            "allowlist_approval_record": "human-approved-placeholder",
            "event_allowlist": {
                "app_started": {
                    "fields": ["app_version", "os_family"],
                }
            },
        }


    def policy_text():
        return POLICY_PATH.read_text(encoding="utf-8")


    def lower_policy_text():
        return policy_text().lower()


    def test_policy_is_traceable_to_deliverable_scope():
        text = policy_text()
        for required in TRACEABILITY:
            assert required in text


    def test_absent_or_malformed_config_fails_closed_to_disabled():
        text = policy_text()
        for required in DEFAULT_OFF_TERMS:
            assert required in text


    def test_transport_and_persistence_require_opt_in_and_allowlist():
        text = policy_text()
        assert "unless all of these are true" in text
        assert "the user has explicitly opted in" in text
        assert "a human-approved event allowlist exists" in text
        assert "event is dropped locally without network behavior" in text
        for banned_surface in INITIALIZATION_BANS:
            assert banned_surface in text


    def test_event_allowlist_rejects_unknown_or_unapproved_fields():
        text = policy_text()
        for required in ALLOWLIST_TERMS:
            assert required in text


    def test_forbidden_payload_field_classes_are_explicit():
        text = policy_text()
        for field_class in FORBIDDEN_FIELD_CLASSES:
            assert field_class in text


    def test_open_decisions_remain_tbd_without_vendor_or_endpoint():
        text = policy_text()
        lowered = lower_policy_text()
        for decision in TBD_DECISIONS:
            assert decision in text
        assert "no endpoint, vendor, transport, or retention behavior is authorized" in text
        for disallowed in DISALLOWED_IMPLEMENTATION_COMMITMENTS:
            assert disallowed not in lowered


    def test_policy_documents_metadata_only_guard_non_authority():
        text = policy_text()
        normalized = " ".join(text.split())
        for required in HELPER_DOC_TERMS:
            assert required in normalized


    def test_resolve_config_absent_empty_unknown_or_malformed_disables_telemetry():
        cases = [
            None,
            {},
            {"mode": "on"},
            {"enabled": "true"},
            {"enabled": True, "endpoint": "TBD"},
        ]

        for case in cases:
            config = resolve_telemetry_config(case)
            assert config.enabled is False
            assert config.requested_enabled is False or config.reason_code in {
                "telemetry_config_unknown",
                "telemetry_config_malformed",
            }
            assert config.as_schema_dict()["network_transport_initialized"] is False
            assert config.as_schema_dict()["telemetry_persistence_initialized"] is False


    def test_enabled_config_requires_opt_in_approved_surface_and_allowlist():
        base = approved_metadata_config()
        missing_opt_in = {**base, "explicit_opt_in": False}
        unapproved_surface = {**base, "consent_surface": "unapproved.surface"}
        no_allowlist_approval = {**base, "allowlist_approved": False}
        empty_allowlist = {**base, "event_allowlist": {}}

        for case in (
            missing_opt_in,
            unapproved_surface,
            no_allowlist_approval,
            empty_allowlist,
        ):
            config = resolve_telemetry_config(case)
            assert config.enabled is False
            assert config.requested_enabled is True
            assert config.reason_code == "telemetry_gates_incomplete"


    def test_prebuilt_enabled_config_is_still_rechecked_fail_closed():
        manually_enabled = TelemetryConfig(
            enabled=True,
            requested_enabled=True,
            explicit_opt_in=False,
            consent_surface="TBD",
            approved_consent_surfaces=(),
            allowlist_approved=False,
        )

        resolved = resolve_telemetry_config(manually_enabled)

        assert resolved.enabled is False
        assert resolved.requested_enabled is True
        assert resolved.reason_code == "telemetry_gates_incomplete"


    def test_allowlisted_metadata_event_passes_without_payload_or_transport():
        result = guard_telemetry_event(
            approved_metadata_config(),
            TelemetryEventAttempt(
                event_name="app_started",
                field_names=("app_version", "os_family"),
                field_classes={
                    "app_version": "operational_metadata",
                    "os_family": "operational_metadata",
                },
                event_version="0",
                source_surface="unit_test",
            ),
        )

        assert result.blocked is False
        assert result.decision.action == "allow_metadata_event"
        assert result.decision.payload_constructed is False
        assert result.decision.network_behavior_initialized is False
        assert result.safe_metadata["field_names"] == ["app_version", "os_family"]
        summary = result.summary()
        assert summary["payload_constructed"] is False
        assert summary["network_transport_initialized"] is False
        assert summary["endpoint_initialized"] is False
        assert summary["vendor_initialized"] is False
        assert summary["upload_queue_initialized"] is False
        assert summary["upload_job_initialized"] is False
        assert summary["telemetry_persistence_initialized"] is False
        assert summary["external_service_client_initialized"] is False


    def test_unknown_event_and_unknown_field_are_rejected_before_payload_construction():
        unknown_event = guard_telemetry_event(
            approved_metadata_config(),
            {
                "event_name": "solver_used",
                "fields": {"app_version": "operational_metadata"},
            },
        )
        unknown_field = guard_telemetry_event(
            approved_metadata_config(),
            {
                "event_name": "app_started",
                "fields": {
                    "app_version": "operational_metadata",
                    "session_identifier": "operational_metadata",
                },
            },
        )

        assert unknown_event.blocked is True
        assert unknown_event.decision.reason_code == "telemetry_event_not_allowlisted"
        assert unknown_event.summary()["payload_constructed"] is False
        assert unknown_field.blocked is True
        assert unknown_field.decision.reason_code == "telemetry_field_not_allowlisted"
        assert "session_identifier" in unknown_field.decision.rejected_field_names
        assert unknown_field.summary()["network_transport_initialized"] is False


    def test_forbidden_private_path_hash_report_secret_and_claim_fields_are_rejected():
        for field_name, field_class in (
            ("app_version", "private_project_data"),
            ("app_version", "protected_suspected"),
            ("app_version", "secret_like_data"),
            ("app_version", "path_data"),
            ("app_version", "model_hash"),
            ("app_version", "generated_report"),
            ("app_version", "professional_claim"),
        ):
            result = guard_telemetry_event(
                approved_metadata_config(),
                {
                    "event_name": "app_started",
                    "fields": {
                        field_name: field_class,
                    },
                },
            )
            assert result.blocked is True
            assert result.decision.reason_code == "telemetry_forbidden_field"
            assert result.decision.payload_constructed is False
            assert result.summary()["network_transport_initialized"] is False


    def test_payload_shaped_event_attempt_is_rejected_before_allowlist_payload_build():
        result = guard_telemetry_event(
            approved_metadata_config(),
            {
                "event_name": "app_started",
                "fields": {
                    "app_version": {
                        "field_class": "operational_metadata",
                        "value": "fixture-version",
                    },
                },
            },
        )

        assert result.blocked is True
        assert result.decision.reason_code == "telemetry_payload_attempt_before_guard"
        assert result.decision.payload_constructed is False
        assert result.summary()["telemetry_persistence_initialized"] is False


    def test_no_runtime_networking_or_product_dependency_was_added():
        assert not (ROOT / "core" / "telemetry").exists()
        assert not (ROOT / "apps" / "telemetry").exists()
        assert not (ROOT / "schemas" / "telemetry.schema.yaml").exists()

## Component: tests/test_accessibility_usability_baseline.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-06 accessibility/usability baseline records."""

    from copy import deepcopy
    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.accessibility import (  # noqa: E402
        build_accessibility_usability_baseline,
        canonical_json,
    )
    from core.gui.editors import build_editor_contract  # noqa: E402
    from core.gui.model_tree import build_model_tree_property_inspector  # noqa: E402
    from core.gui.results_viewer import build_results_viewer_contract  # noqa: E402
    from core.gui.solve_execution import build_solve_execution_ux  # noqa: E402
    from core.gui.warnings import build_warning_ux_contract  # noqa: E402


    VIEWPORT_FIXTURE = ROOT / "fixtures" / "gui" / "invented" / "viewport_editor_session.json"
    REQUIRED_SURFACES = {"DEL-07-01", "DEL-07-02", "DEL-07-03", "DEL-07-04", "DEL-07-05", "DEL-07-07"}
    REQUIRED_FINDING_FIELDS = {
        "finding_id",
        "category",
        "outcome",
        "source_surface",
        "affected_control",
        "severity",
        "remediation_note",
        "evidence_refs",
    }
    REQUIRED_CATEGORIES = {
        "keyboard_path",
        "focus_order",
        "readable_label",
        "warning_visibility",
        "result_review_visibility",
        "solve_state_feedback",
        "review_workflow_continuity",
        "contrast_readability",
        "source_diagnostic_visibility",
        "professional_boundary",
        "privacy_boundary",
    }
    FORBIDDEN_TEXT = (
        "code " + "compliant",
        "certif" + "ied",
        "seal" + "ed",
        "professional " + "acceptance",
        "professional " + "approval",
        "accessibility " + "certified",
        "real " + "secret",
    )


    def load_viewport_contract():
        with VIEWPORT_FIXTURE.open(encoding="utf-8") as json_file:
            return json.load(json_file)


    def invented_contract_records():
        return [
            load_viewport_contract(),
            build_model_tree_property_inspector(
                project_id="invented-accessibility-project",
                selected_ref={"ref_type": "pipe_run", "ref_id": "pipe-P1"},
                entities=[
                    {
                        "entity_id": "node-N1",
                        "entity_type": "node",
                        "label": "Invented node N1",
                        "sort_key": "001",
                        "properties": [
                            {
                                "field_id": "elevation",
                                "label": "Elevation",
                                "value": 12.0,
                                "unit": "m",
                                "editable": True,
                            }
                        ],
                        "provenance_state": "invented_public_example",
                        "privacy_classification": "invented_public_example",
                    },
                    {
                        "entity_id": "pipe-P1",
                        "entity_type": "pipe_run",
                        "label": "Invented pipe P1",
                        "sort_key": "002",
                        "properties": [
                            {
                                "field_id": "nominal_size",
                                "label": "Nominal size",
                                "value": "TBD",
                                "unit": "mm",
                                "editable": True,
                            }
                        ],
                        "privacy_classification": "invented_public_example",
                    },
                ],
            ),
            build_editor_contract(
                editor_set_id="invented-accessibility-editor-set",
                editors=[
                    {
                        "editor_id": "material-editor",
                        "editor_kind": "material",
                        "target_ref": {"ref_type": "material", "ref_id": "mat-public-1"},
                        "library_classification": "invented_public_example",
                        "fields": [
                            {
                                "field_id": "density",
                                "label": "Density",
                                "value": 7850.0,
                                "unit": "kg/m^3",
                                "dimension": "density",
                                "source_ref": {"ref_type": "invented_source", "ref_id": "src-1"},
                            }
                        ],
                    },
                    {
                        "editor_id": "rule-pack-reference",
                        "editor_kind": "rule_pack_reference",
                        "target_ref": {"ref_type": "rule_pack", "ref_id": "rp-invented-ref"},
                        "library_classification": "private_reference_only",
                        "fields": [{"field_id": "rule_pack_name", "label": "Rule pack name", "value": "TBD"}],
                        "rule_pack_lifecycle": {"state": "referenced"},
                    },
                ],
            ),
            build_warning_ux_contract(
                warning_set_id="invented-accessibility-warning-set",
                conditions=[
                    {
                        "warning_id": "warn-missing-support",
                        "warning_class": "incomplete_data",
                        "target_ref": {"ref_type": "support", "ref_id": "support-TBD"},
                        "message": "Invented support has unresolved stiffness.",
                        "source_status": "missing",
                    },
                    {
                        "warning_id": "warn-assumption",
                        "warning_class": "assumption",
                        "target_ref": {"ref_type": "load_case", "ref_id": "load-1"},
                        "source_status": "provided",
                        "assumption_ref": {"ref_type": "assumption", "ref_id": "assumption-1"},
                    },
                ],
            ),
            build_results_viewer_contract(
                result_set_id="invented-accessibility-results",
                result_items=[
                    {
                        "result_id": "disp-node-1",
                        "result_kind": "displacement",
                        "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                        "hashes": [
                            {
                                "algorithm": "sha256",
                                "canonicalization": "JCS",
                                "payload_ref": {"ref_type": "ResultEnvelope", "ref_id": "results:accessibility"},
                                "value": "sha256:invented-accessibility-result",
                            }
                        ],
                        "provenance_refs": [{"ref_type": "AnalysisRun", "ref_id": "run:accessibility"}],
                        "values": [
                            {
                                "value_id": "ux",
                                "component": "UX",
                                "numeric_value": 1.2,
                                "unit": "mm",
                                "dimension": "displacement",
                                "location_ref": {"ref_type": "node", "ref_id": "N1"},
                            }
                        ],
                        "overlay_enabled": True,
                        "overlay_target_ref": {"ref_type": "node", "ref_id": "N1"},
                    },
                    {
                        "result_id": "stress-tbd",
                        "result_kind": "stress",
                        "values": [{"value_id": "smax", "numeric_value": "TBD", "unit": "MPa", "dimension": "stress"}],
                    },
                ],
            ),
            build_solve_execution_ux(
                run_panel_id="invented-accessibility-run-panel",
                events=[
                    {"event_id": "queued", "state": "queued", "progress_percent": 0},
                    {
                        "event_id": "running",
                        "state": "running",
                        "progress_percent": 40,
                        "diagnostic_refs": [{"ref_type": "diagnostic", "ref_id": "diag-1"}],
                        "warning_refs": [{"ref_type": "warning", "ref_id": "warn-missing-support"}],
                    },
                ],
            ),
        ]


    def main():
        records = invented_contract_records()
        records_before = canonical_json(deepcopy(records))

        baseline = build_accessibility_usability_baseline(
            baseline_id="invented-accessibility-baseline",
            gui_contract_records=records,
        )
        again = build_accessibility_usability_baseline(
            baseline_id="invented-accessibility-baseline",
            gui_contract_records=list(reversed(records)),
        )

        assert canonical_json(baseline) == canonical_json(again)
        assert canonical_json(records) == records_before
        assert baseline["deliverable_id"] == "DEL-07-06"
        assert baseline["review_mode"] == "deterministic_contract_records_no_live_desktop_runtime"
        assert baseline["accessibility_target_status"] == "TBD_by_human_project_authority"
        assert baseline["desktop_runtime_evaluation"] == "not_performed"
        assert baseline["review_policy"]["auto_fill_missing_data"] is False
        assert baseline["review_policy"]["mutates_gui_contract_records"] is False
        assert baseline["review_policy"]["software_makes_accessibility_conformance_claim"] is False
        assert baseline["professional_boundary"]["software_makes_compliance_claim"] is False

        surface_ids = {item["deliverable_id"] for item in baseline["source_surfaces"]}
        assert surface_ids == REQUIRED_SURFACES

        findings = baseline["findings"]
        assert findings == sorted(findings, key=canonical_json)
        assert all(REQUIRED_FINDING_FIELDS <= set(item) for item in findings)
        assert all(item["source_surface"] for item in findings)
        assert all(item["affected_control"] for item in findings)
        assert all(item["remediation_note"] for item in findings)
        assert REQUIRED_CATEGORIES <= {item["category"] for item in findings}
        assert {"pass", "warning", "fail", "not_applicable"} <= {item["outcome"] for item in findings}
        assert baseline["summary"]["by_outcome"]["fail"] >= 1
        assert baseline["summary"]["by_outcome"]["warning"] >= 1
        assert baseline["summary"]["by_outcome"]["not_applicable"] >= 1

        text = canonical_json(baseline)
        for expected in (
            "PROPERTY_VALUE_UNRESOLVED",
            "RULE_PACK_CHECKSUM_MISSING",
            "EDITOR_FIELD_VALUE_UNRESOLVED",
            "WARNING_SOURCE_STATUS_UNRESOLVED",
            "RESULT_VALUE_OR_UNIT_UNRESOLVED",
            "SOLVE_UX_TERMINAL_STATE_PENDING",
            "unresolved_TBD",
        ):
            assert expected in text

        lowered = text.lower()
        for term in FORBIDDEN_TEXT:
            assert term not in lowered


    def test_accessibility_usability_baseline_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_adapter_framework_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the adapter framework contract."""

    import copy
    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))

    SCHEMA_PATH = ROOT / "schemas" / "adapter_framework.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "adapters" / "invented" / "invented_adapter_framework.json"

    from core.adapters.framework import (  # noqa: E402
        build_result,
        validate_adapter_declaration,
    )


    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objective",
        "framework_status",
        "tbd_decisions",
        "adapter_declaration",
        "validation_plan",
        "operation_result",
    }

    REQUIRED_DEFS = {
        "AdapterCapability",
        "AdapterDeclaration",
        "AdapterOperationResult",
        "ChecksumRef",
        "Diagnostic",
        "FrameworkStatus",
        "NoBypassControls",
        "OperationBoundary",
        "PrivacyContext",
        "ProfessionalBoundary",
        "Provenance",
        "Reference",
        "ResultEnvelopeRef",
        "TbdDecisions",
        "ValidationPlan",
    }

    REQUIRED_TBD = {
        "external_format_list",
        "public_transport_protocol",
        "endpoint_syntax",
        "adapter_execution_model",
        "plugin_runtime",
        "permission_grant_persistence",
        "package_scripts",
        "ci_provider",
        "release_matrix",
        "physical_project_container",
        "local_fea_package_format",
        "redaction_workflow",
    }

    REQUIRED_NO_BYPASS = {
        "must_use_public_api_boundary",
        "must_use_unit_validation",
        "must_preserve_provenance",
        "must_preserve_redistribution_review",
        "must_preserve_privacy_classification",
        "must_screen_protected_content",
        "must_preserve_diagnostics",
        "must_preserve_rule_pack_sandbox",
        "must_preserve_persistence_hash_controls",
        "must_route_persistence_through_application_services",
        "must_not_expose_sql_or_raw_sqlite",
        "must_not_expose_table_names",
        "must_not_mutate_project_store_directly",
        "must_preserve_report_controls",
        "must_preserve_human_acceptance_boundary",
        "must_not_execute_arbitrary_code",
        "must_not_access_network",
        "must_not_choose_filesystem_roots",
        "must_not_claim_code_compliance",
        "must_not_transmit_private_data_by_default",
    }

    REQUIRED_VALIDATION = {
        "schema_validation",
        "unit_validation",
        "dimension_validation",
        "provenance_validation",
        "redistribution_review",
        "privacy_classification",
        "protected_content_screening",
    }

    FORBIDDEN_TERMS = {
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED_FOR_PROFESSIONAL_RELIANCE",
        "SECURITY_CERTIFIED",
        "COMPLIANCE_ATTESTED",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def current_authority_fixture():
        fixture = load_json(FIXTURE_PATH)
        fixture["adapter_declaration"]["no_bypass_controls"].update(
            {key: True for key in REQUIRED_NO_BYPASS}
        )
        return fixture


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def codes(result):
        return {finding.code for finding in result.findings}


    def test_schema_contract_shape_and_traceability():
        schema = load_json(SCHEMA_PATH)
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-10-02"
        assert schema["properties"]["package_id"]["const"] == "PKG-10"
        assert schema["properties"]["scope_item"]["const"] == "SOW-030"
        assert schema["properties"]["objective"]["const"] == "OBJ-009"


    def test_schema_keeps_runtime_and_format_decisions_tbd():
        schema = load_json(SCHEMA_PATH)

        status = schema["$defs"]["FrameworkStatus"]["properties"]
        assert status["interface_kind"]["const"] == (
            "schema_first_format_neutral_adapter_framework"
        )
        for key in REQUIRED_TBD - {"package_scripts"}:
            assert status[key]["const"] == "TBD"

        tbd = schema["$defs"]["TbdDecisions"]
        assert REQUIRED_TBD <= set(tbd["required"])
        for key in REQUIRED_TBD:
            assert tbd["properties"][key]["const"] == "TBD"


    def test_schema_requires_no_bypass_and_validation_hooks():
        schema = load_json(SCHEMA_PATH)

        assert REQUIRED_NO_BYPASS <= required_at(schema, "NoBypassControls")
        for key in REQUIRED_NO_BYPASS:
            assert schema["$defs"]["NoBypassControls"]["properties"][key]["const"] is True

        assert REQUIRED_VALIDATION <= required_at(schema, "ValidationPlan")
        plan = schema["$defs"]["ValidationPlan"]["properties"]
        for key in REQUIRED_VALIDATION:
            assert plan[key]["const"] == "required"
        assert plan["human_review_required"]["const"] is True

        assert {
            "import_model",
            "export_model",
            "import_library",
            "export_library",
            "validate_payload",
            "contribution_review",
        } <= enum_at(schema, "AdapterCapability")


    def test_schema_preserves_diagnostics_privacy_result_and_authority_boundaries():
        schema = load_json(SCHEMA_PATH)
        defs = schema["$defs"]

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required

        diagnostic_classes = set(defs["Diagnostic"]["properties"]["class"]["enum"])
        assert {
            "PROVENANCE_WARNING",
            "IP_BOUNDARY_WARNING",
            "UNIT_WARNING",
            "PRIVACY_WARNING",
            "EXPORT_BLOCKING",
            "ADAPTER_BLOCKING",
            "RULE_CHECK_BLOCKING",
        } <= diagnostic_classes

        privacy = defs["PrivacyContext"]["properties"]
        assert privacy["local_first"]["const"] is True
        assert privacy["telemetry_allowed"]["const"] is False
        assert "protected_suspected" in privacy["classification"]["enum"]
        assert "export_review_required" in privacy["classification"]["enum"]

        result_ref = defs["ResultEnvelopeRef"]["properties"]
        assert result_ref["schema_ref"]["const"] == "schemas/results.schema.yaml"
        assert result_ref["compatibility"]["const"] == "schema_first_json_result_envelope"

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["mechanics_solve_distinct"]["const"] is True
        assert boundary["user_rule_check_distinct"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_security_certification_claim"]["const"] is False


    def test_invented_fixture_is_format_neutral_and_accepted():
        fixture = load_json(FIXTURE_PATH)
        result = validate_adapter_declaration(fixture)

        assert result.accepted is True
        assert result.outcome == "ACCEPTED_FORMAT_NEUTRAL_DECLARATION"
        assert result.findings == ()
        assert fixture["adapter_declaration"]["format_status"] == "TBD"
        assert fixture["operation_result"]["parse_status"] == "not_parsed_by_framework"
        assert fixture["adapter_declaration"]["privacy"]["local_first"] is True
        assert fixture["adapter_declaration"]["privacy"]["telemetry_allowed"] is False


    def test_concrete_format_selection_is_rejected():
        fixture = current_authority_fixture()
        fixture["adapter_declaration"]["format_status"] = "real_format_name"

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "ADAPTER_FORMAT_SELECTED" in codes(result)


    def test_direct_persistence_access_is_rejected():
        fixture = current_authority_fixture()
        fixture["adapter_declaration"]["persistence_escape_hatch"] = {
            "raw_sqlite_handle": "sqlite://project.db",
            "table_names": ["projects", "model_objects"],
            "direct_store_mutation": True,
        }

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "ADAPTER_FORBIDDEN_PERSISTENCE_ACCESS" in codes(result)


    def test_missing_provenance_blocks_adapter_declaration():
        fixture = current_authority_fixture()
        del fixture["adapter_declaration"]["provenance"]["source_license"]

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "ADAPTER_PROVENANCE_INCOMPLETE" in codes(result)


    def test_protected_suspected_fixture_quarantines():
        fixture = current_authority_fixture()
        fixture["adapter_declaration"]["provenance"][
            "redistribution_status"
        ] = "protected_suspected"

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert result.outcome == "QUARANTINE"
        assert "ADAPTER_PROTECTED_CONTENT_SUSPECTED" in codes(result)


    def test_no_bypass_controls_are_enforced():
        fixture = current_authority_fixture()
        fixture["adapter_declaration"]["no_bypass_controls"][
            "must_use_unit_validation"
        ] = False

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert "ADAPTER_NO_BYPASS_CONTROL_DISABLED" in codes(result)


    def test_application_service_persistence_no_bypass_controls_are_enforced():
        fixture = current_authority_fixture()
        fixture["adapter_declaration"]["no_bypass_controls"][
            "must_route_persistence_through_application_services"
        ] = False

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert "ADAPTER_NO_BYPASS_CONTROL_DISABLED" in codes(result)


    def test_operation_result_builder_preserves_boundaries():
        finding_result = validate_adapter_declaration({})
        built = build_result(
            operation_id="ops.adapter.test.validation",
            operation_class="validate",
            diagnostics=finding_result.findings[:1],
        )

        assert built["parse_status"] == "not_parsed_by_framework"
        assert built["privacy"]["local_first"] is True
        assert built["privacy"]["telemetry_allowed"] is False
        assert built["result_envelope_ref"]["schema_ref"] == "schemas/results.schema.yaml"
        assert built["professional_boundary"]["software_makes_compliance_claim"] is False


    def test_schema_and_fixture_do_not_contain_forbidden_status_terms():
        combined = f"{SCHEMA_PATH.read_text(encoding='utf-8')}\n{FIXTURE_PATH.read_text(encoding='utf-8')}"
        combined_upper = combined.upper()
        for term in FORBIDDEN_TERMS:
            assert term not in combined_upper


    def test_premature_tbd_resolution_is_rejected():
        fixture = copy.deepcopy(current_authority_fixture())
        fixture["tbd_decisions"]["public_transport_protocol"] = "http"

        result = validate_adapter_declaration(fixture)

        assert result.accepted is False
        assert "ADAPTER_DECISION_PREMATURE" in codes(result)


    if __name__ == "__main__":
        test_schema_contract_shape_and_traceability()
        test_schema_keeps_runtime_and_format_decisions_tbd()
        test_schema_requires_no_bypass_and_validation_hooks()
        test_schema_preserves_diagnostics_privacy_result_and_authority_boundaries()
        test_invented_fixture_is_format_neutral_and_accepted()
        test_concrete_format_selection_is_rejected()
        test_direct_persistence_access_is_rejected()
        test_missing_provenance_blocks_adapter_declaration()
        test_protected_suspected_fixture_quarantines()
        test_no_bypass_controls_are_enforced()
        test_application_service_persistence_no_bypass_controls_are_enforced()
        test_operation_result_builder_preserves_boundaries()
        test_schema_and_fixture_do_not_contain_forbidden_status_terms()
        test_premature_tbd_resolution_is_rejected()

## Component: tests/test_agent_rationale_boundary.py

    #!/usr/bin/env python3
    """Focused tests for DEL-16-04 agent rationale boundary controls."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.model_operations.agent_rationale import canonical_json, record_agent_rationale  # noqa: E402
    from core.model_operations.audit_trail import record_operation_audit_trail  # noqa: E402
    from core.model_operations.validation_preview import validate_and_preview_operations  # noqa: E402


    OPERATION_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_operation_set_valid.json"
    MODEL_STATE_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_accepted_model_state.json"


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def validation():
        return {
            "schema_validation": "pending",
            "constraint_validation": "pending",
            "unit_validation": "pending",
            "diff_preview_status": "not_generated",
            "application_status": "not_applied",
        }


    def model_state():
        with MODEL_STATE_FIXTURE.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def quantity_change():
        return {
            "change_id": "change:diameter",
            "change_kind": "set_field",
            "target_object_type": "Component",
            "target_ref": ref("Component", "component:pipe-1"),
            "value_payload": {
                "value_kind": "quantity",
                "scalar_values": [],
                "quantity_values": [{"value": 125.0, "unit": "mm", "dimension": "length"}],
                "reference_values": [],
                "structured_values": [{"diameter": {"value": 125.0, "unit": "mm", "dimension": "length"}}],
                "notes": [],
            },
            "unit_requirements": {
                "unit_metadata_required": True,
                "dimension_check_required": True,
                "missing_unit_behavior": "emit_diagnostic",
            },
        }


    def operation_envelope(*, assumptions=None):
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        operation = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )
        operation["operation_status"] = "ready_for_user_review"
        operation["assumptions"] = assumptions or []
        envelope["operation_set"]["operations"] = [operation]
        return envelope


    def assumption(assumption_id, status):
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        provenance = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )["provenance"]
        return {
            "assumption_id": assumption_id,
            "statement": "Invented operation assumption for rationale testing.",
            "status": status,
            "affected_refs": [ref("ModelOperation", "op:resize")],
            "provenance": deepcopy(provenance),
        }


    def acceptance_signal():
        return {
            "decision": "accept",
            "accepted": True,
            "actor_type": "user",
            "actor_ref": "user:reviewer",
            "source_role": "project_user",
            "decided_at": "2026-05-06T12:00:00Z",
            "rationale": "Invented example review accepted for audit trail test.",
        }


    def preview_ref():
        return {
            "object_type": "DiffPreview",
            "ref": "preview:resize",
            "hash": "sha256:invented-preview",
        }


    def audit_and_preview(envelope):
        preview = validate_and_preview_operations(envelope, model_state())
        audit = record_operation_audit_trail(
            envelope,
            validation_outcome=preview,
            diff_preview_ref=preview_ref(),
            acceptance_signal=acceptance_signal(),
            actor={"actor_type": "user", "actor_ref": "user:reviewer"},
            source={"source_ref": "operation-workbench:invented", "source_channel": "test"},
            accepted_model_state=model_state(),
        )
        return audit, preview


    def rationale_record(envelope, *, rationale_text="Agent notes the diameter change needs user review."):
        audit, preview = audit_and_preview(envelope)
        return record_agent_rationale(
            envelope,
            audit_trail=audit,
            validation_context=preview,
            source={"source_ref": "agent:invented", "source_channel": "test", "source_kind": "agent"},
            actor={"actor_type": "agent", "actor_ref": "agent:worker", "actor_role": "proposal_support"},
            rationale_text=rationale_text,
            assumptions=[{"assumption_id": "asm:rationale", "status": "pending"}],
            audit_references=[{"object_type": "RunNote", "ref": "run:invented"}],
            timestamp="2026-05-06T12:10:00Z",
            accepted_model_state=model_state(),
        )


    def test_rationale_record_is_deterministic_and_preserves_context():
        envelope = operation_envelope(assumptions=[assumption("asm:operation", "unresolved")])
        first = rationale_record(envelope)
        second = rationale_record(deepcopy(envelope))

        assert canonical_json(first) == canonical_json(second)
        assert first["operation_set_ref"] == ref("ModelOperation", "ops:invented")
        assert first["source"]["source_ref"] == "agent:invented"
        assert first["actor"]["actor_type"] == "agent"
        assert first["rationale"]["decision_support_only"] is True
        assert first["rationale"]["creates_accepted_operation_record"] is False
        assert first["rationale"]["mutates_accepted_model_state"] is False
        assert first["rationale"]["bypasses_user_acceptance"] is False
        assert first["affected_entities"] == [ref("Component", "component:pipe-1")]
        assert first["audit_context"]["audit_trail_hash"] != "TBD"
        assert first["validation_context"]["validation"]["diff_preview_status"] == "generated"
        assert first["assumptions"]["unresolved_count"] == 2
        assert {item["assumption_id"] for item in first["assumptions"]["unresolved"]} == {
            "asm:operation",
            "asm:rationale",
        }


    def test_rationale_cannot_mutate_accepted_state_or_bypass_user_acceptance():
        accepted = model_state()
        original = deepcopy(accepted)
        result = record_agent_rationale(
            operation_envelope(),
            rationale_text="Invented proposal note for later user review.",
            accepted_model_state=accepted,
        )

        assert accepted == original
        assert result["accepted_model_state_unchanged"] is True
        assert result["rationale"]["creates_accepted_operation_record"] is False
        assert result["rationale"]["mutates_accepted_model_state"] is False
        assert result["professional_boundary"]["software_can_accept_engineering_work"] is False
        assert result["professional_boundary"]["software_can_mutate_accepted_model_state"] is False
        assert "RATIONALE-AUDIT-CONTEXT-TBD" in {item["code"] for item in result["diagnostics"]}


    def test_missing_context_and_unresolved_assumptions_are_visible():
        result = record_agent_rationale(
            operation_envelope(assumptions=[assumption("asm:missing-context", "TBD")])
        )
        codes = {item["code"] for item in result["diagnostics"]}

        assert {
            "RATIONALE-AUDIT-CONTEXT-TBD",
            "RATIONALE-VALIDATION-CONTEXT-TBD",
            "RATIONALE-SOURCE-TBD",
            "RATIONALE-ACTOR-TBD",
            "RATIONALE-TEXT-TBD",
        } <= codes
        assert result["validation_context"]["status"] == "TBD"
        assert result["audit_context"]["audit_trail_hash"] == "TBD"
        assert result["assumptions"]["unresolved_count"] == 1
        assert result["assumptions"]["unresolved"][0]["status"] == "TBD"


    def test_prohibited_professional_boundary_claims_are_blocked():
        result = rationale_record(
            operation_envelope(),
            rationale_text=(
                "This invented operation is code compliant, certified, sealed, authenticated, "
                "externally validated, has professional approval, and has autonomous engineering acceptance."
            ),
        )

        codes = {item["code"] for item in result["diagnostics"]}
        assert "RATIONALE-AUTHORITY-COMPLIANCE-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-CERTIFICATION-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-SEALING-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-AUTHENTICATION-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-PROFESSIONAL-APPROVAL-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-EXTERNAL-VALIDATION-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-AUTONOMOUS-ACCEPTANCE-BLOCKED" in codes
        assert result["rationale"]["status"] == "blocked_by_professional_boundary"


    def test_prohibited_claims_in_copied_context_are_blocked():
        envelope = operation_envelope()
        audit, preview = audit_and_preview(envelope)
        envelope["operation_set"]["operations"][0]["diagnostics"].append(
            {"message": "Copied operation diagnostic says code compliant."}
        )
        preview["diagnostics"].append({"message": "Copied validation diagnostic says certified."})
        audit["records"][0]["decision"]["rationale"] = "Copied audit context says professional approval."

        result = record_agent_rationale(
            envelope,
            audit_trail=audit,
            validation_context=preview,
            source={"source_ref": "agent:invented", "source_channel": "test", "source_kind": "agent"},
            actor={"actor_type": "agent", "actor_ref": "agent:worker", "actor_role": "proposal_support"},
            rationale_text="Agent notes the proposal needs user review.",
            timestamp="2026-05-06T12:10:00Z",
            accepted_model_state=model_state(),
        )

        codes = {item["code"] for item in result["diagnostics"]}
        assert "RATIONALE-AUTHORITY-COMPLIANCE-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-CERTIFICATION-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-PROFESSIONAL-APPROVAL-BLOCKED" in codes
        assert result["rationale"]["status"] == "blocked_by_professional_boundary"


    def test_enum_style_prohibited_claims_in_copied_context_are_blocked():
        envelope = operation_envelope()
        audit, preview = audit_and_preview(envelope)
        envelope["operation_set"]["operations"][0]["diagnostics"].append(
            {"message": "Copied operation diagnostic says CODE_COMPLIANT."}
        )
        preview["diagnostics"].append({"message": "Copied validation diagnostic says APPROVED."})
        audit["records"][0]["decision"]["rationale"] = (
            "Copied audit context says HUMAN_APPROVED_FOR_PROJECT and engineering acceptance."
        )

        result = record_agent_rationale(
            envelope,
            audit_trail=audit,
            validation_context=preview,
            source={"source_ref": "agent:invented", "source_channel": "test", "source_kind": "agent"},
            actor={"actor_type": "agent", "actor_ref": "agent:worker", "actor_role": "proposal_support"},
            rationale_text="Agent notes the proposal needs user review.",
            timestamp="2026-05-06T12:10:00Z",
            accepted_model_state=model_state(),
        )

        codes = {item["code"] for item in result["diagnostics"]}
        assert "RATIONALE-AUTHORITY-COMPLIANCE-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-PROFESSIONAL-APPROVAL-BLOCKED" in codes
        assert "RATIONALE-AUTHORITY-AUTONOMOUS-ACCEPTANCE-BLOCKED" in codes
        assert result["rationale"]["status"] == "blocked_by_professional_boundary"


    def test_lowercase_approved_coordination_context_is_not_professional_approval():
        envelope = operation_envelope()
        audit, preview = audit_and_preview(envelope)
        preview["diagnostics"].append(
            {"message": "Copied validation context cites approved DAG coordination authority."}
        )

        result = record_agent_rationale(
            envelope,
            audit_trail=audit,
            validation_context=preview,
            source={"source_ref": "agent:invented", "source_channel": "test", "source_kind": "agent"},
            actor={"actor_type": "agent", "actor_ref": "agent:worker", "actor_role": "proposal_support"},
            rationale_text="Agent notes the proposal still needs user review.",
            timestamp="2026-05-06T12:10:00Z",
            accepted_model_state=model_state(),
        )

        assert "RATIONALE-AUTHORITY-PROFESSIONAL-APPROVAL-BLOCKED" not in {
            item["code"] for item in result["diagnostics"]
        }
        assert result["rationale"]["status"] == "captured_for_user_review"


    def test_output_boundary_posture_does_not_make_prohibited_claims():
        result = rationale_record(operation_envelope())
        text = canonical_json(result).lower()

        for forbidden in [
            "code_compliant",
            "code compliant",
            "certified",
            "sealed",
            "authenticated",
            "human_approved_for_project",
            "professional approval",
            "engineering acceptance",
        ]:
            assert forbidden not in text
        assert result["professional_boundary"]["software_makes_approval_claim"] is False


    def main():
        test_rationale_record_is_deterministic_and_preserves_context()
        test_rationale_cannot_mutate_accepted_state_or_bypass_user_acceptance()
        test_missing_context_and_unresolved_assumptions_are_visible()
        test_prohibited_professional_boundary_claims_are_blocked()
        test_prohibited_claims_in_copied_context_are_blocked()
        test_enum_style_prohibited_claims_in_copied_context_are_blocked()
        test_lowercase_approved_coordination_context_is_not_professional_approval()
        test_output_boundary_posture_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_analysis_boundary_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the code-neutral analysis boundary schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "analysis_boundary.schema.yaml"
    FIXTURE_DIR = ROOT / "fixtures" / "analysis_boundary"

    FORBIDDEN_AUTOMATIC = {
        "CODE_COMPLIANT",
        "COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
        "HUMAN_APPROVED_FOR_PROJECT",
    }

    FORBIDDEN_CLAIM_FIELDS = {
        "software_makes_compliance_claim",
        "software_makes_certification_claim",
        "software_makes_sealing_claim",
        "software_makes_professional_acceptance_claim",
    }

    REQUIRED_RULE_PACK_REF_FIELDS = {
        "rule_pack_id",
        "version",
        "checksum",
        "source_notice",
        "supplied_by_user",
        "redistribution_status",
        "provenance",
    }

    REQUIRED_PROVENANCE_FIELDS = {
        "source_name",
        "source_location",
        "source_license",
        "contributor",
        "redistribution_status",
        "review_status",
    }

    REQUIRED_FORBIDDEN_CLAIMS = {
        "code_compliance",
        "certification",
        "sealing",
        "professional_acceptance",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture(name):
        with (FIXTURE_DIR / name).open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        assert "authority_model" in schema["required"]
        authority_model = defs["AuthorityModel"]
        assert authority_model["properties"]["mechanics_authority"]["const"] == (
            "solver_result_only"
        )
        assert authority_model["properties"]["rule_check_authority"]["const"] == (
            "software_computation_using_user_data"
        )
        assert authority_model["properties"]["human_acceptance_authority"]["const"] == (
            "external_hash_bound_human_record_only"
        )
        assert authority_model["properties"]["automatic_status_scope"]["items"][
            "$ref"
        ].endswith("/AutomaticAnalysisStatus")
        forbidden_claim_values = set(
            authority_model["properties"]["forbidden_software_claims"]["items"]["enum"]
        )
        assert REQUIRED_FORBIDDEN_CLAIMS <= forbidden_claim_values

        automatic = enum_at(schema, "AutomaticAnalysisStatus")
        assert automatic.isdisjoint(FORBIDDEN_AUTOMATIC)
        for status in automatic:
            assert not any(forbidden == status for forbidden in FORBIDDEN_AUTOMATIC)

        mechanics_statuses = set(defs["MechanicsSolveBoundary"]["properties"]["status"]["enum"])
        assert mechanics_statuses == {"MODEL_INCOMPLETE", "MECHANICS_SOLVED"}

        rule_statuses = set(defs["UserRuleCheckBoundary"]["properties"]["status"]["enum"])
        assert rule_statuses == {
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
        }
        assert rule_statuses.isdisjoint(FORBIDDEN_AUTOMATIC)

        professional_boundary = defs["ProfessionalBoundary"]["properties"]
        for field in FORBIDDEN_CLAIM_FIELDS:
            assert professional_boundary[field]["const"] is False
        assert professional_boundary["human_review_required"]["const"] is True

        user_rule_check = defs["UserRuleCheckBoundary"]
        assert "rule_pack_ref" in user_rule_check["required"]
        assert user_rule_check["properties"]["rule_pack_ref"]["$ref"].endswith("/RulePackRef")

        rule_pack_ref = defs["RulePackRef"]
        assert REQUIRED_RULE_PACK_REF_FIELDS <= required_at(schema, "RulePackRef")
        assert rule_pack_ref["properties"]["supplied_by_user"]["const"] is True
        assert rule_pack_ref["properties"]["provenance"]["$ref"].endswith("/Provenance")

        assert REQUIRED_PROVENANCE_FIELDS <= required_at(schema, "Provenance")

        human_ref = defs["HumanAcceptanceRef"]
        assert human_ref["properties"]["human_status"]["const"] == "HUMAN_APPROVED_FOR_PROJECT"
        assert "bound_evidence_hashes" in human_ref["required"]
        assert "human_acceptance_refs" in schema["required"]

        missing_input = defs["MissingInputFinding"]
        assert "diagnostic_ref" in missing_input["required"]
        assert set(missing_input["properties"]["status"]["enum"]) == {
            "MODEL_INCOMPLETE",
            "RULE_INPUTS_INCOMPLETE",
            "TBD",
        }


    def check_analysis_boundary_fixtures():
        schema = load_schema()
        fixtures = [
            load_fixture("invented_mechanics_solved_rule_inputs_incomplete.json"),
            load_fixture("invented_user_rule_checked.json"),
            load_fixture("invented_user_rule_failed_with_human_ref.json"),
        ]

        statuses = {item["user_rule_check"]["status"] for item in fixtures}
        assert statuses == {
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
        }
        for fixture in fixtures:
            assert set(schema["required"]) <= set(fixture)
            assert fixture["mechanics_solve"]["status"] == "MECHANICS_SOLVED"
            assert fixture["mechanics_solve"]["authority"] == "solver_result_only"
            assert fixture["user_rule_check"]["authority"] == "software_computation_using_user_data"
            assert fixture["professional_boundary"]["human_review_required"] is True
            assert not fixture["professional_boundary"]["software_makes_compliance_claim"]
            assert not fixture["professional_boundary"]["software_makes_certification_claim"]
            assert not fixture["professional_boundary"]["software_makes_sealing_claim"]
            assert not fixture["professional_boundary"][
                "software_makes_professional_acceptance_claim"
            ]

        human_refs = fixtures[2]["human_acceptance_refs"]
        assert human_refs
        assert human_refs[0]["human_status"] == "HUMAN_APPROVED_FOR_PROJECT"
        assert human_refs[0]["scope_notice"] == "external_human_record_not_software_status"
        assert set(fixtures[2]["authority_model"]["automatic_status_scope"]).isdisjoint(
            FORBIDDEN_AUTOMATIC
        )


    def test_analysis_boundary_schema_contract():
        check_schema_contract()


    def test_analysis_boundary_fixtures_preserve_code_neutral_authority_split():
        check_analysis_boundary_fixtures()


    def main():
        check_schema_contract()
        check_analysis_boundary_fixtures()


    if __name__ == "__main__":
        main()

## Component: tests/test_analysis_run_comparison.py

    #!/usr/bin/env python3
    """Focused tests for DEL-14-04 analysis-run comparison."""

    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.comparison.analysis_run.engine import compare_analysis_runs, comparison_dict


    FORBIDDEN_CLAIMS = {
        "certification",
        "certified",
        "sealing",
        "sealed",
        "authentication",
        "code " + "compliant",
        "professional " + "approval",
        "engineering " + "acceptance",
    }


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def run_record(run_id, model_state_id, result_ref):
        return {
            "run_id": run_id,
            "run_name": f"{run_id} invented fixture",
            "run_kind": "mechanics_solve",
            "created_at": "2026-05-05T00:00:00Z",
            "model_state_ref": ref("ModelState", model_state_id),
            "solver_version": {
                "solver_id": "invented-solver",
                "version": "0.0.0-fixture",
                "build_hash": "invented",
            },
            "settings_ref": ref("SolverSettings", f"settings:{run_id}"),
            "unit_system_ref": ref("UnitSystem", "fixture-units"),
            "load_basis_refs": [ref("LoadCase", "LC-1")],
            "diagnostics": [],
            "result_refs": [ref("ResultEnvelope", result_ref)],
            "rule_pack_refs": [ref("RulePack", "RP-fixture")],
            "library_refs": [ref("Library", "LIB-fixture")],
            "hashes": [
                {
                    "algorithm": "sha256",
                    "canonicalization": "JCS",
                    "payload_ref": ref("AnalysisRun", run_id),
                    "payload_scope": "analysis_run_record",
                    "value": f"hash-{run_id}",
                }
            ],
            "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
            "reproducibility": {
                "input_manifest_refs": [ref("Manifest", f"manifest:{run_id}")],
                "environment_refs": [ref("Environment", "fixture")],
                "determinism_notes": ["invented deterministic fixture"],
                "unresolved_tbd": [],
            },
        }


    def quantity_result(result_id, family, object_id, magnitude, unit, dimension):
        return {
            "result_id": result_id,
            "family": family,
            "object_ref": ref("PipeElement", object_id),
            "basis_ref": ref("LoadCase", "LC-1"),
            "magnitude": magnitude,
            "unit": unit,
            "dimension": dimension,
            "provenance": {"source_name": "invented fixture"},
        }


    def result_envelope(envelope_id, run_id, quantities):
        return {
            "result_envelope": {
                "envelope_id": envelope_id,
                "run_ref": ref("AnalysisRun", run_id),
                "result_sets": [
                    {
                        "result_set_id": f"set:{envelope_id}",
                        "quantity_results": quantities,
                    }
                ],
                "diagnostics": [],
            }
        }


    def mapping(mapping_id, left_result_id, right_result_id, **extra):
        base = {
            "mapping_id": mapping_id,
            "mapping_status": "manual_match",
            "left_ref": ref("Result", left_result_id),
            "right_ref": ref("Result", right_result_id),
        }
        base.update(extra)
        return base


    def tolerance_profile(value=0.25):
        return {
            "tolerance_profile": {
                "profile_id": "TP-invented-review",
                "rules": [
                    {
                        "rule_id": "TR-stress-review",
                        "result_family": "stress",
                        "dimension_id": "stress",
                        "unit_ref": ref("Unit", "Pa"),
                        "tolerance_value": value,
                        "tolerance_value_status": "project_specific_review_required",
                        "normalization_basis": "unit_conversion_required",
                    }
                ],
            }
        }


    def fixture_inputs():
        left_run = {"analysis_run": run_record("RUN-left", "MS-left", "RES-left")}
        right_run = {"analysis_run": run_record("RUN-right", "MS-right", "RES-right")}
        left_results = result_envelope(
            "RES-left",
            "RUN-left",
            [quantity_result("left:stress:E1", "stress", "E1", 1000.0, "kPa", "stress")],
        )
        right_results = result_envelope(
            "RES-right",
            "RUN-right",
            [quantity_result("right:stress:E1", "stress", "E1", 1000500.0, "Pa", "stress")],
        )
        return {
            "left_run": left_run,
            "right_run": right_run,
            "left_results": left_results,
            "right_results": right_results,
            "mappings": [
                mapping(
                    "MAP-stress-E1",
                    "left:stress:E1",
                    "right:stress:E1",
                    normalized_unit="Pa",
                )
            ],
            "tolerance_profile": tolerance_profile(),
            "unit_conversions": {("kPa", "Pa", "stress"): 1000.0},
            "left_settings": {"solver": "linear", "iterations": 1, "audit_mode": "draft"},
            "right_settings": {"solver": "linear", "iterations": 2, "new_flag": True},
            "comparison_id": "CMP-fixture",
        }


    def test_comparison_is_deterministic_and_preserves_context():
        inputs = fixture_inputs()

        first = comparison_dict(compare_analysis_runs(**inputs))
        second = comparison_dict(compare_analysis_runs(**deepcopy(inputs)))

        assert first == second
        assert first["comparison_id"] == "CMP-fixture"
        assert first["run_context"]["left"]["run_id"] == "RUN-left"
        assert first["run_context"]["right"]["run_id"] == "RUN-right"
        assert first["run_context"]["left"]["model_state_ref"] == ref("ModelState", "MS-left")
        assert first["run_context"]["right"]["model_state_ref"] == ref("ModelState", "MS-right")
        assert first["run_context"]["left"]["hashes"][0]["value"] == "hash-RUN-left"
        assert first["run_context"]["right"]["solver_version"]["solver_id"] == "invented-solver"


    def test_unit_normalized_delta_and_classification_keep_raw_evidence_separate():
        output = comparison_dict(compare_analysis_runs(**fixture_inputs()))

        assert output["diagnostics"] == []
        assert len(output["result_deltas"]) == 1
        delta = output["result_deltas"][0]
        assert delta["mapping_id"] == "MAP-stress-E1"
        assert delta["left_magnitude"] == 1000.0
        assert delta["right_magnitude"] == 1000500.0
        assert delta["raw_delta"] == 999500.0
        assert delta["left_normalized_magnitude"] == 1000000.0
        assert delta["right_normalized_magnitude"] == 1000500.0
        assert delta["normalized_delta"] == 500.0
        assert delta["absolute_normalized_delta"] == 500.0
        assert delta["classification"] == "exceeds_tolerance_profile"
        assert delta["classification_basis"] == "caller_supplied_tolerance_rule"
        assert delta["tolerance_profile_ref"] == "TP-invented-review"
        assert delta["tolerance_rule_id"] == "TR-stress-review"
        assert {item["setting_key"] for item in output["settings_deltas"]} == {
            "audit_mode",
            "iterations",
            "new_flag",
        }


    def test_incompatible_or_missing_unit_metadata_produces_diagnostics_not_deltas():
        inputs = fixture_inputs()
        inputs["right_results"]["result_envelope"]["result_sets"][0]["quantity_results"][0][
            "dimension"
        ] = "force"

        dimension_output = comparison_dict(compare_analysis_runs(**inputs))

        assert dimension_output["result_deltas"] == []
        assert {item["code"] for item in dimension_output["diagnostics"]} == {
            "ARC-DIMENSION-INCOMPATIBLE"
        }

        inputs = fixture_inputs()
        inputs["unit_conversions"] = {}

        conversion_output = comparison_dict(compare_analysis_runs(**inputs))

        assert conversion_output["result_deltas"] == []
        assert {item["code"] for item in conversion_output["diagnostics"]} == {
            "ARC-UNIT-CONVERSION-UNSUPPORTED"
        }


    def test_missing_mapping_and_result_data_are_explicit_findings():
        inputs = fixture_inputs()
        inputs["mappings"] = [
            mapping(
                "MAP-unresolved",
                "left:stress:E1",
                "right:stress:E1",
                mapping_status="unresolved_mapping",
            ),
            mapping("MAP-missing-result", "left:stress:E1", "right:missing"),
        ]

        output = comparison_dict(compare_analysis_runs(**inputs))

        assert output["result_deltas"] == []
        assert {item["code"] for item in output["diagnostics"]} == {
            "ARC-MAPPING-NOT-COMPARABLE",
            "ARC-RESULT-DATA-MISSING",
        }
        assert output["has_blocking_findings"]


    def test_carried_run_diagnostics_are_preserved_as_review_evidence():
        inputs = fixture_inputs()
        inputs["left_run"]["analysis_run"]["diagnostics"] = [
            {
                "severity": "blocking",
                "message": "Invented left run diagnostic remains review evidence.",
                "remediation": "Resolve the left run diagnostic before relying on comparison output.",
            }
        ]
        inputs["right_run"]["analysis_run"]["diagnostics"] = [
            {
                "severity": "warning",
                "message": "Invented right run diagnostic remains review evidence.",
                "remediation": "Review the right run diagnostic before relying on comparison output.",
            }
        ]

        output = comparison_dict(compare_analysis_runs(**inputs))
        run_diagnostics = [
            item for item in output["diagnostics"] if item["class"] == "RUN_DIAGNOSTIC"
        ]

        assert output["has_blocking_findings"] is True
        assert {item["code"] for item in run_diagnostics} == {
            "ARC-RUN-DIAGNOSTIC-LEFT",
            "ARC-RUN-DIAGNOSTIC-RIGHT",
        }
        assert {item["severity"] for item in run_diagnostics} == {"blocking", "warning"}
        assert {
            tuple((ref["object_type"], ref["ref"]) for ref in item["affected_refs"])
            for item in run_diagnostics
        } == {
            (("AnalysisRun", "RUN-left"),),
            (("AnalysisRun", "RUN-right"),),
        }
        assert {
            item["message"] for item in run_diagnostics
        } == {
            "Invented left run diagnostic remains review evidence.",
            "Invented right run diagnostic remains review evidence.",
        }


    def test_output_does_not_emit_prohibited_professional_claims():
        output = comparison_dict(compare_analysis_runs(**fixture_inputs()))

        boundary = output["professional_boundary"]
        assert boundary["human_review_required"] is True
        assert boundary["software_makes_compliance_claim"] is False
        assert boundary["software_makes_certification_claim"] is False
        assert boundary["software_makes_sealing_claim"] is False
        assert boundary["software_makes_approval_claim"] is False
        assert boundary["software_makes_authentication_claim"] is False

        claim_surface = {
            "diagnostics": output["diagnostics"],
            "result_classifications": [
                {
                    "classification": item["classification"],
                    "classification_basis": item["classification_basis"],
                }
                for item in output["result_deltas"]
            ],
        }
        text = str(claim_surface).lower()
        for claim in FORBIDDEN_CLAIMS:
            assert claim not in text


    if __name__ == "__main__":
        test_comparison_is_deterministic_and_preserves_context()
        test_unit_normalized_delta_and_classification_keep_raw_evidence_separate()
        test_incompatible_or_missing_unit_metadata_produces_diagnostics_not_deltas()
        test_missing_mapping_and_result_data_are_explicit_findings()
        test_carried_run_diagnostics_are_preserved_as_review_evidence()
        test_output_does_not_emit_prohibited_professional_claims()

## Component: tests/test_analysis_run_records.py

    #!/usr/bin/env python3
    """Focused tests for DEL-14-02 analysis-run record generation."""

    import json
    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )

    from core.analysis_runs.records import (
        PHYSICAL_PROJECT_CONTAINER,
        build_preview_analysis_run_envelope,
        canonical_json,
        validate_analysis_run_envelope,
    )
    from core.project_persistence import (  # noqa: E402
        build_project_persistence_envelope,
        round_trip_project_envelope,
        validate_project_persistence_envelope,
    )


    PREVIEW_RESULT_PATH = ROOT / "fixtures" / "product_preview" / "invented_mechanics_result.json"
    ANALYSIS_RUN_SCHEMA_PATH = ROOT / "schemas" / "analysis_run.schema.json"


    def preview_result():
        return json.loads(PREVIEW_RESULT_PATH.read_text(encoding="utf-8"))


    def analysis_run_schema():
        return json.loads(ANALYSIS_RUN_SCHEMA_PATH.read_text(encoding="utf-8"))


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_preview_result_builds_deterministic_immutable_run_record():
        first = build_preview_analysis_run_envelope(preview_result())
        second = build_preview_analysis_run_envelope(preview_result())

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-14-02"
        run = first["analysis_run"]
        assert run["run_id"] == "run:preview-linear-static-001"
        assert run["immutability_policy"]["run_record_is_read_only"] is True
        assert run["immutability_policy"]["new_run_required_for_change"] is True
        assert "HUMAN_REVIEW_REQUIRED" in run["analysis_status"]
        assert "MECHANICS_SOLVED" in run["analysis_status"]
        assert "RULE_INPUTS_INCOMPLETE" in run["analysis_status"]
        assert validate_analysis_run_envelope(first) == []


    def test_generated_analysis_run_envelope_validates_against_schema():
        envelope = build_preview_analysis_run_envelope(preview_result())
        schema = analysis_run_schema()

        try:
            assert validate_schema_document(schema, schema_label=str(ANALYSIS_RUN_SCHEMA_PATH))
            assert validate_instance(
                schema,
                envelope,
                schema_label=str(ANALYSIS_RUN_SCHEMA_PATH),
                instance_label="generated DEL-14-02 analysis run envelope",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def test_generated_run_binds_run_basis_diagnostics_and_boundary_fields():
        state_ref = {"object_type": "ModelState", "ref": "state:accepted-invented-preview"}
        settings_ref = {"object_type": "SolverSettings", "ref": "settings:linear-static-review"}
        unit_ref = {"object_type": "UnitSystem", "ref": "unit-system:invented-si"}
        load_refs = [
            {"object_type": "LoadCase", "ref": "load:L-100"},
            {"object_type": "LoadCombination", "ref": "combination:C-OPER-ALT"},
        ]
        build_ref = {"object_type": "ExternalReference", "ref": "build:del-14-02-evidence"}

        envelope = build_preview_analysis_run_envelope(
            preview_result(),
            model_state_ref=state_ref,
            settings_ref=settings_ref,
            unit_system_ref=unit_ref,
            load_basis_refs=load_refs,
            solver_name="open_pipe_stress_preview_solver",
            solver_version="0.1.0-test",
            build_ref=build_ref,
        )
        run = envelope["analysis_run"]

        assert run["model_state_ref"] == state_ref
        assert run["settings_ref"] == settings_ref
        assert run["unit_system_ref"] == unit_ref
        assert run["load_basis_refs"] == load_refs
        assert run["solver_version"]["solver_name"] == "open_pipe_stress_preview_solver"
        assert run["solver_version"]["solver_version"] == "0.1.0-test"
        assert run["solver_version"]["build_ref"] == build_ref
        assert run["diagnostics"]
        assert all(item["code"] and item["provenance"] for item in run["diagnostics"])
        assert run["result_refs"]
        assert all(item["hash_refs"] for item in run["result_refs"])
        assert {item["payload_scope"] for item in run["hashes"]} >= {
            "analysis_run_record",
            "result_envelope",
        }
        assert run["professional_boundary"] == {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def test_run_contract_status_uses_sca_003_local_project_store():
        envelope = build_preview_analysis_run_envelope(preview_result())
        contract = envelope["run_contract_status"]
        physical = contract["physical_project_container"]

        assert contract["record_contract"] == "schema_first_analysis_run_records"
        assert physical == PHYSICAL_PROJECT_CONTAINER
        assert physical["profile"] == "sqlite_local_project_store"
        assert physical["decision_ref"] == "SCA-003"
        assert physical["storage_role"] == "local_store_index_projection"
        assert physical["canonical_truth"] == "canonical_json_jcs_payload"
        assert physical["sql_public_contract"] is False
        assert physical["direct_sql_access_allowed"] is False
        assert physical["hosted_db_allowed"] is False
        assert physical["network_required"] is False
        assert physical["sidecars_rebuildable"] is True


    def test_analysis_run_schema_binds_physical_container_to_sca_003_profile():
        schema = json.loads(ANALYSIS_RUN_SCHEMA_PATH.read_text(encoding="utf-8"))
        defs = schema["$defs"]
        contract = defs["RunContractStatus"]["properties"]
        physical = defs["PhysicalProjectContainer"]["properties"]

        assert (
            contract["physical_project_container"]["$ref"]
            == "#/$defs/PhysicalProjectContainer"
        )
        assert physical["profile"]["const"] == "sqlite_local_project_store"
        assert physical["decision_ref"]["const"] == "SCA-003"
        assert physical["canonical_truth"]["const"] == "canonical_json_jcs_payload"
        assert physical["sql_public_contract"]["const"] is False
        assert physical["direct_sql_access_allowed"]["const"] is False


    def test_result_refs_bind_computed_result_ids_to_hashes():
        envelope = build_preview_analysis_run_envelope(preview_result())
        run = envelope["analysis_run"]
        refs = {item["result_ref"]["ref"]: item for item in run["result_refs"]}

        assert "result:force:pipe-P-120:axial" in refs
        assert "result:force:pipe-P-120:axial:end-j" in refs
        assert "result:force:pipe-P-120:midspan:axial" in refs
        assert "result:force:pipe-P-120:quarter-1:shear-y" in refs
        assert "result:force:pipe-P-120:shear-y" in refs
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial" in refs
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y" in refs
        assert "result:stress:pipe-P-120:end-j:torsional-shear" in refs
        assert "result:stress:pipe-P-120:quarter-1:torsional-shear" in refs
        axial = refs["result:force:pipe-P-120:axial"]
        axial_end_j = refs["result:force:pipe-P-120:axial:end-j"]
        axial_midspan = refs["result:force:pipe-P-120:midspan:axial"]
        shear_quarter = refs["result:force:pipe-P-120:quarter-1:shear-y"]
        combination_axial = refs["result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial"]
        combination_shear_quarter = refs[
            "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y"
        ]
        torsional_stress_end_j = refs["result:stress:pipe-P-120:end-j:torsional-shear"]
        torsional_stress_quarter = refs["result:stress:pipe-P-120:quarter-1:torsional-shear"]
        assert axial["result_ref"]["object_type"] == "Result"
        assert axial["result_family"] == "force"
        assert axial_end_j["result_family"] == "force"
        assert axial_midspan["result_family"] == "force"
        assert shear_quarter["result_family"] == "force"
        assert combination_axial["result_family"] == "force"
        assert combination_shear_quarter["result_family"] == "force"
        assert torsional_stress_end_j["result_family"] == "stress"
        assert torsional_stress_quarter["result_family"] == "stress"
        assert axial["privacy_classification"] == "invented_public_example"
        assert axial_end_j["privacy_classification"] == "invented_public_example"
        assert axial_midspan["privacy_classification"] == "invented_public_example"
        assert shear_quarter["privacy_classification"] == "invented_public_example"
        assert combination_axial["privacy_classification"] == "invented_public_example"
        assert combination_shear_quarter["privacy_classification"] == "invented_public_example"
        assert torsional_stress_end_j["privacy_classification"] == "invented_public_example"
        assert torsional_stress_quarter["privacy_classification"] == "invented_public_example"
        assert axial["hash_refs"][0]["payload_scope"] == "result_value"
        assert axial_end_j["hash_refs"][0]["payload_scope"] == "result_value"
        assert shear_quarter["hash_refs"][0]["payload_scope"] == "result_value"
        assert combination_axial["hash_refs"][0]["payload_scope"] == "result_value"
        assert combination_shear_quarter["hash_refs"][0]["payload_scope"] == "result_value"
        assert torsional_stress_end_j["hash_refs"][0]["payload_scope"] == "result_value"
        assert torsional_stress_quarter["hash_refs"][0]["payload_scope"] == "result_value"
        assert axial["hash_refs"][0]["payload_ref"] == {
            "object_type": "Result",
            "ref": "result:force:pipe-P-120:axial",
        }
        assert axial_end_j["hash_refs"][0]["payload_ref"] == {
            "object_type": "Result",
            "ref": "result:force:pipe-P-120:axial:end-j",
        }
        assert combination_axial["hash_refs"][0]["payload_ref"] == {
            "object_type": "Result",
            "ref": "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial",
        }
        assert torsional_stress_end_j["hash_refs"][0]["payload_ref"] == {
            "object_type": "Result",
            "ref": "result:stress:pipe-P-120:end-j:torsional-shear",
        }
        assert any(item["payload_scope"] == "result_envelope" for item in run["hashes"])
        assert any(item["payload_scope"] == "analysis_run_record" for item in run["hashes"])


    def test_result_mutation_changes_corresponding_result_hash():
        base = preview_result()
        changed = deepcopy(base)
        for item in changed["results"]:
            if item["id"] == "result:force:pipe-P-120:axial":
                item["value"] = item["value"] + 1.0

        base_run = build_preview_analysis_run_envelope(base)["analysis_run"]
        changed_run = build_preview_analysis_run_envelope(changed)["analysis_run"]

        def result_hash(run):
            for item in run["result_refs"]:
                if item["result_ref"]["ref"] == "result:force:pipe-P-120:axial":
                    return item["hash_refs"][0]["value"]
            raise AssertionError("axial force ref missing")

        assert result_hash(base_run) != result_hash(changed_run)


    def test_persistence_history_preserves_analysis_run_basis_after_model_change():
        analysis_run = build_preview_analysis_run_envelope(
            preview_result(),
            model_state_ref={"object_type": "ModelState", "ref": "state:original-accepted"},
            settings_ref={"object_type": "SolverSettings", "ref": "settings:original-solve"},
            unit_system_ref={"object_type": "UnitSystem", "ref": "unit-system:original-si"},
            load_basis_refs=[{"object_type": "LoadCase", "ref": "load:L-100"}],
        )
        result_envelope_ref = analysis_run["analysis_run"]["reproducibility"]["input_manifest_refs"][0]

        def persisted_project(model_revision):
            return build_project_persistence_envelope(
                project_id="project:del-14-02-run-history",
                project_name="DEL-14-02 invented run-history check",
                model_payload={
                    "model_id": "model:invented-preview",
                    "revision": model_revision,
                },
                model_state_refs=[{"ref_kind": "model_state", "ref": "state:original-accepted"}],
                analysis_run_records=[analysis_run],
                result_envelope_refs=[
                    {"ref_kind": "result_envelope", "ref": result_envelope_ref["ref"]}
                ],
            )

        original = persisted_project("original")
        changed_model = persisted_project("later-unrelated-model-edit")
        round_trip = round_trip_project_envelope(original)

        original_history = original["project"]["run_history"]
        changed_history = changed_model["project"]["run_history"]
        restored_history = round_trip["envelope"]["project"]["run_history"]

        assert validate_project_persistence_envelope(original) == []
        assert round_trip["semantic_equal"] is True
        assert round_trip["diagnostics"] == []
        assert original["hash"]["project_payload_hash"]["value"] != changed_model["hash"][
            "project_payload_hash"
        ]["value"]
        assert original_history["analysis_run_records"] == changed_history["analysis_run_records"]
        assert original_history["hash_manifest"] == changed_history["hash_manifest"]
        assert restored_history["analysis_run_records"] == original_history[
            "analysis_run_records"
        ]
        persisted_run = restored_history["analysis_run_records"][0]["analysis_run"]
        assert persisted_run["model_state_ref"] == {
            "object_type": "ModelState",
            "ref": "state:original-accepted",
        }
        assert persisted_run["settings_ref"]["ref"] == "settings:original-solve"
        assert persisted_run["unit_system_ref"]["ref"] == "unit-system:original-si"
        assert persisted_run["load_basis_refs"] == [
            {"object_type": "LoadCase", "ref": "load:L-100"}
        ]
        assert any(
            item["payload_scope"] == "analysis_run_record"
            and item["payload_ref"]["ref"] == persisted_run["run_id"]
            for item in restored_history["hash_manifest"]
        )


    def test_validation_blocks_missing_review_boundary_and_result_hashes():
        envelope = build_preview_analysis_run_envelope(preview_result())
        run = envelope["analysis_run"]
        run["analysis_status"] = ["MECHANICS_SOLVED"]
        run["professional_boundary"]["software_makes_compliance_claim"] = True
        run["result_refs"][0]["hash_refs"] = []

        diagnostics = validate_analysis_run_envelope(envelope)
        codes = {item["code"] for item in diagnostics}

        assert "ANALYSIS_RUN_HUMAN_REVIEW_REQUIRED_MISSING" in codes
        assert "ANALYSIS_RUN_PROFESSIONAL_BOUNDARY_VIOLATION" in codes
        assert "ANALYSIS_RUN_RESULT_HASH_MISSING" in codes

## Component: tests/test_analysis_run_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the analysis run schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "analysis_run.schema.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "run_contract_status",
        "analysis_run",
    }

    REQUIRED_DEFS = {
        "AnalysisRunRecord",
        "AnalysisStatus",
        "Checksum",
        "Diagnostic",
        "Id",
        "ImmutabilityPolicy",
        "LibraryRef",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "Reproducibility",
        "ResultRef",
        "ReviewStatus",
        "RulePackRef",
        "RunContractStatus",
        "SolverVersion",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "formal prover approval status",
        "code compliant",
        "certified by software",
        "sealed by software",
        "professional approval by the software",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-14-02"
        assert schema["properties"]["package_id"]["const"] == "PKG-14"
        assert schema["properties"]["scope_item"]["const"] == "SOW-072"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-016"

        contract = defs["RunContractStatus"]["properties"]
        assert contract["record_contract"]["const"] == "schema_first_analysis_run_records"
        assert contract["model_state_binding"]["const"] == "schemas/model_state.schema.json"
        assert contract["result_binding"]["const"] == "schemas/results.schema.yaml"
        assert (
            contract["physical_project_container"]["$ref"]
            == "#/$defs/PhysicalProjectContainer"
        )
        physical = defs["PhysicalProjectContainer"]["properties"]
        assert physical["profile"]["const"] == "sqlite_local_project_store"
        assert physical["decision_ref"]["const"] == "SCA-003"
        assert physical["storage_role"]["const"] == "local_store_index_projection"
        assert physical["canonical_truth"]["const"] == "canonical_json_jcs_payload"
        assert physical["sql_public_contract"]["const"] is False
        assert physical["direct_sql_access_allowed"]["const"] is False
        assert physical["hosted_db_allowed"]["const"] is False
        assert physical["network_required"]["const"] is False
        assert physical["sidecars_rebuildable"]["const"] is True
        assert contract["external_validation_boundary"]["const"] == (
            "reference_only_not_determined_by_software"
        )

        run_required = required_at(schema, "AnalysisRunRecord")
        assert {
            "run_id",
            "run_name",
            "run_kind",
            "created_at",
            "model_state_ref",
            "solver_version",
            "settings_ref",
            "unit_system_ref",
            "load_basis_refs",
            "diagnostics",
            "result_refs",
            "rule_pack_refs",
            "library_refs",
            "hashes",
            "analysis_status",
            "reproducibility",
            "immutability_policy",
            "professional_boundary",
            "provenance",
        } <= run_required
        assert {
            "mechanics_solve",
            "rule_check",
            "combined_analysis",
            "export_generation",
            "comparison_input",
        } <= set(defs["AnalysisRunRecord"]["properties"]["run_kind"]["enum"])

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)
        assert (
            defs["AnalysisRunRecord"]["properties"]["analysis_status"]["contains"]["const"]
            == "HUMAN_REVIEW_REQUIRED"
        )

        checksum_required = required_at(schema, "Checksum")
        assert {
            "algorithm",
            "canonicalization",
            "payload_ref",
            "payload_scope",
            "value",
        } <= checksum_required
        assert {"JCS", "NONE", "TBD"} <= set(
            defs["Checksum"]["properties"]["canonicalization"]["enum"]
        )
        assert {
            "analysis_run_record",
            "model_state_record",
            "solver_settings",
            "load_basis",
            "result_envelope",
            "result_value",
            "audit_manifest",
        } <= set(defs["Checksum"]["properties"]["payload_scope"]["enum"])

        immutability = defs["ImmutabilityPolicy"]["properties"]
        assert immutability["run_record_is_read_only"]["const"] is True
        assert immutability["mutation_policy"]["const"] == (
            "changes_create_new_analysis_run"
        )
        assert immutability["new_run_required_for_change"]["const"] is True
        assert immutability["hash_invalidates_external_acceptance"]["const"] is True

        assert {
            "input_manifest_refs",
            "environment_refs",
            "determinism_notes",
            "unresolved_tbd",
        } <= required_at(schema, "Reproducibility")
        assert "Result" in set(defs["Reference"]["properties"]["object_type"]["enum"])
        assert {
            "result_ref",
            "result_family",
            "hash_refs",
            "privacy_classification",
            "provenance",
        } <= required_at(schema, "ResultRef")
        assert {
            "rule_pack_id",
            "version",
            "checksum",
            "source_notice",
            "redistribution_status",
            "private_payload_redacted",
            "provenance",
        } <= required_at(schema, "RulePackRef")
        assert defs["RulePackRef"]["properties"]["private_payload_redacted"]["const"] is True

        professional = defs["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings


    if __name__ == "__main__":
        main()

## Component: tests/test_analysis_status_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the analysis status schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "analysis_status.schema.yaml"
    ANALYSIS_BOUNDARY_SCHEMA_PATH = ROOT / "schemas" / "analysis_boundary.schema.yaml"
    RESULTS_SCHEMA_PATH = ROOT / "schemas" / "results.schema.yaml"
    API_BOUNDARY_CONTRACT_PATH = ROOT / "api" / "api_boundary_contract.yaml"

    REQUIRED_VOCABULARY = {
        "MODEL_INCOMPLETE",
        "MECHANICS_SOLVED",
        "RULE_INPUTS_INCOMPLETE",
        "USER_RULE_CHECKED",
        "USER_RULE_FAILED",
        "HUMAN_REVIEW_REQUIRED",
        "HUMAN_APPROVED_FOR_PROJECT",
    }

    REQUIRED_AUTOMATIC = REQUIRED_VOCABULARY - {"HUMAN_APPROVED_FOR_PROJECT"}

    FORBIDDEN_AUTOMATIC = {
        "USER_RULE_PASSED",
        "CODE_COMPLIANT",
        "CODE_COMPLIANCE",
        "COMPLIANT",
        "CERTIFIED",
        "CERTIFICATION",
        "SEALED",
        "SEALING",
        "APPROVED",
        "APPROVAL",
        "HUMAN_APPROVED_FOR_PROJECT",
        "PROFESSIONAL_ACCEPTANCE",
        "PROFESSIONAL_RELIANCE",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_json(path):
        with path.open(encoding="utf-8") as json_file:
            return json.load(json_file)


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def assert_no_forbidden_automatic_status_claims(statuses):
        assert "USER_RULE_PASSED" not in statuses
        assert "HUMAN_APPROVED_FOR_PROJECT" not in statuses
        for status in statuses:
            assert not any(forbidden in status for forbidden in FORBIDDEN_AUTOMATIC)


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        vocabulary = enum_at(schema, "AnalysisStatusVocabulary")
        assert REQUIRED_VOCABULARY <= vocabulary
        assert "USER_RULE_PASSED" not in vocabulary

        automatic = enum_at(schema, "AutomaticAnalysisStatus")
        assert REQUIRED_AUTOMATIC <= automatic
        assert_no_forbidden_automatic_status_claims(automatic)

        software_status = defs["SoftwareStatusRecord"]
        assert software_status["properties"]["primary_status"]["$ref"].endswith(
            "/AutomaticAnalysisStatus"
        )
        assert software_status["properties"]["status_set"]["items"]["$ref"].endswith(
            "/AutomaticAnalysisStatus"
        )
        assert software_status["properties"]["rule_check_details"]["items"]["$ref"].endswith(
            "/UserRuleCheckDetails"
        )
        user_rule_checked_condition = next(
            condition
            for condition in software_status["allOf"]
            if condition["if"]["properties"].get("primary_status", {}).get("const")
            == "USER_RULE_CHECKED"
        )
        assert "rule_check_details" in user_rule_checked_condition["then"]["required"]
        assert user_rule_checked_condition["then"]["properties"]["rule_check_details"][
            "minItems"
        ] == 1
        user_rule_checked_set_condition = next(
            condition
            for condition in software_status["allOf"]
            if condition["if"]["properties"].get("status_set", {}).get("contains", {}).get(
                "const"
            )
            == "USER_RULE_CHECKED"
        )
        assert (
            user_rule_checked_set_condition["if"]["properties"]["status_set"]["contains"][
                "const"
            ]
            == "USER_RULE_CHECKED"
        )
        assert "rule_check_details" in user_rule_checked_set_condition["then"]["required"]
        assert user_rule_checked_set_condition["then"]["properties"]["rule_check_details"][
            "minItems"
        ] == 1

        rule_check_details = defs["UserRuleCheckDetails"]
        assert {
            "rule_pack_ref",
            "evaluation_outcome",
            "checked_at",
            "evidence_refs",
        } <= set(rule_check_details["required"])
        detail_outcomes = set(rule_check_details["properties"]["evaluation_outcome"]["enum"])
        assert "checked_no_failures_reported" in detail_outcomes
        assert "USER_RULE_PASSED" not in detail_outcomes
        assert "accepted_for_project" not in detail_outcomes

        root_properties = schema["properties"]
        assert "human_acceptance_records" in root_properties
        human_record_ref = root_properties["human_acceptance_records"]["items"]["$ref"]
        assert human_record_ref.endswith("/HumanAcceptanceRecord")

        human_record = defs["HumanAcceptanceRecord"]
        assert "acceptance_outcome" in human_record["required"]
        assert "acceptance_status" not in human_record["required"]
        assert human_record["properties"]["acceptance_status"]["const"] == (
            "HUMAN_APPROVED_FOR_PROJECT"
        )
        assert "bound_hashes" in human_record["required"]
        assert "software_status" not in human_record["properties"]
        human_actor_constraints = human_record["properties"]["human_actor"]["allOf"]
        assert human_actor_constraints[0]["$ref"].endswith("/Actor")
        assert human_actor_constraints[1]["properties"]["actor_type"]["const"] == "human"
        accepted_branch = human_record["allOf"][0]
        assert "acceptance_status" in accepted_branch["then"]["required"]
        assert accepted_branch["else"]["not"]["required"] == ["acceptance_status"]

        professional_boundary = defs["ProfessionalBoundary"]["properties"]
        assert professional_boundary["software_makes_compliance_claim"]["const"] is False
        assert professional_boundary["software_makes_certification_claim"]["const"] is False
        assert professional_boundary["software_makes_sealing_claim"]["const"] is False
        assert professional_boundary["software_makes_approval_claim"]["const"] is False
        assert professional_boundary["software_makes_authentication_claim"]["const"] is False
        assert (
            professional_boundary["software_makes_professional_acceptance_claim"]["const"]
            is False
        )


    def check_downstream_automatic_status_surfaces():
        analysis_boundary = load_json(ANALYSIS_BOUNDARY_SCHEMA_PATH)
        results_schema = load_json(RESULTS_SCHEMA_PATH)
        api_contract = load_json(API_BOUNDARY_CONTRACT_PATH)

        downstream_status_enums = {
            "analysis_boundary.AutomaticAnalysisStatus": enum_at(
                analysis_boundary, "AutomaticAnalysisStatus"
            ),
            "analysis_boundary.UserRuleCheckBoundary.status": set(
                analysis_boundary["$defs"]["UserRuleCheckBoundary"]["properties"]["status"][
                    "enum"
                ]
            ),
            "results.AnalysisStatus": enum_at(results_schema, "AnalysisStatus"),
            "api.result_envelope.analysis_status": set(
                api_contract["$defs"]["result_envelope"]["properties"]["analysis_status"][
                    "items"
                ]["enum"]
            ),
        }

        for statuses in downstream_status_enums.values():
            assert_no_forbidden_automatic_status_claims(statuses)


    def test_analysis_status_schema_contract():
        check_schema_contract()


    def test_downstream_automatic_status_surfaces_exclude_human_approval_and_passed_claims():
        check_downstream_automatic_status_surfaces()


    def main():
        check_schema_contract()
        check_downstream_automatic_status_surfaces()


    if __name__ == "__main__":
        main()

## Component: tests/test_analytical_solver_boundary_adapter.py

    #!/usr/bin/env python3
    """Focused tests for the internal analytical solver-boundary adapter."""

    import json
    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.model_transform.physical_to_analytical._solver_boundary_adapter import (  # noqa: E402
        adapt_analytical_solver_model,
    )
    from core.model_transform.physical_to_analytical.contract import (  # noqa: E402
        transform_physical_to_analytical,
    )


    PHYSICAL_SOURCE_FIXTURE = (
        ROOT / "fixtures" / "domain" / "invented_physical_source_of_truth_model.json"
    )


    def load_json(path):
        return json.loads(path.read_text(encoding="utf-8"))


    def canonical_physical_model():
        return load_json(PHYSICAL_SOURCE_FIXTURE)["model"]


    def analytical_solver_model():
        result = transform_physical_to_analytical(canonical_physical_model())
        assert not result.has_blocking_findings
        return result.analytical_model


    def ref(object_type, item_id):
        return {"object_type": object_type, "id": item_id}


    def codes(items):
        return {item["code"] for item in items}


    def test_adapter_emits_deterministic_solver_boundary_dtos():
        source = analytical_solver_model()

        first = adapt_analytical_solver_model(source).to_dict()
        second = adapt_analytical_solver_model(deepcopy(source)).to_dict()

        assert first == second
        assert first["model_ref"] == ref("Model", "ANALYTICAL-DERIVED")
        assert first["source_model_ref"] == ref("Model", "PHYS-1")
        assert first["diagnostics"] == []
        assert not first["has_blocking_findings"]

        assert [node["node_id"] for node in first["nodes"]] == ["N-1", "N-2"]
        assert first["nodes"][0]["node_index"] == 0
        assert first["nodes"][0]["coordinates"] == [0.0, 0.0, 0.0]
        assert first["nodes"][0]["coordinate_units"]["x"] == {
            "unit": "m",
            "dimension": "length",
        }
        assert first["nodes"][1]["node_index"] == 1
        assert first["nodes"][1]["coordinates"] == [2.0, 0.0, 0.0]

        assert first["straight_pipe_connectivity"] == [
            {
                "element_id": "E-1",
                "element_index": 0,
                "node_i_id": "N-1",
                "node_i_index": 0,
                "node_j_id": "N-2",
                "node_j_index": 1,
                "material_id": "MAT-1",
                "section_id": "SEC-1",
                "local_coordinate_system": source["elements"][0]["local_coordinate_system"],
                "derived_axis_x": [1.0, 0.0, 0.0],
                "y_reference": [0.0, 1.0, 0.0],
                "solver_orientation_status": "governed_y_reference_ready",
                "source_ref": ref("Element", "E-1"),
            }
        ]

        binding = first["property_bindings"][0]
        assert binding["binding_id"] == "BIND-STRAIGHT-PIPE-E-1"
        assert binding["element_id"] == "E-1"
        assert binding["material_properties"]["elastic_modulus"]["dimension"] == "stress"
        assert binding["material_properties"]["shear_modulus"]["unit"] == "Pa"
        assert binding["section_properties"]["area"]["dimension"] == "area"
        assert (
            binding["section_properties"]["second_moment_y"]["dimension"]
            == "second_moment_area"
        )
        assert (
            binding["section_properties"]["second_moment_z"]["dimension"]
            == "second_moment_area"
        )
        assert (
            binding["section_properties"]["torsion_constant"]["dimension"]
            == "second_moment_area"
        )
        assert binding["section_properties"]["mass_per_length"]["dimension"] == "mass_per_length"

        assert first["support_targets"] == [
            {
                "support_id": "SUP-1",
                "support_type": "anchor",
                "target_type": "Node",
                "target_id": "N-1",
                "target_index": 0,
                "directions": ["UX", "UY", "UZ", "RX", "RY", "RZ"],
                "properties": source["supports"][0]["properties"],
                "source_ref": ref("Support", "SUP-1"),
            }
        ]

        assert first["load_case_records"] == [
            {
                "load_case_id": "LC-1",
                "load_case_index": 0,
                "name": "Invented load case",
                "load_type": "weight",
                "load_count": 3,
                "solver_application_status": "solver_ready",
                "source_ref": ref("LoadCase", "LC-1"),
            }
        ]
        assert first["load_case_diagnostics"] == []
        assert [
            (item["load_record_type"], item["target_type"], item["target_id"], item["direction"])
            for item in first["load_applications"]
        ] == [
            ("element_uniform_distributed_force", "Element", "E-1", "Y"),
            ("element_point_force", "Element", "E-1", "Y"),
            ("nodal_moment", "Node", "N-2", "RZ"),
        ]
        assert first["load_applications"][0]["quantity"]["dimension"] == "force_per_length"
        assert first["load_applications"][0]["span"]["start_fraction"]["dimension"] == "dimensionless"
        assert first["load_applications"][0]["span"]["end_fraction"]["value"] == 1.0
        assert first["load_applications"][1]["station_fraction"]["value"] == 0.5
        assert first["load_applications"][2]["quantity"]["dimension"] == "moment"
        assert [item["dto_id"] for item in first["adapter_dto_records"]] == [
            "dto:load_application:LC-1:0",
            "dto:load_application:LC-1:1",
            "dto:load_application:LC-1:2",
        ]
        first_dto = first["adapter_dto_records"][0]
        assert first_dto["dto_kind"] == "load_application"
        assert first_dto["source_ref"] == ref("LoadCase", "LC-1:load:0")
        assert first_dto["result_trace_anchor"] == {
            "ref_type": "adapter_dto",
            "ref_id": "dto:load_application:LC-1:0",
        }
        assert first_dto["solver_input_trace_anchor"] == {
            "ref_type": "solver_input",
            "ref_id": "solver_input:load_application:LC-1:0",
        }
        assert first_dto["source_chain"] == [
            {
                "trace_id": "trace:analytical-load-to-adapter-dto:LC-1:0",
                "trace_type": "analytical_model_to_adapter_dto",
                "source_ref": ref("LoadCase", "LC-1:load:0"),
                "target_ref": {
                    "ref_type": "adapter_dto",
                    "ref_id": "dto:load_application:LC-1:0",
                },
                "provenance": first_dto["provenance"],
            },
            {
                "trace_id": "trace:adapter-dto-to-solver-input:LC-1:0",
                "trace_type": "adapter_dto_to_solver_input",
                "source_ref": {
                    "ref_type": "adapter_dto",
                    "ref_id": "dto:load_application:LC-1:0",
                },
                "target_ref": {
                    "ref_type": "solver_input",
                    "ref_id": "solver_input:load_application:LC-1:0",
                },
                "provenance": first_dto["provenance"],
            },
        ]
        assert first_dto["payload_hash_ref"]["algorithm"] == "sha256"
        assert first_dto["payload_hash_ref"]["canonicalization"] == "JCS"
        assert first_dto["payload_hash_ref"]["payload_ref"] == ref(
            "AdapterDTO", "dto:load_application:LC-1:0"
        )
        assert len(first_dto["payload_hash_ref"]["value"]) == 64


    def test_adapter_does_not_infer_missing_solver_property_bindings():
        source = analytical_solver_model()
        del source["materials"][0]["properties"]["shear_modulus"]

        result = adapt_analytical_solver_model(source).to_dict()

        assert result["straight_pipe_connectivity"][0]["element_id"] == "E-1"
        assert result["property_bindings"] == []
        assert "ASBA-MATERIAL-PROPERTY-MISSING" in codes(result["diagnostics"])


    def test_adapter_diagnoses_noncanonical_load_semantics_without_mapping_them():
        source = analytical_solver_model()
        source["load_cases"][0]["loads"][0]["load_kind"] = "point_force"

        result = adapt_analytical_solver_model(source).to_dict()

        assert "ASBA-LOAD-NONCANONICAL-SEMANTICS-UNSUPPORTED" in codes(
            result["load_case_diagnostics"]
        )
        assert "ASBA-LOAD-SEMANTICS-AMBIGUOUS" not in codes(result["load_case_diagnostics"])
        assert result["load_case_records"][0]["solver_application_status"] == "blocked_by_diagnostics"
        assert [item["load_index"] for item in result["load_applications"]] == [1, 2]
        assert "user_loads" not in result


    def test_adapter_blocks_invalid_straight_pipe_y_reference_orientation():
        source = analytical_solver_model()
        source["elements"][0]["local_coordinate_system"]["y_reference"] = [1.0, 0.0, 0.0]

        parallel = adapt_analytical_solver_model(source).to_dict()

        assert parallel["straight_pipe_connectivity"] == []
        assert "ASBA-ELEMENT-Y-REFERENCE-PARALLEL" in codes(parallel["diagnostics"])

        source = analytical_solver_model()
        source["elements"][0]["local_coordinate_system"]["y_reference"] = [0.0, 0.0, 0.0]

        zero = adapt_analytical_solver_model(source).to_dict()

        assert zero["straight_pipe_connectivity"] == []
        assert "ASBA-ELEMENT-Y-REFERENCE-ZERO" in codes(zero["diagnostics"])

        source = analytical_solver_model()
        source["elements"][0]["local_coordinate_system"]["y_reference"] = [0.0, float("nan"), 0.0]

        nonfinite = adapt_analytical_solver_model(source).to_dict()

        assert nonfinite["straight_pipe_connectivity"] == []
        assert "ASBA-ELEMENT-Y-REFERENCE-NONFINITE" in codes(nonfinite["diagnostics"])


    def test_adapter_blocks_unordered_uniform_load_span_at_runtime():
        source = analytical_solver_model()
        span = source["load_cases"][0]["loads"][0]["span"]
        span["start_fraction"]["value"] = 0.75
        span["end_fraction"]["value"] = 0.25

        result = adapt_analytical_solver_model(source).to_dict()

        assert "ASBA-LOAD-SPAN-FRACTION-ORDER" in codes(result["load_case_diagnostics"])
        assert result["load_case_records"][0]["solver_application_status"] == "blocked_by_diagnostics"
        assert [item["load_index"] for item in result["load_applications"]] == [1, 2]


    def test_adapter_preserves_load_record_failures_as_result_boundary_diagnostics():
        source = analytical_solver_model()
        unsupported_mapping = {
            "load_record_type": "element_thermal_gradient",
            "target_ref": ref("Element", "E-1"),
            "direction": "Y",
            "quantity": deepcopy(source["load_cases"][0]["loads"][1]["quantity"]),
            "provenance": deepcopy(source["load_cases"][0]["loads"][1]["provenance"]),
        }
        unresolved_target = deepcopy(source["load_cases"][0]["loads"][1])
        unresolved_target["target_ref"] = ref("Element", "E-MISSING")
        wrong_dimension = deepcopy(source["load_cases"][0]["loads"][0])
        wrong_dimension["quantity"]["dimension"] = "force"
        nonfinite_value = deepcopy(source["load_cases"][0]["loads"][2])
        nonfinite_value["quantity"]["value"] = float("inf")
        source["load_cases"][0]["loads"] = [
            "unsupported-load-record",
            unsupported_mapping,
            unresolved_target,
            wrong_dimension,
            nonfinite_value,
        ]

        result = adapt_analytical_solver_model(source).to_dict()

        assert result["load_applications"] == []
        assert result["adapter_dto_records"] == []
        assert result["load_case_records"] == [
            {
                "load_case_id": "LC-1",
                "load_case_index": 0,
                "name": "Invented load case",
                "load_type": "weight",
                "load_count": 5,
                "solver_application_status": "blocked_by_diagnostics",
                "source_ref": ref("LoadCase", "LC-1"),
            }
        ]
        assert {
            "ASBA-LOAD-RECORD-UNSUPPORTED",
            "ASBA-LOAD-RECORD-TYPE-UNSUPPORTED",
            "ASBA-LOAD-TARGET-UNRESOLVED",
            "ASBA-LOAD-QUANTITY-DIMENSION-UNSUPPORTED",
            "ASBA-LOAD-QUANTITY-NONFINITE",
        } <= codes(result["load_case_diagnostics"])
        assert result["diagnostics"] == []
        assert result["has_blocking_findings"]
        assert "user_loads" not in result


    def test_adapter_requires_analytical_solver_model_role():
        source = analytical_solver_model()
        source["model_role"] = "physical_source_of_truth"

        result = adapt_analytical_solver_model(source).to_dict()

        assert result["nodes"] == []
        assert result["straight_pipe_connectivity"] == []
        assert result["property_bindings"] == []
        assert result["support_targets"] == []
        assert result["load_case_records"] == []
        assert result["load_applications"] == []
        assert result["load_case_diagnostics"] == []
        assert codes(result["diagnostics"]) == {"ASBA-SOURCE-ROLE-UNEXPECTED"}


    if __name__ == "__main__":
        test_adapter_emits_deterministic_solver_boundary_dtos()
        test_adapter_does_not_infer_missing_solver_property_bindings()
        test_adapter_diagnoses_noncanonical_load_semantics_without_mapping_them()
        test_adapter_blocks_invalid_straight_pipe_y_reference_orientation()
        test_adapter_blocks_unordered_uniform_load_span_at_runtime()
        test_adapter_preserves_load_record_failures_as_result_boundary_diagnostics()
        test_adapter_requires_analytical_solver_model_role()

## Component: tests/test_api_boundary_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the public API boundary contract."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    CONTRACT_PATH = ROOT / "api" / "api_boundary_contract.yaml"
    PLUGIN_BOUNDARY_PATH = ROOT / "docs" / "architecture" / "plugin_boundary.md"

    REQUIRED_METADATA = {
        "deliverable_id": "DEL-10-01",
        "package_id": "PKG-10",
        "scope_item": "SOW-030",
        "objective": "OBJ-009",
        "decomposition_revision": "0.7",
        "scope_change_authority": "SCA-004",
        "public_transport_protocol": "TBD",
        "endpoint_syntax": "TBD",
        "openapi_transport_binding": "TBD",
        "external_format_list": "TBD",
        "export_profile_contract": "TBD",
        "stable_id_map_contract": "TBD",
        "loss_report_contract": "TBD",
        "external_run_evidence_contract": "TBD",
        "stress_neutral_export_contract": "TBD",
        "conservative_pcf_export_contract": "TBD",
        "review_geometry_export_contract": "TBD",
        "adapter_sdk_contract": "TBD",
        "plugin_runtime": "TBD",
        "plugin_loading_signing_isolation": "TBD",
        "permission_grant_persistence": "TBD",
        "api_stability_level": "TBD",
        "code_generation_tooling": "TBD",
        "schema_basis": "JSON Schema 2020-12",
    }

    REQUIRED_PERSISTENCE_BOUNDARY_PHRASES = {
        "application-service commands, queries, or jobs",
        "must not expose SQL",
        "raw SQLite handles",
        "table names",
        "direct store mutation",
    }

    REQUIRED_OPERATION_CATEGORIES = {
        "command",
        "query",
        "job",
        "result_envelope",
        "plugin_manifest",
        "diagnostic",
        "provenance",
        "permission",
        "privacy",
        "checksum",
        "export_profile",
        "stable_id_map",
        "loss_report",
        "external_run_evidence",
        "adapter_sdk",
        "validation_test",
        "no_bypass",
    }

    REQUIRED_BOUNDARY_AREAS = {
        "model_import",
        "model_export",
        "solver_invocation",
        "results",
        "rule_pack_hooks",
        "plugin_manifest",
        "permissions",
        "diagnostics",
        "provenance",
        "privacy",
        "checksums",
        "export_profile",
        "stable_id_map",
        "loss_report",
        "external_run_evidence",
        "stress_neutral_export",
        "conservative_pcf_export",
        "review_geometry_export",
        "adapter_sdk",
        "validation_test",
        "no_bypass",
    }

    REQUIRED_COMMANDS = {
        "ops.model.import",
        "ops.model.export",
        "ops.solve.start",
        "ops.rule_pack.attach",
        "ops.export.profile",
        "ops.export.id_map",
        "ops.export.loss_report",
        "ops.external_run.record",
        "ops.adapter_sdk.register",
    }

    REQUIRED_QUERIES = {
        "ops.model.describe",
        "ops.results.get",
        "ops.diagnostics.list",
        "ops.plugin.permissions.describe",
        "ops.export.profile.describe",
        "ops.export.id_map.describe",
        "ops.export.loss_report.describe",
        "ops.adapter_sdk.capabilities.describe",
    }

    REQUIRED_JOBS = {
        "ops.solve.job",
        "ops.export.job",
        "ops.report.job",
        "ops.validation.job",
        "ops.export.stress_neutral.job",
        "ops.export.pcf.job",
        "ops.export.review_geometry.job",
    }

    REQUIRED_EXPORT_COMMON_CONCEPTS = {
        "export_profile",
        "stable_id_map",
        "loss_report",
        "external_run_evidence",
        "adapter_sdk",
    }

    REQUIRED_EXPORT_TARGETS = {
        "stress_neutral_export",
        "conservative_pcf_export",
        "review_geometry_export",
        "adapter_sdk",
    }

    REQUIRED_DEFERRED_EXPORT_DECISIONS = {
        "public_transport_protocol",
        "endpoint_syntax",
        "plugin_runtime",
        "plugin_loading_signing_isolation",
        "permission_grant_persistence",
        "code_generation_tooling",
        "concrete_writer_behavior",
        "external_tool_invocation",
    }

    REQUIRED_PLUGIN_ENTRYPOINTS = {
        "export_profile_provider",
        "stable_id_map_provider",
        "loss_report_provider",
        "external_run_evidence_provider",
        "stress_neutral_export",
        "conservative_pcf_export",
        "review_geometry_export",
        "adapter_sdk_provider",
    }

    REQUIRED_PERMISSION_TOKENS = {
        "read_export_profile",
        "write_export_profile",
        "read_stable_id_map",
        "write_stable_id_map",
        "read_loss_report",
        "write_loss_report",
        "record_external_run_evidence",
        "use_adapter_sdk",
        "export_stress_neutral",
        "export_conservative_pcf",
        "export_review_geometry",
    }

    REQUIRED_CHECKSUM_KINDS = {
        "export_profile",
        "stable_id_map",
        "loss_report",
        "external_run_evidence",
        "review_geometry_asset",
        "adapter_sdk_manifest",
    }

    REQUIRED_NO_BYPASS = {
        "must_use_domain_validation",
        "must_use_unit_validation",
        "must_preserve_provenance",
        "must_preserve_privacy_classification",
        "must_return_result_envelope",
        "must_preserve_diagnostics",
        "must_preserve_persistence_hash_controls",
        "must_route_persistence_through_application_services",
        "must_not_expose_sql_or_raw_sqlite",
        "must_not_expose_table_names",
        "must_not_mutate_project_store_directly",
        "must_preserve_report_controls",
        "must_preserve_human_acceptance_boundary",
        "must_not_execute_arbitrary_rule_code",
        "must_not_skip_rule_pack_sandbox",
        "must_not_claim_code_compliance",
        "must_not_bundle_protected_content",
        "must_not_transmit_private_data_by_default",
        "must_not_write_private_library_without_permission",
        "must_preserve_export_profile_registry",
        "must_preserve_stable_id_maps",
        "must_emit_loss_report_for_target_limitations",
        "must_classify_unsupported_approximated_omitted_or_delegated_behavior",
        "must_record_external_run_evidence_as_non_authoritative",
        "must_not_claim_external_solver_validation",
        "must_not_treat_review_geometry_as_solver_geometry",
        "must_not_rely_on_hidden_translator_defaults",
        "must_preserve_stress_neutral_status_boundary",
        "must_preserve_adapter_sdk_no_bypass_controls",
    }

    FORBIDDEN_STATUS_TERMS = {
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED_FOR_PROFESSIONAL_RELIANCE",
    }


    def load_contract():
        with CONTRACT_PATH.open(encoding="utf-8") as contract_file:
            return json.load(contract_file)


    def ids(items):
        return {item["id"] for item in items}


    def main():
        contract = load_contract()
        defs = contract["$defs"]

        assert contract["type"] == "object"
        assert contract["additionalProperties"] is False

        metadata = contract["x_contract_metadata"]
        for key, expected in REQUIRED_METADATA.items():
            assert metadata[key] == expected
        for phrase in REQUIRED_PERSISTENCE_BOUNDARY_PHRASES:
            assert phrase in metadata["persistence_boundary"]
        assert "SCA-004 export concepts" in metadata["export_interoperability_authority"]
        for deferred_key in [
            "public_transport_protocol",
            "endpoint_syntax",
            "plugin_runtime",
            "permission_grant_persistence",
            "code_generation_tooling",
        ]:
            assert metadata[deferred_key] == "TBD"

        categories = set(contract["properties"]["operation_category"]["enum"])
        assert REQUIRED_OPERATION_CATEGORIES <= categories

        boundary_areas = set(
            contract["properties"]["operation"]["properties"]["boundary_area"]["enum"]
        )
        assert REQUIRED_BOUNDARY_AREAS <= boundary_areas
        assert contract["properties"]["operation"]["properties"]["transport"]["const"] == "TBD"

        registry = contract["x_operation_registry"]
        assert REQUIRED_COMMANDS <= ids(registry["commands"])
        assert REQUIRED_QUERIES <= ids(registry["queries"])
        assert REQUIRED_JOBS <= ids(registry["jobs"])

        export_registry = contract["x_export_interoperability_registry"]
        assert export_registry["authority"] == "SCA-004"
        assert export_registry["status"] == "boundary_concepts_only"
        assert REQUIRED_EXPORT_COMMON_CONCEPTS <= set(export_registry["common_concepts"])
        assert REQUIRED_EXPORT_TARGETS <= ids(export_registry["target_families"])
        assert REQUIRED_DEFERRED_EXPORT_DECISIONS <= set(
            export_registry["deferred_decisions"]
        )
        assert "endpoint syntax" in export_registry["scope_boundary"]
        assert "plugin runtime" in export_registry["scope_boundary"]
        assert "permission persistence" in export_registry["scope_boundary"]

        request = defs["request_envelope"]
        assert {"privacy", "provenance", "permissions", "checksums"} <= set(
            request["required"]
        )

        result = defs["result_envelope"]
        assert {"diagnostics", "provenance", "privacy", "checksums", "limitations"} <= set(
            result["required"]
        )
        analysis_status = set(
            result["properties"]["analysis_status"]["items"]["enum"]
        )
        assert "HUMAN_REVIEW_REQUIRED" in analysis_status
        assert "HUMAN_APPROVED_FOR_PROJECT" not in analysis_status
        assert "CODE_COMPLIANT" not in analysis_status

        human_acceptance = defs["human_acceptance_record_ref"]
        assert human_acceptance["properties"]["software_generated"]["const"] is False

        plugin_manifest = defs["plugin_manifest"]
        entrypoints = set(
            plugin_manifest["properties"]["entrypoints"]["items"]["enum"]
        )
        assert REQUIRED_PLUGIN_ENTRYPOINTS <= entrypoints

        privacy_context = defs["privacy_context"]
        assert privacy_context["properties"]["telemetry_allowed"]["const"] is False
        assert "protected_suspected" in privacy_context["properties"]["classification"]["enum"]

        permissions = defs["permission_request"]
        assert permissions["properties"]["denied_by_default"]["const"] is True
        assert permissions["properties"]["grant_state"]["enum"][0] == "TBD"
        permission_tokens = set(permissions["properties"]["requested"]["items"]["enum"])
        assert REQUIRED_PERMISSION_TOKENS <= permission_tokens

        checksum_set = defs["checksum_set"]
        assert "JCS-compatible-json" in checksum_set["properties"]["canonicalization"]["enum"]
        checksum_kinds = set(defs["checksum"]["properties"]["kind"]["enum"])
        assert REQUIRED_CHECKSUM_KINDS <= checksum_kinds

        no_bypass = set(defs["no_bypass_constraints"]["items"]["enum"])
        assert REQUIRED_NO_BYPASS <= no_bypass

        contract_text = CONTRACT_PATH.read_text(encoding="utf-8")
        boundary_text = PLUGIN_BOUNDARY_PATH.read_text(encoding="utf-8")
        combined_upper = f"{contract_text}\n{boundary_text}".upper()
        for term in FORBIDDEN_STATUS_TERMS:
            assert term not in combined_upper

        for phrase in [
            "Public transport protocol",
            "OpenAPI transport binding",
            "plugin runtime",
            "Validation-test execution",
            "human-acceptance boundary controls",
            "application-service commands, queries, or jobs",
            "raw SQLite",
            "table names",
            "direct project-store mutation hooks",
            "SCA-004 export interoperability surfaces",
            "Export profiles",
            "Stable ID maps",
            "Loss reports",
            "External-run evidence",
            "Stress-neutral CSV/JSON exports",
            "Conservative PCF export",
            "GLB/glTF review geometry",
            "Export adapter SDK surfaces",
            "concept-level boundary tokens",
        ]:
            assert phrase in boundary_text


    if __name__ == "__main__":
        main()

## Component: tests/test_caepipe_external_run_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-05 CAEPIPE external-run evidence packages."""

    from __future__ import annotations

    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.caepipe_external import (  # noqa: E402
        build_caepipe_external_run_package,
        build_skipped_caepipe_external_run_package,
        canonical_json,
        parse_caepipe_csv_text,
        write_caepipe_external_run_package,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "caepipe_external_run.schema.json"
    CSV_FIXTURE_PATH = ROOT / "fixtures" / "caepipe_external" / "invented" / "caepipe_results.csv"
    SKIPPED_FIXTURE_PATH = ROOT / "fixtures" / "caepipe_external" / "invented" / "skipped_run_package.json"
    PARSED_FIXTURE_PATH = ROOT / "fixtures" / "caepipe_external" / "invented" / "parser_only_run_package.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def stable_id_map() -> list[dict[str, object]]:
        return [
            {
                "canonical_ref": ref("Node", "node:invented:A"),
                "target_ref": ref("CaePipeMbfRecord", "N001"),
            },
            {
                "canonical_ref": ref("Node", "node:invented:B"),
                "target_ref": ref("CaePipeMbfRecord", "N002"),
            },
            {
                "canonical_ref": ref("PipeElement", "pipe:invented:001"),
                "target_ref": ref("CaePipeMbfRecord", "P001"),
            },
        ]


    def mbf_package_ref() -> dict[str, str]:
        return ref("CaePipeMbfExportPackage", "caepipe-mbf:invented-del-17-04")


    def parsed_csv() -> dict[str, object]:
        return parse_caepipe_csv_text(
            CSV_FIXTURE_PATH.read_text(encoding="ascii"),
            source_csv_ref=ref("CsvArtifact", "csv:invented-caepipe-results"),
            stable_id_map=stable_id_map(),
        )


    def skipped_package() -> dict[str, object]:
        return build_skipped_caepipe_external_run_package(
            run_id="caepipe-run:invented-skipped",
            mbf_package_ref=mbf_package_ref(),
        )


    def parser_only_package() -> dict[str, object]:
        return build_caepipe_external_run_package(
            run_id="caepipe-run:invented-parser-only",
            package_status="parser_only_evidence",
            mbf_package_ref=mbf_package_ref(),
            executable_config={
                "configuration_surface": "TBD-17-05-PH-001",
                "configured_path_state": "absent",
                "license_responsibility_acknowledged": False,
                "environment_responsibility_acknowledged": False,
                "path_record": "not_configured",
            },
            command_profile={
                "profile_id": "TBD-17-05-invocation-profile",
                "invocation_mode": "parser_only_not_invoked",
                "command_shape": "not_invoked_public_fixture_only",
                "profile_basis": "TBD-17-05-PH-001",
            },
            run_directory={
                "run_directory_ref": "fixture:caepipe-external-parser-only",
                "working_directory": "fixtures/caepipe_external/invented",
                "input_mbf_path": "fixtures/caepipe_mbf/invented/caepipe_mbf_export_package.json",
                "expected_csv_path": "fixtures/caepipe_external/invented/caepipe_results.csv",
                "observed_csv_path": "fixtures/caepipe_external/invented/caepipe_results.csv",
                "output_discovery_status": "fixture_observed",
            },
            execution_result={
                "attempted": False,
                "exit_status": None,
                "stdout_capture": "not_available",
                "stderr_capture": "not_available",
                "skip_reason": "Parser-only public fixture; external CAEPIPE execution was not attempted.",
            },
            parsed_csv=parsed_csv(),
        )


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        skipped = load_json(SKIPPED_FIXTURE_PATH)
        parser_only = load_json(PARSED_FIXTURE_PATH)
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            for label, instance in (
                ("skipped fixture", skipped),
                ("parser-only fixture", parser_only),
                ("skipped builder output", skipped_package()),
                ("parser-only builder output", parser_only_package()),
            ):
                assert validate_instance(
                    schema,
                    instance,
                    schema_label=str(SCHEMA_PATH),
                    instance_label=label,
                )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_skipped_without_executable_is_nonblocking_and_deterministic():
        first = skipped_package()
        second = skipped_package()

        assert canonical_json(first) == canonical_json(second)
        assert first["package_status"] == "skipped_no_executable"
        assert first["execution_result"]["attempted"] is False
        assert first["executable_config"]["configured_path_state"] == "absent"
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["checksums"])
        assert first["professional_boundary"]["software_bundles_caepipe"] is False
        assert first["professional_boundary"]["software_invokes_caepipe_without_user_configuration"] is False


    def test_parser_only_package_binds_rows_to_sidecar_stable_ids():
        package = parser_only_package()

        assert package["package_status"] == "parser_only_evidence"
        assert package["parsed_csv"]["row_count"] == 3
        assert {row["correlation_status"] for row in package["parsed_csv"]["rows"]} == {"canonical_id_map"}
        assert {row["section"] for row in package["parsed_csv"]["rows"]} == {
            "ELEMENT_FORCES",
            "NODE_DISPLACEMENTS",
        }
        assert not [item for item in package["diagnostics"] if item["severity"] == "blocking"]
        assert package["professional_boundary"]["software_makes_caepipe_compatibility_claim"] is False
        assert package["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def test_parser_records_unknown_sections_and_unmapped_rows_as_warnings():
        text = (
            CSV_FIXTURE_PATH.read_text(encoding="ascii")
            + "UNKNOWN_SECTION,node:invented:missing,X999,L001,0,0,0,,,,m\n"
        )
        parsed = parse_caepipe_csv_text(
            text,
            source_csv_ref=ref("CsvArtifact", "csv:invented-unknown-row"),
            stable_id_map=stable_id_map(),
        )

        codes = {item["code"] for item in parsed["diagnostics"]}
        assert {"CAEPIPE-CSV-UNKNOWN-SECTION", "CAEPIPE-CSV-UNMAPPED-ROW"} <= codes
        assert parsed["parser_status"] == "parsed_with_diagnostics"
        assert any(row["correlation_status"] == "weak_or_unmapped" for row in parsed["rows"])


    def test_privacy_and_authority_boundary_diagnostics_are_blocking():
        package = build_caepipe_external_run_package(
            run_id="caepipe-run:privacy-boundary",
            package_status="parser_only_evidence",
            mbf_package_ref=mbf_package_ref(),
            executable_config={
                "configured_path_state": "absent",
                "path_record": "not_configured",
            },
            command_profile={
                "command_shape": "not_invoked",
                "free_metadata": {"unsafe_label": "cert" + "ified target run"},
            },
            run_directory={
                "run_directory_ref": "fixture:privacy",
                "working_directory": "fixtures",
                "input_mbf_path": "model.mbf",
                "expected_csv_path": "results.csv",
                "observed_csv_path": "results.csv",
                "output_discovery_status": "fixture_observed",
            },
            execution_result={"attempted": False},
            parsed_csv=parsed_csv(),
            privacy={"protected_payload_embedded": True},
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"CAEPIPE-RUN-PRIVACY-BOUNDARY-VIOLATION", "CAEPIPE-RUN-AUTHORITY-TERM"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])


    def test_attempted_external_run_requires_del_17_04_binding_and_user_acknowledgement():
        package = build_caepipe_external_run_package(
            run_id="caepipe-run:unsafe-attempt",
            package_status="external_run_evidence_recorded",
            mbf_package_ref=ref("NativeJsonExportPackage", "native-json:invented-del-17-03"),
            executable_config={
                "configured_path_state": "present",
                "path_record": "/user/configured/caepipe",
                "license_responsibility_acknowledged": False,
                "environment_responsibility_acknowledged": False,
            },
            command_profile={
                "profile_id": "TBD-17-05-invocation-profile",
                "invocation_mode": "user_configured_external_process",
                "command_shape": "user_owned_executable_path_plus_user_workdir",
                "profile_basis": "TBD-17-05-PH-001",
            },
            run_directory={
                "run_directory_ref": "fixture:unsafe-attempt",
                "working_directory": "user-owned",
                "input_mbf_path": "model.mbf",
                "expected_csv_path": "results.csv",
                "observed_csv_path": "results.csv",
                "output_discovery_status": "observed",
            },
            execution_result={"attempted": True, "exit_status": 0},
            parsed_csv=parsed_csv(),
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {
            "CAEPIPE-RUN-MBF-REF-UNSAFE",
            "CAEPIPE-RUN-LICENSE-RESPONSIBILITY-MISSING",
            "CAEPIPE-RUN-ENVIRONMENT-RESPONSIBILITY-MISSING",
        } <= codes


    def test_writer_outputs_run_metadata_and_sidecars(tmp_path):
        package = parser_only_package()

        write_caepipe_external_run_package(tmp_path, package)

        metadata = load_json(tmp_path / "run_metadata.json")
        assert metadata["run_id"] == package["run_id"]
        assert "parsed_csv" not in metadata
        assert load_json(tmp_path / "parsed_csv.json") == package["parsed_csv"]
        assert load_json(tmp_path / "diagnostics.json") == package["diagnostics"]
        assert load_json(tmp_path / "checksums.json") == package["checksums"]


    def test_fixtures_contain_no_private_or_protected_payload_text():
        text = "\n".join(
            walk_strings(
                {
                    "skipped": load_json(SKIPPED_FIXTURE_PATH),
                    "parser_only": load_json(PARSED_FIXTURE_PATH),
                    "csv": CSV_FIXTURE_PATH.read_text(encoding="ascii"),
                }
            )
        ).lower()
        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text


    def main():
        check_jsonschema_validation()
        test_skipped_without_executable_is_nonblocking_and_deterministic()
        test_parser_only_package_binds_rows_to_sidecar_stable_ids()
        test_parser_records_unknown_sections_and_unmapped_rows_as_warnings()
        test_privacy_and_authority_boundary_diagnostics_are_blocking()
        test_attempted_external_run_requires_del_17_04_binding_and_user_acknowledgement()
        test_fixtures_contain_no_private_or_protected_payload_text()


    if __name__ == "__main__":
        main()

## Component: tests/test_caepipe_mbf_export_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-04 CAEPIPE MBF export packages."""

    from __future__ import annotations

    from copy import deepcopy
    import hashlib
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.caepipe_mbf import (  # noqa: E402
        build_caepipe_mbf_export_package,
        canonical_json,
        canonical_text,
        render_caepipe_mbf_text,
        write_caepipe_mbf_export_package,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "caepipe_mbf_export.schema.json"
    FIXTURE_PATH = ROOT / "fixtures" / "caepipe_mbf" / "invented" / "caepipe_mbf_export_package.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")
    EXPECTED_LOSS_CATEGORIES = {
        "exported",
        "omitted",
        "approximated",
        "delegated",
        "unsupported",
        "tbd",
    }
    EXPECTED_SOURCE_BASIS_REFS = {
        ("Deliverable", "DEL-17-01"),
        ("Deliverable", "DEL-17-02"),
        ("SourceID", "CAEPIPE-IMPORT-MBF"),
        ("SourceID", "CAEPIPE-EXPORT-MBF"),
    }

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
    }


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def source_payload() -> dict[str, object]:
        return {
            "export_id": "caepipe-mbf:invented-del-17-04",
            "source_model_ref": {"object_type": "Model", "ref": "model:invented-caepipe-mbf"},
            "source_model_hash": {
                "algorithm": "sha256",
                "canonicalization": "JCS_compatible_json_payload_hash",
                "payload_ref": {"object_type": "Model", "ref": "model:invented-caepipe-mbf"},
                "payload_scope": "source_model_hash",
                "value": "sha256:" + "1" * 64,
            },
            "model_payload": {
                "units": {"length": "m", "force": "N", "temperature": "C"},
                "nodes": [
                    {"node_id": "node:invented:A", "target_id": "N001", "x": 0, "y": 0, "z": 0},
                    {"node_id": "node:invented:B", "target_id": "N002", "x": 1.5, "y": 0, "z": 0},
                ],
                "elements": [
                    {
                        "element_id": "pipe:invented:001",
                        "target_id": "P001",
                        "from_node": "N001",
                        "to_node": "N002",
                        "section_ref": "section:invented:small-bore",
                        "material_ref": "material:invented:generic",
                    }
                ],
                "supports": [
                    {"support_id": "support:invented:A", "target_id": "S001", "node": "N001", "support_kind": "ANCHOR"}
                ],
                "load_cases": [
                    {"load_case_id": "load:invented:operating", "target_id": "L001", "load_kind": "invented_operating"}
                ],
                "unsupported_entities": [
                    {"object_type": "BranchConnection", "ref": "branch:invented:not-in-first-subset"}
                ],
            },
            "stable_id_map": [
                {
                    "canonical_ref": {"object_type": "Node", "ref": "node:invented:A"},
                    "target_ref": {"object_type": "CaePipeMbfRecord", "ref": "N001"},
                    "mapping_status": "mapped_sidecar",
                    "loss_category": "exported",
                },
                {
                    "canonical_ref": {"object_type": "PipeElement", "ref": "pipe:invented:001"},
                    "target_ref": {"object_type": "CaePipeMbfRecord", "ref": "P001"},
                    "mapping_status": "mapped_sidecar",
                    "loss_category": "exported",
                },
            ],
            "loss_report": [
                {
                    "loss_id": "loss:invented:exported-smoke-subset",
                    "category": "exported",
                    "severity": "info",
                    "affected_refs": [{"object_type": "PipeElement", "ref": "pipe:invented:001"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:mbf_text"},
                    "reason": "Invented straight pipe smoke subset emitted for deterministic package testing.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-02"},
                    "governing_tbd_id": "TBD-17-01-002",
                    "downstream_implication": "Does not close broad MBF record-family coverage.",
                },
                {
                    "loss_id": "loss:invented:direct-id-carrier",
                    "category": "tbd",
                    "severity": "warning",
                    "affected_refs": [{"object_type": "CaePipeMbfRecord", "ref": "P001"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:stable_id_map"},
                    "reason": "Direct MBF stable ID carrier remains unconfirmed; sidecar mapping is used.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-01"},
                    "governing_tbd_id": "TBD-17-01-003",
                    "downstream_implication": "Downstream MBF work must keep sidecar mapping until direct carrier evidence is admitted.",
                },
                {
                    "loss_id": "loss:invented:omitted-expansion-joint",
                    "category": "omitted",
                    "severity": "warning",
                    "affected_refs": [{"object_type": "ExpansionJoint", "ref": "joint:invented:not-in-first-subset"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:loss_report"},
                    "reason": "Invented expansion joint behavior is outside the bounded smoke subset.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-04"},
                    "governing_tbd_id": "TBD-17-01-002",
                    "downstream_implication": "A later source-confirmed profile tranche must classify expansion joint records before export.",
                },
                {
                    "loss_id": "loss:invented:approximated-support",
                    "category": "approximated",
                    "severity": "warning",
                    "affected_refs": [{"object_type": "Support", "ref": "support:invented:A"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:mbf_text"},
                    "reason": "Invented support is represented only as a minimal smoke-subset support record.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-04"},
                    "governing_tbd_id": "TBD-17-01-002",
                    "downstream_implication": "Detailed support target behavior remains source-gated and must not be inferred from this fixture.",
                },
                {
                    "loss_id": "loss:invented:delegated-target-options",
                    "category": "delegated",
                    "severity": "warning",
                    "affected_refs": [{"object_type": "LoadCase", "ref": "load:invented:operating"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:manifest"},
                    "reason": "Target-side execution options are recorded as package metadata and are not executed by this foundation.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-04"},
                    "governing_tbd_id": "TBD-17-04-004",
                    "downstream_implication": "External execution and target result interpretation remain DEL-17-05 or later work.",
                },
                {
                    "loss_id": "loss:invented:unsupported-branch",
                    "category": "unsupported",
                    "severity": "warning",
                    "affected_refs": [{"object_type": "BranchConnection", "ref": "branch:invented:not-in-first-subset"}],
                    "target_artifact_ref": {"object_type": "CaePipeMbfMember", "ref": "caepipe-mbf:invented-del-17-04:loss_report"},
                    "reason": "Invented branch connection is not supported by the first CAEPIPE MBF smoke subset.",
                    "source_basis_ref": {"object_type": "Deliverable", "ref": "DEL-17-04"},
                    "governing_tbd_id": "TBD-17-04-004",
                    "downstream_implication": "The unsupported branch must remain visible until a later profile tranche classifies branch record support.",
                },
            ],
        }


    def build_from_source() -> dict[str, object]:
        payload = source_payload()
        return build_caepipe_mbf_export_package(**payload)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def sha256_value(value: str) -> str:
        return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        built = build_from_source()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(FIXTURE_PATH),
            )
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_caepipe_mbf_export_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_package_members():
        first = build_from_source()
        second = build_from_source()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-04"
        assert first["package_id"] == "PKG-17"
        assert first["package_status"] == "caepipe_mbf_export_foundation"
        assert first["export_profile"]["target_family"] == "caepipe_mbf"
        assert first["export_profile"]["target_version_basis"] == "TBD-17-01-001"
        assert first["export_profile"]["record_subset_basis"] == "TBD-17-01-002"
        assert "TBD-17-01-001" in first["export_profile"]["carried_tbd_refs"]
        assert "TBD-17-01-002" in first["export_profile"]["carried_tbd_refs"]
        assert "TBD-17-01-003" in first["export_profile"]["carried_tbd_refs"]
        source_basis_refs = {
            (item["object_type"], item["ref"]) for item in first["export_profile"]["source_basis_refs"]
        }
        assert source_basis_refs == EXPECTED_SOURCE_BASIS_REFS
        assert ("Deliverable", "DEL-17-03") not in source_basis_refs
        assert first["manifest"]["source_basis_refs"] == first["export_profile"]["source_basis_refs"]

        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "mbf_text",
            "unit_system_disclosure",
            "stable_id_map",
            "loss_report",
            "validation_report",
            "diagnostics",
        }
        assert first["unit_system_disclosure"]["unit_system_ref"]["ref"] == "unit-system:dec-018-si-dual-display"
        assert first["unit_system_disclosure"]["model_units"]["length"] == "m"
        assert first["unit_system_disclosure"]["target_export_units"]["force"] == "N"
        assert first["unit_system_disclosure"]["conversion_performed"] is False
        assert first["unit_system_disclosure"]["protected_content_included"] is False
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert {item["carrier_mode"] for item in first["stable_id_map"]} == {"sidecar_mapping"}
        assert {item["category"] for item in first["loss_report"]} == EXPECTED_LOSS_CATEGORIES
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_fixture_loss_report_covers_required_categories():
        fixture = load_json(FIXTURE_PATH)

        assert {item["category"] for item in fixture["loss_report"]} == EXPECTED_LOSS_CATEGORIES


    def test_rendered_mbf_text_is_stable_and_ascii_safe():
        package = build_from_source()
        text = package["mbf_text"]

        assert text == render_caepipe_mbf_text(package["model_payload"], package["export_profile"])
        assert text == canonical_text(text)
        text.encode("ascii")
        assert "NODE,N001,0,0,0" in text
        assert "PIPE,P001,N001,N002,section:invented:small-bore,material:invented:generic" in text
        assert "Canonical IDs are preserved in sidecar mapping" in text


    def test_missing_subset_stable_ids_and_loss_report_are_blocking():
        payload = source_payload()
        model_payload = deepcopy(payload["model_payload"])
        model_payload["elements"] = []

        package = build_caepipe_mbf_export_package(
            export_id="caepipe-mbf:blocked",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            model_payload=model_payload,
            stable_id_map=[],
            loss_report=[],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"MBF-SMOKE-SUBSET-MISSING", "MBF-STABLE-ID-SIDECAR-MISSING"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["validation_report"]["validation_status"] == "blocked"
        assert package["loss_report"][0]["category"] == "tbd"


    def test_unsupported_entities_require_reference_shape():
        payload = source_payload()
        model_payload = deepcopy(payload["model_payload"])
        model_payload["unsupported_entities"] = [{"object_type": "BranchConnection"}]

        package = build_caepipe_mbf_export_package(
            export_id="caepipe-mbf:malformed-unsupported",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            model_payload=model_payload,
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-UNSUPPORTED-ENTITY-REF-MISSING" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_unsupported_entities_require_matching_loss_report():
        payload = source_payload()
        loss_report = [item for item in payload["loss_report"] if item["category"] != "unsupported"]

        package = build_caepipe_mbf_export_package(
            export_id="caepipe-mbf:unsupported-loss-missing",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            model_payload=payload["model_payload"],
            stable_id_map=payload["stable_id_map"],
            loss_report=loss_report,
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-UNSUPPORTED-ENTITY-LOSS-MISSING" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_unsupported_warning_or_blocking_loss_classifies_entity():
        for severity in ("warning", "blocking"):
            payload = source_payload()
            for item in payload["loss_report"]:
                if item["category"] == "unsupported":
                    item["severity"] = severity

            package = build_caepipe_mbf_export_package(**payload)
            codes = {item["code"] for item in package["diagnostics"]}

            assert "MBF-UNSUPPORTED-ENTITY-LOSS-MISSING" not in codes
            assert "MBF-UNSUPPORTED-LOSS-SEVERITY-UNSAFE" not in codes


    def test_unsupported_info_loss_severity_is_blocking():
        payload = source_payload()
        for item in payload["loss_report"]:
            if item["category"] == "unsupported":
                item["severity"] = "info"

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-UNSUPPORTED-LOSS-SEVERITY-UNSAFE" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_target_version_basis_must_remain_carried_tbd():
        payload = source_payload()
        payload["export_profile"] = {"target_version_basis": ""}

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-TARGET-VERSION-BASIS-UNSAFE" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_record_subset_basis_must_remain_carried_tbd():
        payload = source_payload()
        payload["export_profile"] = {"record_subset_basis": "unreviewed-first-subset"}

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-RECORD-SUBSET-BASIS-UNSAFE" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_required_profile_tbd_refs_must_be_carried():
        payload = source_payload()
        payload["export_profile"] = {
            "carried_tbd_refs": ["TBD-17-01-001", "TBD-17-01-003"],
        }

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-CARRIED-TBD-REFS-MISSING" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_required_source_basis_refs_must_be_carried():
        payload = source_payload()
        payload["export_profile"] = {
            "source_basis_refs": [
                {"object_type": "Deliverable", "ref": "DEL-17-01"},
                {"object_type": "SourceID", "ref": "CAEPIPE-IMPORT-MBF"},
            ],
        }

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-SOURCE-BASIS-REFS-MISSING" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_del_17_03_is_not_caepipe_source_basis_authority():
        payload = source_payload()
        payload["export_profile"] = {
            "source_basis_refs": [
                {"object_type": object_type, "ref": ref}
                for object_type, ref in sorted(EXPECTED_SOURCE_BASIS_REFS)
            ]
            + [{"object_type": "Deliverable", "ref": "DEL-17-03"}],
        }

        package = build_caepipe_mbf_export_package(**payload)

        codes = {item["code"] for item in package["diagnostics"]}
        assert "MBF-SOURCE-BASIS-REFS-UNSAFE" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_privacy_and_authority_boundary_diagnostics_block_public_package():
        payload = source_payload()
        model_payload = deepcopy(payload["model_payload"])
        model_payload["free_metadata"] = {"unsafe_label": "cert" + "ified target export"}
        privacy = {"protected_payload_embedded": True}

        package = build_caepipe_mbf_export_package(
            export_id="caepipe-mbf:privacy-boundary",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            model_payload=model_payload,
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
            privacy=privacy,
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"MBF-PROHIBITED-AUTHORITY-TERM", "MBF-PRIVACY-BOUNDARY-VIOLATION"} <= codes
        assert package["privacy"]["protected_payload_embedded"] is True
        assert package["professional_boundary"]["software_makes_caepipe_compatibility_claim"] is False
        assert package["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def test_writer_outputs_all_manifest_members_with_matching_hashes(tmp_path):
        package = build_from_source()

        write_caepipe_mbf_export_package(tmp_path, package)

        members = package["manifest"]["package_members"]
        expected_paths = {member["path"] for member in members}
        written_paths = {str(path.relative_to(tmp_path)) for path in tmp_path.rglob("*") if path.is_file()}
        assert written_paths == expected_paths

        declared_checksums = package["manifest"]["checksums"]
        for member in members:
            role = member["member_role"]
            path = tmp_path / member["path"]
            assert path.exists()
            assert member["hash"] in declared_checksums

            if role == "manifest":
                assert load_json(path) == package["manifest"]
                continue
            if member["content_kind"] == "text/plain":
                text = path.read_text(encoding="ascii")
                assert text == package[role]
                assert member["hash"]["canonicalization"] == "normalized_ascii_lf_text"
                assert sha256_value(canonical_text(text)) == member["hash"]["value"]
            else:
                text = path.read_text(encoding="utf-8")
                parsed = json.loads(text)
                assert parsed == package[role]
                assert text == canonical_json(package[role]) + "\n"
                assert member["hash"]["canonicalization"] == "JCS_compatible_json_payload_hash"
                assert sha256_value(canonical_json(parsed)) == member["hash"]["value"]


    def test_fixture_contains_no_private_or_protected_payload_text():
        text = "\n".join(walk_strings(load_json(FIXTURE_PATH))).lower()
        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text


    def main():
        check_jsonschema_validation()
        test_builder_is_deterministic_and_preserves_package_members()
        test_fixture_loss_report_covers_required_categories()
        test_rendered_mbf_text_is_stable_and_ascii_safe()
        test_missing_subset_stable_ids_and_loss_report_are_blocking()
        test_unsupported_entities_require_reference_shape()
        test_unsupported_entities_require_matching_loss_report()
        test_unsupported_warning_or_blocking_loss_classifies_entity()
        test_unsupported_info_loss_severity_is_blocking()
        test_target_version_basis_must_remain_carried_tbd()
        test_record_subset_basis_must_remain_carried_tbd()
        test_required_profile_tbd_refs_must_be_carried()
        test_required_source_basis_refs_must_be_carried()
        test_del_17_03_is_not_caepipe_source_basis_authority()
        test_privacy_and_authority_boundary_diagnostics_block_public_package()
        test_fixture_contains_no_private_or_protected_payload_text()


    if __name__ == "__main__":
        main()

## Component: tests/test_calculation_witness.py

    #!/usr/bin/env python3
    """Formal calculation witness checks for TP-WITNESS-023."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import sys
    from tempfile import TemporaryDirectory


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from validation.witness.tools.witness_validator import (  # noqa: E402
        WitnessError,
        assert_generated_artifacts_current,
        evaluate_witness,
        load_json,
        render_markdown,
    )


    WITNESS_PATH = (
        ROOT
        / "validation"
        / "witness"
        / "fixtures"
        / "tp_phys_015_section_property_stress_witness.json"
    )


    def load_witness():
        return load_json(WITNESS_PATH)


    def expect_witness_error(witness, expected_text):
        try:
            evaluate_witness(witness)
        except WitnessError as exc:
            assert expected_text in str(exc)
        else:
            raise AssertionError(f"expected WitnessError containing {expected_text!r}")


    def test_tp_phys_015_witness_validates_and_compares_to_result_export():
        witness = load_witness()
        evaluation = evaluate_witness(witness)
        assert evaluation.witness_id == "WITNESS-TP-PHYS-015-SECTION-PROPERTY-STRESS"
        assert len(evaluation.comparisons) == 6
        by_formula = {comparison.formula_id: comparison for comparison in evaluation.comparisons}
        assert by_formula["bending_normal_stress_z"].passed
        assert by_formula["bending_normal_stress_z"].result_id == (
            "result:stress:element-E-1:midspan:bending-normal-z"
        )


    def test_generated_markdown_and_mathml_are_current():
        witness = load_witness()
        assert_generated_artifacts_current(witness)
        rendered = render_markdown(witness)
        assert "Witness SHA-256 over canonical JSON" in rendered
        assert "Do not edit this file as the authoritative calculation source." in rendered


    def test_rejects_unsupported_openmath_symbol():
        witness = load_witness()
        witness["formulas"][0]["openmath"]["operator"]["name"] = "sin"
        expect_witness_error(witness, "unsupported OpenMath")


    def test_rejects_dimension_mismatch():
        witness = load_witness()
        witness["formulas"][1]["expected_dimension"] = "force"
        expect_witness_error(witness, "dimension mismatch")


    def test_rejects_stale_generated_markdown(tmp_path):
        witness = load_witness()
        stale = tmp_path / "stale.md"
        stale.write_text("stale\n", encoding="utf-8")
        witness["generated_artifacts"]["markdown_path"] = str(stale)
        try:
            assert_generated_artifacts_current(witness)
        except WitnessError as exc:
            assert "generated Markdown is stale" in str(exc)
        else:
            raise AssertionError("expected stale generated Markdown to be rejected")


    def test_rejects_tampered_formula_output():
        witness = load_witness()
        witness["formulas"][-3]["openmath"]["arguments"][0]["name"] = "torsional_moment"
        expect_witness_error(witness, "OPS result mismatch")


    def test_rejects_missing_provenance():
        witness = load_witness()
        del witness["provenance"]
        expect_witness_error(witness, "witness schema validation failed")


    def test_rejects_ops_result_mismatch(tmp_path):
        witness = load_witness()
        result_path = ROOT / witness["result_export"]["path"]
        result_export = json.loads(result_path.read_text(encoding="utf-8"))
        result_export["result_envelope"]["result_sets"][1]["values"][0]["magnitude"] = 8.0
        tampered_result_path = tmp_path / "tampered-result.json"
        tampered_result_path.write_text(json.dumps(result_export), encoding="utf-8")
        witness["result_export"]["path"] = str(tampered_result_path)
        expect_witness_error(witness, "OPS result mismatch")


    def test_rendered_markdown_changes_when_witness_changes():
        witness = load_witness()
        changed = deepcopy(witness)
        changed["title"] = "Changed witness title"
        assert render_markdown(witness) != render_markdown(changed)


    def main():
        test_tp_phys_015_witness_validates_and_compares_to_result_export()
        test_generated_markdown_and_mathml_are_current()
        test_rejects_unsupported_openmath_symbol()
        test_rejects_dimension_mismatch()
        with TemporaryDirectory() as directory:
            test_rejects_stale_generated_markdown(Path(directory))
        test_rejects_tampered_formula_output()
        test_rejects_missing_provenance()
        with TemporaryDirectory() as directory:
            test_rejects_ops_result_mismatch(Path(directory))
        test_rendered_markdown_changes_when_witness_changes()


    if __name__ == "__main__":
        main()

## Component: tests/test_comparison_contracts.py

    #!/usr/bin/env python3
    """Stdlib checks for DEL-14-05 comparison mapping and tolerance schemas."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    MAPPING_SCHEMA_PATH = ROOT / "schemas" / "comparison_mapping.schema.json"
    TOLERANCE_SCHEMA_PATH = ROOT / "schemas" / "comparison_tolerance.schema.json"

    REQUIRED_MAPPING_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "comparison_contract_status",
        "comparison_review",
    }

    REQUIRED_TOLERANCE_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "tolerance_contract_status",
        "tolerance_profile",
    }

    REQUIRED_MAPPING_DEFS = {
        "AffectedRef",
        "AssumptionRecord",
        "Checksum",
        "ComparisonContractStatus",
        "ComparisonParticipant",
        "ComparisonReview",
        "CsvExportContract",
        "Diagnostic",
        "ExportContract",
        "Id",
        "JsonExportContract",
        "MappingConfidence",
        "MappingEvidence",
        "MappingRecord",
        "MappingStatus",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ReportSectionExportRef",
        "ReviewMetadata",
        "ReviewStatus",
        "StableRecordReference",
        "UnmatchedClassification",
        "UnmatchedRecord",
    }

    REQUIRED_TOLERANCE_DEFS = {
        "AssumptionRecord",
        "Checksum",
        "Diagnostic",
        "DimensionId",
        "Id",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ReviewMetadata",
        "ReviewStatus",
        "ToleranceContractStatus",
        "ToleranceProfile",
        "ToleranceRule",
        "UnitMetadataPolicy",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "formal " + "acceptance",
        "code " + "compliant",
        "certified " + "by software",
        "sealed " + "by software",
        "professional approval " + "by the software",
        "commercial prover " + "ingestion",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def assert_common_root(schema, required_root):
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert required_root <= set(schema["required"])
        assert schema["properties"]["deliverable_id"]["const"] == "DEL-14-05"
        assert schema["properties"]["package_id"]["const"] == "PKG-14"
        assert schema["properties"]["scope_item"]["const"] == "SOW-073"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-016"


    def assert_professional_boundary(schema):
        professional = schema["$defs"]["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False


    def assert_forbidden_text_absent(*schemas):
        joined_strings = "\n".join(
            string.lower() for schema in schemas for string in walk_strings(schema)
        )
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings


    def test_mapping_schema_contract():
        schema = load_json(MAPPING_SCHEMA_PATH)
        defs = schema["$defs"]

        assert_common_root(schema, REQUIRED_MAPPING_ROOT)
        assert REQUIRED_MAPPING_DEFS <= set(defs)

        contract = defs["ComparisonContractStatus"]["properties"]
        assert contract["record_contract"]["const"] == (
            "schema_first_comparison_mapping_review_records"
        )
        assert contract["model_state_binding"]["const"] == "schemas/model_state.schema.json"
        assert contract["analysis_run_binding"]["const"] == "schemas/analysis_run.schema.json"
        assert contract["result_envelope_binding"]["const"] == "schemas/results.schema.yaml"
        assert contract["tolerance_profile_binding"]["const"] == (
            "schemas/comparison_tolerance.schema.json"
        )
        assert contract["export_contract_scope"]["const"] == "json_csv_review_contract_only"
        assert contract["report_rendering"]["const"] == (
            "reserved_reference_only_not_implemented"
        )
        assert contract["comparison_engine"]["const"] == "not_implemented_by_this_contract"
        assert contract["external_validation_boundary"]["const"] == (
            "reference_only_not_determined_by_software"
        )

        participant_required = required_at(schema, "ComparisonParticipant")
        assert {
            "participant_id",
            "side",
            "model_state_ref",
            "analysis_run_ref",
            "result_envelope_ref",
            "unit_system_ref",
            "hash_refs",
            "provenance",
        } <= participant_required
        stable_ref = defs["StableRecordReference"]["properties"]
        assert {
            "model_state_record",
            "analysis_run_record",
            "result_export_envelope",
        } <= set(stable_ref["record_type"]["enum"])
        assert {
            "schemas/model_state.schema.json",
            "schemas/analysis_run.schema.json",
            "schemas/results.schema.yaml",
        } <= set(stable_ref["schema_ref"]["enum"])

        mapping_status = enum_at(schema, "MappingStatus")
        assert {
            "automatic_match",
            "manual_match",
            "unresolved_mapping",
            "unmatched_left",
            "unmatched_right",
            "ignored",
            "TBD",
        } <= mapping_status
        mapping_required = required_at(schema, "MappingRecord")
        assert {
            "mapping_id",
            "mapping_kind",
            "mapping_status",
            "left_ref",
            "right_ref",
            "affected_refs",
            "mapping_evidence",
            "confidence",
            "review",
            "provenance",
        } <= mapping_required
        evidence_required = required_at(schema, "MappingEvidence")
        assert {
            "evidence_id",
            "evidence_kind",
            "source_refs",
            "stable_id_preservation",
            "manual_review_state",
            "hash_refs",
            "provenance",
        } <= evidence_required
        evidence = defs["MappingEvidence"]["properties"]
        assert {
            "stable_id_alignment",
            "manual_mapping",
            "unmatched_classification",
            "ignored_by_scope",
            "TBD",
        } <= set(evidence["evidence_kind"]["enum"])
        assert {
            "left_and_right_refs_preserved",
            "source_ref_preserved_for_unmatched",
            "not_applicable",
            "TBD",
        } <= set(evidence["stable_id_preservation"]["enum"])
        assert {
            "not_manual",
            "manual_unreviewed",
            "manual_reviewed",
            "TBD",
        } <= set(evidence["manual_review_state"]["enum"])
        assert {
            "exact_stable_id",
            "manual_reviewed",
            "manual_unreviewed",
            "heuristic_candidate",
            "unresolved",
        } <= set(defs["MappingConfidence"]["properties"]["confidence_level"]["enum"])

        assert {
            "left_only",
            "right_only",
            "missing_counterpart",
            "intentionally_ignored",
            "not_comparable",
            "scope_excluded",
            "unresolved_TBD",
        } <= enum_at(schema, "UnmatchedClassification")
        assert {
            "unmatched_id",
            "classification",
            "subject_ref",
            "affected_refs",
            "hash_refs",
            "review",
            "provenance",
        } <= required_at(schema, "UnmatchedRecord")

        export_required = required_at(schema, "ExportContract")
        assert {
            "diagnostics_included",
            "provenance_included",
            "assumptions_included",
            "hash_refs_included",
            "professional_boundary_notice_included",
        } <= export_required
        export = defs["ExportContract"]["properties"]
        for key in {
            "diagnostics_included",
            "provenance_included",
            "assumptions_included",
            "hash_refs_included",
            "professional_boundary_notice_included",
        }:
            assert export[key]["const"] is True
        json_export = defs["JsonExportContract"]["properties"]
        for key in {
            "stable_ids_required",
            "mapping_ids_required",
            "unit_metadata_required",
            "tolerance_profile_refs_required",
            "diagnostics_required",
            "provenance_required",
            "assumptions_required",
            "hash_refs_required",
            "professional_boundary_notice_required",
        }:
            assert json_export[key]["const"] is True
        csv_columns = set(defs["CsvExportContract"]["properties"]["required_columns"]["items"]["enum"])
        assert {
            "review_row_id",
            "comparison_id",
            "mapping_id",
            "unit",
            "dimension",
            "tolerance_profile_ref",
            "hash_refs",
            "diagnostic_codes",
            "provenance_ref",
            "assumption_ids",
            "professional_boundary_notice",
        } <= csv_columns
        csv_required_columns = {
            rule["contains"]["const"]
            for rule in defs["CsvExportContract"]["properties"]["required_columns"]["allOf"]
        }
        assert {
            "review_row_id",
            "comparison_id",
            "mapping_id",
            "mapping_status",
            "unmatched_classification",
            "left_ref",
            "right_ref",
            "unit",
            "dimension",
            "tolerance_profile_ref",
            "hash_refs",
            "provenance_ref",
            "professional_boundary_notice",
        } <= csv_required_columns
        assert (
            defs["ReportSectionExportRef"]["properties"]["rendering_status"]["const"]
            == "reserved_reference_only_not_implemented"
        )
        report_export = defs["ReportSectionExportRef"]["properties"]
        for key in {
            "hash_refs_required",
            "provenance_required",
            "professional_boundary_notice_required",
        }:
            assert report_export[key]["const"] is True
        assert_professional_boundary(schema)


    def test_tolerance_schema_contract():
        schema = load_json(TOLERANCE_SCHEMA_PATH)
        defs = schema["$defs"]

        assert_common_root(schema, REQUIRED_TOLERANCE_ROOT)
        assert REQUIRED_TOLERANCE_DEFS <= set(defs)

        contract = defs["ToleranceContractStatus"]["properties"]
        assert contract["record_contract"]["const"] == (
            "schema_first_unit_aware_tolerance_profiles"
        )
        assert contract["unit_system_binding"]["const"] == "schemas/units.schema.yaml"
        assert contract["comparison_mapping_binding"]["const"] == (
            "schemas/comparison_mapping.schema.json"
        )
        assert contract["default_numeric_tolerances"]["const"] == (
            "not_defined_by_this_contract"
        )
        assert contract["result_delta_engine"]["const"] == "not_implemented_by_this_contract"
        assert contract["external_validation_boundary"]["const"] == (
            "reference_only_not_determined_by_software"
        )

        profile_required = required_at(schema, "ToleranceProfile")
        assert {
            "profile_id",
            "profile_name",
            "profile_status",
            "unit_system_ref",
            "applicable_dimensions",
            "rules",
            "diagnostics",
            "assumptions",
            "hashes",
            "review",
            "professional_boundary",
            "provenance",
        } <= profile_required
        assert {
            "dimensionless",
            "length",
            "force",
            "moment",
            "stress",
            "displacement",
            "rotation",
            "ratio",
        } <= enum_at(schema, "DimensionId")

        rule_required = required_at(schema, "ToleranceRule")
        assert {
            "rule_id",
            "result_family",
            "dimension_id",
            "unit_ref",
            "quantity_kind",
            "tolerance_value",
            "tolerance_value_status",
            "normalization_basis",
            "unit_metadata_policy",
            "hash_refs",
            "review",
            "provenance",
        } <= rule_required
        tolerance_value = defs["ToleranceRule"]["properties"]["tolerance_value"]
        assert "default" not in set(walk_keys(tolerance_value))
        assert {"TBD", "externally_governed_reference_required"} <= set(
            tolerance_value["oneOf"][1]["enum"]
        )
        assert {
            "externally_governed",
            "project_specific_review_required",
            "not_defined",
            "TBD",
        } <= set(defs["ToleranceRule"]["properties"]["tolerance_value_status"]["enum"])
        numeric_guard = defs["ToleranceRule"]["allOf"][0]
        assert numeric_guard["if"]["properties"]["tolerance_value"]["type"] == "number"
        assert {
            "externally_governed",
            "project_specific_review_required",
        } == set(numeric_guard["then"]["properties"]["tolerance_value_status"]["enum"])
        assert {
            "same_unit_required",
            "unit_conversion_required",
            "dimensionless_direct",
            "not_applicable",
            "TBD",
        } <= set(defs["ToleranceRule"]["properties"]["normalization_basis"]["enum"])
        unit_policy = defs["UnitMetadataPolicy"]["properties"]
        assert unit_policy["dimension_id_required"]["const"] is True
        assert unit_policy["unit_ref_required"]["const"] is True
        assert unit_policy["normalized_delta_unit_metadata_required"]["const"] is True
        assert (
            unit_policy["missing_unit_metadata_behavior"]["const"]
            == "blocking_diagnostic_required"
        )
        assert_professional_boundary(schema)


    def test_contracts_avoid_prohibited_scope_and_defaults():
        mapping = load_json(MAPPING_SCHEMA_PATH)
        tolerance = load_json(TOLERANCE_SCHEMA_PATH)

        assert_forbidden_text_absent(mapping, tolerance)
        all_keys = set(walk_keys(mapping)) | set(walk_keys(tolerance))
        assert "default" not in all_keys


    if __name__ == "__main__":
        test_mapping_schema_contract()
        test_tolerance_schema_contract()
        test_contracts_avoid_prohibited_scope_and_defaults()

## Component: tests/test_component_section_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the section and component library schemas."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )

    SECTION_SCHEMA_PATH = ROOT / "schemas" / "section.schema.yaml"
    COMPONENT_SCHEMA_PATH = ROOT / "schemas" / "component.schema.yaml"
    MODEL_SCHEMA_PATH = ROOT / "schemas" / "model.schema.yaml"
    UNITS_SCHEMA_PATH = ROOT / "schemas" / "units.schema.yaml"
    COMBINED_FIXTURE_PATH = (
        ROOT / "fixtures" / "component" / "invented_section_component_library_valid.json"
    )
    SECTION_FIXTURE_PATH = ROOT / "fixtures" / "component" / "invented_section_library_valid.json"
    COMPONENT_FIXTURE_PATH = (
        ROOT / "fixtures" / "component" / "invented_component_library_valid.json"
    )

    RETIRED_DIMENSIONS = {
        "temperature_difference",
        "area_moment",
        "stiffness",
        "reference",
    }

    REQUIRED_PROVENANCE_FIELDS = {
        "source_name",
        "source_location",
        "source_license",
        "contributor",
        "contributor_certification",
        "redistribution_status",
        "review_status",
    }

    FORBIDDEN_PUBLIC_DATA_TEXT = {
        "ASME",
        "B31",
        "CODE_COMPLIANT",
        "certified component",
        "certified section",
        "automatic compliance",
        "professional approval by the software",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def main():
        section_schema = load_json(SECTION_SCHEMA_PATH)
        component_schema = load_json(COMPONENT_SCHEMA_PATH)
        model_schema = load_json(MODEL_SCHEMA_PATH)
        units_schema = load_json(UNITS_SCHEMA_PATH)
        combined_fixture = load_json(COMBINED_FIXTURE_PATH)
        section_fixture = load_json(SECTION_FIXTURE_PATH)
        component_fixture = load_json(COMPONENT_FIXTURE_PATH)
        accepted_dimensions = set(units_schema["$defs"]["DimensionId"]["enum"])

        for schema in (section_schema, component_schema):
            assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
            assert schema["additionalProperties"] is False
            assert "default" not in set(walk_keys(schema))
            assert REQUIRED_PROVENANCE_FIELDS <= required_at(schema, "Provenance")
            assert {
                "public_permissive",
                "private_only",
                "unknown",
                "protected_suspected",
                "rejected",
                "TBD",
            } <= enum_at(schema, "RedistributionStatus")

        assert {
            "schema_version",
            "section_library",
            "section_records",
            "dimension_definitions",
            "property_definitions",
            "completeness_rules",
            "diagnostics",
            "open_decisions",
        } <= set(section_schema["required"])
        assert {
            "section_id",
            "name",
            "section_type",
            "privacy_class",
            "redistribution_status",
            "dimensions",
            "properties",
            "completeness",
            "provenance",
            "review_status",
        } <= required_at(section_schema, "SectionRecord")
        assert {
            "outside_diameter",
            "wall_thickness",
            "corrosion_allowance",
            "nominal_size_label",
            "user_defined",
            "TBD",
        } <= enum_at(section_schema, "SectionDimensionKind")
        assert {
            "cross_section_area",
            "inside_diameter",
            "moment_of_inertia",
            "section_modulus",
            "mass_per_length",
            "user_defined",
            "TBD",
        } <= enum_at(section_schema, "SectionPropertyKind")
        section_dimensions = enum_at(section_schema, "SectionDimension")
        assert {
            "second_moment_area",
            "section_modulus",
            "volume_per_length",
            "mass_per_length",
        } <= section_dimensions
        assert section_dimensions <= accepted_dimensions
        assert not (section_dimensions & RETIRED_DIMENSIONS)
        assert {
            "SECTION_DIMENSION_MISSING",
            "SECTION_UNIT_MISSING",
            "SECTION_PROVENANCE_MISSING",
            "SECTION_PROTECTED_CONTENT_SUSPECTED",
            "SECTION_CALCULATION_INPUT_INVALID",
            "SECTION_DIMENSION_INCONSISTENT",
            "SECTION_CATALOG_VALUE_NOT_PUBLIC",
        } <= enum_at(section_schema, "SectionDiagnosticCode")
        assert {"class", "source"} <= required_at(section_schema, "SectionDiagnostic")

        assert {
            "schema_version",
            "component_library",
            "component_family_contracts",
            "component_records",
            "field_definitions",
            "completeness_rules",
            "diagnostics",
            "open_decisions",
        } <= set(component_schema["required"])
        assert {
            "component_id",
            "name",
            "component_type",
            "privacy_class",
            "redistribution_status",
            "fields",
            "completeness",
            "provenance",
            "review_status",
        } <= required_at(component_schema, "ComponentRecord")
        assert {
            "bend",
            "elbow",
            "branch",
            "reducer",
            "valve",
            "flange",
            "expansion_joint",
            "rigid",
            "specialty",
            "other",
            "TBD",
        } <= enum_at(component_schema, "ComponentType")
        model_component_types = set(
            model_schema["$defs"]["Component"]["properties"]["component_type"]["enum"]
        )
        assert enum_at(component_schema, "ComponentType") == model_component_types
        assert {
            "bend_centerline_radius",
            "bend_included_angle",
            "bend_plane_orientation",
            "bend_geometry_source_reference",
            "branch_run_size",
            "branch_header_size",
            "branch_connection_angle",
            "branch_connection_type",
            "branch_reinforcement_area",
            "branch_reinforcement_reference",
            "branch_geometry_source_reference",
            "rigid_body_length",
            "connection_end_a_reference",
            "connection_end_b_reference",
            "stiffness_behavior_reference",
            "rigid_component_source_reference",
            "weight",
            "center_of_gravity",
            "linear_stiffness",
            "rotational_stiffness",
            "effective_area",
            "movement_limit",
            "sif_user_value",
            "flexibility_factor_user_value",
            "manufacturer_reference",
            "TBD",
        } <= enum_at(component_schema, "ComponentFieldKind")
        component_dimensions = enum_at(component_schema, "ComponentQuantityDimension")
        assert {"linear_stiffness", "rotational_stiffness"} <= component_dimensions
        assert component_dimensions <= accepted_dimensions
        assert not (component_dimensions & RETIRED_DIMENSIONS)
        assert {
            "COMPONENT_FIELD_MISSING",
            "COMPONENT_UNIT_MISSING",
            "COMPONENT_PROVENANCE_MISSING",
            "COMPONENT_PROTECTED_CONTENT_SUSPECTED",
            "COMPONENT_MODIFIER_NOT_PUBLIC",
            "BEND_GEOMETRY_INCOMPLETE",
            "BEND_RULE_INPUT_MISSING",
            "BRANCH_GEOMETRY_INCOMPLETE",
            "BRANCH_REINFORCEMENT_DATA_MISSING",
            "BRANCH_RULE_INPUT_MISSING",
            "RIGID_COMPONENT_GEOMETRY_INCOMPLETE",
            "RIGID_COMPONENT_MASS_DATA_MISSING",
            "RIGID_COMPONENT_STIFFNESS_DATA_MISSING",
            "RIGID_COMPONENT_CATALOG_VALUE_NOT_PUBLIC",
            "EXPANSION_JOINT_STIFFNESS_DATA_MISSING",
            "EXPANSION_JOINT_EFFECTIVE_AREA_MISSING",
            "EXPANSION_JOINT_MOVEMENT_LIMIT_MISSING",
            "EXPANSION_JOINT_HARDWARE_DATA_MISSING",
            "EXPANSION_JOINT_MANUFACTURER_VALUE_NOT_PUBLIC",
        } <= enum_at(component_schema, "ComponentDiagnosticCode")
        assert {"class", "source"} <= required_at(component_schema, "ComponentDiagnostic")
        assert {
            "contract_id",
            "component_types",
            "geometry_field_kinds",
            "rule_modifier_field_kinds",
            "source_metadata_field_kinds",
            "mechanics_interface",
            "protected_value_policy",
            "review_status",
        } <= required_at(component_schema, "ComponentFamilyContract")

        assert (
            combined_fixture["strict_section_fixture_ref"]
            == "fixtures/component/invented_section_library_valid.json"
        )
        assert (
            combined_fixture["strict_component_fixture_ref"]
            == "fixtures/component/invented_component_library_valid.json"
        )

        assert section_fixture["section_library"]["library_scope"] == "public_schema_fixture"
        assert section_fixture["section_records"][0]["redistribution_status"] == "TBD"
        assert section_fixture["section_records"][0]["dimensions"][0]["value_status"] == "missing"
        assert section_fixture["section_records"][0]["completeness"][0]["status"] == "incomplete"
        assert section_fixture["diagnostics"][0]["code"] == "SECTION_DIMENSION_MISSING"
        assert section_fixture["diagnostics"][0]["class"] == "SOLVE_BLOCKING"
        assert section_fixture["diagnostics"][0]["source"] == (
            "fixtures/component/invented_section_library_valid.json"
        )

        assert component_fixture["component_library"]["library_scope"] == "public_schema_fixture"
        bend_contract = component_fixture["component_family_contracts"][0]
        assert {"bend", "elbow"} <= set(bend_contract["component_types"])
        assert "bend_centerline_radius" in bend_contract["geometry_field_kinds"]
        assert "sif_user_value" in bend_contract["rule_modifier_field_kinds"]
        assert bend_contract["protected_value_policy"] == "schema_slots_only"
        branch_contract = component_fixture["component_family_contracts"][1]
        assert branch_contract["component_types"] == ["branch"]
        assert "branch_run_size" in branch_contract["geometry_field_kinds"]
        assert "branch_reinforcement_reference" in branch_contract["source_metadata_field_kinds"]
        assert "sif_user_value" in branch_contract["rule_modifier_field_kinds"]
        assert branch_contract["protected_value_policy"] == "schema_slots_only"
        rigid_contract = component_fixture["component_family_contracts"][2]
        assert {"valve", "flange", "reducer", "rigid", "specialty"} <= set(
            rigid_contract["component_types"]
        )
        assert "rigid_body_length" in rigid_contract["geometry_field_kinds"]
        assert "connection_end_a_reference" in rigid_contract["geometry_field_kinds"]
        assert "weight" in rigid_contract["rule_modifier_field_kinds"]
        assert "center_of_gravity" in rigid_contract["rule_modifier_field_kinds"]
        assert "linear_stiffness" in rigid_contract["rule_modifier_field_kinds"]
        assert "rotational_stiffness" in rigid_contract["rule_modifier_field_kinds"]
        assert rigid_contract["protected_value_policy"] == "schema_slots_only"
        expansion_contract = component_fixture["component_family_contracts"][3]
        assert expansion_contract["component_types"] == ["expansion_joint"]
        assert "effective_area" in expansion_contract["geometry_field_kinds"]
        assert "movement_limit" in expansion_contract["geometry_field_kinds"]
        assert "linear_stiffness" in expansion_contract["rule_modifier_field_kinds"]
        assert "rotational_stiffness" in expansion_contract["rule_modifier_field_kinds"]
        assert "hardware_reference" in expansion_contract["rule_modifier_field_kinds"]
        assert "manufacturer_reference" in expansion_contract["source_metadata_field_kinds"]
        assert expansion_contract["protected_value_policy"] == "schema_slots_only"
        assert component_fixture["component_records"][0]["redistribution_status"] == "TBD"
        fixture_field_kinds = {
            field["field_kind"] for field in component_fixture["component_records"][0]["fields"]
        }
        assert "bend_centerline_radius" in fixture_field_kinds
        assert "bend_included_angle" in fixture_field_kinds
        assert (
            component_fixture["component_records"][0]["fields"][0][
                "public_repository_value_policy"
            ]
            == "schema_shape_only"
        )
        assert component_fixture["component_records"][0]["completeness"][0]["status"] == "incomplete"
        assert component_fixture["diagnostics"][0]["code"] == "BEND_GEOMETRY_INCOMPLETE"
        assert component_fixture["diagnostics"][0]["class"] == "SOLVE_BLOCKING"
        branch_record = component_fixture["component_records"][1]
        assert branch_record["component_type"] == "branch"
        branch_field_kinds = {field["field_kind"] for field in branch_record["fields"]}
        assert "branch_run_size" in branch_field_kinds
        assert "branch_header_size" in branch_field_kinds
        assert "branch_connection_angle" in branch_field_kinds
        assert "branch_reinforcement_reference" in branch_field_kinds
        assert "sif_user_value" in branch_field_kinds
        assert branch_record["fields"][-1]["public_repository_value_policy"] == "no_public_code_specific_values"
        assert branch_record["completeness"][0]["status"] == "incomplete"
        assert branch_record["completeness"][0]["diagnostic_code"] == "BRANCH_RULE_INPUT_MISSING"
        assert component_fixture["diagnostics"][1]["code"] == "BRANCH_RULE_INPUT_MISSING"
        rigid_record = component_fixture["component_records"][2]
        assert rigid_record["component_type"] == "rigid"
        rigid_field_kinds = {field["field_kind"] for field in rigid_record["fields"]}
        assert "rigid_body_length" in rigid_field_kinds
        assert "connection_end_a_reference" in rigid_field_kinds
        assert "weight" in rigid_field_kinds
        assert "center_of_gravity" in rigid_field_kinds
        assert "linear_stiffness" in rigid_field_kinds
        assert "rotational_stiffness" in rigid_field_kinds
        assert (
            rigid_record["fields"][2]["public_repository_value_policy"]
            == "no_public_proprietary_catalog_values"
        )
        assert rigid_record["completeness"][0]["status"] == "incomplete"
        assert (
            rigid_record["completeness"][0]["diagnostic_code"]
            == "RIGID_COMPONENT_GEOMETRY_INCOMPLETE"
        )
        assert component_fixture["diagnostics"][2]["code"] == "RIGID_COMPONENT_GEOMETRY_INCOMPLETE"
        expansion_record = component_fixture["component_records"][3]
        assert expansion_record["component_type"] == "expansion_joint"
        expansion_field_kinds = {field["field_kind"] for field in expansion_record["fields"]}
        assert "linear_stiffness" in expansion_field_kinds
        assert "rotational_stiffness" in expansion_field_kinds
        assert "effective_area" in expansion_field_kinds
        assert "movement_limit" in expansion_field_kinds
        assert "hardware_reference" in expansion_field_kinds
        assert "manufacturer_reference" in expansion_field_kinds
        assert (
            expansion_record["fields"][0]["public_repository_value_policy"]
            == "private_user_supplied_only"
        )
        assert expansion_record["completeness"][0]["status"] == "incomplete"
        assert (
            expansion_record["completeness"][0]["diagnostic_code"]
            == "EXPANSION_JOINT_STIFFNESS_DATA_MISSING"
        )
        assert (
            component_fixture["diagnostics"][3]["code"]
            == "EXPANSION_JOINT_STIFFNESS_DATA_MISSING"
        )

        all_text = "\n".join(
            [
                *walk_strings(section_schema),
                *walk_strings(component_schema),
                *walk_strings(combined_fixture),
                *walk_strings(section_fixture),
                *walk_strings(component_fixture),
            ]
        )
        for forbidden in FORBIDDEN_PUBLIC_DATA_TEXT:
            assert forbidden not in all_text


    def check_jsonschema_validation():
        section_schema = load_json(SECTION_SCHEMA_PATH)
        component_schema = load_json(COMPONENT_SCHEMA_PATH)
        section_fixture = load_json(SECTION_FIXTURE_PATH)
        component_fixture = load_json(COMPONENT_FIXTURE_PATH)
        try:
            assert validate_schema_document(section_schema, schema_label=str(SECTION_SCHEMA_PATH))
            assert validate_schema_document(
                component_schema,
                schema_label=str(COMPONENT_SCHEMA_PATH),
            )
            assert validate_instance(
                section_schema,
                section_fixture,
                schema_label=str(SECTION_SCHEMA_PATH),
                instance_label=str(SECTION_FIXTURE_PATH),
            )
            assert validate_instance(
                component_schema,
                component_fixture,
                schema_label=str(COMPONENT_SCHEMA_PATH),
                instance_label=str(COMPONENT_FIXTURE_PATH),
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_component_section_schema_contract():
        main()


    def test_component_section_jsonschema_validation_helper():
        check_jsonschema_validation()


    if __name__ == "__main__":
        main()
        check_jsonschema_validation()

## Component: tests/test_constraint_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the constraint entity schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "constraint.schema.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_items",
        "objectives",
        "data_boundary",
        "constraint_set",
    }

    REQUIRED_DEFS = {
        "AssumptionRecord",
        "ConstraintKind",
        "ConstraintRecord",
        "ConstraintSet",
        "DataBoundary",
        "Diagnostic",
        "Id",
        "Parameter",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "Quantity",
        "RedistributionStatus",
        "Reference",
        "ReviewStatus",
        "SourceType",
        "ValidationStatus",
    }

    REQUIRED_CONSTRAINT_KINDS = {
        "connectivity",
        "clearance",
        "no_go_volume",
        "support_zone",
        "route_conflict",
        "slope",
        "drain",
        "vent",
        "access",
        "equipment_interface",
        "missing_required_data",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "CONSTRAINT_MISSING_DATA",
        "CONNECTIVITY_CONFLICT",
        "CLEARANCE_CONFLICT",
        "ROUTE_CONFLICT",
        "SUPPORT_ZONE_CONFLICT",
        "SLOPE_DRAIN_VENT_CONFLICT",
        "PROVENANCE_WARNING",
        "UNIT_WARNING",
        "IP_BOUNDARY_WARNING",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "allowable stress table",
        "stress intensification factor table",
        "B31J",
        "real secret",
        "code compliant",
        "certified by software",
        "sealed by software",
        "professional approval by the software",
    }

    ACCEPTED_PKG02_DIMENSIONS = {
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-13-02"
        assert schema["properties"]["package_id"]["const"] == "PKG-13"
        assert {"SOW-067", "SOW-068"} <= set(
            schema["properties"]["scope_items"]["items"]["enum"]
        )
        assert {"OBJ-014", "OBJ-018"} <= set(
            schema["properties"]["objectives"]["items"]["enum"]
        )

        boundary = defs["DataBoundary"]["properties"]
        assert boundary["public_examples_policy"]["const"] == "invented_or_cleared_data_only"
        assert (
            boundary["protected_source_policy"]["const"]
            == "no_bundled_protected_owner_or_standards_data"
        )
        assert (
            boundary["unit_policy"]["const"]
            == "unit_bearing_values_require_explicit_unit_metadata"
        )
        assert boundary["engineering_authority"]["const"] == (
            "human_review_required_outside_software"
        )

        assert REQUIRED_CONSTRAINT_KINDS <= enum_at(schema, "ConstraintKind")
        assert {"user", "project", "import", "agent", "source_derived"} <= enum_at(
            schema, "SourceType"
        )
        assert {
            "unvalidated",
            "schema_validated",
            "constraint_validated",
            "conflict_detected",
            "missing_data",
            "blocked_by_missing_data",
        } <= enum_at(schema, "ValidationStatus")

        set_required = required_at(schema, "ConstraintSet")
        assert {
            "constraint_set_id",
            "project_ref",
            "model_ref",
            "design_knowledge_refs",
            "constraints",
            "diagnostics",
            "provenance",
            "professional_boundary",
        } <= set_required
        assert (
            defs["ConstraintSet"]["properties"]["constraints"]["items"]["$ref"]
            == "#/$defs/ConstraintRecord"
        )

        record_required = required_at(schema, "ConstraintRecord")
        assert {
            "constraint_id",
            "constraint_kind",
            "state",
            "source_type",
            "target_refs",
            "design_knowledge_refs",
            "parameters",
            "diagnostics",
            "assumptions",
            "validation_status",
            "provenance",
            "professional_boundary",
        } <= record_required

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        assert {"value", "unit", "dimension", "provenance"} <= required_at(
            schema, "Quantity"
        )
        dimensions = set(defs["Quantity"]["properties"]["dimension"]["enum"])
        assert dimensions == ACCEPTED_PKG02_DIMENSIONS
        assert "temperature_difference" not in dimensions
        assert "area_moment" not in dimensions
        assert "stiffness" not in dimensions

        provenance_required = required_at(schema, "Provenance")
        assert {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
            "privacy_classification",
        } <= provenance_required
        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "invented_non_engineering_example",
        } <= enum_at(schema, "RedistributionStatus")

        professional = defs["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings


    if __name__ == "__main__":
        main()

## Component: tests/test_constraint_validation.py

    #!/usr/bin/env python3
    """Focused tests for DEL-13-03 constraint validation."""

    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.constraints.validation import diagnostic_dicts, validate_constraint_envelope


    FORBIDDEN_CLAIMS = {
        "certification",
        "certified",
        "sealing",
        "sealed",
        "authentication",
        "code " + "compliant",
        "professional approval",
        "engineering acceptance",
    }


    def provenance(source_name="invented fixture"):
        return {
            "source_name": source_name,
            "source_location": f"fixtures/{source_name.replace(' ', '_')}",
            "source_license": "invented test fixture",
            "contributor": "DEL-13-03 test",
            "contributor_certification": "invented non-engineering validation fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "pending",
            "privacy_classification": "invented_public_example",
        }


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def quantity(value=1.0, unit="m", dimension="length"):
        return {
            "value": value,
            "unit": unit,
            "dimension": dimension,
            "provenance": provenance("quantity source"),
        }


    def parameter(parameter_id="param:length", value=None):
        return {
            "parameter_id": parameter_id,
            "name": parameter_id,
            "value": quantity() if value is None else value,
            "value_kind": "quantity",
            "provenance": provenance("parameter source"),
        }


    def design_record(record_id, record_kind="requirement", requirement_type="clearance"):
        if record_kind == "zone":
            return {
                "id": record_id,
                "record_kind": "zone",
                "name": record_id,
                "zone_type": "no_go_volume",
                "geometry": {
                    "geometry_kind": "abstract_reference",
                    "coordinate_refs": [],
                    "boundary_refs": [],
                    "quantities": [quantity()],
                },
                "source_notes": [],
                "assumptions": [],
                "provenance": provenance(f"{record_id} source"),
            }
        return {
            "id": record_id,
            "record_kind": "requirement",
            "name": record_id,
            "requirement_type": requirement_type,
            "target_refs": [ref("Component", "C-1")],
            "requirement_statement": "Invented fixture requirement.",
            "parameters": [parameter()],
            "source_notes": [],
            "assumptions": [],
            "provenance": provenance(f"{record_id} source"),
        }


    def design_knowledge():
        records = [
            design_record("DK-clearance", requirement_type="clearance"),
            design_record("DK-slope", requirement_type="slope"),
            design_record("DK-access", requirement_type="access"),
            design_record("DK-zone", record_kind="zone"),
            {
                "id": "DK-equipment",
                "record_kind": "equipment_interface",
                "name": "equipment interface",
                "equipment_ref": ref("Component", "EQ-1"),
                "interface_role": "terminal_point",
                "location": {"x": quantity(), "y": quantity(), "z": quantity()},
                "interface_parameters": [parameter()],
                "source_notes": [],
                "assumptions": [],
                "provenance": provenance("equipment source"),
            },
        ]
        return {
            "schema_version": "0.1.0",
            "deliverable_id": "DEL-13-01",
            "package_id": "PKG-13",
            "scope_item": "SOW-067",
            "objectives": ["OBJ-014"],
            "data_boundary": {
                "public_examples_policy": "invented_or_cleared_data_only",
                "protected_source_policy": "no_bundled_protected_owner_or_standards_data",
                "private_data_policy": "user_controlled_private_paths",
                "unit_policy": "unit_bearing_values_require_explicit_unit_metadata",
                "professional_boundary": professional_boundary(),
            },
            "design_knowledge": {
                "knowledge_set_id": "DKS-1",
                "project_ref": ref("Project", "P-1"),
                "model_ref": ref("Model", "M-1"),
                "records": records,
                "diagnostics": [],
                "provenance": provenance("knowledge source"),
            },
        }


    def constraint_record(kind, design_refs=None, parameters=None, targets=None, status="schema_validated"):
        return {
            "constraint_id": f"C-{kind}",
            "constraint_kind": kind,
            "name": f"{kind} constraint",
            "state": "active",
            "source_type": "user",
            "target_refs": targets if targets is not None else [ref("Component", f"target-{kind}")],
            "design_knowledge_refs": design_refs if design_refs is not None else [],
            "parameters": parameters if parameters is not None else [],
            "diagnostics": [],
            "assumptions": [],
            "validation_status": status,
            "provenance": provenance(f"{kind} source"),
            "professional_boundary": professional_boundary(),
        }


    def constraint_envelope():
        constraints = [
            constraint_record(
                "connectivity",
                targets=[ref("Node", "N-1"), ref("Node", "N-2")],
                status="conflict_detected",
            ),
            constraint_record("clearance", design_refs=[ref("DesignKnowledgeRecord", "DK-clearance")], parameters=[parameter()]),
            constraint_record("no_go_volume", design_refs=[ref("DesignKnowledgeRecord", "DK-zone")]),
            constraint_record("support_zone", design_refs=[ref("DesignKnowledgeRecord", "DK-zone")]),
            constraint_record("route_conflict", design_refs=[ref("DesignKnowledgeRecord", "DK-zone")]),
            constraint_record("slope", design_refs=[ref("DesignKnowledgeRecord", "DK-slope")], parameters=[parameter()]),
            constraint_record("drain", design_refs=[ref("DesignKnowledgeRecord", "DK-slope")], parameters=[parameter()]),
            constraint_record("vent", design_refs=[ref("DesignKnowledgeRecord", "DK-slope")], parameters=[parameter()]),
            constraint_record("access", design_refs=[ref("DesignKnowledgeRecord", "DK-access")], parameters=[parameter()]),
            constraint_record("equipment_interface", design_refs=[ref("DesignKnowledgeRecord", "DK-equipment")]),
            constraint_record("missing_required_data", status="missing_data"),
        ]
        return {
            "schema_version": "0.1.0",
            "deliverable_id": "DEL-13-02",
            "package_id": "PKG-13",
            "scope_items": ["SOW-067", "SOW-068"],
            "objectives": ["OBJ-014", "OBJ-018"],
            "data_boundary": {
                "public_examples_policy": "invented_or_cleared_data_only",
                "protected_source_policy": "no_bundled_protected_owner_or_standards_data",
                "private_data_policy": "user_controlled_private_paths",
                "unit_policy": "unit_bearing_values_require_explicit_unit_metadata",
                "engineering_authority": "human_review_required_outside_software",
            },
            "constraint_set": {
                "constraint_set_id": "CS-1",
                "project_ref": ref("Project", "P-1"),
                "model_ref": ref("Model", "M-1"),
                "design_knowledge_refs": [ref("DesignKnowledgeRecord", "DK-clearance")],
                "constraints": constraints,
                "diagnostics": [],
                "provenance": provenance("constraint set source"),
                "professional_boundary": professional_boundary(),
            },
        }


    def codes(result):
        return {item["code"] for item in diagnostic_dicts(result)}


    def classes(result):
        return {item["class"] for item in diagnostic_dicts(result)}


    def test_validation_is_deterministic_and_covers_represented_classes():
        constraints = constraint_envelope()
        knowledge = design_knowledge()

        first = diagnostic_dicts(validate_constraint_envelope(constraints, knowledge))
        second = diagnostic_dicts(validate_constraint_envelope(deepcopy(constraints), deepcopy(knowledge)))

        assert first == second
        assert {
            "CONNECTIVITY_CONFLICT",
            "CLEARANCE_CONFLICT",
            "ROUTE_CONFLICT",
            "SUPPORT_ZONE_CONFLICT",
            "SLOPE_DRAIN_VENT_CONFLICT",
            "CONSTRAINT_MISSING_DATA",
            "SCHEMA_VALIDATION",
        } <= {item["class"] for item in first}
        assert any(item["code"] == "CV-EQUIPMENT-INTERFACE-AVAILABLE" for item in first)
        assert any(item["code"] == "CV-ACCESS-AVAILABLE" for item in first)


    def test_missing_data_and_unresolved_references_are_explicit_findings():
        constraints = constraint_envelope()
        broken = constraint_record(
            "clearance",
            design_refs=[ref("DesignKnowledgeRecord", "DK-missing")],
            parameters=[],
            targets=[],
        )
        broken.pop("provenance")
        constraints["constraint_set"]["constraints"] = [broken]

        result = validate_constraint_envelope(constraints, design_knowledge())

        assert {
            "CV-CONSTRAINT-MISSING-FIELD",
            "CV-CLEARANCE-TARGETS-MISSING",
            "CV-CLEARANCE-PARAMETERS-MISSING",
            "CV-DESIGN-REF-UNRESOLVED",
            "CV-CONSTRAINT-PROVENANCE-MISSING",
        } <= codes(result)
        assert result.has_blocking_findings


    def test_unit_metadata_is_checked_without_conversion_or_tolerance():
        constraints = constraint_envelope()
        bad_quantity = {"value": 25.0, "unit": "", "dimension": "TBD", "provenance": provenance("bad quantity")}
        constraints["constraint_set"]["constraints"] = [
            constraint_record("slope", design_refs=[ref("DesignKnowledgeRecord", "DK-slope")], parameters=[parameter(value=bad_quantity)])
        ]

        result = validate_constraint_envelope(constraints, design_knowledge())
        unit_diagnostics = [item for item in diagnostic_dicts(result) if item["class"] == "UNIT_WARNING"]

        assert any(item["code"] == "CV-UNIT-METADATA-MISSING" for item in unit_diagnostics)
        joined = "\n".join(item["message"] + "\n" + item["remediation"] for item in unit_diagnostics).lower()
        assert "does not convert units" in joined
        assert "invent tolerances" in joined


    def test_quantity_dimensions_are_checked_against_pkg02_vocabulary():
        constraints = constraint_envelope()
        accepted = constraint_record(
            "slope",
            design_refs=[ref("DesignKnowledgeRecord", "DK-slope")],
            parameters=[parameter(value=quantity(0.01, "m/m", "slope"))],
        )
        retired = constraint_record(
            "access",
            design_refs=[ref("DesignKnowledgeRecord", "DK-access")],
            parameters=[parameter(value=quantity(1.0, "N/m", "stiffness"))],
        )
        constraints["constraint_set"]["constraints"] = [accepted, retired]

        result = validate_constraint_envelope(constraints, design_knowledge())
        dimension_diagnostics = [
            item
            for item in diagnostic_dicts(result)
            if item["code"] == "CV-UNIT-DIMENSION-UNKNOWN"
        ]

        assert len(dimension_diagnostics) == 1
        assert "stiffness" in dimension_diagnostics[0]["message"]
        assert "slope" not in "\n".join(item["message"] for item in dimension_diagnostics)
        assert result.has_blocking_findings


    def test_protected_or_private_provenance_is_preserved_as_boundary_diagnostic():
        constraints = constraint_envelope()
        constraints["constraint_set"]["constraints"][0]["provenance"]["redistribution_status"] = "protected_suspected"
        constraints["constraint_set"]["constraints"][0]["provenance"]["privacy_classification"] = "private_project_data"

        result = validate_constraint_envelope(constraints, design_knowledge())

        assert "IP_BOUNDARY_WARNING" in classes(result)
        protected = [
            item
            for item in diagnostic_dicts(result)
            if item["code"] in {"CV-CONSTRAINT-PROVENANCE-REDISTRIBUTION-REVIEW", "CV-CONSTRAINT-PROVENANCE-PRIVACY-REVIEW"}
        ]
        assert protected
        assert all(item["source_references"] for item in protected)


    def test_output_text_does_not_make_prohibited_authority_claims():
        result = validate_constraint_envelope(constraint_envelope(), design_knowledge())
        text = "\n".join(
            f"{item['code']} {item['message']} {item['remediation']}"
            for item in diagnostic_dicts(result)
        ).lower()

        for forbidden in FORBIDDEN_CLAIMS:
            assert forbidden not in text


    if __name__ == "__main__":
        test_validation_is_deterministic_and_covers_represented_classes()
        test_missing_data_and_unresolved_references_are_explicit_findings()
        test_unit_metadata_is_checked_without_conversion_or_tolerance()
        test_quantity_dimensions_are_checked_against_pkg02_vocabulary()
        test_protected_or_private_provenance_is_preserved_as_boundary_diagnostic()
        test_output_text_does_not_make_prohibited_authority_claims()

## Component: tests/test_coordination_maintenance.py

    from __future__ import annotations

    import importlib.util
    import subprocess
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    MODULE_PATH = ROOT / "tools" / "coordination" / "list_deliverable_status.py"


    def load_module():
        spec = importlib.util.spec_from_file_location("list_deliverable_status", MODULE_PATH)
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module


    def write_status(root: Path, package: str, folder: str, state: str) -> Path:
        deliverable_dir = root / "execution" / package / "1_Working" / folder
        deliverable_dir.mkdir(parents=True)
        status_path = deliverable_dir / "_STATUS.md"
        deliverable_id = folder.split("_", maxsplit=1)[0]
        status_path.write_text(
            "\n".join(
                [
                    f"# Status: {deliverable_id}",
                    "",
                    f"**Current State:** {state}",
                    "**Last Updated:** 2026-06-03",
                    "",
                    "## History",
                    f"- 2026-06-03 - Fixture state set to {state}.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        return status_path


    def write_fixture_repo(root: Path) -> None:
        (root / "execution/_DAG/DAG-006").mkdir(parents=True)
        (root / "execution/_DAG/_LATEST.md").write_text(
            "- Approved graph authority: `execution/_DAG/DAG-006/`\n",
            encoding="utf-8",
        )
        (root / "execution/_DAG/DAG-006/DeliverableNodes.csv").write_text(
            "\n".join(
                [
                    "NodeID,PackageID,DeliverableID,DeliverableName,DeliverableType,ScopeItems,Objectives,ContextEnvelope,ExecutionPath,ContextPath,DependenciesPath,HasFourDocumentKit,HasSemanticMatrix,HasSemanticLensing,HasReview,SourceRegister,Notes",
                    "DEL-00-01,PKG-00,DEL-00-01,Architecture baseline,DOC,SOW,OBJ,M,execution/PKG-00_Runway/1_Working/DEL-00-01_Architecture baseline,context,deps,TRUE,TRUE,TRUE,FALSE,register,",
                    "DEL-01-01,PKG-01,DEL-01-01,Governance,DOC,SOW,OBJ,M,execution/PKG-01_Governance/1_Working/DEL-01-01_Governance,context,deps,TRUE,TRUE,TRUE,FALSE,register,",
                    "DEL-02-01,PKG-02,DEL-02-01,Domain schema,DOC,SOW,OBJ,M,execution/PKG-02_Domain/1_Working/DEL-02-01_Domain schema,context,deps,TRUE,TRUE,TRUE,FALSE,register,",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        write_status(root, "PKG-00_Runway", "DEL-00-01_Architecture baseline", "SEMANTIC_READY")
        write_status(root, "PKG-01_Governance", "DEL-01-01_Governance", "IN_PROGRESS")
        write_status(root, "PKG-02_Domain", "DEL-02-01_Domain schema", "CHECKING")


    def test_discovers_local_status_and_dag_context(tmp_path):
        tool = load_module()
        write_fixture_repo(tmp_path)

        discovered = tool.discover_statuses(tmp_path)
        output_rows = tool.rows(tmp_path, "DAG-006", discovered)

        by_id = {row["DeliverableID"]: row for row in output_rows}
        assert set(by_id) == {"DEL-00-01", "DEL-01-01", "DEL-02-01"}
        assert by_id["DEL-01-01"]["LocalStatus"] == "IN_PROGRESS"
        assert by_id["DEL-02-01"]["DAGNodePresent"] == "TRUE"
        assert by_id["DEL-00-01"]["StatusVocabulary"] == "NONSTANDARD_TOLERATED"


    def test_filters_statuses_without_hiding_inventory_by_default(tmp_path):
        tool = load_module()
        write_fixture_repo(tmp_path)

        output_rows = tool.rows(tmp_path, "DAG-006", tool.discover_statuses(tmp_path))
        filtered = tool.filter_rows(output_rows, {"IN_PROGRESS"}, exclude_issued=False)

        assert len(output_rows) == 3
        assert len(filtered) == 1
        assert filtered[0]["DeliverableID"] == "DEL-01-01"


    def test_live_status_discovery_command_passes():
        completed = subprocess.run(
            [
                sys.executable,
                "tools/coordination/list_deliverable_status.py",
                "--dag",
                "DAG-006",
                "--format",
                "csv",
                "--summary",
            ],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        assert completed.returncode == 0, completed.stderr
        assert "DeliverableID,PackageID,DeliverableName,LocalStatus" in completed.stdout
        assert "Rows:" in completed.stderr

## Component: tests/test_design_authoring_comparison_workspace.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-08 design-authoring and comparison workspace."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.comparison.analysis_run.engine import compare_analysis_runs  # noqa: E402
    from core.comparison.model_state.engine import compare_model_states  # noqa: E402
    from core.constraints.validation.engine import validate_constraint_envelope  # noqa: E402
    from core.gui.design_workspace import (  # noqa: E402
        build_design_authoring_comparison_workspace,
        canonical_json,
    )
    from core.gui.warnings import build_warning_ux_contract  # noqa: E402
    from core.model_operations.audit_trail import record_operation_audit_trail  # noqa: E402
    from core.model_operations.validation_preview import validate_and_preview_operations  # noqa: E402


    FORBIDDEN_CLAIMS = {
        "code compliant",
        "certified",
        "sealed",
        "authenticated",
        "professional approval",
        "engineering acceptance",
        "external validation",
    }

    OPERATION_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_operation_set_valid.json"
    MODEL_STATE_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_accepted_model_state.json"


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def provenance():
        return {
            "source_name": "invented public test fixture",
            "source_location": "tests/test_design_authoring_comparison_workspace.py",
            "source_license": "project-governed",
            "contributor": "OpenPipeStress test",
            "contributor_certification": "invented non-engineering fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "pending",
            "privacy_classification": "invented_public_example",
        }


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def design_knowledge():
        return {
            "schema_version": "0.1.0",
            "deliverable_id": "DEL-13-01",
            "package_id": "PKG-13",
            "scope_item": "SOW-067",
            "objectives": ["OBJ-014"],
            "data_boundary": {
                "public_examples_policy": "invented_or_cleared_data_only",
                "protected_source_policy": "no_bundled_protected_owner_or_standards_data",
                "private_data_policy": "user_controlled_private_paths",
                "unit_policy": "unit_bearing_values_require_explicit_unit_metadata",
                "professional_boundary": professional_boundary(),
            },
            "design_knowledge": {
                "knowledge_set_id": "dk:invented",
                "project_ref": ref("Project", "project:invented"),
                "model_ref": ref("Model", "model:invented"),
                "records": [
                    {
                        "id": "dk:line:1",
                        "record_kind": "line_data",
                        "name": "Invented public line",
                        "line_identifier": "L-invented",
                        "service": "TBD",
                        "attributes": [],
                        "source_notes": [],
                        "assumptions": [
                            {
                                "assumption_id": "assumption:line-service",
                                "statement": "Invented service remains unresolved.",
                                "status": "unresolved",
                                "affected_refs": [ref("DesignKnowledgeRecord", "dk:line:1")],
                                "provenance": provenance(),
                            }
                        ],
                        "provenance": provenance(),
                    },
                    {
                        "id": "dk:req:access",
                        "record_kind": "requirement",
                        "name": "Invented access note",
                        "requirement_type": "access",
                        "statement": "Invented review fixture, not project data.",
                        "parameters": [],
                        "source_notes": [],
                        "assumptions": [],
                        "provenance": provenance(),
                    },
                ],
                "diagnostics": [
                    {
                        "code": "DK-TBD-SERVICE",
                        "class": "TBD",
                        "severity": "warning",
                        "source": ref("DesignKnowledgeRecord", "dk:line:1"),
                        "affected_object": ref("DesignKnowledgeRecord", "dk:line:1"),
                        "message": "Invented line service is unresolved.",
                        "remediation": "Retain TBD until user-supplied data is available.",
                        "provenance": provenance(),
                    }
                ],
                "provenance": provenance(),
            },
        }


    def model_state(state_id, entities):
        return {
            "model_state": {
                "state_id": state_id,
                "state_name": f"Invented {state_id}",
                "state_kind": "comparison_basis",
                "created_at": "2026-05-09T00:00:00Z",
                "model_ref": ref("Model", "model:invented"),
                "parent_state_refs": [],
                "tags": [],
                "notes": [],
                "external_references": [],
                "unresolved_assumptions": [
                    {
                        "assumption_id": f"assumption:{state_id}",
                        "statement": "Invented unresolved state assumption.",
                        "status": "unresolved",
                        "affected_refs": [ref("ModelState", state_id)],
                        "provenance": provenance(),
                    }
                ],
                "warnings": [],
                "analysis_status": ["MODEL_INCOMPLETE"],
                "hashes": [
                    {
                        "algorithm": "sha256",
                        "canonicalization": "JCS",
                        "payload_ref": ref("ModelState", state_id),
                        "payload_scope": "model_state_record",
                        "value": f"hash-{state_id}",
                    }
                ],
                "immutability_policy": {
                    "snapshot_is_read_only": True,
                    "mutation_policy": "changes_create_new_model_state",
                    "new_state_required_for_change": True,
                    "hash_invalidates_external_acceptance": True,
                },
                "professional_boundary": professional_boundary(),
                "provenance": provenance(),
            },
            "entities": entities,
        }


    def entity(stable_id, **fields):
        return {
            "stable_id": stable_id,
            "category": "Component",
            "reference": {"object_type": "Entity", "ref": stable_id, "label": stable_id},
            **fields,
        }


    def run_record(run_id, model_state_id, result_ref):
        return {
            "analysis_run": {
                "run_id": run_id,
                "run_name": f"{run_id} invented fixture",
                "run_kind": "mechanics_solve",
                "created_at": "2026-05-09T00:00:00Z",
                "model_state_ref": ref("ModelState", model_state_id),
                "solver_version": {"solver_id": "invented-solver", "version": "0.0.0-fixture"},
                "settings_ref": ref("SolverSettings", f"settings:{run_id}"),
                "unit_system_ref": ref("UnitSystem", "fixture-units"),
                "load_basis_refs": [ref("LoadCase", "LC-1")],
                "diagnostics": [],
                "result_refs": [ref("ResultEnvelope", result_ref)],
                "rule_pack_refs": [],
                "library_refs": [],
                "hashes": [
                    {
                        "algorithm": "sha256",
                        "canonicalization": "JCS",
                        "payload_ref": ref("AnalysisRun", run_id),
                        "payload_scope": "analysis_run_record",
                        "value": f"hash-{run_id}",
                    }
                ],
                "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                "reproducibility": {
                    "input_manifest_refs": [],
                    "environment_refs": [],
                    "determinism_notes": ["invented deterministic fixture"],
                    "unresolved_tbd": [],
                },
            }
        }


    def result_envelope(envelope_id, run_id, result_id, magnitude, unit):
        return {
            "result_envelope": {
                "envelope_id": envelope_id,
                "run_ref": ref("AnalysisRun", run_id),
                "result_sets": [
                    {
                        "result_set_id": f"set:{envelope_id}",
                        "quantity_results": [
                            {
                                "result_id": result_id,
                                "family": "stress",
                                "object_ref": ref("PipeElement", "E1"),
                                "basis_ref": ref("LoadCase", "LC-1"),
                                "magnitude": magnitude,
                                "unit": unit,
                                "dimension": "stress",
                                "provenance": {"source_name": "invented fixture"},
                            }
                        ],
                    }
                ],
                "diagnostics": [],
            }
        }


    def operation_envelope():
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        operation = next(
            item
            for item in envelope["operation_set"]["operations"]
            if item["operation_id"] == "op:resize"
        )
        operation["operation_status"] = "ready_for_user_review"
        envelope["operation_set"]["operations"] = [operation]
        return envelope


    def accepted_model_state():
        with MODEL_STATE_FIXTURE.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def fixture_workspace_inputs(*, user_acceptance=False):
        left_state = model_state(
            "state:left",
            [
                entity("component:pipe-1", diameter={"value": 100.0, "unit": "mm", "dimension": "length"}),
                entity("component:left-only", note="left"),
            ],
        )
        right_state = model_state(
            "state:right",
            [
                entity("component:pipe-1", diameter={"value": 125.0, "unit": "mm", "dimension": "length"}),
                entity("component:right-only", note="right"),
            ],
        )
        preview = validate_and_preview_operations(operation_envelope(), accepted_model_state())
        acceptance_signal = {
            "decision": "accept",
            "accepted": True,
            "actor_type": "user" if user_acceptance else "agent",
            "actor_ref": "user:reviewer" if user_acceptance else "agent:assistant",
            "source_role": "project_user" if user_acceptance else "automation",
            "decided_at": "2026-05-09T12:00:00Z",
            "rationale": "Invented review signal for workspace test.",
        }
        audit = record_operation_audit_trail(
            operation_envelope(),
            validation_outcome=preview,
            diff_preview_ref={
                "object_type": "DiffPreview",
                "ref": "preview:resize",
                "hash": "sha256:invented-preview-001",
            },
            acceptance_signal=acceptance_signal,
            accepted_model_state=accepted_model_state(),
        )
        return {
            "workspace_id": "workspace:invented",
            "design_knowledge_envelope": design_knowledge(),
            "constraint_validation": validate_constraint_envelope(None),
            "warning_contract": build_warning_ux_contract(
                warning_set_id="warnings:invented",
                conditions=[
                    {
                        "warning_id": "warn:missing-support-stiffness",
                        "warning_class": "incomplete_data",
                        "target_ref": ref("Support", "support:TBD"),
                        "message": "Invented support stiffness remains TBD.",
                        "source_status": "missing",
                    }
                ],
            ),
            "model_states": [left_state, right_state],
            "analysis_runs": [
                run_record("run:left", "state:left", "results:left"),
                run_record("run:right", "state:right", "results:right"),
            ],
            "model_state_comparison": compare_model_states(left_state, right_state),
            "analysis_run_comparison": compare_analysis_runs(
                left_run=run_record("run:left", "state:left", "results:left"),
                right_run=run_record("run:right", "state:right", "results:right"),
                left_results=result_envelope("results:left", "run:left", "result:left:stress", 1000.0, "kPa"),
                right_results=result_envelope("results:right", "run:right", "result:right:stress", 1000500.0, "Pa"),
                mappings=[
                    {
                        "mapping_id": "map:stress:E1",
                        "mapping_status": "manual_match",
                        "left_ref": ref("Result", "result:left:stress"),
                        "right_ref": ref("Result", "result:right:stress"),
                        "normalized_unit": "Pa",
                    }
                ],
                tolerance_profile={
                    "tolerance_profile": {
                        "profile_id": "tol:invented",
                        "rules": [
                            {
                                "rule_id": "tol-rule:stress",
                                "result_family": "stress",
                                "dimension_id": "stress",
                                "unit_ref": ref("Unit", "Pa"),
                                "tolerance_value": 0.25,
                            }
                        ],
                    }
                },
                unit_conversions={("kPa", "Pa", "stress"): 1000.0},
                comparison_id="comparison:analysis",
            ),
            "tolerance_profile": {
                "tolerance_profile": {
                    "profile_id": "tol:invented",
                    "profile_status": "project_specific_review_required",
                    "rules": [{"rule_id": "tol-rule:stress"}],
                    "diagnostics": [],
                    "assumptions": [],
                    "hashes": [],
                    "review": {"status": "pending"},
                    "provenance": provenance(),
                }
            },
            "operation_preview": preview,
            "operation_audit": audit,
            "selected_refs": {"panel_id": "comparison_tables", "row_id": "component:pipe-1"},
        }


    def test_workspace_is_deterministic_and_preserves_review_records():
        inputs = fixture_workspace_inputs()
        first = build_design_authoring_comparison_workspace(**inputs)
        second = build_design_authoring_comparison_workspace(**deepcopy(inputs))

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-07-08"
        assert first["workspace_hash"].startswith("sha256:")
        assert first["design_knowledge_panel"]["summary"]["record_count"] == 2
        assert first["design_knowledge_panel"]["summary"]["records_with_unresolved_tbd"] == 1
        assert first["constraint_warning_panel"]["warnings"][0]["warning_class"] == "incomplete_data"
        assert first["state_run_browser"]["summary"]["model_state_count"] == 2
        assert first["comparison_tables"]["model_state_rows"]["unmatched_rows"]
        assert first["comparison_tables"]["analysis_run_rows"]["result_rows"][0]["tolerance_profile_ref"] == "tol:invented"
        assert first["graphical_overlays"]["overlays"]
        assert first["mutation_boundary"]["workspace_mutates_accepted_model_state"] is False
        assert first["persistence_hash_contract"]["contract_ref"] == "DEL-02-05"
        assert first["state_run_browser"]["persistence_hash_boundary"]["model_state_hashes_present"] is True
        assert first["state_run_browser"]["persistence_hash_boundary"]["analysis_run_hashes_present"] is True
        assert first["state_run_browser"]["model_states"][0]["hash_boundary"]["hashes_present"] is True


    def test_operation_review_requires_explicit_user_acceptance_record():
        without_user = build_design_authoring_comparison_workspace(**fixture_workspace_inputs(user_acceptance=False))
        row = without_user["operation_diff_review"]["rows"][0]

        assert row["can_be_represented_as_accepted_operation"] is False
        assert row["review_state"] == "held_for_user_acceptance"
        assert row["accepted_model_state_mutated_by_workspace"] is False

        with_user = build_design_authoring_comparison_workspace(**fixture_workspace_inputs(user_acceptance=True))
        row = with_user["operation_diff_review"]["rows"][0]

        assert row["can_be_represented_as_accepted_operation"] is True
        assert row["review_state"] == "explicit_user_acceptance_recorded"
        assert row["workspace_application_status"] == "not_applied"


    def test_missing_inputs_and_mutation_signals_remain_visible():
        missing = build_design_authoring_comparison_workspace(workspace_id="workspace:missing")

        assert missing["review_state_routing"]["route_state"] == "input_unavailable_review"
        assert "design_knowledge" in missing["review_state_routing"]["unavailable_panel_ids"]
        assert "WORKSPACE-DESIGN-KNOWLEDGE-MISSING" in {item["code"] for item in missing["diagnostics"]}

        inputs = fixture_workspace_inputs()
        unsafe_preview = deepcopy(inputs["operation_preview"])
        unsafe_preview["diff_preview"][0]["application_status"] = "applied"
        inputs["operation_preview"] = unsafe_preview
        output = build_design_authoring_comparison_workspace(**inputs)

        assert "WORKSPACE-OPERATION-MUTATION-SIGNAL-BLOCKED" in {item["code"] for item in output["diagnostics"]}
        assert output["operation_diff_review"]["rows"][0]["workspace_application_status"] == "not_applied"


    def test_output_boundary_language_does_not_make_prohibited_claims():
        output = build_design_authoring_comparison_workspace(**fixture_workspace_inputs())
        text = canonical_json(output).lower()

        for forbidden in FORBIDDEN_CLAIMS:
            assert forbidden not in text
        assert output["professional_boundary"]["software_makes_approval_claim"] is False


    def main():
        test_workspace_is_deterministic_and_preserves_review_records()
        test_operation_review_requires_explicit_user_acceptance_record()
        test_missing_inputs_and_mutation_signals_remain_visible()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_design_knowledge_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the design knowledge schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "design_knowledge.schema.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "data_boundary",
        "design_knowledge",
    }

    REQUIRED_DEFS = {
        "AssumptionRecord",
        "Coordinate3",
        "DataBoundary",
        "DesignKnowledgeEnvelope",
        "Diagnostic",
        "EndpointRecord",
        "EquipmentInterfaceRecord",
        "GeometryPayload",
        "Id",
        "LineDataRecord",
        "MetadataRecord",
        "Parameter",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "Quantity",
        "RedistributionStatus",
        "Reference",
        "RequirementRecord",
        "ReviewStatus",
        "RoutingCorridorRecord",
        "SourceNote",
        "ZoneRecord",
    }

    RECORD_DEFS = {
        "EndpointRecord": "endpoint",
        "LineDataRecord": "line_data",
        "RoutingCorridorRecord": "routing_corridor",
        "ZoneRecord": "zone",
        "EquipmentInterfaceRecord": "equipment_interface",
        "RequirementRecord": "requirement",
        "MetadataRecord": "owner_project_metadata",
    }

    REQUIRED_REQUIREMENT_TYPES = {
        "access",
        "slope",
        "drain",
        "vent",
        "clearance",
        "support",
        "owner_project_metadata",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "allowable stress table",
        "stress intensification factor table",
        "B31J",
        "real secret",
        "code compliant",
        "certified",
        "sealed",
        "professional approval by the software",
    }

    ACCEPTED_PKG02_DIMENSIONS = {
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-13-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-13"
        assert schema["properties"]["scope_item"]["const"] == "SOW-067"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-014"

        boundary = defs["DataBoundary"]["properties"]
        assert boundary["public_examples_policy"]["const"] == "invented_or_cleared_data_only"
        assert (
            boundary["protected_source_policy"]["const"]
            == "no_bundled_protected_owner_or_standards_data"
        )
        assert (
            boundary["unit_policy"]["const"]
            == "unit_bearing_values_require_explicit_unit_metadata"
        )

        envelope_required = required_at(schema, "DesignKnowledgeEnvelope")
        assert {
            "knowledge_set_id",
            "project_ref",
            "model_ref",
            "records",
            "diagnostics",
            "provenance",
        } <= envelope_required

        for definition_name, record_kind in RECORD_DEFS.items():
            required = required_at(schema, definition_name)
            assert {"id", "record_kind", "name", "source_notes", "assumptions", "provenance"} <= required
            assert defs[definition_name]["properties"]["record_kind"]["const"] == record_kind

        assert {
            "start",
            "end",
            "tie_in",
            "equipment_interface",
            "boundary_condition",
        } <= set(defs["EndpointRecord"]["properties"]["endpoint_role"]["enum"])

        assert {
            "no_go_volume",
            "supportable_zone",
            "access_zone",
            "maintenance_zone",
            "operating_zone",
        } <= set(defs["ZoneRecord"]["properties"]["zone_type"]["enum"])
        assert REQUIRED_REQUIREMENT_TYPES <= set(
            defs["RequirementRecord"]["properties"]["requirement_type"]["enum"]
        )

        provenance_required = required_at(schema, "Provenance")
        assert {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
            "privacy_classification",
        } <= provenance_required
        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "invented_non_engineering_example",
        } <= enum_at(schema, "RedistributionStatus")
        assert {
            "public_metadata",
            "invented_public_example",
            "private_project_data",
            "owner_project_metadata_private",
            "protected_suspected",
            "redacted",
        } <= enum_at(schema, "PrivacyClassification")

        assert {"value", "unit", "dimension", "provenance"} <= required_at(
            schema, "Quantity"
        )
        dimensions = set(defs["Quantity"]["properties"]["dimension"]["enum"])
        assert dimensions == ACCEPTED_PKG02_DIMENSIONS
        assert "temperature_difference" not in dimensions
        assert "area_moment" not in dimensions
        assert "stiffness" not in dimensions

        professional = defs["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings


    if __name__ == "__main__":
        main()

## Component: tests/test_evidence_sweep.py

    """Focused tests for the DEC-025 five-surface evidence sweep entrypoint."""

    from __future__ import annotations

    import importlib.util
    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    MODULE_PATH = ROOT / "tools" / "release" / "run_evidence_sweep.py"

    EXPECTED_SURFACE_ORDER = [
        "cargo_crate_sweep",
        "python_pytest",
        "desktop_vitest",
        "desktop_playwright_e2e",
        "desktop_production_build",
    ]


    def load_module():
        spec = importlib.util.spec_from_file_location("run_evidence_sweep", MODULE_PATH)
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module


    def test_plan_is_the_five_surfaces_in_dec025_order():
        sweep = load_module()
        surfaces = sweep.build_sweep_plan()

        assert [surface.surface_id for surface in surfaces] == EXPECTED_SURFACE_ORDER


    def test_wasm_engine_build_precedes_vitest():
        sweep = load_module()
        vitest = next(
            surface
            for surface in sweep.build_sweep_plan()
            if surface.surface_id == "desktop_vitest"
        )
        commands = [" ".join(command) for command in vitest.commands]

        assert commands == ["npm run build:wasm:desktop", "npm run test:desktop"]


    def test_plan_uses_local_commands_only():
        sweep = load_module()
        for surface in sweep.build_sweep_plan():
            for command in surface.commands:
                assert isinstance(command, tuple)
                assert command[0] in (sys.executable, "npm")


    def test_cargo_surface_reuses_release_readiness_cargo_profile():
        sweep = load_module()
        cargo = sweep.build_sweep_plan()[0]

        assert cargo.commands == (
            (
                sys.executable,
                "tools/release/check_release_readiness.py",
                "--profile",
                "cargo",
                "--execute",
            ),
        )


    def test_summary_binds_commit_hash_and_passes_when_all_surfaces_pass():
        sweep = load_module()

        summary = sweep.run_sweep(sweep.build_sweep_plan(), ROOT, runner=lambda c, r: 0)

        assert summary["artifact"] == "openpipestress.evidence_sweep_summary"
        assert summary["schema_version"] == 2
        assert summary["decision_basis"] == "DEC-025"
        git_state = summary["git"]
        assert git_state["commit_hash"] and len(git_state["commit_hash"]) == 40
        assert git_state["status_capture_failed"] is False
        assert isinstance(git_state["working_tree_dirty"], bool)
        assert summary["overall_status"] == "pass"
        assert [entry["surface_id"] for entry in summary["surfaces"]] == (
            EXPECTED_SURFACE_ORDER
        )
        assert all(entry["status"] == "pass" for entry in summary["surfaces"])
        assert all(
            command["exit_code"] == 0
            for entry in summary["surfaces"]
            for command in entry["commands"]
        )


    def test_parse_porcelain_status_keeps_full_path_for_unstaged_first_record():
        sweep = load_module()
        porcelain = " M projects/chirality-piping/init/init-prompt.md\0"

        assert sweep.parse_porcelain_status(porcelain) == [
            "projects/chirality-piping/init/init-prompt.md"
        ]


    def test_parse_porcelain_status_handles_rename_untracked_and_staged_records():
        sweep = load_module()
        porcelain = (
            "R  docs/renamed.md\0docs/original.md\0"
            " M tools/release/run_evidence_sweep.py\0"
            "?? validation/evidence/sweeps/SWEEP_new.json\0"
            "A  tests/test_new.py\0"
        )

        assert sweep.parse_porcelain_status(porcelain) == [
            "docs/original.md",
            "docs/renamed.md",
            "tests/test_new.py",
            "tools/release/run_evidence_sweep.py",
            "validation/evidence/sweeps/SWEEP_new.json",
        ]


    def test_collect_git_state_does_not_strip_leading_space_from_dirty_paths(
        monkeypatch,
    ):
        """Regression: a stripped ` M <path>` capture cut the first path char."""
        sweep = load_module()

        class FakeCompleted:
            def __init__(self, stdout):
                self.returncode = 0
                self.stdout = stdout

        def fake_run(command, cwd=None, capture_output=False, text=False, check=False):
            if "status" in command:
                assert "-z" in command
                return FakeCompleted(
                    " M projects/chirality-piping/init/init-prompt.md\0"
                )
            if "--abbrev-ref" in command:
                return FakeCompleted("main\n")
            return FakeCompleted("a" * 40 + "\n")

        monkeypatch.setattr(sweep.subprocess, "run", fake_run)

        state = sweep.collect_git_state(ROOT)

        assert state["commit_hash"] == "a" * 40
        assert state["branch"] == "main"
        assert state["working_tree_dirty"] is True
        assert state["dirty_paths"] == [
            "projects/chirality-piping/init/init-prompt.md"
        ]


    def test_sweep_fails_fast_and_marks_later_surfaces_not_run():
        sweep = load_module()

        def failing_pytest(command, root):
            return 1 if "pytest" in command else 0

        summary = sweep.run_sweep(
            sweep.build_sweep_plan(), ROOT, runner=failing_pytest
        )

        statuses = {
            entry["surface_id"]: entry["status"] for entry in summary["surfaces"]
        }
        assert summary["overall_status"] == "fail"
        assert statuses["cargo_crate_sweep"] == "pass"
        assert statuses["python_pytest"] == "fail"
        assert statuses["desktop_vitest"] == "not_run"
        assert statuses["desktop_playwright_e2e"] == "not_run"
        assert statuses["desktop_production_build"] == "not_run"
        not_run = [e for e in summary["surfaces"] if e["status"] == "not_run"]
        assert all(entry["commands"] == [] for entry in not_run)


    def test_failing_command_stops_its_surface():
        sweep = load_module()

        def failing_wasm_build(command, root):
            return 1 if "build:wasm:desktop" in command else 0

        summary = sweep.run_sweep(
            sweep.build_sweep_plan(), ROOT, runner=failing_wasm_build
        )

        vitest = next(
            entry
            for entry in summary["surfaces"]
            if entry["surface_id"] == "desktop_vitest"
        )
        assert vitest["status"] == "fail"
        assert [command["argv"][-1] for command in vitest["commands"]] == [
            "build:wasm:desktop"
        ]


    def test_summary_filename_binds_commit_and_dirty_state():
        sweep = load_module()
        summary = {
            "git": {"commit_hash": "a" * 40, "working_tree_dirty": True},
            "started_utc": "2026-06-11T22:30:05+00:00",
        }

        assert (
            sweep.summary_filename(summary)
            == "SWEEP_20260611T223005Z_aaaaaaaaaaaa-dirty.json"
        )


    def test_collect_git_state_records_capture_failure_explicitly(monkeypatch):
        """Regression: a failed `git status` capture must never read as clean."""
        sweep = load_module()

        class FakeCompleted:
            def __init__(self, stdout, returncode=0):
                self.returncode = returncode
                self.stdout = stdout

        def fake_run(command, cwd=None, capture_output=False, text=False, check=False):
            if "status" in command:
                return FakeCompleted("", returncode=128)
            if "--abbrev-ref" in command:
                return FakeCompleted("main\n")
            return FakeCompleted("a" * 40 + "\n")

        monkeypatch.setattr(sweep.subprocess, "run", fake_run)

        state = sweep.collect_git_state(ROOT)

        assert state["status_capture_failed"] is True
        assert state["working_tree_dirty"] is None
        assert state["dirty_paths"] == []
        assert sweep.git_state_unverified(state) is True


    def test_summary_filename_marks_unverified_git_state():
        sweep = load_module()
        summary = {
            "git": {
                "commit_hash": "a" * 40,
                "status_capture_failed": True,
                "working_tree_dirty": None,
            },
            "started_utc": "2026-06-11T22:30:05+00:00",
        }

        assert (
            sweep.summary_filename(summary)
            == "SWEEP_20260611T223005Z_aaaaaaaaaaaa-gitunverified.json"
        )


    def test_write_summary_emits_valid_json(tmp_path):
        sweep = load_module()
        summary = sweep.run_sweep(sweep.build_sweep_plan(), ROOT, runner=lambda c, r: 0)

        output_path = sweep.write_summary(summary, tmp_path)

        parsed = json.loads(output_path.read_text(encoding="utf-8"))
        assert parsed["overall_status"] == "pass"
        assert parsed["git"]["commit_hash"] == summary["git"]["commit_hash"]


    def test_main_dry_run_prints_plan_without_executing(monkeypatch, capsys):
        sweep = load_module()

        def fail_run_sweep(*args, **kwargs):
            raise AssertionError("dry-run must not execute the sweep")

        monkeypatch.setattr(sweep, "run_sweep", fail_run_sweep)

        result = sweep.main(["--repo-root", str(ROOT)])
        captured = capsys.readouterr()

        assert result == 0
        assert "evidence sweep (dry-run)" in captured.out
        assert "surfaces (sequential, F-4-safe order): 5" in captured.out


    def test_main_execute_writes_summary_and_returns_failure_exit(
        monkeypatch, capsys, tmp_path
    ):
        sweep = load_module()

        monkeypatch.setattr(
            sweep, "run_command", lambda command, root: 1 if "pytest" in command else 0
        )

        result = sweep.main(
            [
                "--execute",
                "--repo-root",
                str(ROOT),
                "--output-dir",
                str(tmp_path),
            ]
        )
        captured = capsys.readouterr()

        assert result == 1
        summaries = list(Path(tmp_path).glob("SWEEP_*.json"))
        assert len(summaries) == 1
        parsed = json.loads(summaries[0].read_text(encoding="utf-8"))
        assert parsed["overall_status"] == "fail"
        assert "overall: fail" in captured.out

## Component: tests/test_export_adapter_sdk.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-09 export adapter SDK admission packages."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.export_adapter_sdk import (  # noqa: E402
        build_export_adapter_sdk_package,
        canonical_json,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "export_adapter_sdk.schema.json"
    PACKAGE_FIXTURE_PATH = ROOT / "fixtures" / "export_adapter_sdk" / "invented" / "export_adapter_sdk_package.json"
    SOURCE_PAYLOAD_PATH = ROOT / "fixtures" / "export_adapter_sdk" / "invented" / "source_adapter_sdk_payload.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
        "compatible with",
        "vendor-compatible",
    }


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def source_payload() -> dict[str, object]:
        return load_json(SOURCE_PAYLOAD_PATH)


    def build_from_source() -> dict[str, object]:
        return build_export_adapter_sdk_package(**source_payload())


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(PACKAGE_FIXTURE_PATH)
        built = build_from_source()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(PACKAGE_FIXTURE_PATH),
            )
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_export_adapter_sdk_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_package_members():
        first = build_from_source()
        second = build_from_source()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-09"
        assert first["package_status"] == "export_adapter_sdk_foundation"
        assert first["adapter_contract"]["runtime_grant_policy"] == "denied_by_default"
        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "target_registry",
            "adapter_contract",
            "validation_checklist",
            "validation_report",
            "diagnostics",
        }
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_target_registry_records_non_gating_candidate_and_checklist_categories():
        package = build_from_source()
        target = package["target_registry"][0]

        assert target["admission_state"] == "candidate_non_gating"
        assert target["target_version_basis"] == "tbd"
        assert target["runtime_grant_policy"] == "denied_by_default"
        assert {item["loss_category"] for item in target["behavior_families"]} == {"tbd", "unsupported"}
        assert {item["category"] for item in package["validation_checklist"]} == {
            "source_basis",
            "target_version",
            "units_coordinates",
            "stable_identity",
            "loss_report",
            "diagnostics",
            "privacy_screening",
            "export_review",
            "human_review",
        }


    def test_runtime_grants_are_denied_by_default():
        package = build_from_source()
        grants = {item["grant_type"]: item for item in package["runtime_grants"]}

        assert set(grants) == {
            "filesystem",
            "network",
            "process",
            "private_data",
            "storage",
            "rule_pack",
            "solver",
            "report_control",
        }
        assert all(item["requested"] is False for item in grants.values())
        assert all(item["decision"] == "denied_by_default" for item in grants.values())
        boundary = package["professional_boundary"]
        assert boundary["creates_runtime_loader"] is False
        assert boundary["creates_public_endpoint"] is False
        assert boundary["creates_external_target_claim"] is False
        assert boundary["creates_release_claim"] is False
        assert boundary["creates_professional_reliance_record"] is False


    def test_negative_cases_block_grants_missing_source_basis_and_missing_policies():
        payload = source_payload()
        payload["requested_runtime_grants"] = [
            {"grant_type": "network", "requested": True, "decision": "requested"}
        ]
        payload["target_registry"] = [deepcopy(payload["target_registry"][0])]
        payload["target_registry"][0]["source_basis_refs"] = []
        payload["target_registry"][0]["stable_id_policy"] = "tbd"
        payload["target_registry"][0]["loss_report_policy"] = "tbd"

        package = build_export_adapter_sdk_package(**payload)
        codes = {item["code"] for item in package["diagnostics"]}

        assert "EASDK-RUNTIME-GRANT-REQUESTED" in codes
        assert "EASDK-SOURCE-BASIS-MISSING" in codes
        assert "EASDK-TARGET-STABLE-ID-POLICY-MISSING" in codes
        assert "EASDK-TARGET-LOSS-REPORT-POLICY-MISSING" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_contract_and_admitted_target_source_basis_are_guarded():
        payload = source_payload()
        payload["adapter_contract"] = {"source_basis_refs": [{"object_type": "Deliverable", "ref": "DEL-17-02"}]}
        payload["target_registry"] = [deepcopy(payload["target_registry"][0])]
        payload["target_registry"][0]["admission_state"] = "source_basis_admitted"
        payload["target_registry"][0]["target_version_basis"] = "invented-target-v1"
        payload["target_registry"][0]["source_basis_refs"] = [
            {"object_type": "Deliverable", "ref": "DEL-17-01"},
            {"object_type": "Deliverable", "ref": "DEL-17-02"},
        ]

        package = build_export_adapter_sdk_package(**payload)
        codes = {item["code"] for item in package["diagnostics"]}

        assert "EASDK-CONTRACT-SOURCE-BASIS-INCOMPLETE" in codes
        assert "EASDK-ADMITTED-TARGET-SOURCE-BASIS-INSUFFICIENT" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_no_prohibited_professional_or_target_claim_language():
        package = build_from_source()
        text = "\n".join(walk_strings(package)).lower()

        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text
        assert "target support" not in text
        assert "release readiness" not in text
        assert "code compliance" not in text
        assert "professional acceptance" not in text


    if __name__ == "__main__":
        test_fixture_and_builder_validate_against_schema()
        test_builder_is_deterministic_and_preserves_package_members()
        test_target_registry_records_non_gating_candidate_and_checklist_categories()
        test_runtime_grants_are_denied_by_default()
        test_negative_cases_block_grants_missing_source_basis_and_missing_policies()
        test_contract_and_admitted_target_source_basis_are_guarded()
        test_no_prohibited_professional_or_target_claim_language()
        print("PASS: DEL-17-09 export adapter SDK checks")

## Component: tests/test_external_prover_boundary_metadata.py

    #!/usr/bin/env python3
    """Focused tests for DEL-15-04 external-prover boundary metadata."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import sys

    from jsonschema import Draft202012Validator


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    SCHEMA_PATH = ROOT / "schemas" / "external_prover_metadata.schema.json"

    from core.handoff.external_prover import (  # noqa: E402
        build_external_prover_metadata,
        canonical_json,
        diagnostics_for_external_prover_metadata,
    )


    FORBIDDEN_OUTPUT_PHRASES = {
        "code " + "compliant",
        "cert" + "ified",
        "se" + "aled",
        "authentic" + "ated",
        "professional " + "approval",
        "external " + "validation",
        "engineering " + "acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def load_schema() -> dict[str, object]:
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def validate_record(record: dict[str, object]) -> None:
        schema = load_schema()
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(record), key=lambda item: item.path)
        assert not errors, [error.message for error in errors]


    def provenance(source_name: str = "Invented DEL-15-04 fixture") -> dict[str, str]:
        return {
            "source_name": source_name,
            "source_location": "tests/test_external_prover_boundary_metadata.py",
            "source_license": "project-invented-test-data",
            "contributor": "OpenPipeStress",
            "contributor_attestation": "invented non-engineering fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_classification": "machine_checked",
            "privacy_classification": "invented_public_example",
        }


    def checksum(payload_ref: dict[str, str], scope: str) -> dict[str, object]:
        return {
            "algorithm": "sha256",
            "canonicalization": "JCS_compatible_json_payload_hash",
            "payload_ref": payload_ref,
            "payload_scope": scope,
            "value": f"sha256:invented-{scope}",
        }


    def metadata_kwargs() -> dict[str, object]:
        return {
            "metadata_record_id": "external-prover-metadata:invented-del-15-04",
            "names": [
                {
                    "name_id": "name:workflow",
                    "label": "Invented external reference workflow",
                    "name_kind": "external_workflow_label",
                    "provenance": provenance("Invented workflow name"),
                }
            ],
            "tags": ["invented", "metadata-only", "provider-neutral"],
            "notes": [
                {
                    "note_id": "note:boundary",
                    "note_kind": "metadata_note",
                    "text": "Invented metadata record for downstream review context.",
                    "related_refs": [ref("HandoffPackage", "handoff:invented-del-15-04")],
                    "provenance": provenance("Invented metadata note"),
                }
            ],
            "external_references": [
                {
                    "reference_id": "external-ref:generic-workspace",
                    "reference_kind": "external_reference",
                    "display_name": "Invented external workspace reference",
                    "external_ref": ref("ExternalReference", "external:invented-workspace"),
                    "hash_refs": [checksum(ref("ExternalReference", "external:invented-workspace"), "external_ref")],
                    "related_refs": [ref("TargetMapping", "tm:invented-del-15-04")],
                    "provenance": provenance("Invented external reference"),
                }
            ],
            "attachments": [
                {
                    "attachment_id": "attachment:metadata-note",
                    "attachment_kind": "external_file_reference",
                    "display_name": "Invented metadata attachment reference",
                    "uri_or_path_ref": ref("ExternalReference", "attachment:invented-note"),
                    "content_hash": checksum(ref("ExternalReference", "attachment:invented-note"), "attachment"),
                    "privacy_classification": "invented_public_example",
                    "payload_embedded": False,
                    "related_refs": [ref("ExportWorkflow", "export:invented-del-15-04")],
                    "provenance": provenance("Invented attachment reference"),
                }
            ],
            "handoff_package_refs": [
                {
                    "link_id": "handoff:invented-del-15-04",
                    "ref": ref("HandoffPackage", "handoff:invented-del-15-04"),
                    "hash_refs": [checksum(ref("HandoffPackage", "handoff:invented-del-15-04"), "handoff")],
                }
            ],
            "target_mapping_refs": [
                {
                    "link_id": "tm:invented-del-15-04",
                    "ref": ref("TargetMapping", "tm:invented-del-15-04"),
                    "hash_refs": [checksum(ref("TargetMapping", "tm:invented-del-15-04"), "target_mapping")],
                }
            ],
            "export_workflow_refs": [
                {
                    "link_id": "export:invented-del-15-04",
                    "ref": ref("ExportWorkflow", "export:invented-del-15-04"),
                    "hash_refs": [checksum(ref("ExportWorkflow", "export:invented-del-15-04"), "export")],
                }
            ],
            "immutable_model_state_refs": [
                {
                    "link_id": "state:invented-del-15-04",
                    "ref": ref("ModelState", "state:invented-del-15-04"),
                    "hash_refs": [checksum(ref("ModelState", "state:invented-del-15-04"), "model_state")],
                }
            ],
            "assumptions": [
                {
                    "assumption_id": "assumption:external-review",
                    "statement": "Invented downstream external context requires human review before reliance.",
                    "affected_refs": [ref("ExternalReference", "external:invented-workspace")],
                    "provenance": provenance("Invented assumption"),
                }
            ],
            "warnings": [
                {
                    "code": "EPM-INVENTED-WARNING",
                    "severity": "warning",
                    "message": "Invented metadata warning for traceability.",
                    "affected_refs": [ref("ExternalReference", "external:invented-workspace")],
                    "provenance": provenance("Invented warning"),
                }
            ],
            "unsupported_target_flags": [
                {
                    "flag_id": "unsupported-target:solver-not-invoked",
                    "behavior_label": "external_solver_not_invoked",
                    "status": "not_implemented",
                    "target_ref": ref("ExternalReference", "external:invented-workspace"),
                    "affected_refs": [ref("ExportWorkflow", "export:invented-del-15-04")],
                    "assumption_refs": [ref("Assumption", "assumption:external-review")],
                    "warning_refs": [ref("Diagnostic", "EPM-INVENTED-WARNING")],
                    "provenance": provenance("Invented unsupported flag"),
                }
            ],
            "provenance": provenance(),
        }


    def test_metadata_is_deterministic_and_preserves_boundary_links():
        first = build_external_prover_metadata(**metadata_kwargs())
        second = build_external_prover_metadata(**metadata_kwargs())

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-15-04"
        assert first["metadata_contract_status"] == "non_authoritative_workflow_metadata"
        assert first["external_references"][0]["external_ref"]["ref"] == "external:invented-workspace"
        assert first["handoff_package_refs"][0]["ref"]["ref"] == "handoff:invented-del-15-04"
        assert first["target_mapping_refs"][0]["ref"]["ref"] == "tm:invented-del-15-04"
        assert first["export_workflow_refs"][0]["ref"]["ref"] == "export:invented-del-15-04"
        assert first["immutable_model_state_refs"][0]["ref"]["ref"] == "state:invented-del-15-04"
        assert first["unsupported_target_flags"][0]["human_review_required"] is True
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]
        validate_record(first)


    def test_proposed_authority_and_lifecycle_claims_are_blocking_diagnostics():
        kwargs = metadata_kwargs()
        kwargs["proposed_authority_claims"] = [
            {
                "claim_id": "claim:authority",
                "claim_kind": "prover_" + "status",
                "claim_text": "Software " + "cert" + "ified external " + "validation lifecycle.",
                "source_ref": ref("ExternalReference", "external:invented-workspace"),
                "provenance": provenance("Invented rejected claim"),
            }
        ]

        record = build_external_prover_metadata(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}
        assert "EPM-AUTHORITY-CLAIM-REJECTED" in codes
        assert "EPM-PROHIBITED-AUTHORITY-TERM" in codes
        assert any(item["severity"] == "blocking" for item in record["diagnostics"])
        assert record["proposed_authority_claims"][0]["disposition"] == "rejected_boundary_claim"
        validate_record(record)


    def test_embedded_attachment_payload_is_blocked():
        kwargs = metadata_kwargs()
        attachments = deepcopy(kwargs["attachments"])
        attachments[0]["payload_embedded"] = True
        kwargs["attachments"] = attachments

        record = build_external_prover_metadata(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}
        assert "EPM-ATTACHMENT-PAYLOAD-EMBEDDED" in codes
        assert any(item["severity"] == "blocking" for item in record["diagnostics"])
        validate_record(record)


    def test_boundary_flags_cannot_be_flipped_to_software_authority():
        record = build_external_prover_metadata(**metadata_kwargs())
        mutated = deepcopy(record)
        mutated["professional_boundary"]["software_makes_approval_claim"] = True
        mutated["professional_boundary"]["external_tool_invoked"] = True

        codes = {item["code"] for item in diagnostics_for_external_prover_metadata(mutated)}
        assert "EPM-SOFTWARE-AUTHORITY-FLAG-BLOCKED" in codes
        assert "EPM-EXTERNAL-EXECUTION-BLOCKED" in codes


    def test_notes_and_tags_authority_wording_are_blocking_diagnostics():
        kwargs = metadata_kwargs()
        kwargs["tags"] = ["metadata-only", "approved"]
        kwargs["notes"] = [
            {
                "note_id": "note:authority-wording",
                "note_kind": "metadata_note",
                "text": "Downstream reviewer marked this as " + "cert" + "ified.",
                "related_refs": [ref("HandoffPackage", "handoff:invented-del-15-04")],
                "provenance": provenance("Invented boundary probe note"),
            }
        ]

        record = build_external_prover_metadata(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}
        affected = {
            item["affected_references"][0]["ref"]
            for item in record["diagnostics"]
            if item["code"] == "EPM-PROHIBITED-AUTHORITY-TERM"
        }
        assert "EPM-PROHIBITED-AUTHORITY-TERM" in codes
        assert {"tags", "notes"} <= affected
        assert any(item["severity"] == "blocking" for item in record["diagnostics"])
        validate_record(record)


    def test_output_boundary_language_does_not_make_prohibited_claims():
        record = build_external_prover_metadata(**metadata_kwargs())
        text = canonical_json(record).lower()

        for forbidden in FORBIDDEN_OUTPUT_PHRASES:
            assert forbidden not in text
        assert record["professional_boundary"]["external_tool_invoked"] is False
        assert record["professional_boundary"]["commercial_result_payload_ingested"] is False
        assert record["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def main():
        test_metadata_is_deterministic_and_preserves_boundary_links()
        test_proposed_authority_and_lifecycle_claims_are_blocking_diagnostics()
        test_embedded_attachment_payload_is_blocked()
        test_boundary_flags_cannot_be_flipped_to_software_authority()
        test_notes_and_tags_authority_wording_are_blocking_diagnostics()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_gui_editors_contract.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-03 GUI editor contracts."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.editors import build_editor_contract, canonical_json  # noqa: E402


    def main():
        record = build_editor_contract(
            editor_set_id="invented-editor-set",
            editors=[
                {
                    "editor_id": "material-editor",
                    "editor_kind": "material",
                    "target_ref": {"ref_type": "material", "ref_id": "mat-public-1"},
                    "library_classification": "invented_public_example",
                    "fields": [
                        {
                            "field_id": "density",
                            "value": 7850.0,
                            "unit": "kg/m^3",
                            "dimension": "density",
                            "source_ref": {"ref_type": "invented_source", "ref_id": "src-1"},
                        }
                    ],
                },
                {
                    "editor_id": "rule-pack-reference",
                    "editor_kind": "rule_pack_reference",
                    "target_ref": {"ref_type": "rule_pack", "ref_id": "rp-private-ref"},
                    "library_classification": "private_reference_only",
                    "fields": [{"field_id": "rule_pack_name", "value": "Invented local checks"}],
                    "rule_pack_lifecycle": {"checksum": "sha256:invented", "state": "referenced"},
                },
            ],
        )
        assert record["deliverable_id"] == "DEL-07-03"
        assert record["private_payload_policy"] == "references_and_checksums_only_no_private_payload_copy"
        assert record["editors"][0]["save_intent"]["mutates_persistent_project"] is False
        assert record["editors"][0]["fields"][0]["unit_metadata"]["dimension_is_canonical"] is True
        assert record["unit_contract"]["contract_ref"] == "DEL-02-02"
        assert record["editors"][1]["rule_pack_lifecycle"]["checksum"] == "sha256:invented"
        assert not record["diagnostics"]
        assert record["professional_boundary"]["software_makes_approval_claim"] is False
        assert "private payload" not in canonical_json(record).lower()

        missing = build_editor_contract(
            editor_set_id="missing-checksum",
            editors=[
                {
                    "editor_id": "rule-pack-reference",
                    "editor_kind": "rule_pack_reference",
                    "fields": [{"field_id": "name", "value": "TBD"}],
                    "rule_pack_lifecycle": {"state": "referenced"},
                }
            ],
        )
        assert any(item["code"] == "RULE_PACK_CHECKSUM_MISSING" for item in missing["diagnostics"])
        assert any(item["code"] == "EDITOR_FIELD_VALUE_UNRESOLVED" for item in missing["diagnostics"])

        missing_unit = build_editor_contract(
            editor_set_id="missing-unit",
            editors=[
                {
                    "editor_id": "component-editor",
                    "editor_kind": "component",
                    "fields": [{"field_id": "diameter", "value": 125.0, "dimension": "length"}],
                }
            ],
        )
        assert any(item["code"] == "EDITOR_UNIT_METADATA_MISSING" for item in missing_unit["diagnostics"])
        assert missing_unit["editors"][0]["validation_state"] == "blocked_by_contract_metadata"


    def test_gui_editors_contract_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_handoff_export_workflow.py

    #!/usr/bin/env python3
    """Focused tests for DEL-15-03 handoff export workflow."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import sys

    from jsonschema import Draft202012Validator


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.handoff.exporter import (  # noqa: E402
        build_handoff_export_workflow,
        canonical_json,
    )
    from core.handoff.target_mapping import build_target_mapping_contract  # noqa: E402


    FIXTURE_PATH = (
        ROOT
        / "execution"
        / "PKG-15_Handoff and External Prover Workflow"
        / "1_Working"
        / "DEL-15-03_Downstream modeling export workflow"
        / "fixtures"
        / "invented_target_fixture.json"
    )
    HANDOFF_SCHEMA_PATH = ROOT / "schemas" / "handoff_package.schema.json"
    TARGET_MAPPING_SCHEMA_PATH = ROOT / "schemas" / "target_mapping.schema.json"

    FORBIDDEN_CLAIMS = {
        "code " + "compliant",
        "cert" + "ified",
        "se" + "aled",
        "authenticated",
        "professional approval",
        "external validation",
        "engineering acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def load_schema(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def validate_with_schema(payload: dict[str, object], path: Path) -> None:
        schema = load_schema(path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(payload), key=lambda item: item.path)
        assert not errors, [error.message for error in errors]


    def provenance(source_name: str = "Invented DEL-15-03 fixture") -> dict[str, str]:
        return {
            "source_name": source_name,
            "source_location": "execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-03_Downstream modeling export workflow/fixtures/invented_target_fixture.json",
            "source_license": "project-invented-test-data",
            "contributor": "OpenPipeStress",
            "contributor_attestation": "invented non-engineering fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_classification": "machine_checked",
            "privacy_classification": "invented_public_example",
        }


    def checksum(payload_ref: dict[str, str], scope: str, value: str) -> dict[str, object]:
        return {
            "algorithm": "sha256",
            "canonicalization": "JCS_compatible_json_payload_hash",
            "payload_ref": payload_ref,
            "payload_scope": scope,
            "value": value,
        }


    MODEL_HASH = checksum(ref("Model", "model:invented-del-15-03"), "model_hash", "sha256:invented-model")


    def handoff_package() -> dict[str, object]:
        units_manifest = {
            "unit_system_ref": ref("UnitSystem", "units:invented-del-15-03"),
            "units_schema": "schemas/units.schema.yaml",
            "dimension_basis": "schemas/units.schema.yaml",
            "coordinate_unit": "m",
            "force_unit": "N",
            "moment_unit": "N-m",
            "displacement_unit": "m",
            "rotation_unit": "rad",
            "stress_unit": "Pa",
            "temperature_unit": "degC",
            "hash_refs": [
                checksum(ref("UnitSystem", "units:invented-del-15-03"), "units_manifest", "sha256:invented-units")
            ],
            "provenance": provenance("Invented units manifest"),
        }
        entity_ids = {
            "component_ids": ["component:pipe-1"],
            "node_ids": ["node:1", "node:2"],
            "element_ids": ["element:1"],
            "station_ids": ["station:1"],
            "load_case_ids": ["load:weight"],
            "result_ids": ["result:displacement"],
            "model_state_ids": ["state:handoff"],
            "analysis_run_ids": ["run:mechanics-reference"],
            "mapping_id_refs": [ref("TargetMapping", "mapping:pipe-diameter")],
        }
        warning = {
            "code": "INVENTED-HANDOFF-WARNING",
            "class": "LOCAL_HANDOFF_WARNING",
            "severity": "warning",
            "source": ref("HandoffPackage", "handoff:invented-del-15-03"),
            "affected_object": ref("Model", "model:invented-del-15-03"),
            "message": "Invented handoff warning for downstream review.",
            "remediation": "Review invented target fixture limitations.",
            "provenance": provenance("Invented warning"),
        }
        assumption = {
            "assumption_id": "assumption:invented-review",
            "statement": "Invented downstream target fixture requires review before use.",
            "status": "requires_human_review",
            "affected_refs": [ref("Model", "model:invented-del-15-03")],
            "provenance": provenance("Invented assumption"),
        }
        unsupported = {
            "flag_id": "unsupported:external-solver-not-invoked",
            "behavior_label": "external_solver_not_invoked",
            "status": "not_implemented",
            "target_ref": ref("ExternalReference", "target:invented-generic"),
            "affected_refs": [ref("AnalysisRun", "run:mechanics-reference")],
            "human_review_required": True,
            "provenance": provenance("Invented unsupported flag"),
        }
        return {
            "schema_version": "0.1.0",
            "deliverable_id": "DEL-15-01",
            "package_id": "PKG-15",
            "scope_item": "SOW-074",
            "objectives": ["OBJ-017"],
            "handoff_contract_status": {
                "record_contract": "schema_first_canonical_handoff_package_records",
                "manifest_contract": "schema_first_handoff_manifest_metadata",
                "model_schema_binding": "schemas/model.schema.yaml",
                "units_schema_binding": "schemas/units.schema.yaml",
                "model_state_binding": "schemas/model_state.schema.json",
                "analysis_run_binding": "schemas/analysis_run.schema.json",
                "result_export_binding": "schemas/results.schema.yaml",
                "local_fea_handoff_binding": "schemas/local_fea_handoff.schema.yaml",
                "audit_hash_binding": "hash_records_follow_audit_manifest_predecessor_semantics",
                "target_mapping_taxonomy": "reserved_for_DEL-15-02",
                "physical_package_container": "TBD",
                "external_prover_status": "not_declared_by_handoff_package",
                "professional_boundary": "downstream_modeling_and_review_support_only",
            },
            "handoff_package_manifest": {
                "package_identity": {
                    "handoff_package_id": "handoff:invented-del-15-03",
                    "manifest_id": "manifest:invented-del-15-03",
                    "package_schema_version": "0.1.0",
                    "created_at": "2026-05-06T00:00:00Z",
                    "created_by": "OpenPipeStress DEL-15-03 fixture",
                    "package_label": "Invented downstream modeling handoff",
                    "package_kind": "canonical_handoff_manifest",
                },
                "model_basis": {
                    "model_ref": ref("Model", "model:invented-del-15-03"),
                    "model_schema": "schemas/model.schema.yaml",
                    "model_kind": "handoff_basis",
                    "basis_state_ref": ref("ModelState", "state:handoff"),
                    "source_refs": [ref("Project", "project:invented-public")],
                    "hash_refs": [MODEL_HASH],
                    "provenance": provenance("Invented model basis"),
                },
                "model_hash": MODEL_HASH,
                "units_manifest": units_manifest,
                "entity_ids": entity_ids,
                "model_state_refs": [
                    {
                        "model_state_ref": ref("ModelState", "state:handoff"),
                        "model_state_schema": "schemas/model_state.schema.json",
                        "state_kind": "handoff_basis",
                        "hash_refs": [checksum(ref("ModelState", "state:handoff"), "model_state_record", "sha256:invented-state")],
                        "privacy_classification": "invented_public_example",
                        "provenance": provenance("Invented model state"),
                    }
                ],
                "analysis_run_refs": [],
                "result_export_refs": [],
                "library_refs": [
                    {
                        "library_ref": ref("Library", "library:invented-public"),
                        "library_kind": "component",
                        "version": "0.1.0",
                        "checksum": checksum(ref("Library", "library:invented-public"), "library_reference_metadata", "sha256:invented-library"),
                        "source_notice": "Invented public fixture metadata only.",
                        "redistribution_status": "invented_non_engineering_example",
                        "review_classification": "machine_checked",
                        "privacy_classification": "invented_public_example",
                        "private_payload_redacted": True,
                        "provenance": provenance("Invented library ref"),
                    }
                ],
                "rule_pack_refs": [
                    {
                        "rule_pack_id": "rule-pack:invented-public",
                        "version": "0.1.0",
                        "checksum": checksum(ref("RulePack", "rule-pack:invented-public"), "rule_pack_reference_metadata", "sha256:invented-rule-pack"),
                        "source_notice": "Invented rule-pack metadata only.",
                        "redistribution_status": "invented_non_engineering_example",
                        "review_classification": "machine_checked",
                        "privacy_classification": "invented_public_example",
                        "private_payload_redacted": True,
                        "provenance": provenance("Invented rule pack ref"),
                    }
                ],
                "checksums": [MODEL_HASH],
                "target_mapping_metadata": {
                    "mapping_schema_status": "reserved_metadata_only",
                    "target_system_kind": "generic_downstream_modeling",
                    "target_mapping_refs": [ref("TargetMapping", "tm:invented-del-15-03")],
                    "field_mapping_summary": "Invented provider-neutral field mappings.",
                    "unsupported_behavior_refs": [ref("UnsupportedBehaviorFlag", "unsupported:external-solver-not-invoked")],
                    "approximate_behavior_refs": [ref("UnsupportedBehaviorFlag", "approximate:target-field")],
                    "detailed_taxonomy_owner": "DEL-15-02",
                    "provenance": provenance("Invented target mapping metadata"),
                },
                "unsupported_behavior_flags": [unsupported],
                "unresolved_assumptions": [assumption],
                "warnings": [warning],
                "diagnostics": [],
                "privacy": {
                    "classification": "invented_public_example",
                    "local_only": True,
                    "telemetry_allowed": False,
                    "private_payload_embedded": False,
                    "protected_payload_embedded": False,
                    "commercial_tool_payload_embedded": False,
                    "redaction_refs": [ref("ExternalReference", "redaction:invented-public")],
                },
                "redistribution_classification": "invented_non_engineering_example",
                "review_classification": "machine_checked",
                "provenance": provenance("Invented handoff manifest"),
                "professional_boundary": {
                    "human_review_required": True,
                    "supports_downstream_modeling": True,
                    "supports_downstream_review": True,
                    "software_makes_compliance_claim": False,
                    "software_makes_certification_claim": False,
                    "software_makes_sealing_claim": False,
                    "software_makes_approval_claim": False,
                    "software_makes_authentication_claim": False,
                    "software_creates_professional_reliance_record": False,
                },
            },
        }


    def source_context(package: dict[str, object]) -> dict[str, object]:
        manifest = package["handoff_package_manifest"]
        return {
            "model_hash": manifest["model_hash"],
            "units_manifest_ref": manifest["units_manifest"]["unit_system_ref"],
            "entity_id_refs": [ref("EntityIdManifest", "entity-ids:invented-del-15-03")],
            "library_refs": [item["library_ref"] for item in manifest["library_refs"]],
            "rule_pack_refs": [ref("RulePack", item["rule_pack_id"]) for item in manifest["rule_pack_refs"]],
            "unresolved_assumption_refs": [
                ref("Assumption", item["assumption_id"])
                for item in manifest["unresolved_assumptions"]
            ],
            "warning_refs": [ref("Diagnostic", item["code"]) for item in manifest["warnings"]],
            "privacy_context": manifest["privacy"],
        }


    def target_mapping(package: dict[str, object]) -> dict[str, object]:
        return build_target_mapping_contract(
            mapping_contract_id="tm:invented-del-15-03",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:invented-generic"),
            source_context=source_context(package),
            mapping_records=[
                {
                    "mapping_id": "mapping:pipe-diameter",
                    "mapping_kind": "field",
                    "source_ref": ref("Component", "component:pipe-1"),
                    "target_ref": ref("ExternalReference", "target:pipe-diameter"),
                    "value_kind": "quantity",
                    "unit_metadata": {"unit": "m", "dimension": "length"},
                    "mapping_status": "mapped",
                    "assumption_refs": [],
                    "warning_refs": [],
                }
            ],
            unsupported_behaviors=[
                {
                    "flag_id": "unsupported:mesh",
                    "behavior_label": "mesh_generation_not_performed",
                    "status": "not_implemented",
                    "target_ref": ref("ExternalReference", "target:mesh"),
                    "affected_refs": [ref("Model", "model:invented-del-15-03")],
                    "assumption_refs": [ref("Assumption", "assumption:invented-review")],
                }
            ],
            approximate_behaviors=[
                {
                    "flag_id": "approximate:target-field",
                    "behavior_label": "approximate_behavior_requires_review",
                    "status": "approximate",
                    "target_ref": ref("ExternalReference", "target:review-field"),
                    "affected_refs": [ref("Component", "component:pipe-1")],
                    "warning_refs": [ref("Diagnostic", "INVENTED-HANDOFF-WARNING")],
                }
            ],
        )


    def target_fixture() -> dict[str, object]:
        with FIXTURE_PATH.open(encoding="utf-8") as handle:
            return json.load(handle)


    def test_export_workflow_is_deterministic_and_preserves_required_context():
        package = handoff_package()
        mapping = target_mapping(package)
        fixture = target_fixture()

        validate_with_schema(package, HANDOFF_SCHEMA_PATH)
        validate_with_schema(mapping, TARGET_MAPPING_SCHEMA_PATH)
        assert fixture["provenance"]["redistribution_status"] == "invented_non_engineering_example"
        assert fixture["provenance"]["privacy_classification"] == "invented_public_example"
        assert "protected standards data" in " ".join(fixture["notes"])

        first = build_handoff_export_workflow(
            export_workflow_id="export:invented-del-15-03",
            handoff_package=package,
            target_mapping_contract=mapping,
            target_fixture=fixture,
        )
        second = build_handoff_export_workflow(
            export_workflow_id="export:invented-del-15-03",
            handoff_package=deepcopy(package),
            target_mapping_contract=deepcopy(mapping),
            target_fixture=target_fixture(),
        )

        assert canonical_json(first) == canonical_json(second)
        payload = first["export_payload"]
        assert payload["model_hash"] == package["handoff_package_manifest"]["model_hash"]
        assert payload["units_manifest"] == package["handoff_package_manifest"]["units_manifest"]
        assert payload["entity_ids"] == package["handoff_package_manifest"]["entity_ids"]
        assert payload["library_refs"] == package["handoff_package_manifest"]["library_refs"]
        assert payload["rule_pack_refs"] == package["handoff_package_manifest"]["rule_pack_refs"]
        assert payload["target_mapping_metadata"] == package["handoff_package_manifest"]["target_mapping_metadata"]
        assert payload["unresolved_assumptions"] == package["handoff_package_manifest"]["unresolved_assumptions"]
        assert payload["warnings"] == package["handoff_package_manifest"]["warnings"]
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_unsupported_and_approximate_target_behavior_is_explicit():
        package = handoff_package()
        export = build_handoff_export_workflow(
            export_workflow_id="export:invented-del-15-03",
            handoff_package=package,
            target_mapping_contract=target_mapping(package),
            target_fixture=target_fixture(),
        )
        records = export["export_payload"]["unsupported_target_records"]
        record_ids = {item["record_id"] for item in records}

        assert {
            "unsupported:external-solver-not-invoked",
            "unsupported:mesh",
            "approximate:target-field",
            "capability:external-solver",
        } <= record_ids
        assert all(item["human_review_required"] is True for item in records)
        assert all(item["affected_refs"] for item in records)


    def test_unit_bearing_mapping_without_unit_metadata_is_blocked():
        package = handoff_package()
        mapping = target_mapping(package)
        mapping["mapping_records"][0]["unit_metadata"] = None

        export = build_handoff_export_workflow(
            export_workflow_id="export:bad-unit",
            handoff_package=package,
            target_mapping_contract=mapping,
            target_fixture=target_fixture(),
        )

        codes = {item["code"] for item in export["diagnostics"]}
        assert "EXP-UNIT-METADATA-MISSING" in codes
        assert any(item["severity"] == "blocking" for item in export["diagnostics"])


    def test_mapping_hash_and_units_mismatch_are_blocked_not_defaulted():
        package = handoff_package()
        mapping = target_mapping(package)
        mapping["source_context"]["model_hash"] = checksum(ref("Model", "model:other"), "model_hash", "sha256:other")
        mapping["source_context"]["units_manifest_ref"] = ref("UnitSystem", "units:other")

        export = build_handoff_export_workflow(
            export_workflow_id="export:mismatch",
            handoff_package=package,
            target_mapping_contract=mapping,
            target_fixture=target_fixture(),
        )

        codes = {item["code"] for item in export["diagnostics"]}
        assert {"EXP-MODEL-HASH-MISMATCH", "EXP-UNITS-MANIFEST-MISMATCH"} <= codes


    def test_target_fixture_authority_metadata_is_blocking_boundary_diagnostic():
        package = handoff_package()
        fixture = target_fixture()
        fixture["notes"] = ["Target fixture marked as " + "approved" + " by downstream reviewer."]
        fixture["free_metadata"] = {"review_label": "cert" + "ified target handoff"}
        fixture["unsupported_capabilities"][0]["behavior_label"] = "engineering_" + "acceptance"

        export = build_handoff_export_workflow(
            export_workflow_id="export:fixture-authority",
            handoff_package=package,
            target_mapping_contract=target_mapping(package),
            target_fixture=fixture,
        )

        codes = {item["code"] for item in export["diagnostics"]}
        assert "EXP-PROHIBITED-AUTHORITY-TERM" in codes
        assert any(item["severity"] == "blocking" for item in export["diagnostics"])
        assert export["export_payload"]["diagnostics"] == export["diagnostics"]


    def test_export_output_contains_no_prohibited_authority_claims():
        package = handoff_package()
        export = build_handoff_export_workflow(
            export_workflow_id="export:boundary",
            handoff_package=package,
            target_mapping_contract=target_mapping(package),
            target_fixture=target_fixture(),
        )
        text = canonical_json(export).lower()

        for forbidden in FORBIDDEN_CLAIMS:
            assert forbidden not in text
        assert export["professional_boundary"]["software_makes_compliance_claim"] is False


    def main():
        test_export_workflow_is_deterministic_and_preserves_required_context()
        test_unsupported_and_approximate_target_behavior_is_explicit()
        test_unit_bearing_mapping_without_unit_metadata_is_blocked()
        test_mapping_hash_and_units_mismatch_are_blocked_not_defaulted()
        test_target_fixture_authority_metadata_is_blocking_boundary_diagnostic()
        test_export_output_contains_no_prohibited_authority_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_handoff_package_schema.py

    #!/usr/bin/env python3
    """Contract checks for the canonical handoff package schema."""

    import json
    from pathlib import Path

    from jsonschema import Draft202012Validator


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "handoff_package.schema.json"
    FIXTURE_PATH = (
        ROOT
        / "execution"
        / "PKG-15_Handoff and External Prover Workflow"
        / "1_Working"
        / "DEL-15-01_Canonical handoff package schema and manifest"
        / "fixtures"
        / "invented_handoff_package.json"
    )

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "handoff_contract_status",
        "handoff_package_manifest",
    }

    REQUIRED_DEFS = {
        "AnalysisRunRef",
        "AssumptionRecord",
        "Checksum",
        "Diagnostic",
        "EntityIdManifest",
        "HandoffContractStatus",
        "HandoffPackageManifest",
        "Id",
        "LibraryRef",
        "ModelBasis",
        "ModelStateRef",
        "PackageIdentity",
        "PrivacyClassification",
        "PrivacyContext",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ResultExportRef",
        "ReviewClassification",
        "RulePackRef",
        "TargetMappingMetadata",
        "UnitsManifestRef",
        "UnsupportedBehaviorFlag",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "LOCAL_HANDOFF_WARNING",
        "EXPORT_BLOCKING",
        "TARGET_MAPPING_WARNING",
        "UNSUPPORTED_BEHAVIOR_WARNING",
        "PRIVACY_WARNING",
        "HASH_WARNING",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "formal prover approval status",
        "code compliant",
        "certified by software",
        "sealed by software",
        "professional approval by the software",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture():
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def validate_fixture(schema):
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(load_fixture()), key=lambda item: item.path)
        assert not errors, [error.message for error in errors]


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-15-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-15"
        assert schema["properties"]["scope_item"]["const"] == "SOW-074"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-017"

        contract = defs["HandoffContractStatus"]["properties"]
        assert (
            contract["record_contract"]["const"]
            == "schema_first_canonical_handoff_package_records"
        )
        assert contract["manifest_contract"]["const"] == (
            "schema_first_handoff_manifest_metadata"
        )
        assert contract["model_schema_binding"]["const"] == "schemas/model.schema.yaml"
        assert contract["units_schema_binding"]["const"] == "schemas/units.schema.yaml"
        assert contract["model_state_binding"]["const"] == "schemas/model_state.schema.json"
        assert contract["analysis_run_binding"]["const"] == "schemas/analysis_run.schema.json"
        assert contract["result_export_binding"]["const"] == "schemas/results.schema.yaml"
        assert contract["local_fea_handoff_binding"]["const"] == (
            "schemas/local_fea_handoff.schema.yaml"
        )
        assert contract["audit_hash_binding"]["const"] == (
            "hash_records_follow_audit_manifest_predecessor_semantics"
        )
        assert contract["target_mapping_taxonomy"]["const"] == "reserved_for_DEL-15-02"
        assert contract["physical_package_container"]["const"] == "TBD"
        assert contract["external_prover_status"]["const"] == (
            "not_declared_by_handoff_package"
        )

        manifest_required = required_at(schema, "HandoffPackageManifest")
        assert {
            "package_identity",
            "model_basis",
            "model_hash",
            "units_manifest",
            "entity_ids",
            "model_state_refs",
            "analysis_run_refs",
            "result_export_refs",
            "library_refs",
            "rule_pack_refs",
            "checksums",
            "target_mapping_metadata",
            "unsupported_behavior_flags",
            "unresolved_assumptions",
            "warnings",
            "diagnostics",
            "privacy",
            "redistribution_classification",
            "review_classification",
            "provenance",
            "professional_boundary",
        } <= manifest_required

        assert {
            "handoff_package_id",
            "manifest_id",
            "package_schema_version",
            "created_at",
            "created_by",
            "package_label",
            "package_kind",
        } <= required_at(schema, "PackageIdentity")

        assert {
            "model_ref",
            "model_schema",
            "model_kind",
            "basis_state_ref",
            "source_refs",
            "hash_refs",
            "provenance",
        } <= required_at(schema, "ModelBasis")
        assert defs["ModelBasis"]["properties"]["model_schema"]["const"] == (
            "schemas/model.schema.yaml"
        )

        checksum_required = required_at(schema, "Checksum")
        assert {
            "algorithm",
            "canonicalization",
            "payload_ref",
            "payload_scope",
            "value",
        } <= checksum_required
        assert {"sha256", "sha512", "TBD"} <= set(
            defs["Checksum"]["properties"]["algorithm"]["enum"]
        )
        assert {
            "JCS",
            "JCS_compatible_json_payload_hash",
            "external_file_native",
            "NONE",
            "TBD",
        } <= set(defs["Checksum"]["properties"]["canonicalization"]["enum"])
        assert {
            "handoff_package_manifest",
            "canonical_handoff_record",
            "model_payload",
            "model_hash",
            "units_manifest",
            "entity_id_manifest",
            "model_state_record",
            "analysis_run_record",
            "result_export_record",
            "library_reference_metadata",
            "rule_pack_reference_metadata",
            "local_fea_handoff_record",
            "audit_manifest",
            "external_reference",
        } <= set(defs["Checksum"]["properties"]["payload_scope"]["enum"])

        assert {
            "unit_system_ref",
            "units_schema",
            "dimension_basis",
            "coordinate_unit",
            "force_unit",
            "moment_unit",
            "displacement_unit",
            "rotation_unit",
            "stress_unit",
            "temperature_unit",
            "hash_refs",
            "provenance",
        } <= required_at(schema, "UnitsManifestRef")
        assert defs["UnitsManifestRef"]["properties"]["units_schema"]["const"] == (
            "schemas/units.schema.yaml"
        )

        assert {
            "component_ids",
            "node_ids",
            "element_ids",
            "station_ids",
            "load_case_ids",
            "result_ids",
            "model_state_ids",
            "analysis_run_ids",
            "mapping_id_refs",
        } <= required_at(schema, "EntityIdManifest")

        assert defs["ModelStateRef"]["properties"]["model_state_schema"]["const"] == (
            "schemas/model_state.schema.json"
        )
        assert defs["AnalysisRunRef"]["properties"]["analysis_run_schema"]["const"] == (
            "schemas/analysis_run.schema.json"
        )
        assert defs["ResultExportRef"]["properties"]["result_schema"]["const"] == (
            "schemas/results.schema.yaml"
        )

        assert {
            "library_ref",
            "library_kind",
            "version",
            "checksum",
            "source_notice",
            "redistribution_status",
            "review_classification",
            "privacy_classification",
            "private_payload_redacted",
            "provenance",
        } <= required_at(schema, "LibraryRef")
        assert defs["LibraryRef"]["properties"]["private_payload_redacted"]["const"] is True
        assert {
            "material",
            "section",
            "component",
            "rule_pack",
            "project_private",
            "commercial_tool_reference",
        } <= set(defs["LibraryRef"]["properties"]["library_kind"]["enum"])

        assert {
            "rule_pack_id",
            "version",
            "checksum",
            "source_notice",
            "redistribution_status",
            "review_classification",
            "privacy_classification",
            "private_payload_redacted",
            "provenance",
        } <= required_at(schema, "RulePackRef")
        assert defs["RulePackRef"]["properties"]["private_payload_redacted"]["const"] is True

        privacy = defs["PrivacyContext"]["properties"]
        assert privacy["local_only"]["const"] is True
        assert privacy["telemetry_allowed"]["const"] is False
        assert privacy["private_payload_embedded"]["const"] is False
        assert privacy["protected_payload_embedded"]["const"] is False
        assert privacy["commercial_tool_payload_embedded"]["const"] is False
        assert {
            "public_metadata",
            "invented_public_example",
            "private_project_data",
            "private_library_data",
            "private_rule_pack_data",
            "commercial_tool_metadata",
            "protected_suspected",
            "redacted",
        } <= enum_at(schema, "PrivacyClassification")

        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "commercial_tool_reference_only",
            "invented_non_engineering_example",
        } <= enum_at(schema, "RedistributionStatus")
        assert {
            "unreviewed",
            "machine_checked",
            "human_review_required",
            "human_reviewed_reference_only",
            "quarantined",
        } <= enum_at(schema, "ReviewClassification")

        target_mapping = defs["TargetMappingMetadata"]["properties"]
        assert target_mapping["mapping_schema_status"]["const"] == "reserved_metadata_only"
        assert target_mapping["detailed_taxonomy_owner"]["const"] == "DEL-15-02"
        assert {
            "local_fea",
            "external_prover",
            "commercial_tool_reference",
            "generic_downstream_modeling",
            "TBD",
        } <= set(target_mapping["target_system_kind"]["enum"])

        flags = defs["UnsupportedBehaviorFlag"]["properties"]
        assert {
            "target_format_not_selected",
            "target_mapping_taxonomy_pending",
            "mesh_generation_not_performed",
            "external_solver_not_invoked",
            "external_prover_not_invoked",
            "commercial_tool_parser_not_implemented",
            "physical_package_not_finalized",
            "boundary_transfer_requires_review",
            "approximate_behavior_requires_review",
            "unsupported_target_behavior",
        } <= set(flags["behavior_label"]["enum"])
        assert {"unsupported", "approximate", "requires_human_review", "not_implemented"} <= set(
            flags["status"]["enum"]
        )
        assert flags["human_review_required"]["const"] is True

        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False
        assert boundary["software_creates_professional_reliance_record"]["const"] is False

        validate_fixture(schema)
        assert boundary["supports_downstream_modeling"]["const"] is True
        assert boundary["supports_downstream_review"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False
        assert (
            boundary["software_creates_professional_reliance_record"]["const"] is False
        )

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings

        joined_enums = set()
        for definition in defs.values():
            if isinstance(definition, dict) and "enum" in definition:
                joined_enums.update(definition["enum"])
        assert joined_enums.isdisjoint(FORBIDDEN_STATUS)


    if __name__ == "__main__":
        main()

## Component: tests/test_headless_runner_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the headless runner contract."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "headless_runner.schema.yaml"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_items",
        "objectives",
        "runner_status",
        "tbd_decisions",
        "request",
        "result",
    }

    REQUIRED_DEFS = {
        "AnalysisStatus",
        "ChecksumRef",
        "Diagnostic",
        "HeadlessRunnerRequest",
        "HeadlessRunnerResult",
        "JobState",
        "PhysicalProjectContainer",
        "PrivacyContext",
        "ProfessionalBoundary",
        "Provenance",
        "Reference",
        "RequestedOutput",
        "ResultEnvelopeRef",
        "RunnerOperation",
        "RunnerStatus",
        "TbdDecisions",
    }

    REQUIRED_OPERATIONS = {
        "solve",
        "validate_input",
        "export_results",
        "run_benchmark",
        "run_regression",
        "TBD",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "RUNNER_BLOCKING",
        "EXPORT_BLOCKING",
        "PRIVACY_WARNING",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    REQUIRED_TBD = {
        "final_cli_command_syntax",
        "package_scripts",
        "process_invocation",
        "network_access",
        "filesystem_mutation_policy",
        "ci_provider",
        "release_matrix",
        "public_transport_protocol",
        "external_adapter_formats",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-10-05"
        assert schema["properties"]["package_id"]["const"] == "PKG-10"
        assert {"SOW-054", "SOW-032"} <= set(
            schema["properties"]["scope_items"]["items"]["enum"]
        )
        assert {"OBJ-008", "OBJ-009", "OBJ-012"} <= set(
            schema["properties"]["objectives"]["items"]["enum"]
        )

        runner_status = defs["RunnerStatus"]["properties"]
        assert runner_status["interface_kind"]["const"] == (
            "schema_first_headless_runner_contract"
        )
        assert (
            runner_status["physical_project_container"]["$ref"]
            == "#/$defs/PhysicalProjectContainer"
        )
        for key in [
            "final_cli_command_syntax",
            "package_scripts",
            "public_transport_protocol",
            "ci_provider",
            "release_matrix",
            "external_adapter_formats",
            "local_fea_package_format",
        ]:
            assert runner_status[key]["const"] == "TBD"

        tbd = defs["TbdDecisions"]
        assert REQUIRED_TBD <= set(tbd["required"])
        for key in REQUIRED_TBD:
            assert tbd["properties"][key]["const"] == "TBD"
        assert "physical_project_container" not in set(tbd["required"])
        assert "physical_project_container" not in tbd["properties"]

        physical = defs["PhysicalProjectContainer"]["properties"]
        assert physical["profile"]["const"] == "sqlite_local_project_store"
        assert physical["decision_ref"]["const"] == "SCA-003"
        assert physical["storage_role"]["const"] == "local_store_index_projection"
        assert physical["canonical_truth"]["const"] == "canonical_json_jcs_payload"
        assert physical["sql_public_contract"]["const"] is False
        assert physical["direct_sql_access_allowed"]["const"] is False
        assert physical["hosted_db_allowed"]["const"] is False
        assert physical["network_required"]["const"] is False
        assert physical["sidecars_rebuildable"]["const"] is True

        request_required = required_at(schema, "HeadlessRunnerRequest")
        assert {
            "request_id",
            "operation",
            "operation_ref",
            "project_ref",
            "model_ref",
            "unit_system_ref",
            "load_basis_refs",
            "input_manifest_ref",
            "requested_outputs",
            "privacy",
            "provenance",
            "professional_boundary",
        } <= request_required
        assert REQUIRED_OPERATIONS <= enum_at(schema, "RunnerOperation")
        assert {"result_envelope", "audit_manifest", "diagnostics"} <= enum_at(
            schema, "RequestedOutput"
        )

        result_required = required_at(schema, "HeadlessRunnerResult")
        assert {
            "run_id",
            "job",
            "analysis_status",
            "result_envelope_ref",
            "result_refs",
            "audit_manifest_ref",
            "checksums",
            "diagnostics",
            "privacy",
            "provenance",
            "professional_boundary",
        } <= result_required

        result_ref = defs["ResultEnvelopeRef"]["properties"]
        assert result_ref["schema_ref"]["const"] == "schemas/results.schema.yaml"
        assert result_ref["compatibility"]["const"] == "schema_first_json_result_envelope"
        assert (
            defs["HeadlessRunnerResult"]["properties"]["result_refs"]["items"]["$ref"]
            == "#/$defs/Reference"
        )

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)
        assert (
            defs["HeadlessRunnerResult"]["properties"]["analysis_status"]["contains"][
                "const"
            ]
            == "HUMAN_REVIEW_REQUIRED"
        )

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        privacy = defs["PrivacyContext"]["properties"]
        assert privacy["local_only"]["const"] is True
        assert privacy["telemetry_allowed"]["const"] is False
        assert "protected_suspected" in privacy["classification"]["enum"]

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False

        checksum = defs["ChecksumRef"]["properties"]
        assert set(checksum["algorithm"]["enum"]) == {"sha256", "sha512", "TBD"}
        assert set(checksum["canonicalization"]["enum"]) == {"rfc8785_jcs", "NONE", "TBD"}
        assert "rfc8785_jcs" in checksum["canonicalization"]["enum"]
        assert "NONE" in checksum["canonicalization"]["enum"]
        assert defs["HeadlessRunnerResult"]["properties"]["checksums"]["minItems"] == 1

        schema_upper = SCHEMA_PATH.read_text(encoding="utf-8").upper()
        for term in FORBIDDEN_STATUS:
            assert term not in schema_upper


    def test_headless_runner_contract():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_invented_example_models.py

    #!/usr/bin/env python3
    """Stdlib smoke checks for invented educational model examples."""

    import json
    import sys
    from copy import deepcopy
    from hashlib import sha256
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    if str(ROOT / "tests") not in sys.path:
        sys.path.insert(0, str(ROOT / "tests"))

    import yaml  # noqa: E402

    from core.project_persistence import (  # noqa: E402
        build_project_persistence_envelope,
        canonical_json,
        project_hash_manifest,
        round_trip_project_envelope,
        validate_project_persistence_envelope,
    )
    from schema_validation import validate_instance  # noqa: E402

    EXAMPLE_DIR = ROOT / "examples" / "models" / "invented"
    EXAMPLE_FILES = {
        "mechanics_only_toy_span.json",
        "fake_rule_pack_toy_model.json",
    }
    MODEL_SCHEMA_PATH = ROOT / "schemas" / "model.schema.yaml"
    PERSISTENCE_SCHEMA_PATH = ROOT / "schemas" / "project_persistence.schema.yaml"
    MODEL_STATE_SCHEMA_PATH = ROOT / "schemas" / "model_state.schema.json"
    ANALYSIS_RUN_SCHEMA_PATH = ROOT / "schemas" / "analysis_run.schema.json"
    RULE_PACK_PATH = ROOT / "examples" / "rule_packs" / "invented_demo.yaml"

    REQUIRED_PROJECT_KEYS = {
        "id",
        "name",
        "unit_system",
        "privacy_class",
        "storage_policy",
        "models",
        "rule_pack_refs",
        "report_settings",
        "reports",
        "diagnostics",
        "hashes",
    }

    REQUIRED_MODEL_KEYS = {
        "id",
        "name",
        "model_role",
        "coordinate_system",
        "nodes",
        "elements",
        "components",
        "materials",
        "sections",
        "supports",
        "load_cases",
        "combinations",
        "results",
        "diagnostics",
        "unresolved_assumptions",
        "traceability_links",
        "design_knowledge_refs",
        "constraint_refs",
        "equipment_interface_refs",
        "operation_refs",
        "model_state_refs",
        "analysis_run_refs",
        "comparison_refs",
        "handoff_package_refs",
        "external_reference_refs",
        "provenance",
    }

    REQUIRED_NOTICE_TEXT = {
        "invented",
        "non-code",
        "non-project",
        "not suitable for engineering reliance",
    }

    FORBIDDEN_TEXT = {
        "A" + "SME",
        "B" + "31",
        "B" + "31J",
        "allowable " + "stress",
        "stress " + "intensification",
        "SIF " + "table",
        "vendor " + "catalog",
        "real " + "secret",
        "private " + "key",
        "BEGIN " + "RSA",
        "BEGIN " + "OPENSSH",
        "pass" + "word",
        "token" + "=",
        "CAE" + "SAR",
        "Auto" + "PIPE",
        "RO" + "HR2",
        "code " + "compliant",
        "certified by " + "openpipestress",
        "sealed by " + "openpipestress",
        "approved by " + "openpipestress",
        "professional " + "approval " + "by the software",
        "OPS_SYNTHETIC_" + "PROTECTED_TABLE",
        "OPS_SYNTHETIC_" + "CODE_FORMULA",
        "OPS_SYNTHETIC_" + "PRIVATE_RULE_PAYLOAD",
        "OPS_SYNTHETIC_" + "VENDOR_CATALOG",
    }


    def load_examples():
        assert EXAMPLE_DIR.is_dir()
        paths = sorted(EXAMPLE_DIR.glob("*.json"))
        assert {path.name for path in paths} == EXAMPLE_FILES
        return [(path, json.loads(path.read_text(encoding="utf-8"))) for path in paths]


    def load_schema(path):
        return yaml.safe_load(path.read_text(encoding="utf-8"))


    def validate_persistence_instance(schema, instance, instance_label):
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
        from referencing.jsonschema import DRAFT202012

        model_schema = load_schema(MODEL_SCHEMA_PATH)
        model_state_schema = load_schema(MODEL_STATE_SCHEMA_PATH)
        analysis_run_schema = load_schema(ANALYSIS_RUN_SCHEMA_PATH)
        registry = Registry().with_resources(
            [
                (
                    uri,
                    Resource.from_contents(schema_doc, default_specification=DRAFT202012),
                )
                for uri, schema_doc in (
                    (model_schema["$id"], model_schema),
                    ("https://openpipestress.org/schemas/model.schema.yaml", model_schema),
                    ("model.schema.yaml", model_schema),
                    (model_state_schema["$id"], model_state_schema),
                    ("https://openpipestress.org/schemas/model_state.schema.json", model_state_schema),
                    ("model_state.schema.json", model_state_schema),
                    (analysis_run_schema["$id"], analysis_run_schema),
                    ("https://openpipestress.org/schemas/analysis_run.schema.json", analysis_run_schema),
                    ("analysis_run.schema.json", analysis_run_schema),
                )
            ]
        )
        validator = Draft202012Validator(schema, registry=registry)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if errors:
            formatted = "\n".join(format_schema_error(error) for error in errors[:10])
            raise AssertionError(f"{instance_label} failed JSON Schema validation:\n{formatted}")


    def format_schema_error(error):
        path = "$"
        for part in error.path:
            path += f"[{part}]" if isinstance(part, int) else f".{part}"
        return f"{path}: {error.message}"


    def artifact_ref(ref_kind, ref):
        return {"ref_kind": ref_kind, "ref": ref}


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def test_invented_examples_follow_model_contract_shape():
        for path, example in load_examples():
            assert example["schema_version"] == "0.1.0", path
            project = example["project"]
            assert REQUIRED_PROJECT_KEYS <= set(project), path
            assert project["privacy_class"] == "public", path
            assert project["storage_policy"] == "public_example", path
            assert project["models"], path

            model_roles = {model["model_role"] for model in project["models"]}
            assert {"physical_source_of_truth", "analytical_solver_model"} <= model_roles

            physical_models = {
                model["id"]: model
                for model in project["models"]
                if model["model_role"] == "physical_source_of_truth"
            }
            assert len(physical_models) == 1

            for model in project["models"]:
                assert REQUIRED_MODEL_KEYS <= set(model), (path, model["id"])
                assert model["nodes"]
                assert model["elements"]
                assert model["materials"]
                assert model["sections"]
                assert model["load_cases"]
                assert model["combinations"]
                if model["model_role"] == "physical_source_of_truth":
                    assert model["results"] == []
                    assert model["traceability_links"] == []
                else:
                    assert model["model_role"] == "analytical_solver_model"
                    assert model["source_model_ref"]["id"] in physical_models
                    assert model["results"]
                    assert any(
                        link["trace_type"] == "physical_to_analytical"
                        and link["source_ref"] == model["source_model_ref"]
                        and link["target_ref"] == {"object_type": "Model", "id": model["id"]}
                        for link in model["traceability_links"]
                    ), (path, model["id"])


    def test_invented_examples_validate_against_full_model_schema():
        schema = load_schema(MODEL_SCHEMA_PATH)

        for path, example in load_examples():
            validate_instance(
                schema,
                example,
                schema_label=str(MODEL_SCHEMA_PATH.relative_to(ROOT)),
                instance_label=str(path.relative_to(ROOT)),
            )


    def test_invented_examples_carry_concrete_hashes_for_published_payloads():
        rule_pack_digest = sha256(RULE_PACK_PATH.read_bytes()).hexdigest()

        for path, example in load_examples():
            project = example["project"]
            hashes = project["hashes"]
            assert len(hashes) == 1, path
            project_hash = hashes[0]
            assert project_hash["algorithm"] == "sha256", path
            assert project_hash["canonicalization"] == "JCS", path
            assert project_hash["value"].startswith("sha256:"), path

            project_without_hashes = deepcopy(project)
            project_without_hashes["hashes"] = []
            expected = "sha256:" + sha256(
                canonical_json(project_without_hashes).encode("utf-8")
            ).hexdigest()
            assert project_hash["value"] == expected, path

            for ref in project["rule_pack_refs"]:
                checksum = ref["checksum"]
                assert checksum["algorithm"] == "sha256", path
                assert checksum["canonicalization"] == "NONE", path
                assert checksum["value"] == f"sha256:{rule_pack_digest}", path


    def test_invented_examples_persist_and_round_trip_with_schema_validation():
        persistence_schema = load_schema(PERSISTENCE_SCHEMA_PATH)

        for path, example in load_examples():
            project = example["project"]
            envelope = build_project_persistence_envelope(
                project_id=project["id"],
                project_name=project["name"],
                model_payload=example,
                model_state_refs=[
                    artifact_ref("model_state", f"model-state:{project['id']}:invented-preview")
                ],
                analysis_run_refs=[
                    artifact_ref("analysis_run", f"analysis-run:{project['id']}:invented-preview")
                ],
                result_envelope_refs=[
                    artifact_ref("result_envelope", f"result-envelope:{project['id']}:invented-preview")
                ],
                result_refs=[
                    artifact_ref("result", f"result:{model['id']}:{result['id']}")
                    for model in project["models"]
                    for result in model["results"]
                ],
                provenance_manifest=[
                    model["provenance"]
                    for model in project["models"]
                    if model["model_role"] == "physical_source_of_truth"
                ],
            )

            validate_persistence_instance(
                persistence_schema,
                envelope,
                f"persistence envelope for {path.relative_to(ROOT)}",
            )
            assert validate_project_persistence_envelope(envelope) == []
            assert project_hash_manifest(envelope) == envelope["hash"]["hash_manifest"]

            round_trip = round_trip_project_envelope(envelope)
            assert round_trip["serialization"] == "canonical_json_jcs"
            assert round_trip["semantic_equal"] is True
            assert round_trip["diagnostics"] == []
            assert round_trip["source_hash"]["value"] == round_trip["round_trip_hash"]["value"]


    def test_invented_examples_carry_non_reliance_notices():
        for path, example in load_examples():
            text = "\n".join(walk_strings(example)).lower()
            for required in REQUIRED_NOTICE_TEXT:
                assert required in text, (path, required)
            assert "HUMAN_" + "APPROVED_FOR_PROJECT" not in text


    def test_invented_examples_do_not_contain_protected_or_private_markers():
        for path, example in load_examples():
            text = "\n".join(walk_strings(example))
            text_lower = text.lower()
            for forbidden in FORBIDDEN_TEXT:
                haystack = text if forbidden != forbidden.lower() else text_lower
                needle = forbidden if forbidden != forbidden.lower() else forbidden.lower()
                assert needle not in haystack, (path, forbidden)


    def test_fake_rule_example_links_only_invented_public_rule_pack():
        _, fake_rule = next(
            (path, example)
            for path, example in load_examples()
            if path.name == "fake_rule_pack_toy_model.json"
        )
        refs = fake_rule["project"]["rule_pack_refs"]
        assert len(refs) == 1
        ref = refs[0]
        assert ref["id"] == "INV_FAKE_RULE_PACK_REF"
        assert ref["redistribution_status"] == "public_permissive"
        assert "invented" in ref["source_notice"].lower()
        assert "engineering acceptance basis" in ref["source_notice"].lower()

## Component: tests/test_library_import_provenance.py

    #!/usr/bin/env python3
    """Checks for public/private library import provenance validation."""

    import copy
    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))

    from core.library_import.provenance_checker import validate_library_import  # noqa: E402


    MATERIAL_FIXTURE = ROOT / "fixtures" / "material" / "invented_material_library_valid.json"
    COMPONENT_FIXTURE = ROOT / "fixtures" / "component" / "invented_section_component_library_valid.json"


    def load_json(path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def accepted_public_component_payload():
        payload = copy.deepcopy(load_json(COMPONENT_FIXTURE))
        payload["component_library"]["library_scope"] = "public_permissive_reviewed"
        payload["component_library"]["privacy_class"] = "public_permissive_reviewed"
        payload["component_library"]["review_status"] = "accepted"
        payload["component_library"]["provenance"]["source_license"] = "public test license"
        payload["component_library"]["provenance"]["redistribution_status"] = "public_permissive"
        payload["component_library"]["provenance"]["review_status"] = "accepted"
        payload["component_records"] = [
            {
                "component_id": "comp.public.example",
                "name": "Public Reviewed Example",
                "component_type": "other",
                "privacy_class": "public_permissive_reviewed",
                "redistribution_status": "public_permissive",
                "fields": [
                    {
                        "field_id": "comp.public.example.weight",
                        "field_kind": "weight",
                        "value_status": "public_permissive_reviewed",
                        "public_repository_value_policy": "public_permissive_reviewed_only",
                        "required_for": "mechanics_solve",
                        "value": {
                            "magnitude": 1.0,
                            "unit": "N",
                            "dimension": "force",
                            "value_status": "public_permissive_reviewed",
                            "provenance": {
                                "source_name": "Invented permissive test source",
                                "source_location": "tests/test_library_import_provenance.py",
                                "source_license": "public test license",
                                "contributor": "OpenPipeStress",
                                "contributor_certification": "invented non-engineering value",
                                "redistribution_status": "public_permissive",
                                "review_status": "accepted",
                            },
                        },
                        "provenance": {
                            "source_name": "Invented permissive test source",
                            "source_location": "tests/test_library_import_provenance.py",
                            "source_license": "public test license",
                            "contributor": "OpenPipeStress",
                            "contributor_certification": "invented non-engineering value",
                            "redistribution_status": "public_permissive",
                            "review_status": "accepted",
                        },
                        "review_status": "accepted",
                    }
                ],
                "completeness": [],
                "provenance": {
                    "source_name": "Invented permissive test source",
                    "source_location": "tests/test_library_import_provenance.py",
                    "source_license": "public test license",
                    "contributor": "OpenPipeStress",
                    "contributor_certification": "invented non-engineering value",
                    "redistribution_status": "public_permissive",
                    "review_status": "accepted",
                },
                "review_status": "accepted",
            }
        ]
        return payload


    def codes(result):
        return {finding.code for finding in result.findings}


    def test_public_component_import_requires_accepted_public_provenance():
        result = validate_library_import(
            accepted_public_component_payload(),
            library_kind="component",
            intended_visibility="public",
        )
        assert result.accepted is True
        assert result.outcome == "ACCEPTED_PUBLIC"
        assert result.findings == ()


    def test_public_material_import_with_tbd_rights_is_rejected_for_review():
        result = validate_library_import(
            load_json(MATERIAL_FIXTURE),
            library_kind="material",
            intended_visibility="public",
        )
        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "IMPORT_REDIS_RIGHTS_MISSING" in codes(result)
        assert "IMPORT_REVIEW_REQUIRED" in codes(result)


    def test_private_material_import_can_remain_local_with_tbd_rights():
        result = validate_library_import(
            load_json(MATERIAL_FIXTURE),
            library_kind="material",
            intended_visibility="private",
        )
        assert result.accepted is True
        assert result.outcome == "PRIVATE_LOCAL_ONLY"
        assert "IMPORT_REDIS_RIGHTS_MISSING" not in codes(result)


    def test_missing_provenance_blocks_import_without_defaults():
        payload = copy.deepcopy(load_json(MATERIAL_FIXTURE))
        del payload["material_records"][0]["provenance"]
        result = validate_library_import(
            payload,
            library_kind="material",
            intended_visibility="public",
        )
        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "IMPORT_PROVENANCE_MISSING" in codes(result)


    def test_protected_suspected_metadata_quarantines_import():
        payload = copy.deepcopy(load_json(MATERIAL_FIXTURE))
        payload["material_library"]["provenance"]["redistribution_status"] = "protected_suspected"
        result = validate_library_import(
            payload,
            library_kind="material",
            intended_visibility="private",
        )
        assert result.accepted is False
        assert result.outcome == "QUARANTINE"
        assert "IMPORT_PROTECTED_CONTENT_SUSPECTED" in codes(result)


    def test_unit_metadata_is_preserved_for_imported_values():
        payload = accepted_public_component_payload()
        del payload["component_records"][0]["fields"][0]["value"]["unit"]
        result = validate_library_import(
            payload,
            library_kind="component",
            intended_visibility="public",
        )
        assert result.accepted is False
        assert result.outcome == "REJECTED"
        assert "IMPORT_UNIT_METADATA_MISSING" in codes(result)


    def test_import_findings_map_to_pkg02_diagnostic_envelope():
        payload = accepted_public_component_payload()
        del payload["component_records"][0]["fields"][0]["value"]["unit"]
        result = validate_library_import(
            payload,
            library_kind="component",
            intended_visibility="public",
        )

        diagnostic = next(
            item
            for item in result.diagnostics
            if item["code"] == "IMPORT_UNIT_METADATA_MISSING"
        )
        assert diagnostic["class"] == "import_boundary"
        assert diagnostic["source"] == "core.library_import.provenance_checker"
        assert diagnostic["affected_object"].endswith(".fields[0].value")
        assert diagnostic["remediation"]
        assert diagnostic["provenance"]["source_name"] == "library_import_payload"


    if __name__ == "__main__":
        test_public_component_import_requires_accepted_public_provenance()
        test_public_material_import_with_tbd_rights_is_rejected_for_review()
        test_private_material_import_can_remain_local_with_tbd_rights()
        test_missing_provenance_blocks_import_without_defaults()
        test_protected_suspected_metadata_quarantines_import()
        test_unit_metadata_is_preserved_for_imported_values()
        test_import_findings_map_to_pkg02_diagnostic_envelope()

## Component: tests/test_local_fea_handoff_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the local FEA handoff contract."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "local_fea_handoff.schema.yaml"
    GUIDANCE_PATH = ROOT / "docs" / "local_analysis" / "local_fea_handoff_guidance.md"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_items",
        "objective",
        "contract_status",
        "handoff_package",
    }

    REQUIRED_DEFS = {
        "Assumption",
        "ChecksumRef",
        "ContractStatus",
        "Diagnostic",
        "EntityIds",
        "GuidanceAssessment",
        "HandoffGuidanceLabel",
        "HandoffPackage",
        "LocalRegion",
        "PrivacyContext",
        "ProfessionalBoundary",
        "Provenance",
        "Reference",
        "Reproducibility",
        "SourceRefs",
        "TransferBasis",
        "UnitsManifest",
        "UnsupportedBehaviorFlag",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "LOCAL_HANDOFF_BLOCKING",
        "LOCAL_HANDOFF_WARNING",
        "PRIVACY_WARNING",
        "EXPORT_BLOCKING",
    }

    REQUIRED_GUIDANCE_LABELS = {
        "global_centerline_expected_sufficient_for_screening",
        "local_detail_review_consider",
        "local_shell_solid_handoff_consider",
        "global_to_local_transfer_inputs_incomplete",
        "human_review_required",
        "TBD",
    }

    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_guidance():
        return GUIDANCE_PATH.read_text(encoding="utf-8")


    def normalize_text(value):
        return " ".join(value.split())


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_schema()
        guidance = load_guidance()
        defs = schema["$defs"]

        assert GUIDANCE_PATH.exists()
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)
        assert "SourceSnapshotRef" not in defs
        assert "HandoffHashManifest" not in defs

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-10-03"
        assert schema["properties"]["package_id"]["const"] == "PKG-10"
        assert {"SOW-031", "SOW-049"} <= set(
            schema["properties"]["scope_items"]["items"]["enum"]
        )
        assert schema["properties"]["objective"]["const"] == "OBJ-009"

        status = defs["ContractStatus"]["properties"]
        assert status["contract_kind"]["const"] == (
            "schema_first_local_fea_handoff_contract"
        )
        assert status["global_analysis_role"]["const"] == (
            "primary_global_centerline_frame_model"
        )
        assert status["local_analysis_role"]["const"] == (
            "optional_specialized_shell_solid_handoff"
        )
        for key in [
            "concrete_export_format",
            "target_solver_adapter",
            "mesh_generation",
            "external_solver_invocation",
        ]:
            assert status[key]["const"] == "TBD"
        assert status["professional_decision"]["const"] == "human_review_required"

        package_required = required_at(schema, "HandoffPackage")
        assert {
            "source_refs",
            "local_region",
            "units_manifest",
            "entity_ids",
            "transfer_basis",
            "guidance_assessment",
            "assumptions",
            "unsupported_behavior_flags",
            "warnings",
            "diagnostics",
            "privacy",
            "provenance",
            "professional_boundary",
            "reproducibility",
        } <= package_required
        package = defs["HandoffPackage"]["properties"]
        assert package["source_refs"]["$ref"] == "#/$defs/SourceRefs"
        assert package["reproducibility"]["$ref"] == "#/$defs/Reproducibility"

        source_required = required_at(schema, "SourceRefs")
        assert {
            "project_ref",
            "model_ref",
            "result_envelope_ref",
            "global_model_kind",
            "model_hash",
            "result_hash",
        } <= source_required
        assert (
            defs["SourceRefs"]["properties"]["global_model_kind"]["const"]
            == "centerline_frame_global_analysis"
        )

        units_required = required_at(schema, "UnitsManifest")
        assert {
            "coordinate_unit",
            "force_unit",
            "moment_unit",
            "displacement_unit",
            "rotation_unit",
            "stress_unit",
            "temperature_unit",
        } <= units_required
        assert "schemas/units.schema.yaml" in defs["UnitsManifest"]["properties"][
            "dimension_basis"
        ]["enum"]

        entity_required = required_at(schema, "EntityIds")
        assert {
            "component_ids",
            "node_ids",
            "element_ids",
            "station_ids",
            "load_case_ids",
            "result_ids",
        } <= entity_required

        transfer_required = required_at(schema, "TransferBasis")
        assert {
            "load_case_refs",
            "displacement_result_refs",
            "force_result_refs",
            "moment_result_refs",
            "boundary_condition_refs",
            "cut_boundary_refs",
            "transfer_method_label",
            "limitations",
        } <= transfer_required
        assert {
            "result_reference_only",
            "user_reviewed_interpolation_reference",
            "TBD",
        } <= set(defs["TransferBasis"]["properties"]["transfer_method_label"]["enum"])

        assessment_required = required_at(schema, "GuidanceAssessment")
        assert {
            "labels",
            "criteria_input_refs",
            "rationale_refs",
            "human_review_required",
            "software_makes_approval_claim",
            "software_makes_compliance_claim",
            "software_makes_certification_claim",
            "software_makes_sealing_claim",
        } <= assessment_required
        assert REQUIRED_GUIDANCE_LABELS <= enum_at(schema, "HandoffGuidanceLabel")
        assessment = defs["GuidanceAssessment"]["properties"]
        assert assessment["labels"]["contains"]["const"] == "human_review_required"
        assert assessment["human_review_required"]["const"] is True
        assert assessment["software_makes_approval_claim"]["const"] is False
        assert assessment["software_makes_compliance_claim"]["const"] is False
        assert assessment["software_makes_certification_claim"]["const"] is False
        assert assessment["software_makes_sealing_claim"]["const"] is False

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        privacy = defs["PrivacyContext"]["properties"]
        assert privacy["local_only"]["const"] is True
        assert privacy["telemetry_allowed"]["const"] is False
        assert privacy["private_payload_embedded"]["const"] is False
        assert "user_supplied_private_reference" in privacy["classification"]["enum"]
        assert "protected_suspected" in privacy["classification"]["enum"]

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False

        flags = defs["UnsupportedBehaviorFlag"]["properties"]
        assert {
            "mesh_generation_not_performed",
            "external_solver_not_invoked",
            "target_format_not_selected",
            "boundary_transfer_requires_review",
            "local_detail_assumption_unresolved",
            "approximate_global_to_local_transfer",
        } <= set(flags["behavior_label"]["enum"])
        assert {"unsupported", "approximate", "requires_human_review", "TBD"} <= set(
            flags["status"]["enum"]
        )

        checksum = defs["ChecksumRef"]["properties"]
        assert "JCS-compatible-json" in checksum["canonicalization"]["enum"]

        normalized_guidance = normalize_text(guidance)
        for label in REQUIRED_GUIDANCE_LABELS:
            assert f"`{label}`" in guidance
        assert "They do not certify" in normalized_guidance
        assert "Final engineering reliance remains a human responsibility" in (
            normalized_guidance
        )
        assert "Target solver, mesh, and exchange format remain separate decisions" in (
            normalized_guidance
        )
        assert "solver-specific execution semantics are outside DEL-10-03" in (
            normalized_guidance
        )


    def test_local_fea_handoff_contract():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_material_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the material library schema."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )

    SCHEMA_PATH = ROOT / "schemas" / "material.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "material" / "invented_material_library_valid.json"

    CANONICAL_DIMENSIONS = {
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    }

    RETIRED_DIMENSIONS = {
        "temperature_difference",
        "area_moment",
        "conductivity",
        "stiffness",
    }

    REQUIRED_TOP_LEVEL = {
        "schema_version",
        "material_library",
        "material_records",
        "property_definitions",
        "completeness_rules",
        "diagnostics",
        "open_decisions",
    }

    REQUIRED_MATERIAL_FIELDS = {
        "material_id",
        "name",
        "material_family",
        "privacy_class",
        "redistribution_status",
        "properties",
        "allowables",
        "completeness",
        "provenance",
        "review_status",
    }

    REQUIRED_PROVENANCE_FIELDS = {
        "source_name",
        "source_location",
        "source_license",
        "contributor",
        "contributor_certification",
        "redistribution_status",
        "review_status",
    }

    FORBIDDEN_PUBLIC_DATA_TEXT = {
        "ASME",
        "B31",
        "ASTM",
        "CODE_COMPLIANT",
        "certified material",
        "sealed",
        "automatic compliance",
        "professional approval by the software",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def main():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_TOP_LEVEL <= set(schema["required"])

        assert REQUIRED_MATERIAL_FIELDS <= required_at(schema, "MaterialRecord")
        assert REQUIRED_PROVENANCE_FIELDS <= required_at(schema, "Provenance")
        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "rejected",
            "TBD",
        } <= enum_at(schema, "RedistributionStatus")

        assert {
            "density",
            "elastic_modulus",
            "poisson_ratio",
            "thermal_expansion_coefficient",
            "allowable_stress",
            "user_defined",
            "TBD",
        } <= enum_at(schema, "MaterialPropertyKind")
        assert {
            "density",
            "stress",
            "temperature",
            "temperature_interval",
            "thermal_conductivity",
            "specific_heat",
            "thermal_expansion_coefficient",
            "dimensionless",
            "TBD",
        } <= enum_at(schema, "MaterialPropertyDimension")
        material_dimensions = enum_at(schema, "MaterialPropertyDimension")
        assert material_dimensions <= CANONICAL_DIMENSIONS
        assert not (material_dimensions & RETIRED_DIMENSIONS)

        allowable = defs["MaterialAllowableSlot"]
        assert {
            "allowable_id",
            "allowable_kind",
            "value_status",
            "public_repository_value_policy",
            "required_for",
            "provenance",
            "review_status",
        } <= set(allowable["required"])
        assert "no_public_code_specific_values" in set(
            allowable["properties"]["public_repository_value_policy"]["enum"]
        )
        assert "private_user_supplied_only" in set(
            allowable["properties"]["public_repository_value_policy"]["enum"]
        )

        completeness_rule = defs["CompletenessRule"]
        assert {
            "rule_id",
            "applies_to",
            "required_property_kinds",
            "required_for",
            "missing_behavior",
            "diagnostic_code",
            "review_status",
        } <= set(completeness_rule["required"])
        assert "diagnostic_blocking" in set(
            completeness_rule["properties"]["missing_behavior"]["enum"]
        )

        diagnostic_codes = enum_at(schema, "MaterialDiagnosticCode")
        assert {
            "MATERIAL_PROPERTY_MISSING",
            "MATERIAL_UNIT_MISSING",
            "MATERIAL_PROVENANCE_MISSING",
            "MATERIAL_PROTECTED_CONTENT_SUSPECTED",
            "MATERIAL_ALLOWABLE_NOT_PUBLIC",
        } <= diagnostic_codes
        assert {"class", "source"} <= required_at(schema, "MaterialDiagnostic")

        open_decision = defs["OpenDecision"]
        assert {
            "public_material_fixture_policy",
            "accepted_material_source_catalog",
            "allowable_value_storage_policy",
            "temperature_interpolation_policy",
        } <= set(open_decision["properties"]["topic"]["enum"])

        assert fixture["material_library"]["library_scope"] == "public_schema_fixture"
        assert fixture["material_records"][0]["redistribution_status"] == "TBD"
        assert (
            fixture["material_records"][0]["allowables"][0][
                "public_repository_value_policy"
            ]
            == "no_public_code_specific_values"
        )
        assert fixture["material_records"][0]["completeness"][0]["status"] == "incomplete"
        assert fixture["diagnostics"][0]["code"] == "MATERIAL_PROPERTY_MISSING"
        assert fixture["diagnostics"][0]["class"] == "SOLVE_BLOCKING"
        assert fixture["diagnostics"][0]["source"] == (
            "fixtures/material/invented_material_library_valid.json"
        )

        all_text = "\n".join([*walk_strings(schema), *walk_strings(fixture)])
        for forbidden in FORBIDDEN_PUBLIC_DATA_TEXT:
            assert forbidden not in all_text


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(FIXTURE_PATH),
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_material_schema_contract():
        main()


    def test_material_schema_jsonschema_validation_helper():
        check_jsonschema_validation()


    if __name__ == "__main__":
        main()
        check_jsonschema_validation()

## Component: tests/test_missing_data_warning_ux.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-04 warning/blocking UX contracts."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.warnings import build_warning_ux_contract, canonical_json  # noqa: E402


    def main():
        record = build_warning_ux_contract(
            warning_set_id="invented-warning-set",
            conditions=[
                {
                    "warning_id": "warn-missing-support",
                    "warning_class": "incomplete_data",
                    "target_ref": {"ref_type": "support", "ref_id": "support-TBD"},
                    "message": "Invented support has unresolved stiffness.",
                    "source_status": "missing",
                },
                {
                    "warning_id": "warn-assumption",
                    "warning_class": "assumption",
                    "target_ref": {"ref_type": "load_case", "ref_id": "load-1"},
                    "source_status": "provided",
                    "assumption_ref": {"ref_type": "assumption", "ref_id": "assumption-1"},
                },
            ],
        )
        assert record["deliverable_id"] == "DEL-07-04"
        assert record["auto_fill_missing_data"] is False
        assert record["blocking_summary"]["has_blocking_items"] is True
        assert record["blocking_summary"]["blocking_warning_ids"] == ["warn-missing-support"]
        assert record["analysis_boundary_contract"]["contract_ref"] == "DEL-02-03"
        assert "USER_RULE_FAILED" in record["analysis_boundary_contract"]["local_warning_class_status_map"]["diagnostic"]
        assert record["warnings"][0]["analysis_boundary_mapping"]["human_acceptance_record_policy"] == (
            "external_hash_bound_human_record_only"
        )
        assert record["warnings"][0]["professional_boundary_preserved"] is True
        assert any(item["code"] == "WARNING_SOURCE_STATUS_UNRESOLVED" for item in record["diagnostics"])
        assert "professional acceptance" not in canonical_json(record).lower()


    def test_missing_data_warning_ux_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_model_operation_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the structured model operation schema."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT / "tests") not in sys.path:
        sys.path.insert(0, str(ROOT / "tests"))

    from schema_validation import validate_instance, validate_schema_document  # noqa: E402

    SCHEMA_PATH = ROOT / "schemas" / "model_operation.schema.json"
    FIXTURE_PATH = ROOT / "fixtures" / "model_operations" / "invented_operation_set_valid.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "operation_contract_status",
        "operation_set",
    }

    REQUIRED_DEFS = {
        "AssumptionRecord",
        "Checksum",
        "Diagnostic",
        "DiffPreviewRef",
        "Id",
        "ModelOperationRecord",
        "OperationAuthorType",
        "OperationChange",
        "OperationContractStatus",
        "OperationKind",
        "OperationModelBasis",
        "OperationPrecondition",
        "OperationSet",
        "OperationStatus",
        "OperationValidation",
        "OperationValuePayload",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "Quantity",
        "RedistributionStatus",
        "Reference",
        "ReviewStatus",
        "UnitRequirements",
        "ValidationState",
    }

    REQUIRED_OPERATION_KINDS = {
        "add",
        "move",
        "modify",
        "delete",
        "reconnect",
        "constraint",
        "load",
        "support",
        "design_knowledge",
    }

    FORBIDDEN_STATUS = {
        "agent_accepted_engineering_state",
        "auto_approved",
        "code_compliant",
        "certified",
        "sealed",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "code compliant",
        "certified by software",
        "sealed by software",
        "professional approval by the software",
    }

    CANONICAL_DIMENSIONS = [
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ]


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture():
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]
        validate_schema_document(schema, schema_label="model_operation.schema.json")

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-16-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-16"
        assert schema["properties"]["scope_item"]["const"] == "SOW-069"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-015"

        contract = defs["OperationContractStatus"]["properties"]
        assert contract["record_contract"]["const"] == "schema_first_model_operation_records"
        assert contract["mutation_route"]["const"] == "structured_operations_only"
        assert contract["direct_model_mutation_allowed"]["const"] is False
        assert contract["user_acceptance_boundary"]["const"] == (
            "downstream_user_acceptance_required"
        )
        assert contract["diff_preview_binding"]["const"] == "downstream_DEL-16-02"
        assert contract["audit_trail_binding"]["const"] == "downstream_DEL-16-03"

        assert REQUIRED_OPERATION_KINDS <= enum_at(schema, "OperationKind")
        assert {"user", "agent", "import_adapter", "project_template"} <= enum_at(
            schema, "OperationAuthorType"
        )
        operation_status = enum_at(schema, "OperationStatus")
        assert {
            "proposed",
            "schema_validated",
            "blocked_by_diagnostics",
            "ready_for_user_review",
            "rejected",
        } <= operation_status
        assert operation_status.isdisjoint(FORBIDDEN_STATUS)

        set_required = required_at(schema, "OperationSet")
        assert {
            "operation_set_id",
            "project_ref",
            "model_ref",
            "model_basis",
            "operations",
            "diagnostics",
            "provenance",
            "professional_boundary",
        } <= set_required
        model_basis_required = required_at(schema, "OperationModelBasis")
        assert {
            "model_ref",
            "canonical_model_role",
            "physical_source_of_truth_ref",
            "accepted_model_state_ref",
            "accepted_model_state_hash",
        } <= model_basis_required
        assert defs["OperationModelBasis"]["properties"]["canonical_model_role"]["const"] == "physical_source_of_truth"

        operation_required = required_at(schema, "ModelOperationRecord")
        assert {
            "operation_id",
            "operation_kind",
            "operation_status",
            "author_type",
            "target_refs",
            "preconditions",
            "changes",
            "validation",
            "diagnostics",
            "diff_preview_refs",
            "assumptions",
            "provenance",
            "professional_boundary",
        } <= operation_required

        precondition_required = required_at(schema, "OperationPrecondition")
        assert {
            "base_model_state_ref",
            "required_current_hashes",
            "required_refs",
            "assumptions",
        } <= precondition_required

        change_required = required_at(schema, "OperationChange")
        assert {
            "change_id",
            "change_kind",
            "target_object_type",
            "target_ref",
            "value_payload",
            "unit_requirements",
            "provenance",
        } <= change_required
        assert {
            "add_object",
            "remove_object",
            "set_field",
            "move_geometry",
            "reconnect",
            "update_constraint",
            "update_load",
            "update_support",
            "attach_design_knowledge",
        } <= set(defs["OperationChange"]["properties"]["change_kind"]["enum"])

        validation_required = required_at(schema, "OperationValidation")
        assert {
            "schema_validation",
            "constraint_validation",
            "unit_validation",
            "diff_preview_status",
            "application_status",
        } <= validation_required
        assert {
            "not_applied",
            "held_for_user_review",
            "downstream_application_required",
        } <= set(defs["OperationValidation"]["properties"]["application_status"]["enum"])

        units = defs["UnitRequirements"]["properties"]
        assert units["unit_metadata_required"]["const"] is True
        assert units["dimension_check_required"]["const"] is True
        assert units["missing_unit_behavior"]["const"] == "emit_diagnostic"
        assert defs["Quantity"]["properties"]["dimension"]["enum"] == CANONICAL_DIMENSIONS

        professional = defs["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings

        fixture = load_fixture()
        validate_instance(
            schema,
            fixture,
            schema_label="model_operation.schema.json",
            instance_label="invented_operation_set_valid.json",
        )
        operations = fixture["operation_set"]["operations"]
        assert {item["operation_kind"] for item in operations} >= REQUIRED_OPERATION_KINDS
        assert {
            change["change_kind"]
            for operation in operations
            for change in operation["changes"]
        } >= {
            "add_object",
            "remove_object",
            "set_field",
            "move_geometry",
            "reconnect",
            "update_constraint",
            "update_load",
            "update_support",
            "attach_design_knowledge",
        }
        assert fixture["operation_set"]["model_basis"]["canonical_model_role"] == "physical_source_of_truth"
        for operation in operations:
            assert any(
                item["payload_scope"] == "model_state_record"
                for item in operation["preconditions"]["required_current_hashes"]
            )


    if __name__ == "__main__":
        main()

## Component: tests/test_model_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the canonical domain model schema."""

    import json
    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        schema_for_definition,
        validate_instance,
        validate_schema_document,
    )

    SCHEMA_PATH = ROOT / "schemas" / "model.schema.yaml"
    MINIMAL_PROJECT_FIXTURE = ROOT / "fixtures" / "domain" / "invented_minimal_project_model.json"
    PHYSICAL_MODEL_FIXTURE = ROOT / "fixtures" / "domain" / "invented_physical_source_of_truth_model.json"

    REQUIRED_DEFS = {
        "Assumption",
        "Project",
        "Model",
        "ModelRole",
        "Node",
        "Element",
        "Component",
        "Material",
        "Section",
        "Support",
        "LoadCase",
        "Combination",
        "RulePackRef",
        "Result",
        "ReportSettings",
        "Report",
        "Quantity",
        "Provenance",
        "Diagnostic",
        "Checksum",
        "Reference",
        "TraceabilityLink",
        "DirectionVector",
        "NodalForceLoadRecord",
        "NodalMomentLoadRecord",
        "ElementPointForceLoadRecord",
        "ElementUniformDistributedForceLoadRecord",
    }

    REQUIRED_ANALYSIS_STATUSES = {
        "MODEL_INCOMPLETE",
        "MECHANICS_SOLVED",
        "RULE_INPUTS_INCOMPLETE",
        "USER_RULE_CHECKED",
        "USER_RULE_FAILED",
        "HUMAN_REVIEW_REQUIRED",
        "HUMAN_APPROVED_FOR_PROJECT",
    }

    CANONICAL_DIMENSIONS = [
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ]

    RETIRED_DIMENSIONS = {
        "temperature_difference",
        "area_moment",
        "stiffness",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "CODE_COMPLIANT",
        "ASME",
        "B31",
        "certified",
        "sealed",
        "automatic compliance",
        "professional approval by the software",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_json(path):
        with path.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def provenance():
        return {
            "source_name": "PKG-02 invented schema test",
            "source_location": "tests/test_model_schema.py",
            "source_license": "project invented public example",
            "contributor": "OpenPipeStress Type 2 worker",
            "contributor_certification": "invented non-engineering example",
            "redistribution_status": "public_permissive",
            "review_status": "accepted",
        }


    def quantity(value, unit, dimension):
        return {
            "value": value,
            "unit": unit,
            "dimension": dimension,
            "provenance": provenance(),
        }


    def reference(object_type, object_id):
        return {
            "object_type": object_type,
            "id": object_id,
        }


    def normalized_minimal_fixture_for_current_schema():
        fixture = load_json(MINIMAL_PROJECT_FIXTURE)
        load = fixture["project"]["models"][0]["load_cases"][0]["loads"][0]
        load["load_record_type"] = "nodal_force"
        return fixture


    def normalized_physical_fixture_for_current_schema():
        fixture = load_json(PHYSICAL_MODEL_FIXTURE)
        physical_model = fixture["model"]
        for element in physical_model["elements"]:
            if element["element_type"] == "straight_pipe":
                coordinate_system = element["local_coordinate_system"]
                coordinate_system["y_reference"] = [0.0, 1.0, 0.0]
                coordinate_system["provenance"] = physical_model["provenance"]
        loads = physical_model["load_cases"][0]["loads"]
        loads[0]["load_record_type"] = "element_uniform_distributed_force"
        loads[0]["quantity"]["unit"] = "N/m"
        loads[0]["quantity"]["dimension"] = "force_per_length"
        loads[0]["span"] = {
            "start_fraction": quantity(0.0, "1", "dimensionless"),
            "end_fraction": quantity(1.0, "1", "dimensionless"),
        }
        loads[1]["load_record_type"] = "element_point_force"
        loads[1]["station_fraction"] = quantity(0.5, "1", "dimensionless")
        loads[2]["load_record_type"] = "nodal_moment"
        loads[2]["target_ref"] = reference("Node", "N-1")
        return fixture


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def assert_required_fields(schema, definition_name, record):
        assert required_at(schema, definition_name) <= set(record)


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert {"schema_version", "project"} <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert REQUIRED_ANALYSIS_STATUSES <= enum_at(schema, "AnalysisStatus")
        assert "CODE_COMPLIANT" not in enum_at(schema, "AnalysisStatus")

        assert {
            "id",
            "name",
            "unit_system",
            "privacy_class",
            "storage_policy",
            "models",
            "rule_pack_refs",
            "report_settings",
            "reports",
            "diagnostics",
            "hashes",
        } <= required_at(schema, "Project")

        assert {
            "model_role",
            "nodes",
            "elements",
            "components",
            "materials",
            "sections",
            "supports",
            "load_cases",
            "combinations",
            "results",
            "diagnostics",
            "unresolved_assumptions",
            "traceability_links",
            "design_knowledge_refs",
            "constraint_refs",
            "equipment_interface_refs",
            "operation_refs",
            "model_state_refs",
            "analysis_run_refs",
            "comparison_refs",
            "handoff_package_refs",
            "external_reference_refs",
            "provenance",
        } <= required_at(schema, "Model")
        assert {
            "physical_source_of_truth",
            "analytical_solver_model",
            "derived_view",
            "TBD",
        } <= enum_at(schema, "ModelRole")

        assert {"id", "statement", "status", "affected_refs", "provenance"} <= required_at(
            schema, "Assumption"
        )
        assert {"unresolved", "resolved", "rejected", "TBD"} <= set(
            defs["Assumption"]["properties"]["status"]["enum"]
        )

        assert {
            "id",
            "trace_type",
            "source_ref",
            "target_ref",
            "diagnostics",
            "provenance",
        } <= required_at(schema, "TraceabilityLink")
        assert {
            "physical_to_analytical",
            "operation_application",
            "state_snapshot",
            "analysis_run",
            "comparison",
            "handoff",
            "external_reference",
            "TBD",
        } <= set(defs["TraceabilityLink"]["properties"]["trace_type"]["enum"])

        assert {
            "DesignKnowledge",
            "Constraint",
            "EquipmentInterface",
            "ModelOperation",
            "ModelState",
            "AnalysisRun",
            "Comparison",
            "HandoffPackage",
            "ExternalProverReference",
            "Assumption",
            "TraceabilityLink",
        } <= set(defs["Reference"]["properties"]["object_type"]["enum"])

        assert {"value", "unit", "dimension", "provenance"} <= required_at(
            schema, "Quantity"
        )
        dimensions = defs["Quantity"]["properties"]["dimension"]["enum"]
        assert dimensions == CANONICAL_DIMENSIONS
        assert not (set(dimensions) & RETIRED_DIMENSIONS)

        coordinate_system = defs["CoordinateSystem"]
        assert coordinate_system["additionalProperties"] is False
        assert {"type", "axes"} <= set(coordinate_system["required"])
        assert {"y_reference", "provenance"} <= set(coordinate_system["properties"])
        assert "local_x_axis" not in coordinate_system["properties"]
        assert defs["DirectionVector"]["minItems"] == 3
        assert defs["DirectionVector"]["maxItems"] == 3

        element_contract_text = json.dumps(defs["Element"])
        assert '"const": "straight_pipe"' in element_contract_text
        assert '"y_reference"' in element_contract_text

        assert {
            "bend",
            "elbow",
            "branch",
            "reducer",
            "valve",
            "flange",
            "expansion_joint",
            "rigid",
            "specialty",
            "other",
            "TBD",
        } <= set(defs["Component"]["properties"]["component_type"]["enum"])
        assert {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
        } <= required_at(schema, "Provenance")

        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= required_at(schema, "Diagnostic")
        assert {
            "SOLVE_BLOCKING",
            "RULE_CHECK_BLOCKING",
            "PROVENANCE_WARNING",
            "ASSUMPTION_WARNING",
            "NONLINEAR_WARNING",
            "IP_BOUNDARY_WARNING",
        } <= set(defs["Diagnostic"]["properties"]["class"]["enum"])

        assert {"algorithm", "canonicalization", "payload_ref", "value"} <= required_at(
            schema, "Checksum"
        )
        assert {"JCS", "NONE", "TBD"} <= set(
            defs["Checksum"]["properties"]["canonicalization"]["enum"]
        )

        assert [item["$ref"] for item in defs["LoadRecord"]["oneOf"]] == [
            "#/$defs/NodalForceLoadRecord",
            "#/$defs/NodalMomentLoadRecord",
            "#/$defs/ElementPointForceLoadRecord",
            "#/$defs/ElementUniformDistributedForceLoadRecord",
        ]
        for load_def in [
            "NodalForceLoadRecord",
            "NodalMomentLoadRecord",
            "ElementPointForceLoadRecord",
            "ElementUniformDistributedForceLoadRecord",
        ]:
            assert defs[load_def]["additionalProperties"] is False
            assert {
                "load_record_type",
                "target_ref",
                "direction",
                "quantity",
                "provenance",
            } <= required_at(schema, load_def)
        assert defs["NodalForceLoadRecord"]["properties"]["load_record_type"]["const"] == (
            "nodal_force"
        )
        assert defs["NodalMomentLoadRecord"]["properties"]["load_record_type"]["const"] == (
            "nodal_moment"
        )
        assert defs["ElementPointForceLoadRecord"]["properties"]["load_record_type"][
            "const"
        ] == "element_point_force"
        assert defs["ElementUniformDistributedForceLoadRecord"]["properties"][
            "load_record_type"
        ]["const"] == "element_uniform_distributed_force"
        assert defs["ForceDirection"]["enum"] == ["X", "Y", "Z"]
        assert defs["MomentDirection"]["enum"] == ["RX", "RY", "RZ"]
        assert defs["ForceQuantity"]["allOf"][1]["properties"]["dimension"]["const"] == "force"
        assert defs["MomentQuantity"]["allOf"][1]["properties"]["dimension"]["const"] == "moment"
        assert (
            defs["ForcePerLengthQuantity"]["allOf"][1]["properties"]["dimension"]["const"]
            == "force_per_length"
        )
        assert defs["FractionQuantity"]["allOf"][1]["properties"]["dimension"]["const"] == (
            "dimensionless"
        )
        assert defs["FractionQuantity"]["allOf"][1]["properties"]["value"] == {
            "minimum": 0,
            "maximum": 1,
        }
        assert {
            "id",
            "support_type",
            "target_ref",
            "directions",
            "properties",
            "provenance",
        } <= required_at(schema, "Support")

        assert {"diagnostics", "provenance"} <= required_at(schema, "Result")
        assert {
            "input_manifest",
            "hashes",
            "analysis_statuses",
            "diagnostics",
            "rule_pack_refs",
            "provenance_summary",
            "professional_boundary_notice",
        } <= required_at(schema, "Report")
        assert {"checksum", "source_notice", "required_input_refs"} <= required_at(
            schema, "RulePackRef"
        )

        all_text = "\n".join(walk_strings(schema))
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden not in all_text


    def check_domain_fixtures():
        schema = load_schema()
        minimal = load_json(MINIMAL_PROJECT_FIXTURE)
        physical = load_json(PHYSICAL_MODEL_FIXTURE)

        assert set(minimal) == {"schema_version", "project"}
        assert minimal["schema_version"] == "0.1.0"
        project = minimal["project"]
        assert_required_fields(schema, "Project", project)
        assert project["privacy_class"] == "public"
        assert project["storage_policy"] == "public_example"
        assert project["models"]

        model = project["models"][0]
        assert_required_fields(schema, "Model", model)
        assert model["model_role"] == "analytical_solver_model"
        assert model["coordinate_system"]["type"] == "cartesian"
        assert model["load_cases"], "fixture must exercise unit-bearing load records"
        quantity = model["load_cases"][0]["loads"][0]["quantity"]
        assert_required_fields(schema, "Quantity", quantity)
        assert quantity["dimension"] == "force"
        assert_required_fields(schema, "Provenance", quantity["provenance"])
        assert_required_fields(schema, "ReportSettings", project["report_settings"])
        assert_required_fields(schema, "Checksum", project["hashes"][0])

        physical_model = physical["model"]
        assert_required_fields(schema, "Model", physical_model)
        assert physical_model["model_role"] == "physical_source_of_truth"
        assert physical_model["unresolved_assumptions"]
        assert_required_fields(schema, "Assumption", physical_model["unresolved_assumptions"][0])
        assert physical_model["traceability_links"]
        assert_required_fields(schema, "TraceabilityLink", physical_model["traceability_links"][0])
        assert physical_model["diagnostics"]
        assert_required_fields(schema, "Diagnostic", physical_model["diagnostics"][0])

        fixture_text = "\n".join(
            walk_strings({"minimal": minimal, "physical": physical})
        )
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden not in fixture_text


    def check_jsonschema_validation():
        schema = load_schema()
        minimal = normalized_minimal_fixture_for_current_schema()
        physical = normalized_physical_fixture_for_current_schema()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                minimal,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(MINIMAL_PROJECT_FIXTURE),
            )
            model_schema = schema_for_definition(schema, "Model")
            assert validate_instance(
                model_schema,
                physical["model"],
                schema_label=f"{SCHEMA_PATH}#/$defs/Model",
                instance_label=f"{PHYSICAL_MODEL_FIXTURE}:model",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def check_typed_load_records_and_orientation_validation():
        schema = load_schema()
        load_record_schema = schema_for_definition(schema, "LoadRecord")
        element_schema = schema_for_definition(schema, "Element")

        valid_nodal_force = {
            "load_record_type": "nodal_force",
            "target_ref": reference("Node", "N-1"),
            "direction": "X",
            "quantity": quantity(1.0, "N", "force"),
            "provenance": provenance(),
        }
        valid_nodal_moment = {
            "load_record_type": "nodal_moment",
            "target_ref": reference("Node", "N-1"),
            "direction": "RZ",
            "quantity": quantity(1.0, "N-m", "moment"),
            "provenance": provenance(),
        }
        valid_element_point_force = {
            "load_record_type": "element_point_force",
            "target_ref": reference("Element", "E-1"),
            "station_fraction": quantity(0.5, "1", "dimensionless"),
            "direction": "Z",
            "quantity": quantity(1.0, "N", "force"),
            "provenance": provenance(),
        }
        valid_uniform_force = {
            "load_record_type": "element_uniform_distributed_force",
            "target_ref": reference("Element", "E-1"),
            "span": {
                "start_fraction": quantity(0.0, "1", "dimensionless"),
                "end_fraction": quantity(1.0, "1", "dimensionless"),
            },
            "direction": "Y",
            "quantity": quantity(1.0, "N/m", "force_per_length"),
            "provenance": provenance(),
        }
        valid_straight_pipe = {
            "id": "E-1",
            "element_type": "straight_pipe",
            "start_node_ref": reference("Node", "N-1"),
            "end_node_ref": reference("Node", "N-2"),
            "material_ref": reference("Material", "MAT-1"),
            "section_ref": reference("Section", "SEC-1"),
            "local_coordinate_system": {
                "type": "cartesian",
                "axes": ["X", "Y", "Z"],
                "y_reference": [0.0, 1.0, 0.0],
                "provenance": provenance(),
            },
            "result_stations": [quantity(0.0, "m", "length")],
        }

        try:
            for record in [
                valid_nodal_force,
                valid_nodal_moment,
                valid_element_point_force,
                valid_uniform_force,
            ]:
                assert validate_instance(load_record_schema, record)
            assert validate_instance(element_schema, valid_straight_pipe)

            invalid_moment_direction = deepcopy(valid_nodal_force)
            invalid_moment_direction["direction"] = "RX"
            assert_invalid_instance(load_record_schema, invalid_moment_direction)

            invalid_target = deepcopy(valid_element_point_force)
            invalid_target["target_ref"] = reference("Node", "N-1")
            assert_invalid_instance(load_record_schema, invalid_target)

            invalid_uniform_dimension = deepcopy(valid_uniform_force)
            invalid_uniform_dimension["quantity"] = quantity(1.0, "N", "force")
            assert_invalid_instance(load_record_schema, invalid_uniform_dimension)

            invalid_fraction = deepcopy(valid_element_point_force)
            invalid_fraction["station_fraction"] = quantity(1.1, "1", "dimensionless")
            assert_invalid_instance(load_record_schema, invalid_fraction)

            missing_orientation = deepcopy(valid_straight_pipe)
            del missing_orientation["local_coordinate_system"]["y_reference"]
            assert_invalid_instance(element_schema, missing_orientation)

            forbidden_local_x = deepcopy(valid_straight_pipe)
            forbidden_local_x["local_coordinate_system"]["local_x_axis"] = [1.0, 0.0, 0.0]
            assert_invalid_instance(element_schema, forbidden_local_x)
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def assert_invalid_instance(schema, instance):
        try:
            validate_instance(schema, instance)
        except AssertionError:
            return
        raise AssertionError("instance unexpectedly passed JSON Schema validation")


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_model_schema_contract():
        check_schema_contract()


    def test_domain_fixtures_exercise_foundation_contracts():
        check_domain_fixtures()


    def test_model_schema_jsonschema_validation_helper():
        check_jsonschema_validation()


    def test_typed_load_records_and_straight_pipe_orientation_contract():
        check_typed_load_records_and_orientation_validation()


    def main():
        check_schema_contract()
        check_domain_fixtures()
        check_jsonschema_validation()
        check_typed_load_records_and_orientation_validation()


    if __name__ == "__main__":
        main()

## Component: tests/test_model_state_comparison.py

    #!/usr/bin/env python3
    """Focused checks for DEL-14-03 model-state comparison."""

    from __future__ import annotations

    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.comparison.model_state.engine import canonical_json, compare_model_states  # noqa: E402


    def provenance():
        return {
            "source_name": "invented public test fixture",
            "source_location": "tests/test_model_state_comparison.py",
            "source_license": "project-governed",
            "contributor": "OpenPipeStress test",
            "contributor_certification": "invented non-engineering fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "pending",
            "privacy_classification": "invented_public_example",
        }


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def state(state_id, entities, *, warnings=None):
        return {
            "model_state": {
                "state_id": state_id,
                "state_name": f"Invented {state_id}",
                "state_kind": "comparison_basis",
                "created_at": "2026-05-05T00:00:00Z",
                "model_ref": {"object_type": "Model", "ref": "model:invented"},
                "parent_state_refs": [],
                "tags": [{"tag": "invented", "tag_kind": "comparison_label", "provenance": provenance()}],
                "notes": [
                    {
                        "note_id": f"note:{state_id}",
                        "note_type": "design_note",
                        "statement": "Invented public comparison fixture.",
                        "visibility": "public",
                        "provenance": provenance(),
                    }
                ],
                "external_references": [
                    {
                        "reference_id": f"ext:{state_id}",
                        "reference_type": "document",
                        "label": "Invented public source",
                        "target": "public-fixture",
                        "binding_hashes": [],
                        "privacy_classification": "invented_public_example",
                        "provenance": provenance(),
                    }
                ],
                "unresolved_assumptions": [
                    {
                        "assumption_id": f"assumption:{state_id}",
                        "statement": "Invented unresolved assumption.",
                        "status": "unresolved",
                        "affected_refs": [{"object_type": "ModelState", "ref": state_id}],
                        "provenance": provenance(),
                    }
                ],
                "warnings": warnings or [],
                "analysis_status": ["MODEL_INCOMPLETE"],
                "hashes": [
                    {
                        "algorithm": "sha256",
                        "canonicalization": "JCS",
                        "payload_ref": {"object_type": "ModelState", "ref": state_id},
                        "payload_scope": "model_state_record",
                        "value": f"hash-{state_id}",
                    }
                ],
                "immutability_policy": {
                    "snapshot_is_read_only": True,
                    "mutation_policy": "changes_create_new_model_state",
                    "new_state_required_for_change": True,
                    "hash_invalidates_external_acceptance": True,
                },
                "professional_boundary": professional_boundary(),
                "provenance": provenance(),
            },
            "entities": entities,
        }


    def entity(stable_id, *, category="Component", label=None, **fields):
        return {
            "stable_id": stable_id,
            "category": category,
            "reference": {"object_type": "Entity", "ref": stable_id, "label": label or stable_id},
            **fields,
        }


    def by_ref(result):
        rows = {}
        for row in result["entities"]:
            left_ref = row["left_ref"]["ref"] if row.get("left_ref") else None
            right_ref = row["right_ref"]["ref"] if row.get("right_ref") else None
            rows[(left_ref, right_ref)] = row
        return rows


    def mapping_context():
        return {
            "mapping_evidence": [
                {
                    "evidence_id": "evidence:manual-map",
                    "evidence_kind": "manual_mapping",
                    "source_refs": [{"object_type": "ModelState", "ref": "state:left"}],
                    "stable_id_preservation": "left_and_right_refs_preserved",
                    "manual_review_state": "manual_reviewed",
                    "hash_refs": [
                        {
                            "algorithm": "sha256",
                            "canonicalization": "JCS",
                            "payload_ref": {"object_type": "ComparisonMapping", "ref": "map:renamed"},
                            "payload_scope": "mapping_evidence",
                            "value": "hash-mapping-evidence",
                        }
                    ],
                    "provenance": provenance(),
                }
            ],
            "hash_refs": [
                {
                    "algorithm": "sha256",
                    "canonicalization": "JCS",
                    "payload_ref": {"object_type": "ComparisonMapping", "ref": "map:renamed"},
                    "payload_scope": "mapping_record",
                    "value": "hash-map-renamed",
                }
            ],
            "provenance": provenance(),
            "confidence": "manual_reviewed",
            "review": {
                "review_status": "pending",
                "reviewer": "OpenPipeStress test",
                "review_note": "Invented public mapping evidence.",
            },
        }


    def test_stable_id_matching_is_order_independent_and_preserves_metadata():
        left = state(
            "state:left",
            [
                entity("entity:changed", nominal_size={"value": 12, "unit": "in", "dimension": "length"}),
                entity("entity:unchanged", nominal_size={"value": 10, "unit": "in", "dimension": "length"}),
            ],
        )
        right_a = state(
            "state:right",
            [
                entity("entity:unchanged", nominal_size={"value": 10, "unit": "in", "dimension": "length"}),
                entity("entity:changed", nominal_size={"value": 14, "unit": "in", "dimension": "length"}),
            ],
        )
        right_b = state("state:right", list(reversed(right_a["entities"])))

        settings = {"unit_bearing_fields": ["nominal_size"], "created_at": "TBD"}
        first = compare_model_states(left, right_a, settings=settings)
        second = compare_model_states(left, right_b, settings=settings)

        assert canonical_json(first) == canonical_json(second)
        assert first["summary"]["changed"] == 1
        assert first["summary"]["unchanged"] == 1
        assert first["metadata"]["left"]["notes"][0]["note_id"] == "note:state:left"
        assert first["metadata"]["right"]["external_references"][0]["reference_id"] == "ext:state:right"
        assert any(item["code"] == "UNRESOLVED_STATE_ASSUMPTION" for item in first["diagnostics"])


    def test_added_removed_changed_unchanged_and_explicit_mapping_are_classified():
        left = state(
            "state:left",
            [
                entity("entity:unchanged", value="same"),
                entity("entity:changed", value="before"),
                entity("entity:removed", value="left-only"),
                entity("entity:left-renamed", value="mapped"),
            ],
        )
        right = state(
            "state:right",
            [
                entity("entity:added", value="right-only"),
                entity("entity:changed", value="after"),
                entity("entity:right-renamed", value="mapped"),
                entity("entity:unchanged", value="same"),
            ],
        )
        mappings = [
            {
                "mapping_id": "map:renamed",
                "mapping_kind": "entity",
                "mapping_status": "manual_match",
                "left_ref": {"object_type": "Entity", "ref": "entity:left-renamed"},
                "right_ref": {"object_type": "Entity", "ref": "entity:right-renamed"},
            }
        ]

        result = compare_model_states(left, right, mappings=mappings)
        assert result["summary"] == {
            "added": 1,
            "removed": 1,
            "changed": 1,
            "unchanged": 1,
            "mapped_changed": 0,
            "mapped_unchanged": 1,
            "unresolved": 0,
            "total": 5,
        }
        rows = by_ref(result)
        assert rows[("entity:left-renamed", "entity:right-renamed")]["match_basis"] == "explicit_mapping"
        assert rows[("entity:changed", "entity:changed")]["changes"][0]["field"] == "value"
        assert "MAPPING_CONTEXT_INCOMPLETE" in {item["code"] for item in result["diagnostics"]}


    def test_explicit_mapping_rows_preserve_evidence_hashes_and_provenance_context():
        left = state("state:left", [entity("entity:left-renamed", value="mapped")])
        right = state("state:right", [entity("entity:right-renamed", value="mapped")])
        context = mapping_context()
        mappings = [
            {
                "mapping_id": "map:renamed",
                "mapping_kind": "entity",
                "mapping_status": "manual_match",
                "left_ref": {"object_type": "Entity", "ref": "entity:left-renamed"},
                "right_ref": {"object_type": "Entity", "ref": "entity:right-renamed"},
                **context,
            }
        ]

        result = compare_model_states(left, right, mappings=mappings)

        row = by_ref(result)[("entity:left-renamed", "entity:right-renamed")]
        preserved = row["mapping_context"]
        assert preserved["mapping_id"] == "map:renamed"
        assert preserved["mapping_evidence"] == context["mapping_evidence"]
        assert preserved["hash_refs"] == context["hash_refs"]
        assert preserved["provenance"]["source_name"] == "invented public test fixture"
        assert preserved["review"]["review_status"] == "pending"
        assert "MAPPING_CONTEXT_INCOMPLETE" not in {item["code"] for item in result["diagnostics"]}


    def test_unresolved_mapping_and_unsupported_category_emit_diagnostics():
        left = state("state:left", [entity("entity:left-only", category="Support")])
        right = state("state:right", [entity("entity:right-only", category="Load")])
        mappings = [
            {
                "mapping_id": "map:unresolved",
                "mapping_kind": "entity",
                "mapping_status": "unresolved_mapping",
                "left_ref": {"object_type": "Entity", "ref": "entity:left-only"},
            }
        ]

        result = compare_model_states(
            left,
            right,
            mappings=mappings,
            settings={"comparable_entity_categories": ["Component"]},
        )

        assert result["summary"]["unresolved"] == 1
        assert result["summary"]["added"] == 1
        assert any(item["code"] == "MAPPING_UNRESOLVED" for item in result["diagnostics"])


    def test_missing_mapping_target_is_unresolved_and_visible():
        left = state("state:left", [entity("entity:left-only", category="Component")])
        right = state("state:right", [])
        mappings = [
            {
                "mapping_id": "map:missing-target",
                "mapping_kind": "entity",
                "mapping_status": "manual_match",
                "left_ref": {"object_type": "Entity", "ref": "entity:left-only"},
                "right_ref": {"object_type": "Entity", "ref": "entity:missing"},
                **mapping_context(),
            }
        ]

        result = compare_model_states(left, right, mappings=mappings)

        assert result["summary"]["unresolved"] == 1
        assert result["entities"][0]["mapping_context"]["mapping_id"] == "map:missing-target"
        assert "MAPPING_TARGET_MISSING" in {item["code"] for item in result["diagnostics"]}


    def test_incompatible_entity_categories_remain_unresolved():
        left = state("state:left", [entity("entity:left-support", category="Support")])
        right = state("state:right", [entity("entity:right-load", category="Load")])
        mappings = [
            {
                "mapping_id": "map:category-mismatch",
                "mapping_kind": "entity",
                "mapping_status": "manual_match",
                "left_ref": {"object_type": "Entity", "ref": "entity:left-support"},
                "right_ref": {"object_type": "Entity", "ref": "entity:right-load"},
                **mapping_context(),
            }
        ]

        result = compare_model_states(
            left,
            right,
            mappings=mappings,
            settings={"comparable_entity_categories": ["Component"]},
        )

        row = by_ref(result)[("entity:left-support", "entity:right-load")]
        assert row["classification"] == "unresolved"
        assert row["mapping_context"]["mapping_id"] == "map:category-mismatch"
        assert "UNSUPPORTED_CATEGORY" in {item["code"] for item in result["diagnostics"]}


    def test_unit_bearing_changes_require_unit_and_dimension_metadata():
        left = state("state:left", [entity("entity:pipe", nominal_size=10)])
        right = state("state:right", [entity("entity:pipe", nominal_size=12)])

        result = compare_model_states(left, right, settings={"unit_bearing_fields": ["nominal_size"]})

        assert result["summary"]["unresolved"] == 1
        assert result["summary"]["changed"] == 0
        diagnostic = next(item for item in result["diagnostics"] if item["code"] == "MISSING_UNIT_METADATA")
        assert diagnostic["severity"] == "blocking"


    def test_state_warnings_are_preserved_as_review_evidence():
        warning = {
            "code": "STATE-WARNING-INVENTED",
            "message": "Invented warning attached to compared state.",
            "provenance": provenance(),
        }

        result = compare_model_states(
            state("state:left", [entity("entity:one")], warnings=[warning]),
            state("state:right", [entity("entity:one")]),
        )

        diagnostic = next(item for item in result["diagnostics"] if item["code"] == "STATE_WARNING_PRESERVED")
        assert diagnostic["affected_refs"][0]["affected_ref"]["ref"] == "STATE-WARNING-INVENTED"
        assert diagnostic["provenance"]["source_name"] == "invented public test fixture"


    def test_output_boundary_language_does_not_make_prohibited_claims():
        result = compare_model_states(
            state("state:left", [entity("entity:one")]),
            state("state:right", [entity("entity:one")]),
        )
        text = canonical_json(result).lower()

        for forbidden in [
            "code compliant",
            "certified",
            "sealed",
            "authenticated",
            "professional approval",
            "external validation",
        ]:
            assert forbidden not in text
        assert result["professional_boundary"]["software_makes_compliance_claim"] is False


    def main():
        test_stable_id_matching_is_order_independent_and_preserves_metadata()
        test_added_removed_changed_unchanged_and_explicit_mapping_are_classified()
        test_explicit_mapping_rows_preserve_evidence_hashes_and_provenance_context()
        test_unresolved_mapping_and_unsupported_category_emit_diagnostics()
        test_missing_mapping_target_is_unresolved_and_visible()
        test_incompatible_entity_categories_remain_unresolved()
        test_unit_bearing_changes_require_unit_and_dimension_metadata()
        test_state_warnings_are_preserved_as_review_evidence()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_model_state_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the immutable model state schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "model_state.schema.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "state_contract_status",
        "model_state",
    }

    REQUIRED_DEFS = {
        "AnalysisStatus",
        "AssumptionRecord",
        "Checksum",
        "Diagnostic",
        "ExternalReference",
        "Id",
        "ImmutabilityPolicy",
        "ModelStateRecord",
        "PhysicalProjectContainer",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ReviewStatus",
        "StateContractStatus",
        "StateNote",
        "StateTag",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "formal prover approval status",
        "code compliant",
        "certified by software",
        "sealed by software",
        "professional approval by the software",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-14-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-14"
        assert schema["properties"]["scope_item"]["const"] == "SOW-071"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-016"

        contract = defs["StateContractStatus"]["properties"]
        assert contract["record_contract"]["const"] == "schema_first_model_state_records"
        assert contract["persistence_binding"]["const"] == (
            "schemas/project_persistence.schema.yaml"
        )
        assert contract["canonicalization"]["const"] == "JCS_compatible_json_payload_hashes"
        assert (
            contract["physical_project_container"]["$ref"]
            == "#/$defs/PhysicalProjectContainer"
        )
        assert contract["external_human_acceptance"]["const"] == (
            "hash_bound_external_record_only"
        )

        physical = defs["PhysicalProjectContainer"]["properties"]
        assert physical["profile"]["const"] == "sqlite_local_project_store"
        assert physical["decision_ref"]["const"] == "SCA-003"
        assert physical["storage_role"]["const"] == "local_store_index_projection"
        assert physical["canonical_truth"]["const"] == "canonical_json_jcs_payload"
        assert physical["sql_public_contract"]["const"] is False
        assert physical["direct_sql_access_allowed"]["const"] is False
        assert physical["hosted_db_allowed"]["const"] is False
        assert physical["network_required"]["const"] is False
        assert physical["sidecars_rebuildable"]["const"] is True

        state_required = required_at(schema, "ModelStateRecord")
        assert {
            "state_id",
            "state_name",
            "state_kind",
            "created_at",
            "model_ref",
            "parent_state_refs",
            "tags",
            "notes",
            "external_references",
            "unresolved_assumptions",
            "warnings",
            "analysis_status",
            "hashes",
            "immutability_policy",
            "professional_boundary",
            "provenance",
        } <= state_required
        assert {
            "design_snapshot",
            "pre_solve_snapshot",
            "post_solve_snapshot",
            "comparison_basis",
            "handoff_basis",
        } <= set(defs["ModelStateRecord"]["properties"]["state_kind"]["enum"])

        immutability = defs["ImmutabilityPolicy"]["properties"]
        assert immutability["snapshot_is_read_only"]["const"] is True
        assert immutability["mutation_policy"]["const"] == "changes_create_new_model_state"
        assert immutability["new_state_required_for_change"]["const"] is True
        assert immutability["hash_invalidates_external_acceptance"]["const"] is True

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)

        checksum_required = required_at(schema, "Checksum")
        assert {
            "algorithm",
            "canonicalization",
            "payload_ref",
            "payload_scope",
            "value",
        } <= checksum_required
        assert {"JCS", "NONE", "TBD"} <= set(
            defs["Checksum"]["properties"]["canonicalization"]["enum"]
        )
        assert {
            "model_state_record",
            "model_payload",
            "state_payload_partition",
            "external_reference",
            "audit_manifest",
            "TBD",
        } <= set(defs["Checksum"]["properties"]["payload_scope"]["enum"])

        assert {
            "document",
            "drawing",
            "model_file",
            "audit_manifest",
            "review_record",
            "external_file",
        } <= set(defs["ExternalReference"]["properties"]["reference_type"]["enum"])

        professional = defs["ProfessionalBoundary"]["properties"]
        assert professional["human_review_required"]["const"] is True
        assert professional["software_makes_compliance_claim"]["const"] is False
        assert professional["software_makes_certification_claim"]["const"] is False
        assert professional["software_makes_sealing_claim"]["const"] is False
        assert professional["software_makes_approval_claim"]["const"] is False
        assert professional["software_makes_authentication_claim"]["const"] is False

        provenance_required = required_at(schema, "Provenance")
        assert {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
            "privacy_classification",
        } <= provenance_required
        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "invented_non_engineering_example",
        } <= enum_at(schema, "RedistributionStatus")

        joined_strings = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden.lower() not in joined_strings


    def test_model_state_schema_contract():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_model_tree_property_inspector.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-02 model tree/property inspector contracts."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.model_tree import build_model_tree_property_inspector, canonical_json  # noqa: E402


    FORBIDDEN = ("certified", "sealed", "code compliant", "professional acceptance")


    def invented_entities():
        return [
            {
                "entity_id": "node-N1",
                "entity_type": "node",
                "label": "Invented node N1",
                "sort_key": "001",
                "properties": [
                    {
                        "field_id": "elevation",
                        "label": "Elevation",
                        "value": 12.0,
                        "unit": "m",
                        "editable": True,
                        "validation_state": "ready_for_service_validation",
                    }
                ],
                "provenance_state": "invented_public_example",
            },
            {
                "entity_id": "pipe-P1",
                "entity_type": "pipe_run",
                "label": "Invented pipe P1",
                "sort_key": "002",
                "properties": [
                    {
                        "field_id": "nominal_size",
                        "label": "Nominal size",
                        "value": "TBD",
                        "unit": "mm",
                        "editable": True,
                    }
                ],
            },
        ]


    def main():
        record = build_model_tree_property_inspector(
            project_id="invented-project",
            entities=invented_entities(),
            selected_ref={"ref_type": "pipe_run", "ref_id": "pipe-P1"},
        )
        again = build_model_tree_property_inspector(
            project_id="invented-project",
            entities=list(reversed(invented_entities())),
            selected_ref={"ref_type": "pipe_run", "ref_id": "pipe-P1"},
        )
        assert canonical_json(record) == canonical_json(again)
        assert record["deliverable_id"] == "DEL-07-02"
        assert record["selection"]["selected"] is True
        assert record["property_inspector"]["status"] == "selection_resolved"
        assert record["property_inspector"]["fields"][0]["validation_state"] == "unresolved_TBD"
        assert record["mutation_policy"] == "application_service_command_intents_only"
        assert record["professional_boundary"]["software_makes_compliance_claim"] is False
        assert any(item["code"] == "PROPERTY_VALUE_UNRESOLVED" for item in record["diagnostics"])
        text = canonical_json(record).lower()
        for term in FORBIDDEN:
            assert term not in text


    def test_model_tree_property_inspector_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_native_json_export_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-03 native open JSON export packages."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.handoff.native_json import (  # noqa: E402
        build_native_json_export_package,
        canonical_json,
        write_native_json_export_package,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "native_json_export.schema.json"
    FIXTURE_PATH = ROOT / "fixtures" / "native_json" / "invented" / "native_json_export_package.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")


    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
    }


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def build_from_fixture() -> dict[str, object]:
        fixture = load_json(FIXTURE_PATH)
        return build_native_json_export_package(
            native_export_id=fixture["native_export_id"],
            source_model_ref=fixture["manifest"]["source_model_ref"],
            source_model_hash=fixture["manifest"]["source_model_hash"],
            model_payload=fixture["model_payload"],
            stable_id_map=fixture["stable_id_map"],
            loss_report=fixture["loss_report"],
            export_profile=fixture["export_profile"],
            validation_checks=fixture["validation_report"]["checks"],
            privacy=fixture["privacy"],
            provenance=fixture["provenance"],
        )


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        built = build_from_fixture()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(FIXTURE_PATH),
            )
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_native_json_export_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_native_package_members():
        first = build_from_fixture()
        second = build_from_fixture()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-03"
        assert first["package_id"] == "PKG-17"
        assert first["package_status"] == "native_open_json_export_package"
        assert first["export_profile"]["target_family"] == "native_open_json"

        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "model_payload",
            "stable_id_map",
            "loss_report",
            "validation_report",
            "diagnostics",
        }
        assert len(first["manifest"]["checksums"]) == 7
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert {item["loss_category"] for item in first["stable_id_map"]} == {"exported"}
        assert {"exported", "TBD"} <= {item["category"] for item in first["loss_report"]}
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_missing_units_stable_ids_and_loss_report_are_blocking_not_defaulted():
        fixture = load_json(FIXTURE_PATH)
        payload = deepcopy(fixture["model_payload"])
        payload["units_manifest"] = {}

        package = build_native_json_export_package(
            native_export_id="native-json:blocked",
            source_model_ref=fixture["manifest"]["source_model_ref"],
            source_model_hash=fixture["manifest"]["source_model_hash"],
            model_payload=payload,
            stable_id_map=[],
            loss_report=[],
            export_profile=fixture["export_profile"],
            privacy=fixture["privacy"],
            provenance=fixture["provenance"],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert "NJ-LOSS-CATEGORY-UNSUPPORTED" not in codes
        assert {"NJ-UNITS-MANIFEST-MISSING", "NJ-STABLE-ID-MAP-MISSING"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["validation_report"]["validation_status"] == "blocked"
        assert package["loss_report"][0]["category"] == "TBD"


    def test_privacy_and_authority_boundary_diagnostics_block_public_package():
        fixture = load_json(FIXTURE_PATH)
        payload = deepcopy(fixture["model_payload"])
        payload["free_metadata"] = {"unsafe_label": "cert" + "ified target export"}
        privacy = deepcopy(fixture["privacy"])
        privacy["protected_payload_embedded"] = True

        package = build_native_json_export_package(
            native_export_id="native-json:privacy-boundary",
            source_model_ref=fixture["manifest"]["source_model_ref"],
            source_model_hash=fixture["manifest"]["source_model_hash"],
            model_payload=payload,
            stable_id_map=fixture["stable_id_map"],
            loss_report=fixture["loss_report"],
            export_profile=fixture["export_profile"],
            privacy=privacy,
            provenance=fixture["provenance"],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"NJ-PROHIBITED-AUTHORITY-TERM", "NJ-PRIVACY-BOUNDARY-VIOLATION"} <= codes
        assert package["privacy"]["protected_payload_embedded"] is True
        assert package["professional_boundary"]["software_makes_compliance_claim"] is False
        assert package["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def test_writer_uses_canonical_json(tmp_path):
        package = build_from_fixture()
        output_path = tmp_path / "native-package.json"

        write_native_json_export_package(output_path, package)

        assert output_path.read_text(encoding="utf-8") == canonical_json(package) + "\n"


    def test_fixture_contains_no_private_or_protected_payload_text():
        text = "\n".join(walk_strings(load_json(FIXTURE_PATH))).lower()
        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text


    def main():
        check_jsonschema_validation()
        test_builder_is_deterministic_and_preserves_native_package_members()
        test_missing_units_stable_ids_and_loss_report_are_blocking_not_defaulted()
        test_privacy_and_authority_boundary_diagnostics_block_public_package()
        test_fixture_contains_no_private_or_protected_payload_text()


    if __name__ == "__main__":
        main()

## Component: tests/test_nonlinear_support_regression.py

    #!/usr/bin/env python3
    """Focused regression checks for invented nonlinear support fixtures."""

    import re
    import subprocess
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    BENCHMARK_DIR = ROOT / "validation" / "benchmarks" / "nonlinear"
    SOURCE_PATH = BENCHMARK_DIR / "src" / "lib.rs"
    HAND_CALCS_DIR = ROOT / "validation" / "hand_calcs" / "nonlinear"
    HAND_CALCS_README = HAND_CALCS_DIR / "README.md"
    BENCHMARK_README = BENCHMARK_DIR / "README.md"

    REQUIRED_FAMILIES = {
        "ActiveSet",
        "Gap",
        "LiftOff",
        "Friction",
        "NonConvergence",
    }

    REQUIRED_FIXTURE_NOTES = {
        "NL-ACTIVE-ONE-WAY-ORIGINAL": "active_set_one_way.md",
        "NL-GAP-CLOSURE-ORIGINAL": "gap_closure.md",
        "NL-LIFT-OFF-ORIGINAL": "lift_off.md",
        "NL-FRICTION-STICK-SLIDE-ORIGINAL": "friction_transition.md",
        "NL-NONCONVERGENCE-LIMIT-ORIGINAL": "unresolved_nonconvergence.md",
    }

    REQUIRED_UNIT_BASIS_LINES = {
        "Translational support displacement and clearance | `mm` | length",
        "Translational support reaction | `N` | force",
        "Rotational support reaction | `N-m` | moment",
        "Friction coefficient | `ratio` | dimensionless",
        "Active-set residual and iteration counts | `count` | dimensionless",
    }

    BOUNDARY_PHRASES = {
        "project-original-public-content",
        "invented support states",
        "not copied from protected standards",
        "commercial software examples",
        "proprietary data",
        "private data",
        "real project records",
    }

    FORBIDDEN_TERMS = {
        "AS" + "ME",
        "B" + "31",
        "B" + "31J",
        "allowable stress " + "table",
        "stress intensification factor " + "table",
        "vendor catalog " + "value",
        "real " + "se" + "cret",
        "cert" + "ified",
        "sea" + "led",
        "code-compliant",
        "professional approval",
        "licensed engineer approval",
        "suitable for professional reliance",
    }

    CANONICAL_DIMENSIONS_RE = re.compile(
        r"const\s+CANONICAL_DIMENSIONS:\s*&\[\&str\]\s*=\s*&\[(?P<body>.*?)\];",
        re.DOTALL,
    )


    def _canonical_dimensions(source: str) -> set[str]:
        match = CANONICAL_DIMENSIONS_RE.search(source)
        assert match is not None
        return set(re.findall(r'"([^"]+)"', match.group("body")))


    def _normalized_text(text: str) -> str:
        return " ".join(text.split())


    def test_nonlinear_benchmark_crate_runs_focused_regressions():
        result = subprocess.run(
            ["cargo", "test", "--quiet"],
            cwd=BENCHMARK_DIR,
            check=False,
            text=True,
            capture_output=True,
        )

        assert result.returncode == 0, result.stdout + result.stderr


    def test_nonlinear_fixture_catalog_is_bounded_and_invented():
        source = SOURCE_PATH.read_text(encoding="utf-8")

        for family in REQUIRED_FAMILIES:
            assert family in source

        for phrase in BOUNDARY_PHRASES:
            assert phrase in source

        assert "PKG09-NONLINEAR-FIXTURE-UNITS-EXPLICIT-MM-N-NM" in source
        assert "unit catalog remains TBD" in source
        assert "tolerance_policy: None" in source
        tolerance_assignments = re.findall(
            r"^\s+tolerance_policy:\s*([^,\n]+)", source, re.MULTILINE
        )
        assert tolerance_assignments
        assert set(tolerance_assignments) == {"None"}

        lowered_source = source.lower()
        for term in FORBIDDEN_TERMS:
            assert term.lower() not in lowered_source


    def test_nonlinear_fixture_notes_cover_each_public_original_fixture():
        source = SOURCE_PATH.read_text(encoding="utf-8")
        readme = HAND_CALCS_README.read_text(encoding="utf-8")

        for fixture_id, note_name in REQUIRED_FIXTURE_NOTES.items():
            note_path = HAND_CALCS_DIR / note_name
            assert note_path.is_file(), note_name

            note = note_path.read_text(encoding="utf-8")
            source_location = f"validation/hand_calcs/nonlinear/{note_name}"

            assert fixture_id in source
            assert fixture_id in readme
            assert fixture_id in note
            assert source_location in source
            assert f"[{note_name}]({note_name})" in readme
            assert "## Provenance" in note
            assert "## Invented Inputs" in note
            assert "## Expected Values" in note

            normalized_note = _normalized_text(note)
            for phrase in BOUNDARY_PHRASES:
                assert phrase in normalized_note


    def test_nonlinear_hand_calc_unit_basis_is_explicit_and_unresolved():
        readme = HAND_CALCS_README.read_text(encoding="utf-8")
        benchmark_readme = BENCHMARK_README.read_text(encoding="utf-8")

        for required_line in REQUIRED_UNIT_BASIS_LINES:
            assert required_line in readme

        assert "PKG09-NONLINEAR-FIXTURE-UNITS-EXPLICIT-MM-N-NM" in benchmark_readme
        assert "fixture-local basis" in benchmark_readme
        normalized_benchmark_readme = _normalized_text(benchmark_readme)
        assert "does not define project conversion constants" in normalized_benchmark_readme
        assert "canonical unit catalog, which remain `TBD`" in normalized_benchmark_readme
        assert "release tolerances" in readme
        assert "CI gate" in readme
        assert "remain `TBD`" in readme

        for note_name in REQUIRED_FIXTURE_NOTES.values():
            note = (HAND_CALCS_DIR / note_name).read_text(encoding="utf-8")
            assert "| Quantity |" in note
            assert "Canonical dimension" in note
            assert "Tolerance policy: `TBD`." in note


    def test_nonlinear_validation_artifacts_avoid_protected_and_claim_terms():
        scanned_paths = [
            SOURCE_PATH,
            BENCHMARK_README,
            HAND_CALCS_README,
            *(HAND_CALCS_DIR / note_name for note_name in REQUIRED_FIXTURE_NOTES.values()),
        ]

        for path in scanned_paths:
            lowered_text = path.read_text(encoding="utf-8").lower()
            for term in FORBIDDEN_TERMS:
                assert term.lower() not in lowered_text, f"{term!r} appears in {path}"


    def test_nonlinear_dimension_allowlist_includes_force_per_length():
        source = SOURCE_PATH.read_text(encoding="utf-8")

        assert "force_per_length" in _canonical_dimensions(source)


    def test_nonlinear_public_provenance_sources_exist_before_fixture_acceptance():
        source = SOURCE_PATH.read_text(encoding="utf-8")
        source_locations = {
            line.split('"')[1]
            for line in source.splitlines()
            if 'validation/hand_calcs/nonlinear/' in line and line.strip().startswith('"')
        }

        assert source_locations
        for source_location in source_locations:
            assert (ROOT / source_location).is_file(), source_location

## Component: tests/test_operation_audit_trail.py

    #!/usr/bin/env python3
    """Focused tests for DEL-16-03 user acceptance operation audit trail."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.model_operations.audit_trail import canonical_json, record_operation_audit_trail  # noqa: E402
    from core.model_operations.validation_preview import validate_and_preview_operations  # noqa: E402


    OPERATION_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_operation_set_valid.json"
    MODEL_STATE_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_accepted_model_state.json"


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def validation():
        return {
            "schema_validation": "pending",
            "constraint_validation": "pending",
            "unit_validation": "pending",
            "diff_preview_status": "not_generated",
            "application_status": "not_applied",
        }


    def model_state():
        with MODEL_STATE_FIXTURE.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def quantity_change():
        return {
            "change_id": "change:diameter",
            "change_kind": "set_field",
            "target_object_type": "Component",
            "target_ref": ref("Component", "component:pipe-1"),
            "value_payload": {
                "value_kind": "quantity",
                "scalar_values": [],
                "quantity_values": [{"value": 125.0, "unit": "mm", "dimension": "length"}],
                "reference_values": [],
                "structured_values": [{"diameter": {"value": 125.0, "unit": "mm", "dimension": "length"}}],
                "notes": [],
            },
            "unit_requirements": {
                "unit_metadata_required": True,
                "dimension_check_required": True,
                "missing_unit_behavior": "emit_diagnostic",
            },
        }


    def operation_envelope(*, assumptions=None):
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        operation = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )
        operation["operation_status"] = "ready_for_user_review"
        operation["assumptions"] = assumptions or []
        envelope["operation_set"]["operations"] = [operation]
        return envelope


    def assumption(assumption_id, status):
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        provenance = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )["provenance"]
        return {
            "assumption_id": assumption_id,
            "statement": "Invented operation assumption for audit trail testing.",
            "status": status,
            "affected_refs": [ref("ModelOperation", "op:resize")],
            "provenance": deepcopy(provenance),
        }


    def user_acceptance():
        return {
            "decision": "accept",
            "accepted": True,
            "actor_type": "user",
            "actor_ref": "user:reviewer",
            "source_role": "project_user",
            "decided_at": "2026-05-06T12:00:00Z",
            "rationale": "Invented example review accepted for audit trail test.",
        }


    def user_rejection():
        return {
            "decision": "reject",
            "accepted": False,
            "actor_type": "user",
            "actor_ref": "user:reviewer",
            "source_role": "project_user",
            "decided_at": "2026-05-06T12:05:00Z",
            "rationale": "Invented example review rejected for audit trail test.",
        }


    def preview_ref():
        return {
            "object_type": "DiffPreview",
            "ref": "preview:resize",
            "hash": "sha256:invented-preview",
        }


    def test_user_accepted_operation_record_is_deterministic_and_complete():
        envelope = operation_envelope(assumptions=[assumption("asm:1", "unresolved")])
        preview = validate_and_preview_operations(envelope, model_state())
        first = record_operation_audit_trail(
            envelope,
            validation_outcome=preview,
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_acceptance(),
            actor={"actor_type": "user", "actor_ref": "user:reviewer"},
            source={"source_ref": "operation-workbench:invented", "source_channel": "test"},
            accepted_model_state=model_state(),
        )
        second = record_operation_audit_trail(
            deepcopy(envelope),
            validation_outcome=deepcopy(preview),
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_acceptance(),
            actor={"actor_type": "user", "actor_ref": "user:reviewer"},
            source={"source_ref": "operation-workbench:invented", "source_channel": "test"},
            accepted_model_state=model_state(),
        )

        assert canonical_json(first) == canonical_json(second)
        assert first["decision_counts"] == {"accepted": 1, "rejected": 0, "held_for_user_acceptance": 0}
        record = first["records"][0]
        assert record["decision"]["status"] == "accepted"
        assert record["decision"]["explicit_user_acceptance"] is True
        assert record["decision"]["accepted_model_state_mutated"] is False
        assert record["affected_entities"] == [ref("Component", "component:pipe-1")]
        assert record["operation_history"]["changes"][0]["change_id"] == "change:diameter"
        assert record["validation_outcome"]["validation"]["diff_preview_status"] == "generated"
        assert record["diff_preview_ref"]["ref"] == "preview:resize"
        assert record["unresolved_assumptions"][0]["assumption_id"] == "asm:1"


    def test_operation_cannot_be_accepted_without_explicit_user_signal():
        result = record_operation_audit_trail(
            operation_envelope(),
            validation_outcome=validate_and_preview_operations(operation_envelope(), model_state()),
            diff_preview_ref=preview_ref(),
            acceptance_signal={"decision": "accept", "accepted": True, "actor_type": "agent"},
            accepted_model_state=model_state(),
        )

        record = result["records"][0]
        assert record["decision"]["status"] == "held_for_user_acceptance"
        assert record["decision"]["explicit_user_acceptance"] is False
        assert "AUDIT-EXPLICIT-USER-ACCEPTANCE-REQUIRED" in {item["code"] for item in record["diagnostics"]}


    def test_blocked_validation_outcome_prevents_accepted_record():
        envelope = operation_envelope()
        accepted = model_state()
        blocked_envelope = deepcopy(envelope)
        blocked_envelope["operation_set"]["operations"][0]["preconditions"]["required_current_hashes"][0][
            "value"
        ] = "sha256:stale"
        blocked_preview = validate_and_preview_operations(blocked_envelope, accepted)

        result = record_operation_audit_trail(
            envelope,
            validation_outcome=blocked_preview,
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_acceptance(),
            accepted_model_state=accepted,
        )

        record = result["records"][0]
        assert record["decision"]["status"] == "held_for_user_acceptance"
        assert "AUDIT-VALIDATION-GATES-BLOCKING" in {item["code"] for item in record["diagnostics"]}


    def test_current_model_state_hash_is_required_for_accepted_record():
        accepted = model_state()
        del accepted["model_state"]["state_hash"]
        preview = validate_and_preview_operations(operation_envelope(), model_state())

        result = record_operation_audit_trail(
            operation_envelope(),
            validation_outcome=preview,
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_acceptance(),
            accepted_model_state=accepted,
        )

        record = result["records"][0]
        assert record["decision"]["status"] == "held_for_user_acceptance"
        assert "AUDIT-MODEL-STATE-HASH-MISSING" in {item["code"] for item in record["diagnostics"]}


    def test_rejected_operation_is_recorded_without_mutating_accepted_state():
        accepted = model_state()
        original = deepcopy(accepted)
        result = record_operation_audit_trail(
            operation_envelope(),
            validation_outcome=validate_and_preview_operations(operation_envelope(), accepted),
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_rejection(),
            accepted_model_state=accepted,
        )

        assert accepted == original
        assert result["accepted_model_state_unchanged"] is True
        assert result["decision_counts"] == {"accepted": 0, "rejected": 1, "held_for_user_acceptance": 0}
        assert result["records"][0]["decision"]["status"] == "rejected"
        assert result["records"][0]["decision"]["accepted_model_state_mutated"] is False


    def test_missing_inputs_are_visible_tbd_diagnostics():
        result = record_operation_audit_trail(operation_envelope())
        top_codes = {item["code"] for item in result["diagnostics"]}
        record_codes = {item["code"] for item in result["records"][0]["diagnostics"]}

        assert {"AUDIT-VALIDATION-OUTCOME-TBD", "AUDIT-DIFF-PREVIEW-REF-TBD", "AUDIT-USER-DECISION-TBD"} <= top_codes
        assert "AUDIT-TIMESTAMP-TBD" in record_codes
        assert "AUDIT-RATIONALE-TBD" in record_codes
        assert result["records"][0]["validation_outcome"]["status"] == "TBD"
        assert result["records"][0]["diff_preview_ref"]["ref"] == "TBD"


    def test_output_boundary_language_does_not_make_prohibited_claims():
        result = record_operation_audit_trail(
            operation_envelope(),
            validation_outcome=validate_and_preview_operations(operation_envelope(), model_state()),
            diff_preview_ref=preview_ref(),
            acceptance_signal=user_acceptance(),
        )
        text = canonical_json(result).lower()

        for forbidden in [
            "code compliant",
            "certified",
            "sealed",
            "authenticated",
            "professional approval",
            "engineering acceptance",
        ]:
            assert forbidden not in text
        assert result["professional_boundary"]["software_makes_approval_claim"] is False


    def main():
        test_user_accepted_operation_record_is_deterministic_and_complete()
        test_operation_cannot_be_accepted_without_explicit_user_signal()
        test_blocked_validation_outcome_prevents_accepted_record()
        test_current_model_state_hash_is_required_for_accepted_record()
        test_rejected_operation_is_recorded_without_mutating_accepted_state()
        test_missing_inputs_are_visible_tbd_diagnostics()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_operation_validation_preview.py

    #!/usr/bin/env python3
    """Focused tests for DEL-16-02 operation validation and diff preview."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.constraints.validation.engine import (  # noqa: E402
        CANONICAL_DIMENSIONS as CONSTRAINT_CANONICAL_DIMENSIONS,
    )
    from core.gui.pkg02_boundary import (  # noqa: E402
        CANONICAL_DIMENSIONS as GUI_CANONICAL_DIMENSIONS,
    )
    from core.model_operations.validation_preview import (  # noqa: E402
        canonical_json,
        validate_and_preview_operations,
    )
    from core.model_operations.validation_preview.engine import (  # noqa: E402
        CANONICAL_DIMENSIONS,
    )


    OPERATION_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_operation_set_valid.json"
    MODEL_STATE_FIXTURE = ROOT / "fixtures" / "model_operations" / "invented_accepted_model_state.json"
    UNITS_SCHEMA = ROOT / "schemas" / "units.schema.yaml"


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def model_state():
        with MODEL_STATE_FIXTURE.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def operation_envelope(change):
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        operation = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )
        operation["changes"] = [change]
        envelope["operation_set"]["operations"] = [operation]
        return envelope


    def quantity_change():
        with OPERATION_FIXTURE.open(encoding="utf-8") as fixture_file:
            envelope = json.load(fixture_file)
        operation = next(
            item for item in envelope["operation_set"]["operations"] if item["operation_id"] == "op:resize"
        )
        return deepcopy(operation["changes"][0])


    def test_valid_operation_generates_stable_preview_without_mutating_state():
        accepted = model_state()
        original = deepcopy(accepted)
        first = validate_and_preview_operations(operation_envelope(quantity_change()), accepted)
        second = validate_and_preview_operations(operation_envelope(quantity_change()), deepcopy(accepted))

        assert canonical_json(first) == canonical_json(second)
        assert accepted == original
        assert first["validation"]["schema_validation"] == "passed"
        assert first["validation"]["unit_validation"] == "passed"
        assert first["validation"]["diff_preview_status"] == "generated"
        assert first["validation"]["application_status"] == "not_applied"
        assert first["accepted_model_state_ref"]["hash"] == "sha256:invented-state-001"
        assert first["diff_preview"][0]["before"]["diameter"]["value"] == 100.0
        assert first["diff_preview"][0]["after"]["diameter"]["value"] == 125.0


    def test_missing_unit_metadata_blocks_preview():
        change = quantity_change()
        change["value_payload"]["quantity_values"] = [{"value": 125.0}]
        result = validate_and_preview_operations(operation_envelope(change), model_state())

        codes = {item["code"] for item in result["diagnostics"]}
        assert "OP-UNIT-METADATA-MISSING" in codes
        assert result["validation"]["diff_preview_status"] == "blocked_by_validation"
        assert result["diff_preview"][0]["preview_status"] == "blocked_by_validation"


    def test_unknown_dimension_blocks_unit_validation():
        change = quantity_change()
        change["value_payload"]["quantity_values"][0]["dimension"] = "temperature_difference"
        result = validate_and_preview_operations(operation_envelope(change), model_state())

        codes = {item["code"] for item in result["diagnostics"]}
        assert "OP-UNIT-DIMENSION-UNKNOWN" in codes
        assert result["validation"]["unit_validation"] == "blocked"
        assert result["validation"]["diff_preview_status"] == "blocked_by_validation"


    def test_force_per_length_dimension_is_accepted_in_quantity_payloads():
        change = quantity_change()
        change["value_payload"]["quantity_values"][0].update(
            {"value": 250.0, "unit": "N/m", "dimension": "force_per_length"}
        )
        result = validate_and_preview_operations(operation_envelope(change), model_state())

        codes = {item["code"] for item in result["diagnostics"]}
        assert "OP-UNIT-DIMENSION-UNKNOWN" not in codes
        assert "OP-UNIT-METADATA-MISSING" not in codes
        assert result["validation"]["unit_validation"] == "passed"
        assert result["validation"]["diff_preview_status"] == "generated"


    def test_canonical_dimensions_match_accepted_pkg02_vocabulary():
        with UNITS_SCHEMA.open(encoding="utf-8") as schema_file:
            accepted = json.load(schema_file)["$defs"]["DimensionId"]["enum"]

        assert CANONICAL_DIMENSIONS == set(accepted)
        assert CONSTRAINT_CANONICAL_DIMENSIONS == set(accepted)
        assert list(GUI_CANONICAL_DIMENSIONS) == accepted


    def test_unresolved_target_and_constraint_findings_are_blocking():
        change = quantity_change()
        change["target_ref"] = ref("Component", "component:missing")
        result = validate_and_preview_operations(
            operation_envelope(change),
            model_state(),
            constraint_diagnostics=[{"code": "CV-BLOCK", "severity": "blocking"}],
        )

        codes = {item["code"] for item in result["diagnostics"]}
        assert "OP-TARGET-REF-UNRESOLVED" in codes
        assert "OP-CONSTRAINT-BLOCKING" in codes
        assert result["validation"]["constraint_validation"] == "blocked"


    def test_direct_mutation_request_is_rejected():
        envelope = operation_envelope(quantity_change())
        operation = envelope["operation_set"]["operations"][0]
        operation["validation"]["application_status"] = "applied"
        result = validate_and_preview_operations(envelope, model_state())

        assert "OP-DIRECT-MUTATION-BLOCKED" in {item["code"] for item in result["diagnostics"]}
        assert result["validation"]["application_status"] == "not_applied"


    def test_schema_invalid_envelope_cannot_report_schema_passed():
        envelope = operation_envelope(quantity_change())
        del envelope["operation_contract_status"]
        result = validate_and_preview_operations(envelope, model_state())

        assert "OP-SCHEMA-VALIDATION-FAILED" in {item["code"] for item in result["diagnostics"]}
        assert result["validation"]["schema_validation"] == "blocked"
        assert result["validation"]["diff_preview_status"] == "blocked_by_validation"


    def test_model_role_and_current_hash_are_required_before_preview():
        accepted = model_state()
        accepted["model"]["model_role"] = "analytical_solver_model"
        envelope = operation_envelope(quantity_change())
        envelope["operation_set"]["operations"][0]["preconditions"]["required_current_hashes"][0]["value"] = "sha256:stale"
        result = validate_and_preview_operations(envelope, accepted)

        codes = {item["code"] for item in result["diagnostics"]}
        assert "OP-ACCEPTED-STATE-MODEL-ROLE-BLOCKED" in codes
        assert "OP-CURRENT-HASH-MISMATCH" in codes
        assert result["validation"]["schema_validation"] == "passed"
        assert result["validation"]["diff_preview_status"] == "blocked_by_validation"


    def test_output_boundary_language_does_not_make_prohibited_claims():
        result = validate_and_preview_operations(operation_envelope(quantity_change()), model_state())
        text = canonical_json(result).lower()

        for forbidden in [
            "code compliant",
            "certified",
            "sealed",
            "authenticated",
            "professional approval",
            "engineering acceptance",
        ]:
            assert forbidden not in text
        assert result["professional_boundary"]["software_makes_approval_claim"] is False


    def main():
        test_valid_operation_generates_stable_preview_without_mutating_state()
        test_missing_unit_metadata_blocks_preview()
        test_unknown_dimension_blocks_unit_validation()
        test_force_per_length_dimension_is_accepted_in_quantity_payloads()
        test_canonical_dimensions_match_accepted_pkg02_vocabulary()
        test_unresolved_target_and_constraint_findings_are_blocking()
        test_direct_mutation_request_is_rejected()
        test_schema_invalid_envelope_cannot_report_schema_passed()
        test_model_role_and_current_hash_are_required_before_preview()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_pcf_export_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-07 conservative PCF export packages."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.pcf_export import (  # noqa: E402
        build_pcf_export_package,
        canonical_json,
        render_pcf_text,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "pcf_export.schema.json"
    PACKAGE_FIXTURE_PATH = ROOT / "fixtures" / "pcf_export" / "invented" / "pcf_export_package.json"
    PCF_FIXTURE_PATH = ROOT / "fixtures" / "pcf_export" / "invented" / "model.pcf"
    SOURCE_PAYLOAD_PATH = ROOT / "fixtures" / "pcf_export" / "invented" / "source_pcf_payload.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
        "compatible with caepipe",
    }


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def source_payload() -> dict[str, object]:
        return load_json(SOURCE_PAYLOAD_PATH)


    def build_from_source() -> dict[str, object]:
        return build_pcf_export_package(**source_payload())


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(PACKAGE_FIXTURE_PATH)
        built = build_from_source()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(PACKAGE_FIXTURE_PATH),
            )
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_pcf_export_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_package_members():
        first = build_from_source()
        second = build_from_source()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-07"
        assert first["package_status"] == "conservative_pcf_export_foundation"
        assert first["export_profile"]["target_family"] == "pcf"
        assert first["export_profile"]["target_profile_version_basis"] == "TBD"
        assert first["export_profile"]["identity_policy"] == "authoritative_sidecar_id_map"
        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "model_pcf",
            "unit_system_disclosure",
            "stable_id_map",
            "loss_report",
            "validation_report",
            "diagnostics",
        }
        assert first["unit_system_disclosure"]["unit_system_ref"]["ref"] == "unit-system:dec-018-si-dual-display"
        assert first["unit_system_disclosure"]["target_export_units"]["coordinates"] == "MM"
        assert first["unit_system_disclosure"]["conversion_performed"] is True
        assert "node.coordinates" in first["unit_system_disclosure"]["conversion_scope"]
        assert first["unit_system_disclosure"]["protected_content_included"] is False
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_pcf_text_is_byte_stable_ascii_and_sidecar_identity_is_authoritative():
        package = build_from_source()
        pcf_text = package["pcf_text"]

        assert pcf_text == render_pcf_text(package["pcf_payload"], package["export_profile"])
        assert pcf_text == PCF_FIXTURE_PATH.read_text(encoding="ascii")
        assert pcf_text.encode("ascii")
        assert pcf_text.endswith("END-ISOGEN\n")
        assert "PIPELINE-REFERENCE OPS-INVENTED-PCF-001" in pcf_text
        assert "COMPONENT-IDENTIFIER OPS-PIPE-AB" in pcf_text
        assert "OUTSIDE-DIAMETER 60.3" in pcf_text
        assert "WALL-THICKNESS 3.91" in pcf_text
        assert "element:invented:AB" not in pcf_text
        assert {
            entry["metadata_carrier"] for entry in package["stable_id_map"]
        } == {"sidecar_id_map"}


    def test_loss_report_covers_required_categories_and_tbd_boundaries():
        package = build_from_source()
        categories = {entry["category"] for entry in package["loss_report"]}

        assert categories == {
            "exported",
            "omitted",
            "approximated",
            "delegated",
            "unsupported",
            "tbd",
        }
        assert any("target profile/version remains unresolved" in entry["reason"] for entry in package["loss_report"])
        assert any("Hidden downstream translator defaults" in entry["reason"] for entry in package["loss_report"])
        assert package["export_profile"]["support_restraint_policy"] == "unsupported_or_tbd_until_source_confirmed"
        assert package["export_profile"]["translator_default_policy"] == "hidden_defaults_blocked_or_loss_reported"


    def test_negative_cases_block_hidden_defaults_and_missing_identity():
        payload = source_payload()
        payload["stable_id_map"] = []
        payload["pcf_payload"]["pipe_segments"][0] = deepcopy(payload["pcf_payload"]["pipe_segments"][0])
        del payload["pcf_payload"]["pipe_segments"][0]["wall_thickness"]
        payload["export_profile"] = {"target_profile_version_basis": "CAEPIPE-PCF"}

        package = build_pcf_export_package(**payload)
        codes = {item["code"] for item in package["diagnostics"]}

        assert "PCF-STABLE-ID-MAP-MISSING" in codes
        assert "PCF-EXPLICIT-FIELD-MISSING" in codes
        assert "PCF-TARGET-PROFILE-OVERCLAIM" in codes
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_profile_source_basis_refs_are_required():
        payload = source_payload()
        payload["export_profile"] = {"source_basis_refs": [{"object_type": "Deliverable", "ref": "DEL-17-02"}]}

        package = build_pcf_export_package(**payload)

        assert "PCF-SOURCE-BASIS-REFS-MISSING" in {item["code"] for item in package["diagnostics"]}
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_no_prohibited_professional_or_external_compatibility_language():
        package = build_from_source()
        text = "\n".join(walk_strings(package)).lower()

        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text
        boundary = package["professional_boundary"]
        assert boundary["software_makes_release_claim"] is False
        assert boundary["software_makes_target_compatibility_claim"] is False
        assert boundary["software_makes_solver_validation_claim"] is False
        assert boundary["software_makes_code_compliance_claim"] is False
        assert boundary["software_creates_professional_reliance_record"] is False


    if __name__ == "__main__":
        test_fixture_and_builder_validate_against_schema()
        test_builder_is_deterministic_and_preserves_package_members()
        test_pcf_text_is_byte_stable_ascii_and_sidecar_identity_is_authoritative()
        test_loss_report_covers_required_categories_and_tbd_boundaries()
        test_negative_cases_block_hidden_defaults_and_missing_identity()
        test_profile_source_basis_refs_are_required()
        test_no_prohibited_professional_or_external_compatibility_language()
        print("PASS: DEL-17-07 PCF export package checks")

## Component: tests/test_persistence_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the project persistence schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "project_persistence.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "persistence" / "invented_persisted_preview_project.json"


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture():
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def ref_name(ref):
        return ref.rsplit("/", 1)[-1]


    def check_schema_contract():
        schema = load_schema()

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False

        required = set(schema["required"])
        assert {"schema_version", "project", "hash", "migration"} <= required

        properties = schema["properties"]
        assert ref_name(properties["project"]["$ref"]) == "ProjectEnvelope"
        assert ref_name(properties["hash"]["$ref"]) == "HashMetadata"
        assert ref_name(properties["migration"]["$ref"]) == "MigrationStatus"
        assert ref_name(properties["validation_profile"]["$ref"]) == "ValidationProfile"
        assert ref_name(properties["professional_boundary"]["$ref"]) == "ProfessionalBoundary"
        assert (
            ref_name(properties["service_operations"]["items"]["$ref"])
            == "PersistenceOperation"
        )
        assert ref_name(properties["external_artifacts"]["items"]["$ref"]) == (
            "ExternalArtifactReference"
        )
        assert ref_name(properties["retrieval_sidecars"]["items"]["$ref"]) == (
            "RetrievalSidecar"
        )

        defs = schema["$defs"]
        project = defs["ProjectEnvelope"]
        assert {"project_id", "unit_system_ref", "model_payload", "private_data"} <= set(
            project["required"]
        )
        assert (
            ref_name(project["properties"]["human_acceptance_refs"]["items"]["$ref"])
            == "HumanAcceptanceRef"
        )
        assert ref_name(project["properties"]["run_history"]["$ref"]) == "RunHistory"

        model_payload_ref = project["properties"]["model_payload"]["$ref"]
        assert ref_name(model_payload_ref) == "ModelPayload"
        model_payload = defs["ModelPayload"]
        assert {"$ref": "model.schema.yaml"} in model_payload["allOf"]

        hash_metadata = defs["HashMetadata"]
        assert hash_metadata["properties"]["canonicalization"]["const"] == "JCS"
        assert {
            "canonicalization",
            "project_payload_hash",
            "hash_manifest",
            "payload_partition_status",
        } <= set(hash_metadata["required"])
        assert "non_json_or_binary_partition_TBD" in set(
            hash_metadata["properties"]["payload_partition_status"]["enum"]
        )
        assert "external_artifacts_by_reference" in set(
            hash_metadata["properties"]["payload_partition_status"]["enum"]
        )

        checksum = defs["Checksum"]
        assert {"algorithm", "canonicalization", "value"} <= set(checksum["required"])
        assert {
            "project_envelope",
            "project_payload",
            "model_payload",
            "rule_pack_reference",
            "input_manifest",
            "report_manifest",
            "external_artifact",
            "model_state_record",
            "analysis_run_record",
            "result_envelope",
            "result_value",
            "retrieval_sidecar_manifest",
            "TBD",
        } <= set(checksum["properties"]["payload_scope"]["enum"])

        migration = defs["MigrationStatus"]
        assert {"status", "source_schema_version", "target_schema_version"} <= set(
            migration["required"]
        )
        assert {
            "current",
            "migration_needed",
            "stale",
            "migrated",
            "unsupported_schema",
            "failed",
            "newer_than_supported",
            "TBD",
        } <= set(migration["properties"]["status"]["enum"])
        assert "db_migration_status" in migration["properties"]
        assert "product_schema_migration_status" in migration["properties"]
        assert {
            "application_service_separate_db_and_product_schema",
            "TBD",
        } <= set(migration["properties"]["migration_framework"]["enum"])

        private_data = defs["PrivateDataMarker"]
        assert {
            "classification",
            "redistribution_status",
            "default_transmission_allowed",
        } <= set(private_data["required"])
        assert private_data["properties"]["default_transmission_allowed"]["const"] is False

        physical = defs["PhysicalContainer"]
        assert {
            "status",
            "profile",
            "decision_ref",
            "storage_role",
            "canonical_truth",
            "sql_public_contract",
            "direct_sql_access_allowed",
            "hosted_db_allowed",
            "network_required",
            "sidecars_rebuildable",
        } <= set(physical["required"])
        assert "accepted" in set(physical["properties"]["status"]["enum"])
        assert "sqlite_local_project_store" in set(
            physical["properties"]["profile"]["enum"]
        )
        assert "SCA-003" in set(physical["properties"]["decision_ref"]["enum"])
        assert physical["properties"]["sql_public_contract"]["const"] is False
        assert physical["properties"]["direct_sql_access_allowed"]["const"] is False
        assert physical["properties"]["hosted_db_allowed"]["const"] is False
        assert physical["properties"]["network_required"]["const"] is False
        assert physical["properties"]["sidecars_rebuildable"]["const"] is True
        assert properties["physical_container"]["$ref"].endswith("/PhysicalContainer")

        external = defs["ExternalArtifactReference"]
        assert {
            "artifact_ref",
            "uri_or_path",
            "hash",
            "size_bytes",
            "classification",
            "verification_status",
            "copy_policy",
        } <= set(external["required"])
        assert external["properties"]["copy_policy"]["const"] == (
            "reference_in_place_by_default"
        )

        sidecar = defs["RetrievalSidecar"]
        assert {"sqlite_fts5_bm25", "numpy_vector_cache_optional"} <= set(
            sidecar["properties"]["sidecar_kind"]["enum"]
        )
        assert sidecar["properties"]["authoritative"]["const"] is False
        assert sidecar["properties"]["rebuildable"]["const"] is True
        assert sidecar["properties"]["affects_project_hash"]["const"] is False
        assert sidecar["properties"]["local_only"]["const"] is True

        round_trip = defs["RoundTripManifest"]
        assert {"serialization", "semantic_equality"} <= set(round_trip["required"])
        assert "canonical_json_jcs" in round_trip["properties"]["serialization"]["enum"]
        assert {
            "schema_approved_only",
            "no_silent_engineering_defaults",
            "documented_volatile_field_exclusion",
            "TBD",
        } <= set(round_trip["properties"]["normalization_rules"]["items"]["enum"])

        validation_profile = defs["ValidationProfile"]
        assert {
            "schema_validation",
            "model_schema_delegation",
            "unit_metadata_check",
            "provenance_check",
            "private_data_check",
            "professional_boundary_check",
        } <= set(validation_profile["required"])
        assert (
            validation_profile["properties"]["model_schema_delegation"]["const"]
            == "schemas/model.schema.yaml"
        )
        assert validation_profile["properties"]["telemetry_default"]["const"] == "off"

        operation = defs["PersistenceOperation"]
        assert {
            "create_project",
            "open_project",
            "save_project",
            "validate_project",
            "version_check",
            "migrate_project",
            "TBD",
        } <= set(operation["properties"]["operation"]["enum"])
        assert operation["properties"]["boundary"]["const"] == "application_service"
        assert operation["properties"]["bypass_prohibited"]["const"] is True
        assert {
            "SCHEMA_VALIDATION",
            "MIGRATION",
            "DB_MIGRATION",
            "PRODUCT_SCHEMA_MIGRATION",
            "UNIT_METADATA",
            "PROVENANCE_WARNING",
            "RULE_CHECK_BLOCKING",
            "IP_BOUNDARY_WARNING",
            "PRIVATE_DATA",
            "EXTERNAL_ARTIFACT",
            "PROFESSIONAL_BOUNDARY",
            "TBD",
        } <= set(operation["properties"]["diagnostic_classes"]["items"]["enum"])

        human_acceptance = defs["HumanAcceptanceRef"]
        assert {
            "acceptance_ref",
            "authority_kind",
            "binding_hashes",
            "invalidates_on_hash_change",
        } <= set(human_acceptance["required"])
        assert (
            human_acceptance["properties"]["invalidates_on_hash_change"]["const"] is True
        )
        assert "external_human_review" in set(
            human_acceptance["properties"]["authority_kind"]["enum"]
        )

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False

        run_history = defs["RunHistory"]
        assert {
            "model_state_refs",
            "analysis_run_refs",
            "result_envelope_refs",
            "result_refs",
            "hash_manifest",
        } <= set(run_history["required"])
        assert ref_name(run_history["properties"]["model_state_records"]["items"]["$ref"]) == (
            "model_state.schema.json"
        )
        assert ref_name(run_history["properties"]["analysis_run_records"]["items"]["$ref"]) == (
            "analysis_run.schema.json"
        )

        rule_pack_ref = defs["RulePackRef"]
        assert {
            "public_permissive",
            "private_only",
            "unknown",
            "protected_suspected",
            "TBD",
        } <= set(rule_pack_ref["properties"]["redistribution_status"]["enum"])


    def check_persistence_fixture_contract():
        fixture = load_fixture()

        assert fixture["document_kind"] == "openpipestress.project_persistence"
        assert fixture["physical_container"]["status"] == "accepted"
        assert fixture["physical_container"]["profile"] == "sqlite_local_project_store"
        assert fixture["physical_container"]["decision_ref"] == "SCA-003"
        assert fixture["physical_container"]["direct_sql_access_allowed"] is False
        assert fixture["physical_container"]["hosted_db_allowed"] is False
        assert fixture["physical_container"]["network_required"] is False
        assert fixture["migration"]["db_migration_status"] == "current"
        assert fixture["migration"]["product_schema_migration_status"] == "current"
        assert fixture["migration"]["migration_framework"] == (
            "application_service_separate_db_and_product_schema"
        )
        assert fixture["retrieval_sidecars"][0]["sidecar_kind"] == "sqlite_fts5_bm25"
        assert fixture["retrieval_sidecars"][0]["affects_project_hash"] is False
        assert fixture["round_trip_manifest"]["serialization"] == "canonical_json_jcs"
        assert "no_silent_engineering_defaults" in fixture["round_trip_manifest"][
            "normalization_rules"
        ]
        assert fixture["validation_profile"]["model_schema_delegation"] == (
            "schemas/model.schema.yaml"
        )
        assert fixture["validation_profile"]["telemetry_default"] == "off"
        assert fixture["project"]["private_data"]["default_transmission_allowed"] is False
        assert fixture["professional_boundary"]["human_review_required"] is True
        assert not fixture["professional_boundary"]["software_makes_compliance_claim"]
        assert not fixture["professional_boundary"]["software_makes_certification_claim"]
        assert not fixture["professional_boundary"]["software_makes_sealing_claim"]
        assert not fixture["professional_boundary"]["software_makes_approval_claim"]
        assert not fixture["professional_boundary"]["software_makes_authentication_claim"]

        scopes = {item["payload_scope"] for item in fixture["hash"]["hash_manifest"]}
        assert {"project_payload", "model_payload", "project_envelope"} <= scopes
        run_history = fixture["project"]["run_history"]
        assert run_history["analysis_run_refs"]
        assert run_history["result_envelope_refs"]
        assert run_history["result_refs"]
        assert "hash_manifest" in run_history


    def test_project_persistence_schema_contract():
        check_schema_contract()


    def test_project_persistence_fixture_preserves_foundation_boundaries():
        check_persistence_fixture_contract()


    def main():
        check_schema_contract()
        check_persistence_fixture_contract()


    if __name__ == "__main__":
        main()

## Component: tests/test_physical_to_analytical_transform.py

    #!/usr/bin/env python3
    """Focused tests for DEL-13-04 physical-to-analytical transform contract."""

    import json
    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.model_transform.physical_to_analytical.contract import (  # noqa: E402
        transform_physical_to_analytical,
    )
    from schema_validation import schema_for_definition, validate_instance  # noqa: E402


    MODEL_SCHEMA_PATH = ROOT / "schemas" / "model.schema.yaml"
    PHYSICAL_SOURCE_FIXTURE = ROOT / "fixtures" / "domain" / "invented_physical_source_of_truth_model.json"
    PREVIEW_ONLY_FIXTURE_KEYS = {
        "load_kind",
        "local_x_axis",
    }


    FORBIDDEN_CLAIMS = {
        "certification",
        "certified",
        "sealing",
        "sealed",
        "authentication",
        "code compliant",
        "professional approval",
        "engineering acceptance",
    }


    def provenance(source_name="invented transform fixture"):
        return {
            "source_name": source_name,
            "source_location": f"fixtures/{source_name.replace(' ', '_')}",
            "source_license": "public_permissive",
            "contributor": "DEL-13-04 test",
            "contributor_certification": "invented non-engineering transform fixture",
            "redistribution_status": "public_permissive",
            "review_status": "pending",
        }


    def ref(object_type, item_id):
        return {"object_type": object_type, "id": item_id}


    def quantity(value=1.0, unit="m", dimension="length"):
        return {
            "value": value,
            "unit": unit,
            "dimension": dimension,
            "provenance": provenance("quantity source"),
        }


    def load_json(path):
        return json.loads(path.read_text(encoding="utf-8"))


    def canonical_physical_model():
        return load_json(PHYSICAL_SOURCE_FIXTURE)["model"]


    def all_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from all_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from all_keys(item)


    def physical_model():
        return canonical_physical_model()


    def codes(result):
        return {item["code"] for item in result.diagnostics}


    def all_text(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from all_text(item)
        elif isinstance(value, (list, tuple)):
            for item in value:
                yield from all_text(item)


    def test_canonical_physical_source_fixture_validates_and_transforms_deterministically():
        schema = load_json(MODEL_SCHEMA_PATH)
        source = canonical_physical_model()

        assert validate_instance(
            schema_for_definition(schema, "Model"),
            source,
            schema_label=f"{MODEL_SCHEMA_PATH}#/$defs/Model",
            instance_label=str(PHYSICAL_SOURCE_FIXTURE),
        )
        assert source["model_role"] == "physical_source_of_truth"
        assert "source_model_ref" not in source
        assert PREVIEW_ONLY_FIXTURE_KEYS.isdisjoint(set(all_keys(source)))
        assert [item["id"] for item in source["nodes"]] == ["N-1", "N-2"]
        assert [item["id"] for item in source["elements"]] == ["E-1"]
        assert [item["id"] for item in source["materials"]] == ["MAT-1"]
        assert [item["id"] for item in source["sections"]] == ["SEC-1"]
        assert [item["id"] for item in source["supports"]] == ["SUP-1"]
        assert [item["id"] for item in source["load_cases"]] == ["LC-1"]
        assert source["diagnostics"][0]["code"] == "ASSUMPTION_VISIBLE"

        first = transform_physical_to_analytical(source).to_dict()
        second = transform_physical_to_analytical(deepcopy(source)).to_dict()

        assert first == second
        assert not first["has_blocking_findings"]
        assert first["diagnostics"] == []

        analytical = first["analytical_model"]
        assert analytical["model_role"] == "analytical_solver_model"
        assert analytical["source_model_ref"] == ref("Model", "PHYS-1")
        assert analytical["diagnostics"] == []
        assert analytical["provenance"]["source_location"] == "physical-model:PHYS-1"
        assert [item["id"] for item in analytical["nodes"]] == ["N-1", "N-2"]

        element = analytical["elements"][0]
        assert element["id"] == "E-1"
        assert element["element_type"] == "straight_pipe"
        assert element["material_ref"] == ref("Material", "MAT-1")
        assert element["section_ref"] == ref("Section", "SEC-1")
        assert element["local_coordinate_system"]["y_reference"] == [0.0, 1.0, 0.0]
        assert element["result_stations"] == [quantity(0.0), quantity(1.0), quantity(2.0)]

        support = analytical["supports"][0]
        assert support["id"] == "SUP-1"
        assert support["target_ref"] == ref("Node", "N-1")
        assert support["properties"]["linear_stiffness"] == quantity(1.0, "N/m", "linear_stiffness")

        load_case = analytical["load_cases"][0]
        assert load_case["id"] == "LC-1"
        assert load_case["provenance"] == provenance("load case source")
        assert [load["target_ref"] for load in load_case["loads"]] == [
            ref("Element", "E-1"),
            ref("Element", "E-1"),
            ref("Node", "N-2"),
        ]
        assert [load["load_record_type"] for load in load_case["loads"]] == [
            "element_uniform_distributed_force",
            "element_point_force",
            "nodal_moment",
        ]
        assert [load["quantity"] for load in load_case["loads"]] == [
            quantity(1.0, "N/m", "force_per_length"),
            quantity(2.0, "N", "force"),
            quantity(3.0, "N*m", "moment"),
        ]
        assert load_case["loads"][0]["span"] == {
            "start_fraction": quantity(0.0, "1", "dimensionless"),
            "end_fraction": quantity(1.0, "1", "dimensionless"),
        }
        assert load_case["loads"][1]["station_fraction"] == quantity(0.5, "1", "dimensionless")

        trace_sources = {
            (link["trace_type"], link["source_ref"]["object_type"], link["source_ref"]["id"])
            for link in analytical["traceability_links"]
        }
        assert {
            ("physical_to_analytical", "Node", "N-1"),
            ("physical_to_analytical", "Node", "N-2"),
            ("physical_to_analytical", "Element", "E-1"),
            ("physical_to_analytical", "Material", "MAT-1"),
            ("physical_to_analytical", "Section", "SEC-1"),
            ("physical_to_analytical", "Support", "SUP-1"),
            ("physical_to_analytical", "LoadCase", "LC-1"),
        } <= trace_sources


    def test_transform_is_deterministic_traceable_and_preserves_source_model():
        source = physical_model()
        original = deepcopy(source)

        first = transform_physical_to_analytical(source).to_dict()
        second = transform_physical_to_analytical(deepcopy(source)).to_dict()

        assert first == second
        assert source == original
        analytical = first["analytical_model"]
        assert analytical["model_role"] == "analytical_solver_model"
        assert analytical["source_model_ref"] == ref("Model", "PHYS-1")
        assert [item["id"] for item in analytical["nodes"]] == ["N-1", "N-2"]
        assert [item["id"] for item in analytical["elements"]] == ["E-1"]
        assert {link["source_ref"]["id"] for link in analytical["traceability_links"]} >= {
            "N-1",
            "N-2",
            "E-1",
            "MAT-1",
            "SEC-1",
            "SUP-1",
            "LC-1",
        }
        assert not first["has_blocking_findings"]


    def test_missing_units_and_unsupported_physical_records_are_explicit_findings():
        source = physical_model()
        next(item for item in source["nodes"] if item["id"] == "N-2")["coordinates"]["x"]["unit"] = ""
        source["elements"].append(
            {
                "id": "E-SOLID",
                "element_type": "solid",
                "start_node_ref": ref("Node", "N-1"),
                "end_node_ref": ref("Node", "N-2"),
                "material_ref": ref("Material", "MAT-1"),
                "section_ref": ref("Section", "SEC-1"),
                "local_coordinate_system": {"type": "cartesian", "axes": ["X", "Y", "Z"]},
                "result_stations": [quantity(0.0)],
            }
        )

        result = transform_physical_to_analytical(source)

        assert {
            "PTA-NODE-COORDINATE-UNIT",
            "PTA-ELEMENT-TYPE-UNSUPPORTED",
            "PTA-ELEMENT-END-NODE-UNRESOLVED",
        } <= codes(result)
        assert result.has_blocking_findings
        assert [item["id"] for item in result.analytical_model["nodes"]] == ["N-1"]
        assert [item["id"] for item in result.analytical_model["elements"]] == []
        assert any(
            link["source_ref"]["id"] == "E-SOLID"
            and link["target_ref"]["object_type"] == "Diagnostic"
            for link in result.traceability_links
        )


    def test_transform_rejects_noncanonical_quantity_dimensions():
        source = physical_model()
        source["sections"][0]["properties"]["legacy_area_moment"] = quantity(
            1.0,
            "m4",
            "area_moment",
        )

        result = transform_physical_to_analytical(source)

        assert "PTA-UNIT-DIMENSION-UNKNOWN" in codes(result)
        assert result.has_blocking_findings
        assert result.analytical_model["sections"] == []
        assert [item["id"] for item in result.analytical_model["elements"]] == []


    def test_straight_pipe_transform_preserves_solver_needed_records():
        result = transform_physical_to_analytical(physical_model())
        analytical = result.analytical_model

        assert not result.has_blocking_findings
        element = analytical["elements"][0]
        material = analytical["materials"][0]
        section = analytical["sections"][0]
        load_case = analytical["load_cases"][0]

        assert element["element_type"] == "straight_pipe"
        assert element["start_node_ref"] == ref("Node", "N-1")
        assert element["end_node_ref"] == ref("Node", "N-2")
        assert element["material_ref"] == ref("Material", "MAT-1")
        assert element["section_ref"] == ref("Section", "SEC-1")
        assert element["result_stations"][0]["unit"] == "m"
        assert element["result_stations"][0]["dimension"] == "length"

        assert material["properties"]["elastic_modulus"]["unit"] == "Pa"
        assert material["properties"]["elastic_modulus"]["dimension"] == "stress"
        assert section["properties"]["area"]["unit"] == "m2"
        assert section["properties"]["area"]["dimension"] == "area"
        assert section["properties"]["second_moment_area"]["unit"] == "m4"
        assert section["properties"]["second_moment_area"]["dimension"] == "second_moment_area"
        assert load_case["loads"][0]["target_ref"] == ref("Element", "E-1")
        assert load_case["loads"][0]["load_record_type"] == "element_uniform_distributed_force"
        assert load_case["loads"][0]["quantity"]["unit"] == "N/m"
        assert load_case["loads"][0]["quantity"]["dimension"] == "force_per_length"
        assert load_case["loads"][0]["span"]["start_fraction"]["dimension"] == "dimensionless"
        assert load_case["loads"][0]["span"]["end_fraction"]["dimension"] == "dimensionless"
        assert load_case["loads"][1]["load_record_type"] == "element_point_force"
        assert load_case["loads"][1]["station_fraction"]["dimension"] == "dimensionless"
        assert load_case["loads"][1]["quantity"]["dimension"] == "force"
        assert load_case["loads"][2]["load_record_type"] == "nodal_moment"
        assert load_case["loads"][2]["target_ref"] == ref("Node", "N-2")
        assert load_case["loads"][2]["quantity"]["dimension"] == "moment"

        trace_targets = {
            (link["source_ref"]["object_type"], link["source_ref"]["id"]): link["target_ref"]
            for link in analytical["traceability_links"]
        }
        for item in [
            ("Element", "E-1"),
            ("Material", "MAT-1"),
            ("Section", "SEC-1"),
            ("LoadCase", "LC-1"),
        ]:
            assert trace_targets[item]["object_type"] == item[0]
            assert trace_targets[item]["id"] == item[1]


    def test_supported_component_metadata_passes_through_when_referenced_by_valid_element():
        source = physical_model()
        component = {
            "id": "COMP-VALVE-1",
            "component_type": "valve",
            "name": "Invented metadata valve",
            "geometry": {
                "face_to_face": quantity(1.0, "m", "length"),
            },
            "mechanics_modifiers": [],
            "provenance": provenance("component metadata source"),
        }
        source["components"] = [component]
        source["elements"][0]["component_ref"] = ref("Component", "COMP-VALVE-1")

        result = transform_physical_to_analytical(source)
        analytical = result.analytical_model

        assert not result.has_blocking_findings
        assert result.diagnostics == ()
        assert analytical["components"] == [component]
        assert analytical["elements"][0]["component_ref"] == ref("Component", "COMP-VALVE-1")

        trace_targets = {
            (link["source_ref"]["object_type"], link["source_ref"]["id"]): link["target_ref"]
            for link in analytical["traceability_links"]
        }
        assert trace_targets[("Component", "COMP-VALVE-1")] == ref("Component", "COMP-VALVE-1")
        assert trace_targets[("Element", "E-1")] == ref("Element", "E-1")


    def test_unsupported_component_reference_blocks_element_without_analytical_approximation():
        source = physical_model()
        source["components"] = [
            {
                "id": "COMP-BEND-1",
                "component_type": "bend",
                "name": "Invented unsupported bend metadata",
                "geometry": {
                    "bend_centerline_radius": quantity(1.0, "m", "length"),
                },
                "mechanics_modifiers": [],
                "provenance": provenance("unsupported component source"),
            }
        ]
        source["elements"][0]["component_ref"] = ref("Component", "COMP-BEND-1")

        result = transform_physical_to_analytical(source)

        assert {
            "PTA-COMPONENT-TYPE-UNSUPPORTED",
            "PTA-ELEMENT-COMPONENT-UNSUPPORTED",
        } <= codes(result)
        assert result.has_blocking_findings
        assert result.analytical_model["components"] == []
        assert result.analytical_model["elements"] == []
        assert any(
            link["source_ref"] == ref("Component", "COMP-BEND-1")
            and link["target_ref"]["object_type"] == "Diagnostic"
            for link in result.traceability_links
        )
        assert any(
            link["source_ref"] == ref("Element", "E-1")
            and link["target_ref"]["object_type"] == "Diagnostic"
            for link in result.traceability_links
        )


    def test_non_axis_aligned_load_metadata_survives_transform():
        source = physical_model()
        source_nodes = {item["id"]: item for item in source["nodes"]}
        source_nodes["N-2"]["coordinates"]["x"] = quantity(0.0)
        source_nodes["N-2"]["coordinates"]["y"] = quantity(4.0)
        source["elements"][0]["local_coordinate_system"] = {
            "type": "cartesian",
            "axes": ["X", "Y", "Z"],
            "y_reference": [1, 0, 0],
            "provenance": provenance("orientation source"),
        }
        source["load_cases"][0]["loads"] = [
            {
                "load_record_type": "element_uniform_distributed_force",
                "target_ref": ref("Element", "E-1"),
                "span": {
                    "start_fraction": quantity(0.0, "1", "dimensionless"),
                    "end_fraction": quantity(1.0, "1", "dimensionless"),
                },
                "direction": "X",
                "quantity": quantity(1.0, "N/m", "force_per_length"),
                "provenance": provenance("distributed x load source"),
            },
            {
                "load_record_type": "element_point_force",
                "target_ref": ref("Element", "E-1"),
                "station_fraction": quantity(0.5, "1", "dimensionless"),
                "direction": "X",
                "quantity": quantity(2.0, "N", "force"),
                "provenance": provenance("point x force source"),
            },
        ]

        result = transform_physical_to_analytical(source)
        analytical = result.analytical_model

        assert not result.has_blocking_findings
        assert analytical["source_model_ref"] == ref("Model", "PHYS-1")

        nodes = {item["id"]: item for item in analytical["nodes"]}
        assert nodes["N-2"]["coordinates"]["x"] == quantity(0.0)
        assert nodes["N-2"]["coordinates"]["y"] == quantity(4.0)

        element = analytical["elements"][0]
        assert element["id"] == "E-1"
        assert element["local_coordinate_system"]["y_reference"] == [1, 0, 0]
        assert element["local_coordinate_system"]["provenance"] == provenance("orientation source")

        load_case = analytical["load_cases"][0]
        loads = load_case["loads"]
        assert load_case["id"] == "LC-1"
        assert load_case["provenance"] == provenance("load case source")
        assert loads[0]["load_record_type"] == "element_uniform_distributed_force"
        assert loads[0]["target_ref"] == ref("Element", "E-1")
        assert loads[0]["direction"] == "X"
        assert loads[0]["span"]["start_fraction"] == quantity(0.0, "1", "dimensionless")
        assert loads[0]["span"]["end_fraction"] == quantity(1.0, "1", "dimensionless")
        assert loads[0]["quantity"] == quantity(1.0, "N/m", "force_per_length")
        assert loads[0]["provenance"] == provenance("distributed x load source")
        assert loads[1]["load_record_type"] == "element_point_force"
        assert loads[1]["target_ref"] == ref("Element", "E-1")
        assert loads[1]["direction"] == "X"
        assert loads[1]["station_fraction"] == quantity(0.5, "1", "dimensionless")
        assert loads[1]["quantity"] == quantity(2.0, "N", "force")
        assert loads[1]["provenance"] == provenance("point x force source")

        trace_targets = {
            (link["source_ref"]["object_type"], link["source_ref"]["id"]): link["target_ref"]
            for link in analytical["traceability_links"]
        }
        assert trace_targets[("Element", "E-1")] == ref("Element", "E-1")
        assert trace_targets[("LoadCase", "LC-1")] == ref("LoadCase", "LC-1")


    def test_unresolved_load_quantity_dimension_blocks_transform_without_inference():
        source = physical_model()
        source["load_cases"][0]["loads"].append(
            {
                "load_record_type": "element_uniform_distributed_force",
                "target_ref": ref("Element", "E-1"),
                "span": {
                    "start_fraction": quantity(0.0, "1", "dimensionless"),
                    "end_fraction": quantity(1.0, "1", "dimensionless"),
                },
                "direction": "Y",
                "quantity": quantity(4.0, "N/m", "TBD"),
                "provenance": provenance("unresolved line-load dimension source"),
            }
        )

        result = transform_physical_to_analytical(source)

        assert "PTA-LOAD-QUANTITY-UNIT" in codes(result)
        assert result.has_blocking_findings
        assert result.analytical_model["load_cases"] == []
        assert any(
            link["source_ref"]["id"] == "LC-1"
            and link["target_ref"]["object_type"] == "Diagnostic"
            for link in result.traceability_links
        )


    def test_transform_output_contains_no_prohibited_authority_claims():
        result = transform_physical_to_analytical(physical_model()).to_dict()
        rendered = "\n".join(all_text(result)).lower()

        for claim in FORBIDDEN_CLAIMS:
            assert claim not in rendered


    if __name__ == "__main__":
        test_canonical_physical_source_fixture_validates_and_transforms_deterministically()
        test_transform_is_deterministic_traceable_and_preserves_source_model()
        test_missing_units_and_unsupported_physical_records_are_explicit_findings()
        test_transform_rejects_noncanonical_quantity_dimensions()
        test_straight_pipe_transform_preserves_solver_needed_records()
        test_supported_component_metadata_passes_through_when_referenced_by_valid_element()
        test_unsupported_component_reference_blocks_element_without_analytical_approximation()
        test_non_axis_aligned_load_metadata_survives_transform()
        test_unresolved_load_quantity_dimension_blocks_transform_without_inference()
        test_transform_output_contains_no_prohibited_authority_claims()

## Component: tests/test_plugin_manifest_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the plugin manifest schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "plugin_manifest.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "plugin_manifest" / "invented_manifest_no_bypass.json"

    REQUIRED_TOP_LEVEL = {
        "metadata",
        "api_boundary_compatibility",
        "entrypoints",
        "permissions",
        "provenance",
        "privacy",
        "checksums",
        "sandbox",
        "no_bypass_constraints",
        "professional_boundary",
    }

    REQUIRED_NO_BYPASS = {
        "unit_controls",
        "provenance_controls",
        "privacy_controls",
        "rule_sandbox_controls",
        "analysis_boundary_controls",
        "persistence_controls",
        "human_acceptance_controls",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture():
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def definition(schema, name):
        return schema["$defs"][name]


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        assert REQUIRED_TOP_LEVEL <= set(schema["required"])
        assert schema["additionalProperties"] is False

        permissions = definition(schema, "PermissionModel")
        assert "denied_by_default" in permissions["required"]
        assert permissions["properties"]["denied_by_default"]["const"] is True
        assert permissions["properties"]["grant_state"]["enum"][0] == "not_granted"

        sandbox = definition(schema, "SandboxDeclaration")
        assert "sandbox_required" in sandbox["required"]
        assert sandbox["properties"]["sandbox_required"]["const"] is True
        assert sandbox["properties"]["arbitrary_code_execution_allowed"]["const"] is False
        assert sandbox["properties"]["filesystem_access_default"]["enum"][0] == "denied"
        assert sandbox["properties"]["network_access_default"]["enum"][0] == "denied"
        assert sandbox["properties"]["process_spawn_default"]["enum"] == ["denied"]
        assert sandbox["properties"]["capability_declaration_required"]["const"] is True

        provenance = definition(schema, "ProvenanceRecord")
        required_provenance = {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
        }
        assert required_provenance <= set(provenance["required"])

        no_bypass = definition(schema, "NoBypassConstraints")
        assert REQUIRED_NO_BYPASS <= set(no_bypass["required"])
        for control in REQUIRED_NO_BYPASS:
            assert no_bypass["properties"][control]["const"] is True

        privacy = definition(schema, "PrivacyDeclaration")
        assert privacy["properties"]["local_first"]["const"] is True
        assert privacy["properties"]["private_data_transmission_default"]["const"] is False
        assert privacy["properties"]["telemetry_enabled_by_default"]["const"] is False
        assert privacy["properties"]["redaction_supported"]["const"] is True

        compatibility = definition(schema, "ApiBoundaryCompatibility")
        assert compatibility["properties"]["domain_contract_ref"]["const"] == (
            "docs/architecture/extension_domain_contracts.md"
        )
        assert compatibility["properties"]["api_boundary_contract_ref"]["const"] == (
            "api/api_boundary_contract.yaml"
        )
        assert compatibility["properties"]["schema_version_contract"]["enum"][0] == (
            "JSON Schema 2020-12"
        )
        assert compatibility["properties"]["result_envelope_required"]["const"] is True

        entrypoint = definition(schema, "Entrypoint")
        assert "domain_surface" in entrypoint["required"]
        assert "canonical_model" in entrypoint["properties"]["domain_surface"]["enum"]
        assert "project_persistence" in entrypoint["properties"]["domain_surface"]["enum"]
        assert "persistence_access" in entrypoint["properties"]

        persistence_access = definition(schema, "PersistenceAccess")
        assert persistence_access["additionalProperties"] is False
        assert persistence_access["properties"]["access_mode"]["const"] == (
            "application_service_command_query_job_only"
        )
        assert persistence_access["properties"]["direct_sql_allowed"]["const"] is False
        assert (
            persistence_access["properties"]["raw_sqlite_handle_allowed"]["const"] is False
        )
        assert (
            persistence_access["properties"]["table_name_coupling_allowed"]["const"] is False
        )
        assert (
            persistence_access["properties"]["direct_store_mutation_allowed"]["const"] is False
        )

        professional_boundary = definition(schema, "ProfessionalBoundary")
        assert (
            professional_boundary["properties"][
                "human_acceptance_record_software_generated"
            ]["const"]
            is False
        )


    def check_plugin_manifest_fixture():
        schema = load_schema()
        manifest = load_fixture()

        assert REQUIRED_TOP_LEVEL <= set(manifest)
        assert manifest["manifest_kind"] == "openpipestress.plugin_manifest"
        assert manifest["permissions"]["denied_by_default"] is True
        assert manifest["permissions"]["grant_state"] == "not_granted"
        assert manifest["sandbox"]["sandbox_required"] is True
        assert manifest["sandbox"]["arbitrary_code_execution_allowed"] is False
        assert manifest["sandbox"]["filesystem_access_default"] == "denied"
        assert manifest["sandbox"]["network_access_default"] == "denied"
        assert manifest["sandbox"]["process_spawn_default"] == "denied"
        assert manifest["privacy"]["local_first"] is True
        assert manifest["privacy"]["private_data_transmission_default"] is False
        assert manifest["privacy"]["telemetry_enabled_by_default"] is False
        assert manifest["privacy"]["redaction_supported"] is True

        for control in definition(schema, "NoBypassConstraints")["required"]:
            assert manifest["no_bypass_constraints"][control] is True

        surfaces = {entry["domain_surface"] for entry in manifest["entrypoints"]}
        assert {"canonical_model", "project_persistence", "units"} <= surfaces
        assert manifest["api_boundary_compatibility"]["transport"] == "TBD"
        assert manifest["professional_boundary"]["human_review_required"] is True
        assert (
            manifest["professional_boundary"]["human_acceptance_record_software_generated"]
            is False
        )


    def test_plugin_manifest_schema_contract():
        check_schema_contract()


    def test_plugin_manifest_fixture_preserves_no_bypass_defaults():
        check_plugin_manifest_fixture()


    def main():
        check_schema_contract()
        check_plugin_manifest_fixture()


    if __name__ == "__main__":
        main()

## Component: tests/test_project_persistence_service.py

    #!/usr/bin/env python3
    """Focused tests for TP-PER-01 project persistence service behavior."""

    import json
    import sys
    from copy import deepcopy
    from hashlib import sha256
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.model_transform.physical_to_analytical.contract import (  # noqa: E402
        transform_physical_to_analytical,
    )
    from core.project_persistence import (
        build_project_persistence_envelope,
        canonical_json,
        create_project_store,
        external_artifact_reference,
        open_project_store,
        physical_container_profile,
        project_hash_manifest,
        rebuild_retrieval_sidecars,
        round_trip_project_envelope,
        save_project_store,
        validate_external_artifact_references,
        validate_project_persistence_envelope,
        version_check_project_store,
    )
    from schema_validation import validate_instance  # noqa: E402


    FIXTURE_PATH = ROOT / "fixtures" / "persistence" / "invented_persisted_preview_project.json"
    MODEL_SCHEMA_PATH = ROOT / "schemas" / "model.schema.yaml"
    PERSISTENCE_SCHEMA_PATH = ROOT / "schemas" / "project_persistence.schema.yaml"
    MODEL_STATE_SCHEMA_PATH = ROOT / "schemas" / "model_state.schema.json"
    ANALYSIS_RUN_SCHEMA_PATH = ROOT / "schemas" / "analysis_run.schema.json"
    PHYSICAL_SOURCE_FIXTURE = ROOT / "fixtures" / "domain" / "invented_physical_source_of_truth_model.json"


    def persisted_project():
        return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


    def load_json(path):
        return json.loads(path.read_text(encoding="utf-8"))


    def artifact_ref(ref_kind, ref):
        return {"ref_kind": ref_kind, "ref": ref}


    def state_ref(object_type, ref, label=None):
        value = {"object_type": object_type, "ref": ref}
        if label is not None:
            value["label"] = label
        return value


    def invented_public_provenance(source_name):
        return {
            "source_name": source_name,
            "source_location": "tests/test_project_persistence_service.py",
            "source_license": "project-governed-invented-fixture",
            "contributor": "OpenPipeStress Type 2 worker",
            "contributor_certification": "invented non-engineering schema fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "accepted",
            "privacy_classification": "invented_public_example",
        }


    def state_checksum(payload_ref, payload_scope, value):
        return {
            "algorithm": "sha256",
            "canonicalization": "JCS",
            "payload_ref": payload_ref,
            "payload_scope": payload_scope,
            "value": value,
        }


    def professional_boundary():
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        }


    def invented_model_state_record(model_payload, *, note_statement=None):
        state_id = "state:tp-per-01-invented-preview"
        model_id = model_payload["project"]["models"][0]["id"]
        provenance = invented_public_provenance(
            "Invented DEL-14-01 model-state persistence record"
        )
        model_ref = state_ref("Model", model_id, "Invented transformed analytical model")
        return {
            "schema_version": "0.1.0",
            "deliverable_id": "DEL-14-01",
            "package_id": "PKG-14",
            "scope_item": "SOW-071",
            "objectives": ["OBJ-016"],
            "state_contract_status": {
                "record_contract": "schema_first_model_state_records",
                "persistence_binding": "schemas/project_persistence.schema.yaml",
                "canonicalization": "JCS_compatible_json_payload_hashes",
                "physical_project_container": {
                    "profile": "sqlite_local_project_store",
                    "decision_ref": "SCA-003",
                    "storage_role": "local_store_index_projection",
                    "canonical_truth": "canonical_json_jcs_payload",
                    "sql_public_contract": False,
                    "direct_sql_access_allowed": False,
                    "hosted_db_allowed": False,
                    "network_required": False,
                    "sidecars_rebuildable": True,
                },
                "external_human_acceptance": "hash_bound_external_record_only",
            },
            "model_state": {
                "state_id": state_id,
                "state_name": "TP-PER-01 invented preview state",
                "state_kind": "design_snapshot",
                "created_at": "2026-06-06T00:00:00Z",
                "model_ref": model_ref,
                "parent_state_refs": [],
                "tags": [
                    {
                        "tag": "invented-preview",
                        "tag_kind": "workflow_label",
                        "provenance": provenance,
                    }
                ],
                "notes": [
                    {
                        "note_id": "note:tp-per-01-preview",
                        "note_type": "design_note",
                        "statement": note_statement
                        or "Invented model state for persistence round-trip evidence.",
                        "visibility": "public",
                        "provenance": provenance,
                    }
                ],
                "external_references": [
                    {
                        "reference_id": "external:tp-per-01-audit-manifest",
                        "reference_type": "audit_manifest",
                        "label": "Invented audit manifest reference",
                        "target": "audit-manifest:tp-per-01-invented-preview",
                        "binding_hashes": [
                            state_checksum(
                                state_ref(
                                    "AuditManifest",
                                    "audit-manifest:tp-per-01-invented-preview",
                                ),
                                "audit_manifest",
                                "invented-audit-manifest-placeholder-hash",
                            )
                        ],
                        "privacy_classification": "invented_public_example",
                        "provenance": provenance,
                    }
                ],
                "unresolved_assumptions": [
                    {
                        "assumption_id": "assumption:tp-per-01-review-needed",
                        "statement": (
                            "Invented fixture keeps professional review as an "
                            "explicit unresolved assumption."
                        ),
                        "status": "unresolved",
                        "affected_refs": [model_ref],
                        "provenance": provenance,
                    }
                ],
                "warnings": [
                    {
                        "code": "STATE_FIXTURE_REVIEW_ONLY",
                        "class": "ASSUMPTION_WARNING",
                        "severity": "warning",
                        "source": state_ref("ModelState", state_id),
                        "affected_object": model_ref,
                        "message": "Invented fixture is review evidence only.",
                        "remediation": "Use user-supplied project data and human review before reliance.",
                        "provenance": provenance,
                    }
                ],
                "analysis_status": ["MODEL_INCOMPLETE", "HUMAN_REVIEW_REQUIRED"],
                "hashes": [
                    state_checksum(
                        model_ref,
                        "model_payload",
                        sha256(canonical_json(model_payload).encode("utf-8")).hexdigest(),
                    )
                ],
                "immutability_policy": {
                    "snapshot_is_read_only": True,
                    "mutation_policy": "changes_create_new_model_state",
                    "new_state_required_for_change": True,
                    "hash_invalidates_external_acceptance": True,
                },
                "professional_boundary": professional_boundary(),
                "provenance": provenance,
            },
        }


    def state_record_hash_from(envelope):
        for item in envelope["project"]["run_history"]["hash_manifest"]:
            if item["payload_scope"] == "model_state_record":
                return item
        raise AssertionError("No model_state_record hash found in run history.")


    def validate_persistence_instance(instance, instance_label):
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
        from referencing.jsonschema import DRAFT202012

        persistence_schema = load_json(PERSISTENCE_SCHEMA_PATH)
        model_schema = load_json(MODEL_SCHEMA_PATH)
        model_state_schema = load_json(MODEL_STATE_SCHEMA_PATH)
        analysis_run_schema = load_json(ANALYSIS_RUN_SCHEMA_PATH)
        registry = Registry().with_resources(
            [
                (uri, Resource.from_contents(schema, default_specification=DRAFT202012))
                for uri, schema in (
                    (model_schema["$id"], model_schema),
                    ("https://openpipestress.org/schemas/model.schema.yaml", model_schema),
                    ("model.schema.yaml", model_schema),
                    (model_state_schema["$id"], model_state_schema),
                    ("https://openpipestress.org/schemas/model_state.schema.json", model_state_schema),
                    ("model_state.schema.json", model_state_schema),
                    (analysis_run_schema["$id"], analysis_run_schema),
                    ("https://openpipestress.org/schemas/analysis_run.schema.json", analysis_run_schema),
                    ("analysis_run.schema.json", analysis_run_schema),
                )
            ]
        )
        validator = Draft202012Validator(persistence_schema, registry=registry)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if errors:
            formatted = "\n".join(format_schema_error(error) for error in errors[:10])
            raise AssertionError(f"{instance_label} failed JSON Schema validation:\n{formatted}")


    def format_schema_error(error):
        path = "$"
        for part in error.path:
            path += f"[{part}]" if isinstance(part, int) else f".{part}"
        return f"{path}: {error.message}"


    def transformed_physical_source_payload():
        physical_model = load_json(PHYSICAL_SOURCE_FIXTURE)["model"]
        transform = transform_physical_to_analytical(physical_model)
        assert not transform.has_blocking_findings
        analytical_model = transform.analytical_model
        payload = {
            "schema_version": "0.1.0",
            "project": {
                "id": "project:tp-phys-012-derived",
                "name": "TP-PHYS-012 invented derived analytical project",
                "description": "Invented project payload derived from the canonical physical source fixture.",
                "unit_system": {
                    "id": "unit-system:tp-phys-012-si",
                    "description": "Invented SI-like unit metadata for transform persistence checks.",
                    "base_units": {
                        "length": "m",
                        "mass": "kg",
                        "force": "N",
                        "temperature": "degC",
                        "angle": "rad",
                    },
                },
                "privacy_class": "public",
                "storage_policy": "public_example",
                "models": [analytical_model],
                "rule_pack_refs": [],
                "report_settings": {
                    "id": "report-settings:tp-phys-012-derived",
                    "include_input_manifest": True,
                    "include_provenance_summary": True,
                    "include_professional_boundary_notice": True,
                    "result_refs": [],
                    "rule_pack_refs": [],
                    "provenance": analytical_model["provenance"],
                },
                "reports": [],
                "diagnostics": [],
                "hashes": [
                    {
                        "algorithm": "sha256",
                        "canonicalization": "JCS",
                        "payload_ref": {
                            "object_type": "Project",
                            "id": "project:tp-phys-012-derived",
                        },
                        "value": "tp-phys-012-invented-placeholder-hash",
                    }
                ],
            },
        }
        validate_instance(
            load_json(MODEL_SCHEMA_PATH),
            payload,
            schema_label=str(MODEL_SCHEMA_PATH),
            instance_label="TP-PHYS-012 derived analytical payload",
        )
        return payload


    def derived_transform_envelope(model_payload, *, model_state_records=None):
        state_refs = (
            [
                artifact_ref("model_state", item["model_state"]["state_id"])
                for item in model_state_records
            ]
            if model_state_records
            else [artifact_ref("model_state", "model-state:tp-phys-012-derived")]
        )
        return build_project_persistence_envelope(
            project_id="project:tp-phys-012-derived",
            project_name="TP-PHYS-012 invented derived analytical project",
            model_payload=model_payload,
            model_state_refs=state_refs,
            model_state_records=model_state_records,
            analysis_run_refs=[
                artifact_ref("analysis_run", "analysis-run:tp-phys-012-derived")
            ],
            result_envelope_refs=[
                artifact_ref("result_envelope", "result-envelope:tp-phys-012-derived")
            ],
            result_refs=[
                artifact_ref("result", "result:tp-phys-012-derived-schema-probe")
            ],
            provenance_manifest=[
                model_payload["project"]["models"][0]["provenance"],
            ],
        )


    def test_invented_persistence_fixture_validates_with_run_history_refs():
        envelope = persisted_project()
        run_history = envelope["project"]["run_history"]

        assert envelope["document_kind"] == "openpipestress.project_persistence"
        assert envelope["physical_container"]["status"] == "accepted"
        assert envelope["physical_container"]["profile"] == "sqlite_local_project_store"
        assert envelope["physical_container"]["decision_ref"] == "SCA-003"
        assert envelope["physical_container"]["direct_sql_access_allowed"] is False
        assert envelope["validation_profile"]["telemetry_default"] == "off"
        assert envelope["project"]["private_data"]["default_transmission_allowed"] is False
        assert validate_project_persistence_envelope(envelope) == []
        assert {item["ref"] for item in run_history["analysis_run_refs"]} == {
            "run:preview-linear-static-001"
        }
        assert "result-envelope:run:preview-linear-static-001" in {
            item["ref"] for item in run_history["result_envelope_refs"]
        }
        assert "result:stress:pipe-P-120:end-j:torsional-shear" in {
            item["ref"] for item in run_history["result_refs"]
        }
        assert "result:force:pipe-P-120:midspan:axial" in {
            item["ref"] for item in run_history["result_refs"]
        }
        assert "result:force:pipe-P-120:quarter-1:shear-y" in {
            item["ref"] for item in run_history["result_refs"]
        }
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial" in {
            item["ref"] for item in run_history["result_refs"]
        }
        assert "result:combination:combination-C-OPER-ALT:force:pipe-P-120:quarter-1:shear-y" in {
            item["ref"] for item in run_history["result_refs"]
        }
        model = envelope["project"]["model_payload"]["project"]["models"][0]
        assert "loadcase:L200" in {item["id"] for item in model["load_cases"]}
        assert "combination:C-OPER-ALT" in {item["id"] for item in model["combinations"]}


    def test_canonical_hashes_are_stable_and_cover_project_payloads():
        envelope = persisted_project()
        cloned = json.loads(canonical_json(envelope))

        assert canonical_json(envelope) == canonical_json(cloned)
        assert project_hash_manifest(envelope) == envelope["hash"]["hash_manifest"]
        scopes = {item["payload_scope"] for item in envelope["hash"]["hash_manifest"]}
        assert {"project_payload", "model_payload", "project_envelope"} <= scopes


    def test_round_trip_keeps_semantic_equality_and_hashes():
        round_trip = round_trip_project_envelope(persisted_project())

        assert round_trip["serialization"] == "canonical_json_jcs"
        assert round_trip["semantic_equal"] is True
        assert round_trip["diagnostics"] == []
        assert round_trip["source_hash"]["value"] == round_trip["round_trip_hash"]["value"]


    def test_model_state_record_embeds_in_run_history_with_deterministic_hash():
        model_payload = transformed_physical_source_payload()
        state_record = invented_model_state_record(model_payload)
        validate_instance(
            load_json(MODEL_STATE_SCHEMA_PATH),
            state_record,
            schema_label=str(MODEL_STATE_SCHEMA_PATH),
            instance_label="DEL-14-01 invented model state record",
        )

        envelope = derived_transform_envelope(
            model_payload,
            model_state_records=[state_record],
        )
        run_history = envelope["project"]["run_history"]
        state_hash = state_record_hash_from(envelope)
        expected_hash = sha256(canonical_json(state_record).encode("utf-8")).hexdigest()

        assert run_history["model_state_refs"] == [
            artifact_ref("model_state", state_record["model_state"]["state_id"])
        ]
        assert run_history["model_state_records"] == [state_record]
        assert state_hash["payload_ref"] == run_history["model_state_refs"][0]
        assert state_hash["payload_scope"] == "model_state_record"
        assert state_hash["value"] == expected_hash
        assert state_hash in envelope["hash"]["hash_manifest"]
        assert validate_project_persistence_envelope(envelope) == []
        validate_persistence_instance(
            envelope,
            "DEL-14-01 model-state-record persistence envelope",
        )


    def test_model_state_record_round_trips_through_persistence_store(tmp_path):
        model_payload = transformed_physical_source_payload()
        state_record = invented_model_state_record(model_payload)
        envelope = derived_transform_envelope(
            model_payload,
            model_state_records=[state_record],
        )
        state_hash = state_record_hash_from(envelope)

        round_trip = round_trip_project_envelope(envelope)
        assert round_trip["semantic_equal"] is True
        assert round_trip["diagnostics"] == []
        assert round_trip["envelope"]["project"]["run_history"]["model_state_records"] == [
            state_record
        ]
        assert state_record_hash_from(round_trip["envelope"]) == state_hash

        store_path = tmp_path / "state-record.opsdb"
        saved = save_project_store(store_path, envelope)
        opened = open_project_store(store_path)

        assert saved["diagnostics"] == []
        assert opened["diagnostics"] == []
        assert opened["envelope"]["project"]["run_history"]["model_state_records"] == [
            state_record
        ]
        assert state_record_hash_from(opened["envelope"]) == state_hash
        assert canonical_json(opened["envelope"]) == canonical_json(saved["envelope"])


    def test_model_state_record_payload_change_changes_persistence_hash():
        model_payload = transformed_physical_source_payload()
        original = derived_transform_envelope(
            model_payload,
            model_state_records=[invented_model_state_record(model_payload)],
        )
        changed = derived_transform_envelope(
            model_payload,
            model_state_records=[
                invented_model_state_record(
                    model_payload,
                    note_statement="Invented model state note changed for hash evidence.",
                )
            ],
        )

        assert state_record_hash_from(original)["value"] != state_record_hash_from(changed)[
            "value"
        ]
        assert project_hash_manifest(original) != project_hash_manifest(changed)


    def test_sqlite_store_round_trip_preserves_canonical_hashes(tmp_path):
        envelope = persisted_project()
        store_path = tmp_path / "project.opsdb"

        saved = create_project_store(store_path, envelope)
        opened = open_project_store(store_path)
        version = version_check_project_store(store_path)

        assert saved["diagnostics"] == []
        assert opened["diagnostics"] == []
        assert opened["envelope"]["hash"]["project_payload_hash"]["value"] == (
            saved["envelope"]["hash"]["project_payload_hash"]["value"]
        )
        assert canonical_json(opened["envelope"]) == canonical_json(saved["envelope"])
        assert version["db_migration_status"] == "current"
        assert version["product_schema_migration_status"] == "current"


    def test_retrieval_sidecar_rebuild_is_hash_neutral(tmp_path):
        store_path = tmp_path / "project.opsdb"
        saved = save_project_store(store_path, persisted_project())

        rebuild = rebuild_retrieval_sidecars(store_path)

        assert saved["diagnostics"] == []
        assert rebuild["sidecar_kind"] == "sqlite_fts5_bm25"
        assert rebuild["hash_neutral"] is True
        assert rebuild["before_hash"] == rebuild["after_hash"]


    def test_external_artifact_references_report_missing_and_private_without_copying(tmp_path):
        missing_path = tmp_path / "missing-large-file.dat"
        artifact = external_artifact_reference(
            artifact_id="external:large-file",
            uri_or_path=str(missing_path),
            size_bytes=1024,
            checksum_value="0" * 64,
            classification="private_project",
            verification_status="missing",
        )
        envelope = persisted_project()
        envelope["external_artifacts"] = [artifact]
        envelope["hash"] = {
            **envelope["hash"],
            "project_payload_hash": project_hash_manifest(envelope)[0],
            "hash_manifest": project_hash_manifest(envelope),
        }

        codes = {item["code"] for item in validate_external_artifact_references(envelope)}

        assert "PERSISTENCE_EXTERNAL_ARTIFACT_MISSING" in codes
        assert not missing_path.exists()


    def test_physical_container_profile_blocks_hosted_db_and_direct_sql():
        profile = physical_container_profile()

        assert profile["profile"] == "sqlite_local_project_store"
        assert profile["sql_public_contract"] is False
        assert profile["direct_sql_access_allowed"] is False
        assert profile["hosted_db_allowed"] is False
        assert profile["network_required"] is False
        assert profile["sidecars_rebuildable"] is True


    def test_mutation_changes_hash_and_validation_reports_mismatch():
        envelope = persisted_project()
        mutated = deepcopy(envelope)
        mutated["project"]["model_payload"]["project"]["name"] = "Changed invented project"

        assert project_hash_manifest(envelope) != project_hash_manifest(mutated)
        codes = {item["code"] for item in validate_project_persistence_envelope(mutated)}
        assert "PERSISTENCE_PROJECT_HASH_MISMATCH" in codes
        assert "PERSISTENCE_HASH_MANIFEST_MISMATCH" in codes


    def test_missing_boundary_fields_return_structured_diagnostics():
        envelope = persisted_project()
        del envelope["project"]["provenance_manifest"]
        del envelope["project"]["private_data"]
        del envelope["professional_boundary"]
        envelope["project"]["run_history"]["result_refs"] = []

        codes = {item["code"] for item in validate_project_persistence_envelope(envelope)}

        assert "PERSISTENCE_PROVENANCE_MISSING" in codes
        assert "PERSISTENCE_PRIVATE_DATA_BOUNDARY_INVALID" in codes
        assert "PERSISTENCE_PROFESSIONAL_BOUNDARY_VIOLATION" in codes
        assert "PERSISTENCE_RUN_HISTORY_REFS_MISSING" in codes


    def test_fixture_preserves_private_data_provenance_and_professional_boundaries():
        envelope = persisted_project()

        assert envelope["project"]["private_data"]["classification"] == "public_permissive"
        assert envelope["project"]["private_data"]["default_transmission_allowed"] is False
        assert envelope["project"]["provenance_manifest"]
        for item in envelope["project"]["provenance_manifest"]:
            assert item["redistribution_status"] == "public_permissive"
            assert item["review_status"] == "accepted"

        boundary = envelope["professional_boundary"]
        assert boundary["human_review_required"] is True
        assert not boundary["software_makes_compliance_claim"]
        assert not boundary["software_makes_certification_claim"]
        assert not boundary["software_makes_sealing_claim"]
        assert not boundary["software_makes_approval_claim"]
        assert not boundary["software_makes_authentication_claim"]


    def test_transformed_physical_fixture_embeds_in_schema_valid_persistence_envelope():
        model_payload = transformed_physical_source_payload()
        envelope = derived_transform_envelope(model_payload)
        model = envelope["project"]["model_payload"]["project"]["models"][0]

        assert model["model_role"] == "analytical_solver_model"
        assert model["source_model_ref"] == {"object_type": "Model", "id": "PHYS-1"}
        assert any(
            link["trace_type"] == "physical_to_analytical"
            and link["source_ref"] == {"object_type": "Element", "id": "E-1"}
            and link["target_ref"] == {"object_type": "Element", "id": "E-1"}
            for link in model["traceability_links"]
        )
        assert validate_project_persistence_envelope(envelope) == []
        validate_persistence_instance(
            envelope,
            "TP-PHYS-012 transformed physical fixture persistence envelope",
        )
        assert project_hash_manifest(envelope) == envelope["hash"]["hash_manifest"]

        round_trip = round_trip_project_envelope(envelope)
        assert round_trip["semantic_equal"] is True
        assert round_trip["diagnostics"] == []


    def test_persistence_schema_rejects_transformed_payload_with_noncanonical_dimension():
        model_payload = transformed_physical_source_payload()
        model_payload["project"]["models"][0]["sections"][0]["properties"]["area"][
            "dimension"
        ] = "area_moment"
        envelope = derived_transform_envelope(model_payload)

        assert validate_project_persistence_envelope(envelope) == []
        try:
            validate_persistence_instance(
                envelope,
                "TP-PHYS-012 noncanonical-dimension persistence envelope",
            )
        except AssertionError as exc:
            assert "area_moment" in str(exc)
        else:
            raise AssertionError("Noncanonical transformed payload dimension was accepted.")

## Component: tests/test_release_readiness_script.py

    from __future__ import annotations

    import importlib.util
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    MODULE_PATH = ROOT / "tools" / "release" / "check_release_readiness.py"


    def load_module():
        spec = importlib.util.spec_from_file_location("check_release_readiness", MODULE_PATH)
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module


    def test_required_release_paths_exist():
        release = load_module()
        assert release.check_required_paths(ROOT) == []


    def test_latest_dag_dependency_edges_uses_approved_graph_pointer():
        release = load_module()
        assert (
            release.latest_dag_dependency_edges(ROOT)
            == Path("execution/_DAG/DAG-006/DependencyEdges.csv")
        )


    def test_cargo_manifest_discovery_is_crate_local():
        release = load_module()
        manifests = release.discover_cargo_manifests(ROOT)

        assert Path("core/runner/headless/Cargo.toml") in manifests
        assert Path("core/reporting/protected_content_linter/Cargo.toml") in manifests
        assert all("target" not in manifest.parts for manifest in manifests)


    def test_skeleton_plan_uses_local_commands_only():
        release = load_module()
        steps = release.build_plan("skeleton", ROOT)
        commands = [" ".join(step.command) for step in steps]

        assert any(
            "validate_dependencies_schema.py execution/_DAG/DAG-006/DependencyEdges.csv"
            in command
            for command in commands
        )
        assert any("test_release_readiness_script.py" in command for command in commands)
        assert all(isinstance(step.command, tuple) for step in steps)


    def test_python_profiles_use_coordination_maintenance_test():
        release = load_module()
        expected = (
            "-m",
            "pytest",
            "-q",
            "tests/test_coordination_maintenance.py",
        )
        old_target = "tools/coordination"

        for profile in ("python", "all"):
            commands = [step.command for step in release.build_plan(profile, ROOT)]

            assert any(command[1:] == expected for command in commands)
            assert all(old_target not in part for command in commands for part in command)


    def test_all_profile_preserves_current_command_surface():
        release = load_module()
        commands = [" ".join(step.command) for step in release.build_plan("all", ROOT)]

        assert any(
            "validate_dependencies_schema.py execution/_DAG/DAG-006/DependencyEdges.csv"
            in command
            for command in commands
        )
        assert any("test_release_readiness_script.py" in command for command in commands)
        assert any(" -m pytest -q tests" in command for command in commands)
        assert any("test_coordination_maintenance.py" in command for command in commands)
        assert any("tests/security" in command for command in commands)
        assert any(
            command == "cargo test --manifest-path core/runner/headless/Cargo.toml"
            for command in commands
        )


    def test_main_dry_run_prints_plan_without_executing(monkeypatch, capsys):
        release = load_module()

        def fail_run_steps(*args, **kwargs):
            raise AssertionError("dry-run must not execute planned checks")

        monkeypatch.setattr(release, "run_steps", fail_run_steps)

        result = release.main(["--profile", "skeleton", "--repo-root", str(ROOT)])
        captured = capsys.readouterr()

        assert result == 0
        assert "OpenPipeStress release readiness profile (dry-run)" in captured.out
        assert "execution/_DAG/DAG-006/DependencyEdges.csv" in captured.out
        assert "planned checks: 2" in captured.out
        assert "running:" not in captured.out


    def test_main_execute_runs_planned_steps(monkeypatch, capsys):
        release = load_module()
        executed: list[str] = []

        def fake_run_steps(steps, root):
            executed.extend(step.name for step in steps)
            assert root == ROOT
            return 0

        monkeypatch.setattr(release, "run_steps", fake_run_steps)

        result = release.main(
            ["--profile", "skeleton", "--execute", "--repo-root", str(ROOT)]
        )
        captured = capsys.readouterr()

        assert result == 0
        assert "OpenPipeStress release readiness profile (execute)" in captured.out
        assert executed == ["dag dependency schema", "release readiness script tests"]

## Component: tests/test_report_generator_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the calculation report generator schema and fixture."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "report_generator.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "reports" / "invented" / "calculation_report_fixture.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "report_generator_status",
        "calculation_report",
    }

    REQUIRED_DEFS = {
        "AnalysisStatus",
        "CalculationReport",
        "Checksum",
        "Diagnostic",
        "DimensionId",
        "LoadCaseSummary",
        "ModelInputSummary",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "Reference",
        "ReferencedEnvelope",
        "RenderedSection",
        "ReportGeneratorStatus",
        "RulePackRef",
        "TemplateSlot",
        "UnresolvedTbd",
    }

    REQUIRED_SECTION_KINDS = {
        "model_input_summary",
        "load_cases",
        "results",
        "warnings_assumptions_provenance",
        "audit_manifest",
        "rule_pack_references",
        "limitations",
        "professional_boundary_notice",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    FORBIDDEN_RUNTIME_COMMITMENTS = {
        "gui_presentation",
        "cli_runtime",
        "api_transport",
        "adapter_behavior",
        "protected_content_linter",
        "private_redaction_export_controls",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as json_file:
            return json.load(json_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-08-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-08"
        assert schema["properties"]["scope_item"]["const"] == "SOW-024"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-007"

        generator_status = defs["ReportGeneratorStatus"]["properties"]
        assert generator_status["baseline_renderer"]["const"] == (
            "deterministic_in_memory_report_assembly"
        )
        assert generator_status["template_slot_contract"]["const"] == (
            "schema_first_template_slots"
        )
        assert generator_status["neutral_test_output"]["const"] == (
            "structured_text_sections"
        )
        for field in FORBIDDEN_RUNTIME_COMMITMENTS:
            assert generator_status[field]["const"] == "TBD"

        report_required = required_at(schema, "CalculationReport")
        assert {
            "model_input_summary",
            "load_case_summary",
            "result_export_refs",
            "audit_manifest_refs",
            "report_section_refs",
            "rule_pack_refs",
            "diagnostics",
            "template_slots",
            "rendered_sections",
            "analysis_status",
            "professional_boundary",
            "provenance",
            "privacy_classification",
            "unresolved_runtime_tbds",
        } <= report_required
        assert (
            defs["CalculationReport"]["properties"]["analysis_status"]["contains"][
                "const"
            ]
            == "HUMAN_REVIEW_REQUIRED"
        )

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)

        model_required = required_at(schema, "ModelInputSummary")
        assert {
            "project_ref",
            "model_ref",
            "persistence_ref",
            "unit_system_ref",
            "model_hash",
            "input_manifest_ref",
            "provenance",
        } <= model_required

        referenced_required = required_at(schema, "ReferencedEnvelope")
        assert {
            "ref",
            "schema_ref",
            "checksum",
            "privacy_classification",
            "provenance",
        } <= referenced_required

        slot_required = required_at(schema, "TemplateSlot")
        assert {
            "slot_id",
            "required",
            "section_kind",
            "source_contract",
            "ordering_index",
        } <= slot_required
        slot_kinds = set(defs["TemplateSlot"]["properties"]["section_kind"]["enum"])
        rendered_kinds = set(defs["RenderedSection"]["properties"]["section_kind"]["enum"])
        assert REQUIRED_SECTION_KINDS <= slot_kinds
        assert REQUIRED_SECTION_KINDS <= rendered_kinds

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert {"REPORT_BLOCKING", "TEMPLATE_BLOCKING"} <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        rule_pack_required = required_at(schema, "RulePackRef")
        assert {
            "rule_pack_id",
            "version",
            "checksum",
            "source_notice",
            "redistribution_status",
            "completeness_status",
            "private_payload_redacted",
        } <= rule_pack_required
        assert defs["RulePackRef"]["properties"]["private_payload_redacted"]["const"] is True

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False

        tbd_topics = set(defs["UnresolvedTbd"]["properties"]["topic"]["enum"])
        assert {
            "gui_presentation",
            "cli_runtime",
            "api_transport",
            "adapter_behavior",
            "redaction_export_controls",
            "protected_content_linter",
            "release_template_integration",
            "final_report_styling_layout_policy",
        } <= tbd_topics
        assert defs["UnresolvedTbd"]["properties"]["review_needed"]["const"] is True

        assert fixture["deliverable_id"] == "DEL-08-01"
        report = fixture["calculation_report"]
        slot_order = [slot["ordering_index"] for slot in report["template_slots"]]
        assert slot_order == sorted(slot_order)
        assert REQUIRED_SECTION_KINDS <= {
            section["section_kind"] for section in report["rendered_sections"]
        }
        assert "HUMAN_REVIEW_REQUIRED" in report["analysis_status"]
        assert report["professional_boundary"]["software_makes_compliance_claim"] is False
        assert report["rule_pack_refs"][0]["private_payload_redacted"] is True
        assert report["privacy_classification"] == "invented_public_example"
        assert any(
            tbd["topic"] == "redaction_export_controls"
            for tbd in report["unresolved_runtime_tbds"]
        )


    if __name__ == "__main__":
        main()

## Component: tests/test_report_protected_content_linter.py

    #!/usr/bin/env python3
    """Stdlib checks for the report protected-content linter schema and fixtures."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "report_protected_content_linter.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "report_lint" / "invented" / "lint_run_fixture.json"
    RISK_FIXTURE_PATH = (
        ROOT / "fixtures" / "report_lint" / "invented" / "synthetic_risk_template.txt"
    )
    SAFE_FIXTURE_PATH = (
        ROOT / "fixtures" / "report_lint" / "invented" / "safe_metadata_template.txt"
    )

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "linter_status",
        "lint_run",
    }

    REQUIRED_DEFS = {
        "FindingClass",
        "FindingCode",
        "FindingSeverity",
        "LintConfiguration",
        "LintFinding",
        "LintRun",
        "LintSummary",
        "LintTarget",
        "LinterStatus",
        "PrivacyClassification",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ReviewRoute",
        "ReviewStatus",
        "SourceLocation",
        "SurfaceKind",
    }

    REQUIRED_CODES = {
        "PROTECTED_CONTENT_SYNTHETIC_MARKER",
        "PRIVATE_DATA_SYNTHETIC_MARKER",
        "PROPRIETARY_SOURCE_SYNTHETIC_MARKER",
        "UNKNOWN_PROVENANCE_REVIEW_REQUIRED",
        "PROHIBITED_PROFESSIONAL_CLAIM",
        "SAFE_METADATA_ALLOWED",
    }

    REQUIRED_CLASSES = {
        "IP_BOUNDARY_WARNING",
        "PRIVATE_DATA_WARNING",
        "PROVENANCE_WARNING",
        "PROFESSIONAL_BOUNDARY_WARNING",
        "SAFE_METADATA",
    }

    FORBIDDEN_STATUS_TRUTH = {
        "legal_clearance",
        "security_sufficiency",
        "professional_approval",
    }

    FORBIDDEN_FIXTURE_TERMS = {
        "ASME",
        "B31",
        "B31J",
        "allowable stress table",
        "stress intensification factor table",
        "vendor catalog value",
        "real secret",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as json_file:
            return json.load(json_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-08-05"
        assert schema["properties"]["package_id"]["const"] == "PKG-08"
        assert schema["properties"]["scope_item"]["const"] == "SOW-043"
        assert {"OBJ-002", "OBJ-007"} >= set(
            schema["properties"]["objectives"]["items"]["enum"]
        )

        linter_status = defs["LinterStatus"]["properties"]
        assert linter_status["baseline_linter"]["const"] == (
            "deterministic_public_surface_heuristic_linter"
        )
        assert linter_status["fixture_policy"]["const"] == "invented_synthetic_markers_only"
        assert linter_status["heuristic_only"]["const"] is True
        for field in FORBIDDEN_STATUS_TRUTH:
            assert linter_status[field]["const"] is False
        assert linter_status["ci_release_policy"]["const"] == "TBD"
        assert linter_status["redaction_export_controls"]["const"] == "TBD"
        assert (
            linter_status["educational_example_dependency"]["const"]
            == "DAG-001-E0621_RETAINED_CANDIDATE_NON_GATING"
        )

        config_required = required_at(schema, "LintConfiguration")
        assert {
            "public_surface_roots",
            "private_surface_default",
            "finding_order",
            "synthetic_marker_policy",
            "clean_scan_disclaimer",
            "candidate_edge_policy",
        } <= config_required
        assert (
            defs["LintConfiguration"]["properties"]["private_surface_default"]["const"]
            == "skip_unless_explicitly_authorized"
        )
        assert (
            defs["LintConfiguration"]["properties"]["candidate_edge_policy"]["const"]
            == "DAG-001-E0621_non_gating_no_DEL-11-04_dependency"
        )

        finding_required = required_at(schema, "LintFinding")
        assert {
            "finding_id",
            "code",
            "class",
            "severity",
            "target_ref",
            "source_location",
            "matched_policy",
            "excerpt",
            "message",
            "remediation",
            "review_route",
            "disposition",
            "provenance",
        } <= finding_required
        assert REQUIRED_CODES <= enum_at(schema, "FindingCode")
        assert REQUIRED_CLASSES <= enum_at(schema, "FindingClass")
        assert {"INFO", "WARNING", "BLOCKING"} <= enum_at(schema, "FindingSeverity")
        assert {
            "public_report_template",
            "public_report_example",
            "public_fixture",
            "private_user_template",
            "private_project_export",
        } <= enum_at(schema, "SurfaceKind")

        summary_required = required_at(schema, "LintSummary")
        assert {
            "target_count",
            "scanned_target_count",
            "skipped_private_target_count",
            "finding_count",
            "blocking_finding_count",
            "clean_scan_is_clearance",
        } <= summary_required
        assert (
            defs["LintSummary"]["properties"]["clean_scan_is_clearance"]["const"] is False
        )

        assert fixture["deliverable_id"] == "DEL-08-05"
        assert fixture["linter_status"]["heuristic_only"] is True
        assert fixture["linter_status"]["legal_clearance"] is False
        assert fixture["linter_status"]["professional_approval"] is False
        assert fixture["lint_run"]["configuration"]["private_surface_default"] == (
            "skip_unless_explicitly_authorized"
        )
        assert fixture["lint_run"]["configuration"]["candidate_edge_policy"] == (
            "DAG-001-E0621_non_gating_no_DEL-11-04_dependency"
        )

        findings = fixture["lint_run"]["findings"]
        assert [finding["finding_id"] for finding in findings] == sorted(
            finding["finding_id"] for finding in findings
        )
        assert {finding["code"] for finding in findings} == {
            "PROTECTED_CONTENT_SYNTHETIC_MARKER",
            "PROHIBITED_PROFESSIONAL_CLAIM",
        }
        assert all(finding["severity"] == "BLOCKING" for finding in findings)
        assert fixture["lint_run"]["summary"]["blocking_finding_count"] == 2
        assert fixture["lint_run"]["summary"]["clean_scan_is_clearance"] is False

        risk_fixture = RISK_FIXTURE_PATH.read_text(encoding="utf-8")
        safe_fixture = SAFE_FIXTURE_PATH.read_text(encoding="utf-8")
        assert "OPS_SYNTHETIC_PROTECTED_TABLE" in risk_fixture
        assert "human review required" in safe_fixture
        for forbidden in FORBIDDEN_FIXTURE_TERMS:
            assert forbidden not in risk_fixture
            assert forbidden not in safe_fixture

        serialized = json.dumps(schema) + json.dumps(fixture)
        assert "DEL-11-04_Invented educational example models" not in serialized
        assert "examples/models/invented" not in serialized


    if __name__ == "__main__":
        main()

## Component: tests/test_report_sections_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the report sections schema."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "report_sections.schema.yaml"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "report_renderer_status",
        "report_sections",
    }

    REQUIRED_DEFS = {
        "AnalysisStatus",
        "AnalysisStatusDisclosure",
        "Assumption",
        "Diagnostic",
        "DimensionId",
        "Limitation",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "Reference",
        "ReportEffect",
        "ReportRendererStatus",
        "ReportSectionEnvelope",
        "UnresolvedTbd",
        "UserSuppliedValue",
        "ValueQuantity",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "REPORT_BLOCKING",
    }

    REQUIRED_DISCLOSURE_CATEGORIES = {
        "diagnostics",
        "analysis_status_disclosures",
        "provenance_notes",
        "user_supplied_values",
        "assumptions",
        "limitations",
        "unresolved_tbds",
        "professional_boundary",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-08-03"
        assert schema["properties"]["package_id"]["const"] == "PKG-08"
        assert schema["properties"]["scope_item"]["const"] == "SOW-024"
        assert {"OBJ-007", "OBJ-011"} <= set(
            schema["properties"]["objectives"]["items"]["enum"]
        )

        renderer = defs["ReportRendererStatus"]["properties"]
        assert renderer["report_section_contract"]["const"] == (
            "schema_first_report_section_records"
        )
        assert renderer["full_report_renderer"]["const"] == "TBD"
        assert renderer["final_template_layout"]["const"] == "TBD"
        assert renderer["gui_presentation"]["const"] == "TBD"
        assert renderer["cli_runtime"]["const"] == "TBD"
        assert renderer["api_transport"]["const"] == "TBD"
        assert renderer["adapter_behavior"]["const"] == "TBD"
        assert renderer["private_redaction_export_controls"]["const"] == "TBD"

        section_required = required_at(schema, "ReportSectionEnvelope")
        assert REQUIRED_DISCLOSURE_CATEGORIES <= section_required
        assert {
            "report_section_id",
            "model_ref",
            "run_ref",
        } <= section_required
        assert (
            defs["ReportSectionEnvelope"]["properties"]["analysis_status_disclosures"][
                "contains"
            ]["properties"]["status"]["const"]
            == "HUMAN_REVIEW_REQUIRED"
        )

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        provenance_required = required_at(schema, "Provenance")
        assert {
            "source_name",
            "source_location",
            "source_license",
            "contributor",
            "contributor_certification",
            "redistribution_status",
            "review_status",
            "privacy_classification",
        } <= provenance_required
        assert {
            "public_metadata",
            "invented_public_example",
            "private_project_data",
            "private_rule_pack_data",
            "protected_suspected",
            "redacted",
        } <= enum_at(schema, "PrivacyClassification")

        user_value_required = required_at(schema, "UserSuppliedValue")
        assert {
            "value_id",
            "value_category",
            "source",
            "provenance",
            "privacy_classification",
            "required_for",
            "review_status",
            "missing_data_finding",
        } <= user_value_required
        assert {
            "mechanics_solve",
            "user_rule_check",
            "reporting",
            "human_review",
        } <= set(
            defs["UserSuppliedValue"]["properties"]["required_for"]["items"]["enum"]
        )

        quantity_required = required_at(schema, "ValueQuantity")
        assert {"magnitude", "unit", "dimension"} <= quantity_required
        assert {
            "dimensionless",
            "length",
            "force",
            "moment",
            "stress",
            "ratio",
            "TBD",
        } <= enum_at(schema, "DimensionId")

        assumption_required = required_at(schema, "Assumption")
        assert {
            "assumption_id",
            "owner",
            "source",
            "affected_scope",
            "statement",
            "review_status",
            "effect",
            "provenance",
        } <= assumption_required
        limitation_required = required_at(schema, "Limitation")
        assert {
            "limitation_id",
            "source",
            "affected_scope",
            "statement",
            "effect",
            "provenance",
        } <= limitation_required

        effect_required = required_at(schema, "ReportEffect")
        assert {
            "mechanics_solve",
            "user_rule_check",
            "report_completeness",
            "human_review",
        } <= effect_required

        tbd_required = required_at(schema, "UnresolvedTbd")
        assert {"tbd_id", "affected_scope", "description", "review_needed"} <= tbd_required
        assert defs["UnresolvedTbd"]["properties"]["review_needed"]["const"] is True

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False


    if __name__ == "__main__":
        main()

## Component: tests/test_results_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the result export schema."""

    import json
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )

    SCHEMA_PATH = ROOT / "schemas" / "results.schema.yaml"
    PRODUCT_PREVIEW_RESULT_PATH = (
        ROOT / "fixtures" / "product_preview" / "invented_mechanics_result.json"
    )
    TP_PHYS_015_RESULT_ENVELOPE_PATH = (
        ROOT
        / "fixtures"
        / "results"
        / "invented"
        / "tp_phys_015_canonical_solve_result_envelope.json"
    )
    TP_PHYS_015_SECTION_EVIDENCE_ENVELOPE_PATH = (
        ROOT
        / "fixtures"
        / "results"
        / "invented"
        / "tp_phys_015_section_property_stress_evidence_envelope.json"
    )

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "export_format_status",
        "result_envelope",
    }

    REQUIRED_DEFS = {
        "AnalysisStatus",
        "Checksum",
        "Diagnostic",
        "DimensionId",
        "DownstreamUse",
        "ExportFormatStatus",
        "ProfessionalBoundary",
        "Provenance",
        "QuantityResult",
        "Reference",
        "Reproducibility",
        "ResultEnvelope",
        "ResultFamily",
        "ResultMetadata",
        "ResultSet",
        "ResultSetType",
        "ResultTraceLink",
        "RulePackRef",
        "SolverVersion",
    }

    REQUIRED_FAMILIES = {
        "displacement",
        "rotation",
        "force",
        "moment",
        "reaction",
        "stress",
        "section_property",
        "ratio",
        "rule_check",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "EXPORT_BLOCKING",
    }

    FORBIDDEN_STATUS = {
        "HUMAN_APPROVED_FOR_PROJECT",
        "CODE_COMPLIANT",
        "CERTIFIED",
        "SEALED",
        "APPROVED",
    }

    FORBIDDEN_FORMAT_COMMITMENTS = {
        "csv",
        "spreadsheet",
        "hdf5",
        "local_fea",
        "openapi_transport",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_product_preview_result():
        with PRODUCT_PREVIEW_RESULT_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def load_tp_phys_015_result_envelope():
        with TP_PHYS_015_RESULT_ENVELOPE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def load_tp_phys_015_section_evidence_envelope():
        with TP_PHYS_015_SECTION_EVIDENCE_ENVELOPE_PATH.open(
            encoding="utf-8"
        ) as fixture_file:
            return json.load(fixture_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-08-04"
        assert schema["properties"]["package_id"]["const"] == "PKG-08"
        assert schema["properties"]["scope_item"]["const"] == "SOW-046"
        assert {"OBJ-007", "OBJ-009"} <= set(
            schema["properties"]["objectives"]["items"]["enum"]
        )

        export_status = defs["ExportFormatStatus"]["properties"]
        assert export_status["baseline_format"]["const"] == (
            "schema_first_json_result_envelope"
        )
        assert export_status["additional_formats"]["const"] == "TBD"
        assert export_status["public_transport_protocol"]["const"] == "TBD"
        assert export_status["local_fea_package_format"]["const"] == "TBD"
        assert export_status["external_adapter_formats"]["const"] == "TBD"
        for name in FORBIDDEN_FORMAT_COMMITMENTS:
            assert name not in {
                export_status["additional_formats"]["const"].lower(),
                export_status["public_transport_protocol"]["const"].lower(),
                export_status["local_fea_package_format"]["const"].lower(),
                export_status["external_adapter_formats"]["const"].lower(),
            }

        envelope_required = required_at(schema, "ResultEnvelope")
        assert {
            "schema_version",
            "envelope_id",
            "model_ref",
            "run_ref",
            "solver_version",
            "unit_system_ref",
            "load_basis_refs",
            "result_sets",
            "diagnostics",
            "provenance",
            "reproducibility",
            "analysis_status",
            "professional_boundary",
            "downstream_use",
        } <= envelope_required

        status = enum_at(schema, "AnalysisStatus")
        assert {
            "MODEL_INCOMPLETE",
            "MECHANICS_SOLVED",
            "RULE_INPUTS_INCOMPLETE",
            "USER_RULE_CHECKED",
            "USER_RULE_FAILED",
            "HUMAN_REVIEW_REQUIRED",
        } <= status
        assert status.isdisjoint(FORBIDDEN_STATUS)
        assert (
            defs["ResultEnvelope"]["properties"]["analysis_status"]["contains"]["const"]
            == "HUMAN_REVIEW_REQUIRED"
        )

        quantity_required = required_at(schema, "QuantityResult")
        assert {
            "result_id",
            "family",
            "object_ref",
            "basis_ref",
            "magnitude",
            "unit",
            "dimension",
            "provenance",
        } <= quantity_required
        assert "metadata" not in quantity_required
        assert (
            defs["QuantityResult"]["properties"]["metadata"]["$ref"]
            == "#/$defs/ResultMetadata"
        )
        assert (
            defs["QuantityResult"]["properties"]["trace_chain"]["items"]["$ref"]
            == "#/$defs/ResultTraceLink"
        )
        assert {
            "trace_id",
            "trace_type",
            "source_ref",
            "target_ref",
            "provenance",
        } <= required_at(schema, "ResultTraceLink")
        assert {
            "physical_source_to_analytical_model",
            "analytical_model_to_adapter_dto",
            "adapter_dto_to_solver_input",
            "solver_input_to_result_value",
            "section_property_evidence_to_result_value",
            "source_trace_link_reference",
            "TBD",
        } <= set(defs["ResultTraceLink"]["properties"]["trace_type"]["enum"])
        assert {
            "component",
            "coordinate_system",
            "location",
            "basis",
            "sign_convention",
        } <= required_at(schema, "ResultMetadata")
        metadata = defs["ResultMetadata"]["properties"]
        assert {
            "axial_force",
            "shear_force_y",
            "shear_force_z",
            "torsional_moment",
            "bending_moment_y",
            "bending_moment_z",
            "nodal_force_x",
            "nodal_force_y",
            "nodal_force_z",
            "nodal_moment_x",
            "nodal_moment_y",
            "nodal_moment_z",
            "axial_normal_stress",
            "bending_normal_stress_y",
            "bending_normal_stress_z",
            "torsional_shear_stress",
            "pressure_hoop_stress",
            "pressure_longitudinal_stress",
            "section_area",
            "section_modulus_y",
            "section_modulus_z",
            "torsion_constant",
            "torsion_radius",
        } <= set(metadata["component"]["enum"])
        assert {"element_local", "pipe_section"} <= set(metadata["coordinate_system"]["enum"])
        assert {"end_i", "end_j", "node", "quarter_1", "midspan", "quarter_3"} <= set(
            metadata["location"]["enum"]
        )
        assert (
            "recovered_from_local_element_stiffness"
            in set(metadata["basis"]["enum"])
        )
        assert (
            "recovered_from_open_mechanics_stress_components"
            in set(metadata["basis"]["enum"])
        )
        assert "assembled_solver_load_vector" in set(metadata["basis"]["enum"])
        assert "interpolated_from_endpoint_resultants" in set(metadata["basis"]["enum"])
        assert "derived_from_user_entered_section_geometry" in set(
            metadata["basis"]["enum"]
        )
        assert "explicit_user_linear_combination" in set(metadata["basis"]["enum"])
        quantity_condition = defs["QuantityResult"]["allOf"][0]
        assert set(quantity_condition["if"]["properties"]["family"]["enum"]) == {
            "force",
            "moment",
            "section_property",
        }
        assert "metadata" in quantity_condition["then"]["required"]
        assert {"area", "section_modulus", "second_moment_area"} <= enum_at(
            schema, "DimensionId"
        )
        assert REQUIRED_FAMILIES <= enum_at(schema, "ResultFamily")
        assert {
            "mechanics",
            "stress_recovery",
            "load_vector_evidence",
            "station_resultants",
            "section_property_evidence",
            "user_rule_check",
            "diagnostic_only",
        } <= enum_at(schema, "ResultSetType")
        assert (
            defs["ResultSet"]["properties"]["set_type"]["$ref"]
            == "#/$defs/ResultSetType"
        )

        preview_result = load_product_preview_result()
        axial_force = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:force:pipe-P-120:axial"
        )
        axial_force_end_j = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:force:pipe-P-120:axial:end-j"
        )
        axial_force_midspan = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:force:pipe-P-120:midspan:axial"
        )
        shear_force_end_i = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:force:pipe-P-120:shear-y"
        )
        shear_force_quarter = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:force:pipe-P-120:quarter-1:shear-z"
        )
        axial_metadata = axial_force["metadata"]
        axial_end_j_metadata = axial_force_end_j["metadata"]
        axial_midspan_metadata = axial_force_midspan["metadata"]
        torsional_stress_end_j = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:stress:pipe-P-120:end-j:torsional-shear"
        )
        torsional_stress_midspan = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:stress:pipe-P-120:midspan:torsional-shear"
        )
        combination_axial_force = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:combination:combination-C-OPER-ALT:force:pipe-P-120:axial"
        )
        pressure_hoop = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:stress:pipe-P-120:end-i:pressure-hoop"
        )
        stress_summary = next(
            result
            for result in preview_result["results"]
            if result["id"] == "result:stress:pipe-P-120"
        )
        assert axial_force["unit"] == "N"
        assert axial_force["basis_ref"] == {"ref_type": "load_case", "ref_id": "load:L-100"}
        assert axial_metadata["component"] in metadata["component"]["enum"]
        assert axial_metadata["coordinate_system"] in metadata["coordinate_system"]["enum"]
        assert axial_metadata["location"] in metadata["location"]["enum"]
        assert axial_metadata["basis"] in metadata["basis"]["enum"]
        assert axial_metadata["sign_convention"]
        assert axial_force_end_j["unit"] == "N"
        assert axial_end_j_metadata["component"] == "axial_force"
        assert axial_end_j_metadata["coordinate_system"] == "element_local"
        assert axial_end_j_metadata["location"] == "end_j"
        assert axial_end_j_metadata["basis"] in metadata["basis"]["enum"]
        assert "j-end" in axial_end_j_metadata["sign_convention"]
        assert axial_force_midspan["unit"] == "N"
        assert axial_midspan_metadata["component"] == "axial_force"
        assert axial_midspan_metadata["coordinate_system"] == "element_local"
        assert axial_midspan_metadata["location"] == "midspan"
        assert axial_midspan_metadata["basis"] == "interpolated_from_endpoint_resultants"
        assert shear_force_end_i["unit"] == "N"
        assert shear_force_end_i["metadata"]["component"] == "shear_force_y"
        assert shear_force_end_i["metadata"]["location"] == "end_i"
        assert shear_force_end_i["metadata"]["basis"] == "recovered_from_local_element_stiffness"
        assert shear_force_quarter["unit"] == "N"
        assert shear_force_quarter["metadata"]["component"] == "shear_force_z"
        assert shear_force_quarter["metadata"]["location"] == "quarter_1"
        assert shear_force_quarter["metadata"]["basis"] == "interpolated_from_endpoint_resultants"
        assert stress_summary["kind"] == "open_formula_stress_summary"
        assert "metadata" not in stress_summary
        assert torsional_stress_end_j["unit"] == "MPa"
        assert torsional_stress_end_j["metadata"]["component"] == "torsional_shear_stress"
        assert torsional_stress_end_j["metadata"]["coordinate_system"] == "element_local"
        assert torsional_stress_end_j["metadata"]["location"] == "end_j"
        assert (
            torsional_stress_end_j["metadata"]["basis"]
            == "recovered_from_open_mechanics_stress_components"
        )
        assert torsional_stress_midspan["unit"] == "MPa"
        assert torsional_stress_midspan["metadata"]["component"] == "torsional_shear_stress"
        assert torsional_stress_midspan["metadata"]["coordinate_system"] == "element_local"
        assert torsional_stress_midspan["metadata"]["location"] == "midspan"
        assert (
            torsional_stress_midspan["metadata"]["basis"]
            == "interpolated_from_endpoint_resultants"
        )
        assert pressure_hoop["unit"] == "MPa"
        assert pressure_hoop["metadata"]["component"] == "pressure_hoop_stress"
        assert pressure_hoop["metadata"]["coordinate_system"] == "pipe_section"
        assert combination_axial_force["unit"] == "N"
        assert combination_axial_force["basis_ref"] == {
            "ref_type": "combination",
            "ref_id": "combination:C-OPER-ALT",
        }
        assert combination_axial_force["source_result_refs"] == [
            "result:force:pipe-P-120:axial",
            "result:loadcase:load-L-200:force:pipe-P-120:axial",
        ]
        assert combination_axial_force["metadata"]["basis"] == "explicit_user_linear_combination"
        assert combination_axial_force["metadata"]["basis"] in metadata["basis"]["enum"]

        tp_phys_015_result = load_tp_phys_015_result_envelope()
        result_envelope = tp_phys_015_result["result_envelope"]
        assert (
            result_envelope["envelope_id"]
            == "MECH-TP-PHYS-015-CANONICAL-SOLVE-RESULT-ENVELOPE"
        )
        assert result_envelope["solver_version"]["solver_name"] == (
            "open_pipe_stress_validation_mechanics_benchmark"
        )
        assert "HUMAN_REVIEW_REQUIRED" in result_envelope["analysis_status"]
        result_sets = {
            result_set["set_type"]: result_set
            for result_set in result_envelope["result_sets"]
        }
        assert {"mechanics", "load_vector_evidence", "station_resultants"} <= set(
            result_sets
        )
        load_vector_value = result_sets["load_vector_evidence"]["values"][0]
        assert load_vector_value["metadata"]["component"] == "nodal_force_y"
        assert load_vector_value["metadata"]["basis"] == "assembled_solver_load_vector"
        assert load_vector_value["diagnostics"][0]["code"] == (
            "TP_RESULT_017_VALUE_TRACE_NOTE"
        )
        assert load_vector_value["trace_chain"][0]["trace_type"] == (
            "solver_input_to_result_value"
        )
        assert load_vector_value["trace_chain"][0]["source_ref"] == {
            "ref_type": "adapter_dto",
            "ref_id": "dto:load_application:LC-TP-PHYS-014:0",
        }
        assert load_vector_value["trace_chain"][0]["target_ref"] == {
            "ref_type": "result_value",
            "ref_id": "result:load-vector:node-N-1:uy",
        }
        station_value = result_sets["station_resultants"]["values"][0]
        assert station_value["station_ref"] == {
            "ref_type": "result_station",
            "ref_id": "E-1:midspan",
        }
        assert station_value["metadata"]["component"] == "bending_moment_z"

        section_result = load_tp_phys_015_section_evidence_envelope()["result_envelope"]
        section_result_sets = {
            result_set["set_type"]: result_set
            for result_set in section_result["result_sets"]
        }
        assert {"section_property_evidence", "stress_recovery"} <= set(
            section_result_sets
        )
        section_values = section_result_sets["section_property_evidence"]["values"]
        section_by_id = {value["result_id"]: value for value in section_values}
        assert (
            section_by_id["result:section-property:tp-stress-016:section-modulus-z"][
                "dimension"
            ]
            == "section_modulus"
        )
        assert (
            section_by_id["result:section-property:tp-stress-016:torsion-constant"][
                "dimension"
            ]
            == "second_moment_area"
        )
        for value in section_values:
            assert value["family"] == "section_property"
            assert value["object_ref"] == {
                "ref_type": "section_property_evidence",
                "ref_id": "SECTION-PROP-TP-STRESS-016-INVENTED-PIPE-OD2-WALL0P25",
            }
            assert value["metadata"]["basis"] == "derived_from_user_entered_section_geometry"
        stress_value = section_result_sets["stress_recovery"]["values"][0]
        assert stress_value["trace_chain"][0]["trace_type"] == (
            "section_property_evidence_to_result_value"
        )
        assert stress_value["trace_chain"][0]["source_ref"] == {
            "ref_type": "section_property_evidence",
            "ref_id": "SECTION-PROP-TP-STRESS-016-INVENTED-PIPE-OD2-WALL0P25",
        }

        diagnostic_required = required_at(schema, "Diagnostic")
        assert {
            "code",
            "class",
            "severity",
            "source",
            "affected_object",
            "message",
            "remediation",
            "provenance",
        } <= diagnostic_required
        assert REQUIRED_DIAGNOSTIC_CLASSES <= set(
            defs["Diagnostic"]["properties"]["class"]["enum"]
        )

        rule_pack_required = required_at(schema, "RulePackRef")
        assert {
            "rule_pack_id",
            "version",
            "checksum",
            "source_notice",
            "redistribution_status",
            "completeness_status",
            "private_payload_redacted",
        } <= rule_pack_required
        assert defs["RulePackRef"]["properties"]["private_payload_redacted"]["const"] is True

        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        assert boundary["software_makes_compliance_claim"]["const"] is False
        assert boundary["software_makes_certification_claim"]["const"] is False
        assert boundary["software_makes_sealing_claim"]["const"] is False
        assert boundary["software_makes_approval_claim"]["const"] is False
        assert boundary["software_makes_authentication_claim"]["const"] is False

        downstream = defs["DownstreamUse"]["properties"]
        assert downstream["review"]["const"] is True
        assert downstream["regression_comparison"]["const"] is True
        assert downstream["report_consumption"]["const"] is True
        assert downstream["headless_automation"]["const"] is True
        assert downstream["governed_downstream_tooling"]["const"] is True
        assert downstream["additional_export_formats"]["const"] == "TBD"


    def check_jsonschema_validation():
        schema = load_schema()
        fixture = load_tp_phys_015_result_envelope()
        section_fixture = load_tp_phys_015_section_evidence_envelope()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(TP_PHYS_015_RESULT_ENVELOPE_PATH),
            )
            assert validate_instance(
                schema,
                section_fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(TP_PHYS_015_SECTION_EVIDENCE_ENVELOPE_PATH),
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_results_schema_contract():
        main()


    def test_results_schema_jsonschema_validation_helper():
        check_jsonschema_validation()


    if __name__ == "__main__":
        main()
        check_jsonschema_validation()

## Component: tests/test_results_viewer_contract.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-05 results viewer contracts."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.results_viewer import build_results_viewer_contract, canonical_json  # noqa: E402


    def main():
        record = build_results_viewer_contract(
            result_set_id="invented-results",
            result_items=[
                {
                    "result_id": "disp-node-1",
                    "result_kind": "displacement",
                    "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                    "hashes": [
                        {
                            "algorithm": "sha256",
                            "canonicalization": "JCS",
                            "payload_ref": {"ref_type": "ResultEnvelope", "ref_id": "results:invented"},
                            "value": "sha256:invented-result",
                        }
                    ],
                    "provenance_refs": [{"ref_type": "AnalysisRun", "ref_id": "run:invented"}],
                    "values": [
                        {
                            "value_id": "ux",
                            "component": "UX",
                            "numeric_value": 1.2,
                            "unit": "mm",
                            "dimension": "displacement",
                            "location_ref": {"ref_type": "node", "ref_id": "N1"},
                        }
                    ],
                    "overlay_enabled": True,
                    "overlay_target_ref": {"ref_type": "node", "ref_id": "N1"},
                },
                {
                    "result_id": "stress-tbd",
                    "result_kind": "stress",
                    "values": [{"value_id": "smax", "numeric_value": "TBD", "unit": "MPa", "dimension": "stress"}],
                },
            ],
        )
        assert record["deliverable_id"] == "DEL-07-05"
        assert record["solver_execution"] == "not_performed"
        assert record["views"][0]["availability"] == "available"
        assert record["views"][1]["availability"] == "unresolved_TBD"
        assert record["views"][0]["analysis_status"] == ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"]
        assert record["views"][0]["hash_boundary"]["hashes_present"] is True
        assert record["unit_contract"]["contract_ref"] == "DEL-02-02"
        assert record["views"][0]["table_columns"] == [
            "component",
            "dimension",
            "location_ref",
            "numeric_value",
            "unit",
            "value_id",
        ]
        assert any(item["code"] == "RESULT_VALUE_OR_UNIT_UNRESOLVED" for item in record["diagnostics"])
        assert record["software_makes_professional_acceptance_claim"] is False
        assert "code compliant" not in canonical_json(record).lower()


    def test_results_viewer_contract_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_review_geometry_export_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-08 glTF review geometry export packages."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.review_geometry import (  # noqa: E402
        build_review_geometry_export_package,
        canonical_json,
        render_review_geometry_gltf,
        write_review_geometry_export_package,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "review_geometry_export.schema.json"
    PACKAGE_FIXTURE_PATH = ROOT / "fixtures" / "review_geometry" / "invented" / "review_geometry_export_package.json"
    GLTF_FIXTURE_PATH = ROOT / "fixtures" / "review_geometry" / "invented" / "model.gltf"
    SOURCE_PAYLOAD_PATH = ROOT / "fixtures" / "review_geometry" / "invented" / "source_centerline_payload.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def source_payload() -> dict[str, object]:
        return {
            "export_id": "review-geometry:invented-del-17-08",
            "source_model_ref": ref("Model", "model:invented-review-geometry"),
            "source_model_hash": {
                "algorithm": "sha256",
                "canonicalization": "JCS_compatible_json_payload_hash",
                "payload_ref": ref("Model", "model:invented-review-geometry"),
                "payload_scope": "source_model_hash",
                "value": "sha256:" + "3" * 64,
            },
            "geometry_payload": {
                "units": {"length": "m"},
                "coordinate_basis": "gltf_y_up_right_handed_meters",
                "nodes": [
                    {"node_id": "node:invented:A", "x": 0, "y": 0, "z": 0},
                    {"node_id": "node:invented:B", "x": 1.5, "y": 0, "z": 0},
                    {"node_id": "node:invented:C", "x": 1.5, "y": 0.75, "z": 0},
                ],
                "elements": [
                    {
                        "element_id": "element:invented:AB",
                        "from_node": "node:invented:A",
                        "to_node": "node:invented:B",
                        "target_name": "ops_segment_AB",
                    },
                    {
                        "element_id": "element:invented:BC",
                        "from_node": "node:invented:B",
                        "to_node": "node:invented:C",
                        "target_name": "ops_segment_BC",
                    },
                ],
                "omitted_entities": [{"object_type": "Support", "ref": "support:invented:A"}],
            },
            "stable_id_map": [
                {
                    "canonical_ref": ref("CenterlineElement", "element:invented:AB"),
                    "gltf_ref": ref("GltfNode", "0"),
                    "metadata_carrier": "gltf_extras_and_sidecar",
                    "mapping_status": "mapped",
                    "loss_category": "exported",
                },
                {
                    "canonical_ref": ref("CenterlineElement", "element:invented:BC"),
                    "gltf_ref": ref("GltfNode", "1"),
                    "metadata_carrier": "gltf_extras_and_sidecar",
                    "mapping_status": "mapped",
                    "loss_category": "exported",
                },
            ],
            "loss_report": [
                {
                    "loss_id": "loss:invented:review-centerline-exported",
                    "category": "exported",
                    "severity": "info",
                    "affected_refs": [ref("CenterlineElement", "element:invented:AB")],
                    "target_artifact_ref": ref("ReviewGeometryMember", "review-geometry:invented-del-17-08:model_gltf"),
                    "reason": "Invented centerline segment emitted as visual review geometry.",
                    "source_basis_ref": ref("Deliverable", "DEL-17-02"),
                    "downstream_implication": "Visual review geometry only; no solver or analysis fidelity is implied.",
                },
                {
                    "loss_id": "loss:invented:support-omitted",
                    "category": "omitted",
                    "severity": "warning",
                    "affected_refs": [ref("Support", "support:invented:A")],
                    "target_artifact_ref": ref("ReviewGeometryMember", "review-geometry:invented-del-17-08:model_gltf"),
                    "reason": "Support symbol review geometry is outside the v1 centerline-only scope.",
                    "source_basis_ref": ref("Deliverable", "DEL-17-08"),
                    "downstream_implication": "Support context remains available only through source records and loss report.",
                },
            ],
        }


    def build_from_source() -> dict[str, object]:
        return build_review_geometry_export_package(**source_payload())


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(PACKAGE_FIXTURE_PATH)
        built = build_from_source()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(PACKAGE_FIXTURE_PATH),
            )
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_review_geometry_export_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_package_members():
        first = build_from_source()
        second = build_from_source()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-08"
        assert first["package_status"] == "review_geometry_gltf_export_foundation"
        assert first["export_profile"]["artifact_format"] == "gltf_json_embedded_buffer"
        assert first["export_profile"]["primitive_mode"] == "LINES"
        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "model_gltf",
            "stable_id_map",
            "loss_report",
            "validation_report",
            "diagnostics",
        }
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_gltf_structure_uses_lines_and_embedded_buffer_with_identity_extras():
        package = build_from_source()
        gltf = package["gltf"]

        assert gltf == render_review_geometry_gltf(package["geometry_payload"], package["export_profile"])
        assert gltf == load_json(GLTF_FIXTURE_PATH)
        assert gltf["asset"]["version"] == "2.0"
        assert gltf["asset"]["generator"].startswith("OpenPipeStress DEL-17-08")
        assert gltf["buffers"][0]["uri"].startswith("data:application/octet-stream;base64,")
        assert gltf["buffers"][0]["byteLength"] == 48
        assert len(gltf["nodes"]) == 2
        assert len(gltf["meshes"]) == 2
        assert all(accessor["count"] == 2 for accessor in gltf["accessors"])
        assert all(mesh["primitives"][0]["mode"] == 1 for mesh in gltf["meshes"])
        node_meta = gltf["nodes"][0]["extras"]["openpipestress"]
        primitive_meta = gltf["meshes"][0]["primitives"][0]["extras"]["openpipestress"]
        assert node_meta["canonical_ref"] == ref("CenterlineElement", "element:invented:AB")
        assert primitive_meta["canonical_ref"] == ref("CenterlineElement", "element:invented:AB")
        assert node_meta["sidecar_authoritative"] is True
        assert gltf["asset"]["extras"]["openpipestress"]["artifact_role"] == "visual_review_geometry_only"


    def test_sidecar_id_map_and_manifest_preserve_canonical_identity():
        package = build_from_source()

        mapped = {item["canonical_ref"]["ref"]: item["gltf_ref"]["ref"] for item in package["stable_id_map"]}
        assert mapped == {"element:invented:AB": "0", "element:invented:BC": "1"}
        artifact = package["manifest"]["gltf_artifact"]
        assert artifact["path"] == "model.gltf"
        assert artifact["gltf_version"] == "2.0"
        assert artifact["primitive_mode"] == "LINES"
        assert artifact["node_count"] == 2
        assert artifact["mesh_count"] == 2
        assert artifact["embedded_buffer"] is True


    def test_bad_geometry_and_missing_sidecars_are_blocking():
        payload = source_payload()
        geometry_payload = deepcopy(payload["geometry_payload"])
        geometry_payload["nodes"][1] = {"node_id": "node:invented:B", "x": 0, "y": 0, "z": 0}
        geometry_payload["coordinate_basis"] = "source_z_up"
        geometry_payload["units"] = {"length": "ft"}

        package = build_review_geometry_export_package(
            export_id="review-geometry:blocked",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            geometry_payload=geometry_payload,
            stable_id_map=[],
            loss_report=[],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {
            "RG-LENGTH-UNIT-NOT-METERS",
            "RG-COORDINATE-BASIS-UNSUPPORTED",
            "RG-ZERO-LENGTH-SEGMENT",
            "RG-STABLE-ID-MAP-MISSING",
            "RG-LOSS-REPORT-MISSING",
        } <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_unresolved_node_refs_and_duplicate_ids_are_blocking():
        payload = source_payload()
        geometry_payload = deepcopy(payload["geometry_payload"])
        geometry_payload["nodes"].append({"node_id": "node:invented:A", "x": 2, "y": 0, "z": 0})
        geometry_payload["elements"][0]["to_node"] = "node:invented:missing"

        package = build_review_geometry_export_package(
            export_id="review-geometry:bad-ids",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            geometry_payload=geometry_payload,
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"RG-UNRESOLVED-NODE-REF", "RG-DUPLICATE-CANONICAL-ID"} <= codes


    def test_privacy_and_authority_boundary_diagnostics_are_blocking():
        payload = source_payload()
        package = build_review_geometry_export_package(
            export_id="review-geometry:privacy-boundary",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            geometry_payload=payload["geometry_payload"],
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
            export_profile={"free_metadata": {"unsafe_label": "cert" + "ified solver geometry"}},
            privacy={"commercial_tool_payload_embedded": True},
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"RG-PRIVACY-BOUNDARY-VIOLATION", "RG-PROFILE-AUTHORITY-TERM"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["professional_boundary"]["software_makes_solver_fidelity_claim"] is False
        assert package["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def test_profile_source_basis_refs_are_required():
        payload = source_payload()
        package = build_review_geometry_export_package(
            export_id="review-geometry:missing-source-basis",
            source_model_ref=payload["source_model_ref"],
            source_model_hash=payload["source_model_hash"],
            geometry_payload=payload["geometry_payload"],
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
            export_profile={"source_basis_refs": [ref("Document", "GLTF-2.0")]},
        )

        assert "RG-SOURCE-BASIS-REFS-MISSING" in {item["code"] for item in package["diagnostics"]}
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_writer_outputs_gltf_and_sidecars(tmp_path):
        package = build_from_source()

        write_review_geometry_export_package(tmp_path, package)

        assert load_json(tmp_path / "model.gltf") == package["gltf"]
        assert load_json(tmp_path / "manifest.json") == package["manifest"]
        assert load_json(tmp_path / "id_map.json") == package["stable_id_map"]
        assert load_json(tmp_path / "loss_report.json") == package["loss_report"]
        assert load_json(tmp_path / "validation_report.json") == package["validation_report"]
        assert load_json(tmp_path / "diagnostics.json") == package["diagnostics"]


    def test_fixtures_contain_no_private_or_protected_payload_text():
        text = "\n".join(
            walk_strings(
                {
                    "package": load_json(PACKAGE_FIXTURE_PATH),
                    "source": load_json(SOURCE_PAYLOAD_PATH),
                    "gltf": load_json(GLTF_FIXTURE_PATH),
                }
            )
        ).lower()
        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text


    def main():
        check_jsonschema_validation()
        test_builder_is_deterministic_and_preserves_package_members()
        test_gltf_structure_uses_lines_and_embedded_buffer_with_identity_extras()
        test_sidecar_id_map_and_manifest_preserve_canonical_identity()
        test_bad_geometry_and_missing_sidecars_are_blocking()
        test_unresolved_node_refs_and_duplicate_ids_are_blocking()
        test_privacy_and_authority_boundary_diagnostics_are_blocking()
        test_profile_source_basis_refs_are_required()
        test_fixtures_contain_no_private_or_protected_payload_text()


    if __name__ == "__main__":
        main()

## Component: tests/test_rule_pack_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the rule-pack schema."""

    import json
    import sys
    from copy import deepcopy
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "rule_pack.schema.yaml"
    EXAMPLE_PATH = ROOT / "examples" / "rule_packs" / "invented_demo.yaml"

    CANONICAL_DIMENSIONS = [
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ]

    RETIRED_DIMENSIONS = {
        "temperature_difference",
        "area_moment",
        "stiffness",
    }

    REQUIRED_TOP_LEVEL = {
        "metadata",
        "classification",
        "required_inputs",
        "formula_declarations",
        "value_slots",
        "check_definitions",
        "diagnostics",
        "checksums",
        "provenance",
        "professional_boundary",
    }

    REQUIRED_PROVENANCE = {
        "source_name",
        "source_type",
        "source_location",
        "source_license",
        "contributor",
        "contributor_certification",
        "redistribution_status",
        "protected_content_review",
        "review_status",
    }

    MIN_ITEM_ARRAYS = {
        "required_inputs",
        "formula_declarations",
        "value_slots",
        "check_definitions",
        "diagnostics",
        "open_decisions",
    }

    REQUIRED_CHECKSUM = {
        "algorithm",
        "canonicalization",
        "payload_ref",
        "payload_scope",
        "verification_status",
        "value",
    }

    REQUIRED_DIAGNOSTIC_POLICY = {
        "rule_check_blocking",
        "missing_input",
        "unit_mismatch",
        "provenance_gap",
        "redistribution_gap",
        "checksum_mismatch",
        "protected_content_suspected",
        "evaluator_error",
    }

    REQUIRED_PROFESSIONAL_BOUNDARY = {
        "software_makes_compliance_claim",
        "software_makes_certification_claim",
        "software_makes_sealing_claim",
        "software_makes_approval_claim",
        "software_makes_authentication_claim",
        "human_review_required",
        "human_acceptance_record_software_generated",
        "external_human_acceptance_ref_allowed",
        "hash_bound_human_acceptance_required",
        "reliance_notice",
    }

    FORBIDDEN_SCHEMA_TEXT = {
        "CODE_COMPLIANT",
        "certified",
        "sealed",
        "automatic compliance",
        "professional approval by the software",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_example():
        with EXAMPLE_PATH.open(encoding="utf-8") as example_file:
            return json.load(example_file)


    def definition(schema, name):
        return schema["$defs"][name]


    def required_at(schema, definition_name):
        return set(definition(schema, definition_name)["required"])


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    EXPRESSION_NODE_KINDS = {
        "literal",
        "variable_ref",
        "unary",
        "binary",
        "compare",
        "logical",
        "select",
        "aggregate",
        "interpolate",
        "lookup",
    }

    EVALUATOR_REFUSAL_MARKERS = {
        "unsupported_form",
        "unsafe_host_access",
    }

    REQUIRED_USER_TABLE = {
        "table_id",
        "argument_dimension",
        "argument_unit_ref",
        "result_dimension",
        "result_unit_ref",
        "rows",
    }

    FROZEN_GRAMMAR_STATUS = "frozen_open_pipe_stress_declared_expression"
    FROZEN_EXPRESSION_LANGUAGE = "open_pipe_stress_declared_expression"
    SEMVER_PATTERN = "^[0-9]+\\.[0-9]+\\.[0-9]+$"


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert REQUIRED_TOP_LEVEL <= set(schema["required"])
        assert "grammar_version" in schema["required"]
        assert schema["properties"]["grammar_version"]["pattern"] == SEMVER_PATTERN
        for property_name in MIN_ITEM_ARRAYS:
            assert schema["properties"][property_name]["minItems"] == 1

        metadata = definition(schema, "RulePackMetadata")
        assert {
            "rule_pack_id",
            "schema_version",
            "rule_pack_version",
            "lifecycle_status",
            "source_notice",
        } <= set(metadata["required"])

        classification = definition(schema, "RulePackClassification")
        assert classification["properties"]["protected_content_review_required"][
            "const"
        ] is True
        assert classification["properties"]["private_values_allowed"]["const"] is True
        assert "private_user_data_not_committed" in classification["properties"][
            "public_repository_policy"
        ]["enum"]

        provenance = definition(schema, "ProvenanceRecord")
        assert REQUIRED_PROVENANCE <= set(provenance["required"])
        assert {
            "invented_public_example",
            "user_private_basis",
            "protected_suspected",
        } <= set(provenance["properties"]["source_type"]["enum"])
        assert "completed_no_protected_content" in provenance["properties"][
            "protected_content_review"
        ]["enum"]

        checksum = definition(schema, "Checksum")
        assert REQUIRED_CHECKSUM <= set(checksum["required"])
        assert {"JCS", "NONE", "TBD"} <= set(
            checksum["properties"]["canonicalization"]["enum"]
        )
        assert "CALLER_SUPPLIED_JCS_BYTES_UNVERIFIED" in checksum["properties"][
            "canonicalization"
        ]["enum"]
        assert {
            "rule_pack_payload",
            "formula_declaration",
            "value_slot_declaration",
            "non_json_asset_manifest",
            "TBD",
        } <= set(checksum["properties"]["payload_scope"]["enum"])
        assert "deferred_to_DEL_06_04" in checksum["properties"][
            "verification_status"
        ]["enum"]
        checksum_set = definition(schema, "ChecksumSet")
        assert {
            "rule_pack_checksum",
            "payload_checksums",
            "checksum_lifecycle_status",
            "hash_basis",
        } <= set(checksum_set["required"])

        required_input = definition(schema, "RequiredInput")
        assert {
            "quantity_intent",
            "completeness_status",
            "missing_value_diagnostic",
            "provenance",
            "redistribution_status",
            "provenance_required",
            "redistribution_status_required",
        } <= set(required_input["required"])
        assert required_input["properties"]["provenance_required"]["const"] is True
        assert required_input["properties"]["redistribution_status_required"][
            "const"
        ] is True

        formula = definition(schema, "FormulaDeclaration")
        assert formula["properties"]["arbitrary_code_execution_allowed"]["const"] is False
        assert {
            "declarative_ast",
            "symbolic_reference",
            "structured_expression",
        } <= set(formula["properties"]["declaration_form"]["enum"])
        assert {
            "declaration_payload",
            "completeness_status",
        } <= set(formula["required"])
        assert formula["properties"]["input_refs"]["minItems"] == 1
        assert "no_protected_text_tables_or_copied_formulas" in formula["properties"][
            "protected_content_policy"
        ]["enum"]
        assert formula["properties"]["output_dimension"]["$ref"] == "#/$defs/QuantityIntent"
        payload = definition(schema, "FormulaDeclarationPayload")
        assert {
            "payload_kind",
            "payload_summary",
            "grammar_status",
            "arbitrary_code_execution_allowed",
            "protected_content_policy",
        } <= set(payload["required"])
        assert payload["properties"]["arbitrary_code_execution_allowed"]["const"] is False
        assert {
            FROZEN_GRAMMAR_STATUS,
            "grammar_not_selected",
            "future_human_approved_grammar_required",
            "TBD",
        } <= set(payload["properties"]["grammar_status"]["enum"])
        assert payload["properties"]["expression_ast"]["$ref"] == "#/$defs/ExpressionNode"
        declarative_gate = payload["allOf"][0]
        assert declarative_gate["if"]["properties"]["payload_kind"]["const"] == (
            "declarative_ast"
        )
        assert declarative_gate["then"]["required"] == ["expression_ast"]
        assert declarative_gate["then"]["properties"]["grammar_status"]["const"] == (
            FROZEN_GRAMMAR_STATUS
        )
        formula_gate = formula["allOf"][0]
        assert formula_gate["if"]["properties"]["declaration_form"]["const"] == (
            "declarative_ast"
        )
        assert formula_gate["then"]["properties"]["expression_language"]["const"] == (
            FROZEN_EXPRESSION_LANGUAGE
        )

        expression_node = definition(schema, "ExpressionNode")
        node_kinds = set()
        for branch in expression_node["oneOf"]:
            node_kinds.add(branch["properties"]["node"]["const"])
            assert branch["additionalProperties"] is False
        assert node_kinds == EXPRESSION_NODE_KINDS
        assert not (node_kinds & EVALUATOR_REFUSAL_MARKERS)
        aggregate_branch = next(
            branch
            for branch in expression_node["oneOf"]
            if branch["properties"]["node"]["const"] == "aggregate"
        )
        assert aggregate_branch["properties"]["operands"]["minItems"] == 1

        expression_quantity = definition(schema, "ExpressionQuantity")
        assert set(expression_quantity["required"]) == {"value", "dimension", "unit_ref"}
        assert expression_quantity["properties"]["dimension"]["$ref"] == (
            "#/$defs/DimensionId"
        )
        assert "unit_required" not in expression_quantity["properties"]
        assert "dimension_check_required" not in expression_quantity["properties"]

        user_table = definition(schema, "UserTableValue")
        assert REQUIRED_USER_TABLE <= set(user_table["required"])
        assert user_table["properties"]["rows"]["minItems"] == 1
        table_row = user_table["properties"]["rows"]["items"]
        assert set(table_row["required"]) == {"argument", "result"}

        quantity_intent = definition(schema, "QuantityIntent")
        assert {
            "dimension",
            "unit_ref",
            "unit_required",
            "dimension_check_required",
        } <= set(quantity_intent["required"])
        assert quantity_intent["properties"]["dimension"]["$ref"] == "#/$defs/DimensionId"
        dimensions = definition(schema, "DimensionId")["enum"]
        assert dimensions == CANONICAL_DIMENSIONS
        assert not (set(dimensions) & RETIRED_DIMENSIONS)

        value_slot = definition(schema, "UserSuppliedValueSlot")
        assert {
            "quantity_intent",
            "value_status",
            "missing_value_diagnostic",
            "provenance",
            "redistribution_status",
            "provenance_required",
            "redistribution_status_required",
            "review_status",
            "completeness_status",
        } <= set(value_slot["required"])
        assert value_slot["properties"]["provenance_required"]["const"] is True
        assert value_slot["properties"]["redistribution_status_required"]["const"] is True

        check = definition(schema, "CheckDefinition")
        assert {"RULE_INPUTS_INCOMPLETE", "USER_RULE_CHECKED", "USER_RULE_FAILED"} <= set(
            definition(schema, "AnalysisStatus")["enum"]
        )
        assert "HUMAN_APPROVED_FOR_PROJECT" not in definition(schema, "AnalysisStatus")[
            "enum"
        ]
        assert {"acceptability_basis", "result_statuses", "diagnostic_policy"} <= set(
            check["required"]
        )
        assert "value_slot_refs" in check["required"]
        assert check["properties"]["required_input_refs"]["minItems"] == 1
        assert check["properties"]["value_slot_refs"]["minItems"] == 1
        diagnostic_policy = definition(schema, "DiagnosticPolicy")
        assert REQUIRED_DIAGNOSTIC_POLICY <= set(diagnostic_policy["required"])

        diagnostic_codes = set(definition(schema, "RulePackDiagnosticCode")["enum"])
        assert {
            "RULE_CHECK_BLOCKING",
            "RULE_INPUT_MISSING",
            "RULE_UNIT_MISMATCH",
            "RULE_PROVENANCE_WARNING",
            "RULE_REDISTRIBUTION_WARNING",
            "RULE_CHECKSUM_MISMATCH",
            "RULE_PROTECTED_CONTENT_WARNING",
            "RULE_EVALUATOR_ERROR",
            "RULE_INCOMPLETE_DATA",
            "RULE_PROFESSIONAL_BOUNDARY_NOTICE",
        } <= diagnostic_codes
        diagnostic = definition(schema, "RulePackDiagnostic")
        assert {
            "diagnostic_class",
            "blocks_rule_check",
        } <= set(diagnostic["required"])
        assert {
            "rule_check_blocking",
            "checksum_mismatch",
            "professional_boundary_notice",
        } <= set(definition(schema, "RulePackDiagnosticClass")["enum"])

        professional_boundary = definition(schema, "ProfessionalBoundary")
        assert REQUIRED_PROFESSIONAL_BOUNDARY <= set(professional_boundary["required"])
        assert (
            professional_boundary["properties"]["software_makes_compliance_claim"][
                "const"
            ]
            is False
        )
        assert professional_boundary["properties"]["human_review_required"]["const"] is True
        assert (
            professional_boundary["properties"][
                "human_acceptance_record_software_generated"
            ]["const"]
            is False
        )
        assert professional_boundary["properties"]["software_makes_approval_claim"][
            "const"
        ] is False
        assert professional_boundary["properties"][
            "software_makes_authentication_claim"
        ]["const"] is False
        assert professional_boundary["properties"][
            "hash_bound_human_acceptance_required"
        ]["const"] is True

        open_decision_topics = set(
            definition(schema, "OpenDecision")["properties"]["topic"]["enum"]
        )
        assert {
            "expression_grammar",
            "evaluator_library",
            "private_encryption_default",
            "storage_container",
            "checksum_library",
        } <= open_decision_topics

        all_text = "\n".join(walk_strings(schema))
        for forbidden in FORBIDDEN_SCHEMA_TEXT:
            assert forbidden not in all_text


    def check_invented_example_shape():
        schema = load_schema()
        example = load_example()
        for property_name in MIN_ITEM_ARRAYS:
            assert example[property_name], property_name
        output_dimension = example["formula_declarations"][0]["output_dimension"]
        assert required_at(schema, "QuantityIntent") <= set(output_dimension)
        assert output_dimension["dimension"] == "dimensionless"
        assert output_dimension["unit_ref"] == "ratio"
        assert output_dimension["unit_required"] is True
        assert output_dimension["dimension_check_required"] is True

        for required_input in example["required_inputs"]:
            assert required_at(schema, "RequiredInput") <= set(required_input)
            assert required_at(schema, "ProvenanceRecord") <= set(
                required_input["provenance"]
            )
            assert required_input["redistribution_status"] == (
                required_input["provenance"]["redistribution_status"]
            )

        assert example["grammar_version"] == "1.0.0"

        formula = example["formula_declarations"][0]
        assert required_at(schema, "FormulaDeclaration") <= set(formula)
        assert formula["declaration_form"] == "declarative_ast"
        assert formula["expression_language"] == FROZEN_EXPRESSION_LANGUAGE
        assert required_at(schema, "FormulaDeclarationPayload") <= set(
            formula["declaration_payload"]
        )
        assert formula["declaration_payload"]["grammar_status"] == FROZEN_GRAMMAR_STATUS
        expression_ast = formula["declaration_payload"]["expression_ast"]
        assert expression_ast["node"] == "binary"
        assert expression_ast["operator"] == "divide"
        assert expression_ast["left"]["variable_id"] == "demo_actual_quantity"
        assert expression_ast["right"]["variable_id"] == "demo_limit_quantity"
        assert formula["declaration_payload"]["arbitrary_code_execution_allowed"] is False
        assert formula["arbitrary_code_execution_allowed"] is False
        assert formula["completeness_status"] == "complete"

        value_slot = example["value_slots"][0]
        assert required_at(schema, "UserSuppliedValueSlot") <= set(value_slot)
        assert value_slot["provenance_required"] is True
        assert value_slot["redistribution_status_required"] is True

        check = example["check_definitions"][0]
        assert check["value_slot_refs"]
        assert REQUIRED_DIAGNOSTIC_POLICY <= set(check["diagnostic_policy"])

        checksum = example["checksums"]["rule_pack_checksum"]
        assert REQUIRED_CHECKSUM <= set(checksum)
        assert checksum["verification_status"] == "verified"
        assert checksum["algorithm"] == "sha256"
        assert checksum["canonicalization"] == "JCS"
        assert checksum["payload_excludes"] == ["checksums"]
        assert example["checksums"]["checksum_lifecycle_status"] == "verified"
        assert example["checksums"]["hash_basis"] == "Canonical JSON/JCS-compatible"

        diagnostic = example["diagnostics"][0]
        assert required_at(schema, "RulePackDiagnostic") <= set(diagnostic)
        assert diagnostic["diagnostic_class"] == "professional_boundary_notice"
        assert diagnostic["blocks_rule_check"] is False

        professional_boundary = example["professional_boundary"]
        assert REQUIRED_PROFESSIONAL_BOUNDARY <= set(professional_boundary)
        assert professional_boundary["software_makes_approval_claim"] is False
        assert professional_boundary["software_makes_authentication_claim"] is False
        assert professional_boundary["hash_bound_human_acceptance_required"] is True

        open_topics = {item["topic"] for item in example["open_decisions"]}
        assert {
            "expression_grammar",
            "evaluator_library",
            "private_encryption_default",
            "storage_container",
            "checksum_library",
            "result_envelope_integration",
        } <= open_topics


    def check_jsonschema_validation():
        schema = load_schema()
        example = load_example()
        try:
            from jsonschema import Draft202012Validator
        except ModuleNotFoundError as exc:
            _skip_or_note_missing_jsonschema(exc)
            return

        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))
        if errors:
            formatted = "\n".join(_format_error(error) for error in errors[:10])
            remaining = len(errors) - 10
            suffix = f"\n... {remaining} more validation errors" if remaining > 0 else ""
            raise AssertionError(f"{EXAMPLE_PATH} failed JSON Schema validation:\n{formatted}{suffix}")


    def _validator_or_skip(schema):
        try:
            from jsonschema import Draft202012Validator
        except ModuleNotFoundError as exc:
            _skip_or_note_missing_jsonschema(exc)
            return None

        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema)


    def _assert_invalid_instance(validator, instance, expected_path):
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if not errors:
            raise AssertionError("instance unexpectedly passed JSON Schema validation")
        paths = {_error_path(error) for error in errors}
        assert expected_path in paths, paths


    def _error_path(error):
        path = "$"
        for part in error.path:
            if isinstance(part, int):
                path += f"[{part}]"
            else:
                path += f".{part}"
        return path


    def _format_error(error):
        path = "$"
        for part in error.path:
            if isinstance(part, int):
                path += f"[{part}]"
            else:
                path += f".{part}"
        return f"{path}: {error.message}"


    def _skip_or_note_missing_jsonschema(exc):
        message = (
            "jsonschema>=4,<5 is required for full rule-pack JSON Schema validation; "
            "install with: python3 -m pip install -r requirements-dev.txt"
        )
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(f"{message}; import error: {exc}")
        print(f"SKIP: {message}; import error: {exc}")


    def test_invented_demo_checksum_matches_jcs_recomputation():
        """Cross-engine parity pin with the Rust golden test in
        core/rules/rule_pack_document (payload = document minus the checksums
        member, RFC 8785 canonical bytes, SHA-256)."""
        from hashlib import sha256

        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from core.project_persistence import canonical_json

        example = load_example()
        payload = {key: value for key, value in example.items() if key != "checksums"}
        digest = sha256(canonical_json(payload).encode("utf-8")).hexdigest()
        assert example["checksums"]["rule_pack_checksum"]["value"] == digest
        member = f'"grammar_version":"{example["grammar_version"]}"'
        assert member in canonical_json(payload)


    def test_rule_pack_schema_contract():
        check_schema_contract()


    def test_invented_demo_uses_unit_bearing_formula_output_metadata():
        check_invented_example_shape()


    def test_invented_demo_validates_against_rule_pack_schema():
        check_jsonschema_validation()


    def test_schema_rejects_missing_or_unsafe_hardened_fields():
        schema = load_schema()
        example = load_example()
        validator = _validator_or_skip(schema)
        if validator is None:
            return

        missing_required_input_provenance = deepcopy(example)
        del missing_required_input_provenance["required_inputs"][0]["provenance"]
        _assert_invalid_instance(
            validator,
            missing_required_input_provenance,
            "$.required_inputs[0]",
        )

        executable_formula = deepcopy(example)
        executable_formula["formula_declarations"][0][
            "arbitrary_code_execution_allowed"
        ] = True
        _assert_invalid_instance(
            validator,
            executable_formula,
            "$.formula_declarations[0].arbitrary_code_execution_allowed",
        )

        missing_checksum_scope = deepcopy(example)
        del missing_checksum_scope["checksums"]["rule_pack_checksum"]["payload_scope"]
        _assert_invalid_instance(
            validator,
            missing_checksum_scope,
            "$.checksums.rule_pack_checksum",
        )

        software_approval_claim = deepcopy(example)
        software_approval_claim["professional_boundary"][
            "software_makes_approval_claim"
        ] = True
        _assert_invalid_instance(
            validator,
            software_approval_claim,
            "$.professional_boundary.software_makes_approval_claim",
        )

        missing_grammar_version = deepcopy(example)
        del missing_grammar_version["grammar_version"]
        _assert_invalid_instance(validator, missing_grammar_version, "$")

        malformed_grammar_version = deepcopy(example)
        malformed_grammar_version["grammar_version"] = "v1"
        _assert_invalid_instance(
            validator,
            malformed_grammar_version,
            "$.grammar_version",
        )

        declarative_without_ast = deepcopy(example)
        del declarative_without_ast["formula_declarations"][0]["declaration_payload"][
            "expression_ast"
        ]
        _assert_invalid_instance(
            validator,
            declarative_without_ast,
            "$.formula_declarations[0].declaration_payload",
        )

        stale_grammar_status = deepcopy(example)
        stale_grammar_status["formula_declarations"][0]["declaration_payload"][
            "grammar_status"
        ] = "grammar_not_selected"
        _assert_invalid_instance(
            validator,
            stale_grammar_status,
            "$.formula_declarations[0].declaration_payload.grammar_status",
        )

        refusal_marker_authored = deepcopy(example)
        refusal_marker_authored["formula_declarations"][0]["declaration_payload"][
            "expression_ast"
        ] = {"node": "unsafe_host_access", "request": "filesystem"}
        _assert_invalid_instance(
            validator,
            refusal_marker_authored,
            "$.formula_declarations[0].declaration_payload.expression_ast",
        )

        relaxed_literal_flags = deepcopy(example)
        relaxed_literal_flags["formula_declarations"][0]["declaration_payload"][
            "expression_ast"
        ] = {
            "node": "literal",
            "quantity": {
                "value": 1.0,
                "dimension": "dimensionless",
                "unit_ref": "ratio",
                "unit_required": False,
            },
        }
        _assert_invalid_instance(
            validator,
            relaxed_literal_flags,
            "$.formula_declarations[0].declaration_payload.expression_ast",
        )

        malformed_table_row = deepcopy(example)
        malformed_table_row["formula_declarations"][0]["declaration_payload"][
            "expression_ast"
        ] = {
            "node": "interpolate",
            "table": {
                "table_id": "demo_invented_table",
                "argument_dimension": "dimensionless",
                "argument_unit_ref": "ratio",
                "result_dimension": "dimensionless",
                "result_unit_ref": "ratio",
                "rows": [{"argument": 1.0}],
            },
            "argument": {
                "node": "variable_ref",
                "variable_id": "demo_actual_quantity",
            },
        }
        _assert_invalid_instance(
            validator,
            malformed_table_row,
            "$.formula_declarations[0].declaration_payload.expression_ast",
        )


    def main():
        check_schema_contract()
        check_invented_example_shape()
        check_jsonschema_validation()


    if __name__ == "__main__":
        main()

## Component: tests/test_section_properties.py

    #!/usr/bin/env python3
    """Checks for pipe section and mass-property calculations."""

    from math import isclose, pi
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))

    from core.section_properties.calculator import (  # noqa: E402
        PipeSectionInput,
        Quantity,
        calculate_pipe_section_properties,
        quantity_from_mapping,
    )


    PROVENANCE = {
        "source_name": "Invented section property test",
        "source_location": "tests/test_section_properties.py",
        "source_license": "project_test",
        "contributor": "OpenPipeStress",
        "contributor_certification": "invented non-engineering test value",
        "redistribution_status": "TBD",
        "review_status": "pending",
    }

    CANONICAL_OUTPUT_DIMENSIONS = {
        "length",
        "area",
        "second_moment_area",
        "section_modulus",
        "volume_per_length",
        "mass_per_length",
    }


    def q(value, unit="m", dimension="length"):
        return Quantity(value, unit, dimension, PROVENANCE)


    def codes(result):
        return {finding.code for finding in result.diagnostics}


    def test_calculates_pipe_section_properties_from_user_dimensions():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=q(10.0),
                wall_thickness=q(1.0),
            )
        )

        assert result.accepted is True
        props = result.properties
        assert isclose(props["inside_diameter"].magnitude, 8.0)
        assert isclose(props["metal_area"].magnitude, pi / 4.0 * (10.0**2 - 8.0**2))
        assert isclose(
            props["moment_of_inertia"].magnitude,
            pi / 64.0 * (10.0**4 - 8.0**4),
        )
        assert isclose(
            props["section_modulus"].magnitude,
            props["moment_of_inertia"].magnitude / 5.0,
        )
        assert props["cross_section_area"].dimension == "area"
        assert props["cross_section_area"].unit == "m^2"
        assert props["moment_of_inertia"].dimension == "second_moment_area"
        assert props["torsional_constant"].dimension == "second_moment_area"
        assert props["section_modulus"].dimension == "section_modulus"
        assert props["contents_volume_per_length"].dimension == "volume_per_length"
        assert {item.dimension for item in props.values()} <= CANONICAL_OUTPUT_DIMENSIONS
        assert (
            props["cross_section_area"]
            .provenance["contributor_certification"]
            .startswith("calculated from user-entered")
        )


    def test_corrosion_allowance_reduces_effective_wall():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=q(10.0),
                wall_thickness=q(1.0),
                corrosion_allowance=q(0.25),
            )
        )

        assert result.accepted is True
        assert isclose(result.properties["inside_diameter"].magnitude, 8.5)


    def test_mass_per_length_uses_only_supplied_densities():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=q(10.0),
                wall_thickness=q(1.0),
                material_density=q(2.0, "kg/m^3", "density"),
                contents_density=q(3.0, "kg/m^3", "density"),
                insulation_thickness=q(0.5),
                insulation_density=q(4.0, "kg/m^3", "density"),
            )
        )

        assert result.accepted is True
        props = result.properties
        metal_area = pi / 4.0 * (10.0**2 - 8.0**2)
        contents_area = pi / 4.0 * 8.0**2
        insulation_area = pi / 4.0 * (11.0**2 - 10.0**2)
        expected = metal_area * 2.0 + contents_area * 3.0 + insulation_area * 4.0
        assert isclose(props["mass_per_length"].magnitude, expected)
        assert props["mass_per_length"].dimension == "mass_per_length"


    def test_missing_dimensions_are_blocking_findings_not_defaults():
        result = calculate_pipe_section_properties(
            PipeSectionInput(outside_diameter=q(10.0), wall_thickness=None)
        )

        assert result.accepted is False
        assert result.properties == {}
        assert "SECTION_DIMENSION_MISSING" in codes(result)
        diagnostic = result.diagnostics[0]
        assert diagnostic.diagnostic_class == "SOLVE_BLOCKING"
        assert diagnostic.source == "core/section_properties/calculator.py"
        assert diagnostic.affected_object == "wall_thickness"
        assert diagnostic.provenance["source_location"] == "core/section_properties/calculator.py"


    def test_missing_provenance_is_blocking_finding():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=Quantity(10.0, "m", "length", {}),
                wall_thickness=q(1.0),
            )
        )

        assert result.accepted is False
        assert result.properties == {}
        assert "SECTION_PROVENANCE_MISSING" in codes(result)


    def test_mixed_units_are_rejected_without_hidden_conversion():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=q(10.0, "in", "length"),
                wall_thickness=q(1.0, "mm", "length"),
            )
        )

        assert result.accepted is False
        assert result.properties == {}
        assert "SECTION_DIMENSION_INCONSISTENT" in codes(result)


    def test_invalid_geometry_is_rejected():
        result = calculate_pipe_section_properties(
            PipeSectionInput(
                outside_diameter=q(10.0),
                wall_thickness=q(0.5),
                corrosion_allowance=q(0.5),
            )
        )

        assert result.accepted is False
        assert "SECTION_CALCULATION_INPUT_INVALID" in codes(result)


    def test_schema_like_quantity_mapping_requires_unit_metadata():
        assert (
            quantity_from_mapping(
                {
                    "magnitude": 10.0,
                    "unit": "m",
                    "dimension": "length",
                    "provenance": PROVENANCE,
                }
            )
            == q(10.0)
        )
        assert quantity_from_mapping({"magnitude": 10.0, "dimension": "length"}) is None
        assert (
            quantity_from_mapping({"magnitude": 10.0, "unit": "m", "dimension": "length"})
            is None
        )


    if __name__ == "__main__":
        test_calculates_pipe_section_properties_from_user_dimensions()
        test_corrosion_allowance_reduces_effective_wall()
        test_mass_per_length_uses_only_supplied_densities()
        test_missing_dimensions_are_blocking_findings_not_defaults()
        test_missing_provenance_is_blocking_finding()
        test_mixed_units_are_rejected_without_hidden_conversion()
        test_invalid_geometry_is_rejected()
        test_schema_like_quantity_mapping_requires_unit_metadata()

## Component: tests/test_security_threat_model.py

    #!/usr/bin/env python3
    """Focused checks for DEL-12-05 security threat-model SCA-004 coverage."""

    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    THREAT_MODEL = ROOT / "docs" / "security" / "threat_model.md"


    def threat_model_text() -> str:
        return THREAT_MODEL.read_text(encoding="utf-8").lower()


    def test_sca004_export_workflows_are_covered():
        text = threat_model_text()
        required_phrases = {
            "sca-004",
            "target profiles",
            "stable id maps",
            "loss reports",
            "caepipe mbf",
            "external-harness evidence",
            "stress-neutral csv/json",
            "conservative pcf",
            "glb/gltf review geometry",
            "native open json",
            "export adapter sdk",
        }

        missing = sorted(phrase for phrase in required_phrases if phrase not in text)
        assert not missing


    def test_sca004_controls_preserve_security_and_data_boundaries():
        text = threat_model_text()
        required_phrases = {
            "do not bundle",
            "bypass licenses",
            "reverse engineer protected formats",
            "proprietary examples",
            "leak private data by default",
            "telemetry is disabled by default",
            "no direct sql",
            "raw sqlite",
            "denied by default",
            "user-owned at external-tool boundaries",
            "non-authoritative evidence labels",
        }

        missing = sorted(phrase for phrase in required_phrases if phrase not in text)
        assert not missing


    def test_threat_model_avoids_positive_reliance_and_target_claims():
        text = threat_model_text()
        prohibited_positive_phrases = {
            "is code compliant",
            "are code compliant",
            "certifies engineering",
            "security certified",
            "professionally approved",
            "approved for reliance",
            "validated by caepipe",
            "caepipe-compatible",
            "vendor-compatible",
            "asme table",
            "b31j",
            "real client",
        }

        present = sorted(phrase for phrase in prohibited_positive_phrases if phrase in text)
        assert not present


    if __name__ == "__main__":
        test_sca004_export_workflows_are_covered()
        test_sca004_controls_preserve_security_and_data_boundaries()
        test_threat_model_avoids_positive_reliance_and_target_claims()
        print("PASS: DEL-12-05 security threat-model checks")

## Component: tests/test_solve_execution_ux.py

    #!/usr/bin/env python3
    """Focused tests for DEL-07-07 solve execution UX contracts."""

    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.gui.solve_execution import build_solve_execution_ux, canonical_json  # noqa: E402


    def main():
        record = build_solve_execution_ux(
            run_panel_id="invented-run-panel",
            events=[
                {"event_id": "queued", "state": "queued", "progress_percent": 0},
                {
                    "event_id": "running",
                    "state": "running",
                    "progress_percent": 40,
                    "diagnostic_refs": [{"ref_type": "diagnostic", "ref_id": "diag-1"}],
                },
                {
                    "event_id": "cancel-request",
                    "state": "cancelling",
                    "progress_percent": 40,
                    "cancellation_requested": True,
                },
                {"event_id": "cancelled", "state": "cancelled", "progress_percent": 40},
            ],
        )
        assert record["deliverable_id"] == "DEL-07-07"
        assert record["solver_execution"] == "not_performed_by_gui_contract"
        assert record["job_orchestration"] == "invented_state_transitions_only"
        assert record["final_state"] == "cancelled"
        assert record["cancellation"]["requested"] is True
        assert record["cancellation"]["mutates_solver_process_directly"] is False
        assert not record["diagnostics"]
        assert record["software_makes_professional_acceptance_claim"] is False
        assert record["analysis_boundary_contract"]["contract_ref"] == "DEL-02-03"
        assert "professional acceptance" not in canonical_json(record).lower()

        completed = build_solve_execution_ux(
            run_panel_id="invented-completed-run-panel",
            events=[
                {
                    "event_id": "completed",
                    "state": "completed",
                    "progress_percent": 100,
                    "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                    "model_hashes": [
                        {
                            "algorithm": "sha256",
                            "canonicalization": "JCS",
                            "payload_ref": {"ref_type": "ModelState", "ref_id": "state:invented"},
                            "value": "sha256:invented-model",
                        }
                    ],
                    "result_hashes": [
                        {
                            "algorithm": "sha256",
                            "canonicalization": "JCS",
                            "payload_ref": {"ref_type": "ResultEnvelope", "ref_id": "results:invented"},
                            "value": "sha256:invented-result",
                        }
                    ],
                    "provenance_refs": [{"ref_type": "AnalysisRun", "ref_id": "run:invented"}],
                }
            ],
        )
        assert completed["timeline"][0]["analysis_status"] == ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"]
        assert completed["timeline"][0]["hash_boundary"]["hashes_present"] is True
        assert not completed["diagnostics"]


    def test_solve_execution_ux_main():
        main()


    if __name__ == "__main__":
        main()

## Component: tests/test_state_comparison_handoff_report_sections.py

    #!/usr/bin/env python3
    """Focused tests for DEL-08-06 state/comparison/handoff report sections."""

    from __future__ import annotations

    from copy import deepcopy
    from pathlib import Path
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    from core.reporting.state_comparison_handoff_sections import (  # noqa: E402
        build_state_comparison_handoff_report_sections,
        canonical_json,
        diagnostics_for_report_sections,
    )


    FORBIDDEN_OUTPUT_PHRASES = {
        "code " + "compliant",
        "cert" + "ified",
        "se" + "aled",
        "authentic" + "ated",
        "professional " + "approval",
        "external " + "validation",
        "engineering " + "acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def provenance(source_name: str = "Invented DEL-08-06 fixture") -> dict[str, str]:
        return {
            "source_name": source_name,
            "source_location": "tests/test_state_comparison_handoff_report_sections.py",
            "source_license": "project-invented-test-data",
            "contributor": "OpenPipeStress",
            "contributor_attestation": "invented non-engineering fixture",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "machine_checked",
            "review_classification": "machine_checked",
            "privacy_classification": "invented_public_example",
        }


    def checksum(payload_ref: dict[str, str], scope: str, value: str) -> dict[str, object]:
        return {
            "algorithm": "sha256",
            "canonicalization": "JCS",
            "payload_ref": payload_ref,
            "payload_scope": scope,
            "value": value,
        }


    def boundary() -> dict[str, bool]:
        return {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
            "software_creates_professional_reliance_record": False,
            "software_creates_external_validation_record": False,
        }


    def model_state() -> dict[str, object]:
        state_id = "state:invented-del-08-06"
        return {
            "model_state": {
                "state_id": state_id,
                "state_name": "Invented state fixture",
                "state_kind": "handoff_basis",
                "created_at": "2026-05-06T00:00:00Z",
                "model_ref": ref("Model", "model:invented-del-08-06"),
                "parent_state_refs": [],
                "tags": [],
                "notes": [],
                "external_references": [],
                "unresolved_assumptions": [
                    {
                        "assumption_id": "assumption:invented-state-review",
                        "statement": "Invented state fixture requires human review before use.",
                        "affected_refs": [ref("ModelState", state_id)],
                        "provenance": provenance("Invented state assumption"),
                    }
                ],
                "warnings": [
                    {
                        "code": "STATE-INVENTED-WARNING",
                        "severity": "warning",
                        "message": "Invented state warning for traceability.",
                        "affected_refs": [ref("ModelState", state_id)],
                        "provenance": provenance("Invented state warning"),
                    }
                ],
                "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                "hashes": [checksum(ref("ModelState", state_id), "model_state_record", "sha256:invented-state")],
                "immutability_policy": {"snapshot_is_read_only": True},
                "professional_boundary": boundary(),
                "provenance": provenance("Invented model state"),
            }
        }


    def analysis_run() -> dict[str, object]:
        run_id = "run:invented-del-08-06"
        return {
            "analysis_run": {
                "run_id": run_id,
                "run_name": "Invented run fixture",
                "run_kind": "mechanics_solve",
                "created_at": "2026-05-06T00:01:00Z",
                "model_state_ref": ref("ModelState", "state:invented-del-08-06"),
                "solver_version": {
                    "solver_id": "invented-solver",
                    "version": "0.0.0-fixture",
                    "build_hash": "sha256:invented-solver",
                },
                "settings_ref": ref("SolverSettings", "settings:invented-del-08-06"),
                "unit_system_ref": ref("UnitSystem", "units:invented-del-08-06"),
                "load_basis_refs": [ref("LoadCase", "load:invented")],
                "diagnostics": [],
                "result_refs": [ref("ResultEnvelope", "results:invented-del-08-06")],
                "rule_pack_refs": [
                    {
                        "rule_pack_id": "rule-pack:invented-del-08-06",
                        "version": "0.1.0",
                        "checksum": checksum(ref("RulePack", "rule-pack:invented-del-08-06"), "rule_pack_reference_metadata", "sha256:invented-rule"),
                        "source_notice": "Invented metadata-only rule-pack reference.",
                        "private_payload_redacted": True,
                        "provenance": provenance("Invented rule-pack reference"),
                    }
                ],
                "library_refs": [ref("Library", "library:invented-del-08-06")],
                "hashes": [checksum(ref("AnalysisRun", run_id), "analysis_run_record", "sha256:invented-run")],
                "analysis_status": ["MECHANICS_SOLVED", "HUMAN_REVIEW_REQUIRED"],
                "reproducibility": {
                    "input_manifest_refs": [ref("Manifest", "manifest:invented-del-08-06")],
                    "environment_refs": [ref("Environment", "environment:invented")],
                    "determinism_notes": ["invented deterministic fixture"],
                    "unresolved_tbd": [],
                },
                "professional_boundary": boundary(),
                "provenance": provenance("Invented analysis run"),
            }
        }


    def analysis_comparison() -> dict[str, object]:
        return {
            "comparison_id": "comparison:invented-run-delta",
            "run_context": {
                "left": {"run_id": "run:left", "hashes": [checksum(ref("AnalysisRun", "run:left"), "analysis_run_record", "sha256:left")]},
                "right": {"run_id": "run:right", "hashes": [checksum(ref("AnalysisRun", "run:right"), "analysis_run_record", "sha256:right")]},
            },
            "result_deltas": [
                {
                    "mapping_id": "mapping:invented-stress",
                    "mapping_status": "manual_match",
                    "left_result_id": "result:left-stress",
                    "right_result_id": "result:right-stress",
                    "result_family": "stress",
                    "dimension": "stress",
                    "normalized_unit": "Pa",
                    "left_magnitude": 1000.0,
                    "right_magnitude": 1001.0,
                    "left_normalized_magnitude": 1000.0,
                    "right_normalized_magnitude": 1001.0,
                    "normalized_delta": 1.0,
                    "absolute_normalized_delta": 1.0,
                    "tolerance_profile_ref": "tolerance:invented-review",
                    "classification": "requires_human_review",
                }
            ],
            "settings_deltas": [],
            "diagnostics": [],
            "professional_boundary": boundary(),
            "provenance": provenance("Invented analysis comparison"),
        }


    def handoff_package() -> dict[str, object]:
        return {
            "deliverable_id": "DEL-15-01",
            "handoff_package_manifest": {
                "package_identity": {
                    "handoff_package_id": "handoff:invented-del-08-06",
                    "manifest_id": "manifest:invented-del-08-06",
                    "package_schema_version": "0.1.0",
                },
                "model_hash": checksum(ref("Model", "model:invented-del-08-06"), "model_hash", "sha256:invented-model"),
                "units_manifest": {
                    "unit_system_ref": ref("UnitSystem", "units:invented-del-08-06"),
                    "force_unit": "N",
                    "stress_unit": "Pa",
                    "provenance": provenance("Invented units manifest"),
                },
                "entity_ids": {
                    "component_ids": ["component:invented-pipe"],
                    "analysis_run_ids": ["run:invented-del-08-06"],
                },
                "library_refs": [],
                "rule_pack_refs": [],
                "target_mapping_metadata": {
                    "target_system_kind": "generic_downstream_modeling",
                    "target_mapping_refs": [ref("TargetMapping", "target-map:invented-del-08-06")],
                    "provenance": provenance("Invented target mapping metadata"),
                },
                "unsupported_behavior_flags": [
                    {
                        "flag_id": "unsupported:external-tool-not-invoked",
                        "behavior_label": "external_tool_not_invoked",
                        "status": "not_implemented",
                        "human_review_required": True,
                        "provenance": provenance("Invented unsupported target flag"),
                    }
                ],
                "unresolved_assumptions": [],
                "warnings": [],
                "diagnostics": [],
                "privacy": {
                    "classification": "invented_public_example",
                    "private_payload_embedded": False,
                    "protected_payload_embedded": False,
                },
                "review_classification": "machine_checked",
                "provenance": provenance("Invented handoff manifest"),
                "professional_boundary": boundary(),
            },
        }


    def export_workflow() -> dict[str, object]:
        return {
            "export_workflow_id": "export:invented-del-08-06",
            "source_handoff_package": handoff_package(),
            "export_payload": {
                "model_hash": checksum(ref("Model", "model:invented-del-08-06"), "model_hash", "sha256:invented-model"),
                "units_manifest": {
                    "unit_system_ref": ref("UnitSystem", "units:invented-del-08-06"),
                    "force_unit": "N",
                    "stress_unit": "Pa",
                },
                "entity_ids": {"component_ids": ["component:invented-pipe"]},
                "target_mapping_metadata": {
                    "target_system_kind": "generic_downstream_modeling",
                    "target_mapping_refs": [ref("TargetMapping", "target-map:invented-export")],
                },
                "unsupported_target_records": [
                    {
                        "record_id": "unsupported:invented-export-record",
                        "status": "not_implemented",
                        "human_review_required": True,
                        "private_payload": "private export data must not pass through",
                    }
                ],
                "unresolved_assumptions": [],
                "warnings": [],
            },
            "diagnostics": [],
            "privacy": {
                "classification": "invented_public_example",
                "private_payload_embedded": False,
                "protected_payload_embedded": False,
            },
            "professional_boundary": boundary(),
            "provenance": provenance("Invented export workflow"),
        }


    def external_prover_metadata() -> dict[str, object]:
        return {
            "metadata_record_id": "external-prover:invented-del-08-06",
            "handoff_package_refs": [ref("HandoffPackage", "handoff:invented-del-08-06")],
            "target_mapping_refs": [ref("TargetMapping", "target-map:invented-del-08-06")],
            "export_workflow_refs": [ref("ExportWorkflow", "export:invented-del-08-06")],
            "immutable_model_state_refs": [ref("ModelState", "state:invented-del-08-06")],
            "unsupported_target_flags": [
                {
                    "flag_id": "unsupported:external-prover-metadata-only",
                    "status": "metadata_only",
                    "human_review_required": True,
                }
            ],
            "assumptions": [],
            "warnings": [],
            "diagnostics": [],
            "professional_boundary": boundary(),
            "provenance": provenance("Invented external prover metadata"),
        }


    def section_kwargs() -> dict[str, object]:
        return {
            "section_set_id": "report-sections:invented-del-08-06",
            "model_states": [model_state()],
            "analysis_runs": [analysis_run()],
            "analysis_run_comparisons": [analysis_comparison()],
            "handoff_packages": [handoff_package()],
            "export_workflows": [export_workflow()],
            "external_prover_metadata": [external_prover_metadata()],
            "source_notes": ["invented public test fixture; no protected standards content"],
        }


    def test_sections_are_deterministic_and_represent_all_required_families():
        first = build_state_comparison_handoff_report_sections(**section_kwargs())
        second = build_state_comparison_handoff_report_sections(**deepcopy(section_kwargs()))

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-08-06"
        assert first["package_id"] == "PKG-08"
        assert {item["section_kind"] for item in first["sections"]["state_run_sections"]} == {
            "analysis_run_record",
            "model_state_record",
        }
        assert first["sections"]["comparison_sections"][0]["section_kind"] == "analysis_run_comparison"
        assert {item["section_kind"] for item in first["sections"]["handoff_sections"]} == {
            "export_workflow_record",
            "external_prover_metadata",
            "handoff_package_manifest",
        }


    def test_sections_preserve_ids_hashes_warnings_assumptions_units_and_review_state():
        record = build_state_comparison_handoff_report_sections(**section_kwargs())
        state_section = next(
            item
            for item in record["sections"]["state_run_sections"]
            if item["section_kind"] == "model_state_record"
        )
        run_section = next(
            item
            for item in record["sections"]["state_run_sections"]
            if item["section_kind"] == "analysis_run_record"
        )
        comparison_section = record["sections"]["comparison_sections"][0]
        handoff_section = next(
            item
            for item in record["sections"]["handoff_sections"]
            if item["section_kind"] == "handoff_package_manifest"
        )
        export_section = next(
            item
            for item in record["sections"]["handoff_sections"]
            if item["section_kind"] == "export_workflow_record"
        )
        external_section = next(
            item
            for item in record["sections"]["handoff_sections"]
            if item["section_kind"] == "external_prover_metadata"
        )

        assert state_section["state_ref"]["ref"] == "state:invented-del-08-06"
        assert state_section["hash_refs"][0]["value"] == "sha256:invented-state"
        assert state_section["warnings"][0]["code"] == "STATE-INVENTED-WARNING"
        assert state_section["assumptions"][0]["assumption_id"] == "assumption:invented-state-review"
        assert state_section["privacy_classification"] == "invented_public_example"
        assert state_section["review_state"] == "machine_checked"
        assert run_section["unit_context"] == ref("UnitSystem", "units:invented-del-08-06")
        assert run_section["rule_pack_refs"][0]["checksum"]["value"] == "sha256:invented-rule"
        assert comparison_section["unit_normalized_deltas"][0]["normalized_unit"] == "Pa"
        assert comparison_section["tolerance_profile_refs"] == ["tolerance:invented-review"]
        assert handoff_section["model_hash"]["value"] == "sha256:invented-model"
        assert handoff_section["unsupported_target_flags"][0]["human_review_required"] is True
        assert export_section["handoff_package_ref"]["ref"] == "handoff:invented-del-08-06"
        assert export_section["unsupported_target_records"][0]["human_review_required"] is True
        assert "private_payload" not in export_section["unsupported_target_records"][0]
        assert external_section["target_mapping_refs"][0] == ref("TargetMapping", "target-map:invented-del-08-06")


    def test_missing_source_values_become_explicit_findings_and_tbds():
        kwargs = section_kwargs()
        kwargs["analysis_runs"] = [analysis_run()]
        del kwargs["analysis_runs"][0]["analysis_run"]["unit_system_ref"]
        del kwargs["analysis_runs"][0]["analysis_run"]["provenance"]

        record = build_state_comparison_handoff_report_sections(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}

        assert "SCH-SOURCE-VALUE-MISSING" in codes
        assert any(item["severity"] == "warning" for item in record["diagnostics"])
        assert any("unit_context" in item["tbd_id"] for item in record["unresolved_tbds"])
        assert any("source_provenance" in item["tbd_id"] for item in record["unresolved_tbds"])


    def test_authority_claims_are_diagnosed_without_copying_claim_text():
        kwargs = section_kwargs()
        kwargs["model_states"] = [model_state()]
        kwargs["model_states"][0]["model_state"]["professional_boundary"]["software_makes_approval_claim"] = True
        kwargs["model_states"][0]["model_state"]["warnings"][0]["message"] = (
            "Software says code " + "compliant and cert" + "ified."
        )

        record = build_state_comparison_handoff_report_sections(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}
        text = canonical_json(record).lower()

        assert "SCH-SOFTWARE-AUTHORITY-FLAG-BLOCKED" in codes
        assert "SCH-AUTHORITY-CLAIM-REJECTED" in codes
        assert "software says code " + "compliant" not in text
        assert "omitted_prohibited_authority_or_reliance_claim" in text


    def test_disallowed_analysis_status_is_diagnosed_and_not_emitted():
        kwargs = section_kwargs()
        kwargs["analysis_runs"] = [analysis_run()]
        kwargs["analysis_runs"][0]["analysis_run"]["analysis_status"].append("HUMAN_APPROVED_FOR_PROJECT")

        record = build_state_comparison_handoff_report_sections(**kwargs)
        run_section = next(
            item
            for item in record["sections"]["state_run_sections"]
            if item["section_kind"] == "analysis_run_record"
        )
        codes = {item["code"] for item in record["diagnostics"]}
        text = canonical_json(record)

        assert "SCH-ANALYSIS-STATUS-BLOCKED" in codes
        assert "HUMAN_APPROVED_FOR_PROJECT" not in run_section["analysis_status"]
        assert "HUMAN_APPROVED_FOR_PROJECT" in text


    def test_external_prover_execution_claim_is_out_of_scope():
        kwargs = section_kwargs()
        kwargs["external_prover_metadata"] = [external_prover_metadata()]
        kwargs["external_prover_metadata"][0]["external_prover_executed"] = True

        record = build_state_comparison_handoff_report_sections(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}

        assert "SCH-EXTERNAL-PROVER-EXECUTION-OUT-OF-SCOPE" in codes


    def test_numeric_comparison_deltas_need_units_and_dimensions():
        kwargs = section_kwargs()
        kwargs["analysis_run_comparisons"] = [analysis_comparison()]
        del kwargs["analysis_run_comparisons"][0]["result_deltas"][0]["dimension"]

        record = build_state_comparison_handoff_report_sections(**kwargs)
        codes = {item["code"] for item in record["diagnostics"]}

        assert "SCH-COMPARISON-DELTA-UNIT-MISSING" in codes
        assert "SCH-NUMERIC-UNIT-METADATA-MISSING" in codes


    def test_boundary_flags_cannot_be_flipped_on_section_set():
        record = build_state_comparison_handoff_report_sections(**section_kwargs())
        mutated = deepcopy(record)
        mutated["professional_boundary"]["human_review_required"] = False
        mutated["professional_boundary"]["software_creates_professional_reliance_record"] = True

        codes = {item["code"] for item in diagnostics_for_report_sections(mutated)}

        assert "SCH-HUMAN-REVIEW-NOT-REQUIRED-BLOCKED" in codes
        assert "SCH-SOFTWARE-AUTHORITY-FLAG-BLOCKED" in codes


    def test_output_boundary_language_does_not_make_prohibited_claims_for_clean_sources():
        record = build_state_comparison_handoff_report_sections(**section_kwargs())
        text = canonical_json(record).lower()

        for forbidden in FORBIDDEN_OUTPUT_PHRASES:
            assert forbidden not in text
        assert record["professional_boundary"]["human_review_required"] is True
        assert record["professional_boundary"]["software_makes_compliance_claim"] is False
        assert record["professional_boundary"]["software_makes_certification_claim"] is False
        assert record["professional_boundary"]["software_makes_sealing_claim"] is False
        assert record["professional_boundary"]["software_makes_approval_claim"] is False
        assert record["professional_boundary"]["software_makes_authentication_claim"] is False


    def main():
        test_sections_are_deterministic_and_represent_all_required_families()
        test_sections_preserve_ids_hashes_warnings_assumptions_units_and_review_state()
        test_missing_source_values_become_explicit_findings_and_tbds()
        test_authority_claims_are_diagnosed_without_copying_claim_text()
        test_disallowed_analysis_status_is_diagnosed_and_not_emitted()
        test_external_prover_execution_claim_is_out_of_scope()
        test_numeric_comparison_deltas_need_units_and_dimensions()
        test_boundary_flags_cannot_be_flipped_on_section_set()
        test_output_boundary_language_does_not_make_prohibited_claims_for_clean_sources()


    if __name__ == "__main__":
        main()

## Component: tests/test_stress_neutral_export_package.py

    #!/usr/bin/env python3
    """Focused tests for DEL-17-06 stress-neutral CSV/JSON export packages."""

    from __future__ import annotations

    from copy import deepcopy
    import json
    from pathlib import Path
    import re
    import sys


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    TESTS_DIR = ROOT / "tests"
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from core.handoff.stress_neutral import (  # noqa: E402
        build_stress_neutral_export_package,
        canonical_json,
        render_stress_neutral_csv,
        write_stress_neutral_export_package,
    )
    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )


    SCHEMA_PATH = ROOT / "schemas" / "stress_neutral_export.schema.json"
    FIXTURE_PATH = ROOT / "fixtures" / "stress_neutral" / "invented" / "stress_neutral_export_package.json"
    CSV_FIXTURE_PATH = ROOT / "fixtures" / "stress_neutral" / "invented" / "stress_neutral_results.csv"
    SOURCE_PAYLOAD_PATH = ROOT / "fixtures" / "stress_neutral" / "invented" / "source_result_payload.json"
    SHA256_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")

    CSV_HEADER = (
        "result_id,canonical_ref,row_kind,result_family,load_case_ref,station_ref,"
        "component_ref,value,unit,dimension,correlation_status"
    )

    FORBIDDEN_PAYLOAD_TEXT = {
        "real client",
        "asme table",
        "b31j",
        "cert" + "ified by openpipestress",
        "code " + "compliant",
        "professional " + "acceptance",
    }


    def ref(object_type: str, value: str) -> dict[str, str]:
        return {"object_type": object_type, "ref": value}


    def load_json(path: Path) -> dict[str, object]:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)


    def source_payload() -> dict[str, object]:
        return {
            "export_id": "stress-neutral:invented-del-17-06",
            "source_result_ref": ref("ResultEnvelope", "result-envelope:invented-del-17-06"),
            "source_run_ref": ref("AnalysisRun", "run:invented-del-17-06"),
            "source_model_ref": ref("Model", "model:invented-del-17-06"),
            "source_hashes": [
                {
                    "algorithm": "sha256",
                    "canonicalization": "JCS_compatible_json_payload_hash",
                    "payload_ref": ref("ResultEnvelope", "result-envelope:invented-del-17-06"),
                    "payload_scope": "source_result_envelope",
                    "value": "sha256:" + "2" * 64,
                }
            ],
            "result_rows": [
                {
                    "result_id": "result:invented:force:P001:axial",
                    "canonical_ref": ref("Result", "result:invented:force:P001:axial"),
                    "row_kind": "result_value",
                    "result_family": "force",
                    "load_case_ref": ref("LoadCase", "load:invented:operating"),
                    "station_ref": ref("Station", "station:invented:P001:end-i"),
                    "component_ref": ref("PipeElement", "pipe:invented:001"),
                    "value": 12.5,
                    "unit": "N",
                    "dimension": "force",
                    "source_result_ref": ref("Result", "result:invented:force:P001:axial"),
                    "correlation_status": "canonical_id_map",
                },
                {
                    "result_id": "result:invented:stress:P001:sustained",
                    "canonical_ref": ref("Result", "result:invented:stress:P001:sustained"),
                    "row_kind": "result_value",
                    "result_family": "stress",
                    "load_case_ref": ref("LoadCase", "load:invented:sustained"),
                    "station_ref": ref("Station", "station:invented:P001:midspan"),
                    "component_ref": ref("PipeElement", "pipe:invented:001"),
                    "value": 3450.0,
                    "unit": "Pa",
                    "dimension": "stress",
                    "source_result_ref": ref("Result", "result:invented:stress:P001:sustained"),
                    "correlation_status": "canonical_id_map",
                },
            ],
            "stable_id_map": [
                {
                    "canonical_ref": ref("Result", "result:invented:force:P001:axial"),
                    "export_ref": ref("StressNeutralRow", "result:invented:force:P001:axial"),
                    "mapping_status": "mapped",
                    "loss_category": "exported",
                },
                {
                    "canonical_ref": ref("Result", "result:invented:stress:P001:sustained"),
                    "export_ref": ref("StressNeutralRow", "result:invented:stress:P001:sustained"),
                    "mapping_status": "mapped",
                    "loss_category": "exported",
                },
            ],
            "loss_report": [
                {
                    "loss_id": "loss:invented:stress-neutral-exported",
                    "category": "exported",
                    "severity": "info",
                    "affected_refs": [ref("ResultEnvelope", "result-envelope:invented-del-17-06")],
                    "target_artifact_ref": ref("StressNeutralExportPackage", "stress-neutral:invented-del-17-06"),
                    "reason": "Invented result rows exported to stress-neutral CSV/JSON for deterministic package testing.",
                    "source_basis_ref": ref("Deliverable", "DEL-17-02"),
                    "downstream_implication": "Does not define comparison pass/fail or professional reliance semantics.",
                }
            ],
        }


    def build_from_source() -> dict[str, object]:
        return build_stress_neutral_export_package(**source_payload())


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def check_jsonschema_validation():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        built = build_from_source()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(schema, fixture, schema_label=str(SCHEMA_PATH), instance_label=str(FIXTURE_PATH))
            assert validate_instance(
                schema,
                built,
                schema_label=str(SCHEMA_PATH),
                instance_label="build_stress_neutral_export_package output",
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_fixture_and_builder_validate_against_schema():
        check_jsonschema_validation()


    def test_builder_is_deterministic_and_preserves_members():
        first = build_from_source()
        second = build_from_source()

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-17-06"
        assert first["package_status"] == "stress_neutral_export_package"
        assert first["export_profile"]["comparison_semantics"] == "diagnostic_export_only_no_pass_fail"
        assert first["export_profile"]["unit_policy"] == "unit_and_dimension_required_per_row"
        member_roles = {item["member_role"] for item in first["manifest"]["package_members"]}
        assert member_roles == {
            "manifest",
            "csv_text",
            "result_rows",
            "unit_system_disclosure",
            "stable_id_map",
            "loss_report",
            "validation_report",
            "diagnostics",
        }
        assert first["unit_system_disclosure"]["unit_system_ref"]["ref"] == "unit-system:dec-018-si-dual-display"
        assert first["unit_system_disclosure"]["result_units"] == ["N", "Pa"]
        assert first["unit_system_disclosure"]["conversion_performed"] is False
        assert first["unit_system_disclosure"]["protected_content_included"] is False
        assert all(SHA256_PATTERN.match(item["value"]) for item in first["manifest"]["checksums"])
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]


    def test_csv_and_json_rows_are_synchronized_and_ascii_safe():
        package = build_from_source()
        text = package["csv_text"]

        assert text == render_stress_neutral_csv(package["result_rows"])
        assert text == CSV_FIXTURE_PATH.read_text(encoding="ascii")
        assert text.splitlines()[0] == CSV_HEADER
        text.encode("ascii")
        assert "result:invented:force:P001:axial" in text
        assert "result:invented:stress:P001:sustained" in text
        assert {row["unit"] for row in package["result_rows"]} == {"N", "Pa"}
        assert {row["dimension"] for row in package["result_rows"]} == {"force", "stress"}


    def test_missing_units_stable_ids_and_loss_report_are_blocking():
        payload = source_payload()
        rows = deepcopy(payload["result_rows"])
        rows[0]["unit"] = ""

        package = build_stress_neutral_export_package(
            export_id="stress-neutral:blocked",
            source_result_ref=payload["source_result_ref"],
            source_run_ref=payload["source_run_ref"],
            source_model_ref=payload["source_model_ref"],
            source_hashes=payload["source_hashes"],
            result_rows=rows,
            stable_id_map=[],
            loss_report=[],
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"SN-UNIT-DIMENSION-MISSING", "SN-STABLE-ID-MAP-MISSING", "SN-LOSS-REPORT-MISSING"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["validation_report"]["validation_status"] == "blocked"


    def test_privacy_and_authority_boundary_diagnostics_are_blocking():
        payload = source_payload()
        package = build_stress_neutral_export_package(
            export_id="stress-neutral:privacy-boundary",
            source_result_ref=payload["source_result_ref"],
            source_run_ref=payload["source_run_ref"],
            source_model_ref=payload["source_model_ref"],
            source_hashes=payload["source_hashes"],
            result_rows=payload["result_rows"],
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
            export_profile={"free_metadata": {"unsafe_label": "cert" + "ified comparison export"}},
            privacy={"protected_payload_embedded": True},
        )

        codes = {item["code"] for item in package["diagnostics"]}
        assert {"SN-PRIVACY-BOUNDARY-VIOLATION", "SN-PROFILE-AUTHORITY-TERM"} <= codes
        assert any(item["severity"] == "blocking" for item in package["diagnostics"])
        assert package["professional_boundary"]["software_makes_compliance_claim"] is False
        assert package["professional_boundary"]["software_creates_professional_reliance_record"] is False


    def test_source_basis_refs_cover_result_export_run_and_comparison_contracts():
        package = build_from_source()
        refs = {
            (item["object_type"], item["ref"])
            for item in package["export_profile"]["source_basis_refs"]
        }

        assert {
            ("Deliverable", "DEL-08-04"),
            ("Deliverable", "DEL-14-02"),
            ("Deliverable", "DEL-14-05"),
            ("Deliverable", "DEL-17-02"),
        } <= refs

        payload = source_payload()
        unsafe = build_stress_neutral_export_package(
            export_id="stress-neutral:missing-source-basis",
            source_result_ref=payload["source_result_ref"],
            source_run_ref=payload["source_run_ref"],
            source_model_ref=payload["source_model_ref"],
            source_hashes=payload["source_hashes"],
            result_rows=payload["result_rows"],
            stable_id_map=payload["stable_id_map"],
            loss_report=payload["loss_report"],
            export_profile={"source_basis_refs": [ref("Deliverable", "DEL-17-02")]},
        )

        assert "SN-SOURCE-BASIS-REFS-MISSING" in {item["code"] for item in unsafe["diagnostics"]}
        assert unsafe["validation_report"]["validation_status"] == "blocked"


    def test_writer_outputs_csv_and_sidecars(tmp_path):
        package = build_from_source()

        write_stress_neutral_export_package(tmp_path, package)

        assert (tmp_path / "stress_neutral_results.csv").read_text(encoding="ascii") == package["csv_text"]
        assert load_json(tmp_path / "manifest.json") == package["manifest"]
        assert load_json(tmp_path / "result_rows.json") == package["result_rows"]
        assert load_json(tmp_path / "stable_id_map.json") == package["stable_id_map"]
        assert load_json(tmp_path / "loss_report.json") == package["loss_report"]
        assert load_json(tmp_path / "validation_report.json") == package["validation_report"]
        assert load_json(tmp_path / "diagnostics.json") == package["diagnostics"]


    def test_fixtures_contain_no_private_or_protected_payload_text():
        text = "\n".join(
            walk_strings(
                {
                    "package": load_json(FIXTURE_PATH),
                    "source": load_json(SOURCE_PAYLOAD_PATH),
                    "csv": CSV_FIXTURE_PATH.read_text(encoding="ascii"),
                }
            )
        ).lower()
        for forbidden in FORBIDDEN_PAYLOAD_TEXT:
            assert forbidden not in text


    def main():
        check_jsonschema_validation()
        test_builder_is_deterministic_and_preserves_members()
        test_csv_and_json_rows_are_synchronized_and_ascii_safe()
        test_missing_units_stable_ids_and_loss_report_are_blocking()
        test_privacy_and_authority_boundary_diagnostics_are_blocking()
        test_source_basis_refs_cover_result_export_run_and_comparison_contracts()
        test_fixtures_contain_no_private_or_protected_payload_text()


    if __name__ == "__main__":
        main()

## Component: tests/test_target_mapping_contract.py

    #!/usr/bin/env python3
    """Focused tests for DEL-15-02 target mapping contract."""

    from __future__ import annotations

    import json
    import sys
    from pathlib import Path

    from jsonschema import Draft202012Validator


    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    SCHEMA_PATH = ROOT / "schemas" / "target_mapping.schema.json"

    from core.handoff.target_mapping import (  # noqa: E402
        build_target_mapping_contract,
        canonical_json,
        diagnostics_for_target_mapping_contract,
    )


    def ref(object_type, value):
        return {"object_type": object_type, "ref": value}


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def validate_contract(contract):
        schema = load_schema()
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(contract), key=lambda item: item.path)
        assert not errors, [error.message for error in errors]


    def source_context():
        return {
            "model_hash": {
                "algorithm": "sha256",
                "value": "invented-hash",
                "payload_ref": ref("Model", "model:invented"),
            },
            "units_manifest_ref": ref("ExternalReference", "units:invented"),
            "entity_id_refs": [ref("Component", "component:pipe-1")],
            "library_refs": [ref("ExternalReference", "library:public-metadata")],
            "rule_pack_refs": [ref("ExternalReference", "rule-pack:metadata-only")],
            "unresolved_assumption_refs": [ref("Diagnostic", "assumption:review")],
            "warning_refs": [ref("Diagnostic", "warning:handoff")],
            "privacy_context": {
                "private_payload_redacted": True,
                "privacy_classification": "public_metadata",
            },
        }


    def mapping_record():
        return {
            "mapping_id": "mapping:pipe-diameter",
            "mapping_kind": "field",
            "source_ref": ref("Component", "component:pipe-1"),
            "target_ref": ref("ExternalReference", "target:pipe-diameter"),
            "value_kind": "quantity",
            "unit_metadata": {"unit": "mm", "dimension": "length"},
            "mapping_status": "mapped",
            "assumption_refs": [],
            "warning_refs": [],
        }


    def unsupported_flag():
        return {
            "flag_id": "unsupported:mesh",
            "behavior_label": "mesh_generation_not_performed",
            "status": "not_implemented",
            "target_ref": ref("ExternalReference", "target:mesh"),
            "affected_refs": [ref("Model", "model:invented")],
        }


    def test_contract_is_deterministic_and_preserves_handoff_context():
        first = build_target_mapping_contract(
            mapping_contract_id="tm:invented",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:generic"),
            source_context=source_context(),
            mapping_records=[mapping_record()],
            unsupported_behaviors=[unsupported_flag()],
        )
        second = build_target_mapping_contract(
            mapping_contract_id="tm:invented",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:generic"),
            source_context=source_context(),
            mapping_records=[mapping_record()],
            unsupported_behaviors=[unsupported_flag()],
        )

        assert canonical_json(first) == canonical_json(second)
        assert first["deliverable_id"] == "DEL-15-02"
        assert first["source_context"]["model_hash"]["value"] == "invented-hash"
        assert first["source_context"]["units_manifest_ref"]["ref"] == "units:invented"
        assert first["unsupported_behavior_flags"][0]["human_review_required"] is True
        assert not [item for item in first["diagnostics"] if item["severity"] == "blocking"]
        validate_contract(first)


    def test_unit_bearing_mapping_without_unit_metadata_is_blocked():
        broken = mapping_record()
        broken["unit_metadata"] = None
        contract = build_target_mapping_contract(
            mapping_contract_id="tm:unit-missing",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:generic"),
            source_context=source_context(),
            mapping_records=[broken],
        )

        codes = {item["code"] for item in contract["diagnostics"]}
        assert "TM-UNIT-METADATA-MISSING" in codes
        assert any(item["severity"] == "blocking" for item in contract["diagnostics"])
        validate_contract(contract)


    def test_missing_context_and_untraceable_behavior_emit_diagnostics():
        contract = build_target_mapping_contract(
            mapping_contract_id="tm:missing-context",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:generic"),
            source_context={},
            mapping_records=[],
            unsupported_behaviors=[{"flag_id": "unsupported:untraced"}],
        )

        codes = {item["code"] for item in diagnostics_for_target_mapping_contract(contract)}
        assert "TM-SOURCE-CONTEXT-FIELD-MISSING" in codes
        assert "TM-AFFECTED-REFS-MISSING" in codes
        validate_contract(contract)


    def test_behavior_label_authority_wording_is_blocking_boundary_diagnostic():
        flagged = unsupported_flag()
        flagged["behavior_label"] = "cert" + "ified_by_target"

        contract = build_target_mapping_contract(
            mapping_contract_id="tm:authority-label",
            target_system_kind="generic_downstream_modeling",
            target_ref=ref("ExternalReference", "target:generic"),
            source_context=source_context(),
            mapping_records=[mapping_record()],
            unsupported_behaviors=[flagged],
        )

        codes = {item["code"] for item in contract["diagnostics"]}
        assert "TM-PROHIBITED-AUTHORITY-TERM" in codes
        assert any(item["severity"] == "blocking" for item in contract["diagnostics"])
        validate_contract(contract)


    def test_output_boundary_language_does_not_make_prohibited_claims():
        contract = build_target_mapping_contract(
            mapping_contract_id="tm:boundary",
            target_system_kind="TBD",
            target_ref=ref("ExternalReference", "target:tbd"),
            source_context=source_context(),
            mapping_records=[mapping_record()],
        )
        text = canonical_json(contract).lower()

        for forbidden in [
            "code compliant",
            "certified",
            "sealed",
            "authenticated",
            "professional approval",
            "external validation",
        ]:
            assert forbidden not in text
        assert contract["professional_boundary"]["software_makes_compliance_claim"] is False


    def main():
        test_contract_is_deterministic_and_preserves_handoff_context()
        test_unit_bearing_mapping_without_unit_metadata_is_blocked()
        test_missing_context_and_untraceable_behavior_emit_diagnostics()
        test_behavior_label_authority_wording_is_blocking_boundary_diagnostic()
        test_output_boundary_language_does_not_make_prohibited_claims()


    if __name__ == "__main__":
        main()

## Component: tests/test_units_schema.py

    #!/usr/bin/env python3
    """Stdlib checks for the unit system schema."""

    import json
    import sys
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    TESTS_DIR = Path(__file__).resolve().parent
    if str(TESTS_DIR) not in sys.path:
        sys.path.insert(0, str(TESTS_DIR))

    from schema_validation import (  # noqa: E402
        JsonSchemaDependencyMissing,
        validate_instance,
        validate_schema_document,
    )

    SCHEMA_PATH = ROOT / "schemas" / "units.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "units" / "invented_unit_contract_fixture.json"

    CANONICAL_DIMENSIONS = [
        "dimensionless",
        "length",
        "mass",
        "time",
        "temperature",
        "temperature_interval",
        "angle",
        "rotation",
        "force",
        "force_per_length",
        "moment",
        "pressure",
        "stress",
        "area",
        "volume",
        "density",
        "linear_stiffness",
        "rotational_stiffness",
        "displacement",
        "velocity",
        "acceleration",
        "thermal_conductivity",
        "specific_heat",
        "thermal_expansion_coefficient",
        "second_moment_area",
        "section_modulus",
        "mass_per_length",
        "volume_per_length",
        "slope",
        "TBD",
    ]

    RETIRED_DIMENSIONS = {
        "temperature_difference",
        "area_moment",
        "stiffness",
    }

    REQUIRED_QUANTITY_FIELDS = {
        "quantity_id",
        "quantity_kind",
        "magnitude",
        "unit_ref",
        "dimension_id",
        "unit_required",
        "missing_unit_behavior",
        "provenance",
    }

    FORBIDDEN_DEFAULT_TERMS = {
        "assume zero",
        "assumed zero",
        "assume unity",
        "assumed unity",
        "defaults to",
        "default value",
        "fallback default",
        "implicit default",
        "silently",
    }


    def load_schema():
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            return json.load(schema_file)


    def load_fixture():
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            return json.load(fixture_file)


    def walk_strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                yield from walk_strings(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_strings(item)


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def check_schema_contract():
        schema = load_schema()
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))

        required_root = {
            "schema_version",
            "unit_system",
            "dimension_records",
            "quantity_records",
            "conversion_declarations",
            "dimension_checks",
            "operation_rules",
            "test_obligations",
            "open_decisions",
            "diagnostics",
        }
        assert required_root <= set(schema["required"])

        dimensions = defs["DimensionId"]["enum"]
        assert dimensions == CANONICAL_DIMENSIONS
        assert not (set(dimensions) & RETIRED_DIMENSIONS)

        vector = defs["DimensionVector"]
        assert {
            "length",
            "mass",
            "time",
            "temperature",
            "angle",
            "electric_current",
            "substance_amount",
            "luminous_intensity",
        } <= set(vector["required"])

        quantity = defs["QuantityRecord"]
        assert REQUIRED_QUANTITY_FIELDS <= set(quantity["required"])
        assert quantity["additionalProperties"] is False
        assert quantity["properties"]["missing_unit_behavior"]["enum"] == [
            "diagnostic_blocking",
            "diagnostic_warning",
            "not_applicable_explicit_dimensionless",
            "TBD",
        ]

        conversion = defs["ConversionDeclaration"]
        assert {
            "conversion_id",
            "source_unit_ref",
            "target_unit_ref",
            "dimension_id",
            "transform_kind",
            "factor_representation",
            "provenance",
            "review_status",
        } <= set(conversion["required"])

        operation = defs["OperationRule"]
        assert {
            "operation",
            "compatibility_rule",
            "unsupported_behavior",
            "diagnostic_codes",
            "review_status",
        } <= set(operation["required"])
        assert {
            "same_dimension_required",
            "derived_dimension_required",
            "explicit_dimensionless_classification_required",
            "unsupported_until_decision",
        } <= set(operation["properties"]["compatibility_rule"]["enum"])
        assert {
            "addition",
            "subtraction",
            "comparison",
            "conversion",
            "multiplication",
            "division",
            "power",
            "dimensionless_classification",
            "import_validation",
            "export_validation",
            "rule_evaluation",
        } <= set(operation["properties"]["operation"]["enum"])

        test_obligation = defs["TestObligation"]
        assert {
            "test_id",
            "test_kind",
            "required_for",
            "fixture_data_policy",
            "gating_status",
            "evidence_ref",
        } <= set(test_obligation["required"])
        assert "conversion_gated_pending_constants" in test_obligation["properties"]["test_kind"]["enum"]
        assert (
            "no_numeric_conversion_constants_until_approved"
            in test_obligation["properties"]["fixture_data_policy"]["enum"]
        )
        assert "blocked_pending_decision" in test_obligation["properties"]["gating_status"]["enum"]

        open_decision = defs["OpenDecision"]
        assert {
            "decision_id",
            "topic",
            "status",
            "blocking_scope",
            "required_before",
            "owner",
            "notes",
        } <= set(open_decision["required"])
        assert {
            "unit_catalog",
            "base_dimension_vector",
            "dimensionless_classification",
            "conversion_tolerance_policy",
            "offset_temperature_semantics",
            "gauge_absolute_pressure_semantics",
            "diagnostic_code_namespace",
        } <= set(open_decision["properties"]["topic"]["enum"])

        diagnostic_codes = set(defs["UnitDiagnosticCode"]["enum"])
        assert {
            "UNIT_MISSING",
            "UNIT_UNKNOWN",
            "UNIT_AMBIGUOUS",
            "DIMENSION_MISMATCH",
            "CONVERSION_UNSUPPORTED",
            "DIMENSIONLESS_CLASSIFICATION_REQUIRED",
            "PROTECTED_UNIT_DATA_SUSPECTED",
            "CONVERSION_TEST_GATED",
        } <= diagnostic_codes
        assert defs["UnitDiagnostic"]["properties"]["code"]["$ref"] == "#/$defs/UnitDiagnosticCode"

        all_text = "\n".join(walk_strings(schema)).lower()
        for forbidden in FORBIDDEN_DEFAULT_TERMS:
            assert forbidden not in all_text


    def check_unit_fixture():
        schema = load_schema()
        fixture = load_fixture()

        assert set(schema["required"]) <= set(fixture)
        assert set(fixture["unit_system"]) >= required_at(schema, "UnitSystemRecord")
        assert fixture["unit_system"]["storage_convention"] == "entered_units_preserved"
        assert fixture["dimension_records"]
        assert {item["dimension_id"] for item in fixture["dimension_records"]} >= {
            "length",
            "force",
        }

        quantity = fixture["quantity_records"][0]
        assert required_at(schema, "QuantityRecord") <= set(quantity)
        assert quantity["unit_required"] is True
        assert quantity["missing_unit_behavior"] == "diagnostic_blocking"

        diagnostic_codes = {item["code"] for item in fixture["diagnostics"]}
        assert "UNIT_MISSING" in diagnostic_codes
        assert fixture["dimension_checks"][0]["outcome"] == "blocked"
        diagnostic_items = schema["$defs"]["DimensionCheckRecord"]["properties"]["diagnostics"][
            "items"
        ]
        assert {"oneOf"} <= set(diagnostic_items)
        assert any(
            item.get("$ref") == "#/$defs/Reference" for item in diagnostic_items["oneOf"]
        )
        assert fixture["dimension_checks"][0]["diagnostics"][0] == {
            "ref_type": "UnitDiagnostic",
            "ref_id": "unit-diagnostic:missing-unit",
        }

        operation_kinds = {item["operation"] for item in fixture["operation_rules"]}
        assert {"addition", "conversion", "rule_evaluation"} <= operation_kinds

        open_topics = {item["topic"] for item in fixture["open_decisions"]}
        assert {
            "unit_catalog",
            "conversion_tolerance_policy",
            "canonical_calculation_basis",
            "offset_temperature_semantics",
            "gauge_absolute_pressure_semantics",
        } <= open_topics
        assert {item["status"] for item in fixture["open_decisions"]} == {"open_TBD"}

        gated_tests = {
            item["test_kind"]: item for item in fixture["test_obligations"]
        }
        assert gated_tests["conversion_gated_pending_constants"]["gating_status"] == (
            "blocked_pending_decision"
        )
        assert fixture["conversion_declarations"][0]["transform_kind"] == "unsupported_TBD"


    def check_jsonschema_validation():
        schema = load_schema()
        fixture = load_fixture()
        try:
            assert validate_schema_document(schema, schema_label=str(SCHEMA_PATH))
            assert validate_instance(
                schema,
                fixture,
                schema_label=str(SCHEMA_PATH),
                instance_label=str(FIXTURE_PATH),
            )
        except JsonSchemaDependencyMissing as exc:
            _skip_or_note_missing_jsonschema(exc)


    def _skip_or_note_missing_jsonschema(exc):
        if "pytest" in sys.modules:
            import pytest

            pytest.skip(str(exc))
        print(f"SKIP: {exc}")


    def test_units_schema_contract():
        check_schema_contract()


    def test_unit_fixture_preserves_missing_unit_diagnostics_and_tbd_gates():
        check_unit_fixture()


    def test_unit_schema_jsonschema_validation_helper():
        check_jsonschema_validation()


    def main():
        check_schema_contract()
        check_unit_fixture()
        check_jsonschema_validation()


    if __name__ == "__main__":
        main()

## Component: tests/test_user_guide_status_wording.py

    #!/usr/bin/env python3
    """Focused checks for DEL-11-01 user-guide analysis status wording."""

    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    USER_GUIDE = ROOT / "docs" / "user_guide" / "index.md"


    def test_user_guide_lists_external_human_approval_status_without_software_claim():
        text = USER_GUIDE.read_text(encoding="utf-8")
        lower = text.lower()

        assert "`HUMAN_APPROVED_FOR_PROJECT`" in text
        assert "external human acceptance record" in lower
        assert "exact reviewed hashes" in lower
        assert "not emitted by the solver or rule-pack evaluator" in lower
        assert "not software approval" in lower
        assert "not software approval, certification, sealing, authentication, or code-compliance determination" in lower


    if __name__ == "__main__":
        test_user_guide_lists_external_human_approval_status_without_software_claim()

## Component: tests/test_viewport_editor_contract.py

    #!/usr/bin/env python3
    """Stdlib checks for the viewport editor schema and invented fixture."""

    import json
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]
    SCHEMA_PATH = ROOT / "schemas" / "viewport_editor.schema.yaml"
    FIXTURE_PATH = ROOT / "fixtures" / "gui" / "invented" / "viewport_editor_session.json"

    REQUIRED_ROOT = {
        "schema_version",
        "deliverable_id",
        "package_id",
        "scope_item",
        "objectives",
        "viewport_status",
        "viewport_session",
    }

    REQUIRED_DEFS = {
        "CameraState",
        "CommandIntent",
        "CommandType",
        "DiagnosticClass",
        "DiagnosticSeverity",
        "InteractionState",
        "Point3",
        "PrivacyClassification",
        "ProfessionalBoundary",
        "Provenance",
        "RedistributionStatus",
        "Reference",
        "ReviewStatus",
        "Vector3",
        "ViewGeometry",
        "ViewPrimitive",
        "ViewPrimitiveType",
        "ViewportDiagnostic",
        "ViewportDiagnosticCode",
        "ViewportSession",
        "ViewportStatus",
        "ViewportTool",
    }

    REQUIRED_PRIMITIVES = {
        "node",
        "pipe_run",
        "bend_arc",
        "branch_symbol",
        "valve_symbol",
        "flange_symbol",
        "reducer_symbol",
        "expansion_joint_symbol",
        "support_symbol",
    }

    REQUIRED_COMMANDS = {
        "create_node",
        "connect_pipe_run",
        "insert_bend",
        "insert_branch_symbol",
        "insert_component_symbol",
        "select_entities",
        "clear_selection",
    }

    REQUIRED_DIAGNOSTIC_CLASSES = {
        "SOLVE_BLOCKING",
        "RULE_CHECK_BLOCKING",
        "PROVENANCE_WARNING",
        "ASSUMPTION_WARNING",
        "NONLINEAR_WARNING",
        "IP_BOUNDARY_WARNING",
        "UNIT_WARNING",
        "GUI_STATE_WARNING",
    }

    FORBIDDEN_FIXTURE_TERMS = {
        "ASME",
        "B31",
        "B31J",
        "allowable stress table",
        "stress intensification factor table",
        "vendor catalog value",
        "real secret",
        "code compliant",
        "certified",
        "sealed",
    }


    def load_json(path):
        with path.open(encoding="utf-8") as json_file:
            return json.load(json_file)


    def required_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["required"])


    def enum_at(schema, definition_name):
        return set(schema["$defs"][definition_name]["enum"])


    def walk_keys(value):
        if isinstance(value, dict):
            for key, item in value.items():
                yield key
                yield from walk_keys(item)
        elif isinstance(value, list):
            for item in value:
                yield from walk_keys(item)


    def main():
        schema = load_json(SCHEMA_PATH)
        fixture = load_json(FIXTURE_PATH)
        defs = schema["$defs"]

        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["additionalProperties"] is False
        assert "default" not in set(walk_keys(schema))
        assert REQUIRED_ROOT <= set(schema["required"])
        assert REQUIRED_DEFS <= set(defs)

        assert schema["properties"]["deliverable_id"]["const"] == "DEL-07-01"
        assert schema["properties"]["package_id"]["const"] == "PKG-07"
        assert schema["properties"]["scope_item"]["const"] == "SOW-020"
        assert schema["properties"]["objectives"]["contains"]["const"] == "OBJ-006"

        status = defs["ViewportStatus"]["properties"]
        assert status["frontend_app_shell"]["const"] == "TBD"
        assert status["viewport_renderer"]["const"] == "Three_js_runtime_integration_TBD"
        assert status["durable_state_mutation"]["const"] == (
            "application_service_command_intents_only"
        )
        assert status["transient_state_policy"]["const"] == (
            "camera_hover_selection_drag_snap_are_not_persisted_project_payload"
        )
        assert status["command_transport"]["const"] == "TBD"
        assert status["dependency_versions"]["const"] == "TBD"

        boundary_required = required_at(schema, "ProfessionalBoundary")
        assert {
            "human_review_required",
            "software_makes_compliance_claim",
            "software_makes_certification_claim",
            "software_makes_sealing_claim",
            "software_makes_approval_claim",
            "software_makes_authentication_claim",
        } <= boundary_required
        boundary = defs["ProfessionalBoundary"]["properties"]
        assert boundary["human_review_required"]["const"] is True
        for field in boundary_required - {"human_review_required"}:
            assert boundary[field]["const"] is False

        assert REQUIRED_PRIMITIVES <= enum_at(schema, "ViewPrimitiveType")
        assert REQUIRED_COMMANDS <= enum_at(schema, "CommandType")
        assert REQUIRED_DIAGNOSTIC_CLASSES <= enum_at(schema, "DiagnosticClass")
        assert {
            "VIEWPORT_UNIT_MISMATCH",
            "VIEWPORT_COMMAND_REQUIRES_SERVICE_VALIDATION",
            "VIEWPORT_COMPONENT_DATA_MISSING",
            "VIEWPORT_PROTECTED_CONTENT_SUSPECTED",
            "VIEWPORT_TRANSIENT_STATE_NOT_PERSISTED",
        } <= enum_at(schema, "ViewportDiagnosticCode")

        command_required = required_at(schema, "CommandIntent")
        assert {
            "intent_id",
            "command_type",
            "target_ref",
            "payload_refs",
            "unit_policy",
            "reversible",
            "validation_state",
            "diagnostic_refs",
            "provenance",
        } <= command_required
        assert (
            defs["CommandIntent"]["properties"]["unit_policy"]["const"]
            == "unit_aware_domain_validation_required"
        )

        assert fixture["deliverable_id"] == "DEL-07-01"
        assert fixture["viewport_status"]["frontend_app_shell"] == "TBD"
        assert (
            fixture["viewport_status"]["durable_state_mutation"]
            == "application_service_command_intents_only"
        )
        assert fixture["viewport_status"]["professional_boundary"][
            "software_makes_compliance_claim"
        ] is False
        assert fixture["viewport_session"]["interaction_state"]["active_tool"] == (
            "connect_pipe_run"
        )
        assert fixture["viewport_session"]["view_primitives"][0]["primitive_type"] == (
            "node"
        )
        assert fixture["viewport_session"]["view_primitives"][1]["primitive_type"] == (
            "pipe_run"
        )
        assert fixture["viewport_session"]["command_intents"][0]["validation_state"] == (
            "pending_service_validation"
        )
        assert fixture["viewport_session"]["command_intents"][0]["unit_policy"] == (
            "unit_aware_domain_validation_required"
        )
        assert fixture["viewport_session"]["diagnostics"][0]["class"] == "GUI_STATE_WARNING"
        assert fixture["viewport_session"]["provenance"]["redistribution_status"] == (
            "invented_non_engineering_example"
        )
        assert fixture["viewport_session"]["provenance"]["privacy_classification"] == (
            "invented_public_example"
        )

        fixture_text = FIXTURE_PATH.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_FIXTURE_TERMS:
            assert forbidden.lower() not in fixture_text.lower()


    def test_viewport_editor_contract_main():
        main()


    if __name__ == "__main__":
        main()
