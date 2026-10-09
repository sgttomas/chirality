"""RV130, read-only: PP lib.rs, b2's hunks re-expressed in ED (main + U3)
coordinates through B2U = merge(b2, main, U3), and the gap from each of
T4-U3's cited lib.rs edit sites (ED coordinates) to the nearest B2U change.

Usage: python -I rv130_lib_gaps.py <repo-root> <scratch-dir>
"""
import difflib
import os
import subprocess
import sys

REPO, OUT = sys.argv[1], sys.argv[2]
MAIN, ED, B2 = "ec5d397359", "ed012c7ccf", "e582b61f9e"
PATH = "projects/chirality-piping/core/product_physics/src/lib.rs"


def show(c):
    return subprocess.run(["git", "-C", REPO, "show", f"{c}:{PATH}"], capture_output=True, check=True).stdout.decode()


def write(name, text):
    p = os.path.join(OUT, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


main, ed, b2 = show(MAIN), show(ED), show(B2)
r = subprocess.run(["git", "merge-file", "-p", write("lib.b2", b2), write("lib.main", main), write("lib.ed", ed)], capture_output=True)
b2u = r.stdout.decode()
print(f"B2U = merge(b2, main, U3) for PP lib.rs: {'clean' if r.returncode == 0 else 'CONFLICT'}")
sm = difflib.SequenceMatcher(None, ed.splitlines(), b2u.splitlines(), autojunk=False)
touched = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        touched.append((i1 + 0.5, i1 + 0.5) if i1 == i2 else (i1 + 1, i2))
print(f"B2U changes in ED coordinates: {len(touched)} hunks, span ED {min(a for a, _ in touched)}-{max(b for _, b in touched)}")
for a, b in touched:
    print(f"   ED {a}-{b}")
SITES = [(51, 53), (66, 66), (363, 363), (1225, 1251), (1454, 1466), (1558, 1559), (2050, 2050), (2412, 2417),
         (2779, 2781), (3538, 3545), (3759, 3774), (3897, 3897), (4435, 4435), (4933, 4933), (5060, 5060),
         (5236, 5236), (5359, 5359), (5755, 5758), (6100, 6107), (6135, 6143), (6256, 6264), (6382, 6450),
         (7211, 7211), (7326, 7326), (7337, 7338), (7417, 7417), (7482, 7593), (8466, 8466), (8621, 8650),
         (8777, 8840), (11906, 12005), (12246, 12247), (17393, 17587)]
print("T4-U3 lib.rs sites (ED) -> gap to nearest B2U change (unchanged ED lines):")
for lo, hi in SITES:
    best = min((0 if (b >= lo and a <= hi) else (lo - b if lo > b else a - hi)) for a, b in touched)
    print(f"   ED {lo}-{hi}: {best}")
