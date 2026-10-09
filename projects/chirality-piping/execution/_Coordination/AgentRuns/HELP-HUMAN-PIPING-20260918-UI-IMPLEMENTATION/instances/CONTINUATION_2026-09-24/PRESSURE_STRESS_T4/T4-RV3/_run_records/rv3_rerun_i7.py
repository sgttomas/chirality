"""T4-RV3: re-run T4-I7's own scripts from a scratch copy and compare their outputs byte for byte with
the committed files.

    python -I -B rv3_rerun_i7.py <R4/T4-I7> <empty scratch dir> <WT/scratch/t4_RV1/h2_check.py>

Only basenames are printed."""
import filecmp
import hashlib
import os
import shutil
import subprocess
import sys

src, out, h2 = sys.argv[1], sys.argv[2], sys.argv[3]
rr = os.path.join(src, "_run_records")
code = os.path.join(out, "code")
os.makedirs(code, exist_ok=True)
for f in os.listdir(rr):
    if f.endswith(".py"):
        shutil.copy(os.path.join(rr, f), code)
print("h2_check.py sha256", hashlib.sha256(open(h2, "rb").read()).hexdigest())


def run(script, args, stdout_name):
    with open(os.path.join(out, stdout_name), "wb") as fh:
        subprocess.run([sys.executable, "-I", "-B", os.path.join(code, script)] + args, stdout=fh, check=True,
                       cwd=out)
    same = filecmp.cmp(os.path.join(out, stdout_name), os.path.join(rr, stdout_name), shallow=False)
    print("%-36s stdout byte-identical: %s" % (script, same))


run("u2_generate.py", [out], "u2_generate.stdout.txt")
for f in ("u2_reference_cases.json", "u2_document_sketches.json"):
    print("%-36s byte-identical: %s" % (f, filecmp.cmp(os.path.join(out, f), os.path.join(src, f), shallow=False)))
run("u2_crosscheck.py", [src], "u2_crosscheck.stdout.txt")
run("u2_precision_check.py", [src], "u2_precision_check.stdout.txt")
run("rv1_seed_comparison.py", [h2], "rv1_seed_comparison.stdout.txt")
