# WORKING-P2-PKG08 Manager Attempts

## M-01 — disposable syntax-check cache

Detection layer: manager helper preflight. Failure class: safe mechanical
generated evidence. Reason code: `PY_COMPILE_CACHE`. `python3 -m py_compile`
created three interpreter cache files while validating the manager helpers:

- `run_package_checks.cpython-313.pyc` — SHA-256 `ef12fd9384b58bc17b9c3a3676ca9cef95c4ff1000617da66cc2db7a9ebc9fb0`
- `build_manifest.cpython-313.pyc` — SHA-256 `6dbe39c0c58d6fa249fb33b0702133a90313a15cfdb2247d2681fa3e22bebeb4`
- `manager_fan_in.cpython-313.pyc` — SHA-256 `03ab49470bc07a3cccfa10761731c34d3e1897b4de3fa587635b441090cc484a`

Disposition: remove the disposable cache directory before manager execution,
then build and verify all terminal bindings. No source, candidate, project,
authority, lifecycle, scope, or acceptance byte is affected.

## M-02 — adapted helper deliverable-prefix assertion

Detection layer: first manager fan-in invocation. Failure class: safe
mechanical helper adaptation. Reason code: `STALE_DELIVERABLE_PREFIX`. The
copied completeness harness correctly selected PKG-08 rows but retained its
PKG-07 expected-ID assertion, so it failed closed before reading or writing
member outputs. Disposition: change only the expected string prefix from
`DEL-07-` to `DEL-08-`, rerun the entire manager fan-in, and rebuild all
terminal bindings. No candidate, project, source, semantic, authority,
lifecycle, scope, or acceptance byte was changed.
