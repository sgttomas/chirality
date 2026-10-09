"""T4-RV5: re-run T4-I12's three scripts (as frozen at a744c09021) and compare their outputs
byte for byte with the frozen JSON and stdouts.

Usage: python -I rv5_reproduce_i12.py <dir holding the frozen T4-I12 files> <empty scratch dir>
The frozen directory is extracted with `git -C NUM4 show a744c09021:R4/T4-I12/<file>`.
"""
import hashlib
import os
import shutil
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


rr = os.path.join(out, "_run_records")
os.makedirs(rr, exist_ok=True)
for f in ["u3_reference.py", "check_reference_json.py", "probe_binary64.py"]:
    shutil.copy(os.path.join(src, "_run_records", f), rr)
py = sys.executable
res = subprocess.run([py, "-I", "u3_reference.py", "../u3_reference_cases.json"], cwd=rr, capture_output=True)
open(os.path.join(rr, "u3_reference.stdout.txt"), "wb").write(res.stdout + res.stderr)
print("u3_reference.py exit", res.returncode)
for script in ["check_reference_json.py", "probe_binary64.py"]:
    r2 = subprocess.run([py, "-I", script, "../u3_reference_cases.json"], cwd=rr, capture_output=True)
    open(os.path.join(rr, script.replace(".py", ".stdout.txt")), "wb").write(r2.stdout + r2.stderr)
    print(script, "exit", r2.returncode)
for rel in ["u3_reference_cases.json", "_run_records/u3_reference.stdout.txt",
            "_run_records/check_reference_json.stdout.txt", "_run_records/probe_binary64.stdout.txt"]:
    a, b = sha(os.path.join(src, rel)), sha(os.path.join(out, rel))
    print("%-48s frozen %s  re-run %s  %s" % (rel, a[:16], b[:16], "IDENTICAL" if a == b else "DIFFERENT"))
print("python", sys.version.split()[0])
