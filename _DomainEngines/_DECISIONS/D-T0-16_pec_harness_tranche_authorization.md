# D-T0-16 - PROPOSAL: PEC harness tranche authorization

**Status:** PROPOSAL / awaiting owner ruling.  
**Date prepared:** 2026-07-04  
**Decision ID:** D-T0-16  
**Prepared by:** PEC work loop agent under the standing plan. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Decision to rule

Authorize or defer the harness code tranche that makes PEC a harness-aware
domain-engine profile after the registration package lands.

## Verified facts

| Fact | Source |
|---|---|
| Current project aliases include app-dev and piping only. | `tools/practitioner_harness/harness.py:61-66` |
| Current bridge-status register/profile/project awareness includes app-dev, piping, tier-0, and `open_pipe_stress` only. | `tools/practitioner_harness/cmd_bridge_status.py:73-104` |
| Current self-check default scope includes app-dev, piping, `_DomainEngines`, and governance harness only. | `tools/practitioner_harness/cmd_self_check.py:216-222` |
| Current reference resolution checks app-dev and piping project-relative references only. | `tools/practitioner_harness/cmd_self_check.py:982-995` |
| The adapter currently loops over `_DomainEngines/profiles/*.yaml` and writes a single observation's profile fields. | `tools/practitioner_harness/adapter_domain_engines.py:103-131` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Authorize the TOOLMAKER brief as one later PR after the registration package lands. | Enables multi-profile safety, PEC alias/register/status awareness, and profile movement into `_DomainEngines/profiles/`. |
| O-B | Authorize only the multi-profile adapter fix; defer PEC harness awareness. | Reduces risk but leaves PEC mostly staged. |
| O-C | Defer the whole harness tranche. | Keeps PEC registered only in docs/profile staging. |
| O-D | Custom tranche scope. | Owner supplies a narrower or broader scope. |

## Recommendation

Recommend O-A after this registration package is accepted. The tranche should
carry conscious live-baseline pin updates and full practitioner harness pytest
at the final SHA.

## Human ruling

HumanRuling: OPEN - awaiting owner ruling.
