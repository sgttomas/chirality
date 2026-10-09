"""RV130, read-only: re-measure T4-U3's overlap with b2 (e582b61f9e) in the two
shared files where T4-I10 states exact hunks, by three-way file merges.

Usage: python -I rv130_overlap.py <repo-root> <scratch-dir>

For each file: MAIN = ec5d397359, ED = ed012c7ccf (main + U3), B2 = e582b61f9e.
1. B2U = merge(B2, base MAIN, ED): b2 with U3 (the J0b state of the file).
2. T4 = ED with T4-I10's exact hunks applied (SLOT_TABLE section 4.4).
3. RESULT = merge(T4, base ED, B2U). Clean iff no conflict markers.
Also reports the unchanged-line gap, in ED coordinates, between each T4 hunk
and B2U's nearest change. Uses `git show` and `git merge-file -p` only (no
repository writes); files go to <scratch-dir>.
"""
import difflib
import os
import subprocess
import sys

REPO, OUT = sys.argv[1], sys.argv[2]
MAIN, ED, B2 = "ec5d397359", "ed012c7ccf", "e582b61f9e"
P = "projects/chirality-piping/"


def show(commit, path):
    return subprocess.run(["git", "-C", REPO, "show", f"{commit}:{P}{path}"], capture_output=True, check=True).stdout.decode()


def write(name, text):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def merge(ours, base, theirs, tag):
    a, b, c = write(f"{tag}.ours", ours), write(f"{tag}.base", base), write(f"{tag}.theirs", theirs)
    r = subprocess.run(["git", "merge-file", "-p", a, b, c], capture_output=True)
    return r.returncode, r.stdout.decode()


def changed_lines(base, other):
    """Base line numbers (1-based) touched by other's change; insertions are
    recorded as the half-line after the preceding base line."""
    sm = difflib.SequenceMatcher(None, base.splitlines(), other.splitlines(), autojunk=False)
    touched = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        touched.append((i1 + 0.5, i1 + 0.5) if i1 == i2 else (i1 + 1, i2))
    return touched


def gap(span, touched):
    lo, hi = span
    best = None
    for a, b in touched:
        d = 0 if (b >= lo and a <= hi) else (lo - b if lo > b else a - hi)
        best = d if best is None or d < best else best
    return best


def apply(text, edits):
    lines = text.splitlines(keepends=True)
    for kind, line_no, payload in sorted(edits, key=lambda e: -e[1]):
        if kind == "replace":
            old, new = payload
            assert old in lines[line_no - 1], (line_no, lines[line_no - 1])
            lines[line_no - 1] = lines[line_no - 1].replace(old, new)
        elif kind == "insert_after":
            lines.insert(line_no, payload)
        elif kind == "delete":
            assert payload in lines[line_no - 1], (line_no, lines[line_no - 1])
            del lines[line_no - 1]
    return "".join(lines)


FILES = {
    "core/product_physics/src/retained_product.rs": [
        ("replace", 1558, ("built.user_stiffness_elements", "built.connectors")),
    ],
    "core/product_physics/tests/s11f_site_test.rs": [
        ("insert_after", 221, '    ("PP/lib.rs", "add_connector_reference_loads", "connector reference state: +B^T K q_ref per nonzero DOF (formed, Bounded)"),\n'),
        ("replace", 511, ('"append_expansion_joint_user_stiffness_results", 1, "integer: appended count"',
                          '"add_connector_reference_loads", 0, "producer"')),
        ("insert_after", 1382, '    (\n        "add_connector_reference_loads",\n        "formed: connector +B^T K q_ref, Bounded, self-equilibrated",\n        &["Formation::Bounded"],\n        Some(&["true"]),\n    ),\n'),
    ],
}

for path, edits in FILES.items():
    tag = path.rsplit("/", 1)[-1]
    main, ed, b2 = show(MAIN, path), show(ED, path), show(B2, path)
    code, b2u = merge(b2, main, ed, tag + ".b2u")
    print(f"== {path}")
    print(f"   B2U = merge(b2, main, U3): {'clean' if code == 0 else f'CONFLICT ({code})'}")
    t4 = apply(ed, edits)
    code, result = merge(t4, ed, b2u, tag + ".t4")
    print(f"   merge(T4, ED, B2U): {'clean' if code == 0 else f'CONFLICT ({code})'}")
    touched = changed_lines(ed, b2u)
    for kind, line_no, _ in edits:
        span = (line_no + 0.5, line_no + 0.5) if kind == "insert_after" else (line_no, line_no)
        print(f"   T4 {kind} at ED:{line_no}: nearest B2U change gap {gap(span, touched)} unchanged ED lines")
    # The result must contain both sides' changes.
    expect_t4 = [e[2] if e[0] == "insert_after" else e[2][1] for e in edits]
    ok = all(x.strip().splitlines()[0] in result for x in expect_t4)
    b2_only = [l for l in b2u.splitlines() if l not in ed.splitlines()]
    ok_b2 = all(l in result.splitlines() for l in b2_only)
    print(f"   result keeps every T4 hunk: {ok}; keeps every b2 line: {ok_b2} ({len(b2_only)} b2-only lines)")
