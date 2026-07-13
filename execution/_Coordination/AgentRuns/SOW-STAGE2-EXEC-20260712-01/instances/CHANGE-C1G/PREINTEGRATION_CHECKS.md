# C1G Preintegration Checks

Date: 2026-07-13
Branch: `codex/sow-stage2-canon`
Basis and parent: `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`
Verdict: `PASS`

| Check | Result |
|---|---|
| Branch basis | `PASS`; branch was created directly from the required basis and HEAD remained at that basis before edits |
| Exact live SHA-256 | `PASS`; standard `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f`, TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`, SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27` |
| Exact candidate comparison | `PASS`; `cmp` exit `0` for all three live/candidate pairs |
| Changed canon paths | `PASS`; exactly `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, `docs/TYPES.md`, and `docs/SPEC.md` |
| `git diff --check` | `PASS`; exit `0` |
| Path anchors | `PASS`; `python3 tools/validation/validate_path_anchors.py . --text` reported no literal home-directory paths in 447 live surfaces |
| Instruction entrypoints | `PASS`; `python3 tools/validation/validate_instruction_entrypoints.py .` reported canonical root entrypoints |
| Agent instructions | `PASS`; `python3 tools/validation/validate_agent_instructions.py` reported 33 files, 0 errors, 0 warnings |
| Governance self-check | `PASS`; `python3 tools/practitioner_harness/harness.py self-check` exited `0` with no `BLOCK`; pre-existing REVIEW/WARN observations remain outside the C1 subject |

The three live canon files were applied from the independently validated
candidate without reinterpretation. The diff is 171 insertions and 70
deletions across exactly those three files. No required check failed.
