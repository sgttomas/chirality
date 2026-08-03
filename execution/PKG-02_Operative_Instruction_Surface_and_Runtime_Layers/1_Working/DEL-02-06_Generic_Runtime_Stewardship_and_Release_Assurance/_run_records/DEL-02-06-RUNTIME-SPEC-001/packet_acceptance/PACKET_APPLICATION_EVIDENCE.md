# DEL-02-06 accepted-input packet application evidence

Status: `EXACT ACCEPTED BYTES COPIED — FRESH N0 REQUIRED`

Date: `2026-08-03`

## Authority and acceptance

| Evidence | SHA-256 |
|---|---|
| Owner acceptance ruling | `7ddbef0480700483cb07efe771b64e3f413b489288a02bde987a6a85b9ba70f7` |
| Candidate presentation | `2ecd01dcfe95ca9417592875624dff1990cc4ddf6622a2d1126e24e97a2d4a42` |
| W4 return | `25cd4cd934d0141612c15719db1aa562ba4615657ca5eb2a4787fcfe61aeeac0` |
| External acceptance record | `ee035e91d561935d36c6238a50304752d2fd4e67d24e5c2203c550ff8d40760c` |
| Accepted CandidateSetManifestSHA256 | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` |

The acceptance validator returned `valid: true`, exactly one token, and equal
bound/candidate manifest identities.

## Byte-identical live copy

Source: `packet_candidate/`.

Destination: RunID-local `accepted_inputs/`.

Both roots contain exactly the same six regular files. Pairwise byte compare,
content/manifest validation, and SHA-256 recomputation pass.

| Exact file | Candidate SHA-256 | Accepted-input SHA-256 | Result |
|---|---|---|---|
| `CANDIDATE_SET_MANIFEST.sha256` | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` | `360f8f12c4719d79a506394bcd98a4b630c2610f9c80d90a08b0519e8a1d508f` | `BYTE_IDENTICAL` |
| `DEGRADED_MODE_CONTRACT_CANDIDATE.md` | `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` | `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` | `BYTE_IDENTICAL` |
| `OPEN_ITEMS.csv` | `26f967b5773dd0f0c1a91f6378b7037cf6ba253288b1902652764fbfc27dc351` | `26f967b5773dd0f0c1a91f6378b7037cf6ba253288b1902652764fbfc27dc351` | `BYTE_IDENTICAL` |
| `OWNER_GATE.md` | `89b389b7f4c1af8ca2f7ef92ee2a1fc0f9e8534d4b11b02862c482825df4874e` | `89b389b7f4c1af8ca2f7ef92ee2a1fc0f9e8534d4b11b02862c482825df4874e` | `BYTE_IDENTICAL` |
| `OWNER_SELECTION.md` | `0d802a85681924d17e314ebbe178e051ccfd915727c314f38a51a6a43ff04b73` | `0d802a85681924d17e314ebbe178e051ccfd915727c314f38a51a6a43ff04b73` | `BYTE_IDENTICAL` |
| `ROOT_COMPATIBILITY_POLICY_CANDIDATE.md` | `337a93d7075872f852beaeddd0841a4fb73cabc4b273ae1aa175cf6af57a8b38` | `337a93d7075872f852beaeddd0841a4fb73cabc4b273ae1aa175cf6af57a8b38` | `BYTE_IDENTICAL` |

## Current basis and boundary

PRD `d4f97d75…5cc4`, decomposition `23f6ae0f…64f3d`, fresh audit
`ee10313f…20e1`, and Gate-1 confirmation `05395c30…f40f` reproduced before
acceptance and copy.

This record authorizes no runtime semantic adoption, implementation,
client/project work, lifecycle/release/reliance effect, Task Management, Git,
or foreign write. Fresh N0 independently verifies the packet and basis before
any later manager decision.
