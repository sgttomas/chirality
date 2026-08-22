# Brief amendment 01 — bounded cache-miss retry

The first exact `npm run desktop:pack` attempt compiled the application and
failed only because Electron Builder could not resolve `github.com` while
fetching the pinned, uncached Electron `43.2.0` arm64 artifact. That first
attempt is retained in `executor/desktop-pack.log` and `executor/RETURN.md`.

The owner-directed package rebuild authorizes a second exact attempt with a
narrow sandbox escalation for the dependency download already selected by the
tracked lockfile/package manifest. This does not authorize changing or
installing dependency versions, running `npm install`, broad browsing, GUI
launch, proof execution, signing/notarization/distribution, operator deployment,
or mutation of the forbidden label/plist/launcher paths.

For attempt 2:

- request escalation only for exact `npm run desktop:pack` from `frontend`;
- preserve the attempt-1 log; write attempt-2 evidence separately;
- retain every original brief boundary and return requirement;
- if the narrowly escalated exact command still fails, return the calibrated
  blocker without broadening or using an alternate package command.

