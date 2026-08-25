# APP-DEV LOOP STEER — v3 G0 Task-Management triage preparation — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: App-dev loop.
> Authorizing ruling: A10
> (`chirality_app_v3_app_ruling_record_a10_2026-08-24.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together).
> Governing role instruction: `agents/AGENT_TASK_MANAGEMENT.md` (D-GOV-32).
> This steer is the contract for one bounded act. Read it in full before any
> write.

## Basis gate (check before any write; stop and report if any line fails)

1. `origin/main` contains merge commits
   `4251530ec8a5d5b7abfc035cbdde63dab7fa80f3` (PR #665, pointer act) and
   `f60f3e42d53aaaae64858736ff7caae0c492d04a` (PR #666, R9 transcription).
   Work on a fresh branch `codex/app-tm-triage-2026-08-<DD>` from current
   `origin/main`. Record the exact basis commit.
2. All paths below are relative to `projects/chirality-app-dev/` unless
   rooted. Verify these exact identities at the basis:
   - `execution/_Coordination/_TaskManagement/REGISTER.csv` — SHA-256
     `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.
   - `execution/_Coordination/NOTICE_2026-08-03_ROOT_TM-ROOT-122_ELECTRON_AUTHORITY_DRIFT.md`
     — SHA-256
     `f806474b4500b2b081a49d759a0c0793fe65bce860d7efd146147abc38d5951e`.
   - `execution/_Coordination/NOTICE_2026-08-19_ROOT_TM-APP-027_TM-APP-028_COMPATIBILITY_COMPLETION.md`
     — SHA-256
     `17f269567c3a5795799e5be92a9ac75281dc8ff553afa11376a055d3e78924ed`.
   - `execution/_ScopeChange/_LATEST.md` — SHA-256
     `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`
     (the applied SCA-APP-008 pointer).
3. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record A10 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.
4. If any check fails, stop and report.

## Authority context

The final release plan requires a G0 Task-Management triage for
TM-APP-027/028/032, names TM-APP-025 in G0's evidence list, and assigns
TM-APP-030 to G-HELPER. A10-A authorizes preparation only. Per K-TM-1..6,
every disposition is a human act: this tranche drafts candidates and
assembles evidence; it rules nothing and mutates no register.

## N1 — the triage packet

Produce one packet directory
`execution/_Coordination/_TaskManagement/TRIAGE_2026-08-<DD>_G0_V3_RELEASE/`
containing:

1. **Owner triage sheet** — one entry per row for TM-APP-025, TM-APP-027,
   TM-APP-028, TM-APP-030, and TM-APP-032: the live register row restated;
   what changed since it was opened or deferred (citing the 2026-08-19
   compatibility-completion notice and the applied SCA-APP-008 state where
   relevant, by exact path and SHA-256); the plan's G0 requirement for the
   row; and two to four concrete disposition options with evidence each,
   none marked as chosen.
2. **Electron-drift disposition candidate** — a drafted App disposition
   answering the 2026-08-03 TM-ROOT-122 notice: establish the live Electron
   version authority (D-APP-72 text, the executable manifest, lockfiles, and
   any other governed surface that names an Electron version, each cited by
   exact path and identity), state the drift precisely, and draft the
   disposition options (amend D-APP-72; re-pin the manifest; or another
   instrument-conformant resolution), none marked as chosen. Note that
   TM-ROOT-122 closes only on a recorded App disposition and that the drift
   is a named G1 blocker.
3. **Notice-adoption assessment** — for each of the two unadopted notices, a
   recorded adoption-candidate entry (adopt / amend / decline options with
   consequences), respecting that TM-APP-040 (notice-ledger adoption and
   scanner scoping) is itself an OPEN row whose ruling the owner has not
   made: this packet may recommend, not adopt.
4. **Staleness and closure echo** — for the remaining OPEN rows
   (TM-APP-029, 033, 034, 036, 038, 040, 042): whether the SCA-APP-008
   applied state, the Gate-5 audit findings, or any routed notice changes
   their factual basis, with citations; flag rows whose recorded basis is
   now stale.
5. **Register maintenance candidates** — any `LastReviewed` stamps or other
   register writes the register's own contract would permit for a triage
   pass, expressed as an exact CSV row-diff candidate with pre/post
   identities — produced as a candidate file in the packet, not applied.

Ground every claim in bytes on the basis commit. Fabricating or paraphrasing
a hash is a stop condition: cite only identities the tranche itself computed
or verified.

## Post-write validation

- Run candidate whitespace against the recorded basis commit; it must pass.
- Run the loop's receipt validator after the receipt append and the Task
  Management register validator in read-only form (the register bytes must
  still equal the basis identity).
- Confirm with `git status`/diff that exactly the write set below changed and
  nothing else.

## Receipt and return

- Append Receipt 201 (parent `Receipt-200`) to `loop/LOOP_RECEIPTS.md`,
  incorporating this steer and A10 by immutable path and SHA-256 and
  recording the packet's artifact identities.
- Record run evidence under
  `execution/_Coordination/AgentRuns/APP_TM_TRIAGE_2026-08-<DD>/`.
- Commit, push the branch, and open one unlabeled PR against `main`. Do not
  merge. The owner rules on the packet separately; dispositions land in a
  later authorized tranche.

## Write set, exactly

- New files strictly inside
  `execution/_Coordination/_TaskManagement/TRIAGE_2026-08-<DD>_G0_V3_RELEASE/`.
- One append to `loop/LOOP_RECEIPTS.md` (Receipt 201; parent Receipt-200).
- New files strictly inside
  `execution/_Coordination/AgentRuns/APP_TM_TRIAGE_2026-08-<DD>/`.

Not selectable: `execution/_Coordination/_TaskManagement/REGISTER.csv` and
`REGISTER_CLOSED.csv`; every existing notice file; `execution/_ScopeChange/`
in its entirety; the decomposition, contract, and companion register;
`AUTHORITY_CORPUS.json` and every `_REFERENCES.md`, `Dependencies.csv`, or
`_DEPENDENCIES.md`; any carrier SOW, `_CONTEXT.md`, `_STATUS.md`, or
lifecycle file; any `_Evaluation` file; anything under
`projects/chirality-app-dev/frontend/` or any other
`projects/chirality-app-dev/docs/` file; any Root-loop path (read-only
citation excepted); `agents/**`, `tools/**`, `AGENTS.md`, root `docs/**`,
`exports/**`, `plans/**`; any other project.

## Sync rule

If `origin/main` advances mid-run, the Receipt-197 standing authorization
permits one non-rewriting sync; record it, and stop fail-closed if the sync
changes any identity named in the basis gate.

## Rollback and abort

This tranche adds files only. Any validation failure, identity disagreement,
or unexpected write reverts the additions on the branch (or abandons the
branch), verifies that every pre-existing surface remains byte-identical to
the basis, and stops with a report. A stop-and-report is a compliant outcome
of this steer, not a failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set for any reason; if the act appears to require a
write outside the set, stop and report — the owner decides. No authority is
inferred from this steer beyond the preparation it names.
