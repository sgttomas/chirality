# DEL-02-06 regenerated six-file candidate presentation

Status: `CURRENT CANDIDATE VALID — OWNER GATE OPEN — NOT ACCEPTED`

Date: `2026-08-03`

## Exact current candidate identity

Candidate directory:
`packet_candidate/` under RunID `DEL-02-06-RUNTIME-SPEC-001`.

CandidateSetManifestSHA256:
`360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f`.

| Exact packet file | SHA-256 |
|---|---|
| `CANDIDATE_SET_MANIFEST.sha256` | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` |
| `DEGRADED_MODE_CONTRACT_CANDIDATE.md` | `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` |
| `OPEN_ITEMS.csv` | `26f967b5773dd0f0c1a91f6378b7037cf6ba253288b1902652764fbfc27dc351` |
| `OWNER_GATE.md` | `89b389b7f4c1af8ca2f7ef92ee2a1fc0f9e8534d4b11b02862c482825df4874e` |
| `OWNER_SELECTION.md` | `0d802a85681924d17e314ebbe178e051ccfd915727c314f38a51a6a43ff04b73` |
| `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md` | `337a93d7075872f852beaeddd0841a4fb73cabc4b273ae1aa175cf6af57a8b38` |

The manifest omits itself and contains exactly five sorted hash lines. Its
exact bytes supply the candidate-set identity above.

## Exact corrected and confirmed basis

| Evidence | SHA-256 / identity |
|---|---|
| Git observation | `HEAD 2b7a7d828e9173836e5b0a71fc015e4f45024215` with exact applied S5/S6 worktree bytes |
| Accepted DEL-02-06 Scope of Work | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` |
| Owner continuation ruling | `9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6` |
| `docs/PRD_ROOT.md` | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` |
| Live Root decomposition | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| Fresh AUDIT_DECOMP return | `ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1` |
| Gate 1 owner-confirmation record | `05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f` |
| SCA Decision Log | `d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508` |
| SCA Handoff State | `625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6` |
| S5 applied-file hashes | `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de` |
| S5 applied validation | `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8` |

The fresh audit is `PASS`, `COV-POST-001` is closed, and Gate 1 is confirmed
as zero actions/no decomposition change. Those acts do not themselves accept
this packet; packet authority remains the prior DEL continuation ruling and
this separate exact owner gate.

## Stale predecessor disposition

W3 manifest `dd0075229486b98a5b28936ce55ea94e0fcbb6c8d5befc2f453cff78f6d053cf`
was never accepted and is now stale derivative history because it bound prior
decomposition SHA-256 `69bdb9ca…1278c`. Exact historical hashes and no-effect
state are retained in `STALE_CANDIDATE_HISTORY.md`; neither identity is
current packet truth.

## Validation evidence

- Candidate validator SHA-256:
  `c2a1bc80442cebea214e0a810e73ba4f9b7eeb4ed4225dbfbb45a6a76824dbb4`.
- Owner-acceptance validator SHA-256:
  `fb153b5648bbb909838c50215a11705ae4f7c66737d75a6f2d46016d89c3d152`.
- Negative-case harness SHA-256:
  `fbd47a25b1c6aab51969e2ab2bf106ecca2192154e2721470d7258368dd1c21c`.
- Content-only validation: `PASS` with five exact content hashes.
- Full validation: `PASS` twice with byte-identical JSON and manifest
  identity `360f8f12…d508f`.
- Isolated negative validation: `PASS`; 20/20 cases rejected for their
  expected issue.
- Validator compilation, JSON, candidate whitespace, and protected-state
  checks: `PASS`.

## Exact owner token

The only matching acceptance line for this exact current candidate is:

```text
ACCEPT DEL-02-06 INPUT PACKET 360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f — Ryan Tufts 2026-08-03
```

No acceptance token has been recorded. No `packet_acceptance/` record exists.

## Stop boundary and next owner

No `accepted_inputs/` directory was created or written. No N0/N0-R2 was
dispatched. No runtime, client/project, SCA/decomposition/PRD, lifecycle,
release, reliance, register, foreign-loop, or Git action occurred.

Next owner: the human owner through `HELP_HUMAN`, solely to `ACCEPT`, `RETURN`,
or `DEFER` the exact current candidate manifest above.
