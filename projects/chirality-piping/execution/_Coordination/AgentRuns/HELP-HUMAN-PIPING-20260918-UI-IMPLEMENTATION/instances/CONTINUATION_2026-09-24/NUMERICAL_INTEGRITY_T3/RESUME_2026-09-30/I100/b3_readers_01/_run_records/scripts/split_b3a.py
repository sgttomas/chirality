"""I100 B3: write the B3a-only tree state into the lane (from HEAD plus B3a's edits), saving the full working files.
Usage: split_b3a.py save|b3a|restore"""
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("WT/b2-p")
P = "projects/chirality-piping/"
KEEP = Path("WT/scratch/i100_b3r/work/full")
FILES = ["core/analysis_runs/retained_precision.py", "core/analysis_runs/compatibility.py",
         "tests/test_retained_precision_contract.py", "tests/test_retained_precision_b3.py"]


def head(rel):
    return subprocess.run(["git", "-C", str(LANE), "show", "HEAD:" + P + rel], check=True, capture_output=True, text=True).stdout


if sys.argv[1] == "save":
    for rel in FILES:
        (KEEP / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(LANE / P / rel, KEEP / rel)
elif sys.argv[1] == "restore":
    for rel in FILES:
        shutil.copyfile(KEEP / rel, LANE / P / rel)
else:
    full = (KEEP / FILES[0]).read_text()
    rp = head(FILES[0])
    old = '''    # The model scope, as PP accepts it (the alignment set, item 2): no reference_configurations member (null
    # included); pressure_contract absent or null; combinations and components absent or [].
    need(model.get("schema_version") in ("0.1.0", "0.2.0", "0.3.0") and model.get("pressure_contract") is None and model.get("combinations", []) == [], "INVOCATION_MISMATCH")'''
    new = '''    # The model scope, as PP accepts it (the alignment set, item 2): no reference_configurations member (null
    # included); the namespace (B3a, below); combinations and components absent or [].
    need(_legacy_namespace(model) and model.get("combinations", []) == [], "INVOCATION_MISMATCH")'''
    assert rp.count(old) == 1
    rp = rp.replace(old, new)
    start = full.index("LEGACY_PRESSURE_CONTRACT = {")
    end = full.index("def _legacy_namespace(model):")
    end = full.index("\n\n\n", end) + 3
    block = full[start:end]
    assert rp.count("def _g8(body, source, invocation):") == 1
    rp = rp.replace("def _g8(body, source, invocation):", block + "def _g8(body, source, invocation):")
    (LANE / P / FILES[0]).write_text(rp)
    (LANE / P / FILES[1]).write_text(head(FILES[1]))
    shutil.copyfile(KEEP / FILES[2], LANE / P / FILES[2])
    b3 = (KEEP / FILES[3]).read_text()
    cut = b3.index("# ---------------------------------------------------------------------------------------------------------------\n# B3b:")
    b3a = b3[:cut].rstrip() + "\n"
    b3a = b3a.replace('''def reseal(source, invocation, definition_hash=rp.DEFINITION_HASH):
    """The 07e format rule on a copy: the invocation digest, each complete preparation hash with the route's
    definition hash (S-1; B3-D REVISION_01 §2), the selected cases' source identities, then publication and receipt."""''', '''def reseal(source, invocation):
    """The 07e format rule on a copy: the invocation digest, each complete preparation hash, the selected cases'
    source identities, then publication and receipt."""''').replace("rp._preparation_payload(attempt, definition_hash))", "rp._preparation_payload(attempt))")
    assert "definition_hash" not in b3a
    (LANE / P / FILES[3]).write_text(b3a)
print(sys.argv[1], "done")
