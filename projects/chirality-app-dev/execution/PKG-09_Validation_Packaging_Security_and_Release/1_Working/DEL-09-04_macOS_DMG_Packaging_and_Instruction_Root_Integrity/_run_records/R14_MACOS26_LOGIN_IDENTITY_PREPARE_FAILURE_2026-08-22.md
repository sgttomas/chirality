# DEL-09-04 macOS 26 login-identity preparation failure

- Date: `2026-08-22`
- Run: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- Authority: owner-authorized repair direction transcribed in the run root
- Result: `OWNER-REPORTED PREPARE FAILURE — NO PROOF`
- Deliverable state: `IN_PROGRESS`

## Owner-reported attempt

The owner reported that the R13 Phase 1 Terminal attempt stopped with the
exact error:

```text
Current GUI login-session identity is not valid JSON
```

The attempt failed before proof preparation completed. The owner reported no
proof plist and no proof job; only the old empty proof root proposed in R13
exists. No logout/login or capture followed. This is evidence of a failed
attempt, not a passing proof, lifecycle acceptance, publication, release,
signing, notarization, distribution, issuance, or reliance.

The prior detector depended on JXA importing CoreGraphics and serializing
`CGSessionCopyCurrentDictionary`. The exact error is consistent with that probe
returning bytes that its JSON parser could not accept on the owner's current
host. This causal diagnosis is grounded in the then-current source path; it
does not upgrade the owner-reported no-plist/no-job state into an independent
live observation.

## Observation boundary

The repair manager independently performed a read-only `stat` and one-level
`find` of the old R13 proof root. That observation confirmed the root exists as
an empty mode-`0700` directory. It did not mutate the root. The no-plist/no-job
claim remains owner-reported: this repair run did not inspect
`~/Library/LaunchAgents`, a proof or operator service/job, or the CLI launcher.
It did not run a service-level `launchctl print`, bootstrap or kickstart a
label, launch the GUI, prepare, or capture. The only live login-session
observation made after repair is the strictly read-only detector preflight
recorded in R15.

DEL-09-04 remains `IN_PROGRESS` and unproved. The repaired bytes must pass
review, be committed, and be rebuilt into a new unsigned package before a new
executable owner procedure can be staged.
