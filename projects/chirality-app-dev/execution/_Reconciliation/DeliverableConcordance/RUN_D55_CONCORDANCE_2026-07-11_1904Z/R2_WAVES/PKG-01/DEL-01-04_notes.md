# DEL-01-04 concordance notes — R2 Wave 5 (PKG-01)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; frontend reviewed at `fac46e33f`
(byte-identical through HEAD `242900ae9`); documents/registers read at
`242900ae9`. Discovery only; no file outside the two wave artifacts touched.

## Census

**20 rows total.**

By ClaimType:

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 11 |
| EXCLUSION | 4 |
| ACCEPTANCE | 4 |
| REMAINING_WORK | 1 |
| REGISTER_DEFECT | 0 |

By Disposition:

| Disposition | Rows |
|---|---:|
| ALIGNED | 15 |
| STALE_SPECIFICATION | 4 |
| DOCUMENTED_UNIMPLEMENTED | 1 |

Requirement re-derivation: the R1 REQUIREMENT_INDEX carries all 11
`DEL-01-04-REQ-###` IDs (no parser gap for this deliverable); the re-derived
set from `Specification.md` lines 29–39 matches it exactly. MR-4 fold: the
Datasheet Attributes rows restate the REQ set and were folded into the REQ
rows; the four ACCEPTANCE rows carry only datasheet/kit-distinct conditions
(lifecycle wording, BR-005 register wording, the SCA-APP-001 register
expectation, the corpus-version label).

## Enforcement-truth checks performed (PKG-01 duty)

Every boundary the register asserts as OUT was checked against the live tree,
not just the documents:

- **SOW-065 / REQ-002:** no plugin loader, marketplace, remote MCP config, or
  tool-search surface in `frontend/src` or `frontend/electron`; MCP servers
  are in-process (`read-tools.ts` 1051–1081); the only network-touching tools
  are the two ruled pec proposal tools on a 127.0.0.1 endpoint-allowlisted
  transport (D-APP-52).
- **SOW-076 / REQ-003/004:** `sdk-options-builder.ts` defaults
  `settingSources` to `[]`, admits only `'project'` (never user/local), and
  gates `bypassPermissions` behind `CHIRALITY_ALLOW_SDK_BYPASS=1`; tests
  assert all three behaviors.
- **SOW-077 / REQ-005/006:** live-absence grep for all five retired PKG-08
  item names is clean; runtime event logging exists exactly as the allowed
  adjacent infrastructure (`sessions/<id>/events.jsonl`).
- **SOW-078 / REQ-007:** `package.json` build config has a single mac
  dmg/arm64 target, min macOS 15.0.0, unsigned; no win/linux target;
  policy test pins it.
- **Domain boundary / REQ-008:** four `mcp__chirality__domain_*` tools live
  under D-APP-49..52 rulings; no apply surface exists (grep clean); human
  gate preserved.

No boundary the register declares OUT is crossed by the implementation
without a ruling; no retired-scope item is present live. Hence no
enforcement-defect rows.

## Least-confident rows (mandatory self-flagging)

1. **DEL-01-04-ACC-002 (STALE_SPECIFICATION, MEDIUM)** — originally recorded
   ACCEPTED_DIVERGENCE (this agent's self-flagged alternative); flipped to
   STALE_SPECIFICATION at W5 fan-in verification, and I concur on review:
   the strict affirmative-permission test fails — D-APP-50's "Scope not
   granted" and D-APP-52's "What this authorizes" affirmatively permit the
   TOOL SURFACE (with riders) but contain no text accepting or deferring the
   BR-005 register-wording divergence; MR-11 routes an untranscribed ruled
   pivot to MR-8, and the row's own RemainingWork ("annotate BR-005 … so the
   register row again matches the ruled boundary") is repair-shaped, which
   is by definition not ACCEPTED_DIVERGENCE. Evidence cells unchanged; only
   the disposition token flipped. **Minority ALIGNED reading flagged for
   R3:** BR-005's own statement carve-in ("agents may write proposals and
   summaries, while application requires explicit human acceptance")
   arguably already covers the ruled propose/validate/read surface; the
   pivot fact is whether the staged loopback tools count as "domain-engine
   integration as a shipping feature". Under that reading the row is ALIGNED
   and no repair is implied.
2. **DEL-01-04-ACC-003 (DOCUMENTED_UNIMPLEMENTED, MEDIUM)** — `_CONTEXT.md`
   SCA-APP-001 alignment says the register "must prohibit Pi
   adapter/import/spike and concrete provider expansion", and no BR row or
   REQ carries it. **Alternative reading:** the SCA note is context/impact
   narration rather than a normative register requirement (it never entered
   the Specification requirement set), in which case there is no claim and
   the row drops to a notes observation. I kept the row because the sentence
   is imperative ("must prohibit") and SCA-APP-001 is accepted. D-APP-44's
   F1 amendment (owner-permitted, default-closed provider config) is context
   for wording, not a supersession of the default-closed posture.
3. **DEL-01-04-REQ-011 (ALIGNED, MEDIUM)** — REQ-011 requires the rows and
   fields to be *inspectable*, which they are; the all-TBD Human Ruling
   fields are the designed conservative state (REQ-010/K-INVENT-1).
   **Alternative reading:** INSP-03's PARTIAL treats unruled fields as an
   unmet part of REQ-011 → PARTIALLY_IMPLEMENTED with the owner ruling as
   the residual. I put the owner act in RemainingWork/NEW-PACKET instead of
   flipping the disposition, because the requirement text asks for fields,
   not rulings.
4. **DEL-01-04-REQ-008 (ALIGNED, MEDIUM)** — read "operation execution" as
   *applying* operations (apply excluded outright, human-gated), which the
   live tree honors. **Alternative reading:** the write-graded
   `domain_propose_operation` already counts as domain operation execution →
   the row would become ACCEPTED_DIVERGENCE under D-APP-50/52 rather than
   ALIGNED. The spec's own second clause ("proposal records and explicit
   human acceptance before application") supports the narrower reading.

## Register-defect summary

**0 REGISTER rows.** All three registers were verified directly:

- `Dependencies.csv`: 13 rows, schema-consistent, all ACTIVE/SATISFIED,
  LastSeen 2026-07-10; counts match the `_DEPENDENCIES.md` lifecycle summary
  exactly; D53A evidence file agrees (13 closed / 0 open).
- `_REFERENCES.md`: all seven hashes recomputed live this run — every one
  matches, and the values equal the corpus **v6** snapshot
  (`AUTHORITY_CORPUS.json`, binding commit `a9fb1af4a`).
- The staleness found is all **kit text about the registers**, not register
  content, so it is classified per MR-8 as STALE_SPECIFICATION on claim rows
  instead of MR-5 REGISTER rows: Procedure line 14 ("declares none extracted
  yet" — false since 2026-05-20) on EXC-002, and the "D-APP-38 corpus `v1`"
  labels (Datasheet 36/78, Procedure 12, Guidance 65–66) on ACC-004. If the
  fan-in verifier prefers these coded as REGISTER metadata-lag rows, the
  facts transfer 1:1.

## Other observations (no rows)

- Guidance CF-001 (dispatch-path package naming vs
  `PKG-01_Product_Governance_and_Reliance_Boundaries` on disk) remains an
  open TBD conflict-table entry about a historical dispatch string; it is a
  preserved human-ruling placeholder, not a live normative conflict, so no
  AUTHORITY_CONFLICT row.
- `_DEPENDENCIES.md` has no human-owned Declared Upstream/Downstream content
  (both sections point at the extracted register); Procedure line 14 records
  the declared lists as TBD. Per the Wave-5 rule this is not a register
  defect; noted for the SPEC §5.2 declared-vs-extracted distinction.
- INSP-03 carries no ADQ superseding note; its now-false statements
  (lifecycle CHECKING, REF-006 mismatch open, 13 deps PENDING) are recorded
  as OVERTAKEN in `AssessmentEvidence` on the rows they touch, and the ACC-004
  RemainingWork proposes the R5 supersession annotation. No row uses
  STALE_ASSESSMENT because in each case a kit surface (not only the
  assessment) still carries the stale wording, making STALE_SPECIFICATION the
  operative defect per MR-1.

## Method deviations

None. No tests executed; behavioral evidence bound to
GATE-TRANSCRIPT(W1@fac46e33f); cross-project surfaces untouched (the pec
engine seam was assessed only via this project's own frontend sources and
D-APP-51/52 ruling records); no secret or key values copied.
