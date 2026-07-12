# DEL-08-04 concordance notes (R2 Wave-3, RUN_D55_CONCORDANCE_2026-07-11_1904Z)

Deliverable: DEL-08-04 Type 2 Subagent Governance Bridge (PKG-08). Source state:
frontend/ at fac46e33f (byte-identical through HEAD 74150b3a8). INSP-03 reviewed
`d92ef1253b`; behavior re-verified against the live tree.

## Census

By ClaimType: REQUIREMENT 11, ACCEPTANCE 2, IMPLEMENTED_UNMAPPED 1,
REGISTER_DEFECT 1, REMAINING_WORK 2 (total 17).

By Disposition: ALIGNED 14, STALE_SPECIFICATION 2, REMAINING_STATE_MISMATCH 1.

By Confidence: HIGH 12, MEDIUM 5, LOW 0.

## Parser-gap note (brief Read-first item 5)

`R1_INVENTORY/REQUIREMENT_INDEX.csv` scanned ZERO IDs for DEL-08-04 (the known
regex-parser gap). The 11 requirement rows were re-derived directly from
`Specification.md` Requirements table (DEL-08-04-R01..R11, lines 23-33). The
Datasheet restatements (Attributes/Conditions) were folded into the matching
REQ rows per MR-4; the datasheet-distinct Governance Decision Contract and the
Verification/Documentation implementation-path declarations became the two
ACCEPTANCE rows.

## ID-mapping note (MR-9)

`Specification.md` uses IDs `DEL-08-04-R01..R11`; `Assessment_INSP-03` uses
`REQ-08-04-001..011`. The mapping is 1:1 positional (R0n <-> 00n) and is stated
in each REQ row's AssessmentEvidence. The spec was not materially rewritten
after INSP-03 (both describe the same landed bridge), so no old-REQ conclusion
is orphaned.

## D-APP-10 as governing ruling

The executable bridge is governed by D-APP-10 (Option C, RULED 2026-06-16):
`subagent-bridge.ts` literally encodes `SUBAGENT_BRIDGE_RULING_REF =
'D-APP-10 Option C'`. D-APP-10 is an affirmative permitting decision — it
approves bounded executable Type 2 child-turn integration — so behavioral REQ
rows cite it as governing (R01/R05/R06/R07/R08) or context (R02/R03/R04/R09/R10/R11).
Its boundary list (no capability inheritance, no nested subagents, no
provider/network/Pi, no release/issuance claims) is honored by the
implementation and tests; nothing on this surface crosses those boundaries.

## PKG-08 caution (plan §3 boundary 8)

No claim here required judging or changing an agent instruction file, the agent
matrix, a persona/skill contract, or the dispatch workflow design, so no
DEFERRED_AGENT_WORKFLOW row was emitted. The bridge reads agent instruction
frontmatter (persona `subagents:` allowlist, candidate `AGENT_TYPE`/`AGENT_CLASS`)
as FROZEN_PROCESS_INPUT to make product-runtime allow/deny decisions; the
concordance facts checked are only "does the cited runtime consume that frozen
surface as implemented," which is in scope. If R3 decides the persona-allowlist
frontmatter contract itself needs adjustment, that routes to
AGENT_WORKFLOW_OBSERVATIONS.md — not this ledger.

## Context handle (brief): subagent permission class / conditional Agent exposure

Verified on this surface and mapped as UNMAPPED-1 (Disposition ALIGNED). The
`subagent` permission-class *declaration* lives in
`frontend/packages/harness-contract/src/tool-descriptor.ts` lines 1152-1155
(the Agent tool descriptor: `permissions: ['subagent']`), which is a PKG-06
DEL-06-01 surface (the W2 handle: DEL-06-01 UNMAPPED-1). The *consumption* —
conditional exposure of the `Agent` tool only when a bridge exists and Agent is
requested (`sdk-options-builder.ts` 97-103), and routing the Agent tool to the
subagent hook family (`chirality-hooks.ts` 111-127, 461-476) — is DEL-08-04
behavior, ruled by D-APP-10. UNMAPPED-1 maps the DEL-08-04 consumption and
records the DEL-06-01 cross-deliverable handle so R3 can reconcile the two
without double-mapping the class declaration here.

## Least-confident rows (mandatory self-flagging)

- **DEL-08-04-R07 (ALIGNED, MEDIUM).** Alt reading that flips it: "restricted
  cwd" (Spec R07 / Datasheet line 27) could be read to require a *distinct*
  child working root narrowed below the parent. Implementation gives the child
  `tools: []` + `disallowedTools` + `maxTurns:1` and inherits the parent SDK
  `cwd = session.projectRoot` (no separate child-cwd field), with hook-level
  instruction-root/network blocks. If a distinct narrowed child cwd is required,
  this is PARTIALLY_IMPLEMENTED, not ALIGNED. INSP-03 rated REQ-007 PASS and the
  D-APP-10 required-action bullet is about non-expansion (satisfied), so ALIGNED
  is the primary reading.
- **UNMAPPED-1 (ALIGNED, MEDIUM).** Alt readings: (a) fold entirely into R06/R09
  (no separate row); or (b) if D-APP-10 is judged not to be an "accepted
  mapping" for this specific toggle, it would be IMPLEMENTED_UNDOCUMENTED. I
  treat the D-APP-10 ruling + the in-code `rulingRef` constant as an accepted
  mapping, so ALIGNED (behavior + ruling + tests agree) with the DEL-06-01
  handle noted.
- **DEL-08-04-ACC-001 (STALE_SPECIFICATION, MEDIUM).** Alt reading: the spec
  sentence "exact serialized decision-object type is TBD until implementation
  locates or defines the evaluateSubagentGovernance contract" could be read as a
  *deliberately-open design placeholder* (approval-reference format genuinely
  remains loosely specified as "non-empty string"), in which case it is not
  fully stale. I classify STALE_SPECIFICATION because the decision object is
  concretely defined and exported (`SubagentGovernanceDecision`,
  preflight `safeMetadata`, `ChildRunRecord`), so the flat "TBD" assertion is
  now false (MR-8: flatly-false state -> STALE_SPECIFICATION, repair-shaped, no
  ruling implied).
- **REGISTER-1 / DEP-08-04-003 (REMAINING_STATE_MISMATCH, MEDIUM).** Alt
  reading: the extracted register may deliberately keep `SatisfactionStatus=TBD`
  pending a *formal* dependency-closure acceptance separate from the code
  existing, in which case only the `TargetType=UNKNOWN`/`TargetLocation=TBD`
  cells (not the satisfaction cell) are stale. Either way at least the target
  identification is factually overtaken (evaluateSubagentGovernance is a
  concrete exported function), so a metadata-lag defect stands.

## Register-defect summary (MR-5)

One REGISTER_DEFECT emitted: REGISTER-1 (DEP-08-04-003 — `evaluateSubagentGovernance`
target recorded UNKNOWN/TBD though the contract is concretely landed).

Considered-but-not-emitted (recorded here per the brief's cross-reference duty):
- **DEP-08-04-004 (permission overlay / hook infrastructure) and DEP-08-04-005
  (DEL-04-01 SDK probe)** both carry `SatisfactionStatus=TBD`. The underlying
  capabilities exist live (`permission-overlay.ts`, `chirality-hooks.ts`; SDK
  `agents` are constructed and executable under D-APP-10). I did not flag these
  as defects because their satisfaction is arguably a separate governed gate —
  DEL-04-01 is IN_PROGRESS and D-APP-10 explicitly withholds project-wide
  dependency-closure claims. Lower confidence than REGISTER-1; left as an
  observation.
- **`_DEPENDENCIES.md` "Downstream Handoff Notes: Not applicable;
  CONSUMER_CONTEXT=NONE"** coexists with an active DOWNSTREAM HANDOVER row
  (DEP-08-04-006 -> DEL-08-05). This is a run-parameter artifact (no consumer
  context supplied at extraction), not a register contradiction; not flagged.
- **Declared Upstream/Downstream "TBD"** in `_DEPENDENCIES.md` are human-owned
  declaration sections (docs/SPEC.md §5.2; W3 rule), NOT register defects.
- **`_REFERENCES.md` REF-001..REF-007**: all seven ExpectedSHA256 == ActualSHA256
  re-verified by direct `shasum -a 256` against the live docs this run (all
  MATCH, incl. REF-006 PRD under D-APP-38). No reference defect. The kit's
  C-001 conflict entry (former PRD source-state warning) is correctly recorded
  as resolved.
- **D53A coverage** row `DEL-08-04,Y,6,Y,Y` matches the live Dependencies.csv
  (6 ACTIVE rows, one IMPLEMENTS_NODE anchor, schema valid); the
  `_DEPENDENCIES.md` Lifecycle Summary counts (SATISFIED 1 / PENDING 1 / TBD 4)
  reproduce the live rows. No count-lag defect.

## Remaining section (2 items -> 2 REMAINING_WORK rows)

- REMAINING-1 (gated): per-attempt subagent decision-replay artifact. Gate
  suffix verbatim `(gated: new owner ruling required — D-APP-53 2026-07-10 ruled
  Option A only)`; SelectableUnderCurrentLoop=NO (gate unsatisfied). This is an
  evidence-backed residual (INSP-03 Gap "no persisted decision artifact",
  Forward Rec event/record linkage), NOT a WITHHELD-authorization ACCEPTED_DIVERGENCE:
  D-APP-53 ruled Option A only and did NOT unlock the Option C lane this item
  sits in, so it stays REMAINING_WORK/ALIGNED with HumanDecisionNeeded=NEW-PACKET
  per the W3 judgment rule.
- REMAINING-2 (ungated): the concordance bootstrap item; SelectableUnderCurrentLoop=YES.
  This run is its in-progress execution.

## False-absence discipline (W3 rule)

The "no per-attempt decision-replay artifact" assertion in REMAINING-1 was
checked against the frontend test/lib trees: `evaluateSubagentGovernance` emits
console decision logs (`subagent-governance.ts` 66-81) and `ChildRunRecord`
governance state exists, but grep of `frontend/src` finds no persisted
per-attempt allow/deny decision record/event beyond logs and options — matching
the INSP-03 Gap. No test asserts such an artifact (none should; it is unbuilt).

## Method deviations

None. Two files written (claims.csv, notes.md); all other surfaces read-only; no
tests executed; no lifecycle transitions.
