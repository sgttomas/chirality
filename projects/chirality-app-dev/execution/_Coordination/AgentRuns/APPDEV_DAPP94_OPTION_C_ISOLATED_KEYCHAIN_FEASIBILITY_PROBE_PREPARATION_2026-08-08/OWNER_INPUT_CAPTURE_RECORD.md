# D-APP-94 Option C owner input-capture record

Status: `OWNER-ATTESTED IMMUTABLE INPUT — ACCEPTED FOR PREPARATION`

The owner personally ran the two commands authorized by
`INPUT_CAPTURE_AUTHORITY_ADOPTION_V1.md` in the intended security session and
reported use of shell builtin `echo $?` for each exit status.

| Command | Complete stdout object | Exit-status object |
|---|---|---|
| `/usr/bin/security default-keychain -d user` | `inputs/default-keychain.stdout.txt` | `inputs/default-keychain.exit-status.txt` (`0`) |
| `/usr/bin/security list-keychains -d user` | `inputs/list-keychains.stdout.txt` | `inputs/list-keychains.exit-status.txt` (`0`) |

Each stdout object contains exactly one four-space-indented, double-quoted path
line terminated by LF:
`/Users/ryan/Library/Keychains/login.keychain-db`. The default restoration
operand and the complete ordered one-element search-list restoration operand are
therefore both literal and identical to that path.

No keychain item, password, credential, environment, process, or other output
is part of this accepted input.
