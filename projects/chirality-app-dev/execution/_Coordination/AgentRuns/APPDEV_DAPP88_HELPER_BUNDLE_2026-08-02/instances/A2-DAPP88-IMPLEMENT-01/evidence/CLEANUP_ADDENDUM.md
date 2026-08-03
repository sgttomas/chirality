# Cleanup addendum — exact D-APP-88 temporary trees

Cleanup was performed only after sanitized, claim-bound evidence was copied to
`raw-salvage/` and indexed by SHA-256. Each exact tree below had zero open file
holders according to `lsof -t +D <exact-path>` immediately before deletion.

| Exact path | Files | Allocated bytes | Open holders |
| --- | ---: | ---: | ---: |
| `/private/tmp/chirality-dapp88-childicu.mJyQLr` | 4 | 16,384 | 0 |
| `/private/tmp/chirality-dapp88-childlinks.ggQil7` | 0 | 0 | 0 |
| `/private/tmp/chirality-dapp88-childres.FTGKhJ` | 4 | 16,384 | 0 |
| `/private/tmp/chirality-dapp88-exact-sibling.TFJKQe` | 257 | 289,103,872 | 0 |
| `/private/tmp/chirality-dapp88-final.lCXULO` | 4 | 16,384 | 0 |
| `/private/tmp/chirality-dapp88-flags.ZACdBS` | 4 | 16,384 | 0 |
| `/private/tmp/chirality-dapp88-frameworkid.VooWCM` | 4 | 16,384 | 0 |
| `/private/tmp/chirality-dapp88-gui-control-escalated.MPEQ3Y` | 6 | 20,480 | 0 |
| `/private/tmp/chirality-dapp88-gui-control.Asfm7t` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-helper-escalated.eEadlg` | 6 | 24,576 | 0 |
| `/private/tmp/chirality-dapp88-helper-full.rl1tTr` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-helper-idnamefix.5Toh6P` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-helper-loginitem.9LwzU7` | 2 | 4,096 | 0 |
| `/private/tmp/chirality-dapp88-helper-namefix.5WmLKA` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-helper-r2.74jOKn` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-helper-valid.4oaZCR` | 2 | 4,096 | 0 |
| `/private/tmp/chirality-dapp88-helper.HTt6JO` | 2 | 0 | 0 |
| `/private/tmp/chirality-dapp88-sibling.6nSdX2` | 257 | 289,103,872 | 0 |
| `/private/tmp/chirality-dapp88-trace.PKsuzq` | 4 | 16,384 | 0 |
| **Total** | **566** | **578,359,296** | **0** |

The directories were removed by passing all 19 absolute paths explicitly to
`rm -rf`; no deletion glob or broad parent path was used. The post-delete
command `find /private/tmp -maxdepth 1 -type d -name
'chirality-dapp88-*' -print` emitted no paths, and its count was `0`.
An unsandboxed process-list check found no command containing a D-APP-88
temporary path or `Chirality Runtime Helper`; `launchctl print gui/501` found
no D-APP-88 label or temporary path.
