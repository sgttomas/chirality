# Run summary — DEL-01-05 RF-002 independent rerun

The revised 18-row activation inventory reproduces exactly. The producer
enforcement suite independently reran 19/19 PASS. All three owner-bound
regressions now BLOCK with located findings.

Six fresh sources absent from producer tests exercised imported-symbol,
module-alias, fixed-point callable/class/instance-alias, inline-constructor,
and keyword-endpoint combinations. Four external forms BLOCK with exact
locations; the Unix-domain and IPv6-loopback forms PASS without locality
findings. This supports a general import-binding/AST repair, not a spelling
patch.

`RF-002` is `RESOLVED` on the revised exact hashes. `RF-001` remains `OPEN`
with owner disposition `REVISE` because the final manifest reseal is reserved
until all evidence and review bytes land. DEL-01-05 remains `INITIALIZED`.
