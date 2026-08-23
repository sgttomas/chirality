# Full-suite cure pre-run freeze

- Agent: `A2-PKG09-R18-FULLTEST-CURE-01`
- Basis: `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`
- Index: empty
- Candidate diff: `candidate.pre.diff`
- Candidate diff bytes: `16238`
- Candidate diff SHA-256:
  `12d4ccf9e4de7b0924cfdbf7af6db2e3da9fcf2761eaa5cc49f9dd20d8568b1e`

## Frozen semantic candidate hashes

- `frontend/scripts/verify-electron-dist.mjs`:
  `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`
- `frontend/scripts/pack-electron-with-supply.mjs`:
  `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db`
- `frontend/src/__tests__/scripts/verify-electron-dist.test.ts`:
  `c9c4af600a703afa995f8316ee04eb3160d72ef7f8cba8ec2ce53c7f952cb38d`
- `frontend/src/__tests__/scripts/pack-electron-with-supply.test.ts`:
  `a66af130420412e5a3d9cf48856c1b416234fea5aa78e14e3867b4adfd7664e2`
- `frontend/package.json`:
  `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`

## Retained sandbox diagnostic

- Log: `review-1/full-vitest.log`
- SHA-256:
  `8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19`
- Classification: `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`
- Result: not PASS; exit 1; 21 failed / 1,246 passed / 4 skipped.
- Failure boundary: local TCP/Unix-socket `listen EPERM` only.
