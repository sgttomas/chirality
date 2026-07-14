# Retained Verifier Failure Attempt 1

Member: `DEL-03-07`
Checkpoint: 3, first converter reproduction
Classification: verifier-local harness binding failure
Reason code: `REF_LIST_WHITESPACE_NOT_NORMALIZED`

The first harness attempt passed `scope_refs` and `objective_refs` values after
splitting the frozen comma-separated fields without trimming the leading space
from later values. The fresh converter therefore emitted doubled spaces in the
frontmatter, traceability sentence, and matrix row. Its SHA-256 was
`57faa6cdc1330940cec3945534567ca193954e1eabbb9a440427739d80ef7237`,
not the accepted evidence SHA-256
`2c5dece5094332698991983931a48fcb7100765359a8dfe5a2bcc30c9c120916`.

No candidate or project file was written. The incomplete verifier-local member
folder is retained under `attempts/attempt1/DEL-03-07/`. Remediation trims each
list item before invoking the registered converter and restarts DEL-03-07 from
checkpoint 1. No acceptance gate is weakened.
