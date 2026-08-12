# Minder Semantic Review — D-APP-93 Owner Packet (2026-08-11)

Reviewer: session minder (HELP_HUMAN role, owner-directed review; not the ruled
agent verifier — substitution to be made explicit in the owner freeze ruling).
Basis: the six candidate packet files at
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_TWELFTH_PACKET_AUTHORING_2026-08-10/packet/`
read from `origin/main@43f89f96b6beaac87a448e281be512818eec8a60` (post PR #549).

## 1. Identity basis

Six files re-hashed on the post-#549 tip; all match the twelfth lineage's
`FINAL_INVENTORY.sha256` and the previously staged freeze manifest:

```
1e5c3297553d0320efbc8c0aa01b004a4869585c3143523aa010bf5752ab910b  APPROVAL_REQUEST.md
644161c551518a6312fa823bf5ae6a7f5950324368cee9826562d80821495b76  EVIDENCE_CAPTURE.md
d737413bcc609a97ab3a9e0ccaec6ee892878a86a859a0d00961b8a5dfc69a52  LEDGER_CITATION.md
83c87eefa43eece41281cfe1dfc61d7c34cccf5cd5fdfa86dce5d6f6bcdfc081  OWNER_RUNBOOK.md
c780bfdd579cd445b7007f1341f7c64c3d856ad771d9e4d034225ab19aab81f8  scripts/CAPTURE_TRACE_EVIDENCE.zsh
5d007a54a0bb0df643614fbb27beafbc6e867c986e8d055a12007fd942d5bf70  scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh
```

Aggregate packet identity (SHA-256 of the sorted six-line manifest above):
`db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`

PR #549 scope check: the merge touched only the thirteenth-lineage run root and
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`; no packet path changed.

## 2. Host-environment probes (owner's actual machine, minder authority)

The packet's Step-0 prohibition on agent execution was honored: the packet
scripts were NOT executed. Equivalent independent probes were run instead.

| Fact Step 0 depends on | Result |
|---|---|
| `/bin/zsh` SHA-256 | `528da649…c725e8` — MATCHES pin |
| `/usr/bin/lldb` SHA-256 | `44a68ddc…408698` — MATCHES pin |
| `/bin/ps` SHA-256 | `a1d8c4a0…61115c` — MATCHES pin |
| `/usr/bin/shasum` SHA-256 | `0812595f…3de1e3` — MATCHES pin |
| `/usr/bin/perl` SHA-256 | `626702a7…8c8afd` — MATCHES pin |
| `/usr/bin/lldb --version` | exit 0; first line `lldb-2100.0.17.203` — matches required `lldb-*` shape |
| `/bin/ps -p $$ -o pid=` | exit 0; numeric output — matches required shape |

Conclusion: Step 0 will PASS on this host as it stands today. Residual risk:
a macOS or CLT update before execution would change binary identities and Step 0
would (correctly) stop; execute soon or re-probe after any update.

## 3. Technical review of the LLDB procedure (OWNER_RUNBOOK.md)

- `process handle SIGTERM -s true -n true -p false` is valid LLDB syntax and is
  the correct configuration for the diagnostic question: stop and notify on
  SIGTERM without auto-forwarding it, so the owner controls whether and when the
  signal reaches the target.
- The observation sequence (pre-signal `process status` / `thread list` /
  `thread backtrace all`, then `continue`, then the same triple on stop) is
  sufficient to establish which thread receives SIGTERM, the handler frames,
  and process state — i.e., the causal material for the survival question.
- `process detach` then `quit` leaves the target running; post-detach
  `/bin/ps -p PID` identity check is correct and its "missing process is
  evidence, not conclusion" framing is sound.
- Stop rules are total (hash/identity/attach/topology/rejection/evidence-gap/
  detach classes) and each stop preserves accumulated evidence.
- The packet deliberately does not prescribe helper-PID discovery, the SIGTERM
  delivery mechanism (it defers to "the already-defined external reproduction"),
  or the transcript-recording facility. These are owner burdens, not defects —
  see §6.

## 4. Script review

`OWNER_ENVIRONMENT_PREFLIGHT.zsh`: pinned `PATH=/usr/bin:/bin`; `set -eu`;
argument-count guard; evidence dir must exist, not `/`, not `$HOME` (physical
path compare); hash verification hardcodes the same five pins as the runbook
and the capsule (verified identical); LLDB and ps probes match the runbook's
required shapes (`lldb-*` prefix, zsh numeric pattern `<->`); every check
writes its line to the record before the pass/fail decision, so a failed run
still leaves evidence. `zsh -n` clean.

`CAPTURE_TRACE_EVIDENCE.zsh`: same guards; transcript must exist and resolve
(physical path) inside the evidence directory; requires the evidence copy of
`EVIDENCE_CAPTURE.md` to exist; appends one transcript-identity row. The append
lands under the form's final heading "Transcript identity row appended by
capture script" — form and script are mutually consistent. `zsh -n` clean.

`EVIDENCE_CAPTURE.md`: field set covers run identity, host facts, Step 0
results with the five-pin table, target selection basis, transcript identity,
pre/post-stop observations, stop/detach/cleanup, variance, and a fact/
interpretation separation. No sentinel, no historical-ID pattern hits.

`LEDGER_CITATION.md`: cites the cleared 80-row command-authority ledger by
exact path and SHA-256 `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`
(previously verified against the committed ledger, 80 rows), plus the six
fifth-lineage clearance-record identities. Citation-by-hash only, as required.

## 5. Material finding — APPROVAL_REQUEST.md placeholders (ruling must address)

`APPROVAL_REQUEST.md` contains seven literal `TO_BE_FROZEN_BY_MANAGER`
placeholders (five component hashes, one aggregate, per its design the manager
would fill them during the freeze act). The twelfth manager blocked before that
act, so the candidate index is by-design incomplete. This is not a content
defect, but the owner freeze ruling must supersede the placeholder-filling
step explicitly. Recommended treatment (Option A): freeze all six files AS-IS
(placeholders intact, preserving the verified byte identities above); the
ruling itself carries the six-line manifest and the aggregate identity and
serves as the approval surface in place of a filled APPROVAL_REQUEST.md; the
placeholders remain as historical evidence that the manager freeze never ran.
This also avoids the self-reference problem of writing the aggregate into a
file that is itself part of the aggregate. The runbook's phrase "manager-frozen
byte identity" (line 5) and APPROVAL_REQUEST.md's "manager will replace"
language are likewise superseded by the same ruling clause.

## 6. Owner burdens at execution time (outside the packet, lawful to prepare)

1. Helper-PID discovery is the owner's act: launch Chirality App per the
   established D-APP-92 reproduction, identify the helper process PID by your
   own means, and be able to state the selection basis in the evidence form.
2. SIGTERM delivery is the owner's act via the already-defined external
   reproduction; the packet neither generates nor authorizes the signal.
3. Transcript recording facility is the owner's choice (e.g. `script(1)` or
   terminal logging); record the facility and path in the evidence form.
4. macOS debugger authorization: attaching may require Developer Tools access.
   Verifying attachability against a scratch process of your own BEFORE packet
   approval is outside the packet and lawful; doing so avoids consuming the
   approved run on a permissions stop.

## 7. Verdict

PASS with one required ruling clause (§5). The procedure is technically sound
for the D-APP-93 causal-trace objective; the scripts are safe, contained, and
consistent with the runbook and form; every Step-0-checkable environment fact
already verifies on the execution host. No content change to any of the six
files is needed or recommended.
