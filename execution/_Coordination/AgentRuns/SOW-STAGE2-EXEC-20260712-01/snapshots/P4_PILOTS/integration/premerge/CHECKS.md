# P4 Pilot Integration Premerge Checks

Verdict: `PASS — READY FOR REMOTE VALIDATION`

Basis is `main@0d260eb024d8b8dada0df477b70ac880a6906ffa` and accepted
preintegration R1 snapshot SHA-256
`8e5d453f98e7be40256c200f15e80eb05df02f0167b037b90d1f59332ff10224`.

| Gate | Result |
|---|---|
| Accepted artifact hashes | PASS — 15/15 |
| Replacement and inverse manifests | PASS — 50/50 unique; exact inverse |
| Evidence binding commit | PASS — `7bfb128d4ad0bf02dd12364713fa328ec7c4dfa2`; 386 root-run paths; zero project paths |
| Serial architecture | PASS — ten commits in accepted order; no merge commit |
| Per-commit path containment | PASS — each commit exactly five paths for one member |
| Per-commit diff hygiene | PASS — zero output for all ten commits |
| Candidate byte identity | PASS — 10/10 |
| Legacy absence | PASS — 40/40 absent |
| SOW post-state | PASS — 10/10 `SOW_V1`; zero dual/partial/invalid |
| Status identity | PASS — 10/10 byte-identical |
| Lifecycle | PASS — 10/10 `IN_PROGRESS` |
| Exact project range | PASS — 50 paths equal replacement manifest; no other project path |
| App focused consumers | PASS — 2 files; 20 tests |
| App full tests | PASS — 97 files; 713 passed; 4 skipped |
| App typecheck and build | PASS |
| SOW tool tests | PASS — 18 passed |
| Piping dependency registers | PASS — 14, 18, 14, and 20 rows |
| Practitioner self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| JSON and manifest structure | PASS |
| Accepted-package path portability | PASS — checkout/temp prefix 0/0 |
| Findings, blockers, material unknowns, waivers | none |

The legacy-only `check_four_documents.sh` is intentionally not applicable to
these accepted SOW-only post-states: its contract requires the four legacy
files whose exact deletion is the approved replacement. The current
fail-closed SOW resolver is the applicable production-format check and passes
for all ten members. Dependency-register checks remain applicable and pass.

## Exhaustive diff-hygiene classification

Per `P-G-DIFF-HYGIENE-001`, the full PR-range raw `git diff --check` output is
exhaustively allowlisted to these six already byte-bound intentional Markdown
two-space hard breaks:

- `instances/CHANGE-P-G/LAUNCH_BRIEF.md`: lines 3, 4, and 5;
- `instances/RECON-PF-R1/LAUNCH_BRIEF.md`: line 3;
- `snapshots/P4_PILOTS/preintegration-r1/ACCEPTANCE.md`: lines 3 and 4.

Each named source line ends in exactly two ASCII spaces followed by newline.
There is no other PR-range diff-hygiene finding. Mutable CHANGE readiness and
integration evidence is normalized. Accepted preintegration bytes and the
evidence-binding commit are unchanged.
