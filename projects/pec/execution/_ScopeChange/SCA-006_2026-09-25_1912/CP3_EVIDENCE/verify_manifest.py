#!/usr/bin/env python3
"""Verify the applied tranche manifest: stripping the one named
`group2_amendment_1` block and restoring the §9 slot defaults yields the
§6.1 draft (852b1d5b...). Also parses the YAML and prints the block."""
import hashlib, pathlib, sys, yaml
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
p = R / "docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml"
t = p.read_text()
i = t.index("group2_amendment_1:\n")
base = t[:i]
for new, old in [
    ("PEC-SCA006-OPERATIONAL-RELIANCE-20260926", "PEC-SCA006-OPERATIONAL-RELIANCE-20260925"),
    ("\ndate: 2026-09-26\n", "\ndate: 2026-09-25\n"),
    ("basis: 94e9255b68d6cda15926c7ee0187d6e9a759a43b", "basis: 4d5f7b91102b7106ff74b98118b2bda2fe873f36"),
    ("NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md", "NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md"),
    ("'SCA-006 CP2: accept; Q1 a; Q2 a'", "'[SLOT CP2-ACT: the owner's checkpoint-2 act, transcribed\n    verbatim from the group-2 DECISION.md]'"),
    ("AGENTS.candidate.md, which\n    carries SCA-006 Seq 14-17 plus the work-graph node I1 corrections", "[SLOT CP2-VARIANT: AGENTS.candidate.md, which\n    carries SCA-006 Seq 14-17 plus the work-graph node I1 corrections, or\n    AGENTS.candidate_without_I1.md, which carries SCA-006 Seq 14-17 only]"),
]:
    base = base.replace(new, old)
h = hashlib.sha256(base.encode()).hexdigest()
print("draft reverse proof:", h, "MATCH" if h == "852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45" else "MISMATCH")
d = yaml.safe_load(t)
print("manifest sha256:", hashlib.sha256(t.encode()).hexdigest())
print("top-level keys:", list(d))
print("group2_amendment_1 keys:", list(d["group2_amendment_1"]))
print("owner_words:", d["group2_amendment_1"]["owner_words"])
print("owner_hunk_approval:", d["group2_amendment_1"]["owner_hunk_approval"])
sys.exit(0 if h == "852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45" else 1)
