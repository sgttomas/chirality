#!/usr/bin/env python3

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_agent_instructions as validator


VALID_AGENT = """---
description: "fixture"
---
[[DOC:AGENT_INSTRUCTIONS]]
# AGENT INSTRUCTIONS — TASK (Fixture)
AGENT_TYPE: 2

## Agent Type
| Property | Value |
|---|---|
| **AGENT_TYPE** | TYPE 2 |
| **AGENT_CLASS** | TASK |
| **INTERACTION_SURFACE** | INIT-TASK |
| **WRITE_SCOPE** | bounded-task-brief |
| **BLOCKING** | never |
| **PRIMARY_OUTPUTS** | fixture |

[[BEGIN:PROTOCOL]]
## PROTOCOL
[[END:PROTOCOL]]
[[BEGIN:SPEC]]
## SPEC
[[END:SPEC]]
[[BEGIN:STRUCTURE]]
## STRUCTURE
[[END:STRUCTURE]]
[[BEGIN:RATIONALE]]
## RATIONALE
[[END:RATIONALE]]
"""


class ValidateAgentInstructionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "agents").mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self, text: str, name: str = "AGENT_TASK.md") -> list[validator.Finding]:
        path = self.root / "agents" / name
        path.write_text(text, encoding="utf-8")
        return validator.validate_file(path, self.root, {"R1", "R12", "R17"})

    def test_valid_task_fixture(self) -> None:
        self.assertEqual([], self.validate(VALID_AGENT))

    def test_type_mismatch_is_error(self) -> None:
        findings = self.validate(VALID_AGENT.replace("AGENT_TYPE: 2", "AGENT_TYPE: 1"))
        self.assertIn("TYPE_MISMATCH", {item.code for item in findings})

    def test_non_task_type2_requires_requalification(self) -> None:
        text = VALID_AGENT.replace("— TASK (", "— AUDITOR (")
        findings = self.validate(text, "AGENT_AUDITOR.md")
        self.assertIn("TYPE2_REQUALIFICATION_REQUIRED", {item.code for item in findings})

    def test_missing_agent_reference_warns(self) -> None:
        text = VALID_AGENT.replace("## PROTOCOL", "See `AGENT_MISSING.md`.\n## PROTOCOL")
        findings = self.validate(text)
        self.assertIn("AGENT_REFERENCE_UNRESOLVED", {item.code for item in findings})


if __name__ == "__main__":
    unittest.main()
