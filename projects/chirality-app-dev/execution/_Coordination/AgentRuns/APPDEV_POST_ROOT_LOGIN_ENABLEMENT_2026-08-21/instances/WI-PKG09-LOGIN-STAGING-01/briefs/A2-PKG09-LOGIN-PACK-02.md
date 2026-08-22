# Sealed brief v2 — A2-PKG09-LOGIN-PACK-02

- RequestedBy: `WI-PKG09-LOGIN-STAGING-01`
- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-STAGING-01`
- ChildInstanceID: `A2-PKG09-LOGIN-PACK-02`
- AgentType: fresh ephemeral generalist Agent 2 (no delegation)
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- AcceptedBasis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Predecessor: A2-PKG09-LOGIN-PACK-01 attempt 1 compiled successfully but
  failed when Electron Builder could not resolve GitHub for the pinned,
  uncached Electron 43.2.0 arm64 artifact. Its evidence is immutable input.

## Objective

Run the exact owner-directed unsigned app-directory packaging command from
`projects/chirality-app-dev/frontend`, using narrowly escalated network access
only for Electron Builder's locked Electron 43.2.0 artifact retrieval, then
return a current packaged app and complete identity/containment evidence.

## Declared reads, tools, and writes

Read root instructions; run plan/transcription; DEL-09-04 status and R12;
owner launcher ruling; build profile/docs; package/lock manifest; predecessor
return/log; current Git state. Tools: read-only shell inspection and exact
`npm run desktop:pack` with `require_escalated`. Do not run `npm install`,
change package/dependency/lockfile bytes, or perform other network actions.

Writes are limited to documented ignored build/evidence outputs under
`projects/chirality-app-dev/frontend/{.next,dist-electron,dist-runtime,dist,artifacts}`
and this instance's `executor-attempt-2/**`. No tracked source edit is allowed.

## Required execution and return

1. Record exact 40-character HEAD, branch, Node/npm versions, and porcelain
   status before execution.
2. Record read-only before identity/hash observations for the forbidden
   operator label, plist, and launcher where safely available. Never mutate.
3. Request sandbox escalation for exact `npm run desktop:pack` with a narrow
   explanation that the pinned Electron artifact must be downloaded. Execute
   no alternate command.
4. Do not launch `Chirality.app`, run `prepare`/`capture`, or invoke any
   mutating `launchctl` action.
5. On success, verify the absolute app path, safe app metadata, arm64 main
   executable, and unsigned/adhoc posture without modifying the bundle.
6. Inspect current instruction-root summary: require `status: pass`, current
   build Git SHA, source/bundle `agents/AGENT_HELP_HUMAN.md` SHA-256
   `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`,
   and matching source/bundle bytes.
7. Prove `git diff --stat <build-commit>..HEAD -- projects/chirality-app-dev/frontend`
   is empty and record post-command porcelain status.
8. Repeat forbidden-target observations; require no change.
9. Write `executor-attempt-2/RETURN.md` and `desktop-pack.log`; return PASS or
   calibrated blocker. Do not stage, commit, push, open a PR, or write shared
   completion/receipt surfaces.

## Hard fences

Fail closed on GUI launch, proof prepare/capture, bootstrap/kickstart,
logout/login, operator deployment, mutation of `com.chirality.runtime`, its
plist, or `~/.local/bin/chirality`, signing/notarization/distribution,
publication/release/issuance claims, provider expansion, tracked source
mutation, or network use beyond the locked Electron download selected by the
exact package command.

