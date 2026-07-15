#!/usr/bin/env python3
"""Build W-P3 by applying audited wave deltas to the accepted W-P2 builder."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "ORCHESTRATOR-P2-B0/build_preflight.py"
text = SOURCE.read_text()

replacements = [
    ('"""Build the deterministic, read-only W-P2 Piping preflight snapshot."""',
     '"""Build the deterministic, read-only W-P3 Piping preflight snapshot."""'),
    ('OUT = RUN / "snapshots/W_P2/preflight"', 'OUT = RUN / "snapshots/W_P3/preflight"'),
    ('DISPATCH = "eaad463c0d481f6f1654e6adb5ee718f566176e9"',
     'DISPATCH = "4d153302c3c4cd42578936db160c2bac1270225a"'),
    ('PACKAGES = {"PKG-05": 5, "PKG-06": 5, "PKG-07": 8, "PKG-08": 6, "PKG-09": 5}',
     'PACKAGES = {"PKG-10": 5, "PKG-11": 5, "PKG-12": 5}'),
    ('("I1 merge", "6d56a1b6f391d21618f3328179d5a48654aec422"),',
     '("I1 merge", "6d56a1b6f391d21618f3328179d5a48654aec422"),\n'
     '        ("W-P2 merge", "7b5f27c17f425c1e1f8e47f4e81200b070227f69"),'),
    ('if len(selected) != 29 or counts != PACKAGES:', 'if len(selected) != 15 or counts != PACKAGES:'),
    ('managers = {pkg: f"WORKING-P2-{pkg.replace(\'-\', \'\')}" for pkg in PACKAGES}',
     'managers = {pkg: f"WORKING-P3-{pkg.replace(\'-\', \'\')}" for pkg in PACKAGES}'),
    ('candidates/W_P2/', 'candidates/W_P3/', 2),
    ('"P2_MANIFEST.tsv"', '"P3_MANIFEST.tsv"'),
    ('depends = "W-P2-B0_ACCEPTED"', 'depends = "W-P3-B0_ACCEPTED"'),
    ('else f"W-P2-', 'else f"W-P3-'),
    ('"wave": "W-P2"', '"wave": "W-P3"'),
    ('snapshots/W_P2/preflight/PACKAGE_BRIEFS/', 'snapshots/W_P3/preflight/PACKAGE_BRIEFS/'),
    ('and r["package"] in {"PKG-01", "PKG-02", "PKG-03", "PKG-04"}',
     'and r["package"] in {"PKG-01", "PKG-02", "PKG-03", "PKG-04", "PKG-05", "PKG-06", "PKG-07", "PKG-08", "PKG-09"}'),
    ('("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/ACCEPTANCE.md", "ACCEPTED_P1_PREDECESSOR"),',
     '("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/ACCEPTANCE.md", "ACCEPTED_P1_PREDECESSOR"),\n'
     '        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P2/integration/postmerge/HANDOFF_STATE.md", "ACCEPTED_P2_PREDECESSOR"),\n'
     '        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P2/integration/postmerge/MANIFEST.tsv", "ACCEPTED_P2_POSTMERGE_BINDING"),'),
    ('# W-P2 Sequential Package Execution Contract', '# W-P3 Sequential Package Execution Contract'),
    ('exact 29-member ordinary Piping P2', 'exact 15-member ordinary Piping P3'),
    ('strict order PKG-05 through\nPKG-09', 'strict order PKG-10 through\nPKG-12'),
    ('reproduce every package row and hash from `P2_MANIFEST.tsv`',
     'reproduce every package row and hash from `P3_MANIFEST.tsv`'),
    ('validate_scope_of_work.py --json (29 members)', 'validate_scope_of_work.py --json (15 members)'),
    ('validate_dependencies_schema.py (29 registers)', 'validate_dependencies_schema.py (15 registers)'),
    ('len(binding_rows) == 261', 'len(binding_rows) == 135'),
    ('"wave": "P2"', '"wave": "P3"'),
    ('"selected_members": 29', '"selected_members": 15'),
    ('"expected_live_bindings": 261', '"expected_live_bindings": 135'),
    ('"dependency_registers": 29', '"dependency_registers": 15'),
    ('# W-P2 Ordinary Piping Preflight Basis', '# W-P3 Ordinary Piping Preflight Basis'),
    ('The exact population is 29 P3 ordinary Piping members in PKG-05 through\nPKG-09, split 5/5/8/6/5. All 116 legacy sources, 29 statuses, and 261 live',
     'The exact population is 15 P3 ordinary Piping members in PKG-10 through\nPKG-12, split 5/5/5. All 60 legacy sources, 15 statuses, and 135 live'),
    ('seven batches: PKG-05 5; PKG-06 5; PKG-07 5+3; PKG-08 5+1; PKG-09 5.',
     'three batches: PKG-10 5; PKG-11 5; PKG-12 5.'),
]

for replacement in replacements:
    old, new, *expected_values = replacement
    expected = expected_values[0] if expected_values else 1
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"expected {expected} builder delta matches, got {count}: {old!r}")
    text = text.replace(old, new)

namespace = {"__name__": "w_p3_builder", "__file__": str(HERE / "generated_w_p3_builder.py")}
exec(compile(text, namespace["__file__"], "exec"), namespace)
namespace["main"]()
namespace["bind_snapshot"]()
