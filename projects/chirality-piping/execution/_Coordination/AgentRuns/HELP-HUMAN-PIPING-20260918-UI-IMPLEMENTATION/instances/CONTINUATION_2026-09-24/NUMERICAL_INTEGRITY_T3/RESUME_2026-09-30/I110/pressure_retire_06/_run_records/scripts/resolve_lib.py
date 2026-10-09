#!/usr/bin/env python3
"""I110 round 6: resolve the one PP/src/lib.rs import conflict between the U3 branch and main ec5d397359 (PR-N):
keep main's correct_norm import (with I109's comment) and the branch's exact_sum import without exact_rounded_sum.
Works for either side order and the diff3 style. Usage: resolve_lib.py <lib.rs>"""
import re, sys
p = sys.argv[1]; s = open(p).read()
rx = re.compile(r"<<<<<<< [^\n]*\n(.*?)(?:\|\|\|\|\|\|\| [^\n]*\n.*?)?=======\n(.*?)>>>>>>> [^\n]*\n", re.S)
blocks = rx.findall(s)
assert len(blocks) == 1, f"{len(blocks)} conflicts"
a, b = blocks[0]
branch = "use open_pipe_stress_frame_kernel::exact_sum::ExactAccumulator;\n"
main = ("// I109: magnitudes formerly formed with libm `hypot` are correctly rounded norms; `source_receipt::scaled_norm` and `displacement_magnitude` stay deterministic IEEE, not correctly rounded.\n"
        "use open_pipe_stress_frame_kernel::correct_norm::{norm2, norm3};\n"
        "use open_pipe_stress_frame_kernel::exact_sum::{exact_rounded_sum, ExactAccumulator};\n")
assert {a, b} == {branch, main}, (a, b)
resolved = main.replace("exact_sum::{exact_rounded_sum, ExactAccumulator};", "exact_sum::ExactAccumulator;")
s = rx.sub(lambda m: resolved, s, count=1)
assert "exact_rounded_sum" not in s
open(p, "w").write(s); print("resolved")
