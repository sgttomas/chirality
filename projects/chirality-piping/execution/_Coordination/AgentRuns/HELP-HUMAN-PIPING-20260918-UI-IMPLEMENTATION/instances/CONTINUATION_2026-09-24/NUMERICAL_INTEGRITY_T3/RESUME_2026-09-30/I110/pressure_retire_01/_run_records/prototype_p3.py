"""I110 probe-only P3 (never committed): mechanical_fixture_for_test strips the named demo pressure primitives
instead of zeroing them. Usage: prototype_p3.py <lib.rs>"""
import sys
path = sys.argv[1]
s = open(path).read()
anchor = '''        // T0R (M07 containment): omit the demo's realized joint C-150, which
        // the ordinary route refuses (JOINT_ELEMENT_EQUILIBRIUM_UNQUALIFIED).
        input.model.components.retain(|component| component.id != "component:C-150");
        input
    }'''
assert s.count(anchor) == 1
s = s.replace(anchor, '''        // I110 P3 probe: strip the zeroed legacy pressure primitives.
        for case in &mut input.model.load_cases {
            case.primitive_loads.retain(|load| !(load.category == "pressure" && load.magnitude.value == 0.0));
        }
''' + anchor)
open(path, 'w').write(s)
print('applied P3')
