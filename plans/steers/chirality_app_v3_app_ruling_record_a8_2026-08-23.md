# APP RULING RECORD A8 — Gate-5 authorization, register-anchor correction, pointer disposition — owner rulings of 2026-08-23

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: authorization of the SCA-APP-008 Gate-5 application act, disposition of a defect found in the A7-A-approved companion-register candidate, and the `_LATEST.md` pointer disposition for that act. Target workspace: App-dev loop. Supersedes A7-A **only** as to the companion-register candidate identity; every other A7-A approval stands. Companion instruments: the Gate-5 steer (SHA-256 recorded in the PR that published this record — the files merged together), and records A3 (SHA-256 `91d6867286de465f56bb41a6de9e9d8657e6b63ddb009f294d81b3e6dcccded9`), A5 (SHA-256 `1896d89200c4cd390b4606aed0229fe03bf7c5070f454e1dca5d6c6acde2bb9b`), A6 (SHA-256 `66bd22a1b439979f74bbaedf2c182d222a6ba38952ec046f78fc2091885e4e63`), A7 (SHA-256 `56b9dc8ed8835a3220ccab10416cd9457d2a1d58b62c92582d84c773430e22d2`), and the approved Gate-3 (`1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`) and Gate-4 (`47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`) packages.

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-23. "[click]" marks the option the owner selected.

## Defect context for A8-A

Before drafting the Gate-5 steer, HELP_HUMAN verified the approved
candidates against real artifacts and found that the A7-A-approved
companion-register candidate
`69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0`
cites, in all 83 rows of its `AppDecompositionBasis` column, the
decomposition candidate identity
`932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`,
which matches no artifact that has ever existed in the repository.

The true decomposition post-image is
`932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`.
HELP_HUMAN established it independently by applying the approved Gate-3
D-01 through D-05 transactions to the live decomposition pre-image
`dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`,
each anchor matching exactly once, producing 112419 bytes — the byte count
Gate-4 states — and that identity. Gate-3, Gate-4, ruling record A3, and
all Phase-1 evidence cite the true value correctly.

Origin and blast radius: the incorrect value was introduced in the Phase-2
companion-register rebuild and carried forward verbatim into Phase 2b,
which is why a Phase-2-to-Phase-2b differential could not surface it. It
appears only in candidate and evidence artifacts — the Phase-2 and
Phase-2b register candidates, their transaction records, and the Phase-2
N2 and Phase-2b N4 evidence. **It never reached live authoritative truth:**
the live register cites neither value. HELP_HUMAN additionally audited every
64-hex identity cited across all six approved Phase-2b artifacts against
the content of every tracked file and every independently derived identity;
this anchor is the only unresolvable one. The pre-amendment Root contract
identity `ed87eaff…` also resolves to no current file, correctly, because
the candidates cite it as superseded lineage.

A8-A — Gate-5 authorization and register-anchor correction: [click] "Fold
into Gate 5, approve `62c9a318…`".
  The owner authorizes the SCA-APP-008 Gate-5 application act under a
  separate owner-carried steer, covering the decomposition and contract
  groups in one act per A3-C and A5-C, and directs that the register-anchor
  defect be resolved as the first node of that act.

  The correction is a pure deterministic transformation of the approved
  candidate: replace every occurrence of the incorrect value with the true
  value in the `AppDecompositionBasis` column and change nothing else. The
  owner approves the resulting exact identity

  ```text
  62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3
  ```

  at 98230 bytes, 83 rows, 50 families, with `AppDecompositionBasis` the
  only column differing from `69abc885…`, zero occurrences of the incorrect
  value, and 83 of the true value. HELP_HUMAN computed and structurally
  verified that identity before this ruling. It supersedes
  `69abc885…` for application; every other A7-A-approved identity —
  K-CONTROL-1 `cf889103…`, K-EVENT-4 `c6b6d314…`, and the resolved
  full-contract identity `842bf170…` — stands unchanged and re-verified.

  The corrected candidate must be regenerated and independently reviewed
  inside the Gate-5 act, with exact pre→post lineage recorded. If
  regeneration yields any other identity, or if house convention would
  require re-labelling the anchor rather than correcting its value, the loop
  stops and reports; a different label is a different owner decision. The
  superseded Phase-2 and Phase-2b candidates and their evidence retain the
  incorrect value as immutable history and are not edited.

A8-B — `_LATEST.md` pointer disposition: [click] "Withhold; produce a
candidate".
  The owner does **not** authorize pointer movement in the Gate-5 act.
  `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` remains
  byte-identical at
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`
  throughout. Gate 5 instead produces an exact pointer candidate — pre-image
  identity, proposed post-image bytes, and post-image SHA-256 — as an
  artifact for a separate later owner act, exactly as Gate-4 section 8's
  fallback directs, and closes the application run as awaiting pointer
  authority. Applying the pointer, or treating written targets as implying
  pointer movement, is forbidden in this act.

## Boundary of this authorization

The Gate-5 act applies exactly the approved transactions to exactly the
named targets, re-extracts dependencies for the amended carriers, runs the
fresh named closure audit
`AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION`, and returns under
fresh independent review. It confers no carrier activation, SOW change,
lifecycle transition, dependency hand-edit, implementation dispatch,
release, publication, readiness, or reliance authority, and lifts no
blocker. TM-ROOT-106/122, C1, TM-APP-030, D-APP-97/F-APP-2, G6a, G1, the
ten held `HELD_UNAVAILABLE` DEL-02-06 bindings, WP-03/WP-05 fixtures, the
accepted Root/App account-consent contract, and WP-09/WP-11 separation all
remain exactly as they are. D-APP-103 continues to defer. Per A7-B the
regenerated Root notice is produced and marked routable but not routed, and
no Root-loop path is written.

Not ruled here: the pointer bytes and their application; routing of the
regenerated notice; Root schedule-basis transcription; any later gate; any
implementation, activation, release, publication, or reliance act.
