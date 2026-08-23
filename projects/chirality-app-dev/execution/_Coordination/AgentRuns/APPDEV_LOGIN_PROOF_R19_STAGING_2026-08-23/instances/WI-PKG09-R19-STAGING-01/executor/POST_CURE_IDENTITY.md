# Post-cure identity

The sole local-socket-permitted exact `npm test` exited 1 at 1 failed / 1,266
passed / 4 skipped. It was not rerun.

All pre-cure hashes match exactly after the cure:

```text
9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4  frontend tree
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
141a2e52d9e65e8526f5203350fde5eb23a75f2020228dd5c1b37790763aba52  run-packaged-launchagent-login-proof.mjs
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  pack-electron-with-supply.mjs
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  runtime-host.ts
9338631ef1b295806e17f8be85ffd1a3600c51e68c27d014fc485278a500f595  login-proof test
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  runtime-host socket-path test
```

Before the calibrated R19/status blocker amendment, the same complete
semantic candidate diff remained 21,477 bytes with SHA-256
`9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`.
The later R19/status byte changes only record the observed failure; they do not
change product source, tests, packages, manifests, or the built frontend tree.

The exact proof root remains absent and the index remains empty.
