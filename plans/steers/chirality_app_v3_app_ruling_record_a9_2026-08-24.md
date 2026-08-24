# APP RULING RECORD A9 — `_LATEST.md` pointer act authorization — owner ruling of 2026-08-24

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: authorization of the SCA-APP-008 `_LATEST.md` pointer act withheld by A8-B. Target workspace: App-dev loop. Companion instrument: the pointer-act steer (`chirality_app_v3_pointer_act_steer_app_2026-08-24.md`; SHA-256 recorded in the PR that published this record — the files merged together). Prior instruments: A8 (SHA-256 `d4018737aa9ae33e5b26f2afd3fbb2ffc1e9c8d3fe0a2494cf64c951224b6c8f`), the Gate-5 steer (SHA-256 `1dfe6492f97d76d7cb57d44f4ba6f37c5011fc56c918149230800883326cf299`), and the approved Gate-4 package (`47daaedf84ba4e9450bef3c12be3d1ab42316e0e3daabc37641d06f1040fd8d6`).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-24. "[click]" marks the option the owner selected.

## Context

The SCA-APP-008 Gate-5 application act merged to `main` as
`d5e40b3c25fe527919f1d2d2a31ea97ce2835795` (PR #662). Per A8-B, that act
produced an exact pointer candidate and left
`projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` byte-identical.
HELP_HUMAN independently verified on `main`, post-merge:

- Live `_LATEST.md` pre-image: SHA-256
  `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`,
  1347 bytes, Git blob OID `c6ce8b2a92c67506887d95c88790a445dbc5668d`.
- Pointer candidate record `Phase5/LATEST_POINTER_CANDIDATE.md`: SHA-256
  `44c39e11b4de7621fe25d643d049443223ffbbcd8160855c3fb85d4a4186609a`.
- Proposed post-image payload `Phase5/_LATEST.proposed.md`: SHA-256
  `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`,
  1572 bytes, 21 lines.
- Four-way byte agreement: the candidate's embedded pre-image block hashes to
  the live pre-image identity, and its embedded post-image block hashes to the
  materialized payload identity.

A9-A — Pointer act authorization: [click] "Authorize — publish both".
  The owner authorizes one bounded App-loop act that replaces the live
  `_LATEST.md` bytes with exactly the bytes of the immutable snapshot file
  `Phase5/_LATEST.proposed.md`, producing post-image

  ```text
  12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b
  ```

  under the companion pointer-act steer. The act must re-verify the exact live
  pre-image immediately before the atomic replacement and fail closed on any
  divergence. The bytes are copied from the immutable snapshot, never re-typed
  or regenerated. If the applied identity differs from the value above in any
  way, the loop restores the pre-image and stops.

## Boundary of this authorization

The act moves one pointer file and appends one loop receipt, with run
evidence. It confers no notice routing, carrier activation, SOW change,
lifecycle transition, implementation dispatch, release, publication,
readiness, or reliance authority, and lifts no blocker. TM-ROOT-106/122, C1,
TM-APP-030, D-APP-97/F-APP-2, G1, G6a, the ten held `HELD_UNAVAILABLE`
DEL-02-06 bindings, WP-03/WP-05 fixtures, the accepted Root/App
account-consent contract work, and WP-09/WP-11 separation all remain exactly
as they are. The Gate-5 audit warnings remain unresolved derivative findings.

Not ruled here: routing of the regenerated Root notice
(`75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`); Root
schedule-basis transcription; the App Server 0.149.0 supply authorization;
any later gate; any implementation, activation, release, publication, or
reliance act.
