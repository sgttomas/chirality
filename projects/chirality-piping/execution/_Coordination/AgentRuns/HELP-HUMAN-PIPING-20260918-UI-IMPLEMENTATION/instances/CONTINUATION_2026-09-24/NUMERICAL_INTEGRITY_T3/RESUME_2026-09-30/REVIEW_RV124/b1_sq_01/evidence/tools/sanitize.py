"""RV124: copy a text file with machine paths replaced by placeholders (WT; CARGO_HOME; RUSTUP_HOME; SCRATCHPAD)."""
import sys, re
src, dst = sys.argv[1:3]
t = open(src, "rb").read().decode("utf-8", "replace")
reps = [
    ("R", "R"),
    ("T", "T"),
    ("WT", "WT"),
    ("CARGO_HOME", "CARGO_HOME"),
    ("RUSTUP_HOME", "RUSTUP_HOME"),
]
for a, b in reps:
    t = t.replace(a, b)
t = re.sub(r"SCRATCHPAD'\"]*", "SCRATCHPAD", t)
t = re.sub(r"SCRATCHPAD'\"]*", "SCRATCHPAD", t)
open(dst, "w").write(t)
