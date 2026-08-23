# Supply and prebuild freeze

## Supply verifier

- Exact command count: `1`
- Cwd: `projects/chirality-app-dev/frontend`
- Command: `npm run electron:supply-chain`
- Exit: `0`
- Verifier result line: `/Users/ryan/Library/Caches/chirality/electron-dist`
- Verifier stderr: empty
- The surrounding npm lifecycle preamble named only the package and exact
  underlying verifier command. The verifier itself emitted only the exact
  resolved directory.

## Prebuild ignored-artifact inventory

- File/symlink count across `dist`, `dist-electron`, `.next`, and `artifacts`:
  `742`
- `du -sk`:
  - `dist`: `1447628`
  - `dist-electron`: `3840`
  - `.next`: `202564`
  - `artifacts`: `956`

## Prebuild semantic hashes

```text
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  scripts/verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  scripts/pack-electron-with-supply.mjs
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  electron/runtime-host.ts
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  src/__tests__/electron/runtime-host-socket-path.test.ts
```

The R19 package command had not started when this inventory froze.
