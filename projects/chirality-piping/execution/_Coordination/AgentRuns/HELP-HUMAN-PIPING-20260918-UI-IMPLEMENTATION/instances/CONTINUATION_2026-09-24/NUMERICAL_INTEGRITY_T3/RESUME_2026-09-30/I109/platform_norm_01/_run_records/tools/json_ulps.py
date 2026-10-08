#!/usr/bin/env python3
"""I109: compare two JSON documents leaf by leaf (same structure expected).

Numbers that differ are reported with their ulp distance (binary64, ordered
bits); strings that differ are reported as text changes (hashes, ids, message
text). Usage: json_ulps.py <a.json> <b.json> [label]  -> one JSON line.
"""
import json
import math
import struct
import sys


def ordered(x):
    u = struct.unpack("<q", struct.pack("<d", x))[0]
    return u if u >= 0 else -(u & 0x7FFFFFFFFFFFFFFF)


def ulps(a, b):
    if math.isnan(a) or math.isnan(b) or math.isinf(a) or math.isinf(b):
        return None
    return abs(ordered(a) - ordered(b))


def walk(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out["structure"].append(f"{path}/{k}")
            else:
                walk(a[k], b[k], f"{path}/{k}", out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out["structure"].append(f"{path}[len {len(a)}!={len(b)}]")
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", out)
    elif isinstance(a, bool) or isinstance(b, bool):
        if a != b:
            out["other"].append(path)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if float(a) != float(b) or (isinstance(a, float) and isinstance(b, float) and math.copysign(1, a) != math.copysign(1, b)):
            out["numbers"].append((path, a, b, ulps(float(a), float(b))))
    elif isinstance(a, str) and isinstance(b, str):
        if a != b:
            out["strings"].append(path)
    elif a != b:
        out["other"].append(path)


def compare(pa, pb):
    a = json.load(open(pa), parse_float=float)
    b = json.load(open(pb), parse_float=float)
    out = {"numbers": [], "strings": [], "structure": [], "other": []}
    walk(a, b, "", out)
    hist = {}
    for _, _, _, u in out["numbers"]:
        hist[str(u)] = hist.get(str(u), 0) + 1
    return {
        "numbers_changed": len(out["numbers"]),
        "ulps_histogram": hist,
        "strings_changed": len(out["strings"]),
        "structure_changed": len(out["structure"]),
        "number_paths": [[p, x, y, u] for p, x, y, u in out["numbers"][:2000]],
        "string_paths": out["strings"][:40],
        "structure_paths": out["structure"][:20],
    }


if __name__ == "__main__":
    r = compare(sys.argv[1], sys.argv[2])
    if len(sys.argv) > 3:
        r = {"label": sys.argv[3], **r}
    print(json.dumps(r))
