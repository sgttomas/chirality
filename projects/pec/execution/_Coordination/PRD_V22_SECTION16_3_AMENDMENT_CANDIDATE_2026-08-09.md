---
doc_kind: coordination.product_authority_amendment_candidate
status: DRAFT_FOR_OWNER_RULING
prepared: 2026-08-09
prepared_by: SCOPE_CHANGE
basis_git_ref: origin/main
basis_git_sha: d269f0e04204bc463a11684499213b2283bd28f7
target: projects/pec/docs/PRD.md
target_preimage_sha256: 6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba
authority_effect: NONE_UNTIL_OWNER_RULING_AND_EXACT_POSTIMAGE_ADOPTION
---

# PEC PRD v2.2 §16.3 amendment candidate — loop-registry disposition

## 1. Candidate status and boundary

This is a preparation-only, non-binding decision interface produced from the
owner's 2026-08-09 direction. It is not a ruling, an adopted PRD postimage, a
decomposition amendment, a SCOPE_CHANGE intake, or permission to edit any
governed surface. Its only purpose is to present exact successor wording for
the stale product-authority text in PRD §16.3.

Package-role classification: this file is a **coordination candidate**. It is
derivative of the accepted records cited below and is authoritative for none
of the product, decomposition, source, lifecycle, or release facts it
summarizes.

## 2. Verified conflict

### 2.1 Exact current product text

At `origin/main@d269f0e04204bc463a11684499213b2283bd28f7`, the adopted PRD
preimage is SHA-256
`6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
Its current section heading and item 3 are, exactly:

```markdown
## 16. Open product decisions (owner)

3. Home and shape of the loop registry (which loops PEC serves; today five).
```

The section closes with the exact sentence:

```markdown
None of these blocks P0–P2.
```

These bytes occur at `projects/pec/docs/PRD.md` §16, currently lines 493,
499, and 515 respectively. Item 3 therefore still textually presents the
loop-registry home and shape as open.

### 2.2 Later accepted product decision

`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md`
is SHA-256
`3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565`.
It records:

- status `RULED O-A / PRODUCT DECISION SETTLED / SCOPE_CHANGE INTAKE REQUIRED`
  (line 3);
- the verbatim owner ruling `D-PEC-78: O-A` (line 75);
- the selected long-term shape: the existing PEC-owned JSON/schema paths and
  typed core port, with strict schema version 1, PEC ownership limited to its
  configured service set, and each listed loop retaining authority over its
  entrypoint and governed truth (lines 77–83); and
- the explicit statement that the ruling settles upstream PRD §16.3 / OI-003
  while changing no source or accepted decomposition byte (lines 85–88).

The associated packet at
`projects/pec/execution/_Coordination/D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md`
defines O-A's exact homes as
`projects/pec/v2/config/loops.json` and
`projects/pec/v2/config/loops.schema.json`, and its typed core contract as
`RegisteredLoop` plus `LoopRegistry.registered_loops()`.

### 2.3 Already-accepted decomposition truth

The required downstream propagation already completed through SCA-004; it is
not awaiting this PRD correction:

- `SCA-004_2026-08-02_2325/Decision_Log.md`, SHA-256
  `c377d7f094b46ede1b0ec8f108e7c52e61dada9565227820415b47301a87cd3c`,
  records confirmed Gate 1 resolution of OI-003 and confirmed/executed Gates
  2–5.
- `SCA-004_2026-08-02_2325/Handoff_State.md`, SHA-256
  `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c`,
  identifies revision 1.4 as the authoritative successor under D-PEC-78 O-A,
  with closure `CLOSED_FOR_SCOPE_CHANGE_ONLY`.
- `projects/pec/execution/_Decomposition/_LATEST.md`, SHA-256
  `7abf65e641a5a247f0c783192808ae1f9186f76ebe0d09d6e84e2983fffcd7a3`,
  points to revision 1.4 `current_basis` and says OI-003 is retained and
  resolved.
- `SOFTWARE_DECOMP.md` revision 1.4, SHA-256
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`,
  carries SOW-077 as `IN` at §2, OI-003 as resolved at §10, and SCA-004 in
  revision history.
- `ScopeLedger.csv`, SHA-256
  `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25`,
  maps SOW-077 to `PKG-01 / DEL-01-06 / OBJ-004` under D-PEC-78.

**Verdict:** the mismatch is a stale statement in the adopted product
definition. The accepted decomposition is already current. Correcting the
PRD is a product-authority amendment and must not be represented as new or
replacement decomposition truth.

## 3. Proposed exact §16 replacement — recommended

Preserve item number 3 so existing `§16.3` citations remain stable. Apply the
following three exact substitutions only within §16.

### 3.1 Heading

Replace:

```markdown
## 16. Open product decisions (owner)
```

with:

```markdown
## 16. Product decisions (owner)
```

### 3.2 Item 3

Replace:

```markdown
3. Home and shape of the loop registry (which loops PEC serves; today five).
```

with:

```markdown
3. **Resolved 2026-08-02 by `D-PEC-78` O-A.** The long-term home and shape
   of PEC's loop registry is the existing PEC-owned strict-version-1
   JSON/schema paths with the core-owned typed `LoopRegistry` port. PEC owns
   only its configured service set; each listed loop remains authoritative
   for its own entrypoint and governed truth. Later row changes remain
   owner-gated PEC configuration changes. Listing or removing a loop creates
   no duty, lifecycle effect, cadence, conformance obligation, or authority
   over that loop, and no governed act may depend on PEC or the registry.
```

### 3.3 Closing sentence

Replace:

```markdown
None of these blocks P0–P2.
```

with:

```markdown
None of the remaining open decisions blocks P0–P2.
```

This wording transcribes and clarifies D-PEC-78 O-A; it proposes no new
registry owner, path, contract, compatibility rule, consumer effect, or
cross-loop duty. An adopted product amendment should advance the PRD version
from v2.2 to v2.3 and record the eventual ruling ID/date in the document
header. Those mechanical header bytes are deliberately not invented here:
they must be included in, hashed with, and accepted as part of the later exact
PRD postimage.

## 4. Owner options

| Option | Owner disposition | Effect |
|---|---|---|
| **ADOPT** | Approve the exact §16 semantic replacement in §3 and authorize preparation of a byte-pinned PRD v2.3 postimage and D-PEC product-amendment packet. | Opens only the exact-postimage preparation gate described in §6; does not itself edit the PRD. |
| **AMEND** | State exact changes to the §3 wording, version posture, or application fence. | Regenerate this candidate or the exact postimage for a later owner gate; no wording is inferred. |
| **DECLINE** | Reject this candidate. | PRD v2.2 remains unchanged; D-PEC-78 and SCA-004 remain effective and the textual mismatch remains disclosed. |
| **DEFER** | Leave the candidate pending and name a trigger or review date. | PRD v2.2 remains unchanged; no product, decomposition, source, or lifecycle state moves. |

## 5. Non-binding recommendation

**Recommend ADOPT.** The proposed in-place replacement is the smallest
correction that removes the false open-state signal, preserves stable §16.3
citations, and states the already-ruled D-PEC-78 boundaries. Deleting item 3
and renumbering the list is not recommended because it would make existing
§16.3 references ambiguous and create avoidable citation churn.

## 6. Exact on-ruling mechanism and gates

No step below is authorized by this candidate.

1. **Semantic disposition gate — owner.** The owner chooses `ADOPT`, `AMEND`,
   `DECLINE`, or `DEFER`. `ADOPT` approves only the exact §16 semantic payload
   in §3 for exact-postimage preparation.
2. **Exact carrier preparation — PEC product-governance owner.** Allocate the
   next valid D-PEC decision ID from the live register at that time. Prepare a
   product-amendment packet and exact PRD v2.3 postimage against PRD preimage
   SHA-256
   `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`.
   The packet must include the final header/version/date/ruling-ID bytes, the
   exact path fence, postimage SHA-256, verification, rollback, and this
   candidate as non-authoritative preparation evidence. Preparation writes
   remain coordination-only; the live PRD is not edited.
3. **Exact-byte adoption gate — owner.** The owner rules on the identified
   D-PEC packet and exact PRD postimage by hash. No approval is inferred from
   the recommendation or from a semantic `ADOPT` disposition alone.
4. **Application gate — ruled exact fence only.** After exact-byte adoption,
   apply only the ruled product-governance postimages. At minimum the fence
   must identify `projects/pec/docs/PRD.md` and the new D-PEC carrier/register
   surfaces. Any standing-plan, pointer, status, receipt, or other concordance
   edit must be named explicitly in that same ruled fence; otherwise it
   remains unchanged.
5. **Product/decomposition parity gate.** Verify that the adopted PRD wording
   is semantically identical to D-PEC-78 O-A and revision 1.4. Because SCA-004
   already propagated the same meaning, no SCA is opened and no decomposition
   byte or pointer moves. If the owner-amended wording introduces any new or
   conflicting product meaning, stop and route a separate human-gated
   SCOPE_CHANGE impact intake; do not silently treat SCA-004 as covering it.
6. **Git closeout gate — CHANGE.** Staging, commit, push, or merge is a later
   CHANGE-owned act after validation. Product adoption and Git publication
   remain distinct.

## 7. Verification for a later application tranche

The applying tranche must record all of the following:

1. `git rev-parse HEAD` descends from the ruled immutable basis, and the live
   PRD preimage hash matches the packet.
2. The final §16 heading, item 3, and closing sentence are byte-identical to
   the exact adopted postimage.
3. The PRD header consistently names v2.3, the actual ruling date, and the
   actual D-PEC decision ID; that decision record names the accepted PRD
   postimage hash.
4. `D-PEC-78` and its packet remain byte-unchanged historical authority.
5. `_ScopeChange/_LATEST.md`, `_Decomposition/_LATEST.md`,
   `SOFTWARE_DECOMP.md`, `ScopeLedger.csv`, and SCA-004 remain byte-unchanged;
   their live hashes still match the accepted evidence in §2.3.
6. A targeted search finds no present-current PRD statement that §16.3 is
   open, while the eight other §16 decisions remain open exactly as before.
7. No source/configuration, lifecycle, artifact, dependency, estimate,
   schedule, receipt, or foreign-loop path appears in the diff unless a later
   owner ruling separately names it.
8. The PEC reliance-hold preflight permits the exact correction preparation
   and later candidate validation at the time each act runs.
9. `git diff --check` passes, and the changed-path set equals the exact ruled
   fence.

## 8. Rollback for a later application tranche

- Before Git publication, restore the ruled PRD preimage and any other
  pre-existing ruled surfaces to their exact preimage blobs; remove only a
  newly prepared, unaccepted carrier if the applicable governance procedure
  permits it.
- After publication, use a separately approved revert or successor product
  decision. Do not silently rewrite the adopted PRD history, D-PEC-78, or any
  SCA-004 artifact.
- No decomposition rollback is part of this amendment because this candidate
  proposes no decomposition change and revision 1.4 remains the accepted
  current basis.

## 9. Non-effects

This candidate, any semantic disposition on it, and the recommended product
correction do not by themselves:

- amend, reopen, supersede, or rerun SCA-004;
- change accepted decomposition revision 1.4, its pointers, hashes, topology,
  mappings, objectives, open-issue counts, or derivative-closure state;
- open or execute another SCOPE_CHANGE gate;
- change `loops.json`, `loops.schema.json`, `RegisteredLoop`, `LoopRegistry`,
  adapters, tests, or any source/configuration byte;
- add, remove, retarget, activate, poll, or impose a duty on any loop or
  consumer;
- resolve any of the eight other open PRD §16 decisions;
- update Task Management, decisions/registers, the standing plan, receipts,
  status, lifecycle, dependencies, estimates, schedules, artifacts, reviews,
  releases, or reliance state;
- authorize implementation, external writes, professional reliance, or Git
  staging/commit/push/merge; or
- cure the separately recorded stale derivative surfaces in SCA-004's
  `Handoff_State.md`.

## 10. Preparation result and blockers

- **Candidate readiness:** `READY_FOR_OWNER_DISPOSITION`.
- **Preparation blocker:** none. The exact textual mismatch and successor
  authority are verified at the stated basis.
- **Application blockers:** owner semantic disposition; exact D-PEC ID and
  byte-pinned v2.3 carrier/postimage preparation; owner exact-byte adoption;
  ruled fence; product/decomposition parity verification; separate CHANGE
  closeout.
- **Current governed state:** unchanged.
