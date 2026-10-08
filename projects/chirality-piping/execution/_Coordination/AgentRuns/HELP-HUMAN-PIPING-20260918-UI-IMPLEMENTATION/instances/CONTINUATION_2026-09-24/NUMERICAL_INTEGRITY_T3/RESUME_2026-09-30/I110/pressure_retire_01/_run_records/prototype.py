"""I110 probe-only prototype (never committed). Usage: prototype.py <pressure_runtime.rs> P1|P2
P1: refuse the 1.0.0/legacy_pressure_v1 label on 0.3.0 with PRESSURE_MODEL_REAUTHOR_REQUIRED, and remove the
    test-only historical-scope bypass of the nonzero legacy-pressure refusal (zero-valued primitives still pass).
P2: P1, and refuse every pressure primitive in a non-exact document, zero included."""
import sys
path, mode = sys.argv[1], sys.argv[2]
s = open(path).read()
old_label = '''            Some(contract) => {
                if !matches!(
                    (contract.version.as_deref(), contract.mode.as_deref()),
                    (Some("1.0.0"), Some("legacy_pressure_v1"))
                        | (Some(EXACT_VERSION), Some(EXACT_MODE))
                ) {'''
new_label = '''            Some(contract) => {
                if (contract.version.as_deref(), contract.mode.as_deref()) == (Some("1.0.0"), Some("legacy_pressure_v1")) {
                    problem(diagnostics, "PRESSURE_MODEL_REAUTHOR_REQUIRED", &["pressure_contract"],
                        "the 1.0.0/legacy_pressure_v1 pressure contract is retired; re-author this model to 2.0.0/exact_straight_pressure_v2");
                } else if !matches!(
                    (contract.version.as_deref(), contract.mode.as_deref()),
                    (Some(EXACT_VERSION), Some(EXACT_MODE))
                ) {'''
old_bypass = '''                    // Only named in-crate historical tests can enter this scope; normal builds have no selector.
                    #[cfg(test)]
                    if crate::historical_pressure_reference::active() {
                        continue;
                    }
'''
old_zero = '''                if (load.category == "pressure" || load.dimension == "pressure")
                    && load.magnitude.value != 0.0
                {'''
new_zero = '''                if load.category == "pressure" || load.dimension == "pressure" {'''
assert s.count(old_label) == 1 and s.count(old_bypass) == 1 and s.count(old_zero) == 1
s = s.replace(old_label, new_label).replace(old_bypass, '')
if mode == 'P2':
    s = s.replace(old_zero, new_zero)
open(path, 'w').write(s)
print('applied', mode)
