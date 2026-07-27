# PROJECT_SETUP Blocker — G2 Nested Deliverable Ownership

State: `RESOLVED_BY_G2_CAPABILITY_CORRECTION`

Resolution basis:
`ff04694afa709856a58f9f54a79ca2056b8e0b4e` (PR #368)

## Trigger

After PREPARATION created DEL-02-06, PROJECT_SETUP applied the exact G1/G2/G3
state changes approved in SCA-001:

- G1 count 45 → 46 and basis → PR #366 merge SHA;
- G2 PKG-02 gains `runtime/**`;
- G2 gains the approved DEL-02-06 deliverable entry; and
- G3 basis → PR #366 merge SHA and PKG-02 gains `runtime/**`.

Observed results:

- G1: PASS, 46 status files;
- G2: BLOCK;
- G3: PASS, six pending nodes and no edges; and
- G0: registration-file PASS, but it does not rerun G2 and therefore does not
  discharge the live G2 blocker.

## Exact G2 finding

```text
G2 BLOCK: surface-ownership register execution/_harness/surface_ownership.yaml is invalid:
  - entry DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance: undeclared write target — no declared target covers the entry's own tree execution/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/
  INFO: identical write target 'runtime/**' declared by ['DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance', 'PKG-02_Operative_Instruction_Surface_and_Runtime_Layers'] — recorded as a static fact only; this guard makes no concurrency claim (serialization is G3's question)
```

## Cause

The approved G2 entry correctly declares the actual nested deliverable tree:

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/**`

The current validator's own-tree check constructs
`execution/{entry_id}/` for every entry. It does not distinguish
`kind: deliverable` from `kind: package`, so no truthful nested deliverable
entry can satisfy that check.

## Scope boundary

SCA-001 §4.5 required validator code to remain unchanged and directed any real
capability gap to separate governed work. PROJECT_SETUP therefore:

- did not add a false top-level target;
- did not remove the approved deliverable-level entry;
- did not edit validator code or tests;
- did not dispatch post-change AUDIT_DECOMP;
- did not stage, commit, push, or open a PR; and
- did not perform any product or runtime work.

## Decision routes

1. **Recommended — bounded G2 capability correction.** Through the appropriate
   HELPS_HUMANS/M2 instruction-tool tranche, teach G2 to validate nested
   `kind: deliverable` ownership against its actual declared tree and add
   deterministic tests. Then resume this PROJECT_SETUP run and require
   G0–G4 plus 46/46 AUDIT_DECOMP.
2. **State-only deferral.** Remove the deliverable-level G2 entry and rely on
   PKG-02 ownership of its execution tree plus `runtime/**`. This is smaller
   but gives up the fine-grained ownership record approved in SCA-001 and
   therefore requires an explicit owner-approved propagation deviation.

No other route is proposed. A fabricated `execution/DEL-02-06.../**` target
would misstate the filesystem and is rejected.

## Resolution

The owner selected Route 1 and declined Route 2. HELPS_HUMANS delivered the
bounded M2 correction in PR #368; its governance-harness check passed and the
merge commit above became the resumed instruction basis.

PROJECT_SETUP then reran the accepted nested entry unchanged. G2 passed with
seven entries, six materialized package children, exact deliverable-register
membership, and strict containment of DEL-02-06 beneath PKG-02. The shared
`runtime/**` declaration remains an informational static fact only. No false
top-level target, schema change, ownership-policy change, or state-only
deviation was introduced.
