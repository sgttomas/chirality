# D-APP-86 helper-rerun validation

Overall verdict: `PARTIAL — STOPPED`

| Gate | Result | Evidence |
|---|---|---|
| Focused parity tests | PASS | 6 files, 36 tests; deterministic `focused-tests.log.gz` SHA-256 `84a667c1...930c`; decompressed raw SHA-256 `1aae3ff6...db46` |
| Typecheck | PASS | `npm run typecheck`; deterministic `typecheck.log.gz` SHA-256 `2bee31ac...e61d`; decompressed raw SHA-256 `dc2149de...d1f` |
| Production build | PASS | `npm run build`; deterministic `build.log.gz` SHA-256 `dd6a9737...5f5`; decompressed raw SHA-256 `f964c583...becd` |
| Frozen package bytes | PARTIAL | A 446-file package exists and its manifest revalidates; retained command log ends at the sandboxed DNS failure, so successful-command and network-authorization provenance are `UNKNOWN`. |
| Isolated daemon and deterministic fixture | PASS | daemon status, project registration, completed 2-event/1-item stub replay |
| Packaged Workbench/Pipeline/selection/replay UI | BLOCKED | owner-state launcher write at GUI startup; no UI action performed |
| Reachable packaged premerge | NOT RUN | stopped by sealed escalation rule |
| Release-quality wrapper | NOT RUN | stopped by sealed escalation rule |
| Secret scan | NOT RUN | stopped; retained evidence contains identifiers/paths and deterministic fixture text, but no credential values |
| Final package/source revalidation | PASS | First fresh verifier revalidated 509/509 source and 446/446 package-manifest rows; the closeout-amendment verifier repeats hash/index checks after claim correction. |

The retained deterministic `desktop-pack.log.gz` decompresses to the exact raw
log for the initial sandboxed DNS failure (raw SHA-256 `5675bdbb...6513`).
The resulting frozen package proves that package bytes existed; it does not
prove who authorized a later network attempt, which command produced those
bytes, or whether dependency-boundary and instruction-root checks completed in
that unrecorded attempt. Those provenance claims remain `UNKNOWN`.

Packaged GUI startup omitted the verification opt-out
`CHIRALITY_SKIP_CLI_LAUNCHER=1` exposed by live source and wrote the owner
launcher before UI action. This is an instrument invocation defect. The
launcher was left untouched afterward. The live package contains no distinct
D-APP-88 headless helper identity, so the recorded rerun trigger is not
established and no parity rerun is authorized on this basis.

No skipped gate is represented as passing.
