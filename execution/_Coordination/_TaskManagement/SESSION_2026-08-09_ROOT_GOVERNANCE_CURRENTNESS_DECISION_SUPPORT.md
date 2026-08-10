# Root Task Management — governance-currentness decision support

Date: 2026-08-09

Status: `OWNER-RULED APPLICATION COMPLETE — TERMINAL RECEIPT 103 APPENDED — CHANGE PUBLICATION NEXT`

Invoking loop: Root. Parent: HELP_HUMAN. Mode: mandatory federation
preflight plus the four owner-enumerated currentness items only. This is an
on-demand Task Management invocation, not Root loop entry. No harvest or
deferral review was run.

## Authority and write boundary

The opening owner direction is preserved at
`execution/_Coordination/_TaskManagement/OWNER_DIRECTION_2026-08-09_ROOT_GOVERNANCE_CURRENTNESS.md`.
The application ruling is preserved verbatim at
`execution/_Coordination/_TaskManagement/OWNER_RULING_2026-08-09_ROOT_GOVERNANCE_CURRENTNESS.md`,
SHA-256 `010fb186cca493fd18141cb285b470865234c185e824eb68361bdfaf70eb370a`.
It accepts the exact TM-ROOT-116 draft, selects TM-ROOT-105 Option A, directs
the terminal receipt/handoff, and authorizes later CHANGE publication without
merge. No authority beyond those exact acts is inferred.

## Session basis and mandatory preflight

- Repository root: `/Users/ryan/.codex/worktrees/0b6e/chirality`.
- Initial inspection used detached
  `HEAD@81c376b41a1e181d3edb0737d4f3c9e398527dbe`; its two-commit delta to
  `origin/main` added only `minder/MINDER_INIT.md` and affected no scoped
  source. Before owner-ruled application, HELP_HUMAN established branch
  `codex/root-governance-currentness-20260809` at exact synchronized base
  `d269f0e04204bc463a11684499213b2283bd28f7`; that is the application and
  publication basis.
- Invocation-local federation: `COMPLETE`; four canonical registers validated;
  72 typed findings presented; zero register writes; no invalid, unreadable,
  ambiguous, or excluded-lookalike inputs. Counts at entry: PEC 18 live / 7
  archived; Root 21 / 102; App 16 / 26; Piping 34 / 6.
- Root register validators: live PASS (21 rows), archive PASS (102 rows).
- App and Piping versioned receipt validators: PASS. The repository has no
  Root-scoped receipt validator at this basis, a known surface limitation;
  Root `LOOP_RECEIPTS.md` remained untouched in this pre-ruling tranche.
- Root guards G0–G4: PASS.

## Scoped results

### 1. TM-ROOT-116 — exact draft accepted and applied; row remains OPEN

Decision-ready exact insertion bytes are in
`DRAFT_TM-ROOT-116_IDLE_WORKPLAN_STEP0_2026-08-09.md`, SHA-256
`4d496e0d1e545a67349a23b39076abb34fb837587e80a9b1c880ef1d8c55af4c`.
The owner accepted that exact identity. Its 2,139-byte fenced Step-0 block was
inserted byte-for-byte at the named location in the standing idle workplan;
an exact extraction comparison passes. The resulting workplan SHA-256 is
`f75497926a2ba74ae9038b4e09a06eb951bb8b86d41d6672894c79e6b9f3318d`.
`CURRENT_WORKPLAN.md` remains byte-identical at
`efaea5b88a58e9fe408efffde3ac92ae3c4ec55fdde43b6c61f8add7d3913776`.
TM-ROOT-116 remains OPEN without any row edit; later disposition requires
separate owner action after PR/merge evidence.

### 2. Handoff counts — direct currentness refresh authorized

At entry, deterministic CSV parsing re-derived 21 live rows (12 OPEN, 9
DEFERRED) from `REGISTER.csv` and 102 CLOSED archived rows from
`REGISTER_CLOSED.csv`. The owner-ruled `TM-ROOT-119` maintenance below keeps
the live total at 21 while changing the post-ruling split to 11 OPEN / 10
DEFERRED; the archive remains 102. The Root handoff refresh records both the
Receipt-102 historical transition and this session's post-ruling split.

### 3. TM-ROOT-105 — Option A selected and mechanically applied

The archived row pins `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
Current bytes at its exact EvidenceRef hash to
`9b6d0a17ac73c4494541f1fb323760c03148d8978802b593c4f7d4b09ad0874a`.
The routed Root notice itself hashes to
`501163a9b6c762af1c28e44727c6c7bd21fd1800a8abb020137521020d1f3f88`;
its cited App original reproduces
`3d9061b60f85903fdf3a8dca8dfa28870d20a5db35e093f888f28845162f3ada`.

Git history establishes this sequence:

1. Commit `ba4678ca00c0cf9fb862ba36d1410d11ce1ff6ac` at
   `2026-08-03T21:59:28-06:00` created the transcript and closed/archived
   `TM-ROOT-105` in the same commit. The transcript blob in that commit
   reproduces the pinned `66b96700…bb06` hash.
2. Commit `2b6d53027ea10374dd515a4a5a203f8ed4cf2f04` at
   `2026-08-03T22:22:52-06:00`, 23 minutes 24 seconds later, changed 82 files
   under commit subject `fix: normalize candidate whitespace`. For the cited
   transcript its exact numstat is zero additions / one deletion: the only
   deleted byte sequence is one empty terminal line after
   `<!-- VERBATIM_OWNER_RETURN_END -->`. No owner-ruling text or custodial
   metadata changed. The resulting blob reproduces the current
   `9b6d0a17…874a` hash.

The causal account is therefore a post-closure mechanical whitespace
normalization whose broad commit also touched the closure evidence. The
statement about intent is an evidence-bound inference from the commit subject,
82-file scope, and exact one-empty-line diff; Git proves the byte change but
does not independently prove the committer's subjective intent.

The decision packet presented these owner disposition options:

- **Option A — re-pin to the normalized bytes (recommended):** retain the same
  EvidenceRef, disposition, closure date, and EvidenceQuote; change only
  EvidenceSha to `9b6d0a17…874a` and append a provenance note citing both Git
  commits and both hashes. This is the smallest currentness repair and makes
  no semantic reinterpretation, but it is still a human-gated archived-row
  write and must not be called a silent re-close.
- **Option B — retain the stale historical pin:** make no archived-row change;
  record that `66b96700…bb06` truthfully identifies the bytes used at closure
  and preserve this decision-support record as the standing drift finding.
  Current-path validation will continue to report the mismatch.
- **Option C — restore the original EvidenceRef bytes:** restore the single
  terminal empty line so the current path again hashes to `66b96700…bb06`.
  This exactly recovers the closure-time blob, but it reverses the later
  candidate-whitespace normalization and is therefore not recommended.

The owner selected Option A. Only `EvidenceSha` and `Notes` changed on the
archived row: `EvidenceSha` now equals the current EvidenceRef hash
`9b6d0a17…874a`, and Notes append both full hashes, both full commits, the
one-terminal-empty-line cause, the application-ruling path/SHA, and the
explicit statements that no ruling text or closure meaning changed and this
is not a re-close. `EvidenceRef`, `Disposition`, `Closed`, `EvidenceQuote`,
and every other field reproduce their pre-application values exactly. No
other archived row changed.

### 4. TM-ROOT-119 — owner-ruled row maintenance

The exact owner ruling is bound to the owner-direction artifact. The row is
mapped from OPEN/MEDIUM/no Trigger to DEFERRED/`PRIORITY 1` with
Trigger `Owner declares loop-observation period complete.`, LastReviewed
`2026-08-09`, and the ruling transcribed verbatim in `EvidenceQuote` and
SHA-bound through `EvidenceRef`/`EvidenceSha`. It is not closed or archived
and no convergence candidate is implemented.

Exact before/after mapping:

| Field | Before | After |
|---|---|---|
| `ActionItemID` | `TM-ROOT-119` | unchanged |
| `Priority` | `MEDIUM` | `PRIORITY 1` |
| `PriorityBasis` | `Owner ruling 2026-08-03 harvest slate` | `On re-entry: first substantive ruling of the session in which the trigger fires.` |
| `Status` | `OPEN` | `DEFERRED` |
| `Trigger` | empty | `Owner declares loop-observation period complete.` |
| `Disposition` | empty | empty (non-CLOSED row) |
| `EvidenceRef` | empty | `execution/_Coordination/_TaskManagement/OWNER_DIRECTION_2026-08-09_ROOT_GOVERNANCE_CURRENTNESS.md` |
| `EvidenceSha` | empty | `1eea9ec401793df2f87dd60b509b2b667894bd4b89e74b5f97d68d23db5adc55` |
| `EvidenceQuote` | empty | exact owner ruling beginning `TM-ROOT-119 — owner ruling, 2026-08-09.` and ending `in the interim.` |
| `LastReviewed` | `2026-08-03` | `2026-08-09` |
| `Notes` | prior promotion/overlap provenance | prior provenance preserved; 2026-08-09 deferral/no-partial-implementation record appended |

All other fields are unchanged. In particular, `Opened=2026-08-03`,
`Closed` remains empty, and the row remains in the live register.

## Post-change validation and exact identities

- Root live register: PASS, 21 rows; final SHA-256 is reported in the return
  accompanying this packet.
- Root archive: PASS, 102 rows; final SHA-256
  `d1e699c475c5a34a468028ada622d7b9b69bdb1f7641e4970d478dc00c23a001`.
- Final federation: `COMPLETE`, four canonical registers, 72 typed findings,
  zero register writes, zero invalid/unreadable/ambiguous inputs. Root now
  reports 11 OPEN / 10 DEFERRED / 102 archived; relationship-class counts
  remain 48 foreign-link-to-local, 2 local-link-to-foreign, 1
  remote-closed/local-open, and 21 local-closed/remote-open.
- App and Piping receipt validators: PASS after the Root-local changes; both
  ledgers are unchanged. No Root-scoped receipt validator exists at this
  basis; terminal Root Receipt 103 is therefore checked by derived receipt-ID,
  append-only, format, path, and diff checks rather than misrepresented as
  covered by a project validator. Manual checks confirm Receipt 103 is the
  unique new ID after latest Receipt 102; they also expose two pre-existing
  historical Receipt-80 headings, unchanged and outside this bounded repair.
- Candidate-whitespace validator: PASS. `git diff --check`: PASS.
- Root guards G0–G4: PASS after the scoped changes.
- Updated Root handoff SHA-256:
  `c03f4ce560aa554af18a7e11efa149573c5a3f71646eab8407374c96313fab42`.
- Root receipt ledger with terminal Receipt 103 SHA-256:
  `d68320d24484b138b4ca477767ae71bb54a61de7bb322f97e132aa4a9a7449e5`.
- Owner-direction evidence SHA-256:
  `1eea9ec401793df2f87dd60b509b2b667894bd4b89e74b5f97d68d23db5adc55`.
- TM-ROOT-116 draft SHA-256:
  `4d496e0d1e545a67349a23b39076abb34fb837587e80a9b1c880ef1d8c55af4c`.
- The accepted idle workplan now hashes to
  `f75497926a2ba74ae9038b4e09a06eb951bb8b86d41d6672894c79e6b9f3318d`.

## Accountable-human rulings applied

1. **TM-ROOT-116:** exact draft accepted and applied; row intentionally left
   OPEN for later disposition after publication/merge evidence.
2. **TM-ROOT-105:** Option A applied mechanically; no semantic change and no
   re-close.
3. **Closeout/publication:** Receipt 103 appended and handoff finalized IDLE
   AND RESUMABLE. CHANGE may commit, push, and open a non-draft PR from the
   named branch/base. Merge is expressly prohibited in-session.

## Terminal state of this decision-support tranche

The Task Management session is terminal at Root Receipt 103 and the loop is
`IDLE AND RESUMABLE`. The ruled Step 0 and mechanical evidence-currentness
repair are applied only in the bounded branch worktree. Nothing has been
staged, committed, pushed, opened as a PR, merged, or applied to `main` by
TASK_MANAGEMENT. CHANGE owns the authorized publication handoff.
