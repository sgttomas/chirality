# Integration Contract — APP-HOLD-1 DEL-09-07 Bootstrap

Status: `CANDIDATE_NOT_APPLIED`

## Runtime order

1. Resolve the canonical Git root and exact App paths.
2. Scan every live `ScopeOfWork.md` and determine `CLEAR`/`HELD` exactly as
   before.
3. Load and schema-check all typed register rows.
4. Compare scan-derived holds with `HOLD` rows. Any mismatch blocks before
   target evaluation.
5. Evaluate known targets through ordinary hold behavior. A `HOLD` row always
   blocks; an ordinary known `CLEAR` target remains allowed.
6. Only for an unknown target with the exact structural row, evaluate the
   operation, entry token, three pinned hashes, ScopeOfWork absence, and
   folder shape. Return `ALLOW` plus
   `admission_kind=STRUCTURAL_BOOTSTRAP` only if every predicate passes.

## Exact stable entry paths

- `SCA-APP-009:GATE5:PREPARATION:CANDIDATE_MIRROR`
- `SCA-APP-009:GATE5:PREPARATION:ACTUAL_WORKTREE`

No prefix, suffix, wildcard, alias, case folding, or free-form owner text is
accepted.

## Register contract

Every row uses the exact 19-column header. `HOLD` rows preserve their current
contract fields and set bootstrap-only fields to `NONE`.
`STRUCTURAL_BOOTSTRAP` rows set hold-only fields to `NONE` and must match all
DEL-09-07 constants compiled into the tool. Duplicate deliverable IDs or
record IDs fail closed. The candidate register contains exactly one row, the
DEL-09-07 bootstrap; it contains no active hold row.

The released-target guard remains active for ordinary hold rows. A later
active hold cannot be converted to or overridden by a bootstrap row because
duplicate target IDs are invalid and hold parity is checked before admission.

## Folder contract

The exact target is:

`projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback/`

It may be absent or contain only any subset of the exact five authorized
names. The target folder itself cannot be a symlink. Every observed authorized
name must be a regular non-symlink file. An unexpected name, directory,
nested path, symlink, socket, or other non-regular object blocks.

## Expiry and retirement

The old pointer content is hashed on every check. The separately approved
pointer movement therefore expires the admission without relying on an agent
to edit the register. Appearance of `ScopeOfWork.md` and drift of either
authority postimage produce the same fail-closed result. Later removal of the
inert row is ordinary separately reviewed maintenance; it is not a prerequisite
for expiry.

## Exit codes and result vocabulary

- `0`: all targets `ALLOW`;
- `2`: invalid arguments, unknown nonbootstrap target, malformed register, or
  invalid authority evidence;
- `3`: `BLOCK_APP_HOLD` or `BLOCK_STRUCTURAL_BOOTSTRAP`;
- `4`: `BLOCK_REGISTER_DRIFT`.

The top-level blocked verdict is `BLOCK_APP_HOLD` if any ordinary hold blocks;
otherwise it is `BLOCK_STRUCTURAL_BOOTSTRAP` for a failed bootstrap predicate.

## Caller obligations

PROJECT_SETUP/PREPARATION must run one check from the checkout it is about to
write, with the exact token for that checkout and only target `DEL-09-07`.
The returned JSON must show `ALLOW`, `admission_kind=STRUCTURAL_BOOTSTRAP`, all
predicate booleans true, and no active holds. A passing candidate-mirror check
does not authorize or substitute for the actual-worktree check.

Both dispatches remain governed by their independent SCA-APP-009 owner
authority. APP-HOLD admission is necessary, not sufficient.
