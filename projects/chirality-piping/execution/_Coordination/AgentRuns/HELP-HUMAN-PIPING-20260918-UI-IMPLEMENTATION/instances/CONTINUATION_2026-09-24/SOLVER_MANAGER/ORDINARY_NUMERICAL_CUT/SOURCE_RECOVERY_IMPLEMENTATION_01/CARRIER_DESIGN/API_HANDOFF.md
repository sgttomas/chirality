# Immediate facade and consumer API handoff

This is a proposal, not a registered contract. The closed wire shape is [source_block_receipt.schema.json](source_block_receipt.schema.json); normative constraints and source custody are in [CONTRACT.md](CONTRACT.md).

```text
MechanicsEnvelope.source_block_recovery?: SourceBlockReceipt  // omit for p1
SourceBlockReceipt = {body, receipt_sha256}
body = {
  receipt_version: "1.0.0", policy: "SOURCE-BLOCKS-1",
  status: "qualified" | "partial" | "unavailable",
  invocation: {algorithm:"sha256", canonicalization:"openpipestress_jcs_ijson_v1",
               payload_scope:"source_blocks_invocation_v1", value:Hex64},
  publication_sha256: Hex64,
  cases: SourceBlockCase[], envelope_observation_result_ids:string[]
}
SourceBlockCase = {
  basis_ref:{ref_type:"load_case",ref_id:string},
  outcome:"qualified"|"unsupported"|"failed",
  requested_mode:"dense_scrutiny"|"sparse_interactive",
  selected_method:"retained_source_blocks_exact_v1" |
                  "ordinary_dense_structural_v1" |
                  "ordinary_sparse_structural_v1" | null,
  ordinary_attempt, source:null|SourceCommitment,
  projections:Projection[], rows:RowTreatment[], supports:SupportAttribution[],
  failure:null|Failure, work:Work
}
```

- `ordinary_attempt` = requested mode, actual outcome, nullable structural-report diagnostic ref, nullable failure-stage/diagnostic, matching ordinary `numerical_quality.cases` index. Preserve existing q fields and M03 policy as ordinary-attempt evidence. N06 may have q unresolved and a qualified exact receipt. A report that never existed stays null.
- `SourceCommitment` = level, complete normalized-source/functional-plan digests, source counts, free/prescribed maps, exact free blocks, member/support IDs. Qualified exact cases require it; ordinary selections have null. These are private finalized producer commitments, not digest-based arithmetic proof.
- `Projection` = projection/function/result IDs, typed quantity, actual final value/bits/unit, interval, absolute/relative error bounds, exact 1e-9 criterion, basis. It comes only from the same private exact Response/plan. All published affine components are recovered before output projection.
- `RowTreatment` = result ID, treatment (`qualified_projection/checked_derived/ordinary_checked/inspection_only`), nullable projection/recipe, input result refs. Exactly accounts for final actual rows; closed reviewed recipe IDs are in the schema. A recipe name alone is not qualified implementation.
- `SupportAttribution` = support/node identity, unique-source attribution and six component mappings with actual ideal/spring/structural-zero source terms. Exact support rows use the already selected physics kind, components and metadata basis.
- `Failure` and `Work` are closed and truthful about actual reached stage and charges. No reset budget or unsafe usize-as-JSON-number.

Mixed-case rule: each requested case qualifies either by complete exact method evidence or the unchanged p1 ordinary predicates under an explicit ordinary tag; Sensitive ordinary never qualifies. All cases qualified => whole receipt qualified. Some => partial. None => unavailable. A partial/unavailable envelope cannot enter qualified Current/rule/export. New producer ID if the source-block method is selected/recorded; p1 record/table remain unchanged. Physics-1 uses its separate explicit dispatch until ROOT's reviewed join.

The source facade should expose private `FinalizedSourceBlockCase` and `FinalizedSourceBlockReceipt` constructors. Public fields/JSON cannot create them; wire deserialization never becomes a live producer certificate. Core TASK only needs to expose privately bound functional/projection/source accessors and metered failure records. It does not own row semantics or external hashes.

Hash order is acyclic:

1. Actual raw invocation `{request:<entire preparse Value>,solver_mode:<actual resolved mode>}`.
2. Private complete normalized source, then source-bound required functional plan.
3. Final raw envelope **without** `source_block_recovery` (all rows/summary/q/status/diagnostics included).
4. Receipt body.
5. Final raw carrier with receipt, then existing outer AnalysisRun/derivative hashes.

Use checked canonical JSON on `{domain:<fixed scope>,payload:<value>}`; exact scope strings are in CONTRACT. No step hashes its own checksum. Consumers recompute invocation from independently retained actual request, publication and receipt hashes; only the actual authenticated producer can warrant hidden source/projection construction.

Extend shared standing with an optional independent source-block context. For p1 keep behavior. For source-blocks-1 require actual invocation binding; the old `(source,requested_case_refs)` inputs alone cannot return positive new-method standing. Caller must additionally keep its current actual source/model/build/input/record authentication.

Whole-envelope gates remain simple: every physical row must be a qualified projection, a registered checked derived recipe, or an ordinary-checked row from a p1-qualified ordinary case. Inspection-only physical rows/headlines withhold the whole envelope. Observational nonphysical rows can remain disclosed. No general capabilities/store framework is introduced.

Input seam: add a Value-aware public entrypoint whose private CapturedInvocation::parse retains the complete actual request Value/mode before checked deserialization. No DTO reserialization, default insertion or unknown-field dropping. Private implementation receives optional capture. Existing typed entrypoints keep historical ordinary/p1 behavior and cannot mint an eligible source-block receipt; adapters/observer must migrate to the raw Value entry. Public JSON/hashes cannot construct the capture.
