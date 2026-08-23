# Pre-cure semantic freeze

- Sandboxed diagnostic command count: `1`
- Sandboxed result: exit `1`; 22 failed / 1,245 passed / 4 skipped
- Frontend tree: `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`

```text
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52  scripts/run-packaged-launchagent-login-proof.mjs
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  scripts/verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  scripts/pack-electron-with-supply.mjs
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  electron/runtime-host.ts
9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595  src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  src/__tests__/electron/runtime-host-socket-path.test.ts
```

The complete semantic candidate diff consists of the tracked `_STATUS.md`
delta plus the new R19 record. Deterministic binary-diff concatenation:

- bytes: `21477`
- SHA-256: `9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`
- status SHA-256:
  `c9e6ff5211ec7faa4d80c3ad30475d9f9a35c88e0844eae2cc6df4dd72de960b`
- R19 SHA-256:
  `73f8d59e31591bf6aaa96429484160e785b8f810ab8e48fc086aa65626e5c7ab`

Executor evidence is excluded from the semantic candidate-diff hash because
it continues to receive the cure and proportional-gate logs. It remains fully
inventoried and App-contained at return freeze.
