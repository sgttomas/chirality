# ROOT LOOP STEER — v3 supply pinning: App Server 0.149.0 exact-pin analysis — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (repository root `execution/`, DEL-02-08 lane). The loop's instruments
> govern; this steer directs one bounded tranche under them. Authorizing
> ruling: R12 (`chirality_app_v3_root_ruling_record_r12_2026-08-24.md`;
> SHA-256 recorded in the PR that published this steer — the files merged
> together). This steer is the contract for one bounded act. Read it in full
> before any write.

## Basis gate (check before any write; stop and report if any line fails)

1. The notice-ingestion tranche (R11) has merged: `origin/main` contains
   `execution/_Coordination/NOTICE_2026-08-24_APP_SCA-APP-008_GATE5_APPLIED_STATE.md`
   at SHA-256
   `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834` and
   the Receipt-128 append. If not, stop: this tranche runs after ingestion so
   receipt numbering stays linear.
2. Work on a fresh branch `codex/root-supply-pinning-2026-08-<DD>` from
   current `origin/main`. Record the exact basis commit.
3. Verify the accepted DEL-02-08 Scope of Work at SHA-256
   `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430` and
   the C1 row in the accepted blocker register at SHA-256
   `9eccd494d7a93680ce644370150683c63e357c3c8bf202ed8291b429c29ce137`.
4. Incorporate by reference (immutable path + SHA-256; do not transcribe):
   this steer and ruling record R12 at their `plans/steers/` paths, with the
   SHA-256 values recorded in the PR that published them.
5. If any check fails, stop and report.

## Authority context

R12-A authorizes the download; R12-B authorizes bounded empirical execution
for supply-evidence generation. Nothing else is authorized: no pin
amendment, no cutover, no implementation, no G2 acceptance (that remains the
owner's act on the returned evidence), no reliance. TM-ROOT-106/122 remain
G1 blockers untouched by this tranche. Fail closed on every disagreement.

## N1 — source identification (before any download)

From current official OpenAI documentation and release channels, identify
the official distribution channel for the App Server 0.149.0 artifact for
macOS arm64. Record as evidence: the channel, the exact artifact URL(s), the
retrieval date, and the documentation pages relied on (URL and retrieved
identity). If the official channel no longer offers exactly 0.149.0, record
the drift precisely (what versions are offered, what changed) and stop —
downloading any other version is forbidden under R12.

## N2 — download, quarantine, and inventory

1. Download the exact artifact into a quarantine directory outside version
   control (`runtime/supply/quarantine/` if the loop's instruments accept a
   repo-local ignored path, otherwise a recorded loop-local path). Verify
   the quarantine path is not tracked before the download.
2. Immediately capture and record: SHA-256 and byte size of every downloaded
   file; the URL each was retrieved from; any checksum or signature the
   channel publishes, verified against the downloaded bytes.
3. Inventory without executing: archive contents, the license text and its
   identity, redistribution terms (G2 treats a redistribution gap as a hard
   stop — record the terms exactly), any vendor code signature and its
   verification result, and the declared platform/architecture.
4. Commit only the supply manifest and evidence records. The artifact bytes
   are never committed, and nothing installs the artifact into any live
   `CODEX_HOME`, PATH, launchd, or daemon surface.

## N3 — bounded empirical execution (R12-B terms, exactly)

Only after N2 completes clean, generate the exact-pin evidence G2 names:

- generated protocol schema/types as the artifact emits them;
- configuration readback and precedence probing against the candidate
  posture in the release plan's Appendix B.1, recording exact 0.149.0
  names, enums, precedence, and readback — including `multi_agent_v2`
  precedence and the `features`/`agents` switches;
- the method/config/feature/experimental-capability matrix, marking every
  experimental capability explicitly;
- current official-doc drift: exact differences between observed behavior
  and the documentation relied on in N1.

Containment for every run: a disposable throwaway `CODEX_HOME` and working
directory created for this tranche; no credentials, tokens, keychain access,
or accounts; no login or device-code flow; command network off and every
network approval denied; no write outside the disposable workspace; full
teardown of the disposable state at closeout, recorded. Any prompt for
credentials, any attempted network egress beyond the artifact's local
operation, or any write outside the disposable workspace stops the tranche.

Record what could not be produced under these bounds rather than loosening a
bound to produce it.

## N4 — supply-unit candidate and return

Assemble the DEL-02-08 supply-unit candidate: the exact supply manifest
(artifact identities, source, license, signature, redistribution terms), the
generated schema/types, the capability/config matrix, the doc-drift record,
and a candidate `G2` acceptance sheet stating exactly what the owner would
be accepting. Mark everything `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`. No
acceptance, cutover, pin-amendment, or reliance claim.

## Post-write validation

- Run candidate whitespace against the recorded basis commit; it must pass.
- Run CI-form G4 (no instruction surface is expected to change — if G4
  demands a covering manifest, stop and report).
- Confirm the quarantine path is untracked and that `git status`/diff shows
  exactly the write set below.

## Receipt and return

- Append Receipt 129 to `execution/_Coordination/LOOP_RECEIPTS.md` following
  the ledger's receipt contract, incorporating this steer and R12 by
  immutable path and SHA-256 and recording the artifact identities, the
  containment attestations, and the candidate state.
- Record run evidence under
  `execution/_Coordination/AgentRuns/ROOT_SUPPLY_PINNING_2026-08-<DD>/`.
- Commit, push the branch, and open one unlabeled PR against `main`. Do not
  merge. The owner rules on G2 acceptance separately, on the returned
  evidence.

## Write set, exactly

- New files strictly inside
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/`
  and any new evidence subfolder of that deliverable the loop's instruments
  direct for supply-unit candidates (additions only; no existing deliverable
  file is modified).
- One append to `execution/_Coordination/LOOP_RECEIPTS.md` (Receipt 129).
- New files strictly inside
  `execution/_Coordination/AgentRuns/ROOT_SUPPLY_PINNING_2026-08-<DD>/`.
- The untracked quarantine directory (never committed).

Not selectable: any pin, version, or manifest surface (no pin amendment);
`docs/CONTRACT.md` and every other root `docs/**` file; the DEL-02-08
`ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, or `Dependencies.csv`; every `execution/_ScopeChange/`
snapshot file; any other deliverable; `agents/**`, `tools/**`, `AGENTS.md`,
`exports/**`, `plans/**`, `skills/**`; any live `runtime/**` configuration
or daemon surface; anything under `projects/**` or `_DomainEngines/**`; any
live `CODEX_HOME`, launchd, keychain, or credential surface.

## Sync rule

If `origin/main` advances mid-run, the standing routine-sync authorization
recorded in Receipt 125 permits one non-rewriting sync; record it, and stop
fail-closed if the sync changes any identity named in the basis gate.

## Rollback and abort

Any identity, version, license, signature, containment, or validator
disagreement: delete the quarantine contents, tear down all disposable
state, revert branch additions (or abandon the branch), verify every
pre-existing surface remains byte-identical to the basis, and stop with a
report. A stop-and-report — including "the official channel no longer offers
0.149.0" — is a compliant outcome of this steer, not a failure.

## Discipline

Fail closed on every disagreement. Produce durable evidence for every claim.
Do not expand the write set or loosen a containment bound for any reason; if
the act appears to require either, stop and report — the owner decides. No
authority is inferred from this steer beyond the download, bounded
execution, and candidate assembly it names.
