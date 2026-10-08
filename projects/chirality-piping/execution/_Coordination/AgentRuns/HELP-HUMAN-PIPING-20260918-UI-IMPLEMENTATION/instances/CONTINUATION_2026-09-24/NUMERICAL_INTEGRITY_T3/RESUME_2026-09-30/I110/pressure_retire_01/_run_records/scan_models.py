import json, os, sys, collections
root = sys.argv[1]
skip = ('/execution/', '/node_modules/', '/target/', '/.git/', '/_run_records/')
out = []
def is_model(d):
    return isinstance(d, dict) and 'pipe_segments' in d and 'nodes' in d and 'load_cases' in d and 'schema_version' in d
def walk(o, path, file):
    if is_model(o):
        out.append(summarize(o, file, path))
        return
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, path + '/' + str(k), file)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, path + '/' + str(i), file)
def summarize(d, file, path):
    pc = d.get('pressure_contract')
    pcs = None if pc is None else f"{pc.get('version')}/{pc.get('mode')}" if isinstance(pc, dict) else repr(pc)
    pl = []
    regions = 0; eqs = 0
    for c in d.get('load_cases') or []:
        if not isinstance(c, dict): continue
        if c.get('pressure_regions') is not None: regions += 1
        if c.get('equivalent_static') is not None: eqs += 1
        for l in c.get('primitive_loads') or []:
            if isinstance(l, dict) and (l.get('category') == 'pressure' or l.get('dimension') == 'pressure'):
                m = l.get('magnitude') or {}
                pl.append(m.get('value'))
    sup = d.get('supports') or []
    nl = sum(1 for s in sup if isinstance(s, dict) and s.get('nonlinear') is not None)
    ce = sum(1 for s in sup if isinstance(s, dict) and (s.get('family') == 'constant_effort_support' or s.get('constant_effort') is not None))
    return dict(file=file, path=path or '/', schema=d.get('schema_version'), kind=d.get('document_kind'), contract=pcs,
        pressure_loads=len(pl), nonzero_pressure=sum(1 for v in pl if v not in (0, 0.0, None)),
        regions_cases=regions, components=len(d.get('components') or []), combinations=len(d.get('combinations') or []),
        nonlinear_supports=nl, constant_effort=ce, equivalent_static=eqs, cases=len(d.get('load_cases') or []))
for dp, dn, fn in os.walk(root):
    if any(s in dp + '/' for s in skip): dn[:] = []; continue
    dn[:] = [x for x in dn if x not in ('node_modules', 'target', '.git', 'execution', '_run_records')]
    for f in fn:
        if not f.endswith('.json'): continue
        p = os.path.join(dp, f)
        if os.path.getsize(p) > 200_000_000: continue
        try: d = json.load(open(p))
        except Exception: continue
        walk(d, '', os.path.relpath(p, root))
json.dump(out, open(sys.argv[2], 'w'), indent=1)
c = collections.Counter((r['schema'], r['contract']) for r in out)
for k, v in sorted(c.items(), key=str): print(k, v)
print('total', len(out), 'files', len({r['file'] for r in out}))
