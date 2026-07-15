#!/usr/bin/env python3
"""Load the proven W-P3 full-reproduction harness with sealed W-P4 bindings."""

from pathlib import Path

source = Path(__file__).parents[1] / "RECON-P3/reconcile_p3.py"
text = source.read_text(encoding="utf-8")
replacements = {
    "15-member W-P3": "22-member W-P4",
    '"instances/RECON-P3"': '"instances/RECON-P4"',
    '"snapshots/W_P3/preintegration"': '"snapshots/W_P4/preintegration"',
    '"snapshots/W_P3/preflight"': '"snapshots/W_P4/preflight"',
    '"candidates/W_P3"': '"candidates/W_P4"',
    'PACKAGES = ["10", "11", "12"]': 'PACKAGES = ["14", "15", "16", "17"]',
    '"10": (1567, "4856fe725d0feaf4866d39a749d2e3769031204b452268466119cf210023ed0a"),\n    "11": (1530, "4dc1714c70c38fe4469af9e4d680f3f32a8d050f7d3c53c20ebafeff97608ee7"),\n    "12": (1397, "ab265d917a4d51e6e1bae7f0e9c2aa75e0f36cb9f82f329e783f345c8793a417"),':
        '"14": (1202, "b5b3ef134d2a9563552f1ec0ad37e93bd22998d5267c238244389db9423778cf"),\n    "15": (923, "a5dfe903f5a3abe8dfe8671536d62dcf327cdca4267334d7f8185e7224432533"),\n    "16": (1205, "0c73fd053eeaf6788203c7fa129680c6d8c4c910165b2d045d27b51a6e6683c8"),\n    "17": (2328, "dd6951bc037be7a7b33e8b5205a4abd3ddaebf8fa1fe39f7f76982d39b73192d"),',
    'RUN / f"instances/WORKING-P3-PKG{pkg}"': 'RUN / f"instances/WORKING-P4-PKG{pkg}"',
    'children = ["AUTHOR-B1", "VERIFY-B1"] if pkg != "12" else ["AUTHOR-B1", "VERIFY-B1", "VERIFY-B1-R1"]':
        'children = ["AUTHOR-B1", "VERIFY-B1"] if pkg != "17" else ["AUTHOR-B1", "VERIFY-B1", "AUTHOR-B2", "VERIFY-B2"]',
    'accepted = not (pkg == "12" and child == "VERIFY-B1")': 'accepted = True',
    'assert manager_total == 4494 and accepted_children == 6 and excluded_children == 1':
        'assert manager_total == 5658 and accepted_children == 10 and excluded_children == 0',
    '"P3_MANIFEST.tsv"': '"P4_MANIFEST.tsv"',
    'assert len(rows) == 15': 'assert len(rows) == 22',
    'prefix=f"recon-p3-{did}-"': 'prefix=f"recon-p4-{did}-"',
    'assert total_maps == 493 and total_lines == 4919 and len(replacement) == len(rollback) == 75 and len(negative) == 105':
        'assert total_maps == 729 and total_lines == 6759 and len(replacement) == len(rollback) == 110 and len(negative) == 154',
    '"basis": "main@4d153302c3c4cd42578936db160c2bac1270225a"':
        '"basis": "main@e8f59a63372f38d9e788ac39b39995558f5aba73"',
    '"members": 15, "packages": 3': '"members": 22, "packages": 4',
    '"candidate_files": 45, "replacement_rows": 75, "rollback_rows": 75':
        '"candidate_files": 66, "replacement_rows": 110, "rollback_rows": 110',
    '"simulations_pass": 15, "negative_probes_pass": 105':
        '"simulations_pass": 22, "negative_probes_pass": 154',
    '"dependency_schema_checks": 15': '"dependency_schema_checks": 22',
    '"full_member_reproduction": "15_OF_15"': '"full_member_reproduction": "22_OF_22"',
    '"pkg12_replacement_independence": "PASS_ZERO_PROHIBITED_READS",\n               ': '',
    'sow = f"{row[\'live_path\']}/ScopeOfWork.md"; replacement.append([did, "ADD", sow, "ABSENT", sha(production)]); rollback.append([did, "DELETE", sow, sha(production), "ABSENT"])\n        for name in LEGACY:\n            path = f"{row[\'live_path\']}/{name}"; source_hash = row[HASH_COLS[name]]\n            replacement.append([did, "DELETE", path, source_hash, "ABSENT"]); rollback.append([did, "ADD", path, "ABSENT", source_hash])':
        'sow = f"{row[\'live_path\']}/ScopeOfWork.md"\n        for name in LEGACY:\n            path = f"{row[\'live_path\']}/{name}"; source_hash = row[HASH_COLS[name]]\n            replacement.append([did, "DELETE", path, source_hash]); rollback.append([did, "RESTORE", path, source_hash])\n        replacement.append([did, "ADD", sow, sha(production)]); rollback.append([did, "DELETE", sow, sha(production)])',
    'write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], replacement)':
        'write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "operation", "path", "sha256"], replacement)',
    'write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], rollback)':
        'write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "operation", "path", "sha256"], rollback)',
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f"missing inherited harness binding: {old}")
    text = text.replace(old, new)
exec(compile(text, str(source), "exec"), {"__name__": "__main__", "__file__": str(__file__)})
