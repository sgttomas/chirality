# W7 launch-brief EOF normalization provenance bridge

Date: `2026-08-03`

Status: `NON_SEMANTIC_PREIMAGE_PROVEN`

## Authority and scope

Owner ruling item 4 authorizes normalization of the three EOF-whitespace
findings. The ruling SHA-256 is
`671dd05838c75a0e885052f52e951ab5609ac44b4db66a90f0fe283cba071aea`.
W8 limits the repair to one surplus terminal LF in exactly the three launch
briefs below. No semantic candidate, admitted decision-support member, package
manifest, child return, or execution-time status was rewritten.

## Exact preimage and normalized identities

| File | Execution-time / preimage SHA-256 | Normalized current SHA-256 | Bytes before → after | Re-append-one-LF proof |
|---|---|---|---:|---|
| `children/AUTHOR/attempt-3/LAUNCH_BRIEF.md` | `334ed4961681edca3ee2f8418df8fc2a07a445fcf878d4d21a4ef5fe62c065aa` | `09aded2e4228a1316883cc5dcb4a47764ea994222e99d8f6675e259a1b97e86f` | `5772 → 5771` | `SHA256(normalized_bytes + LF) = 334ed496...065aa` |
| `children/VERIFY/LAUNCH_BRIEF.md` | `f8f96df356cc746188c7ff9fa74e1cfaac9e78880c8690430f87add17df73063` | `4483b792ddaec10272e87635e21ecde8b4217fb427c2ebcc3557c906ea65b0c8` | `7172 → 7171` | `SHA256(normalized_bytes + LF) = f8f96df3...063` |
| `children/VERIFY/R2/LAUNCH_BRIEF.md` | `fea2ef22265313f7b95f51c5202279f073dace943634da29a276cf25f9fe7bb3` | `9c686a961094aa9b8b17c371f6b760ed329e1ff23b9d1733af7d482b61829ced` | `7007 → 7006` | `SHA256(normalized_bytes + LF) = fea2ef22...7bb3` |

For each file, the preimage ended in exactly two LF bytes and the normalized
file ends in exactly one LF byte. Removing that one final byte was the complete
change. Re-appending exactly one LF to each normalized byte string reproduces
the full former byte string and its execution-time SHA-256 exactly.

## Citation reconciliation

The following surviving citations intentionally retain execution-time hashes:

- author attempt-3 launch `334ed496...065aa`: W7 `RETURN.md`, attempt-3
  `AUTHOR_RETURN.md`, R2 `LAUNCH_BRIEF.md`, and R2 `VERIFIER_RETURN.md`;
- verifier-1 launch `f8f96df3...063`: verifier-1 `VERIFIER_RETURN.md`;
- verifier-R2 launch `fea2ef22...7bb3`: W7 `RETURN.md` and R2
  `VERIFIER_RETURN.md`.

Those statements are immutable claims about the exact bytes read during the
recorded executions and remain true. They were not replaced with normalized
hashes. Consumers inspecting current repository bytes must use the normalized
identities in this bridge. Consumers reconstructing execution-time inputs must
append one LF and use the preimage identities. This bridge is the reciprocal
mapping between those two valid provenance contexts.

## No-effect boundary

The normalization does not alter launch semantics, author/verifier results,
the W7 `ADMIT`, the owner ruling, or the admitted package. It performs no option
selection, semantic adoption, N0 restart, implementation/runtime check,
foreign or Task Management write, lifecycle/release/reliance act, or Git
operation.
