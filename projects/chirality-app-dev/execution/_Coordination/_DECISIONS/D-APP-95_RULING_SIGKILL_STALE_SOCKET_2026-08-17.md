# D-APP-95 — SIGKILL stale-socket residual

Status: `RULED — A1`

DecisionID: `D-APP-95`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**A1 — SIGKILL stale-socket residual, DEL-09-04.**

Recover-on-start — unlink the control socket and owner record only when the path is a socket owned by this uid and the recorded owner pid is demonstrably absent, otherwise refuse — is the accepted and complete handling for a SIGKILLed daemon. Nothing further is owed. Remove the item from DEL-09-04 Remaining and record the ruling in its History.
```

## Effect

The exact DEL-09-04 residual is discharged. This recording tranche changes no
product/runtime bytes, lifecycle state, Checking Approval SHA, release posture,
or foreign-loop state.
