# Frontend Premerge Check Evidence Normalization

Verdict: `PASS`.

The registered runner wrote one scratch preimage (13,852 bytes, SHA-256
`be4026f9656830a235746045b83f870bf10aaff0e427edcaa087cd5cd325ee76`)
before promotion. The planned evidence pipeline replaced exactly 23 checkout
root strings with `~` and exactly four machine temporary-root strings with
`${TMPDIR}`, producing the accepted `PROJECT_CHECKS_PREMERGE.json`
postimage (12,868 bytes, SHA-256
`83714cb1d6e9a3dd84ef53827909ed776f7a20760973e25008457eb0c8cf260a`).

Reverse substitution reproduced the exact scratch preimage hash. The
postimage parses, its registered `frontend-premerge` result remains PASS
with exit code zero, and it contains zero checkout-root, machine-temp, or
local-file URI strings. The scratch preimage was removed after promotion.
