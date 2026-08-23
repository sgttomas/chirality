# ROOT RULING RECORD R1 — D-GOV-35, DEL-02-03 M2 application, SCA-004 Gate 1, TM-ROOT-107 — owner rulings of 2026-08-22

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: Root decisions following PR #620 (Root v3 Phase 0). Target workspace: Root governance loop (transcribed into Receipt 115). Supersedes nothing; the loop's instruments govern. Companion to `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`.


Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-22, after PR #620 merged as `abf3c1bf5996cd9333ad706df14e62df32fbbf0f`.
The rulings were presented as a four-item decision slate by HELP_HUMAN, who had
byte-verified the packet on `main`; "[click]" marks the option the owner
selected. Each ruled subject is identified by the exact bytes it was ruled
against. Where a ruling has a recorded form, that form is what the loop
transcribes and acts on.

R1-A — D-GOV-35 (delegated-harness-native delegation class): [click]
  "Approve as proposed".
  Subject bytes: `docs/governance_harness/_PROPOSALS/D-GOV-35_2026-08-22_delegated_harness_native_class/D-GOV-35.proposed.md`
  SHA-256 `924c1b098f1510bca9189e1ac06e4c2fd8e9d358a9fc3c4e42fdd04a53b69c88`;
  exact delta `AGENTS.proposed.patch` SHA-256
  `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`
  against `AGENTS.md` SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
  Recorded form: all eight proposed ruling items are ruled as written. D-GOV-14
  item 7 is superseded only in its sentence "managed child sessions are the
  sole executable app-harness delegation path"; the record-less SDK `Agent`
  bridge remains retired. Item 7 of D-GOV-35 resolves TM-ROOT-126 by
  prospectively superseding `docs/WORKFLOW_COMPONENT_STANDARD.md` §4.1
  ("Agent 0 delegates only to named Agent 1 roles."), `docs/TYPES.md` §4.3
  ("Agent 0 supervises only named Agent 1 managers."), and
  `docs/DBM_Agent_Instruction_Architecture.md` §2 ("Agent 0 delegates only to
  named Agent 1 roles. Agent 1 delegates to Agent 2.") with the ruled
  hierarchy: Agent 0 dispatches named Agent 1 managers and may directly
  dispatch bounded Agent 2 instances under the same sealed-brief,
  declared-scope, and durable-evidence requirements. The ruling is recorded
  per the D-GOV-34 convention (owner ruling recorded before publication;
  CandidateSHA / PublicationSHA / EffectiveSHA backfilled by their Git acts).

R1-B — DEL-02-03 M2 application tranche: [click] "Authorize, one tranche,
  export deferred".
  Recorded form: one bounded instruction tranche applies the exact
  `AGENTS.proposed.patch`, propagates the ruled wording to the three
  concordance sentences named in R1-A, finalizes the N2 draft manifest
  (`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-03_Delegation_Hierarchy_and_Entry_Rules/_run_records/DEL-02-03-M2-PREP-001/ROOT-DGOV35-DELEGATED-HARNESS-NATIVE-20260822.yaml`,
  SHA-256 `59f0ed42ce498a6d3fbed9148b70691a0e4ceda49e37c890ed8391c4861ef7da`)
  into the live manifest corpus, routes the App and Piping coordination
  notices in the same tranche, and records the Root-owned Chirality App
  public-export regeneration as an explicit deferral to the next export
  release. No lifecycle state of DEL-02-03 changes; no hold is lifted.

R1-C — SCA-004 Gate 1 (v3 release-pathway Root carrier intake): [click]
  "Accept as parsed".
  Subject bytes: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Brief.md`
  SHA-256 `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`;
  `Gate_1_Validation.md` SHA-256
  `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14`;
  `WORK_GRAPH.json` SHA-256
  `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`.
  Recorded form: the owner accepts the eight parsed actions — MODIFY
  DEL-02-06 as the standing integration/release-assurance carrier; ADD
  DEL-02-07 through DEL-02-12 under PKG-02; ADD DEL-04-11 under PKG-04 — with
  all ten DEL-02-06 bindings held and App coupling as notice edges only.
  Acceptance opens Gate 2 impact refinement only; it creates no folder, SOW,
  mapping, or implementation authority, and no later gate is inferred.

R1-D — TM-ROOT-107: [click] "Yes" — record TM-ROOT-107 as
  `SUPERSEDED_BY_SCOPE_CHANGE` with `ScaRef` SCA-004 via routine Task
  Management. TM-ROOT-035, TM-ROOT-042, and TM-ROOT-108 remain OPEN on the
  closure conditions in `Task_Management_Harvest.csv`; TM-ROOT-106 and
  TM-ROOT-122 are untouched. Consequential to R1-A and G0 B5: TM-ROOT-126 is
  resolved by D-GOV-35 and may be recorded `RESOLVED_BY_DECISION` in the same
  routine Task Management act.

Not ruled here: C1 (App Server 0.149.0 artifact download) remains not
authorized; no pin change (G0 B4); no App-loop act — SCA-APP-008 reciprocates
under App authority when the App steer is issued.
