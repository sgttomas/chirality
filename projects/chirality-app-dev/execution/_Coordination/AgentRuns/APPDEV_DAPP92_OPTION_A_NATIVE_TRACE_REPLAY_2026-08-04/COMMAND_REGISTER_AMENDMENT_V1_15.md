# Command-register amendment v1.15 — Attempt-7 timing-only mock retry

Status: `OWNER APPROVED — FROZEN BEFORE C231`

The complete operative C231-C244 graph is incorporated without amendment
from `COMMAND_REGISTER_AMENDMENT_V1_15_PROPOSED.md`, whose exact SHA-256 is:

`5f4d65f1c44caae38e7ae7499b2cff2c2e489338f67c2decb394f09c1f6677aa`.

The exact owner token is transcribed in
`OWNER_ATTEMPT7_PREPARATION_APPROVAL_ADOPTION.md`. The v2 controller and
unchanged second-session scripts remain frozen at the SHA-256 identities
stated in the adopted proposal and adoption record.

Only C231-C244 are executable under this amendment. C242 is mandatory after
every C235 invocation and always precedes C243. C243-C244 are mandatory after
C234 on every terminal path when C242 has proved session A terminal. Stop on
any hash mismatch, pre-existing root, readiness/output/schema/PID/state
mismatch, early or non-natural child exit, timeout, command deviation, or
cleanup failure. No retry or alteration is authorized.

This amendment grants no LLDB, attach, package/reconstruction, cache seed,
network, helper, GUI, signal, replay, credential, memory or environment dump,
process inspection, product remedy, release, Git, Task Management,
foreign-loop, or other authority. C196/C197 remains separately approved but
unused. A pass authorizes preparation of a fresh real-runtime packet only; it
does not authorize that packet's commands.
