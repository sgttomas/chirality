# WORKING-P2-PKG09 Manager Attempts

## M-01 — disposable verifier interpreter cache

Detection layer: manager verifier fan-in. Failure class: safe mechanical
generated evidence. Reason code: `PY_COMPILE_CACHE`. Three manifest-excluded
interpreter cache files were present after verifier terminalization:

- `build_manifest.cpython-313.pyc` — SHA-256 `65af13cd5d3194bcf97724d472ab0090a13c82057a8e657354f2922ed03e15c6`
- `finalize_verifier.cpython-313.pyc` — SHA-256 `f1dd3730d70d35d905fe56f15653d6b0a143dc4116f49af7447d55d3d75479fe`
- `run_verifier.cpython-313.pyc` — SHA-256 `6f6d53a791393421423f51801b01208dcc1b18fa1386c95b03cc3689ed2bedfa`

Disposition: removed the disposable cache directory and reproduced all 481
terminal manifest bindings. Manifest SHA-256 remained exactly
`82bc36aa0359e9f50fa2fee183f3fcc12b3c94432c2bc5c369b6769d96f9f99e`.
No source, candidate, project, authority, lifecycle, scope, or acceptance byte
was affected.
