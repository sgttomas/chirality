# Owner triage sheet — G0 v3 release rows

Status: `OPTIONS UNSELECTED — NO REGISTER DELTA`

The exact live rows are in `../REGISTER.csv` at basis SHA-256
`eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.
Each row identity below is the SHA-256 of its complete newline-terminated CSV
record. The restatement names the fields material to this triage; the cited
CSV record remains the exact row.

## TM-APP-025 — Dual-target App product-delivery direction

- Exact live row: line 2, SHA-256
  `326816615419aa76c61af973b739d509338b5f5372c7c9da7a2787ac6062fd57`.
- Live state: `OPEN`; priority `TBD`; assignment `App planning instrument;
  A=human-only`; no Trigger, Disposition, or closure evidence.
- Live concern: rule how App UI, packaging, and runtime-contract planning
  serve standalone desktop and the per-domain control-plane skin.
- Source remains exact: `execution/_Coordination/NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`,
  SHA-256 `3231f46463e5a9d2b93793ae39b3b78a041878220932b369d76a976601090cb3`.

Change since opening: G0 B1 ruled `macOS arm64 only; 2nd target deferred` and
said this row closes `RESOLVED_BY_DECISION` when SCA-APP-008 applies
(`plans/steers/chirality_app_v3_g0_record_2026-08-22.md:80-82`, SHA-256
`86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`).
SCA-APP-008 is now applied: `_LATEST.md` is `12c7758...`; its
`Impact_Assessment.md:105` says macOS arm64 is rc.1 and a second target is
deferred, at SHA-256
`068c7b29734ea7ca4a0af9bc63d6355beb23f2083b668725d93c951bf53f4cf0`.
The release plan's G0 evidence list requires TM-APP-025 to be recorded
(`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:614,780`,
SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`).

Unselected options:

1. `RESOLVED_BY_DECISION` using G0 B1 plus the applied SCA exact bytes as
   closure evidence. This is the evidence-aligned execution of the recorded
   conditional closure path.
2. Retain `OPEN` only through a new owner ruling that supersedes B1's closure
   instruction and states the remaining undecided product question. Without
   that new ruling, retention would leave a closure echo.
3. `SUPERSEDED_BY_SCOPE_CHANGE` using SCA-APP-008. This would be a new owner
   choice and is less exact than B1's expressly selected
   `RESOLVED_BY_DECISION` taxonomy.

## TM-APP-027 — Shared-runtime version negotiation

- Exact live row: line 3, SHA-256
  `5bc5966ea43648d02ed83c2858bf675d7c002a296e665a0f4041e38ef945e48a`.
- Live state: `DEFERRED`; priority `TBD`; Trigger SHA-256
  `656107530a0fc95611c26d94d356f5ac4ef938443716b0b57bdd09bbd2d45b8d`
  over 728 UTF-8 bytes.
- Trigger requires accountable-human acceptance of the exact compatibility
  package, positive-decimal epoch, complete immutable six-member binding
  manifest, and a routed App notice stating the negotiation posture.

Change since deferral: epoch 1 and exact package bytes were accepted, and the
App received `NOTICE_2026-08-21_ROOT_DEL0206_COMPATIBILITY_ACCEPTANCE.md`
`5930ad2c...`, but the accepted snapshot at
`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`,
SHA-256 `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`, keeps all ten
`HELD_UNAVAILABLE` bindings, including `release_act`. The required complete
binding condition is not met. The 2026-08-19 compatibility notice
`17f26956...` remains the reciprocal carrier history. SCA-APP-008 does not
lift these holds. G0 B3 says retain `DEFERRED`, not fired, expected at G6a–G7
when `release_act` completes the manifest (`g0_record:86-87`).

Unselected options:

1. Retain `DEFERRED` with the Trigger byte-identical; classify
   `STILL_BLOCKED`. This is supported by current bytes and G0 B3.
2. Retain `DEFERRED` but prospectively sharpen the Trigger to cite the exact
   acceptance-005 snapshot and all ten current held bindings. This is a later
   owner-directed row-maintenance act, not performed here.
3. Close only after a later accepted package satisfies the complete binding
   condition and the required routed notice states the negotiation posture;
   current evidence cannot support closure.

## TM-APP-028 — Complete shared-runtime degraded mode

- Exact live row: line 4, SHA-256
  `bf292765033d18fed549b67a4b8b8588c6a029ac5f29bdf8caa8d037128909da`.
- Live state: `DEFERRED`; priority `TBD`; Trigger SHA-256
  `3e4676ea6bb408f47b2d112982a518ae8083e7a557d8409e50d63549837ac8b6`
  over 743 UTF-8 bytes.
- Trigger requires the same accepted complete package/binding gate and a
  routed App notice saying whether the accepted ten-condition degraded-mode
  contract remains current.

Change since deferral: the exact epoch/package acceptance and App notice
landed, but all ten bindings remain held. SCA-APP-008 applies carrier and
contract changes without satisfying this compatibility-completion Trigger.
The release plan says to triage the exact Trigger without inferring that it
fired (`release plan:614,666`); G0 B3 retains it `DEFERRED`.

Unselected options:

1. Retain `DEFERRED`, Trigger byte-identical, as `STILL_BLOCKED`.
2. Retain `DEFERRED` with a later owner-directed exact-evidence sharpening
   parallel to TM-APP-027; no semantic weakening is implied.
3. Close only after the complete manifest and reciprocal-current-posture
   evidence exist; no present bytes support that result.

## TM-APP-030 — Daemon/helper bundle identity

- Exact live row: line 6, SHA-256
  `7359b18b66a1a8974ced33c11c9a6aaf5ddd9a95efe71805f9692819ca88d1d5`.
- Live state: `OPEN`; priority `TBD`; assignment `HELP_HUMAN packet
  preparation; A=human-only`; no Trigger or Disposition.
- Live concern: the shared Electron bundle identity remains an owner-choice
  residual despite recovery evidence.

Change since opening: G0 B2 says, verbatim, `Let it resolve at G-HELPER`
(`g0_record:84`). Applied SCA-APP-008 preserves the row: its
`Carrier_Map.md:45` says no carrier makes the bundle-identity decision and
its `Impact_Assessment.md:102` says the row remains open for G-HELPER. The
Carrier Map is
`projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Carrier_Map.md`,
SHA-256 `72a1b55b5307b6df5131011e30581e323737e95f3bcf85471121481ded25b619`;
the Impact Assessment SHA-256 is `068c7b29...`. The release plan assigns the second-job
host/installer/identity proof to G-HELPER (`release plan:484,785`).

Unselected options:

1. Retain `OPEN` until G-HELPER produces the decision packet/evidence named by
   B2. This matches the current owner route.
2. Owner rules the bundle identity now and closes `RESOLVED_BY_DECISION` with
   a separate exact decision record; the present packet supplies no such
   decision.
3. A later accepted carrier explicitly absorbs the decision, followed by
   `SUPERSEDED_BY_SCOPE_CHANGE`; SCA-APP-008 expressly did not do so.

## TM-APP-032 — Current Root successor identity for D-APP-48

- Exact live row: line 7, SHA-256
  `3456bc79c6255d84036aa34e7a69cc27cbab73e235920edfcc76e9d9c3d6e696`.
- Live state: `DEFERRED`; priority `TBD`; Trigger SHA-256
  `86db999c69fe6ac0a2de49a664a118bad99f5e81699afe3a3e4e7a51fd5ba511`
  over 664 UTF-8 bytes.
- Trigger requires accepted exact compatibility-completion bytes with epoch,
  complete immutable manifest, a routed notice, and the separate human
  acceptance record; semantic bytes, epoch-only selection, draft production,
  implementation behavior, and TM-ROOT-117 closure alone do not fire it.

Change since deferral: the row's 2026-08-21 Notes entry (complete Notes
SHA-256 `1cdbb7abeacc6126cfb67a27bddc01b61030cf2b2e300f85898ac55bc0d2a1f3`)
already records that TM-APP-027/028/032 await the same DEL-02-06 accountable-
human gate, with no successor accepted. Acceptance-005 still carries ten held
bindings. SCA-APP-008 does not consume this Trigger. G0 B3 retains the row
`DEFERRED` through the later `release_act`-complete manifest.

Unselected options:

1. Retain `DEFERRED`, Trigger byte-identical, as `STILL_BLOCKED`.
2. Retain `DEFERRED` and, only by later owner act, sharpen its evidence pins
   to acceptance-005 while preserving every negative firing clause.
3. Close only after the current Trigger is satisfied or a new owner decision
   expressly supersedes the concern; current evidence supports neither.

## Packet-wide result

No option is selected. The evidence-aligned current classifications are:
TM-APP-025 `closure echo ready for owner ruling`; TM-APP-027/028/032
`STILL_BLOCKED / retain DEFERRED`; TM-APP-030 `retain OPEN for G-HELPER`.
Those are recommendations, not applied dispositions.
