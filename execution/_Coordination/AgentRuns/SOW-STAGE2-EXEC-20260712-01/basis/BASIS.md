# B0 Synchronized-Main Basis

Status: `PASS`
Observed: 2026-07-13 (America/Edmonton)
Basis commit: `c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`

## Accepted upstreams

- D-GOV-16 ruling publication: `7584718aa32b112e415331736d1a8e68c12ac176`.
- accepted Stage-2 plan snapshot: `27f03730c956447b9a9696422cc9c63b8f061939`.
- accepted plan binding: `b22a24fda994a8387a9bf2e04a2826dc311a36dd`.
- Stage-1 inventory: `execution/_Coordination/AgentRuns/SOW-STAGE1-20260712/instances/RECON-FANIN/evidence/DELIVERABLE_INVENTORY.json`, SHA-256 `ef65cfa7bf7ed4e09285a00df20fb575271a825adb3cd1c0617730b08df835fa`.
- App candidate evidence commit: `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`.
- Piping candidate evidence commit: `31c35ea9798c29cd0af16b7089186f3942dcfcb1`.

Local `main`, local `origin/main`, and remote `refs/heads/main` all resolved to the basis commit. Both the plan binding and ruling publication are ancestors of it.

## Ruled bytes

| Artifact | SHA-256 | Result |
|---|---|---|
| successor standard | `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` | exact |
| `TYPES.proposed.patch` | `9614166c7db8340532d838768be2de52567862757fe0d5add3d3a90edea9d4b4` | exact; apply-check PASS |
| `SPEC.proposed.patch` | `543200af8a617e2f5673db110eef2b0a5cf742c54e70ccda8bce0cad870d4b2e` | exact; apply-check PASS |
| Stage-2 evidence index | `8a6e48ac8247fe5147afb4208d3e7c0b4f48cb1071b1e086b4f24a2ceeded806` | exact |

## Census freeze

- 154 tracked members: App 53; Piping 101.
- ten pilots; 144 remaining; 143 ordinary remaining plus one ISSUED.
- 153 `IN_PROGRESS`; one `ISSUED`.
- sole ISSUED path: `projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline`.
- zero missing companions; zero tracked or working-tree `ScopeOfWork.md` members.
- sorted path digest: `b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31`.

Every pilot's four live source hashes and `_STATUS.md` hash match the Stage-1 inventory. Candidate hashes reproduced from the evidence commits:

| Pilot | Candidate SHA-256 |
|---|---|
| App `DEL-07-01` | `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744` |
| App `DEL-07-02` | `80fbd86600af8516d75d2d11ccf53d304ec36426069728fbe30a8fceb846d952` |
| App `DEL-07-03` | `6fa7732954b95314176d81045edeb9492405785cf4568acf210968f903cc9ab0` |
| App `DEL-07-04` | `d456e9d29262c0cb9d0fc3350ab52b1b5a36b9c3bfab1378476c2e3ae55a9342` |
| App `DEL-07-05` | `f38b0e741949abd9a892e8fea1a93c91be7da95bda668b3c80c2fd4dac7f450e` |
| App `DEL-07-06` | `6de59e2a9d6806fb620c673b1da4822337b4c531a41de3186c9f0fde8e10b93e` |
| Piping `DEL-13-01` | `6c76b2c785acc56ee1e67aaba64930e457b8c2ca20d4d9e8b4156cebe579c43d` |
| Piping `DEL-13-02` | `43d9ea2fa0e4fa95c4906fb8f7abffabe7c23a92d7bbc6ea4a4c9f430293c6d8` |
| Piping `DEL-13-03` | `cde7f4b4332c5e89dbe72afca11f1dbc907b06a459f56962b1c1cd35fad0df4c` |
| Piping `DEL-13-04` | `01ce58d6636f39535933c8f365735336118da7bf85223346bf6b7d1c78bdd046` |

## Caller freeze and containment

The accepted original-vocabulary search now returns 5,370 paths with digest `c06c8b449fa1dc56ca1398baf4fb888b848a5a1d36f2d53373fe385e5c243f66`. The five-path increase from the accepted planning basis is exactly the five integrated accepted-plan records; nothing was removed. The targeted transition-vocabulary search returns 117 paths with digest `91b1d8719135c23bd77185506929859613bb25d22260f3f5998a9ff02f7050f1`. Their union is 5,414 paths with digest `4895fdd43564019a8b70457507653212a6573cdd08e34872658d0bbe8696a89d`.

`CALLER_MANIFEST.tsv` enumerates 58 active governing/executable surfaces, five retained legacy surfaces, and one derivative export; historical and independent families are aggregate-count/digest rows. Zero active callers are unclassified.

Tracked state was clean. `git status --porcelain=v1 --untracked-files=normal` reported only the pre-existing `.claude-worktrees/` container and this fresh execution-run directory. No `.claude-worktrees/` content was read or mutated.

This basis package is immutable derivative evidence. It does not replace D-GOV-16, the accepted plan, decomposition truth, deliverable truth, or lifecycle truth.
