# Exact PKG09 D121 carrier application

Verdict: `READY_AFTER_PARENT_RELEASE`; no live carrier has been changed.

## Frozen identity table

| Carrier | Owner | Current/frozen preimage SHA-256 | Accepted postimage SHA-256 |
|---|---|---|---|
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_STATUS.md` | PKG02 | `da18f6ef905840270718f88947fcbfdd13d26609f1c9a06522f1463385999ecd` | `af33c2623097cdffb3eedb58819a0bfbdf8c5dcb987b4f13befbeed6b72b1960` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md` | PKG09 | `d8152c669ca3e57768004e184ec75ac9aaccaba5791d96589547e017545c1fe0` | `0f4b65b53eef04a1108f1cfddc082a98be465e1655faf019c5a98643356f11f25` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/ScopeOfWork.md` | PKG09 | `1fed47a10b3f480a545947e6cf1d60ef7e150f166caceb4a26c0267f92dde652` | `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0` |

Accepted patch:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_RULED_INCREMENT_2026-09-06/pdf-application/ACCEPTED.patch`

SHA-256: `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32`.

The full patch is `+12/-3` over exactly three carriers: DEL-02-03 status `+1/-0`, DEL-09-06 status `+8/-0`, and DEL-09-06 SOW `+3/-3`. `git apply -p0 --check` passes at current HEAD `f3f68d744fc745996776cfbe8f30cbd2bb7b100a`; all three carriers are byte-identical to their `9428e4af44c91063f2188e31698e4c84d8549be9` versions.

## Gate state

- `SATISFIED`: D121 ruling and A-design/A-proof are observable on `origin/main` `9428e4af44c91063f2188e31698e4c84d8549be9`; no repeat vote is due.
- `SATISFIED`: accepted patch, design, preserved postimages, and packet manifest rehash exactly.
- `SATISFIED`: current PKG09 carrier preimages match the frozen accepted preimages; V3-07 is absent from live status.
- `SATISFIED_FOR_PREPARATION`: current APP-HOLD reliance and accepted-dependency-consumption both return `ALLOW` for DEL-09-06 at HEAD `f3f68d744fc745996776cfbe8f30cbd2bb7b100a`, register `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc`, scan `b30a546177fbdf6ea49e3407f8b1df994b83061c7024cc0dfe6ccabc646af437`. The parent preflight at `9428e4af…` also returned `ALLOW`, with scan `196b62347df4216d0512bdb5e97d34f8e723011f4e033b101667c323332e2bd9`; scan values are HEAD-sensitive and are not copied forward as current.
- `PENDING`: explicit HELP_HUMAN release after Root fixed-head publication/shared-scope coordination.
- `PENDING_AFTER_APPLICATION`: parent-frozen twelve-locus source identity, accepted PKG02 first-ten-locus predecessor, and serialized proof/process lane.

## Exact application procedure after release

From repo root, first recompute all three preimage hashes and require exact equality with the table and preserved `PREPOST_IDENTITIES.json`. Then run a fresh APP-HOLD dispatch check:

```sh
cd projects/chirality-app-dev
python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path WORKING_ITEMS:PKG09:D121_CARRIER_APPLICATION --target DEL-09-06
cd ../..
```

Apply only the two PKG09 hunks from the accepted full patch, retaining the PKG02 hunk for its owner:

```sh
git apply -p0 --check \
  --include='projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md' \
  --include='projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/ScopeOfWork.md' \
  projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_RULED_INCREMENT_2026-09-06/pdf-application/ACCEPTED.patch
git apply -p0 \
  --include='projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md' \
  --include='projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/ScopeOfWork.md' \
  projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_RULED_INCREMENT_2026-09-06/pdf-application/ACCEPTED.patch
```

Require final hashes `0f4b65b53eef04a1108f1cfddc082a98be465e1655faf019c5a98643356f11f25` and `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0`. Validate the live SOW with `tools/scope_of_work/validate_scope_of_work.py ... --json`, derive a fresh review checklist in application evidence, run governance/control-plane checks, and record a factual DEL-09-06 `MEMORY.md`/run-record entry without changing lifecycle or Checking Approval SHA. Frontend gates are skipped for this carrier-only application because no runtime source changes.

Do not fuzz, rebase, manually reproduce, or partially reinterpret a hunk. Any hash/context drift returns to HELP_HUMAN. The exact accepted wording, including “effective only after owner ruling and owning amendment,” remains byte-for-byte; the ruling and application evidence establish current effect.
