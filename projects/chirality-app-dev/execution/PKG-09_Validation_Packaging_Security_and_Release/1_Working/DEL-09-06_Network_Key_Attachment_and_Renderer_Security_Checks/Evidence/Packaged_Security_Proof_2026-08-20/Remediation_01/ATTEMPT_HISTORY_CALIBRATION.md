# N1 remediation 01 — source attempt-history calibration

This versioned note corrects the claim boundary for the preserved first source
network-policy attempt at `../source-network-policy/`. It does not alter or
supersede the bytes of that failed attempt.

## Preserved first attempt

- The first attempt started Electron without setting `CHIRALITY_USER_DATA`
  before process launch. Electron therefore began with the owner's default
  user-data path.
- No pre-run or post-run filesystem audit of that default user-data path was
  captured.
- Consequently, the attempt cannot support a claim that owner user-data was
  untouched or that no owner-machine filesystem write occurred.
- The earlier global `ownerUserDataTouched: false` / no-owner-write claim is
  retracted for this first attempt. The absence of a recorded audit remains an
  evidence gap, not evidence of either mutation or non-mutation.

## Credited remediation reruns

Every source proof rerun credited by remediation 01 must set an isolated
`CHIRALITY_USER_DATA` path in its child-process environment before Electron is
spawned. Credited reruns are written only below this `Remediation_01/`
directory and are evaluated independently from the preserved failed attempt.
