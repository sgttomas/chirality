# Exact PKG09 D121 carrier application — v2

Verdict: `READY_AFTER_PARENT_RELEASE`; no live carrier has been changed. This file supersedes the failed v1 `CARRIER_APPLICATION.md`.

## Directly computed identity table

| Carrier | Owner | Current/frozen preimage SHA-256 | Accepted and exact-patch-result postimage SHA-256 |
|---|---|---|---|
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_STATUS.md` | PKG02 | `da18f6ef905840270718f88947fcbfdd13d26609f1c9a06522f1463385999ecd` | `af33c2623097cdffb3eedb58819a0bfbdf8c5dcb987b4f13befbeed6b72b1960` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md` | PKG09 | `d8152c669ca3e57768004e184ec75ac9aaccaba5791d96589547e017545c1fe0` | `0f4b65b53f0e05183fcd8a5f489bb2da8ccdb4ead6fab22944f89f8daf42e6ba` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/ScopeOfWork.md` | PKG09 | `1fed47a10b3f480a545947e6cf1d60ef7e150f166caceb4a26c0267f92dde652` | `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0` |

The values were computed directly with SHA-256 over the live preimages, retained postimages, and an isolated `git apply -p0` result. Each isolated result is byte-identical to its retained postimage. The authoritative patch is:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_RULED_INCREMENT_2026-09-06/pdf-application/ACCEPTED.patch`

SHA-256: `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32`.

The patch is `+12/-3` over exactly three carriers: DEL-02-03 status `+1/-0`, DEL-09-06 status `+8/-0`, and DEL-09-06 SOW `+3/-3`. All carrier preimages are unchanged from `origin/main` `9428e4af44c91063f2188e31698e4c84d8549be9` through current HEAD `f3f68d744fc745996776cfbe8f30cbd2bb7b100a`.

## Current gates

- `SATISFIED`: D121 owner A-design/A-proof ruling is observable on `origin/main`; no repeat vote is due.
- `SATISFIED`: accepted patch, design, application packet and all three retained postimages rehash exactly.
- `SATISFIED`: exact patch application from all three current preimages produces the accepted postimages byte-for-byte.
- `SATISFIED_FOR_PREPARATION`: current APP-HOLD reliance and accepted-dependency-consumption return `ALLOW`, with register `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc` and scan `b30a546177fbdf6ea49e3407f8b1df994b83061c7024cc0dfe6ccabc646af437`.
- `PENDING`: explicit HELP_HUMAN release after fixed-head publication and shared-scope coordination.
- `PENDING_AFTER_APPLICATION`: parent-frozen twelve-locus source identity, accepted PKG02 first-ten-locus return, and serialized proof/process lane.

## Exact PKG09 application after parent release

Recompute all three preimages and require literal equality with the table. Then run a fresh dispatch preflight from the App working root:

```sh
/Users/ryan/.local/share/mise/installs/python/3.13/bin/python execution/_Scripts/app_hold.py check \
  --operation dispatch \
  --entry-path WORKING_ITEMS:PKG09:D121_CARRIER_APPLICATION_V2 \
  --target DEL-09-06
```

From repository root, apply only the two PKG09 hunks:

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

Require the PKG09 final hashes `0f4b65b53f0e05183fcd8a5f489bb2da8ccdb4ead6fab22944f89f8daf42e6ba` and `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0`. Validate the live SOW, derive a fresh checklist, run the governance checks with the configured Python, and record factual `MEMORY.md` and `_run_records` evidence without changing lifecycle or Checking Approval SHA. No frontend gates are due for the carrier-only application because no runtime source changes.

Do not use v1, fuzz, rebase, manually reproduce, or reinterpret any hunk. Any identity or context drift returns to HELP_HUMAN before writing.
