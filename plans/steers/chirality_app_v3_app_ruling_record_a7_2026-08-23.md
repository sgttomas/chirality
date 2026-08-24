# APP RULING RECORD A7 — Phase-2b candidate approval — owner ruling of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: approval of the exact regenerated SCA-APP-008 Phase-2b candidates returned by the App-dev loop (Receipt 198, merged as PR #659, main `8a022e44881211027d3da7309093e14e3759d21f`). Target workspace: App-dev loop. Supersedes nothing; the loop's instruments govern. Companion instruments: records A4 (SHA-256 `14db687762b9af099debbfe9cfcaab0879e7082922f6eda9897b3f4d61ff330d`), A5 (SHA-256 `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b`), A6 (SHA-256 `66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63`), and the Phase-2b steer (SHA-256 `41580e3b2079388873e8bcc56552bc59bc343674c5454915fe383eadc7417fda`).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-23. "[click]" marks the option the owner selected.

A7-A — Phase-2b candidate approval: [click] "Approve as published".
  The owner approves these exact candidate identities (SHA-256), all held
  inside
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2b/`:

  - regenerated K-CONTROL-1 transaction artifact
    `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`,
    carrying the regenerated C-01 LF-terminated row
    `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616`
  - re-pinned K-EVENT-4 transaction artifact
    `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463`,
    carrying the resolved C-06 LF-terminated row
    `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`
    (byte-identical to the Phase-2 resolved row)
  - resolved full App-contract candidate identity
    `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`
    (`34877` bytes, 214 lines), an in-memory reconstruction from the
    approved Gate-3 transactions, recorded by
    `RESOLVED_APP_CONTRACT_RECONSTRUCTION.md`
    `920a5f4091270d42048ab44161726ca87687624d97351d5a02840bf17617e2dd`
  - companion invariant-coverage register post-image candidate
    `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`,
    with application grammar recorded by
    `COMPANION_REGISTER_REBUILD_TRANSACTION.md`
    `db1941c1c87ae7cd849dac3b32968a6911e74eaee8c56239725682e44b93603d`

  Approval covers these exact bytes. HELP_HUMAN byte-verified before this
  ruling: the regenerated K-CONTROL-1 row states exactly one live control
  socket, gates the private daemon-to-Process-Supervisor socket behind
  DEL-02-07/WP-03, names the Root daemon as exclusive owner of the
  `{userData}/runtime` control surfaces under Root K-RUNTIME-1, and makes no
  "app-owned" runtime-directory or second-writer claim; the quoted ratified
  Root row is byte-identical to `docs/CONTRACT.md`
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`
  line 162, whose K-RUNTIME-1 and K-STORE-2 neighbours are byte-identical
  across the amendment; independent replay of the Gate-3 transactions
  reproduces both the Phase-2 control identity and the approved full-file
  identity above; and the register preserves its 83-ID/50-family accounting
  with K-CONTROL-1 recorded as design-mapped external Root authority
  (`MAPPED_WITH_OPEN_ISSUE`, `OpenIssueIDs = RUNTIME-OPEN-005;DEL-02-07;WP-03`)
  and no implementation-coverage claim.

  With Root's K-CONTROL-1 amendment ratified (A5-B) and this approval, the
  contract group's Gate-5 eligibility prerequisites are satisfied.
  Eligibility is not application: per A5-C, one separate expressly
  authorized Gate-5 act covers the decomposition and contract groups
  together, and any movement of `_LATEST.md` requires its own express owner
  authorization. This approval confers no application, pointer, lifecycle,
  register-as-truth, decomposition-target, SOW, dependency, code, docs,
  frontend, notice-routing, carrier-activation, implementation, release,
  publication, readiness, or reliance effect. Any byte change to an
  approved candidate voids this approval for the changed candidate and
  requires regeneration, fresh independent review, and a new owner act.

A7-B — C-03 notice routing: [click] "Route after Gate 5".
  The owner rules that the SCA-APP-008 notice to the Root loop is routed
  only after the Gate-5 application act, and only as a regenerated notice
  describing applied state. The frozen draft
  `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/DRAFT_NOTICE_TO_ROOT.md`,
  SHA-256
  `8ebc728b6d6c408a3dfeb60ae07887dbe7d5b88ba8fe06c1b954e98e8a380f72`,
  remains unrouted and is superseded for
  routing purposes: it predates both the Root K-CONTROL-1 ratification and
  the approved Phase-2b candidate bytes, so routing it would describe
  superseded content. Regeneration and routing are to be directed as part
  of the Gate-5 tranche, not as a separate earlier act. Routing is
  coordination, not authority: the receiving Root loop adopts, amends, or
  declines under its own instruments and cadence (AGENTS.md agent-index
  change-notice rule).

Not ruled here: the Gate-5 act itself and any pointer move; the exact
regenerated notice bytes and their destination surface; Root schedule-basis
transcription; TM-ROOT-106/122 and every held DEL-02-06 binding; C1;
TM-APP-030; D-APP-97/F-APP-2; G1 and every later gate; any implementation,
activation, release, publication, or reliance act.
