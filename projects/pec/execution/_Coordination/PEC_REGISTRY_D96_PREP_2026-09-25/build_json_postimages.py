#!/usr/bin/env python3
"""Build the D-PEC-96 JSON postimages in canonical form (sorted keys, indent 2, LF, final newline).

Preparation aid only. The bound act script embeds the resulting bytes.
Usage: build_json_postimages.py <out-root>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

D94 = "projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md"
PEC_AGENTS = "projects/pec/AGENTS.md"
PEC_LOOP_INIT = "projects/pec/loop/LOOP_INIT.md"


def canonical(obj: object) -> bytes:
    return (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("utf-8")


PATH_RULE = (
    "Normalized repository-relative path (no leading '/', no '..' segment, no backslash)"
)

SCHEMA = {
    "$id": "https://chirality.local/pec/v2/config/loops.schema.v2.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "additionalProperties": False,
    "description": (
        "Local configuration format naming the loops PEC serves and the closed, "
        "PEC-versioned feed profiles PEC reads each loop with. Schema version 1 is "
        "not accepted by the version-2 loader."
    ),
    "properties": {
        "loops": {
            "description": "The configured loops PEC may read as non-authoritative file-truth locations.",
            "items": {
                "additionalProperties": False,
                "properties": {
                    "feed_profiles": {
                        "description": (
                            "The feed profiles PEC applies to this loop: PEC's reading hypothesis, "
                            "never the loop's truth. At least one entry and at least one live entry; "
                            "a profile identifier appears at most once per loop, and the profiles "
                            "on one loop cover pairwise-disjoint surfaces, so no surface is read "
                            "under two grammars or declared both live and historical."
                        ),
                        "items": {
                            "additionalProperties": False,
                            "properties": {
                                "basis": {
                                    "description": (
                                        "Citation to the loop's own record that supports this declaration. "
                                        + PATH_RULE
                                        + "."
                                    ),
                                    "minLength": 1,
                                    "type": "string",
                                },
                                "profile": {
                                    "description": (
                                        "Identifier from PEC's closed feed-profile vocabulary. Each option "
                                        "ends with the surfaces it covers. Path conventions and grammars "
                                        "for each profile live in PEC's adapters."
                                    ),
                                    "oneOf": [
                                        {
                                            "const": "agentruns-json",
                                            "description": (
                                                "JSON run evidence anywhere under the loop's execution/ tree "
                                                "(WORK_GRAPH.json, STATUS.json, RUNTIME_SUMMARY.json), including "
                                                "AgentRuns/ and deliverable _run_records/; the identifier keeps "
                                                "its SCA-005 name. Surfaces: json-run-evidence."
                                            ),
                                        },
                                        {
                                            "const": "loop-receipts-ledger",
                                            "description": (
                                                "The loop's loop/LOOP_RECEIPTS.md receipt ledger, under that "
                                                "loop's grammar. Surfaces: receipt-ledger."
                                            ),
                                        },
                                        {
                                            "const": "shared-dev-loop",
                                            "description": (
                                                "The shared development-loop method: undertaking work graphs "
                                                "(execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md), "
                                                "central receipts (execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md), "
                                                "the deliverable MEMORY.md run index, _STATUS.md lifecycle, "
                                                "dependency registers and decision registers. Surfaces: "
                                                "central-receipts, decision-registers, dependency-registers, "
                                                "memory-run-index, status-lifecycle, work-graphs."
                                            ),
                                        },
                                    ],
                                    "type": "string",
                                },
                                "state": {
                                    "description": (
                                        "live: the loop currently writes this generation. historical: the "
                                        "generation is frozen, and its silence is never reported as staleness."
                                    ),
                                    "enum": ["historical", "live"],
                                    "type": "string",
                                },
                                "version": {
                                    "const": 1,
                                    "description": "Version of the selected profile; every profile in this vocabulary is at version 1.",
                                    "type": "integer",
                                },
                            },
                            "required": ["basis", "profile", "state", "version"],
                            "type": "object",
                        },
                        "minItems": 1,
                        "type": "array",
                    },
                    "loop_id": {
                        "description": "Stable lower-case identifier for one configured loop.",
                        "minLength": 1,
                        "pattern": "^[a-z][a-z0-9-]*$",
                        "type": "string",
                    },
                    "loop_init_path": {
                        "description": "Repository-relative path to the loop's governed LOOP_INIT.md surface.",
                        "minLength": 1,
                        "type": "string",
                    },
                },
                "required": ["feed_profiles", "loop_id", "loop_init_path"],
                "type": "object",
            },
            "minItems": 1,
            "type": "array",
        },
        "schema_version": {
            "const": 2,
            "description": "Version of this local loop-registry configuration format.",
            "type": "integer",
        },
    },
    "required": ["schema_version", "loops"],
    "title": "PEC local loop registry configuration v2",
    "type": "object",
}


def default_document() -> dict:
    profiles = [
        {"basis": D94, "profile": "shared-dev-loop", "state": "live", "version": 1},
        {"basis": PEC_AGENTS, "profile": "loop-receipts-ledger", "state": "historical", "version": 1},
        {"basis": D94, "profile": "agentruns-json", "state": "historical", "version": 1},
    ]
    return {
        "loops": [
            {
                "feed_profiles": profiles,
                "loop_id": "pec",
                "loop_init_path": PEC_LOOP_INIT,
            }
        ],
        "schema_version": 2,
    }


FIXTURE_ROW_PROFILES = [
    {"basis": D94, "profile": "shared-dev-loop", "state": "live", "version": 1},
]

DUPLICATE = {
    "loops": [
        {"feed_profiles": FIXTURE_ROW_PROFILES, "loop_id": "pec", "loop_init_path": PEC_LOOP_INIT},
        {"feed_profiles": FIXTURE_ROW_PROFILES, "loop_id": "pec", "loop_init_path": "somewhere/else/LOOP_INIT.md"},
    ],
    "schema_version": 2,
}

MISSING = {
    "loops": [
        {"feed_profiles": FIXTURE_ROW_PROFILES, "loop_init_path": PEC_LOOP_INIT},
    ],
    "schema_version": 2,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("out_root")
    args = parser.parse_args()
    out = Path(args.out_root)
    files = {
        "v2/config/loops.schema.json": canonical(SCHEMA),
        "v2/config/loops.json": canonical(default_document()),
        "v2/tests/config/fixtures/duplicate_loop_id.json": canonical(DUPLICATE),
        "v2/tests/config/fixtures/missing_loop_id.json": canonical(MISSING),
    }
    for rel, data in files.items():
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
