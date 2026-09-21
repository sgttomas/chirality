# V-DEL-09-07 — verifier shard notes (R0 calibration, unit V)

Shard: `DEL-09-07` ledger (30 selected rows) plus `SURFACES` HARNESS capability rows
(10 selected, plus the extra `d+` row CAP-HARNESS-058). Evidence was read at the frozen
tree `00115c719`. Git use: read-only `git show --stat` on `da95ec194`, `cb08dbe2f`,
`9ecbdecdf` and `ccb95e06a`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 28 | 23 | 1 | 4 |
| b | 2 | 2 | 0 | 0 |
| d | 10 | 8 | 0 | 2 |
| d+ (extra) | 1 | 0 | 1 | 0 |
| **Total** | **41** | **33** | **2** | **6** |

- **REFUTED:**
  - DEL-09-07#STATE-2 → ACCEPTED_DIVERGENCE;
  - CAP-HARNESS-058, whose capability text is wrong.
- **CONTESTED:**
  - DEL-09-07#SEC-2.1, #SEC-2.5, #SEC-2.13 and #REGISTER-1;
  - CAP-HARNESS-011 and CAP-HARNESS-021 (granularity).

## Part 1 — DEL-09-07 ledger

### MR-8 check on the 24 ACCEPTED_DIVERGENCE rows

MR-8 has two limbs: the text must acknowledge the gate, and a GOVERNING ruling must
permit the difference.

**GOVERNING ruling limb: satisfied on all 24 rows.**

- D-APP-127 is a `RULED` register row (`_REGISTER.md:152`).
- The ruling names DEL-09-07 retired (`D-APP-127…md:44`).
- It supersedes D-APP-107 in whole and keeps "the DEL-09-07 folder, its ScopeOfWork … immutable history" (`:159-173`).

**Text-acknowledgement limb: satisfied by the SoW itself.** The worker's premise was that
only `_STATUS.md` acknowledges the gate. That premise is wrong: the preserved SoW text
acknowledges the gate in its own words.

- `ScopeOfWork.md:19-20` says the SoW "does not assert that the target has been implemented or accepted".
- `ScopeOfWork.md:66-69` says "implementation and completion remain gated".
- `ScopeOfWork.md:86-87` says the methods "authorize no execution now".

**Result.**

- **21 of the 24 rows hold as ACCEPTED_DIVERGENCE on a literal reading of MR-8.** The sibling `_STATUS.md:9` records the retirement, which strengthens this.
- **3 rows are CONTESTED.** The reason is not MR-8 but the choice between readings:
  - SEC-2.1 is a CONTEXT_CLAIM that accurately reports its sources;
  - SEC-2.5 could be ALIGNED on a vacuous-satisfaction reading;
  - SEC-2.13 mixes a gate that is moot with gates that are still live.

**Caveat.** This satisfies MR-8 only because a gate acknowledgement in general wording
("implementation gated") is accepted as acknowledging *this* gate (retirement). A strict
reader could hold that the text must acknowledge the specific difference. The rulebook
does not say which reading applies. That ambiguity is the real friction here.

### Assessment of the proposed `RETIRED_BY_RULING` (calibration candidate only)

- **It adds real signal.** It separates "the subject was withdrawn in whole by a ruling" from "the implementation legitimately differs from live text". ACCEPTED_DIVERGENCE blurs the two.
- **It fixes a real inconsistency in this ledger.** The same preserved-history folder produced ACCEPTED_DIVERGENCE for the SoW rows and STALE_SPECIFICATION with R4 for `_CONTEXT.md` (STATE-2). A rule scoped to "text inside the ruling's preserved-history set" would have made those consistent.
- **It would allow collapsing roughly 27 rows to about 4 whole-section rows.** That loses no information when one ruling governs every item.

**Suggested definition, if adopted.** A GOVERNING ruling must:

- name the deliverable, or the scope item, as retired; and
- preserve its text as history.

Under that definition:

- MR-8's text-acknowledgement limb is waived for text inside the preserved set;
- CauseTag still records the cause;
- the disposition does not apply to text outside the preserved set, which stays under MR-11 and STALE_SPECIFICATION, as the decomposition does in REGISTER-2.

**Open question for the owner: machine registers inside the preserved folder.** Examples
are `Dependencies.csv` rows that are still ACTIVE and PENDING. They can feed dependency
tooling, so "immutable history" and "register hygiene" pull in opposite directions (see
REGISTER-1).

**Alternative.** Keep ACCEPTED_DIVERGENCE, and add one sentence to MR-8: "a ruling that
preserves text as history, plus a sibling `_STATUS.md` acknowledgement, satisfies the
text limb".

### Other findings

- **STATE-2 is REFUTED.**
  - The worker's own LEAST-CONFIDENT alternative is correct. D-APP-127 preserves "the DEL-09-07 folder", which contains `_CONTEXT.md`.
  - `_CONTEXT.md:24-27` acknowledges the same gate as the SoW ("No … implementation, or release act is authorized").
  - The Notes misread the ruling as covering only the SoW.
- **SEC-2.13 contains a factual error.**
  - Its rationale, "5 retires as gates", misreads IMPACT.md family 5. At `IMPACT.md:168`, family 5 is process hygiene, not release gates.
  - D-APP-97 is still RULED (`_REGISTER.md:112`), and IMPACT keeps G6a (`:121`).
  - So the paragraph's release-gate half is plausibly still ALIGNED.
- **SEC-4.4 is CONFIRMED.** It is the strongest ACCEPTED_DIVERGENCE row, because D-APP-127 names D-APP-107 explicitly. Its LOW confidence understates it.
- **The evidence paths and lines all exist.** Checked:
  - `runtime-control-ipc.ts:9-14` and `runtime-service-host.ts:1-9`;
  - the test cases at `runtime-control-ipc.test.ts:51` and `runtime-service-host.test.ts:175` and `:262`;
  - `cli.test.ts:339`, which is the assertion line inside the case at `:331`;
  - `api-key-ipc.ts:131`;
  - `runtime-connectivity.test.ts:182`;
  - `PRD.md:1777`, `SPEC.md:1248` and CONTRACT K-RUNTIME-1 (`:224`);
  - decomposition `:384`, `:483` and `:597`;
  - `APP_HOLD_REGISTER.csv`, which has 0 DEL-09-07 rows;
  - `APP_EXECUTION_RETURN.md:42`, which says `RETIRED` while the frozen `_STATUS.md` says OPEN. The carrier discrepancy is real.
- **PostReleaseBasis = NO is correct on every row.** None of the four commits touches the relied-on files.

### (ii) Systematic patterns — ledger

1. **The MR-8 text limb is ambiguous for retired deliverables.**
   - The worker applied the limb inconsistently across files in one preserved folder: SoW rows got ACCEPTED_DIVERGENCE, while STATE-2 (`_CONTEXT.md`) and REGISTER-1 (`Dependencies.csv`) got STALE_SPECIFICATION.
   - The worker also mis-stated which text acknowledges the gate.
   - Keys: STATE-2, REGISTER-1, SEC-1.1.
2. **There is no rule for vacuous satisfaction.**
   - An exclusion or value that holds only because nothing was built is ALIGNED in SEC-1.5 but ACCEPTED_DIVERGENCE in SEC-2.5 and SEC-4.2.
   - Keys: SEC-1.5, SEC-2.5, SEC-4.2.
3. **AuthorityTier "highest tier restated" is stretched.**
   - GOVERNANCE_INVARIANT is used for Root-SoW ownership partitions (SEC-2.5) and for App decision gates (SEC-2.13), which are neither DIRECTIVE, CONTRACT, SPEC nor TYPES.
   - PRD is used for a decomposition register defect (REGISTER-2).
   - The tier vocabulary has no slot for decomposition or App-decision authority.
4. **Minor field-convention issues.**
   - **RecordedRemaining** is truncated to the first sentence of each TBD, not kept verbatim (MR-6). Keys: SEC-2.10 to SEC-2.12.
   - **DirectionEvidence** appends "GOVERNING basis D-APP-127" to the CONTEXT HANDOFF citation, which mixes classes in a field meant to be CONTEXT-only. This affects all ACCEPTED_DIVERGENCE rows.
   - **AssessmentEvidence** carries the token plus a parenthetical. Tolerable, but it is not "exactly one token".
   - **MechanicallyUnblocked = NO** on moot gates is correct but uninformative.
5. **CauseTag DOC_HYGIENE on REGISTER-2 is arguable.** The divergence is caused by A2_TOPOLOGY. Untranscribed scope is not a metadata defect.

## Part 2 — SURFACES (HARNESS capabilities), class d

### Accuracy

For every selected row, the checks passed:

- Paths exist, and every exported EntryPoint symbol exists.
- Consumer paths exist and import the module.
- CoveringTests files exist, and most import the module directly.
- `PostReleaseBasis = NO` is verified: none of the four commits touches `frontend/src/lib/harness/**`.

Minor accuracy nits, none of them blocking:

- **016.** `hydrateHostedBootstrapProject` is named in the Capability but missing from EntryPoints. The route test is indirect coverage. D-APP-127 retires hosted admission and identity binding in direction, which the Notes could flag.
- **021.** The EntryPoint `workflow-draft-review.tsx` imports only the type; the real consumer is `chat-panel.tsx:1673`. `NONE_FOUND` for tests is correct.
- **024.** CoveringTests is incomplete: `daemon-proxy-boundary.test.ts` and `v3-runtime-proxy.integration.test.ts` also exercise the stream.
- **028.** The `LEGACY-IN-PROCESS` tag is verified: the only importers are `lib/harness/mcp/coordination-tools.ts` and tests. However, the Notes say the runtime "composes the test fake daemon harness port"; the reverse is true (`fake-daemon-harness-port.ts:10` imports `getHarnessRuntime`).

**Extra row CAP-HARNESS-058 (`d+`) is REFUTED.** The DEL-08-04 worker's report is correct.

- `subagent-bridge.ts:5-9` sets the policy version to `subagent-bridge.v4.disabled-after-managed-delegation`, with a denial reason pointing to `delegate_agent`.
- `createExecutableSubagentBridge` returns `undefined` (`:84-90`).
- `evaluateSubagentPreflight` always returns `allowed: false` with `executionPosture: 'hard-denied'` and `executableBridge: false` (`:92-116`).
- Only `createExecutableAgentDefinition` survives, as a builder.
- The Capability text "executable subagent bridge (D-APP-10 Option C)" was evidently taken from symbol names and the ruling reference, not from behavior.
- The `LEGACY-IN-PROCESS` tag is correct. The only non-test mention outside `lib/harness` is `scripts/harness-section9-manifest.json`, which is data, not an importer.

### Capability granularity against CONVENTIONS_CANDIDATE §5

- **Most rows meet the per-behavior target.**
  - 004, 015, 016, 017, 024 and 026 each describe one observable behavior or contract surface.
  - 008 correctly folds duplicate client surfaces into one row.
  - 028 is one composition behavior.
- **011 and 021 are CONTESTED.**
  - Each is a single function in an 8- or 11-line file, so each is effectively a per-file or per-function row.
  - They read as helpers that could fold into 010 (native plan client) and 020 (workflow draft review). The worker's notes say small helpers were folded, but these two were not.
  - Either reading is defensible, because each is a distinct display or prompt behavior.
- **Area-level observation.** The 60-row ceiling was hit because the area mixes a thin live layer (001–027) with a legacy in-process engine (028–060). The worker's proposal has merit and should go to the manager:
  - a `Reachability` column with values `PRODUCTION`, `SCRIPT_ONLY`, `TEST_ONLY` and `TYPE_ONLY`; or
  - a `HARNESS_LEGACY` sub-area.
- **The reachability tag does not protect against misdescribing behavior.** The 058 error shows this: a legacy row can still describe disabled code as live. A `Behavior` check (disabled or retired) would need its own field or note convention.

### (ii) Systematic patterns — capabilities

1. **Capability text inferred from names rather than behavior.** Key: 058.
2. **Loosely defined EntryPoints.** Symbols are mixed with consumer paths, and some consumers are type-only. Key: 021.
3. **Per-function rows despite the stated folding rule.** Keys: 011, 021.

## (iii) Effort

- **Files read.** About 35, as greps or line ranges:
  - 8 run files (brief, conventions, basis, ledger, notes, reverse, capabilities, notes);
  - 8 deliverable and decision files (SoW, `_STATUS`, `_CONTEXT`, Dependencies, D-APP-127, register, IMPACT, HANDOFF and carrier return);
  - about 20 code and test files.
- **Tooling.** One scripted existence and export check covered the capability rows. `git show --stat` was run on the 4 commits.
- **Context budget.** Moderate, not tight. The ledger's heavy repetition (the same evidence on 24 rows) made the ledger cheap to verify.
