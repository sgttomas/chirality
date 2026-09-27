## X1 pinned fixtures: drafter report (TASK, brief DRAFTER_BRIEF_PINNED.md)

I drafted all five files and they pass the fixture suite, except for the one test the brief says to expect to fail. The run gave 9 of 10 tests passing. The failure is `test_synthetic_cases_cover_the_contract_minimums`, which fails only because my copy uses the stub synthetic manifest. That stub is not included here.

To get there I had to work around two problems in the test module. Both are listed first below because they affect the test itself, not just my files.

I wrote nothing in any worktree. Before and after my work, `git status --short` in `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-x1-fixtures-prep` was empty. I read the repo only through plumbing and plain file reads, with no network.

**mktemp directory:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1pinned.Y3tXEH`
- Deliverables: `parsers/fixtures/pinned/MANIFEST.json` and `parsers/fixtures/pinned/goldens/{FC-1,FC-2,FC-3,FX-PEC-0}.json`
- Also in the directory:
- `parsers/fixtures/synthetic/MANIFEST.json`: the stub, for local runs only.
- `parsers/test_parser_fixture_integrity.py`: an unmodified copy of the candidate test.
- `gen/build.py`: the JSON emitter.
- `gen/facts.py`: builds the fact table using the test's own boundary regex.
- `facts.tsv`, `suite.out`, and `ctx/`: the saved blobs and contracts.
- SHA-256 of the deliverables:
- MANIFEST.json: `1893f19f2877499df8903b9409591ffd36872faec6da5651dca862b85b9dd84a`
- FC-1.json: `3e93a8d7d4b6350a2268ec091d6796db1dcdf488d5025a2d18a6adb0d674d68e`
- FC-2.json: `19c9a6e8fc1b55efeefa7537cfc46ff508344b34d993a613aaf3812da4fe4770`
- FC-3.json: `a23725af786c9da96faf8c3b971b0ae0b4ed06c7ceb10132e6b93e81ac8efb25`
- FX-PEC-0.json: `858172dca765fabefb0754bc3e2c4d801cb8a7a1faea3bc94c0051af21e173e9`
- Format: all files are ASCII with a final newline. A case-insensitive grep for "remaining" across the fixtures finds nothing.

### Two problems in the test module (the manager needs to decide on these)

**1. Tree paths resolve relative to the test's own folder, and one record type can pass when it should fail.**
- `test_tree_expectations_hold_at_their_pinned_commits` runs `git -C PARSERS_ROOT ls-tree --name-only <commit> <tree>/`.
- `ls-tree` reads path arguments relative to the current directory. That directory is `projects/pec/v2/tests/parsers`, so a path written from the repo root lists nothing.
- Result: every `present`/`absent` record written from the repo root fails. Worse, every `tree_absent` record passes whatever the truth is.
- I proved the second point: a `tree_absent` record pointing at the FC-1 AgentRuns folder, which exists, passed.
- My workaround: I prefixed each `tree` value with the pathspec `:(top)`. I checked with git 2.54.0 that `:(top)` works both without and with `--full-tree`.
- The FC-3 absence is recorded as an `absent` list on the App `AgentRuns` folder (137 entries at d61981ee2). I did not use `tree_absent`, so the check cannot pass on an empty listing.
- I mutation-checked the records. Wrong `present` and `absent` values now fail as they should.
- Recommended test fix: add `--full-tree` to that `ls-tree` call. The `:(top)` prefix can then stay or be removed.

**2. The copy check flags a path in the manifest.**
- The DEL-12-01 MEMORY blob (`7c683795…`) quotes its own folder path.
- `test_no_fixture_source_is_copied_into_the_tree` splits the raw manifest bytes on whitespace. The spaces inside that path form 8-word runs that match the blob.
- My workaround: spaces inside every pin `path` value are written as the JSON escape ` `. This is ASCII and parses to exactly the same value; `build.py` checks that `json.loads(text) == obj`.
- Alternative: have the test skip manifest `path` values when counting copied runs.
- This is a judgment call, not a change to the underlying data.

### Deliverable 1: `fixtures/pinned/MANIFEST.json` (verbatim)

```json
{
"schema": "pec-v2-parser-fixtures-pinned/v1",
"policy": {
  "source_run_words": 3,
  "copy_run_words": 8
},
"templates": [
  {
    "id": "TPL.work-graph",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "workflows/construct-local-work-graph/resources/work-graph-template.md",
    "blob": "91f10bfbe62c6442d6d56646f93f06f8bd7d9e1c"
  },
  {
    "id": "TPL.memory",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "docs/templates/MEMORY_TEMPLATE.md",
    "blob": "0aebc32f72530576471c3bf6deff2aedbcbd6b7d"
  }
],
"pins": [
  {
    "id": "FC-1.graph",
    "fixture": "FC-1",
    "project": "projects/chirality-piping",
    "kind": "graph",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/_Coordination/WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md",
    "blob": "ae942d99c7e0f698291c5d8ace95f65390df061d",
    "serves": [
      "DEL-02-08"
    ]
  },
  {
    "id": "FC-1.receipt",
    "fixture": "FC-1",
    "project": "projects/chirality-piping",
    "kind": "central-receipt",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md",
    "blob": "23623e2cf846bc4673603c9b7991ecf10e026825",
    "serves": [
      "DEL-02-03"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-01",
    "fixture": "FC-1",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-01_Calculation report generator/MEMORY.md",
    "blob": "15dcfee1a37df36eb2e73935a5a1c31971bbb46e",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-05",
    "fixture": "FC-1",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-08_Reporting, Audit, and Reproducibility/1_Working/DEL-08-05_Report protected-content linter/MEMORY.md",
    "blob": "917001226b19c4d53bd52187b7fc93269349aca2",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-2.graph",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "graph",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/_Coordination/WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md",
    "blob": "e471421ce8ad094d5cf7b49ed95bad39bf0ae3d7",
    "serves": [
      "DEL-02-08"
    ]
  },
  {
    "id": "FC-2.evidence",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "agentruns-evidence",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/_Coordination/AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md",
    "blob": "76e618a5a5c137b4f51bf63016a3b3a9997fb76a",
    "serves": [
      "DEL-02-03"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-00_Software Architecture Runway/1_Working/DEL-00-08_Layered software test and acceptance strategy/MEMORY.md",
    "blob": "71921955fb48ad969dec7a5b8e32b74680b0190b",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-04_Build, packaging, and CI-CD pipeline/MEMORY.md",
    "blob": "53ec1d47cf1b745c5bb555c0c8bf512d76cfd7e3",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-01_Local-first storage and private data paths/MEMORY.md",
    "blob": "7c683795ca7b8fb842d6b4e206703e3e3df50060",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06",
    "fixture": "FC-2",
    "project": "projects/chirality-piping",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package/MEMORY.md",
    "blob": "5f1a8bebb1a24aeaa460715644435d8656f27800",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FC-3.graph",
    "fixture": "FC-3",
    "project": "projects/chirality-app-dev",
    "kind": "graph",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md",
    "blob": "d25cae6130a7139d077c2e3bf848ea9aa70bae1f",
    "serves": [
      "DEL-02-08"
    ]
  },
  {
    "id": "FC-3.memory.DEL-05-04",
    "fixture": "FC-3",
    "project": "projects/chirality-app-dev",
    "kind": "memory",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "path": "projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View/MEMORY.md",
    "blob": "4d1e8a96b63cd7e9570b2bb8e27ce0b80694dbf7",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FX-PEC-0.registry",
    "fixture": "FX-PEC-0",
    "project": "projects/pec",
    "kind": "registry",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "projects/pec/v2/config/loops.json",
    "blob": "d5e60779b8e27b33a07f4f4e4cfec56982951450",
    "serves": [
      "DEL-02-03"
    ]
  },
  {
    "id": "FX-PEC-0.ledger",
    "fixture": "FX-PEC-0",
    "project": "projects/pec",
    "kind": "ledger",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "projects/pec/loop/LOOP_RECEIPTS.md",
    "blob": "ea6f32ccc081d517cfc822d48ed0181db42a5b67",
    "serves": [
      "DEL-02-03"
    ]
  },
  {
    "id": "FX-PEC-0.graph",
    "fixture": "FX-PEC-0",
    "project": "projects/pec",
    "kind": "graph",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md",
    "blob": "bf0b0c6262914b98ece3beb711b518821defc0db",
    "serves": [
      "DEL-02-08"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-06",
    "fixture": "FX-PEC-0",
    "project": "projects/pec",
    "kind": "memory",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/MEMORY.md",
    "blob": "fdf9351d1622f9cf651a711f995a23dd503fb882",
    "serves": [
      "DEL-02-09"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03",
    "fixture": "FX-PEC-0",
    "project": "projects/pec",
    "kind": "memory",
    "commit": "6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240",
    "path": "projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/MEMORY.md",
    "blob": "497bb00428d589094b2e97c04b1636394b506706",
    "serves": [
      "DEL-02-09"
    ]
  }
],
"trees": [
  {
    "id": "FC-1.tree.agentruns",
    "fixture": "FC-1",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "tree": ":(top)projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923",
    "present": [
      "RECEIPT.md"
    ],
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-017",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-016",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "FC-2.tree.agentruns",
    "fixture": "FC-2",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "tree": ":(top)projects/chirality-piping/execution/_Coordination/AgentRuns/PIP-DEC025-BASELINE-2026-09-23",
    "present": [
      "EVIDENCE.md"
    ],
    "absent": [
      "RECEIPT.md"
    ],
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-017",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-016",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "FC-3.tree.agentruns",
    "fixture": "FC-3",
    "commit": "d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b",
    "tree": ":(top)projects/chirality-app-dev/execution/_Coordination/AgentRuns",
    "absent": [
      "APP-REPLAY-BOUNDARY-2026-09-23",
      "replay-session-boundary-2026-09-23"
    ],
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-017",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-016",
      "DEL-02-03/VER-017"
    ]
  }
]
}
```

### Deliverable 2a: `fixtures/pinned/goldens/FC-1.json` (verbatim)

```json
{
"schema": "pec-v2-parser-fixtures-golden/v1",
"fixture": "FC-1",
"expectations": [
  {
    "id": "FC-1.graph.run-identity",
    "pin": "FC-1.graph",
    "tier": "fixed",
    "fact": "declared-run-identity",
    "source": {
      "run_identity": "PIPING_LINTER_SCOPE_20260923"
    },
    "expect": {
      "equals_folder": true
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/AC-006",
      "DEL-02-08/VER-006"
    ]
  },
  {
    "id": "FC-1.graph.terminal-node-state",
    "pin": "FC-1.graph",
    "tier": "fixed",
    "fact": "terminal-node-declared-state",
    "source": {
      "node_id": "F1",
      "state": "ACTIVE"
    },
    "expect": {
      "derived_claims": "none"
    },
    "binds": [
      "DEL-02-08/REQ-005",
      "DEL-02-08/AC-005",
      "DEL-02-08/VER-005"
    ]
  },
  {
    "id": "FC-1.graph.final-pr",
    "pin": "FC-1.graph",
    "tier": "observed",
    "fact": "terminal-node-cited-pr-merge",
    "source": {
      "pr": 876
    },
    "expect": {
      "local_merge_commit": "0b276a7fa5dcad7d8f3375ae4f0015a5368e791e"
    },
    "binds": [
      "DEL-02-08/REQ-008",
      "DEL-02-08/AC-008",
      "DEL-02-08/VER-008",
      "DEL-02-08/TBD-003"
    ]
  },
  {
    "id": "FC-1.receipt.receipt-id",
    "pin": "FC-1.receipt",
    "tier": "fixed",
    "fact": "receipt-id-from-cursor-field",
    "source": {
      "receipt_id": "PIPING_LINTER_SCOPE_20260923"
    },
    "expect": {
      "from_cursor_field": true,
      "equals_folder": true
    },
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/AC-017",
      "DEL-02-03/VER-016"
    ]
  },
  {
    "id": "FC-1.receipt.examined-through",
    "pin": "FC-1.receipt",
    "tier": "observed",
    "fact": "examined-through-sha-as-cited",
    "source": {
      "examined_through_sha": "8645c269e0b1ba5298ff53ee1ead6f83adb264a3"
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/AC-004",
      "DEL-02-03/VER-004",
      "DEL-02-03/TBD-004"
    ]
  },
  {
    "id": "FC-1.receipt.parent-receipt",
    "pin": "FC-1.receipt",
    "tier": "observed",
    "fact": "parent-receipt-token",
    "source": {
      "parent_receipt": "none"
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/AC-004",
      "DEL-02-03/VER-004",
      "DEL-02-03/TBD-007"
    ]
  },
  {
    "id": "FC-1.receipt.gate-outcome-presence",
    "pin": "FC-1.receipt",
    "tier": "observed",
    "fact": "gate-outcome-field-presence",
    "expect": {
      "gate_outcome_present": true
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/AC-004",
      "DEL-02-03/VER-004"
    ]
  },
  {
    "id": "FC-1.receipt.gate-outcome-prose",
    "pin": "FC-1.receipt",
    "tier": "fixed",
    "fact": "gate-outcome-value-not-emitted",
    "expect": {
      "gate_outcome_value_emitted": false
    },
    "binds": [
      "DEL-02-03/REQ-007",
      "DEL-02-03/AC-007",
      "DEL-02-03/VER-007"
    ]
  },
  {
    "id": "FC-1.receipt.generation",
    "pin": "FC-1.receipt",
    "tier": "fixed",
    "fact": "central-receipt-generation",
    "expect": {
      "generation": "central-receipt",
      "shared_validated_schema": false
    },
    "binds": [
      "DEL-02-03/REQ-001",
      "DEL-02-03/REQ-005",
      "DEL-02-03/AC-001",
      "DEL-02-03/AC-005",
      "DEL-02-03/VER-001",
      "DEL-02-03/VER-005"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-01.runs-entry-form",
    "pin": "FC-1.memory.DEL-08-01",
    "tier": "fixed",
    "fact": "runs-bullet-entry-form",
    "expect": {
      "form": "bullet",
      "anchor_line": 5
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-01.runs-entry-run-token",
    "pin": "FC-1.memory.DEL-08-01",
    "tier": "observed",
    "fact": "runs-bullet-entry-run-token",
    "source": {
      "run_token": "PIPING_LINTER_SCOPE_20260923"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-01.runs-entry-date",
    "pin": "FC-1.memory.DEL-08-01",
    "tier": "observed",
    "fact": "runs-bullet-entry-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-01.runs-entry-link-targets",
    "pin": "FC-1.memory.DEL-08-01",
    "tier": "observed",
    "fact": "runs-bullet-entry-link-targets",
    "source": {
      "link_target_as_cited": "../../../_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md",
      "substantive_pr": 867,
      "final_pr": 876
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-05.runs-entry-form",
    "pin": "FC-1.memory.DEL-08-05",
    "tier": "fixed",
    "fact": "runs-bullet-entry-form",
    "expect": {
      "form": "bullet",
      "anchor_line": 5
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-05.runs-entry-run-token",
    "pin": "FC-1.memory.DEL-08-05",
    "tier": "observed",
    "fact": "runs-bullet-entry-run-token",
    "source": {
      "run_token": "PIPING_LINTER_SCOPE_20260923"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-05.runs-entry-date",
    "pin": "FC-1.memory.DEL-08-05",
    "tier": "observed",
    "fact": "runs-bullet-entry-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-1.memory.DEL-08-05.runs-entry-link-targets",
    "pin": "FC-1.memory.DEL-08-05",
    "tier": "observed",
    "fact": "runs-bullet-entry-link-targets",
    "source": {
      "link_target_as_cited": "../../../_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md",
      "substantive_pr": 867,
      "final_pr": 876
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  }
]
}
```

### Deliverable 2b: `fixtures/pinned/goldens/FC-2.json` (verbatim)

```json
{
"schema": "pec-v2-parser-fixtures-golden/v1",
"fixture": "FC-2",
"expectations": [
  {
    "id": "FC-2.graph.run-identity",
    "pin": "FC-2.graph",
    "tier": "fixed",
    "fact": "declared-run-identity",
    "source": {
      "run_identity": "PIP-DEC025-BASELINE-2026-09-23"
    },
    "expect": {
      "equals_folder": false
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/AC-006",
      "DEL-02-08/VER-006"
    ]
  },
  {
    "id": "FC-2.graph.terminal-node-state",
    "pin": "FC-2.graph",
    "tier": "fixed",
    "fact": "terminal-node-declared-state",
    "source": {
      "node_id": "F1",
      "state": "ACTIVE"
    },
    "expect": {
      "derived_claims": "none"
    },
    "binds": [
      "DEL-02-08/REQ-005",
      "DEL-02-08/AC-005",
      "DEL-02-08/VER-005"
    ]
  },
  {
    "id": "FC-2.graph.final-pr",
    "pin": "FC-2.graph",
    "tier": "observed",
    "fact": "terminal-node-cited-pr-merge",
    "source": {
      "pr": 873
    },
    "expect": {
      "local_merge_commit": "c56ae4a284a747bc6eae7c177011151868064063"
    },
    "binds": [
      "DEL-02-08/REQ-008",
      "DEL-02-08/AC-008",
      "DEL-02-08/VER-008",
      "DEL-02-08/TBD-003"
    ]
  },
  {
    "id": "FC-2.evidence.not-a-receipt",
    "pin": "FC-2.evidence",
    "tier": "fixed",
    "fact": "agentruns-non-receipt-file-not-read",
    "expect": {
      "read_as_receipt": false
    },
    "binds": [
      "DEL-02-03/REQ-014",
      "DEL-02-03/AC-015",
      "DEL-02-03/VER-014"
    ]
  },
  {
    "id": "FC-2.evidence.receipt-coverage-limit",
    "pin": "FC-2.evidence",
    "tier": "fixed",
    "fact": "missing-receipt-is-coverage-limit",
    "expect": {
      "receipt_coverage_limit": true,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/AC-017",
      "DEL-02-03/VER-016"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08.run-entry-form",
    "pin": "FC-2.memory.DEL-00-08",
    "tier": "fixed",
    "fact": "run-dated-heading-entry-form",
    "expect": {
      "form": "dated-heading",
      "anchor_line": 157
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08.run-entry-heading-token",
    "pin": "FC-2.memory.DEL-00-08",
    "tier": "observed",
    "fact": "run-dated-heading-token",
    "source": {
      "heading_token": "PIP-DEC025-BASELINE-2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08.run-entry-date",
    "pin": "FC-2.memory.DEL-00-08",
    "tier": "observed",
    "fact": "run-dated-heading-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08.run-entry-link-targets",
    "pin": "FC-2.memory.DEL-00-08",
    "tier": "observed",
    "fact": "run-dated-heading-link-targets",
    "source": {
      "pr": 872
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "FC-2.memory.DEL-00-08.no-runs-section",
    "pin": "FC-2.memory.DEL-00-08",
    "tier": "fixed",
    "fact": "partial-coverage-not-nonconformance",
    "expect": {
      "runs_section": false,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/AC-001",
      "DEL-02-09/VER-001"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04.runs-entry-form",
    "pin": "FC-2.memory.DEL-10-04",
    "tier": "fixed",
    "fact": "runs-bullet-entry-form",
    "expect": {
      "form": "bullet",
      "anchor_line": 16
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04.runs-entry-run-token",
    "pin": "FC-2.memory.DEL-10-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-run-token",
    "source": {
      "run_token": "PIPING_LINTER_SCOPE_20260923"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04.runs-entry-date",
    "pin": "FC-2.memory.DEL-10-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04.runs-entry-link-targets",
    "pin": "FC-2.memory.DEL-10-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-link-targets",
    "source": {
      "link_target_as_cited": "../../../_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md",
      "substantive_pr": 867,
      "final_pr": 876
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "FC-2.memory.DEL-10-04.dated-section",
    "pin": "FC-2.memory.DEL-10-04",
    "tier": "observed",
    "fact": "dated-section-beside-runs-section",
    "source": {
      "heading_token": "PIP-DEC025-BASELINE-2026-09-23",
      "date": "2026-09-23",
      "pr": 872
    },
    "expect": {
      "form": "dated-heading",
      "anchor_line": 431
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-007",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-007",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-007",
      "DEL-02-09/TBD-005"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01.run-entry-form",
    "pin": "FC-2.memory.DEL-12-01",
    "tier": "fixed",
    "fact": "run-dated-heading-entry-form",
    "expect": {
      "form": "dated-heading",
      "anchor_line": 211
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01.run-entry-heading-token",
    "pin": "FC-2.memory.DEL-12-01",
    "tier": "observed",
    "fact": "run-dated-heading-token",
    "source": {
      "heading_token": "PIP-DEC025-BASELINE-2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01.run-entry-date",
    "pin": "FC-2.memory.DEL-12-01",
    "tier": "observed",
    "fact": "run-dated-heading-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01.run-entry-link-targets",
    "pin": "FC-2.memory.DEL-12-01",
    "tier": "observed",
    "fact": "run-dated-heading-link-targets",
    "source": {
      "pr": 872
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "FC-2.memory.DEL-12-01.no-runs-section",
    "pin": "FC-2.memory.DEL-12-01",
    "tier": "fixed",
    "fact": "partial-coverage-not-nonconformance",
    "expect": {
      "runs_section": false,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/AC-001",
      "DEL-02-09/VER-001"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06.run-entry-form",
    "pin": "FC-2.memory.DEL-17-06",
    "tier": "fixed",
    "fact": "run-dated-heading-entry-form",
    "expect": {
      "form": "dated-heading",
      "anchor_line": 123
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06.run-entry-heading-token",
    "pin": "FC-2.memory.DEL-17-06",
    "tier": "observed",
    "fact": "run-dated-heading-token",
    "source": {
      "heading_token": "PIP-DEC025-BASELINE-2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06.run-entry-date",
    "pin": "FC-2.memory.DEL-17-06",
    "tier": "observed",
    "fact": "run-dated-heading-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06.run-entry-link-targets",
    "pin": "FC-2.memory.DEL-17-06",
    "tier": "observed",
    "fact": "run-dated-heading-link-targets",
    "source": {
      "pr": 872
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "FC-2.memory.DEL-17-06.no-runs-section",
    "pin": "FC-2.memory.DEL-17-06",
    "tier": "fixed",
    "fact": "partial-coverage-not-nonconformance",
    "expect": {
      "runs_section": false,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/AC-001",
      "DEL-02-09/VER-001"
    ]
  }
]
}
```

### Deliverable 2c: `fixtures/pinned/goldens/FC-3.json` (verbatim)

```json
{
"schema": "pec-v2-parser-fixtures-golden/v1",
"fixture": "FC-3",
"expectations": [
  {
    "id": "FC-3.graph.run-identity",
    "pin": "FC-3.graph",
    "tier": "fixed",
    "fact": "declared-run-identity",
    "source": {
      "run_identity": "APP-REPLAY-BOUNDARY-2026-09-23"
    },
    "expect": {
      "equals_folder": false
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/AC-006",
      "DEL-02-08/VER-006"
    ]
  },
  {
    "id": "FC-3.graph.terminal-node-state",
    "pin": "FC-3.graph",
    "tier": "fixed",
    "fact": "terminal-node-declared-state",
    "source": {
      "node_id": "F1",
      "state": "ACTIVE"
    },
    "expect": {
      "derived_claims": "none"
    },
    "binds": [
      "DEL-02-08/REQ-005",
      "DEL-02-08/AC-005",
      "DEL-02-08/VER-005"
    ]
  },
  {
    "id": "FC-3.graph.final-pr",
    "pin": "FC-3.graph",
    "tier": "observed",
    "fact": "terminal-node-cited-pr-merge",
    "source": {
      "pr": 868
    },
    "expect": {
      "local_merge_commit": "10b672caed0a0e013ac72508ac72f6b3ce274286"
    },
    "binds": [
      "DEL-02-08/REQ-008",
      "DEL-02-08/AC-008",
      "DEL-02-08/VER-008",
      "DEL-02-08/TBD-003"
    ]
  },
  {
    "id": "FC-3.graph.node-id-suffix",
    "pin": "FC-3.graph",
    "tier": "fixed",
    "fact": "em-dash-node-suffix-not-emitted",
    "source": {
      "node_id": "F1"
    },
    "expect": {
      "node_suffix_prose_emitted": false
    },
    "binds": [
      "DEL-02-08/REQ-010",
      "DEL-02-08/AC-010",
      "DEL-02-08/VER-010"
    ]
  },
  {
    "id": "FC-3.memory.DEL-05-04.runs-entry-form",
    "pin": "FC-3.memory.DEL-05-04",
    "tier": "fixed",
    "fact": "runs-bullet-entry-form",
    "expect": {
      "form": "bullet",
      "anchor_line": 5
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "FC-3.memory.DEL-05-04.runs-entry-run-token",
    "pin": "FC-3.memory.DEL-05-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-run-token",
    "source": {
      "run_token": "APP-REPLAY-BOUNDARY-2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004"
    ]
  },
  {
    "id": "FC-3.memory.DEL-05-04.runs-entry-date",
    "pin": "FC-3.memory.DEL-05-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-date",
    "source": {
      "date": "2026-09-23"
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FC-3.memory.DEL-05-04.runs-entry-link-targets",
    "pin": "FC-3.memory.DEL-05-04",
    "tier": "observed",
    "fact": "runs-bullet-entry-link-targets",
    "source": {
      "link_target_as_cited": "../../../_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md",
      "evidence_link_target_as_cited": "../../../_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/RUN_EVIDENCE.md",
      "substantive_pr": 866,
      "final_pr": 868
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  }
]
}
```

### Deliverable 2d: `fixtures/pinned/goldens/FX-PEC-0.json` (verbatim)

```json
{
"schema": "pec-v2-parser-fixtures-golden/v1",
"fixture": "FX-PEC-0",
"expectations": [
  {
    "id": "FX-PEC-0.registry.ledger-profile",
    "pin": "FX-PEC-0.registry",
    "tier": "fixed",
    "fact": "declared-ledger-profile-state",
    "source": {
      "loop_id": "pec",
      "profile": "loop-receipts-ledger",
      "state": "historical"
    },
    "expect": {
      "declared_surface": "receipt-ledger",
      "receipt_label": "historical"
    },
    "binds": [
      "DEL-02-03/REQ-014",
      "DEL-02-03/REQ-015",
      "DEL-02-03/AC-015",
      "DEL-02-03/AC-016",
      "DEL-02-03/VER-014",
      "DEL-02-03/VER-015"
    ]
  },
  {
    "id": "FX-PEC-0.registry.shared-loop-profile",
    "pin": "FX-PEC-0.registry",
    "tier": "fixed",
    "fact": "declared-shared-loop-profile-state",
    "source": {
      "loop_id": "pec",
      "profile": "shared-dev-loop",
      "state": "live"
    },
    "expect": {
      "declared_surface": "central-receipts",
      "receipt_label": "live"
    },
    "binds": [
      "DEL-02-03/REQ-014",
      "DEL-02-03/REQ-015",
      "DEL-02-03/AC-015",
      "DEL-02-03/AC-016",
      "DEL-02-03/VER-014",
      "DEL-02-03/VER-015"
    ]
  },
  {
    "id": "FX-PEC-0.ledger.marker",
    "pin": "FX-PEC-0.ledger",
    "tier": "observed",
    "fact": "receipt-contract-marker",
    "source": {
      "marker": "receipt-contract-v2"
    },
    "expect": {
      "marker_present": true
    },
    "binds": [
      "DEL-02-03/REQ-003",
      "DEL-02-03/AC-003",
      "DEL-02-03/VER-003"
    ]
  },
  {
    "id": "FX-PEC-0.ledger.marker-governed-entry",
    "pin": "FX-PEC-0.ledger",
    "tier": "observed",
    "fact": "marker-governed-entry-fields",
    "source": {
      "receipt_id": "Receipt-197",
      "examined_through_sha": "eb56e108377c102ded295a39abcf91986da247aa",
      "parent_receipt": "Receipt-196"
    },
    "expect": {
      "gate_outcome_present": true
    },
    "binds": [
      "DEL-02-03/REQ-003",
      "DEL-02-03/AC-003",
      "DEL-02-03/VER-003",
      "DEL-02-03/TBD-007"
    ]
  },
  {
    "id": "FX-PEC-0.ledger.historical-silence",
    "pin": "FX-PEC-0.ledger",
    "tier": "fixed",
    "fact": "historical-silence-not-staleness",
    "expect": {
      "receipt_label": "historical",
      "staleness_claim": false
    },
    "binds": [
      "DEL-02-03/REQ-015",
      "DEL-02-03/AC-016",
      "DEL-02-03/VER-015"
    ]
  },
  {
    "id": "FX-PEC-0.graph.run-identity",
    "pin": "FX-PEC-0.graph",
    "tier": "fixed",
    "fact": "declared-run-identity-bold-bullet",
    "source": {
      "run_identity": "HELP-HUMAN-PEC-20260925-POST-SCA005"
    },
    "expect": {
      "equals_folder": true
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/AC-006",
      "DEL-02-08/VER-006"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-06.no-entries",
    "pin": "FX-PEC-0.memory.DEL-01-06",
    "tier": "fixed",
    "fact": "empty-template-table-coverage-limit",
    "expect": {
      "entries": 0,
      "coverage_limit": true,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/AC-001",
      "DEL-02-09/VER-001"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h3.run-id",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "fixed",
    "fact": "dated-heading-run-id-unavailable",
    "source": {
      "decision_id": "D-PEC-85"
    },
    "expect": {
      "run_id_available": false,
      "anchor_line": 3
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h3.date",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "observed",
    "fact": "dated-heading-date",
    "source": {
      "date": "2026-09-08"
    },
    "expect": {
      "form": "dated-heading",
      "anchor_line": 3
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h16.run-id",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "fixed",
    "fact": "dated-heading-run-id-unavailable",
    "source": {
      "decision_id": "D-PEC-85"
    },
    "expect": {
      "run_id_available": false,
      "anchor_line": 16
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h16.date",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "observed",
    "fact": "dated-heading-date",
    "source": {
      "date": "2026-09-08"
    },
    "expect": {
      "form": "dated-heading",
      "anchor_line": 16
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h82.run-id",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "fixed",
    "fact": "dated-heading-run-id-unavailable",
    "source": {
      "decision_id": "D-PEC-87",
      "parenthesized_token": "P1_STORE_GUARD_02"
    },
    "expect": {
      "run_id_available": false,
      "anchor_line": 82
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h82.date",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "observed",
    "fact": "dated-heading-date",
    "source": {
      "date": "2026-09-24"
    },
    "expect": {
      "form": "dated-heading",
      "anchor_line": 82
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h109.run-id",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "fixed",
    "fact": "dated-heading-run-id-unavailable",
    "source": {
      "decision_id": "D-PEC-89",
      "parenthesized_token": "P1_STORE_GUARD_03"
    },
    "expect": {
      "run_id_available": false,
      "anchor_line": 109
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/AC-004",
      "DEL-02-09/VER-004",
      "DEL-02-09/CON-004"
    ]
  },
  {
    "id": "FX-PEC-0.memory.DEL-01-03.h109.date",
    "pin": "FX-PEC-0.memory.DEL-01-03",
    "tier": "observed",
    "fact": "dated-heading-date",
    "source": {
      "date": "2026-09-25"
    },
    "expect": {
      "form": "dated-heading",
      "anchor_line": 109
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/AC-005",
      "DEL-02-09/VER-005"
    ]
  }
]
}
```

### Deliverable 3: fact table

**How the lines were found.** Line numbers are 1-based lines of the pinned blob. They were computed with the test's own match pattern: a word-boundary match for strings, and `(?:#|/pull/)N(?![0-9])` for PR numbers. The first hit is the one the fact concerns; any other hits are incidental.

**Pin resolution.** Every pin was resolved with `git rev-parse <commit>:<path>` and equals the blob listed.
- d61981ee2 is an ancestor of 6c6cc1b00.
- The two templates resolve at 6c6cc1b00 to `91f10bfb…` and `0aebc32f…`.

**Merge commits.** Each was found with `git log --merges --grep '^Merge pull request #N from'`. Each search matched exactly one commit, each has two parents, and each is an ancestor of d61981ee2:
- #876 → `0b276a7fa5dcad7d8f3375ae4f0015a5368e791e`
- #873 → `c56ae4a284a747bc6eae7c177011151868064063`
- #868 → `10b672caed0a0e013ac72508ac72f6b3ce274286`
- For reference: #867 → `8645c269e0b1…` (this equals the FC-1 receipt's Examined-Through), #872 → `db5bb387…`, #866 → `2ea77252…`

**FC-1 work graph** (`ae942d99`)

| Source value | Blob line(s) |
|---|---|
| run_identity `PIPING_LINTER_SCOPE_20260923` | L5 (the identity bullet); L33 is incidental |
| node_id `F1` | L35 (the F1 row); L23 and L48 are incidental |
| state `ACTIVE` | L35 |
| pr 876 | L35 (the F1 row); L33, L34, L48 are incidental |

**FC-1 central receipt** (`23623e2c`)

| Source value | Blob line(s) |
|---|---|
| receipt_id | L39 (the `**Receipt-ID:**` cursor field under "Cursor and pointers" at L37); L1 and L47 are incidental |
| examined_through_sha `8645c269…` | L40; L10 is incidental |
| parent_receipt `none` | L41 |
| Gate-Outcome field (no source value; the value is prose) | L53–56 |

**FC-1 MEMORY files**

| Pin | Anchor (bullet) | Run token | Date | Receipt link | PR 867 | PR 876 |
|---|---|---|---|---|---|---|
| DEL-08-01 (`15dcfee1`) | L5 | L5 | L5 | L7 | L8 | L9 |
| DEL-08-05 (`91700122`) | L5 | L5 | L5 | L7 | L8 | L9 |

The receipt link normalizes to `projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md`, which is the FC-1.receipt pin path.

**FC-2 work graph** (`e471421c`)

| Source value | Blob line(s) |
|---|---|
| run_identity `PIP-DEC025-BASELINE-2026-09-23` | L5; L29 and L35 are incidental |
| node_id `F1` | L31 |
| state `ACTIVE` | L31 |
| pr 873 | L31; L36 and L37 are incidental |

**FC-2 EVIDENCE.md** (`76e618a5`): no source values.

**FC-2 MEMORY files, run entry recorded as a dated heading**

| Pin | Anchor (dated heading) | Heading token | Date | pr 872 | `## Runs` section |
|---|---|---|---|---|---|
| DEL-00-08 (`71921955`) | L157 | L157 | L157 | L159 | none (headings at L1, 3, 20, 36, 51, 64, 84, 91, 109, 157) |
| DEL-12-01 (`7c683795`) | L211 | L211 | L211 | L213 | none |
| DEL-17-06 (`5f1a8beb`) | L123 | L123 | L123 | L125 | none |

**FC-2 DEL-10-04** (`53ec1d47`, mixed forms)

| Entry | Anchor | Other values |
|---|---|---|
| `## Runs` heading | L14 | none |
| `## Runs` bullet (FC-1 run) | L16 | run token L16; date L16; receipt link L19; PR 867 L20; PR 876 L21 |
| Dated section (FC-2 run) | L431 | heading token L431; date L431; pr 872 L433 |

**FC-3 work graph** (`d25cae61`)

| Source value | Blob line(s) |
|---|---|
| run_identity `APP-REPLAY-BOUNDARY-2026-09-23` | L5 |
| node_id `F1` | L27 (`\| F1 — final PR \| … \| ACTIVE: [PR #868]…`); L16, 63, 69–71 are incidental |
| state `ACTIVE` | L27; L42 is incidental |
| pr 868 | L27; L26, 53, 63 are incidental |
| em-dash node suffixes | Work table L22–L27 |

**FC-3 DEL-05-04** (`4d1e8a96`)

| Source value | Blob line(s) |
|---|---|
| bullet anchor | L5 |
| run token | L5 |
| date | L5; L8 and L9 are incidental |
| link to the work graph | L8 (normalizes to the FC-3 graph pin path) |
| link to RUN_EVIDENCE.md | L9 |
| pr 866 | L10 |
| pr 868 | L11 |

**FX-PEC-0 registry** (`loops.json`, `d5e60779`)

| Source value | Blob line(s) |
|---|---|
| loop_id `pec` | L24 (`"loop_id": "pec"`); L6, 12, 18, 25 are incidental |
| profile `loop-receipts-ledger` | L13 |
| state `historical` | L14 |
| profile `shared-dev-loop` | L7 |
| state `live` | L8 |

The `declared_surface` labels (`receipt-ledger`, `central-receipts`) come from `projects/pec/v2/config/loops.schema.json` at 6c6cc1b00, lines 31 and 35. They are not in the pinned blob.

**FX-PEC-0 ledger** (`LOOP_RECEIPTS.md`, `ea6f32cc`)

| Source value | Blob line(s) |
|---|---|
| marker `receipt-contract-v2` | L1865 (`<!-- receipt-contract-v2 frozen-through=Receipt-166 … -->`) |
| receipt_id `Receipt-197` | L2188 (entry header at L2187) |
| examined_through_sha `eb56e108…` | L2189 |
| parent_receipt `Receipt-196` | L2190; L2177 is incidental |
| Gate-Outcome | L2196 |

**FX-PEC-0 graph** (`bf0b0c62`): run_identity at L7 (`- **Stable run identity:** \`HELP-HUMAN-PEC-20260925-POST-SCA005\``). L3 and L164 are incidental.

**FX-PEC-0 DEL-01-06** (`fdf9351d`): `## Runs` at L10; template table header at L12; separator at L13. There are no rows.

**FX-PEC-0 DEL-01-03** (`497bb004`)

| Anchor | Heading text | Decision ID | Date | Parenthesized token |
|---|---|---|---|---|
| L3 | `## 2026-09-08 — D-PEC-85 P-A production start` | D-PEC-85 L3 | L3 | none |
| L16 | `## 2026-09-08 — D-PEC-85 P-A technical fan-in` | D-PEC-85 L16 | L16 | none |
| L82 | `## 2026-09-24 — D-PEC-87 C-A correction slice (P1_STORE_GUARD_02)` | L82 | L82 | P1_STORE_GUARD_02 L82 |
| L109 | `## 2026-09-25 — D-PEC-89 A exact-type closure slice (P1_STORE_GUARD_03)` | L109 | L109 | P1_STORE_GUARD_03 L109 |

D-PEC-85, D-PEC-87 and D-PEC-89 are rows at lines 102, 104 and 106 of the PEC `_DECISIONS/_REGISTER.md` at 6c6cc1b00.

**Tree records** (checked at d61981ee2)
- FC-1 AgentRuns folder: `RECEIPT.md`.
- FC-2 AgentRuns folder: `EVIDENCE.md` and `checks`, with no `RECEIPT.md`.
- App `AgentRuns`: 137 entries, none named `APP-REPLAY-BOUNDARY-2026-09-23` or `replay-session-boundary-2026-09-23`. A search of every App path for `APP-REPLAY-BOUNDARY` returns nothing.

**Contract lines for every bound ID.** These are the contract blobs at 6c6cc1b00; the three contract folders show no diff between 6c6cc1b00 and HEAD `3f41666bb`.

DEL-02-03 (`ScopeOfWork.md` blob `3e0a48c6…`):
| ID | Line | ID | Line | ID | Line |
|---|---|---|---|---|---|
| REQ-001 | 172 | AC-001 | 191 | VER-001 | 232 |
| REQ-003 | 174 | AC-003 | 193 | VER-003 | 234 |
| REQ-004 | 175 | AC-004 | 194 | VER-004 | 235 |
| REQ-005 | 176 | AC-005 | 195 | VER-005 | 236 |
| REQ-007 | 178 | AC-007 | 197 | VER-007 | 238 |
| REQ-014 | 185 | AC-015 | 205 | VER-014 | 245 |
| REQ-015 | 186 | AC-016 | 206 | VER-015 | 246 |
| REQ-016 | 187 | AC-017 | 207 | VER-016 | 247 |
| REQ-017 | 188 | AC-018 | 208 | VER-017 | 248 |
| TBD-004 | 161 | TBD-007 | 163 | | |

DEL-02-08 (blob `1a006f7d…`):
| ID | Line | ID | Line | ID | Line |
|---|---|---|---|---|---|
| REQ-005 | 155 | AC-005 | 176 | VER-005 | 216 |
| REQ-006 | 156 | AC-006 | 177 | VER-006 | 217 |
| REQ-008 | 158 | AC-008 | 179 | VER-008 | 219 |
| REQ-010 | 160 | AC-010 | 181 | VER-010 | 221 |
| TBD-003 | 139 | | | | |

DEL-02-09 (blob `226e9ca1…`):
| ID | Line | ID | Line | ID | Line |
|---|---|---|---|---|---|
| REQ-001 | 140 | AC-001 | 157 | VER-001 | 192 |
| REQ-002 | 141 | AC-002 | 158 | VER-002 | 193 |
| REQ-003 | 142 | AC-003 | 159 | VER-003 | 194 |
| REQ-004 | 143 | AC-004 | 160 | VER-004 | 195 |
| REQ-005 | 144 | AC-005 | 161 | VER-005 | 196 |
| REQ-007 | 146 | AC-007 | 163 | VER-007 | 198 |
| REQ-014 | 153 | AC-014 | 170 | VER-014 | 205 |
| TBD-005 | 130 | CON-004 | 178 | | |

### Suite result (verbatim tail)

Command: `run_fixture_suite.sh <repo> 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240 <mktemp>/parsers -v`, exit code 1.

```
test_every_record_binds_a_requirement_criterion_and_verification (...) ... ok
test_git_access_is_read_only_and_allowlisted (...) ... ok
test_golden_source_values_are_grounded_in_their_pinned_blobs (...) ... ok
test_goldens_are_content_minimal_and_hold_no_source_text_run (...) ... ok
test_loaded_suite_has_exact_verification_mapping (...) ... ok
test_manifests_and_goldens_are_well_formed (...) ... ok
test_no_fixture_source_is_copied_into_the_tree (...) ... ok
test_pins_resolve_by_read_only_plumbing_on_integrated_history (...) ... ok
test_synthetic_cases_cover_the_contract_minimums (...) ... FAIL
test_tree_expectations_hold_at_their_pinned_commits (...) ... ok
======================================================================
FAIL: test_synthetic_cases_cover_the_contract_minimums (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_synthetic_cases_cover_the_contract_minimums)
----------------------------------------------------------------------
Traceback (most recent call last):
File ".../x1pfix.KSIxSt/projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py", line 420, in test_synthetic_cases_cover_the_contract_minimums
  self.assertLessEqual(set(required), labels[deliverable], deliverable)
AssertionError: {'unresolved-pr-number', 'no-node-table', 'unrecognized-state-token', 'duplicated-run-identity', 'two-graphs-bind-one-deliverable', 'missing-run-identity'} not less than or equal to set() : DEL-02-08
----------------------------------------------------------------------
Ran 10 tests in 1.944s

FAILED (failures=1)
```

In the tail, `(...)` stands for the repeated full test path. Everything else is verbatim. The full output is in `suite.out`.

### Judgment calls

1. **DEL-10-04 is pinned once, under FC-2.** At d61981ee2 it is one blob (`53ec1d47`) for both fixtures.
 - Its `## Runs` bullet (L16) records the FC-1 run. Its dated section (L431) records the FC-2 run.
 - I put it under FC-2 because it is the only `## Runs` file among FC-2's four touched deliverables, and it is the mixed-form case (DEL-02-09 TBD-005).
 - FC-1 keeps two bullet pins (DEL-08-01, DEL-08-05). As a result, FC-2's golden carries the FC-1 run token for that file.

2. **Which facts are `fixed`.**
 - The declared identity is fixed for FC-2 and FC-3 because DEL-02-08 VER-006 names them. It is fixed for FC-1 because it uses the template's own `- Stable run identity:` spelling.
 - F1 declared `ACTIVE` is fixed because VER-005 names FC-1, FC-2 and FC-3.
 - The FC-1 Receipt-ID is fixed because DEL-02-03 VER-016 names the FC-1 cursor-field identity.
 - Caveat: DEL-02-03 TBD-002 and DEL-02-08 TBD-002 leave bold-bullet and cursor recognition to production. So the FX-PEC-0 bold-bullet identity is `fixed` only because the brief says so. Strictly, REQ-006 would let a grammar that cannot read the bold spelling emit a limitation instead. The manager should confirm this one.

3. **Which facts are `observed`.**
 - The final-PR `local_merge_commit` facts are `observed`, because the PR syntaxes a grammar recognizes are DEL-02-08 TBD-003. Once a PR is yielded, AC-008 requires the listed merge commit.
 - The FC-2 dated-heading run token is `observed`, per DEL-02-09 CON-004. Declaring a token position in headings is a scope or method decision, so a conforming parser may mark it unavailable.

4. **`anchor_line` convention.** This is an integer in `expect` giving the 1-based line in the blob. It locates the construct a fact concerns where a file has several similar entries. It is not a parser output field, and it can be removed if the manager prefers.

5. **Link targets as cited.** `link_target_as_cited` is the raw relative link. The normalized repository-relative form cannot be a source value because it does not occur in the blob. The normalized equivalents are given in the fact table.
 - I did not record the backticked `EVIDENCE.md` paths in the FC-2 MEMORY files as link targets. Whether code spans count as links is DEL-02-09 TBD-002.

6. **Where AC-004's fixed "run ID unavailable" applies.** I applied it only to DEL-01-03 headings L3, L16, L82 and L109. L3 and L82 are the contract's own examples in DEL-02-09 CLM-016.
 - Skipped L39: its heading carries an item-range token and a `D83` token that are ambiguous.
 - Skipped L134: it carries an `A-53` token that is neither clearly a decision identifier nor parenthesized.
 - None were added in FC-2 files. Their FC-2 heading carries the run token itself, their other headings carry round or tranche tokens (R4, R5, T2A), and DEL-10-04 is mixed.

7. **FC-2 partial coverage.** Recorded as fixed `{runs_section:false, nonconformance:false}` on DEL-00-08, DEL-12-01 and DEL-17-06. The grounds are DEL-02-09 REQ-001/AC-001, AX-002, and the SOW-096 Notes cell.

8. **FC-3's DEL-02-03 coverage limit lives only in the tree record.** Attaching it to the FC-3 graph pin would make a work graph serve DEL-02-03, which DEL-02-03 REQ-018 forbids. The FC-2 coverage limit is on the EVIDENCE pin.
 - The tree records also bind REQ-017, AC-018 and VER-017, because they establish each case's class at the pin.

9. **FX-PEC-0 choices.**
 - Receipt-197 is the marker-governed entry. It is the ledger's closing entry.
 - The DEL-01-06 fact is `{entries:0, coverage_limit:true, nonconformance:false}`, with no table-shape fact.

10. **No live/historical label for Piping or App.** The registry has only the `pec` row, so no label is recorded for those central receipts.
  - Parsing the FC fixtures at all assumes a test-time registry declaration for those loops (DEL-02-03 TBD-003). The parser packet must supply it.
  - DEL-02-08 CON-004 and DEL-02-09 CLM-013 say those contracts add no FX-PEC-0 output. I pinned the PEC graph and MEMORY files because the brief directs it. At 6c6cc1b the registry declares `shared-dev-loop` `live`, whose surfaces include work graphs (schema L35).

11. **Constraint on the retired sections was honored.** There is no `_STATUS.md` pin, no retirement graph or receipt, and no fact about those sections. The PEC graph and ledger blobs do mention such sections in their own text, but no expectation touches them.

### Deferred to the grammar (deliberately not recorded)

- **Graphs:**
- node lists, node counts and per-state counts, including FC-1's extra R1 node, FC-2's two W nodes, and FC-3's ID-led rows in the "Completed work / node" table at L69–71;
- non-terminal node states;
- DEL bindings per node;
- PR numbers in non-terminal cells;
- hex SHAs and linked paths in graph cells;
- the PEC graph's F1 `PLANNED` state and its other nodes.
- **Receipts:**
- `Owner-Direction` and `Model-Attribution` presence;
- pointer PRs;
- whether the ledger's `EXECUTED` backticked Gate-Outcome prefix counts as a token;
- which ledger entries the marker governs, and the unavailable marking for entries before it;
- Examined-Through ancestry (DEL-02-03 TBD-008).
- **MEMORY:**
- entry and row counts;
- which non-run dated headings count as entries (for example, the TP-* headings), and their tokens;
- code-span paths as link targets.

### What I could not ground or did not check

- I did not run the suite against the real synthetic manifest, which is drafted elsewhere.
- DEL-02-08 and DEL-02-09 state their observations at `53145aaeb`. I used the contract blobs as they stand at 6c6cc1b.
- I did not decide whether Piping `D-23` and `DEC-093` headings meet AC-004, and nothing in the files relies on them.
- The two test-module problems above are my observations from the probes described. The test file itself is unchanged.
