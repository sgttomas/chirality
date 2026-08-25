# Command Record — N3 R14-Amended Empirical Evidence

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**Verdict:** `PASS_WITH_ADMITTED_DENIED_EGRESS_AND_DOCUMENTED_GAPS`

## Read and identity gate

The instance read its sealed brief, `AGENTS.md`, all cumulative R12–R14
instruments, and N1/N2/N2b returns. It independently required the frozen
identities before execution:

- app server: `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`;
- code-mode host: `8f9f6969cd5e69540482d58791f72e4e9b9888e576ae3ad446c422a058b70128`;
- sandbox profile: `17a579161aa13d50b1f5f735c48408ce2ae45000a6fd1a26a4a0d58a045676ab`.

## Per-run mandatory gate

Before every vendor invocation the command sequence:

1. ran `shasum -a 256` on the exact executable and profile;
2. invoked `/usr/bin/sandbox-exec -f <profile> /usr/bin/nc -z -v -G 1
   1.1.1.1 443`;
3. required nonzero exit plus the literal error `Operation not permitted`;
4. invoked the frozen executable with `/usr/bin/sandbox-exec` and
   `/usr/bin/env -i` using only disposable paths and the fixed local input.

`EXECUTION_GATE_INVENTORY.json` and the per-run `raw/*.preflight.*.gz` and
`raw/*.gate_hashes.txt.gz` records preserve all ten gate results.

## Vendor invocations

| Run | Exact invocation purpose | Exit |
| --- | --- | ---: |
| `version` | app server `--version` | 0 |
| `help` | app server `--help` | 0 |
| `codehost-help` | ancillary code-mode host `--help` | 0 |
| `stable` | stable JSONL initialize/config/config-requirements/feature page 1 | 0 |
| `plugins-off` | same config read with `-c features.plugins=false` | 0 |
| `precedence` | session-flag overrides for plugins and three delegation controls | 0 |
| `experimental` | experimental-capable client plus feature page 1 | 0 |
| `feature-page2` | feature cursor `100` | 0 |
| `schema-attempt` | direct `generate-json-schema` negative probe | 2 |
| `types-attempt` | direct `generate-ts` negative probe | 2 |

The negative generation probes failed only because the dedicated entrypoint
does not accept those arguments. No generated output directory was created.
The package `rg` and `zsh` were not invoked because doing so would not produce
R14-B evidence.

## Evidence and containment result

The stable run captured three sandbox-denied plugin destinations and complete
triggering traces. Two plugin-off runs read back the exact switch false and
eliminated all plugin startup attempts. Config/read established user,
untrusted-project, and session-flag precedence; feature pagination completed
118 exact entries. No completed network connection, credential prompt, login
flow, approval grant, `auth.json`, or external write occurred.

All raw textual traces were copied with byte fidelity and deterministically
gzip-compressed (`gzip -n -9`). `gzip -t` passed for every trace; decompression
of the principal stable stderr trace compared byte-identical to its source.
The evidence-whitespace convention is therefore satisfied without altering
the raw semantic record.

After evidence fan-in, the exact current disposable directory, both artifact
quarantines, and two temporary static-string extracts were removed and their
absence verified. The prior-stop evidence archive was read-only provenance,
not a current quarantine, and remained untouched.
