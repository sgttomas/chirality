# M0 pre-dispatch validation

Verdict: `PASS — N1 MAY DISPATCH`

## Basis and citations

- Exact base `33841b30654fb61a7ce559e41d69e79d52a90212`; Receipt 159 validator PASS.
- Authorized fifth clearance identities reverified byte-exact: Stage 1 `3649230d...`, Stage 2 `abf88e19...`, Stage 3 `8a4b86a6...`, normalized Stage 4 `3a0e8235...`, Stage 5 `2d95d467...`, Stage 6 `9a22716a...`; M01 exit 0 for all.
- Authorized ruled ledger reverified at exact SHA-256 `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`; M01 exit 0.
- No prior-root content beyond these seven exact citations was read. Historical-root name enumeration was path metadata only.

## Skeleton and non-circular intake

- Six packet files and two return files existed before dispatch, each exactly its one-line sentinel.
- M02 exit 0: six of six stubs exact, zero filled, census exact sentinel.
- Specs are separate, immutable files with identities pinned in `specs/SPEC_IDENTITIES.sha256`.
- Capsule includes the complete pattern set, rules, pins, scope, time budget, and exact replacement method. Full capsule and SPEC content will be embedded in the dispatch message. N1 requires no read command.

## Manager symmetry and executable probes

Manager scripts are pinned in `manager/MANAGER_SCRIPT_IDENTITIES.sha256`. Binary and transitive interpreter pins are in `allowlists/MANAGER_COMMAND_ALLOWLIST.md`, including resolved real ripgrep and `/usr/bin/perl` for shasum.

| Form | Result |
|---|---|
| M01 citation verifier | exit 0, seven exact identities PASS |
| M02 skeleton validator | exit 0, exact sentinel relation PASS |
| M03 end-to-end filled fixture fan-in | first attempt exit 1 due a relative-path composition defect; manager script repaired before dispatch and re-pinned; retry exit 0 |
| M04 classified rejection fixture | first attempt same relative-path defect; retry exit 2 as expected, five classified hits covering all four patterns |
| M06 progress observer | exit 0, six packet files / 193 bytes / 0 filled / 6 remaining |
| P01–P13 | all exit 0; zsh, Python, Perl, shasum, stat, wc, grep, BSD sed, awk, find, resolved rg, and both harmless zsh syntax fixtures execute |

The M03/M04 repair occurred wholly before child dispatch; no child existed, no packet byte was authored, and the final script identity is `3e7d5dc5d55fe55422385b4ae52aecca36fca1570a14c862fdad69638661765d`. The embedded rg path is the resolved real binary `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg`, pinned at `1c579059...`; both clean and rejecting end-to-end behaviors were executed.

Packet tool preflight available to the author: `/bin/zsh`, `/usr/bin/lldb`, `/bin/ps`, `/usr/bin/shasum`, and transitive `/usr/bin/perl` are readable and pinned. Neutral zsh, LLDB, and shasum forms passed during manager intake. `/bin/ps -p 0 -o pid=` was denied by the sandbox with `operation not permitted`, observed exit 127; the binary exists/readable/pinned and process observation is necessary to identify the trace target, so it meets OWNER_PREFLIGHT criteria. LLDB attach is REVIEWED_NOT_EXECUTED because neutral attach would be operative.

## Historical-identity classification

The full four-pattern set is present in the capsule. It is permitted only on rules/spec/control surfaces. M03 proves filled-stub zero-hit classification. M04 proves exact pattern/file/line classification and rejection. `validation/ELEVENTH_SCAN_CAUSAL_EXPLANATION.md` records the Receipt-159-based causal account without reading the eleventh root.

## Gate

All pre-dispatch obligations are dischargeable. N1 is bounded to exact sentinel replacement by apply_patch only. No execution authority exists.
