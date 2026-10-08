"""RV124: for each named type, its definition (enum/struct) body, and any String/Box<str>/Cow field in it."""
import re, sys, os
root = sys.argv[1]; names = sys.argv[2:]
srcs = {}
for d, _, fs in os.walk(root):
    for f in fs:
        if f.endswith('.rs') and not f.endswith('_tests.rs'):
            srcs[os.path.join(d, f)] = open(os.path.join(d, f)).read()
for n in names:
    found = False
    for p, t in srcs.items():
        for m in re.finditer(r'\b(?:pub(?:\([^)]*\))?\s+)?(enum|struct)\s+' + n + r'\b[^{;(]*([{(])', t):
            i = m.end() - 1; depth = 0; j = i
            open_c, close_c = t[i], '}' if t[i] == '{' else ')'
            while True:
                if t[j] == open_c: depth += 1
                elif t[j] == close_c:
                    depth -= 1
                    if depth == 0: break
                j += 1
            body = t[i:j + 1]
            hits = re.findall(r'[^\n]*\b(String|Box<str>|Cow<)[^\n]*', body)
            lines = [l.strip() for l in body.split('\n') if re.search(r'\bString\b|Box<str>|Cow<', l)]
            print(f"{n} ({os.path.relpath(p, root)}): {'NO String-bearing field' if not lines else lines}")
            found = True
    if not found:
        print(n, 'NOT FOUND')
