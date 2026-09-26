---
amendment: SCA-006
doc_kind: scope_change.prd_successor_diff
status: candidate_awaiting_checkpoint_2
prepared: 2026-09-25
prepared_by: TASK child T1 under WORKING_ITEMS brief B5, HELP_HUMAN undertaking HELP-HUMAN-PEC-20260925-POST-SCA005 (work-graph node R2)
candidate: CP2_CANDIDATE/docs/PRD.md
preimage: projects/pec/docs/PRD.md (v2.3)
preimage_sha256: fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32
candidate_sha256: ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe
---

# PRD v2.4 successor candidate — section-by-section diff against live v2.3

This is the checkpoint-2 PRD candidate for SCA-006. It applies nothing. Live
`projects/pec/docs/PRD.md` stays v2.3 at the preimage hash above until the
owner accepts checkpoint group 2 and a separately authorized application
writes the candidate bytes. The candidate implements exactly intake actions
Seq 1–13 (the K group) of the accepted `Amendment_Actions.csv`, using the
shared canon's PRD texts. Every other v2.3 byte is unchanged (§8 proves it).

## 1. Identities

| Artifact | Path | Lines | SHA-256 |
|---|---|---|---|
| Preimage (live PRD v2.3) | `projects/pec/docs/PRD.md` | 597 | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| Successor candidate (this package) | `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/docs/PRD.md` | 654 | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |

The candidate hash is recorded here because it cannot appear inside the
candidate. It is computed with every acceptance-bound slot at its default
value (§6). A changed slot changes this hash, and the applied file's hash is
re-measured at the owner's act.

## 2. Basis

Every hash below was recomputed before drafting and matched the brief.

| Basis | Path | SHA-256 |
|---|---|---|
| Live PRD v2.3 (preimage) | `projects/pec/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| Accepted Impact Assessment (Annex B loci; §8.1, §9.3, §9.4) | `_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md` | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` |
| Accepted intake, Seq 1–13 | `_ScopeChange/SCA-006_2026-09-25_1912/Amendment_Actions.csv` | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` |
| `D-PEC-90` ruling | `_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md` | `43a0c663c1a57a95001f0470cabb0d36bab098754867ecfe6c30127e7de5efab` |
| `D-PEC-90` proposal | `_Coordination/_DECISIONS/D-PEC-90_agent_reliance_on_pec_data_proposal_2026-09-25.md` | `b04a8aa25c1d402fb03f6f15b6fb1eb27a0110e5cd3f3ded1db3717649a5e147` |
| `D-PEC-91` ruling (budget carry-forward) | `_Coordination/_DECISIONS/D-PEC-91_RULING_2026-09-25.md` | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| Group-1 decision snapshot | `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md` | `0160dd881c0501e95c7245b71ffccffc332240573bb96a31196ed492c67250df` |
| Shared drafting canon, §1, §2 and §5 (manager-owned, B5 scratch; not a repository file) | `CANON.md` in the B5 run scratchpad | `5617eb1c0ead3cfb04246945fc033b3e5c0744b7d091ac2d47affae4cb0e67d0` |

Paths other than the PRD's are relative to `projects/pec/execution/`. The
group-1 act recorded in that snapshot selects DQ-a, ENV-a, BUD-a, GATE-a and
INS-a, and excludes R-C. GATE-a also keeps the §12 P1 row text unedited.
Checkpoint-2 candidate bindings that concern this file are SB-1 (PEC-K-03,
H-05), SB-2 (§8 Agents, H-07), SB-3 (§8 access classes, H-08), SB-5
(PEC-ORI-007, PEC-API-006, PEC-API-007 and the gate, H-09–H-11 and H-14;
supplementary extension) and SB-6 (§15 K-03 byte-identity claim, H-16)
(Impact Assessment §9.3). This document does not write
`Supersession_Delta.csv`. The form follows the SCA-005 precedent
`_ScopeChange/SCA-005_2026-09-23_2139/PRD_V2_3_SUCCESSOR_DIFF.md`.

## 3. Hunks in PRD order

Each hunk shows v2.3 (`-`) against the candidate (`+`). The `@@` header gives
the v2.3 start line and count, then the candidate start line and count. A hunk
is one locus. Its provenance label is the one the candidate's own v2.4 block
assigns (candidate L67–77). The header hunks H-01–H-03 carry no label in that
block, so they are marked "header". Application order is document order. An
empty line inside a block is a blank context line; it is written without the
leading space so this file carries no trailing whitespace. §8 proves that
applying these 17 blocks to the preimage yields the candidate byte for byte.
A plain `diff -u` merges them into 13 context hunks.

### Header table

#### H-01 — Header table: Version and Status rows (Date row is an unchanged slot)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 13 | 5–7 | 5–7 | header — acceptance record (Seq 13; not itself labelled in the v2.4 block) |

```diff
@@ -5,3 +5,3 @@
-| **Version** | 2.3 |
+| **Version** | 2.4 |
 | **Date** | 2026-09-25 |
-| **Status** | **Adopted 2026-09-25** by owner acceptance of SCA-005 checkpoint group 2 (`execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/`); v2.0 adopted by `D-PEC-58`; directed-bootstrap clarification adopted as v2.1 by `D-PEC-61`; exact PEC-K-03/-11 rows adopted by `D-PEC-67`; consumer-interface concordance adopted as v2.2 by `D-PEC-68`; §16.3 loop-registry disposition concordance adopted as exact v2.3 candidate bytes by `D-PEC-79` (not separately applied; carried into this successor); SCA-005 feed-model, presence and runtime-topology concordance adopted with this successor; product definition of record |
+| **Status** | **Adopted 2026-09-25** by owner acceptance of SCA-006 checkpoint group 2 (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`); v2.0 adopted by `D-PEC-58`; directed-bootstrap clarification adopted as v2.1 by `D-PEC-61`; exact PEC-K-03/-11 rows adopted by `D-PEC-67`; consumer-interface concordance adopted as v2.2 by `D-PEC-68`; §16.3 loop-registry disposition concordance adopted as exact v2.3 candidate bytes by `D-PEC-79` (not separately applied; carried into the v2.3 successor); v2.3 successor adopted by owner acceptance of SCA-005 checkpoint group 2; SCA-005 feed-model, presence and runtime-topology concordance adopted with that successor; `D-PEC-90` operational reliance on PEC data carried into this successor; product definition of record |
```

### Epistemic status

#### H-02 — Epistemic-status paragraph

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 13 | 17–20 | 17–25 | header — acceptance record (Seq 13; not itself labelled in the v2.4 block) |

```diff
@@ -17,4 +17,9 @@
-> exact bytes on 2026-08-09 (`D-PEC-79`) but not applied; this successor
+> exact bytes on 2026-08-09 (`D-PEC-79`) but not applied; the successor
 > v2.3 carries those changes and was adopted on 2026-09-25 by owner
 > acceptance of SCA-005 checkpoint group 2, which also reconciles the feed,
-> presence and runtime-topology premises to current file truth. Adoption
+> presence and runtime-topology premises to current file truth. v2.4 was
+> adopted on 2026-09-25 by owner acceptance of SCA-006 checkpoint group 2
+> under `D-PEC-90` R-A; it writes operational reliance on PEC data into
+> the product definition without changing authority, and operational
+> reliance begins only at a release that passes the §12
+> reliance-advertisement gate. Adoption
```

### Provenance labels

#### H-03 — New v2.4 successor provenance-label block after the SCA-005 block

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 13 | 60–60 | 65–77 | header — provenance record (Seq 13); this block assigns the labels in this column |

```diff
@@ -60,1 +65,13 @@
 > source, configuration, consumer, lifecycle, or release authority.
+
+> **v2.4 successor provenance labels (SCA-006):** In this block `PROPOSED`
+> means product text adopted through the SCA-006 checkpoint-group-2 owner
+> gate. PEC-K-03, the §8 Agents bullet and access-class sentence,
+> PEC-ORI-007, PEC-API-006, PEC-API-007 and the §12 reliance-advertisement
+> gate are `PROPOSED` (substance selected at SCA-006 checkpoint 1 under
+> `D-PEC-90` R-A and the owner's direct-query answer); §1.1, the §8
+> Harnesses sentence, §11 metric 4, the §12 P3 row and closing paragraph,
+> §15 and §16.6 are `CLARIFIED`. Earlier label blocks stay as history. None
+> of the changes creates an implementation mandate, a receiving-loop duty,
+> or a source, configuration, consumer, lifecycle, release or authority
+> grant.
```

### §1.1 Thesis

#### H-04 — §1.1 Thesis, availability sentence

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 4 | 74–75 | 91–93 | CLARIFIED |

```diff
@@ -74,2 +91,3 @@
 It is available to explicitly PEC-enabled consumers, including harnesses
-acting on behalf of agents, and to the human owner through dashboards. It is
+acting on behalf of agents and agents querying directly through tool calls,
+and to the human owner through dashboards. It is
```

### §6 Product invariants

#### H-05 — §6 PEC-K-03 row (whole cell text)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 1 | 212–212 | 230–230 | PROPOSED |

```diff
@@ -212,1 +230,1 @@
-| **PEC-K-03** | **Pull-oriented interface; consumer-owned use.** PEC provides labeled, non-authoritative orientation data on request and never self-polls, schedules a consumer, injects into an agent, or claims an external cadence. An explicitly PEC-enabled consumer decides under its own authority whether and when to consume. If it injects PEC data, verify-before-rely is an interface precondition; injection is not required. |
+| **PEC-K-03** | **Pull-oriented interface; consumer-owned use.** PEC provides labeled, non-authoritative orientation data on request and never self-polls, schedules a consumer, injects into an agent, or claims an external cadence. An explicitly PEC-enabled consumer decides under its own authority whether and when to consume; injection is not required. Non-authoritative means never citable as authority (PEC-K-02). Within the pin, coverage and trust tier that a response declares (PEC-ORI-007), a consumer, or an agent acting through one or through the tool-call surface (PEC-API-007), may take a record-tier claim as true as of its examined-through SHA and act on it without re-reading the cited source (operational reliance); wherever PEC is absent, degraded, failing its own checks or stating a limitation, it falls back to the files (PEC-K-01). Operational reliance is available only from a PEC release that has passed the §12 reliance-advertisement gate. |
```

### §8 Users and access

#### H-06 — §8 Harnesses bullet (sentence appended)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 2 | 278–278 | 296–297 | CLARIFIED |

```diff
@@ -278,1 +296,2 @@
-  deferred, PEC-STR-003).
+  deferred, PEC-STR-003). A harness is one enabled path to PEC data, not the
+  only one.
```

#### H-07 — §8 Agents bullet (text replaced)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 2 | 279–282 | 298–306 | PROPOSED |

```diff
@@ -279,4 +298,9 @@
-- **Agents** — never call PEC directly by instruction under the current access
-  classes. They may receive orientation as labeled, non-authoritative data
-  only if an explicitly enabled consumer chooses to inject it; injection is
-  not required (PEC-K-03).
+- **Agents** — may act on PEC data received through an explicitly enabled
+  consumer, and may query PEC directly through tool calls under the
+  read-only `agent` access class (PEC-API-007) where that surface is
+  enabled. Either way they act on labeled, non-authoritative data under
+  operational reliance within the declared envelope (PEC-K-03,
+  PEC-ORI-007), never as authority (PEC-K-02), and only from a release that
+  has passed the §12 reliance-advertisement gate. Enabling any path is
+  consumer-owned; injection is not required, and no agent, harness or loop
+  is required to query PEC (PEC-K-01, PEC-K-11).
```

#### H-08 — §8 access sentence (four access classes)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 3 | 285–286 | 309–315 | PROPOSED |

```diff
@@ -285,2 +309,7 @@
   the prototype's implemented 14-role RBAC set (`core/src/types.ts`) are
-  retired; access classes are owner, harness, and admin.
+  retired; access classes are owner, harness, agent, and admin. The `agent`
+  class is read-only query access for tool calls: orientation, deltas, gate
+  verdicts, decision-slate and presence reads, with no event ingest, no
+  presence reports and no admin act. Every class is local-only and
+  token-scoped; the token mechanism, including credentials for the `agent`
+  class, is the open §16.6 decision.
```

### §9.1 Orientation (PEC-ORI)

#### H-09 — §9.1 new row PEC-ORI-007 after PEC-ORI-006

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 5 | 301–301 | 330–331 | PROPOSED |

```diff
@@ -301,1 +330,2 @@
 | PEC-ORI-006 | Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited. |
+| PEC-ORI-007 | Every orientation response shall declare the operational reliance it supports (its reliance envelope): its pin (examined-through SHA); per-feed coverage and freshness with any stated limitation (PEC-ORI-006); the trust tier of each claim, where only record-tier claims support correctness decisions and presence-tier facts are advisory at their stated heartbeat age (PEC-K-05); and a file-fallback signal whenever PEC is absent, degraded or failing its own checks. No consumer may treat silence as a claim. |
```

### §9.6 API (PEC-API)

#### H-10 — §9.6 new row PEC-API-006 after PEC-API-005

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 6 | 353–353 | 383–384 | PROPOSED |

```diff
@@ -353,1 +383,2 @@
 | PEC-API-005 | PEC shall offer an SSE subscription for deltas and presence changes (dashboards; long-running managers). |
+| PEC-API-006 | Responses shall be bounded by declared size budgets suited to agent consumers and met by pagination or continuation. A budget is never met by dropping citations, stamps or stated limitations, and any truncation is stated in the response, never silent. Numeric budgets are confirmed at Phase 1. |
```

#### H-11 — §9.6 new row PEC-API-007 after PEC-API-006 (anchored on the following v2.3 lines)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 7 | 354–355 | 385–387 | PROPOSED |

```diff
@@ -354,2 +385,3 @@
+| PEC-API-007 | PEC shall offer a read-only query interface packaged for agent tool calls, over the same versioned API and responses (PEC-API-003, PEC-API-004, PEC-API-006, PEC-ORI-007), under the `agent` access class. Enabling it in any harness, App or agent configuration is consumer-owned (PEC-K-03, PEC-K-11); PEC never injects or schedules. Before any such tool is declared or invoked, the PEC Domain Engine Profile (`_DomainEngines/profiles/pec.yaml`) is amended under its own tier-0 act. P3 capability. |

 ### 9.7 Dashboards (PEC-DSH)
```

### §11 Success metrics

#### H-12 — §11 metric 4, candidate-consumer sentence

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 10 | 395–396 | 427–429 | CLARIFIED |

```diff
@@ -395,2 +427,3 @@
-   loop. Candidate consumers are registered loops or harnesses for which PEC
-   exposes a compatible interface; membership asserts no duty.
+   loop. Candidate consumers are registered loops, harnesses, or enabled
+   agent tool-call surfaces for which PEC exposes a compatible interface;
+   membership asserts no duty.
```

### §12 Release strategy

#### H-13 — §12 table, P3 row Scope cell

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 9 | 415–415 | 448–448 | CLARIFIED |

```diff
@@ -415,1 +448,1 @@
-| **P3 — Opt-in consumer integration** | PEC-side interfaces/adapters usable by hooks CLI or daemon consumers; presence registry + Git/worktree scanner; live use requires a separately authorized receiving consumer | Capability contract tests pass; consumer enablement/use is measured without external conformance; overlap warnings fire on seeded conflicts; falsification clause armed |
+| **P3 — Opt-in consumer integration** | PEC-side interfaces/adapters usable by hooks CLI or application-owned Runtime service consumers, and the agent tool-call query surface (PEC-API-007); presence registry + Git/worktree scanner; live use requires a separately authorized receiving consumer | Capability contract tests pass; consumer enablement/use is measured without external conformance; overlap warnings fire on seeded conflicts; falsification clause armed |
```

#### H-14 — §12 standing reliance-advertisement gate paragraph (after the table; P1 row not edited)

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 8 | 417–418 | 450–463 | PROPOSED |

```diff
@@ -417,2 +450,14 @@

+**Standing reliance-advertisement gate.** No PEC release advertises
+operational reliance on PEC data (PEC-K-03) until its gates prove, for the
+scope it serves: parity with the practitioner harness clean, or each
+difference explained by a recorded DriftFinding disposition (PEC-RCN-005);
+complete coverage statements under seeded unparseable and stale feeds
+(PEC-ORI-006); the reliance envelope on every response (PEC-ORI-007);
+passing parser fixture suites; and the kill test (PEC-K-01). The gate is
+re-proved at each release that advertises operational reliance. A release
+that has not passed it advertises none, and consumers keep reading the
+files. The gate creates no consumer duty and does not change the phase exit
+tests above.
+
 The PEC v2 build itself runs through the governed pipeline (SOFTWARE_DECOMP →
```

#### H-15 — §12 closing paragraph, authorization sentence

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 9 | 437–438 | 482–483 | CLARIFIED |

```diff
@@ -437,2 +482,2 @@
-consumers. They do not themselves authorize Root, App, a harness, or another
-loop to poll, push, inject, subscribe, or consume.
+consumers. They do not themselves authorize Root, App, a harness, an agent's
+tool host, or another loop to poll, push, inject, subscribe, or consume.
```

### §15 Governance and compliance posture

#### H-16 — §15 D-PEC-67 bullet replaced; new D-PEC-90 bullet

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 11 | 513–516 | 558–572 | CLARIFIED |

```diff
@@ -513,4 +558,15 @@
-- **`D-PEC-67` — exact consumer-interface rows preserved.** PEC-K-03 and
-  PEC-K-11 remain byte-identical to the rows adopted by D-PEC-67. Surrounding
-  v2.2 prose makes their optional, consumer-owned use coherent across the
-  PRD; it creates no receiving-loop duty or implementation authority.
+- **`D-PEC-67` — exact consumer-interface rows.** PEC-K-11 remains
+  byte-identical to the row adopted by D-PEC-67. PEC-K-03 is amended under
+  `D-PEC-90` R-A through SCA-006; the D-PEC-67 K03-A bytes are preserved as
+  historical exact input, and the amended row keeps pull-oriented,
+  consumer-owned use. Surrounding prose makes their optional, consumer-owned
+  use coherent across the PRD; it creates no receiving-loop duty or
+  implementation authority.
+- **`D-PEC-90` — operational reliance is not authority.** PEC-K-03,
+  PEC-ORI-007 and the §12 reliance-advertisement gate let a consumer act on a
+  record-tier claim within its declared bounds. No governed record cites
+  PEC; no ruling, acceptance, lifecycle transition or merge rests on PEC
+  output; deleting PEC still blocks nothing. `D-GOV-01` Option A, Root PRD
+  N-1 and K-AUTH-1 are therefore complied with unchanged, and PEC output
+  stays never citable as authority (the `D-PEC-90` R-C option was not
+  selected).
```

### §16 Product decisions (owner)

#### H-17 — §16 item 6, last sentence

| Intake Seq | v2.3 lines | Candidate lines | Provenance label |
|---|---|---|---|
| 12 | 567–567 | 623–624 | CLARIFIED |

```diff
@@ -567,1 +623,2 @@
-   decision on PEC's own token mechanism stays open.
+   decision on PEC's own token mechanism stays open; it includes the
+   credentials of the `agent` access class for tool-call query (PEC-API-007).
```

### 3.1 Fittings made to canonical texts

The canon permits changes to line wrapping, table-cell syntax and surrounding
grammar. Every such change is listed here. No canonical text needed a change
of meaning, so no locus was stopped. The manager accepted F-01 to F-03 as
fittings. The manager then directed two revisions, F-16 and F-17. It gave them
in its message to T1 of 2026-09-25, under brief B5. `check_canon.py` (§8)
normalizes whitespace and blockquote markers, then confirms these texts occur
in the candidate:
- each verbatim canonical text: C-K03, C-S8-HARNESS, C-S8-ACCESS, C-S1.1,
  C-ORI-007, C-API-006, C-API-007, C-S12-GATE, C-S12-P3 (both parts),
  C-S11-M4, C-S15 (both bullets) and C-S16.6;
- C-S8-AGENTS, with the F-16 insertion as its only difference;
- the F-17 definition sentence.

| # | Hunk | Canon | Fitting | Why it keeps the meaning |
|---|---|---|---|---|
| F-01 | H-01 | C-HEADER | Status row realized from the canon's description. The lead is verbatim. Every v2.3 lineage item is kept in its order. "v2.3 successor adopted by owner acceptance of SCA-005 checkpoint group 2" is placed after the `D-PEC-79` item, and "`D-PEC-90` operational reliance on PEC data carried into this successor" is placed last, before "product definition of record". | canon lists the items and their places; the order follows the chain. Accepted by the manager |
| F-02 | H-01 | C-HEADER | In pre-existing lineage items: `D-PEC-79` "(not separately applied; carried into this successor)" -> "… carried into the v2.3 successor)"; SCA-005 item "adopted with this successor" -> "adopted with that successor". | In v2.4, "this successor" denotes v2.4. Unchanged, the row would say the SCA-005 concordance was adopted with v2.4. It touches existing words inside the Seq 13 locus (L7). Accepted by the manager |
| F-03 | H-02 | C-HEADER | In the pre-existing epistemic sentence: "this successor v2.3 carries" -> "the successor v2.3 carries". | Same reason as F-02, inside the Seq 13 locus L11–23. Accepted by the manager |
| F-04 | H-02 | C-HEADER | Canon sentence used word for word ("v2.4 was adopted on 2026-09-25 … passes the §12 reliance-advertisement gate."), inserted after the SCA-005 sentence and before "Adoption makes a PRD …". Only the insertion lines are rewrapped; the existing short line "document is an implementation" is kept. | insertion only |
| F-05 | H-03 | C-HEADER | Canon block content rendered as a `>` blockquote with a bold lead, as the earlier label blocks are. Its canon words are verbatim, including "Earlier label blocks stay as history." and "None of the changes creates …". The block is rewrapped around the F-17 sentence. | layout only |
| F-06 | H-04 | C-S1.1 | Rewrapped at the insertion point; v2.3 L76 onward unchanged, so candidate L93 is a short line. | wrapping only |
| F-07 | H-06 | C-S8-HARNESS | Appended to the bullet's last line and wrapped with its two-space indent. | wrapping only |
| F-08 | H-07 | C-S8-AGENTS | `> **Agents** — …` rendered as the list item `- **Agents** — …` with two-space continuation indent. | layout only |
| F-09 | H-08 | C-S8-ACCESS | The canon's leading "..." is realized as the unchanged v2.3 text before "access classes are"; wrapped with the bullet's indent. | canon instruction |
| F-10 | H-12 | C-S11-M4 | Wrapped with the list's three-space indent; the rest of metric 4 and the falsification clause are unchanged. | wrapping only |
| F-11 | H-13 | C-S12-P3 | Canon text placed as the P3 Scope cell; the Phase and Exit-test cells are unchanged. | table-cell syntax |
| F-12 | H-14 | C-S12-GATE | Blockquote rendered as a body paragraph immediately after the §12 table (after its trailing blank line), followed by a blank line before "The PEC v2 build itself …". | layout only |
| F-13 | H-15 | C-S12-P3 | Closing sentence rewrapped over the same two lines. | wrapping only |
| F-14 | H-16 | C-S15 | Both blockquote bullets rendered as `-` list items with two-space continuation indent. | layout only |
| F-15 | H-17 | C-S16.6 | The canon sentence replaces the v2.3 last sentence; its first word "The" stays at the end of the unchanged v2.3 L566; wrapped with the item's three-space indent. | wrapping only |
| F-16 | H-07 | C-S8-AGENTS | **Manager-directed** (canon §1 rule "keep 'non-authoritative'"). The second sentence becomes "Either way they act on labeled, non-authoritative data under operational reliance within the declared envelope (PEC-K-03, PEC-ORI-007), never as authority (PEC-K-02), and only from a release that has passed the §12 reliance-advertisement gate." The rest of the bullet is unchanged from the canon text; the bullet is rewrapped (8 -> 9 lines). | Carries v2.3 L280's "labeled, non-authoritative data" in the authority sense, which the canon's §1 rule requires. Adds no selection and drops no limit |
| F-17 | H-03 | C-HEADER | **Manager-directed** (resolves §5 R-01). The v2.4 block's first sentence is now "In this block `PROPOSED` means product text adopted through the SCA-006 checkpoint-group-2 owner gate." It sits where the SCA-005 block puts its equivalent sentence, after the lead and before the label lists. No earlier label block is edited. | States which gate the block's `PROPOSED` label refers to, as each earlier block does |

H-05 (PEC-K-03), H-09 (PEC-ORI-007), H-10 (PEC-API-006) and H-11
(PEC-API-007) use the canon text byte for byte, with no fitting.

## 4. Invariants that stand

The evidence is from `evidence.py` (§8), which compares exact lines of the two
files. "L" numbers are v2.3 -> candidate.

| Invariant | Evidence | Holds |
|---|---|---|
| PEC-K-01 graceful absence | Row byte-identical, L210 -> L228. The kill test stays in PEC-SVC-004 (unchanged) and in the new gate (H-14). K-03 names the file fallback (PEC-K-01). | yes |
| PEC-K-02 files govern | Row byte-identical, L211 -> L229. K-03 now says "Non-authoritative means never citable as authority (PEC-K-02)". | yes |
| PEC-K-11 byte-identical | Row byte-identical, L220 -> L238 (single occurrence in each file). K-04..K-10 are also byte-identical; only K-03 changes (H-05). | yes |
| K-AUTH-1 | v2.3 L162 (§4.2 "Rulings are file-native (K-AUTH-1)") and L321 (PEC-GAT-004) unchanged at L180 and L351. The new §15 `D-PEC-90` bullet (L570) states that K-AUTH-1 is complied with unchanged. | yes |
| `D-GOV-01` | §15 `D-GOV-01` bullet byte-identical, L488–499 -> L533–544. §2 L102 -> L120 and §4.2 L160 -> L178 unchanged. The new bullet (L569) states that Option A is complied with unchanged. | yes |
| Root PRD N-1 | Not named in v2.3. Named only at L569–570, as complied with unchanged. No new text makes PEC output an authority source or cites it from a governed record. | yes |
| "non-authoritative" in the authority sense | v2.3 has it at L212, L245, L280, L496 and L505. The candidate has it at L230, L263, L301, L541 and L550. L245, L496 and L505 are unchanged (L263, L541, L550). The K-03 cell (L230) keeps "labeled, non-authoritative orientation data" and now defines the term. The §8 Agents bullet (L301) carries "labeled, non-authoritative data", as it did at v2.3 L280, next to "never as authority (PEC-K-02)". This is the manager-directed fitting F-16, and it resolves the earlier tension between the canon's §1 rule and C-S8-AGENTS. | yes |
| Pull-oriented, consumer-owned use | K-03 keeps its lead and "never self-polls, schedules a consumer, injects into an agent, or claims an external cadence" (L230). "injection is not required" appears at L230 and L305. The §8 Agents bullet says "Enabling any path is consumer-owned" and "no agent, harness or loop is required to query PEC". PEC-API-007 says "PEC never injects or schedules". §5 L195–197 -> L213–215 and PEC-API-002's "pull path" (L350 -> L380) are unchanged. The §12 closing sentence adds "an agent's tool host" to the parties it does not authorize (L482–483). | yes |
| No operational reliance before the §12 gate | Every candidate occurrence of "operational reliance": L7 (Status lineage), L22–25 (epistemic; "begins only at a release that passes the §12 reliance-advertisement gate"), L230 (K-03; "available only from a PEC release that has passed the §12 reliance-advertisement gate"), L302–304 (§8 Agents; "only from a release that has passed the §12 reliance-advertisement gate"), L331 (PEC-ORI-007: a requirement on response content, which grants no availability), L451–458 (the gate itself) and L565–566 (§15; names the gate). The v2.4 label block (L70) names the gate only as a label target. The added lines contain 0 unqualified "reliance" or "rely" (every use is "operational reliance", "reliance envelope" or "reliance-advertisement"). The §12 P1 row is byte-identical (L413 -> L446), as GATE-a requires. | yes |
| §16 decisions stay open | §16.6 stays open ("stays open; it includes …", L623–624). "None of the remaining open decisions blocks P0–P2." is unchanged (L585 -> L642). PEC-API-007, which needs the agent credentials, is a P3 capability. | yes |

## 5. Residual text

These candidate loci still read against the K-group changes, or sit next to
them. R-01 is resolved by the manager-directed sentence F-17. T1 did not edit
the text of R-02 to R-08. R-02 and R-03 are inside a Seq 13 locus or its
"history" clause. R-04 to R-08 are outside every accepted action.

| # | Candidate line(s) | Text | Tension | Arguably covered by an accepted action? |
|---|---|---|---|---|
| R-01 | 50–51 (SCA-005 label block; unedited) | "In this successor `PROPOSED` means product text adopted through the SCA-005 checkpoint-group-2 owner gate." | In v2.4, "this successor" could read as v2.4. | **Resolved** by F-17. The v2.4 block (L67–77) now opens "In this block `PROPOSED` means product text adopted through the SCA-006 checkpoint-group-2 owner gate". The SCA-005 block stays as history, unedited. |
| R-02 | 34–36 (v2.2 label block) | "The PEC-K-03 and PEC-K-11 rows are `TRANSCRIBED` byte-for-byte from the PRD bytes adopted by `D-PEC-67`" | No longer true of the current K-03 row. | Yes, as history: Seq 13 keeps the earlier label blocks as history, and H-03 and H-16 state the K-03 change. |
| R-03 | 7 (Status row) | "exact PEC-K-03/-11 rows adopted by `D-PEC-67`" | This lineage item predates the K-03 amendment. It is true as history, and the same row now names `D-PEC-90`. | Yes (Seq 13 keeps every earlier lineage item). |
| R-04 | 445 (§12 P0 row) | "PRD lineage ruled through `D-PEC-58`, `D-PEC-61`, `D-PEC-67`, and `D-PEC-68`" | Omits the `D-PEC-79`, SCA-005 and SCA-006 adoptions. This predates SCA-006; SCA-005 left it too. | No. It is P0 phase history; a later PRD change could decide it. Stays residual, unedited |
| R-05 | 498 (§13 domain-engine row) | "profile superseded when v2 has shape" | New PEC-API-007 (L385) requires a tier-0 amendment of `_DomainEngines/profiles/pec.yaml` before any tool. `D-T0-27` O-A already adopted the PEC v2 successor profile (`projects/pec/AGENTS.md`), so the row is stale. It was already listed as residual by the SCA-005 diff §8. | No. Stays residual, unedited |
| R-06 | 349 (PEC-GAT-002) | "Gate verdicts … advisory only." | The `agent` class reads gate verdicts, and agents act on them under operational reliance. Impact Assessment §8.1 finds no conflict: acting on a verdict is operational, and the governed gate is decided from the files. Listed for completeness. | Not needed (IA §8.1: "No action is proposed"). |
| R-07 | 446 (§12 P1 exit test) | "Parity-diff vs harness clean or explained" | The gate (L451–461) requires each difference to be explained by a recorded DriftFinding disposition, which is stricter. This is intended: GATE-a keeps the P1 row, and the gate says it "does not change the phase exit tests above". | Not needed (GATE-a). |
| R-08 | 291–297 (§8 Harnesses bullet), 273 (§7.2 Session), 357 (PEC-PRS-001) | Harnesses are "permitted machine consumers of the API on behalf of agent sessions"; presence comes only from a hooks consumer. | Read against the new `agent` class (presence reads only; no presence reports), these stay consistent, and the appended harness sentence removes the exclusivity reading. Listed as checked. | Not needed. |

No other candidate text says that agents never call PEC directly, requires
verify-before-rely, lists only three access classes, or names daemon
consumers in the P3 row (`check_canon.py` absence checks). The §14 family
list stays correct (§7).

## 6. Acceptance-bound slots and hash rule

These tokens are bound to the owner's act. They take the actual values at that
act, and no other byte may change at acceptance. The candidate hash in §1 is
computed with every slot at its default value (CANON.md §5): dates
`2026-09-25` and the group-2 folder token `SCA-006_GROUP-2_2026-09-25`.

| # | File | Candidate line (locus) | Token (default) | Binds to |
|---|---|---|---|---|
| S1 | `CP2_CANDIDATE/docs/PRD.md` | 6 (Date row) | `2026-09-25` | date of the owner's checkpoint-group-2 acceptance |
| S2 | `CP2_CANDIDATE/docs/PRD.md` | 7 (Status row) | `2026-09-25` in "**Adopted 2026-09-25**" | same date |
| S3 | `CP2_CANDIDATE/docs/PRD.md` | 7 (Status row) | `SCA-006_GROUP-2_2026-09-25` in `execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/` | the actual group-2 snapshot folder name (its date token follows S1) |
| S4 | `CP2_CANDIDATE/docs/PRD.md` | 21 (epistemic paragraph) | `2026-09-25` in "v2.4 was adopted on 2026-09-25" (line text "> adopted on 2026-09-25 by owner acceptance of SCA-006 checkpoint group 2") | same date |

**Hash rule.** If the owner acts on another date, or the group-2 folder takes
another name, the verifier substitutes the actual values at exactly S1–S4 and
recomputes the SHA-256. No other byte changes. The S1 Date row keeps its v2.3
bytes at the default value, so no hunk shows it. It is a slot nonetheless.
Other dates are not slots. `2026-09-25` at L18 ("was adopted on 2026-09-25 by
owner acceptance of SCA-005") records the v2.3 act and was a slot only in
v2.3. `2026-07-24`, `2026-07-27`, `2026-08-02`, `2026-08-09` and `2026-09-24`
record past acts.

The Status row and the epistemic sentence presume that the owner accepts the
whole group ("adopted … by owner acceptance of SCA-006 checkpoint group 2").
A partial or modified acceptance needs a redrafted candidate, not a slot fill.
This document is itself outside the slot rule. Its front-matter
`candidate_sha256` is re-measured with the candidate.

## 7. Requirement count and §14 family check

| Measure | v2.3 | Candidate |
|---|---|---|
| Requirement rows in §§9–10 (`\| PEC-XXX-NNN \|`) | 46 | 49 |
| Unique requirement IDs | 46 | 49 |
| New IDs | — | PEC-ORI-007, PEC-API-006, PEC-API-007 (none occurs anywhere in v2.3) |
| Families present | API, DSH, GAT, ORI, PRS, RCN, STR, SVC | same eight |
| Per family | ORI 6, RCN 6, GAT 4, PRS 7, STR 5, API 5, DSH 7, SVC 6 | ORI 7, RCN 6, GAT 4, PRS 7, STR 5, API 7, DSH 7, SVC 6 |
| Invariant rows (PEC-K-01..11) | 11 | 11 |

§14's identifier sentence, "`PEC-{ORI,RCN,GAT,PRS,STR,API,DSH,SVC}-NNN`
(requirements); no family overlaps v1.0 or v0.4", is byte-unchanged (L480–482
-> L525–527). It still covers every ID, because the new IDs extend two
existing families. No identifier is reused.

## 8. Checks

Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`
(Python 3.13.7). Git 2.54.0. The scripts are in the B5 run scratchpad
`…/scratchpad/B5/prd/`. They are run evidence, not repository files. Each
reads only the fixed absolute paths of this worktree.

| Check | Script (SHA-256) and command (cwd = scratchpad `B5/prd`) | Exit | Result |
|---|---|---|---|
| Build | `build_candidate.py` (`02e78b103e446e1994f28a407dd644fc09d5e029f0fb16ad5fea12014e14af05`); `python3 build_candidate.py` | 0 | Writes the candidate and the §3 hunk fragment from a line-anchored op list over v2.3; asserts the preimage hash |
| **Mechanical proof** | `prove_diff.py` (`cef834a7b951a3fe5950515539d636d996042f47f033713b05be9f47de8c4573`); `python3 prove_diff.py` | 0 | PASS: 17/17 blocks applied in document order, each matching exactly once at its stated v2.3 and candidate lines; result SHA-256 equals the candidate `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`; front-matter hashes checked |
| Canon texts present and old phrases absent | `check_canon.py` (`492ff4e6936069a72ba4029c78eb8a6d9031fb5493cb3d94727c8cb42004487b`); `python3 check_canon.py` | 0 | 16/16 texts found (14 canon texts verbatim; C-S8-AGENTS with the F-16 insertion as its only difference; the F-17 sentence); 6/6 removed v2.3 phrases absent |
| Invariant, terminology and count evidence (§4, §7) | `evidence.py` (`0ba29b6e96b8f2074ae0bd4fef7f46573ee725ffabcf75d5c5dc0c373ac8eba1`); `python3 evidence.py` | 0 | as reported in §4 and §7 |
| Document composition | `compose_doc.py` (`4e42859b689684de2e9526d265680319c38c509cd63a51a94d872cec7f92b61c`); `python3 compose_doc.py` | 0 | this file, from the §3 fragment |
| Unified diff | `diff -u projects/pec/docs/PRD.md …/CP2_CANDIDATE/docs/PRD.md` (cwd repo root) | 1 (differences) | 13 context hunks; every changed line belongs to H-01..H-17 |
| Whitespace | `git diff --check --no-index /dev/null <file>` for the candidate and for this file (cwd repo root) | 1 for each file (with `--no-index`, exit 1 means the files differ from `/dev/null`) | no whitespace error printed for either file; an independent `grep -nE '[[:space:]]$'` over both files finds none (exit 1), and neither file contains a tab |

`prove_diff.py` reads the `diff` blocks of §3 in this file in document order.
For each block it checks that the `-`/context lines sit at the stated v2.3
lines and the `+`/context lines at the stated candidate lines. It then applies
the block to the working text as an exact, line-anchored string replacement
that must match exactly once. The working text starts as the live preimage
bytes. At the end it asserts byte equality with the candidate and checks both
front-matter hashes. The PEC reliance-hold preflight was not run: this run
only drafts a candidate, and it performs no dispatch, reliance, promotion or
fan-in.
