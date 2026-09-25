# Independent scientific JSON design review

**Result: clear after a custody-contract clarification.** No unresolved blocking
design finding remains in the six-file packet identified by
[FINAL_HASHES.json](FINAL_HASHES.json). This is a prospective design review, not
qualification of a new canonicalizer, producer, numerical method or result.
Current source-method qualification need not adopt or wait for this design.

Reviewer `/root/load_state_design/reference_review` acted as TASK (Type 2),
following a new bounded assignment from `/root/load_state_design`. The actual
mechanism was native `collaboration.followup_task`; no delegation occurred.
Instruction origins and initial packet hashes are in
[BASIS_START.json](BASIS_START.json). Writes stayed in this review directory.
The committed LOAD_REFERENCE_STATES packet was not edited. No Git mutation,
product change, Cargo/npm/build, native interaction, operational library data or
code rule was involved.

## Finding and repair

**SJ-R1, P2, resolved — raw custody and semantic identity needed concrete separate
carriers.** The draft correctly stated that canonical hashing loses spelling and
discarded precision, but “keep raw supplied document and consumed projection
linked” left the raw-custody carrier implicit. A future reader could wrongly
interpret a canonical invocation hash as authenticating the original supplied
bytes. The independent control confirms that `{"x":9007199254740993}` and
`{"x":9007199254740992}` have different raw SHA-256 digests but identical
binary64 semantic serialization.

The final DESIGN now specifies `ingress_kind`, the exact `source_text_scope`, a
source-created `source_utf8_sha256` with retained bytes when raw custody is
claimed, and a separate `canonical_invocation_sha256` over the admitted request,
mode, profile and receipt domain. It does not fabricate source text from an
already parsed object or accept caller-supplied digests as capture. Digest
preimages are acyclic. These additions resolve the ambiguity without requiring
a general evidence framework.

The caller subsequently clarified typed-count variant preservation, bounded
token parsing and implementation paths. Those final changes were read and are
included in the final hashes. A root-origin stress-unit counterexample was also
added during review and independently checked below.
The final parent handoff RETURN.md was read and included; its reference-versus-
production limits match the underlying evidence.

## Standards and semantics

The reference account accurately separates normative categories and local
application choices:

- [RFC7493 §2.2](https://www.rfc-editor.org/rfc/rfc7493.html#section-2.2)
  concerns binary64 interoperability and exact large-integer expectations. It
  does not justify rejecting every large integral-valued finite real. The
  explicit safe-integer field range remains a valid application constraint.
- [RFC8785 numeric serialization and Appendix B](https://www.rfc-editor.org/rfc/rfc8785.html)
  use binary64/ECMAScript semantics; application integer interpretation does not
  change the serializer. Its finite examples include 2^68 and subnormals. It
  distinguishes rendering from admissible input and requires preserved strings,
  UTF-16 property order, valid Unicode, and nonfinite rejection. The proposal's
  integer-token grammar and nonzero-underflow rejection are explicitly stricter
  application rules. The document is Informational, not Standards Track.
- The official [RFC8785 errata listing](https://www.rfc-editor.org/errata/rfc8785)
  reports 7920 as **Verified**, recommending negative-zero input rejection, and
  6292 as **Verified**, editorial. The official
  [RFC7493 errata listing](https://www.rfc-editor.org/errata/rfc7493) reports 5354
  and 6861 as **Reported**. The design correctly does not present either as a
  verified standards correction. Extending scalar/noncharacter checks to a
  top-level string is an explicit application policy.

Direct errata fetches failed through the web tool; one reported a redirect to
the errata host and another a rate limit. The observed status evidence came
from complete official RFC Editor search records. No successful live direct
fetch or exhaustive future-standards check is claimed.

The proposed real/count distinction is implementable. Typed integer admission
must precede float normalization; retaining an admitted integer representation
for typed DTO construction does not require a different canonical numeric
renderer. Arbitrary-precision identifiers/operands stay strings. Exact field
inventories and narrower bounds remain required implementation work.

Rejecting new negative-zero input and normalizing computed public zeros are
different operations. The design correctly requires a successor publication
recipe and row binding after public-zero projection, preserves exact source bit
strings, and forbids using canonicalization to repair untrusted results. It
does not silently change historical source-blocks or p1 meaning.

## Independent observations

Reviewer-owned [reference_probe.py](reference_probe.py) and
[reference_probe.mjs](reference_probe.mjs) import only standard libraries and
built-ins. They import neither product code nor the author probe. Exact rational
distance to adjacent binary64 values checks conversion decisions; the stock
Node number renderer supplies separate reference observations.

Actual commands and output are retained in [CHECK_RUN.json](CHECK_RUN.json),
with values in [PYTHON_REFERENCE.json](PYTHON_REFERENCE.json) and
[NODE_REFERENCE.json](NODE_REFERENCE.json):

- **29 parsing cases pass**: 24 representative numeric tokens and five exact
  midpoint cases. Python 3.13 and Node 24.18 agree on 28 finite bit patterns and
  the one overflow classification. Additional exact overflow-boundary controls
  distinguish the largest finite value from conversion to infinity.
- **All 24 finite RFC8785 Appendix B vectors** match stock Node's numeric JSON
  rendering. This includes the historical negative-zero-to-zero algorithm
  vector; it does not admit negative-zero input under the proposed profile.
- Direct integer, decimal and exponent spellings converge on the expected real
  bits. A u64-max token becomes binary64 2^64, whose ECMAScript text is
  `18446744073709552000`, not the original u64 digits. `1e160` is finite and
  integral-valued. `1e20` renders in plain decimal.
- Exact-integer lexical/range checks reject fractional/exponent spellings and
  unsafe magnitudes before their information disappears. A separate
  nonnegative-count bound rejects -1. Python bool is an int subclass; Python's
  ordinary parser erases the sign of integer-token -0 while retaining the sign
  of -0.0. These observations support the required typed/raw boundary checks.
- Exact halfway values near 1 and the smallest subnormal exercise ties-to-even;
  nearby decimal values discriminate from the tie. Nonzero values that round to
  zero demonstrate the new ingress refusal case.
- Decoded duplicate keys, supplementary characters, surrogate/noncharacter
  controls, and UTF-16 sorting pass the independent checks. This is not a new
  production Unicode validator. The design preserves NFC/NFD distinctions.
- Stock JS observations confirm why freezing must precede JSON.stringify:
  negative zero becomes 0, nonfinite values become null, undefined/hole data can
  disappear or become null, getters execute, and BigInt throws. The strict
  prospective adapter itself was not implemented or tested here.

These are reference/host probes, **not Rust authority, WASM, native application
or new-profile conformance tests**. The author probe's narrower claim remains
accurate. No passing host probe implies a qualified solution for those numbers.

## Stress-unit extension

Independent rational arithmetic on the actual represented inputs
`1e-306 N / 596902.6041820607 m²` confirms the root-supplied distinction:

| Representation | Bits | Relative error against represented-input exact division |
|---|---|---|
| Pa | `0000004ef331b289` | approximately 6.645747e-13 |
| Binary64 MPa after division by 1e6 | `0000000000052c90` | approximately 1.269450175e-6 |

Pa passes the unchanged 1e-9 criterion for this example; MPa fails it. Both are
finite subnormals, and Python/Node reproduce the same bits. This demonstrates a
unit-projection loss rather than a JSON magnitude failure. It is an arithmetic
witness, not an independently observed product execution.

The new SI quantity carrier is a reasonable narrow remedy: preserve Pa with its
dimension, unit and standing across rows, maxima, summaries and machine export;
version downstream readers; keep display formatting separate. The design
explicitly refuses renaming the unit beneath `max_stress_mpa`, changing old
hashes, or loosening the tolerance. Actual calculation error and final stored
unit error must remain separate. If Pa itself is inaccurate, serialization
cannot make the value qualified.

## Implementation map and limits

Bounded source inspection, recorded in [SOURCE_SEAMS.json](SOURCE_SEAMS.json),
confirmed the v1 unsafe-integral-float guard, the unrestricted exact i64/u64
rendering branches, strict adapter seams, and the existing source invocation's
pre-DTO serde Value capture. That capture is not original byte custody. The
inspected files were moving working source; this was not a complete frozen
implementation review.

The map covers the necessary authority, adapter, capture, producer, readers,
schema and persistence seams. Remaining qualification includes the actual Rust
parser/renderer, raw lexical admission at every transport, field inventory,
successor row/receipt/unit bindings, unchanged legacy hashes, genuine producer
invocations, and native/save/reopen/export witnesses. A generic hash helper alone
cannot certify typed-count correctness or Current/rules/export eligibility.
Preserve the old 1e160 refusal and current numerical containment. No source
method or previously verified historical contract is superseded by this review.

## Final display-path backcheck

ROOT requested a bounded follow-up after the first review freeze. The original
six-file hash manifest and review return are preserved verbatim as
[BEFORE_DISPLAY_FINAL_HASHES.json](BEFORE_DISPLAY_FINAL_HASHES.json) and
[BEFORE_DISPLAY_RETURN.md](BEFORE_DISPLAY_RETURN.md). The final hashes now cover
the added display-path paragraph/map entry, the corresponding parent-return
limit clarification, and six joined-source origins in BASIS. The numeric
contract, reference cases, author probe and reference document are unchanged;
the already passing numerical probes were not rerun.

Read-only inspection of the six added source files matched all six parent basis
hashes. [DISPLAY_BACKCHECK.json](DISPLAY_BACKCHECK.json) records those identities
and observations. The inspected chain is:

1. `QuantityReadout` consumes `useDisplayQuantity`, which accepts a response
   marked converted when the value is finite and the target unit matches.
2. `displayQuantityService` dispatches the conversion through the Tauri command
   or the loaded WASM engine.
3. `operation_applier/src/display_units.rs` accepts the finite result of
   `convert_for_dimension` as converted.
4. `core/units/src/lib.rs` preserves same-unit identity and otherwise performs
   the unit scale/offset operations. The cross-unit path has no relative-error
   bound. Finiteness alone can admit an inaccurate subnormal or a zero projection.

The added loss-location distinction is accurate after a wording clarification:
the canonical derivative copies received value/unit into target rows and
validates that preservation; AnalysisRun retains unit annotations and hashes
and binds the unchanged received rows/result, without embedding a second
numeric-value table. Neither operation is the separate source-block producer
recipe that publishes a fixed MPa value.

This follow-up establishes source/interface facts only. It does not reproduce a
current physics producer failure, run a native display scenario, qualify a
precision-aware conversion implementation, or change the earlier review limits.
The prospective display response and base-value preservation remain authorized
implementation work. No additional blocking finding remains.
