"""I101 lane T: the carrier-schema mutants, one per new schema check (B3-D §7; REVISION_01 §6). Each replaces exactly
one occurrence in a schema of the TS head; killed by the PY schema tests (test_retained_precision_schema,
test_source_block_schema_contract, test_results_dispatcher_v0_3, which validates the committed exact goldens)."""
R = "schemas/results.v0.3.schema.yaml"
A = "schemas/analysis_run.v0.3.schema.json"
N = "schemas/stress_neutral_export.v0.3.schema.json"
X = "c4987e874889645ac315b5f55f58690082ad5e7745527f20e3e316efa3e70a3d"
SUCC_SHA = "b2b4a54d610aa38c66f5d31921c2d8f3113313e33eb6933e45093ba6f1e3667c"
EXACT = "openpipestress.result_semantics/0.3.0/physics-retained-1"
M = [
 ("R1", "results: the exact branch does not require the receipt", R,
  '"required": [\n            "contract_evidence",\n            "retained_precision"\n          ],\n          "properties": {\n            "producer": {\n              "properties": {\n                "semantic_contract_id": {\n                  "const": "' + EXACT + '"',
  '"required": [\n            "contract_evidence"\n          ],\n          "properties": {\n            "producer": {\n              "properties": {\n                "semantic_contract_id": {\n                  "const": "' + EXACT + '"'),
 ("R2", "results: the exact branch admits source_block_recovery", R,
  '"$ref": "retained_precision_mp_v2.schema.json"\n            }\n          },\n          "not": {\n            "anyOf": [\n              {\n                "required": [\n                  "source_block_recovery"\n                ]\n              }\n            ]\n          }\n        }\n      ]\n    },',
  '"$ref": "retained_precision_mp_v2.schema.json"\n            }\n          }\n        }\n      ]\n    },'),
 ("R3", "results: the profile enum without the exact profile (CARRIER_PROFILE_ENUMS)", R,
  '"product_preview_retained_w1a_v2",\n                "exact_straight_retained_w1a_v2"\n              ]',
  '"product_preview_retained_w1a_v2"\n              ]'),
 ("R4", "results: the producer identity enum without the exact id", R,
  '"openpipestress.result_semantics/0.3.0/preview-physics-retained-1",\n                "' + EXACT + '"\n              ]\n            }\n          }\n        },\n        "semantic_contract_ref"',
  '"openpipestress.result_semantics/0.3.0/preview-physics-retained-1"\n              ]\n            }\n          }\n        },\n        "semantic_contract_ref"'),
 ("R5", "results: the exact branch's first limitation edited", R,
  '"Small-displacement homogeneous-isotropic straight circular members with explicit common E/nu selection; G is derived, and source OD/effective wall define the section.",',
  '"Small-displacement homogeneous-isotropic straight circular members with explicit common E/nu selection; G is derived.",'),
 ("A1", "analysis_run: the SemanticContract sha256 enum without XTABLE's hash", A,
  '"' + SUCC_SHA + '",\n            "' + X + '"\n          ]', '"' + SUCC_SHA + '"\n          ]'),
 ("A2", "analysis_run: the exact id paired with the preview successor's hash", A,
  '"const": "' + EXACT + '"\n            },\n            "sha256": {\n              "const": "' + X + '"',
  '"const": "' + EXACT + '"\n            },\n            "sha256": {\n              "const": "' + SUCC_SHA + '"'),
 ("A3", "analysis_run: the exact branch does not require the receipt", A,
  '{\n          "required": [\n            "retained_precision"\n          ],\n          "properties": {\n            "reproducibility": {\n              "properties": {\n                "semantic_contract": {\n                  "properties": {\n                    "id": {\n                      "const": "' + EXACT + '"',
  '{\n          "properties": {\n            "reproducibility": {\n              "properties": {\n                "semantic_contract": {\n                  "properties": {\n                    "id": {\n                      "const": "' + EXACT + '"'),
 ("A4", "analysis_run: the exact branch admits contract_evidence", A,
  '"source_block_recovery"\n                ]\n              },\n              {\n                "required": [\n                  "contract_evidence"\n                ]\n              }\n            ]\n          }\n        }\n      ]',
  '"source_block_recovery"\n                ]\n              }\n            ]\n          }\n        }\n      ]'),
 ("N1", "stress_neutral: the profile enum without the exact profile (CARRIER_PROFILE_ENUMS)", N,
  '"product_preview_retained_w1a_v2",\n            "exact_straight_retained_w1a_v2"\n          ]',
  '"product_preview_retained_w1a_v2"\n          ]'),
 ("N2", "stress_neutral: the exact branch reads the preview evidence", N,
  '"const": "exact_straight_retained_w1a_v2"\n            }\n          }\n        },\n        "contract_evidence": {\n          "$ref": "#/$defs/PhysicsContractEvidence"',
  '"const": "exact_straight_retained_w1a_v2"\n            }\n          }\n        },\n        "contract_evidence": {\n          "$ref": "#/$defs/PreviewPhysicsContractEvidence"'),
 ("N3", "stress_neutral: the exact branch's table hash is the preview successor's", N,
  '"const": "' + EXACT + '"\n            },\n            "sha256": {\n              "const": "' + X + '"',
  '"const": "' + EXACT + '"\n            },\n            "sha256": {\n              "const": "' + SUCC_SHA + '"'),
]
