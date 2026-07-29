# Validation — GOV-STEP4-APPLICATION-20260729

Status: `PRE-COMMIT PASS`

## Basis and pre-application integrity

- Worktree branch `gov/step4-sca-application` resolved to
  `204321467b567ede862636a36dd67bcac1ff326a` (frozen basis; clean before
  authoring).
- The three live decomposition surfaces matched the v1.1 basis SHA-256
  identities before application (working surface `2dd37e20…`, ledger
  `0d48abe0…`, register `ec32b36f…`).
- `validate_gate3_candidate.py` re-ran pre-application: PASS 37/37; the
  regenerated `Gate_3_Validation.json` was byte-identical to the frozen
  copy (git status clean — the frozen package was not modified).
- Grant-candidate file hash re-verified at basis for context only:
  `cdd8844b42ca772aab96b5c942873eb4e7c957f0b262fba6daabc61834f2f38e`
  (file untouched; inert draft per the owner's in-session direction).
- Merge facts verified in git: PR #417 merge
  `6e21530f7182ca2a7e7831b9528f85889a4a4467` carries second parent
  `dfc8d4af532b07f8e562ace2f910ca777e63173f` (the approved HEAD); PR #418
  merge `204321467b567ede862636a36dd67bcac1ff326a` carries second parent
  `e5e8f760548e739078a1735b176cd56604d5d4c9` (the approved HEAD).

## Owner-act byte verification

Each act was transcribed to a scratch file with `printf`, then measured
with `wc -c` and `shasum -a 256` before any transcription into records
(em dash U+2014 between statement and signature):

| Act | Bytes | SHA-256 | Result |
|---|---|---|---|
| `ACCEPT SCA-002 271d456a — Ryan Tufts 2026-07-29` | 49 | `cfd81bc53f29c051b8d59b89b3566c36a459011c52d8deaa2eb39ddbe592208b` | MATCH |
| `BRACKET AS RECOMMENDED: at application, update SOW-042 SourceRef to cite D-GOV-31 adoption — Ryan Tufts 2026-07-29` | 116 | `a34878f59dcd4365a5f95fd68b7da70a452c875cc398724148c4a189d8db035a` | MATCH |
| `APPROVE HEADS dfc8d4af5 (PR #417) AND e5e8f760 (PR #418); MERGE #417 THEN #418 ON MY BEHALF — Ryan Tufts 2026-07-29` | 117 | `f7b0136d3b8daf11d312d4d6e0714f6e45c59d35e618ff03c3fd6d67e190834b` | MATCH |

Fence re-verification after writing (extract between the
`BEGIN/END OWNER RULING VERBATIM` markers, strip indentation, re-hash):

- `execution/_ScopeChange/SCA-002_2026-07-29_0800/Decision_Log.md` —
  2 fences (acceptance, bracket ruling), both byte/hash MATCH.
- `execution/_Coordination/LOOP_RECEIPTS.md` Receipt 63 — 3 fences
  (acceptance, bracket ruling, merge direction), all byte/hash MATCH.

## Applied-state verification

- Working surface applied SHA-256
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`
  == accepted candidate hash (exact-byte copy).
- Deliverable register applied SHA-256
  `b18ebe6b9bc3cdac6bd0bd78f6470be328a81783c7c6ab5b55478b506c61e8da`
  == accepted candidate hash (exact-byte copy).
- Scope ledger applied SHA-256
  `fea77787c2e20217bf168f7f773c4c86d1dbb5e2984d1712723afea95173c1dc`;
  differs from the accepted candidate in exactly one record (0-based
  index 42, file line 43, SOW-042) and within it exactly the `SourceRef`
  cell: `PRD §5.3 D-8 [TRANSCRIBED]` → `PRD §5.3 D-8 [ADOPTED-D-GOV-31]`
  per the owner bracket ruling; CRLF preserved (105 CRLF, 105 LF total).
  The bracket form follows the ledger's single-token bracket vocabulary.
- Diff vs basis touches exactly the intended cells: SOW-042 row
  (statement + SourceRef bracket) in the ledger; DEL-04-06 row
  (Description + AnticipatedArtifacts) in the register; the working
  surface per the accepted candidate diff. All other records byte-equal.
- `validate_gate5_applied.py` over the LIVE files: **PASS 33/33**
  (`Gate_5_Validation.json`), exit 0.

## Deterministic checks

- `python3 -m pytest tools/validation/test_validate_instruction_tranche_manifest.py -q`
  — 36 passed, exit 0.
- `python3 tools/validation/validate_instruction_tranche_manifest.py`
  (G4 CI mode) — `G4 PASS (CI mode)`: all 16 manifests schema-valid,
  including `ROOT-SCA002-APPLICATION-20260729`, exit 0.
- `git diff --check` — clean, exit 0 (the .gitattributes CRLF policy from
  PR #417 covers the exact-byte CRLF register).
- Placeholder grep over every new artifact — clean (no matches).
- G4 diff mode
  (`--base 204321467b567ede862636a36dd67bcac1ff326a --head HEAD`) and the
  committed-HEAD whitespace validator
  (`validate_candidate_whitespace.py --base-ref 204321467…`) — run
  against the tranche commit; results recorded below.

## Post-commit check (appended at closeout)

- Committed-HEAD results recorded in HANDOFF_STATE alongside the commit
  SHA by the supervising session at fan-in.
