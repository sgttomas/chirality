"""Byte identity of the 35 written targets against the act script's tabled postimages
(and candidate copies), plus hygiene of the written files (UTF-8 with U+2014 as the only
non-ASCII character; LF; no tabs or trailing blanks; final newline).
Usage (cwd repo root): check_bytes_hygiene.py <run root>"""
import hashlib, importlib.util, sys
from pathlib import Path
rr = Path(sys.argv[1])
s = importlib.util.spec_from_file_location("a", rr / "apply_x1p.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
bad = 0
for rel, (_, post) in m.TARGETS.items():
    b = Path(rel).read_bytes(); h = hashlib.sha256(b).hexdigest(); c = hashlib.sha256((rr / "candidates" / rel).read_bytes()).hexdigest()
    ok = h == post == c; bad += not ok
    print(f"{'OK  ' if ok else 'FAIL'} {h} {rel}")
extra = sorted(p.as_posix() for p in Path(m.NEW_DIR).rglob("*") if p.is_file() and p.as_posix() not in m.TARGETS)
for e in extra: print("FAIL extra file", e); bad += 1
print(f"BYTES {'PASS' if not bad else 'FAIL'} {len(m.TARGETS)} targets; extra files under {m.NEW_DIR}: {len(extra)}")
hb = 0
for rel in m.TARGETS:
    b = Path(rel).read_bytes(); t = b.decode("utf-8"); probs = []
    if any(ord(ch) > 127 and ch != "—" for ch in t): probs.append("non-ASCII other than U+2014")
    if b"\r" in b: probs.append("CR")
    if b"\t" in b: probs.append("tab")
    if any(l.endswith(" ") for l in t.split("\n")): probs.append("trailing blank")
    if not b.endswith(b"\n"): probs.append("no final newline")
    if probs: hb += 1; print("HYGIENE", rel, probs)
print(f"HYGIENE {'PASS' if not hb else 'FAIL'} {len(m.TARGETS)-hb}/{len(m.TARGETS)}")
sys.exit(1 if bad or hb else 0)
