# Full-suite cure post-run freeze

- Exact command count: `1`
- Exact command: `npm test`
- Exact cwd:
  `projects/chirality-app-dev/frontend`
- Permission classification: owner-approved execution-tool elevation for local
  loopback/Unix-socket test binding only; no network request, URL, or network
  tool.
- Exit: `0`
- Result: 155 test files passed / 1 skipped; 1,267 tests passed / 4 skipped.
- Complete whitespace-normalized returned-output log:
  `npm-test.unrestricted.log`
- Log bytes / SHA-256: `485` /
  `f7313d0e79460d09de5b09f055e75c7a7fc8d9561a6ed238ce1a4ae6bf68cb92`

The log's sole normalization removed the surplus blank terminal line reported
by staged-equivalent whitespace checking. No substantive returned output was
changed and the command was not rerun.

## Exact before/after equality

| Candidate path | Pre/post SHA-256 |
|---|---|
| `frontend/scripts/verify-electron-dist.mjs` | `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457` |
| `frontend/scripts/pack-electron-with-supply.mjs` | `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db` |
| `frontend/src/__tests__/scripts/verify-electron-dist.test.ts` | `c9c4af600a703afa995f8316ee04eb3160d72ef7f8cba8ec2ce53c7f952cb38d` |
| `frontend/src/__tests__/scripts/pack-electron-with-supply.test.ts` | `a66af130420412e5a3d9cf48856c1b416234fea5aa78e14e3867b4adfd7664e2` |
| `frontend/package.json` | `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc` |

The complete tracked-plus-no-index candidate diff remains exactly 16,238
bytes with SHA-256
`12d4ccf9e4de7b0924cfdbf7af6db2e3da9fcf2761eaa5cc49f9dd20d8568b1e`;
byte comparison with `candidate.pre.diff` passed. Therefore no source, test,
or package-script byte changed between runs.

## Updated documentation hashes

- R18:
  `f7ac51f841c87d8f56ed96b2dc8efcad7a25954eabcf492e072a8e8c2a44e303`
- DEL-09-04 `_STATUS.md`:
  `cafdd98b81e73705b642928b46e1240fd0a8b5f42caa2208fa11547983deba1a`
- Harvest-only TM candidate:
  `2ad6e115196082f52d0763f87161bde1b237847ed265e7be401b0f7ef0c3e284`

The retained sandbox diagnostic remains not PASS at 21 failed / 1,246 passed
/ 4 skipped and remains classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`.
DEL-09-04 remains `IN_PROGRESS` and unproved; the package remains evidence
only and non-adopted; R19 remains separate.
