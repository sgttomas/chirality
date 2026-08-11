# Eighth-lineage executable non-circular preflight

Status: `BLOCK — F09 EXACT RESTRICTED PROBE EXITED 127 BEFORE N1`

Native context telemetry was unavailable and is not inferred.

## Passed gates

- baseline/origin-main and Receipt 155: PASS;
- 62/62 allowlist paths existing and unique: PASS;
- fifth citation identities 8/8, third ledger, and five template identities:
  PASS;
- five exact F01 whole-file intake reads: exit 0 and complete output;
- five exact F02 re-hashes: PASS;
- F03 full-pattern scratch scan: exit 1, stdout 0 bytes: PASS;
- F04/F05 scratch count: 33 bytes both: PASS;
- F06 executable checks: 23/23 exit 0: PASS;
- F07 pinned-zsh syntax: exit 0: PASS;
- F08 exact `env -i`, `PATH=/nonexistent`, no-rc zsh form: exact
  `SAFE_ENV_OK`, exit 0: PASS.

The five sealed intake identities were:

| File | Bytes | SHA-256 |
|---|---:|---|
| capsule | 8,659 | `5a251c10e7b29cabb2034f894ea674837fab90edc63aa3f3d8a0c9f49d4084b5` |
| brief | 1,818 | `dc99126114e94a91229cbf3b9bf0357ab29bded177684fbcd33466474bcca4d3` |
| read allowlist | 9,560 | `354f3ea2e020e9f3291d074bc7c4b61db18625e29576f29bdfb08245adc1f454` |
| historical fence | 1,201 | `d1f21faed9bb867c07b9745e45638a90c2f9725d0926781794302a31271bced7` |
| diagnostic catalog | 6,637 | `98f4fda49c231d7c22c9d18beaf8004fc3d283b266740ceddf5b16ceb2ee6c44` |

## Terminal F09 failure

The exact restricted probe ran from the eighth run root with:

```text
/usr/bin/env -i PATH=/nonexistent HOME=<eighth scratch home> TMPDIR=<eighth scratch tmp> LANG=C LC_ALL=C /bin/zsh --no-rcs <sealed M0_SAFE_PROBES.zsh>
```

It safely completed `printf`, `sw_vers`, `uname`, and the recursively closed
`shasum -> /usr/bin/perl` probe. At script line 35 it attempted the candidate
component form `/bin/ps -p $$ -o pid=,ppid=,comm=`. The managed host sandbox
returned `operation not permitted`; observed F09 exit was 127. The durable
stdout/stderr record is `scratch/M0_SAFE_PROBE_OUTPUT.txt`.

This was also a design error against the eighth rule that preparation probes
must not touch system state: a process observer should have been classified
as operative `REVIEWED_NOT_EXECUTED`, not placed in the harmless safe-probe
script. The failure occurred after the form was sealed. Retained doctrine says
an exact pre-dispatch probe failure blocks before any child exists. No form
was edited, retried, substituted, or widened after that terminal result.

Verdict: `HOLD N1 — BLOCK_DAPP93_EIGHTH_PREDISPATCH_PS_PROBE_SANDBOX_DENIED`.
