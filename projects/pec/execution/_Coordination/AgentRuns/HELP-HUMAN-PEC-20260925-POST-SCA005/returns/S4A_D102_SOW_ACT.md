# Return — S4A: D-PEC-102 act (S4 Scope of Work currency, eight exact replacements)

WORKING_ITEMS (Type 1) under HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`,
work-graph node S4 (the act), 2026-09-26. Brief `briefs/S4A_D102_SOW_ACT.md`
(`98f744886651e3d4ce9e54ef22dbbbbfaca486de421b45b9e80e46ceada6932e`, copied unchanged).
`Workflow: chirality-root:bundled:workflow:scope-of-work` (`WORKFLOW.md` `84dadde4…2b`,
`resources/checks.md` `44ab41ac…f188`). Host-reported model `claude-opus-5-5`; the
high effort and the roles are instruction-asserted.

## PR

- PR #998, https://github.com/sgttomas/chirality/pull/998, against `main`, **not merged**.
- Head: the commit that adds this return, on top of `a763940a5` (run-root records). The
  exact head SHA is in the manager's handback to HELP_HUMAN and on the PR.
- Base `origin/main` `4c2a7768f` (PR #994, carrying the ruling). `origin/main` then
  moved to `78e74f590` (PR #995, with no `projects/pec` path), which was merged
  without a rebase (`c8b3a8f9c`).

## Act report

- **Preconditions met.**
  - Fetched `origin/main` held the ruling and the register row `D-PEC-102`
    `RULED A / PART B AND 3a, 3b CONFIRMED / M / EFFECTIVE ON MERGE`.
  - Prep `SHA256SUMS` checked 107/107 OK. The 36 files copied into the run root
    matched 36/36.
  - `apply_s4p.py --check-only` exited 0, with all 8 preimages and all 19 pins as
    tabled.
  - `pec_reliance_hold.py` (header-only register `f877d931…c741cbc`) returned `ALLOW`
    ×8 at three points:
    - `dispatch-for-production` at 04:51:45Z, before the act and the verifier
      dispatch;
    - `rely-for-production` at 04:54:03Z, before the act commit;
    - `rely-for-production` at 05:22:53Z, before the verdict fan-in.
- **Write-set decision.** `apply_s4p.py` leaves its own directory out of its
  write-set inventory, so the run-root copy was run and its output written beside it
  in the run root. The verifier found this consistent with the script and the
  proposal.
- **The act.** One real run from the repository root at 04:53:46Z exited 0 with
  `CHECK targets 8/8 byte-exact; write set = grant (0 created, 8 modified, 0 removed under projects/pec outside the run root); pinned 19/19 unchanged`.
  Act commit `5d13cfdb8`.
- **Add-on M** was not run. It belongs to closeout node M1, and no `MEMORY.md` was
  created.

## Written paths (SHA-256)

Products, under `projects/pec/execution/`:

| Path | SHA-256 (= tabled postimage) |
|---|---|
| `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0` |
| `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` | `bcd69f503acf308e2ef7e73cc722efd61b59710877a5561624260aad71736b11` |
| `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` | `b8c021f581448d1ff5413938563d40b015672aefede15ed97da9dd9b92865e01` |
| `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` | `d4bb8ffa475a7165a00f4d383a210f3d232dd16af3a971b87d9c1bad77cf81bf` |
| `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` | `16d731a51556cb644220c2c532696d8d0144972e20576db29495e200a775404c` |
| `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` | `10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md` | `5f7bd434694c8a87bba512ba74a8b8f2dee4f5e2a0ab10e5a50c234e432b196f` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` | `e0df75bdcbdeaa2ecd0c320a3c36082c7c47551f2f514392856c761a96b99865` |

Run root `_Coordination/SOW_CURRENCY_S4_2026-09-26/` (265 files, each listed in its
`SHA256SUMS`):

| File | SHA-256 |
|---|---|
| `SHA256SUMS` | `91b6a1acdd737f1b36c0e209dcbb5f320a9ff74d28d9ab4ec7a76f878dc2b502` |
| `MANIFEST.md` | `56eff9dfc64cb70e1976a19695ea858a8968eabbe018f200ee0a0905aca7d95b` |
| `VALIDATION.md` | `cbbd2232f1674e8191aabb6f0dc3d26d70b76e04edda14e9f2d5dce857a4751a` |
| `HANDOFF_STATE.md` | `21749f44244960ac6748e45fee8c463cc667a4f6bc0d040b7d825023fb5edda6` |
| `VERIFIER_VERDICT_01.md` | `9e3bd56010ef486a7ddc4b69c1bfa1c2b5d25c0017ee36dcc5b5f06af57a318f` |
| `apply_s4p.py` | `2b6792fee7b69266ad28f517734f89f9c01b60c6e6d4489118fd14375f364869` |

AgentRuns:
- `briefs/S4A_D102_SOW_ACT.md` `98f744886651e3d4ce9e54ef22dbbbbfaca486de421b45b9e80e46ceada6932e`;
- `returns/S4A_D102_SOW_ACT.md` (this file).

## Check results (proposal "Finite verification")

| Row | Result |
|---|---|
| 1 Preconditions | as above; pins as tabled; `ALLOW` everywhere |
| 2 Validator | `PASS format=SOW_V1` ×8 |
| 3 Checklists | exit 0; reruns byte-identical; each equals the prepared hash ×8 |
| 4 Boundary owners | exit 0 ×8. No `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`. `NOT_CHECKABLE` sets exactly as tabled, and the JSON is identical to preparation. The verifier did the hand resolution (F1 below) |
| 5 Quotes | `RESULT PASS 740/740` |
| 6 State claims | `RESULT PASS 1144/1144` |
| 7 Cited IDs; S2 scan | `RESULT PASS 57/57`; `SUMMARY stale=0 kept=2` |
| 8 Lifecycle | no `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` or `MEMORY.md` change |
| 9 Registers; dependency-quote currency | Strict: exit 1, 0 errors, 26 `XRG-013` (D-GOV-48 deferred). Dependency-quote currency: 127/127. Both identical before and after |
| 10 Harness; receipts | exit 0 each, identical before and after |
| 11 Containment | see below |
| 12 `git diff --check` | clean (no `.gitattributes` exemption) |
| Pins after the act; second run | 19/19 pins and 8/8 postimages. The second run refuses (exit 1) |
| Rerun method | `run_s4p_checks.sh` on the `4c2a7768f` exports and on the `78e74f590` exports: `OVERALL PASS` both, including fault injection 9/9. Negative controls: 6/6 tripped |
| After the `78e74f590` merge | `--check-only` passes on a `78e74f590` export and refuses on HEAD (by design). Quotes 740/740, claims 1144/1144, IDs 57/57, pins 19/19. Strict, harness, receipts and quote currency are identical to the pre-act baselines |

The informational consequence scan on the pre-act exports gives `stale=13 kept=26`
(preparation: `kept=25`). The added KEPT line is the D-PEC-103 act's DEL-08-06
quoting DEL-04-01 text that the postimage still carries.

## Verifier verdicts

`VERIFIER_VERDICT_01.md`, from a fresh read-only `pec-reviewer` (`opus`, host-reported
`claude-opus-5-5`, agent `aba354cc9ba64fbab`, foreground) on candidate `a26ca1613`:
**PASS WITH NOTES**, nothing blocking. The file is the handback text verbatim plus a
final newline; the text's SHA-256 is `64b1635d…fca32`.

Every check passed:
- basis;
- byte identity (8/8 against base, candidate, run-root copy and prep copy);
- the `MODE=VERIFY` subset of `checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21);
- claims and quotations, with independent spot-checks;
- scope within ledger, `Deliverables.csv` and PRD v2.4;
- open items as `TBD`/`CON` with none resolved;
- kept IDs, with none retired or reused and counts equal to the proposal;
- no verify-before-rely rebuild;
- the **Part B landings**: verbatim against the exhibit, with the DEL-04-01 gates
  stated as still binding;
- **reading 3a**: seven components, "no eighth";
- **reading 3b**: the envelope is declared beside the stamp, and `REQ-001` is
  byte-identical;
- **seven-component consistency** across all eight postimages;
- no Remaining surface;
- containment and lifecycle.

Dispositions (in `VALIDATION.md`):
- **F1** (non-blocking): the proposal's QA 21 row for DEL-10-03 `REQ-013` omits the
  "not cited" annotation. The owner is resolved in substance. Recorded, and carried as
  a DEL-10-03 currency note.
- **N1**: acted on through the no-rebase merge and the rechecks.
- **N2 to N6**: recorded.

## Containment

`git diff --name-status origin/main...HEAD` at the records commit (merge base
`78e74f590`) lists:
- the eight `M` contracts;
- the brief copy `A`;
- 266 `A` under the run root.

The return adds one more `A`. Nothing else under `projects/pec` or elsewhere is
changed: no register, `Dependencies.csv`, `_DEPENDENCIES.md`, `_CONTEXT.md`,
`_REFERENCES.md`, decomposition, `v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**`
or work-graph write. `git diff --check` is clean. Scratch stayed in the session
scratchpad, with one exception: a `/tmp/_s4a_unused_<pid>` file created and removed
within one command (disclosed in `MANIFEST.md`). The verifier deleted only its own
`mktemp -d` directory.

## Unresolved, for the caller

1. **Review and merge PR #998.** Independent review of the complete candidate is still
   needed. Verdict 01 covered `a26ca1613`; later commits add the verdict, the merge,
   the rechecks, the records and this return. HELP_HUMAN also adds the graph and
   STATUS records to the PR.
2. **If `origin/main` moves again:** merge without a rebase, then rerun `--check-only`
   on a new-base export, `run_s4p_checks.sh`, and the quote and state-claim verifiers.
3. **DEL-04-01 acceptance lapse.** The owner's 2026-08-09 exact-byte acceptance of
   DEL-04-01's prior contract lapses when this lands. `_REVIEW.md` stays untouched and
   still describes the prior bytes. No review is opened.
4. **Add-on M at node M1.** Create eight `MEMORY.md` files from the template, with the
   proposal's row; `{PR}` = #998.
5. **Consequences outside the packet, as disclosed.** DEL-04-05 (S1), DEL-10-11 and
   DEL-03-04 have later currency items. There are also DEL-10-03 `REQ-013` (F1) and
   the dated "not yet ruled" wording (N4).
6. **Carried unchanged.** All `CON`/`TBD` items stay open, and the DEL-04-01 Part B
   production gates still bind.

No lifecycle change, `CON` resolution, dependency edge, tool declaration or
invocation, CHECKING, ISSUED, REVIEW gate, acceptance, readiness, release or reliance
claim is made. Nothing here prompts about CHECKING.
