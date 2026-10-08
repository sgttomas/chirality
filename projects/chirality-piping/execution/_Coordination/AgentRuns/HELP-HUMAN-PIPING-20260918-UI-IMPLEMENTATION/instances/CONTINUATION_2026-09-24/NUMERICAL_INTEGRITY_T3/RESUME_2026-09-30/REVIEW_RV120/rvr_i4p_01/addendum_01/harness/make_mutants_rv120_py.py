"""RV120 (RV-R): my own PY mutants on rulings 1, 2 and 5's new or moved checks, added on top of RV113's PY schema
(make_py_mutants_r2.py and _r2b.py, run first on the same copy; they define `_mx` on RV113_MUT in retained_precision.py).
Here each file gets its own guard on the same variable. Each anchor must match exactly once.
Usage: python3 make_mutants_rv120_py.py <P root> <manifest out>
"""
import json
import sys

root, manifest_out = sys.argv[1], sys.argv[2]
GUARD = 'import os as _rv120_os\n\n\ndef _qx(i):\n    return _rv120_os.environ.get("RV113_MUT") == i\n\n\n'
manifest = []


def edit(rel, pairs, after_imports):
    path = f"{root}/{rel}"
    src = open(path).read()
    assert src.count(after_imports) == 1, (rel, after_imports[:60])
    src = src.replace(after_imports, after_imports + GUARD, 1)
    for old, new, mid, desc in pairs:
        assert src.count(old) == 1, (mid, src.count(old), old[:90])
        src = src.replace(old, new)
        if mid:
            manifest.append({"id": mid, "item": "rulings 1, 2 (PY)", "description": desc})
    open(path, "w").write(src)


edit("core/analysis_runs/compatibility.py", [
    ('    if "carrier_evidence" in source and not rust_header_order:\n',
     '    if "carrier_evidence" in source and (_qx("Q01") or not rust_header_order):\n',
     "Q01", "ruling 1: the carrier branch kept on the retained transport header"),
    ('    if rust_header_order and recovery_forbidden:\n',
     '    if rust_header_order and recovery_forbidden and not _qx("Q02"):\n',
     "Q02", "ruling 1: source_block_recovery no longer checked before contract_evidence"),
    ('def _source_contract(source: Mapping[str, Any], *, check_receipt: bool = True, rust_header_order: bool = False) -> tuple[str, str, Path]:\n',
     'def _source_contract(source: Mapping[str, Any], *, check_receipt: bool = True, rust_header_order: bool = False) -> tuple[str, str, Path]:\n    rust_header_order = rust_header_order or _qx("Q03")\n',
     "Q03", "ruling 1's scope: the plain preview-physics-1 dispatch also takes Rust's order"),
], "from __future__ import annotations\n")
edit("core/analysis_runs/preview_physics_evidence.py", [
    ('    withheld = (lambda records: tuple(sorted(records))) if withheld_multiset else frozenset\n',
     '    withheld = (lambda records: tuple(sorted(records))) if withheld_multiset and not _qx("Q04") else frozenset\n    if _qx("Q05"):\n        withheld = lambda records: tuple(sorted(set(records)))\n',
     "Q04", "ruling 2: transport compares withheld records as sets again"),
],"from __future__ import annotations\n")
manifest.append({"id": "Q05", "item": "rulings 1, 2 (PY)", "description": "ruling 2: multiset by sorted(set(...)) (multiplicity lost)"})
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
