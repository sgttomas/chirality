"""I100: two Python sources have the same code apart from docstrings: their ASTs, with every docstring removed,
dump identically. Usage: ast_same.py <a.py> <b.py>"""
import ast
import sys


def stripped(path):
    tree = ast.parse(open(path).read())
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                node.body = node.body[1:] or [ast.Pass()]
    return ast.dump(tree, include_attributes=False)


a, b = stripped(sys.argv[1]), stripped(sys.argv[2])
print("same code apart from docstrings" if a == b else "CODE DIFFERS")
sys.exit(0 if a == b else 1)
