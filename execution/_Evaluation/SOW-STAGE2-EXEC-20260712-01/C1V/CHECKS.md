# C1V Checks

Date: 2026-07-13
Runtime: Python `3.13.7`; Git CLI from the accepted workspace

| Check | Command or method | Result |
|---|---|---|
| Basis and Git identity | `git rev-parse HEAD main origin/main` | `PASS`; all three resolved to `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983` |
| Live subject unchanged | SHA-256 plus `git diff --exit-code` / cached diff against the basis for live canon, higher root canon, and projects | `PASS`; both diffs exit `0`; live hashes remain standard `8409bf3c...0013`, TYPES `6b17e67e...1d45`, SPEC `4cb7e341...d6a8b`, DIRECTIVE `a67b8521...71c2`, CONTRACT `d89a6b96...1ab` |
| Ruled identities | SHA-256 of the four live proposal artifacts and the same paths from proposal snapshot `31e5efd...e4f` | `PASS`; standard `7f742901...85a6f`, TYPES patch `9614166c...d4b4`, SPEC patch `543200af...4b2e`, evidence index `8a6e48ac...d806` in both locations |
| Exact standard | `cmp` ruled standard to candidate | `PASS`, exit `0`; candidate SHA-256 `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| Live patch preflight | `git apply --unidiff-zero --check` for TYPES and SPEC | `PASS`, exit `0` for both |
| Independent patch reproduction | Copy frozen live TYPES/SPEC under `C1V/reproduction/docs/`, apply each ruled patch with `git apply --unidiff-zero`, then `cmp` to candidate | `PASS`; apply and compare exits `0`; reproduced/candidate hashes TYPES `5094610af55d18982658ea589be95a60fac9c89ca611846fc57279b494c6d2ae`, SPEC `915c3b59d35afff5e489c9c387f09c17a6e4c307fd5e91cd81a8960d97a91e27` |
| Candidate reverse patches | `git apply --unidiff-zero --reverse --check --directory=<candidate>` | `PASS`, exit `0` for both |
| Candidate containment | Exact expected-path set, realpath containment, and symlink scan | `PASS`; six expected files only, zero symlinks, all realpaths within candidate root |
| C1 return containment and evidence shape | Exact HELPS-C1 instance-path set; JSON parse/type/reference checks; TSV header/row/column/unique-path/hash checks | `PASS`; three expected instance files; declared JSON shape valid; manifest has exact eight-column header, three rows, and all recorded hashes reproduce |
| Vocabulary coherence | Direct deterministic extraction from the three candidate sections and `tools/scope_of_work/id_catalog.json` | `PASS`; all three carry exactly the five format states; standard and TYPES carry the exact nine local ID prefixes; dispositions align with the catalog |
| Path anchors | `python3 tools/validation/validate_path_anchors.py . --text` | `PASS`, exit `0`; no literal home-dir paths in 447 live surfaces |
| Instruction entrypoints | `python3 tools/validation/validate_instruction_entrypoints.py .` | `PASS`, exit `0` |
| Agent instructions | `python3 tools/validation/validate_agent_instructions.py` | `PASS`, exit `0`; 33 files, 0 errors, 0 warnings |
| Governance self-check | `python3 tools/practitioner_harness/harness.py self-check` | `PASS`, exit `0`; no BLOCK finding. Existing REVIEW/WARN observations are outside the C1 subject and are present on the frozen basis. |

All required commands completed. No required check failed and no check mutated the subject or Git state.

