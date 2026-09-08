# Independent review return — Runtime SOW successor adoption

Verdict: **PASS**

Role: fresh nondelegating ephemeral Agent 2 independent reviewer. Role and nondelegation are instruction-asserted. Requested model allocation: `gpt-5.6-sol`, medium.

## Sealed basis

- Lane HEAD: `c5192790f98ec024e7c2728cb1d4df3ae2b2a2dd`.
- Author `OUTPUT_MANIFEST.json`: SHA256 `96eda353cdd6f34d7353fee820cf834856cb7508b68c65e4e0e7d7e8e3d34360`, 113 members.
- Author `CANDIDATE_DIFF.patch.gz`: SHA256 `310f3aeed23fa94d7e7b8579b2f7e42b12e1347f9d375dee039b5fa7313caf04`; uncompressed size 343525 bytes; uncompressed SHA256 `9b0e6db3861c2e1451dab4063bc27aa66ac649657421404570aad8b6bd2e47fe`.
- Successor policy: SHA256 `bc0aa4c917f1773bba26cb3bee98fd4cca1c9788addeff0582626d485caae840`.

All 113 manifest members match their recorded bytes, SHA256, and Git-status class. The frozen diff reproduces the exact 112-path combined delta from HEAD; the self-excluded output manifest makes the complete package 114 paths.

## Findings

The three predecessor adoption objects are byte-for-byte identical to the account-authority policy and remain in the same order: `D36_STAGE1`, `D36_STAGE2`, `D36_ACCOUNT_AUTHORITY`. The new fourth object is only `D36_RUNTIME_SOW_PROPAGATION`, containing exactly the Runtime DEL-02-06 and DEL-02-09 SOW paths with continuous predecessors and accepted postimages. App DEL-02-05 is absent from the Root policy.

The format-aware verifier is narrow and fail-closed. It selects the exact Runtime SOW acceptance schema and verifies the pinned owner acceptance, Markdown subject, acceptance package and all members, manager manifest and all members, audit manifest and PASS verdict, application addendum and all members, bindings, postimage index and ordered two-file projection, current pointer, handoff manifest and Root input, live postimages, and publication bytes. Existing canonical path, symlink, duplicate, predecessor, scope, and no-execution rules remain active.

Independent hash checks verified every direct policy reference and all 32 members of the five selected manifests. Runtime owner acceptance `0329293b…`, subject `37141786…`, acceptance manifest `e90c7850…`, index `ffac4201…`, audit `432aa2e1…`, application `efb4011f…`, pointer `da47241b…`, and both live SOW postimages match exactly.

The positive composition is exactly four ordered adoptions with `state=accepted-pending-publication`, `published=false`, and `execution_authority=false`. Counts remain 53 source, 46 governance, seven Runtime, and nine holds.

The 32 retained negatives meaningfully cover missing/altered acceptance, subject, every selected manifest/index/binding/pointer/input class, a manifest member, wrong type, symlink, mixed Runtime SOW state, wrong predecessor/postimage, App/unknown/escaping path injection, and duplicate changes. The focused suite passes all 14 tests with `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python`. Independent G0, G1, G2, G3, and G4 checks pass. Author evidence also records 839 affected tests and 48 subtests passing, clean candidate whitespace, clean `git diff --check`, and a zero-exit harness self-check with its existing diagnostics retained.

Staged custody is unchanged: exactly 83 paths, index tree `64f944b55cc69b34ecccaca585f4ca399354d8c5`, staged binary diff SHA256 `4e00e0147eb66b779ce6a7aecc079c61ad87e2afc854110e12685df2b7f61577`, and no worktree drift on any staged path. The 29 unstaged Root-author paths are exactly within the sealed write scope. The staged `.gitattributes`, Runtime/App SOWs, proof files, and pointers were not edited by Root authoring; no Runtime/App canonical, source, SOW, or `.gitattributes` path appears in the unstaged Root delta.

D-GOV-40, the register, Receipt 150, M2/G4 manifest, notices, and handoff consistently record existing D-GOV-37 authority, local pending-publication status, App exclusion, and no execution/release grant. No publication is claimed. CHANGE staging/publication, CI, and fetched-main recognition backcheck remain required.

This review wrote only the three new `review-v1` artifacts. It did not stage, commit, push, alter the candidate or index, or mutate Runtime/App evidence.
