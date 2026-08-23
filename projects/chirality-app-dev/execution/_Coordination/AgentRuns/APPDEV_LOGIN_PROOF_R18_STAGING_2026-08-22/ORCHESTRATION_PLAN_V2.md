# DEL-09-04 R18 Electron supply-freeze precursor — orchestration plan v2

Status: `FROZEN BEFORE WP-02 DISPATCH`

This v2 plan supersedes the successful-work objective in v1 without rewriting
v1 or its terminal cache-miss evidence. RunID, manager instance, branch, and
accepted basis remain unchanged.

## Objective and graph

1. Fresh `A2-PKG09-R18-WP02-EXECUTE-02` performs exactly one purpose-limited
   SHASUMS request, implements and tests the fail-closed Electron distribution
   verifier plus safe pack wrapper, runs exactly one offline evidence build,
   then writes R18/status and unique executor-2 evidence.
2. WORKING_ITEMS validates fan-in and freezes remaining non-review bytes.
3. Fresh `A2-PKG09-R18-WP02-REVIEW-01` performs evidence-only full review and
   writes only its unique review record.

Edge: `EXECUTE-02 -> manager fan-in/freeze -> REVIEW-01 -> closeout`.
The executor is the sole overlapping source/R18/status/run-evidence write
owner. At most two repair plus fresh-review cycles are allowed.

## Network and build gates

- One curl request only to the exact HTTPS GitHub SHASUMS URL, redirects
  disabled, no other host, text only. Any failure, redirect, unexpected size,
  absent/different arm64 line, or artifact behavior stops the node.
- No artifact download. The owner-staged zip is read-only and must independently
  pass regular/non-symlink, exact size, and SHA-256 gates.
- The nested `app-builder-lib/node_modules/@electron/get` 3.1.0 cause is cited
  by repo-local source path, line region, and source hash.
- Production pins cannot be bypassed by caller input; explicit dist path is
  literal, default derives only from `os.homedir()`, and hashing is streaming.
- Exactly one new post-implementation `npm run desktop:pack` runs in the
  restricted network sandbox. It must log custom electronDist use, no download,
  preserve embedded dependency/instruction-root gates, and exit zero.
- The resulting ignored package is evidence only and is not adopted as an R18
  proof package. R18 stages no owner procedure; R19 remains separate.

## Hard fences

No additional network request/host/redirect, artifact fetch, second build or
retry, proof package adoption, R19 procedure, GUI, prepare, capture,
logout/login, bootstrap, kickstart, operator/default job/plist/launcher action,
signing, notarization, deployment, distribution, release-readiness or proof
acceptance, Receipt 189, stage, commit, push, PR, or merge. App-only repository
writes and the explicit read-only owner-staged Electron dist are the boundary.
