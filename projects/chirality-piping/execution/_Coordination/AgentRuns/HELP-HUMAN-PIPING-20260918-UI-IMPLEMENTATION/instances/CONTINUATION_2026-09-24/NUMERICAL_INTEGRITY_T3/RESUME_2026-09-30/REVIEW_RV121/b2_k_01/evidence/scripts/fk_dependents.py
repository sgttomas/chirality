import sys, os, re, tomllib
root = os.path.abspath(sys.argv[1])
crates = {}
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('target','node_modules','.git','execution')]
    if 'Cargo.toml' in fn:
        p = os.path.join(dp, 'Cargo.toml')
        with open(p,'rb') as f:
            try: t = tomllib.load(f)
            except Exception as e: print('ERR', p, e); continue
        deps = []
        for sec in ('dependencies','dev-dependencies','build-dependencies'):
            for k, v in (t.get(sec) or {}).items():
                if isinstance(v, dict) and 'path' in v:
                    deps.append(os.path.normpath(os.path.join(dp, v['path'])))
        for tk, tv in (t.get('target') or {}).items():
            for sec in ('dependencies','dev-dependencies'):
                for k, v in (tv.get(sec) or {}).items():
                    if isinstance(v, dict) and 'path' in v:
                        deps.append(os.path.normpath(os.path.join(dp, v['path'])))
        crates[os.path.normpath(dp)] = (deps, os.path.exists(os.path.join(dp,'Cargo.lock')), 'workspace' in t)
fk = os.path.normpath(os.path.join(root, 'core/solver/frame_kernel'))
dep = {fk}
changed = True
while changed:
    changed = False
    for c, (ds, _, _) in crates.items():
        if c not in dep and any(d in dep for d in ds):
            dep.add(c); changed = True
for c in sorted(dep):
    print(os.path.relpath(c, root), 'lock' if crates[c][1] else 'NOLOCK', 'ws' if crates[c][2] else '')
