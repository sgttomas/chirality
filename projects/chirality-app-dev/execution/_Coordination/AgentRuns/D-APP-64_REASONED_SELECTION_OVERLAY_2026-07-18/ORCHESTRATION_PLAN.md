# Orchestration Plan — D-APP-64 Reasoned-Selection Standing-Approval Overlay

- **RunID:** `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`
- **Orchestrator:** HELP_HUMAN (Agent 0), Claude Fable 5, this session
- **Plan version:** 1
- **Authority basis:** owner standing direction (Ryan Tufts, K-AUTH-1, in-chat,
  2026-07-18) — transcribed verbatim in `LAUNCH_BRIEF_GOVERNED_WRITES.md`
  §Owner direction and, as its governed home, in the D-APP-64 packet
  §Owner Direction. Canonical span SHA-256
  `1bba870869e096ebd975ba503ce4afbc69de3b1b2360508bc6e8b680fb502e39`
  (3,081 UTF-8 bytes between the verbatim markers, excluding marker lines and
  delimiter newlines).
- **Base:** branch `claude/dapp64-reasoned-selection-overlay` off `origin/main`
  = `34774f5795936fa07d5c13b3d52d5f69eb63bf4f`; clean tree at Step 0.
- **Step-0 record:** receipt validator VALID (frozen through Receipt-52,
  versioned contract satisfied; newest receipt Receipt-69); register scanned —
  rows through D-APP-63 all `RULED`, next ID D-APP-64; D-APP-38 corpus status
  no drift; repo-wide practitioner-harness self-check at the recorded baseline;
  filename preflight — no standing surface hardcodes
  `WORKPLAN_2026-07-18_app_dev_loop` (dated history only: one AgentRuns record
  and the receipts ledger).

## Effect fence

No exercise of the refined discretion, and no product, lifecycle, issuance,
release, publication, merge, push, protected-data, domain-engine,
provider/network, or other external effect, before the single atomic landing
commit. Owner merge of the PR remains the terminal integration act; this run
never self-merges.

## Work graph

| Node | Role | Work | Depends on |
|---|---|---|---|
| N1 GOV-WRITES | Agent 1 child, HELPS_HUMANS posture, sealed brief | Author the D-APP-64 packet (incl. Appendix W candidate bytes), append the register row, write the run-dir candidate file and rationale artifact, amend `LOOP_INIT.md` §2 to the committed-HEAD loader | Step 0 |
| N2 V1-CARRY-FORWARD | fresh verifier child, sealed refutation-only brief | Refute: the Appendix W candidate differs from `WORKPLAN_2026-07-18_app_dev_loop.md` only by the enumerated D-APP-64 delta set | N1 |
| N3 LANDING-ARTIFACTS | Agent 0 (control plane) | `CLOSED_INVARIANT_MATRIX.md` (I1–I12), `LANDING_MANIFEST.md`, `PROMOTION_CHOREOGRAPHY.md` | N1 |
| N4 MATERIALIZE | Agent 0 executing the frozen choreography (CHANGE-posture mechanics; no judgment) | Materialize `loop/WORKPLAN_2026-07-18b_app_dev_loop.md` from the candidate bytes; `cmp -s` + `git hash-object` equality; stage declared scope | N2, N3 |
| N5 V2-INVARIANTS | fresh verifier child, sealed refutation-only brief | Check I1–I12 against the staged tranche (commit-dependent cells staged-empty) | N4 |
| N6 RECEIPT | Agent 0 | Append Receipt-70 to `LOOP_RECEIPTS.md`; rerun receipt validator | N5 |
| N7 V3-GOVERNED-DIFF | fresh verifier child, sealed refutation-only brief | Enumeration-derived claims over every governed artifact the staged diff touches (NM-5 rule) plus the whole-diff claim | N6 |
| N8 LAND + CLOSEOUT | Agent 0 (CHANGE-posture mechanics) | Single atomic commit of the declared scope; post-commit HEAD-only discovery proof; closeout battery; push; open PR; stop for owner merge | N7 |

Verdicts are recorded only after the corresponding return file exists
(staged-empty → staged-filled). Nothing lands on `BLOCK`; a `BLOCK` return is
repaired and re-verified with the failed return preserved.

## Write scopes

- Agent 0: this run directory; `loop/LOOP_RECEIPTS.md` (Receipt-70 append);
  choreography execution (materialized workplan file, staging, one commit).
- N1 child: exactly the five targets named in its sealed brief; nothing else.
- Verifier children: their own `RETURN_*.md` file in this run directory only.
- Never touched: Shared-Block v1 bytes, D-APP-59..63 records, prior workplans,
  receipts through Receipt-69, `projects/chirality-piping/**`,
  `_DomainEngines/**`, `projects/pec/**`.

## Node returns

- **N1 GOV-WRITES — RETURNED, complete, no deviations.** Five targets written
  exactly. Candidate: 14,932 file bytes, blob `5f01938c92b719426e9c0716a5d5a3980cf78566`,
  span SHA-256 `a8e1a1d05e1f5c2a44db30cac2cbfb28bf5a9ff5c4dd3984d9ef94a4e0a22573`
  (14,931 bytes), Appendix W span recomputed equal. Direction span recomputed
  from the packet's markers equal to `1bba8708…2e39`; Shared-Block v1
  recomputed from the D-APP-60 packet span equal to `76438ab0…7668`
  (5,108 bytes). Scope confirmed by porcelain status; nothing staged or
  committed; §10 verdict lines staged-empty.
- **N2 V1-CARRY-FORWARD — RETURNED `COMMIT-SAFE`** (`RETURN_CARRY_FORWARD_1.md`).
  Independent diff found exactly the six enumerated regions and nothing else;
  no fence, stop, non-negotiable, or check obligation weakened; Appendix W
  span byte-identical to the candidate minus its trailing LF (independent
  extraction and hashing). Packet §10 V1 verdict filled after the return
  existed.
- **N3 LANDING-ARTIFACTS — DONE.** Invariant matrix (I1–I12), landing
  manifest (frozen candidate: file bytes 14,932; blob `5f01938c…8566`; span
  `a8e1a1d0…2573`; six-item scope), promotion choreography written.
- **N4 MATERIALIZE — DONE.** Choreography steps 1–4 executed: frozen bytes
  recomputed equal to the manifest; active path confirmed absent from
  `HEAD`, index, and worktree; materialized by byte-copy; `cmp` equal and
  `git hash-object` equal (`5f01938c…8566`); bytewise sort places
  `WORKPLAN_2026-07-18b_…` last. Scope staged (Receipt-70 pending by
  design).
- **N5 V2-INVARIANTS — RETURNED `COMMIT-SAFE`** (`RETURN_INVARIANTS_1.md`).
  All rows independently attacked; I4 and post-commit I7 halves correctly
  `PENDING-COMMIT`; staged set equals manifest items 1–4 and 6; pre-commit
  `HEAD` discovery still selects `WORKPLAN_2026-07-18_app_dev_loop.md`;
  Shared-Block v1 recomputation equals the piping D-50 record. Packet §10
  V2 verdict filled after the return existed. V3-cell convention set
  pre-V3: verdict recorded in the PR body only (Receipt-69 recording-only
  precedent) so the verified staged bytes stay stable; V3's return file and
  the N7 completion line below are the only post-V3 additions, both inside
  the manifest's item-6 path scope.
- **N5a CLOSEOUT-BATTERY (pre-receipt) — DONE, one repair.** Validation
  pytest pass; instruction-entrypoint validator pass; practitioner-harness
  pytest initially failed its two live-baseline pins on the three D-APP-64
  records carrying the owner direction's absolute-path citation; resolved by
  conscious pin update (rationale item 8; Landing Manifest amendment v2 adds
  `tools/practitioner_harness/test_live_baseline.py` as item 7). Re-run:
  full practitioner-harness pytest pass; repo-wide self-check exit zero at
  the newly pinned anchor (REVIEW thirty; other severities unchanged).
- **N6 RECEIPT — DONE.** Receipt-70 appended (one heading-format repair
  during authoring: the heading wrapped across two lines and the versioned
  grammar requires one; reworded to a single line before any use of the
  ledger); receipt validator VALID; corpus status no drift; staged
  whitespace check clean.
- **N7 V3-GOVERNED-DIFF — RETURNED `COMMIT-SAFE`**
  (`RETURN_GOVERNED_DIFF_1.md`; verdict recorded here and in the PR only,
  after the return existed, per the pre-declared convention). All six claim
  families independently re-derived: staged paths all inside the amended
  seven-item manifest; register a pure conforming one-row append with
  truthful attribution; both packet hashes recompute; workplan byte-equals
  Appendix W span + LF; Receipt-70 pure append, validator VALID, every
  Checks assertion reproduced; protected artifacts untouched
  (Shared-Block v1 recomputed equal); pre-commit `HEAD` discovery still
  selects the 2026-07-18 plan. Non-blocking observation: §11 "six-item
  scope" predates manifest Amendment v2's lawful seventh item — the
  amendment and rationale item 8 are the governing declarations. This line
  and the V3 return are the only post-check additions, both inside manifest
  item 6.
