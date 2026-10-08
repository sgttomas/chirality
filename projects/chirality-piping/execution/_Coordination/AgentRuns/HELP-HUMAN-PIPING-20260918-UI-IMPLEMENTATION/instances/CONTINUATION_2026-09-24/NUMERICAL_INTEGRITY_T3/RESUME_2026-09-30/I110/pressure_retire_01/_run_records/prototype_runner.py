"""I110 probe-only (never committed): runner tests strip in-memory pressure primitives instead of zeroing them.
Usage: prototype_runner.py <runner crate dir>"""
import re, sys
root = sys.argv[1]
typed = re.compile(r'for load in &mut case\.primitive_loads \{\s*if load\.category == "pressure" \|\| load\.dimension == "pressure" \{\s*load\.magnitude\.value = 0\.0;\s*\}\s*\}')
value = re.compile(r'for load in case\["primitive_loads"\]\.as_array_mut\(\)\.unwrap\(\) \{\s*if load\["category"\] == "pressure"( \|\| load\["dimension"\] == "pressure")? \{\s*load\["magnitude"\]\["value"\] = (serde_json::)?json!\(0\.0\);\s*\}\s*\}')
total = 0
for f in ['src/lib.rs', 'src/result_envelope_binding.rs', 'tests/preview_physics_admission.rs']:
    p = f'{root}/{f}'; s = open(p).read()
    s, a = typed.subn('case.primitive_loads.retain(|load| !(load.category == "pressure" || load.dimension == "pressure"));', s)
    s, b = value.subn('case["primitive_loads"].as_array_mut().unwrap().retain(|load| !(load["category"] == "pressure" || load["dimension"] == "pressure"));', s)
    open(p, 'w').write(s); total += a + b; print(f, a, b)
print('sites', total)
