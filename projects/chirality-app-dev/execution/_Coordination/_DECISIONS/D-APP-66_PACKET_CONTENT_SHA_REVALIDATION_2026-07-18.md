# D-APP-66 — Content-Change SHA Revalidation (DEL-07-04 status-transition surface)

**Status:** RULED — Option C (status quo), owner ruling 2026-07-19
transcribed in §Human Ruling

**Date prepared:** 2026-07-18

**Prepared by:** N8 packet-author child under sealed brief
`execution/_Coordination/AgentRuns/D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18/LAUNCH_BRIEF_PACKETS_T4.md`.
Packet preparation is agent work; the ruling is the owner's (K-AUTH-1).

## Context

**The gated item.** DEL-07-04 `_STATUS.md` line 10 carries the deferred item:
"Add content-change SHA revalidation to the status-transition surface (needs
its own decision packet before code)" — gated since D-APP-53 ruled Option A
only (2026-07-10) and reaffirmed open/unselectable by D-APP-56 R4-P46
(2026-07-12; `_STATUS.md` line 26). D-APP-65 disposition 5 authorized this
packet; it does not pre-authorize any code.

**The assessed gap.** `Assessment_INSP-03_DEL-07-04.md` (Gap Inventory, ~line
47): "Approval SHA binding is persisted but not automatically revalidated
against content changes" (Medium), anchored at
`frontend/src/lib/lifecycle/status-writer.ts:125-160`; REQ-014 is PARTIAL for
the same reason (assessment line 36): approval evidence is persisted, but
content-change voiding is a governance/checklist rule, not automatic
enforcement.

**What the live code actually does** (read 2026-07-18, live tree):

- Human-gated transitions (`CHECKING`, `ISSUED`;
  `frontend/src/lib/lifecycle/transition.ts:88-90`) require an `approvalSha`
  and validate **presence and format only**: pattern `/^[0-9a-f]{7,64}$/i`
  (`transition.ts:65`), with typed errors `APPROVAL_SHA_REQUIRED` and
  `INVALID_APPROVAL_SHA` (`transition.ts:92-118`; error-code union at
  `transition.ts:32-38`).
- The accepted SHA is persisted as status-document metadata — `Checking
  Approval SHA` on CHECKING, `Approval SHA` on ISSUED
  (`transition.ts:120-135`), written by `updateStatusDocument`
  (`frontend/src/lib/lifecycle/status-writer.ts:125-160`), which merges
  fields and rewrites the document without any verification step.
- `applyLifecycleTransition` is pure content-in/content-out
  (`transition.ts:137-195`); the only filesystem-aware entry is
  `transitionStatusFile` (`transition.ts:197-212`), reached by both the API
  route and the MCP `status_transition` tool through the single choke point
  `transitionDeliverableStatus`
  (`frontend/src/lib/workspace/deliverable-contracts.ts:364-386`), which
  knows the deliverable folder path (`deliverable-contracts.ts:374`).

**What the approval SHA references.** In recorded practice it is a git commit
SHA of the approved repository state (e.g., the owner-approved
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` recorded 2026-06-20 in DEL-07-04
`_STATUS.md` lines 5-7). The kit requires only a "7-64 char hex SHA-like
token" (`docs/PRD.md` FR-054 line 572; `docs/SPEC.md:222`; `docs/CONTRACT.md`
K-STATUS-2 line 100). The lifecycle runtime is git-free — no lifecycle module
shells out to git — so **the runtime cannot deterministically verify that a
supplied git SHA exists or that its commit contains the approved content**.
Any honest transition-time revalidation must therefore check something the
runtime can compute deterministically: the deliverable's governed content
itself.

## Options

### Option A — Transition-time revalidation via a recorded content-hash binding (draft-recommended)

Bind approval to content deterministically, and verify the binding before any
human-gated status write:

1. **New deterministic digest.** A new module
   (`frontend/src/lib/lifecycle/content-digest.ts`) computes a SHA-256
   digest over the deliverable folder's governed document set — sorted
   relative paths + file contents — excluding `_STATUS.md` itself (the
   transition mutates it), `_run_records/`, and `MEMORY.md`. The exact
   inclusion manifest is pinned in the module and in tests.
2. **Binding at CHECKING.** When a human-gated transition to `CHECKING`
   supplies an `approvalSha`, the digest is computed and persisted alongside
   it as a new metadata field (`Approved Content SHA-256`) through the
   existing metadata path (`transition.ts:120-135`,
   `status-writer.ts:52-81`).
3. **Revalidation at ISSUED.** On a transition to `ISSUED`, the digest is
   recomputed and compared to the persisted binding **before**
   `updateStatusDocument` is invoked (enforcement in the transition module,
   ahead of the `transition.ts:182` write path). Mismatch — or a missing
   binding — throws a new typed error code **`APPROVAL_SHA_STALE`** (added to
   the union at `transition.ts:32-38`); nothing is written. Fail-closed on a
   missing binding is safe today: all 53 deliverables are `IN_PROGRESS`
   (D-APP-54; D-APP-56 P50), so every future ISSUED is preceded by a
   binding-minting CHECKING.
4. **Wiring.** Digest computation lives at the filesystem-aware layer
   (`transitionStatusFile` / `transitionDeliverableStatus`, which already
   holds the deliverable path at `deliverable-contracts.ts:374`);
   `applyLifecycleTransition` stays pure by accepting the
   computed digest as an option. Both the API route and the MCP tool inherit
   the check through the shared choke point.
5. **Tests** in `frontend/src/__tests__/lib/lifecycle-status.test.ts`:
   (a) **match** — CHECKING mints the binding; ISSUED over unchanged content
   succeeds and preserves both SHA fields; (b) **stale** — a governed file
   edited between CHECKING and ISSUED yields `APPROVAL_SHA_STALE` and no
   status write; (c) **malformed/missing** — a tampered or absent
   `Approved Content SHA-256` field yields `APPROVAL_SHA_STALE`; existing
   `APPROVAL_SHA_REQUIRED` / `INVALID_APPROVAL_SHA` cases
   (`lifecycle-status.test.ts:205-252`) remain unchanged.

**Honest limits, stated plainly:** the git-commit SHA itself remains
format-validated evidence only. Whether that commit exists, or contains the
approved content, stays a governance/audit check (register + ruling records)
— the runtime does not gain git access under this option. What Option A does
verify deterministically is the actual voiding condition named by REQ-014:
that the governed content at the gated write is byte-identical to the content
that was approved.

- **Risks:** digest-manifest choice must be exact or the gate false-trips
  (e.g., `_run_records` churn); small metadata-surface growth in
  `_STATUS.md`.
- **Validation:** frontend typecheck + Vitest; new cases above.
- **Affected files:** `frontend/src/lib/lifecycle/transition.ts`,
  `frontend/src/lib/lifecycle/content-digest.ts` (new),
  `frontend/src/lib/workspace/deliverable-contracts.ts`,
  `frontend/src/__tests__/lib/lifecycle-status.test.ts`.

### Option B — Consumption-time warning only (no transition blocking)

No transition-path change. The status **read** surfaces (status API route and
MCP status read tool) recompute the content digest and annotate the returned
snapshot with a staleness flag (e.g., `approvalContentStale: true`) when a
persisted binding mismatches. Human-gated writes still succeed on stale
approvals; the warning relies on a human noticing it. Smaller surface, but it
leaves REQ-014 PARTIAL: voiding remains advisory, and the D-APP-53-era
checklist posture effectively continues with better instrumentation.

### Option C — Keep as governance checklist; no code (status quo)

The INSP-03 recommendation as written ("Keep as governance checklist unless a
future accepted design adds content-hash validation",
`Assessment_INSP-03_DEL-07-04.md` ~line 47). The deferred item is discharged
by recording that content-change voiding is intentionally procedural. Zero
code risk; the gap survives to issuance time, where F-APP-4 already puts the
owner at every gate.

## Recommended option and rationale

**Option A.** It is the only option that closes the REQ-014 gap with a
deterministic check at the moment that matters (the gated write), it is
honest about what a git-free runtime can and cannot verify, and it is
consistent with the snapshot rule (later phases consume accepted snapshots,
not mutable working state). The surface is small and single-choke-point
(`transitionDeliverableStatus`), and the accepted D-APP-65 basis already
graded this "cheap determinism win, medium priority" (D-APP-65 packet §2,
recommendation 6).

**No code lands unless and until the owner rules for it.** A declined or
deferred ruling leaves this packet AWAITING_RULING and DEL-07-04's
`_STATUS.md` line 10 gate intact.

## Human Ruling and Disposition

Transcription note: the owner's ruling below is chat evidence (the session's
structured-question interface), transcribed verbatim; this packet is one of
its two governed homes (the other is the D-APP-67 packet — the two rulings
were delivered as one block and the full block is transcribed in each, with
the same canonical hash). The prompts and option descriptions are
agent-drafted; the selections are the owner's acts (K-AUTH-1).

<!-- BEGIN OWNER RULING VERBATIM -->
On 2026-07-19, the agent presented both AWAITING_RULING packets' options to the owner through the session's structured-question interface; the prompts and option descriptions are agent-drafted, the selections are the owner's acts:

Question 1 (D-APP-66): "D-APP-66 (DEL-07-04 content-change SHA revalidation): how should the approval-SHA surface treat content changes after a human approval? Today validation is presence + hex-format only; nothing detects that governed content changed after the approval was recorded."
Owner selection: "C: Status quo" — keep content-change voiding as a governance checklist item; no code. The gap survives to issuance, where the owner is at every gate anyway (F-APP-4).

Question 2 (D-APP-67): "D-APP-67 (DEL-05-03 secret-registry redaction taxonomy): how far should the redaction contract broaden beyond configured API keys? Context: the pec agent password is currently protected only by envelope construction, and the fixture-marker boundary tripped four verifier returns on 2026-07-18 because it was unwritten convention."
Owner selection: "B: Taxonomy doc only" — ratify the committed-file rules + verifier-quoting rule (which is where all four trips happened) but keep the runtime helper API-key-specific. Zero runtime risk; the pec password stays protected only by envelope construction.
<!-- END OWNER RULING VERBATIM -->

**Canonical ruling-text SHA-256:**
`766058c8a5831859df867519ed3a19c3a5d91f00b16318401150322a4d134955`
(1332 bytes; UTF-8 text between the verbatim markers, excluding the marker
lines and delimiter newlines; computed by the executing instance from this
packet's marker span after writing and recomputed to confirm — same value
recorded in the D-APP-67 packet's identical span)

**Disposition (Option C, this packet's part of the block):** no code is
authorized. Content-change voiding of a recorded approval SHA remains a
governance/checklist concern, enforced procedurally at the human gates
rather than deterministically at the transition write; the REQ-014 PARTIAL
posture and the INSP-03 recommendation-as-written stand. The DEL-07-04
`_STATUS.md` line-10 deferred item is discharged by this ruling (its
required decision packet now exists and is ruled). The Option A design above
is preserved in this packet as reference should a future owner ruling
revisit transition-time revalidation; nothing in this ruling pre-authorizes
it. No lifecycle transition, no `Checking Approval SHA` change, no fence
contact (F-APP-1..5).

## On-ruling mechanics (planned)

1. Transcribe the owner's ruling verbatim into this packet between markers,
   with the canonical ruling-text SHA-256 (D-APP-63 convention); flip the
   `_REGISTER.md` row to RULED (ruled rows above untouched).
2. If ruled for code (Option A or B): implement exactly the ruled option in
   the same program under the normal gates (typecheck, Vitest, secret-scan);
   discharge the DEL-07-04 `_STATUS.md` Remaining item with a dated History
   line citing D-APP-66 (no lifecycle transition; `Checking Approval SHA`
   untouched); record a dated run record under the deliverable's
   `_run_records/`.
3. If ruled Option C: discharge the Remaining item with a dated History line
   recording the procedural-voiding decision; no code.
4. If declined/deferred: no writes beyond the transcription; the packet
   stays AWAITING_RULING and the deliverable gate stands.
5. No fence contact under any ruling (F-APP-1..5): no issuance, no release
   posture, no domain-engine surface.
