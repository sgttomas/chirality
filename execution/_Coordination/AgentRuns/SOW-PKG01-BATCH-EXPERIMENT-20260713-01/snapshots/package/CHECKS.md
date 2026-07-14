# PKG-01 Batch Experiment Package Checks

Verdict: `PASS — READY FOR INDEPENDENT EXPERIMENTAL RECONCILIATION`

## Coverage and sufficient-quality contract

Exactly `DEL-01-02`, `DEL-01-03`, and `DEL-01-04` were processed in one
batch-author session followed by one fresh batch-verifier session. The
candidate hashes are:

| Member | Candidate SHA-256 | Mappings | Source lines |
|---|---|---:|---:|
| DEL-01-02 | `44d3ec6f9d608eb0d92da54a07efa521c6dba1dd60ea622526ce6bdcec480330` | 26 | 204 |
| DEL-01-03 | `ff45f0783bdd90116b81d594e53667788f91748eaecc4759e7f65a6ff354d4b4` | 34 | 290 |
| DEL-01-04 | `2b304500ac7833adefe33e422a3f2e74df747adc824af35540c1bb221a3669cb` | 28 | 233 |

Aggregate coverage is 88/88 mappings over 727/727 source lines. Author and
fresh verifier both reproduced byte-identical converter outputs, claim maps,
parity reports, checklists, and renders per member. Candidates validate as
`SOW_V1`; isolated workspaces validate as authorized `MIGRATION_DUAL`; all
partial/unauthorized states fail closed. Scope, objectives, OUT/AC/VER,
immutable literals, lifecycle meaning, and source/control hashes remain
conservative and unchanged.

This is sufficient evidence for faithful representation replacement only. It
does not substantively approve the engineering/governance content.

## Strict manager fan-in

- Author manifest: 265/265 entries rehashed; 21 progress rows, seven stages
  per member.
- Verifier manifest: 317/317 entries rehashed; 103 evidence files per member;
  33 progress rows including an append-only correction.
- Fresh manager reproduction: 3/3 duplicate conversions match candidates;
  all validations, maps, parity, checklists, renders, and 12 negative cases
  reproduced.
- Live four-document checks and dependency-schema checks: 3/3 PASS each.
- Replacement manifest: exactly 15 rows (three adds and twelve deletes).
- Rollback manifest: exact 15-row operation/hash inverse.
- Apply / target validation / rollback simulation: 3/3 PASS without project
  writes.
- Generated manager evidence portability: 15 checkout-root fields in 15 files
  normalized deterministically to `{REPO_ROOT}`; zero machine-root hits remain
  in manager-generated reproduction evidence.
- Practitioner self-check: exit 0; unchanged baseline `INFO=15`,
  `NOT_APPLICABLE=2`, `REVIEW=27`, `WARN=6`; no BLOCK.
- Full practitioner harness: 264 passed in 68.23 seconds.
- DEC-025: not applicable because no project code path changed.

## Retained execution findings

1. Author member 1 initially failed before output because the sealed brief
   conflated path-scoped experiment authority with the exact D-GOV-16 tool
   token. `AMENDMENT-001.md` separated them; the full member was rerun.
2. Verifier member 1 had one contained local shell-quote harness failure after
   five progress stages. Both row sequences and stderr are retained;
   `EVIDENCE_CORRECTION-001.md` classifies the fresh-workspace restart.
3. The first manager reproduction used the wrong parity JSON array key and
   was rerun from fresh inputs. A later portability inspection caused one
   further full reproduction with deterministic path normalization. Both are
   recorded in `MANAGER_ATTEMPTS.md`.
4. The final parent-manifest verifier initially rejected all nested
   `/MANIFEST.tsv` bindings instead of excluding only the parent manifest
   itself. The overbroad assertion failed after the snapshot-manifest PASS;
   the exact-self-path assertion then rehashed all 28 parent rows to PASS.

None weakened a gate, repaired a candidate, changed project state, or caused
semantic drift. They are real setup/reliability costs relevant to whether the
batch model is efficient.

## Scope and closure

No project, candidate-after-author, lifecycle, Git, Stage-2 plan/current run,
H1/H2, `DEL-01-01`, integration, release, retirement, unrelated audit, or
`.claude-worktrees/**` path was modified. The four pre-existing unrelated
audit paths and excluded worktree state remain external.

Blockers / waivers / unknowns: none. The package derivative is current at the
recorded hashes and must now receive the chartered independent experimental
RECONCILIATION verdict before the overall experiment can close.
