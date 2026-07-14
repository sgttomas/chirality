# CHANGE-I0-H1-G Attempts and Mechanical Normalization

All attempts were retained. None wrote a project path or changed candidate,
status, lifecycle, authority, or H1/H2 state.

## Diagnostic attempts

1. The first generic manifest audit used `path` as a zsh loop variable, which
   shadows zsh's command-search path. It stopped with `command not found`
   before any write. The corrected schema-aware read-only audit passed all six
   then-current manifests and 378/378 bindings.
2. The first agent-validator invocation passed `agents` as a file rather than
   using the validator's default discovery. It stopped with `agent file not
   found` before any write. The corrected invocation passed 33 files with zero
   errors and zero warnings.
3. The default Homebrew `python3` lacked pytest. The identical 20-test command
   was rerun with `/usr/local/bin/python3`; all 20 tests passed.

## Exact terminal-blank-line normalization

The staged whole-diff check found one extra terminal blank line in each file.
Each correction removed exactly one final LF byte:

| Path | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `instances/CHANGE-I0-H1-G/LAUNCH_BRIEF.md` | `1cbac68de3cb1db68178625a94587a7ea0f332999472ef64f118bce09f19e8a4` | `ea9ceaca7bcf31a9db129ee93fa847942712b87d1974e910f4c71dd223660f63` |
| `instances/WORKING-I0-PKG01/LAUNCH_BRIEF.md` | `6e88c38262cbcca25b8edeaa21f5fe3ff0fe038775798170cac73a8322931627` | `f6141ba2f62e52416e2297e6677a607df409952496211df6e10c8ca370f7aacc` |
| `snapshots/I0/H1_EVIDENCE/H1_DECISION_SLATE.md` | `faeeacc5405f38a1e3e5d91b7b1ad1a1d5ef2c2b487dd8e97167bf4cb8efe91c` | `dd7f13e81237ea54619edf5bb420949ac3d412c774389aec9624889666d44654` |
| `snapshots/I0/H1_EVIDENCE/HANDOFF_STATE.md` | `a38eec20115e7cfa43dfad7ea75a78e7d87839f53c724a9fa18d010014c31061` | `25f4a1226d3e6246b2fd1106a66a2c53114672f8d2dcf1369477bf75394197cf` |
| `snapshots/I0/H1_EVIDENCE/HELP_HUMAN_ACCEPTANCE.md` | `d0a09b0fc6ede630ba544a222d494527233cf9ab84b179104ea9ac7830e0434e` | `8d0fad512331f5831341634ddb5bebe6a1363e873a224983dbf157dac28939eb` |
| `snapshots/W_P1/ACCEPTANCE.md` | `b1b64e2a6ff8cd0b832f187aa4d729a38165b7574fc953200055cb30a1746635` | `ed2169954363600840ce9a773adecb63e82a39ec4f890e7425f9ae85e1864fc9` |
| `snapshots/W_P1/HANDOFF_STATE.md` | `94107f79aa733dec0880b9aa4fb0e63200447e70f634c25912a4d78fa5c9b62c` | `91822779b7ae1878edab70bf63a9b6c0a5899df2add6fda7d4853ec127288ac2` |

Affected bindings were rebuilt before freeze. The WORKING manifest changed
from `6ae8d61bab3b2e2a02e06a9c08fad0eb1a84eb011a5c9bd6a213aa7791e90eee`
to `096bb62a3e6b02948469479bc761870ee64f6234439aa44d5512af001c349e23`;
the RECON snapshot manifest changed from
`a8c36925daaba4595d8f9a8017bedb840293c54f0ab078e85c9154b5b149eefe`
to `802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74`;
the RECON instance manifest changed from
`ea3a7169f92fe928eca2c64982960809a7f7c7c1ce8bf775b4b927b4ce709080`
to `0d88da31ab15f217ddcbad4ef920d1bd629af08767118a8b1c49b7dd102ea77e`;
and the H1 manifest changed from
`b28fc08be9a40cdb9d913ad31bbd75323308f5c890a23add6cbe48ab2676b081`
to `4c9a71df041a37755cd0c291f3013130245b7d44156cc0bb558370c701394df2`.
The retained RECON attempt continues to record the exact pre-normalization
audit; the current snapshot audit and all current citations bind the rebound
manifests.
