# Versioned Amendment — Candidate Harvest Post-Acceptance Whitespace

Date: 2026-08-09

Status: **CORRECTIVE PROVENANCE RECORD — NOT A FRESH OWNER ACCEPTANCE**

Affected path:
`execution/_Coordination/_TaskManagement/CANDIDATE_HARVEST_2026-08-09_GENERATIONAL_PASS.md`

## Version identities

| Version | Identity | Size | Authority posture |
|---|---|---:|---|
| Owner-accepted report bytes | SHA-256 `bee380dedbcc302dc7be606cf55c05a8431d6398995c4d488a79c2044d3a3cab` | 7,006 bytes | Object accepted by `ACCEPT the report and PROMOTE NO CANDIDATES.` |
| Post-acceptance repository amendment | SHA-256 `3ca25470440490360af014d526a285b2d407df0979f3a2ddf21fac4c329ebac1` | 7,000 bytes | Custodial whitespace-clean version; not separately accepted |

## What changed, when, and why

The change occurred after the owner's Step-2 acceptance and before the first
PR #532 commit `f3af7bbbb9e46e07ca1b653cf7bd99a415e8e0d3`, during final pre-commit
validation on 2026-08-09. No finer durable wall-clock timestamp was recorded.

`validate_candidate_whitespace.py` reported trailing whitespace at report
lines 5, 6, and 7. To satisfy that repository guard, exactly two trailing
ASCII spaces (`0x20 0x20`) were removed immediately before the LF on each
line—six removed bytes total:

```text
line 5 accepted: Invoking loop: Root[SP][SP]\n
line 5 amended:  Invoking loop: Root\n

line 6 accepted: Register home: `execution/_Coordination/_TaskManagement/`[SP][SP]\n
line 6 amended:  Register home: `execution/_Coordination/_TaskManagement/`\n

line 7 accepted: Mode: Candidate harvest (generational pass, Step 2)[SP][SP]\n
line 7 amended:  Mode: Candidate harvest (generational pass, Step 2)\n
```

No other byte changed. The edit removed Markdown hard-break whitespace only;
the words, findings, counts, candidate conclusions, and recommendation
remained identical. That semantic observation does not transfer the owner's
byte-bound acceptance to the amended version.

## Faithful reconstruction

The accepted bytes are faithfully reconstructible: append `0x20 0x20`
before the LF on current lines 5–7. Applying exactly that reverse delta to
the 7,000-byte `3ca25470…bac1` version yields 7,006 bytes with SHA-256
`bee380dedbcc302dc7be606cf55c05a8431d6398995c4d488a79c2044d3a3cab`.

The accepted byte object is not committed as a second Markdown file because
doing so would deliberately reintroduce the whitespace-guard violation that
caused the custodial amendment. This record preserves the exact reversible
delta, both complete identities, sizes, ordering, and rationale.

## Corrective effect

- The ruling record pins `bee380de…3cab` as the accepted identity.
- The path in PR #532 remains the distinct amended `3ca25470…bac1` version.
- No fresh acceptance is inferred for `3ca25470…bac1`.
- The accepted ruling outcome—promote no candidates—remains recorded against
  its actual accepted bytes.
