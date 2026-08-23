# REPAIR — final cycle 2 — A2-PKG09-R20-IMPLEMENT-01

Verdict: `PASS`

Basis: owner-authorized `ORCHESTRATION_PLAN_V3.md`, `WORK_GRAPH_V3.json`,
and sealed brief `briefs/A2-PKG09-R20-REPAIR-02.md`. The immutable cycle-1
BLOCKED evidence remains unchanged.

## F-01 through F-05 closure matrix

| Finding | Final implementation | Focused evidence | Closure |
|---|---|---|---|
| F-01 | Computes final PASS once and assigns it before best-effort PASS-only copy deletion. Deletion failure cannot append a cleanup error or retroactively create FAIL; retained/partial state is reported without changing PASS. | Deterministic injected deletion failure returns PASS and leaves both complete token-free copies intact. | `CLOSED_FOR_REVIEW` |
| F-02 | Removes all `/dev/fd` traversal. Canonicalizes and validates all five expected ancestor directories; opens each final log/token path directly with `O_NOFOLLOW`; holds all three descriptors; validates `fstat` type/owner/mode; compares path `lstat` dev/ino; revalidates ancestors and final identities before descriptor-only reads; verifies descriptor stability after reads. Any ambiguity copies neither and retains runtime private-only. | Ordinary safe path passes; `logs`, `auth`, and `tokens` ancestor symlinks fail closed; post-open final-file substitution fails closed with no copy/runtime removal. | `CLOSED_FOR_REVIEW` |
| F-03 | Capture requires both daemon logs. Either or both missing returns explicit private-only preservation and blocks runtime removal. Prepare/install cleanup retains only its justified both-absent allowance. | Zero-log proof-observation failure and one-log later-default-protection failure both retain runtime data and copy neither. | `CLOSED_FOR_REVIEW` |
| F-04 | Detects last-exit field presence independently of content. Empty and whitespace-only values throw; exact `(never exited)` remains the sole noninteger sentinel. | Real fixture, integer, empty, whitespace-only, and other malformed forms pass their assertions. | `CLOSED_FOR_REVIEW` |
| F-05 | A successful bootout that leaves the job loaded but stops the process independently refuses destructive cleanup. | Dedicated case reports job present/process absent, preserves plist/runtime, and retains both intact copies. | `CLOSED_FOR_REVIEW` |

## Helper-complexity accounting

Cycle 2 deletes the nonportable descriptor-relative directory traversal and
its directory-open helper. No module or unrelated abstraction was added.
The remaining bounded helper surface is:

1. `assertSafeSnapshotMetadata`: one shared type, owner, and mode predicate.
2. `sameSnapshotIdentity`: one dev/ino comparison predicate.
3. `validateSnapshotAncestors`: validates exactly the five fixed runtime
   ancestors for lexical containment, canonical equality, directory type,
   ownership, mode, and stable identity across the two validation passes.
4. `readFailureLogSnapshots`: opens exactly three fixed final paths with
   `O_NOFOLLOW`, holds them through revalidation, then reads only their held
   descriptors and verifies stable metadata.

The final tracked candidate is 754 insertions and 28 deletions relative to
HEAD across the one script and one focused test. Cycle 2 reduced the script by
10 net inserted lines relative to the frozen cycle-1 attempt while replacing
the incompatible mechanism; the test and verbatim fixture bytes are unchanged
from cycle 1.
