# Brief amendment 01 — exact retry for locked Electron retrieval

- Disposition: `REPLAN / AUTHORIZE EXACT RETRY`
- Applies to: `A2-PKG09-R16-EXECUTE-01`
- Detection: the first exact `npm run desktop:pack` exited `1` only after
  Electron Builder encountered a cache miss for pinned Electron `43.2.0`
  arm64 and sandbox DNS returned `getaddrinfo ENOTFOUND github.com`.
- Preserved evidence: `executor/desktop-pack.log` and its exit record.

This is an operational sandbox/cache failure, not an App authority fence. The
executor may request sandbox escalation and rerun the exact same tracked
command once from the exact frontend cwd, with network permission limited by
purpose to Electron Builder's pinned Electron `43.2.0` arm64 artifact
retrieval. Preserve the full retry log separately under
`executor-attempt-2/desktop-pack.log` and its exact exit status.

No dependency/package/lockfile/source update, alternate command, provider
expansion, prior-temp read/adoption, GUI/proof/operator action, signing,
notarization, deployment, Git mutation, or further retry is authorized. All
other brief requirements and fences remain in force.
