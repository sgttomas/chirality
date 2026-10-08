#!/bin/bash
# RV120 B3 ADDENDUM_03: my own pass over the hash-order class at the repair-03 heads (sources extracted read-only with
# `git show` into WT/rv120b3/r3src and r3py): RS, every iteration over a name bound to a HashMap/HashSet (or to
# `indexed`/`strings`) in the reader modules; PY, an AST pass for loops and comprehensions over set-valued expressions.
# Each hit is then read by hand (ADDENDUM_03.md). Usage: class_scan.sh > CLASS_SCAN.txt
cd WT/rv120b3/r3src && python3 - <<'PY'
import re
for f in ["retained_precision.rs","physics_evidence.rs","preview_physics_evidence.rs","physics_source.rs","semantic_contract.rs","source_blocks.rs","derivative.rs"]:
    src = open(f).read().split("\n"); hashed = set()
    for i, l in enumerate(src):
        m = re.search(r"let\s+(?:mut\s+)?(\w+)\s*(?::\s*[^=]*Hash(?:Map|Set)[^=]*)?=\s*(.*)", l)
        if m and (re.search(r"Hash(Map|Set)", l) or re.search(r"\b(indexed|strings)\(", m.group(2)) or "collect::<Hash" in l + " ".join(src[i+1:i+4])):
            hashed.add(m.group(1))
    hits = []
    for i, l in enumerate(src):
        if "#[cfg(test)]" in l: break
        for n in hashed:
            if re.search(rf"\bfor\b[^{{]*\bin\s+&?\s*(?:mut\s+)?{n}\b(?!\[)(?:\s*\{{|\.iter\(\)|\.values\(\)|\.keys\(\)|\.into_iter\(\)|\s*$)", l) or re.search(rf"\b{n}\.(values|keys|iter|into_iter|drain)\(\)", l):
                hits.append((i + 1, n, l.strip()[:150]))
    print(f"RS {f}: {len(hits)} sites"); [print("  ", h) for h in hits]
PY
cd WT/rv120b3/r3py && python3 - <<'PY'
import ast
def setish(node, names):
    if isinstance(node, (ast.Set, ast.SetComp)): return True
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("set", "frozenset"): return True
    if isinstance(node, ast.Name) and node.id in names: return True
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Sub, ast.BitOr, ast.BitAnd, ast.BitXor)): return setish(node.left, names) or setish(node.right, names)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ("union", "intersection", "difference", "symmetric_difference"): return True
    return False
for fn in ["retained_precision.py","compatibility.py","physics_evidence.py","preview_physics_evidence.py","physics_source.py","source_blocks.py","load_reference_evidence.py","load_reference_source.py"]:
    text = open(fn).read(); tree = ast.parse(text); hits = set()
    for func in [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.Lambda, ast.Module))]:
        names = {t.id for n in ast.walk(func) if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name) and setish(n.value, set())}
        for n in ast.walk(func):
            its = [n.iter] if isinstance(n, ast.For) else [g.iter for g in n.generators] if isinstance(n, (ast.ListComp, ast.GeneratorExp, ast.DictComp, ast.SetComp)) else list(n.args) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("list","tuple","next","iter","min","max","enumerate","zip","sum","any","all","map","filter","sorted") else []
            for it in its:
                if setish(it, names): hits.add((getattr(n, "lineno", 0), ast.get_source_segment(text, n)[:140].replace("\n", " ")))
    print(f"PY {fn}: {len(hits)} sites"); [print("  ", h) for h in sorted(hits)]
PY
