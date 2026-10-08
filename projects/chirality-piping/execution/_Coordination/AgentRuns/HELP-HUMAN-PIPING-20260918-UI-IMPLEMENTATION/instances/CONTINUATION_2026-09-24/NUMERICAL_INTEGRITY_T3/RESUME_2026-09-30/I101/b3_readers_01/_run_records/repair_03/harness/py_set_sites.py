"""I101 repair 03: candidate sites where a PY reader module iterates or renders a set (str sets are hash-randomized per
process: PYTHONHASHSEED). Flags for-loops and comprehensions over, and list/tuple/join/next(iter())/min/max/pop/str/repr/
f-string/format/% of, an expression that is set-valued: set()/frozenset() calls, set literals and comprehensions, set
operators on such values, .keys()/.items() views combined with set operators, set methods (union, difference, ...), or a
name bound anywhere in the module to one of these. A candidate list for review, not a verdict.
Usage: py_set_sites.py <file.py>..."""
import ast, sys

SET_METHODS = {"union", "difference", "intersection", "symmetric_difference"}
RENDER = {"list", "tuple", "next", "min", "max", "str", "repr", "enumerate", "zip", "reversed", "iter"}


def set_names(tree):
    names = set()
    changed = True
    while changed:
        changed = False
        for node in ast.walk(tree):
            targets, value = [], None
            if isinstance(node, ast.Assign):
                targets, value = node.targets, node.value
            elif isinstance(node, ast.AnnAssign) and node.value is not None:
                targets, value = [node.target], node.value
                ann = ast.unparse(node.annotation)
                if ann.startswith(("set", "frozenset", "Set", "FrozenSet", "AbstractSet")):
                    for t in targets:
                        if isinstance(t, ast.Name) and t.id not in names:
                            names.add(t.id); changed = True
            elif isinstance(node, ast.AugAssign) and isinstance(node.op, (ast.BitOr, ast.BitAnd, ast.Sub)):
                targets, value = [node.target], node.value
            if value is not None and is_set(value, names):
                for t in targets:
                    if isinstance(t, ast.Name) and t.id not in names:
                        names.add(t.id); changed = True
    return names


def is_set(e, names):
    if isinstance(e, (ast.Set, ast.SetComp)):
        return True
    if isinstance(e, ast.Call):
        f = e.func
        if isinstance(f, ast.Name) and f.id in {"set", "frozenset"}:
            return True
        if isinstance(f, ast.Attribute) and f.attr in SET_METHODS and is_set(f.value, names):
            return True
    if isinstance(e, ast.BinOp) and isinstance(e.op, (ast.BitOr, ast.BitAnd, ast.Sub, ast.BitXor)):
        return is_set(e.left, names) or is_set(e.right, names) or view(e.left) or view(e.right)
    if isinstance(e, ast.Name):
        return e.id in names
    if isinstance(e, ast.IfExp):
        return is_set(e.body, names) or is_set(e.orelse, names)
    return False


def view(e):
    return isinstance(e, ast.Call) and isinstance(e.func, ast.Attribute) and e.func.attr in {"keys", "items"}


def main():
    for path in sys.argv[1:]:
        tree = ast.parse(open(path).read())
        names = set_names(tree)
        hits = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.comprehension)) and is_set(node.iter, names):
                hits.append((node.iter.lineno, "iterates", ast.unparse(node.iter)))
            elif isinstance(node, ast.Call):
                f = node.func
                fn = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
                if fn in RENDER | {"join", "sorted"} and node.args and is_set(node.args[0], names) and fn != "sorted":
                    hits.append((node.lineno, fn, ast.unparse(node)[:110]))
                if fn == "pop" and isinstance(f, ast.Attribute) and is_set(f.value, names):
                    hits.append((node.lineno, "pop", ast.unparse(node)[:110]))
                if fn == "format" and any(is_set(a, names) for a in node.args):
                    hits.append((node.lineno, "format", ast.unparse(node)[:110]))
            elif isinstance(node, ast.FormattedValue) and is_set(node.value, names):
                hits.append((node.lineno, "f-string", ast.unparse(node.value)[:110]))
            elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod) and isinstance(node.left, ast.Constant) \
                    and isinstance(node.left.value, str) and is_set(node.right, names):
                hits.append((node.lineno, "%", ast.unparse(node)[:110]))
        for line, kind, text in sorted(hits):
            print(f"{path.rsplit('/', 1)[-1]}:{line}: {kind}: {text}")
        print(f"{path.rsplit('/', 1)[-1]}: set-bound names: {sorted(names)}")


main()
