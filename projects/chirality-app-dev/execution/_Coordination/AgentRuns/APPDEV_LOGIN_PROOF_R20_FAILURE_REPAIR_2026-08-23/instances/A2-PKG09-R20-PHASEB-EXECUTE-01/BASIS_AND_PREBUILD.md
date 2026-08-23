# Phase-B basis and prebuild freeze

- HEAD: `cb008dc5d6aa9b249639c91f3453a18609530d0f`
- Parent: `a702dd6ec5005b361c8c023b12b599a425e5e2b8`
- Frontend tree: `b4c73edda1fe3346815ce75449b2327c80c79bf8`
- Branch: `codex/app-login-proof-r20-repair`
- Tracked/untracked frontend porcelain excluding ignored build outputs: empty.
- Ignored `frontend/dist` inventory: 465 paths; sorted-path SHA-256 `bd7c06b9e614e5b69682f712dc65051ff50111693a798396978d842b9a9578e8`.
- Prebuild `du -sk`: `dist=1444900`, `dist-electron=3840`, `.next=199836`, `artifacts=956`.
- APP-HOLD reliance: `ALLOW`; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `5604717a7b0950f19850ac9542fd38a98cb883c7b7de2bd968d582abfed5dba7`.

## Prebuild semantic SHA-256

```text
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  scripts/verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  scripts/pack-electron-with-supply.mjs
f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306  scripts/run-packaged-launchagent-login-proof.mjs
6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18  src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531  src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  electron/runtime-host.ts
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  src/__tests__/electron/runtime-host-socket-path.test.ts
```

The supply and package logs plus exit files were preinitialized before either one-shot command.
