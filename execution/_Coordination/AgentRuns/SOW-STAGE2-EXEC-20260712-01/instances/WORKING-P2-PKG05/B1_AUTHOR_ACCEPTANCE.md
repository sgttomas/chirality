# WORKING-P2-PKG05 Author-B1 Acceptance

Status: `ACCEPTED FOR FRESH VERIFIER`

The manager reproduced the author terminal package: 5/5 exact members,
148/148 mapping blocks, 1,292/1,292 physical legacy-source lines, 25 exact
replacement rows, 25 exact inverse rows, five apply/target/rollback
simulations, and 15/15 candidate files. The self-excluding child manifest has
1,168 rows, SHA-256
`69f53c9229ee541b270df0d9c34710a6d2d65316fa0537a30e73a1a487f70b49`;
all rows, byte counts, and hashes reproduced, and all 51 bound JSON files
parsed. Candidate manifest SHA-256 is
`c13d33625c3f256ee8860dd0ae41576db0f7e01e1943cbb3b08e784b80ca27c4`.

| Member | Evidence SHA-256 | Production SHA-256 | Finalization SHA-256 | Mappings | Lines |
|---|---|---|---|---:|---:|
| DEL-05-01 | `84d35dda5f8440d49046cc668af1d828a97f46031b08d99d85ca21a6f98be515` | `248beedc9e4dfd0febbae4a8e03ac2507946ee480627251d0ab74a02f3280acf` | `9fc28b036fb58499ba817d80c1799cb8ba715aba39b17539974c8e14c6286a0e` | 34 | 291 |
| DEL-05-02 | `21a0d9e04e6859592f182e54e7966f6939b9e0341ddb373d3375620526552712` | `ec94d8e446bf25760405893229bd91a773992c8ece3cb271d539292141fda783` | `f542697d2be32eede102f9806b001bc320b88430bf02b5928c8ac7c23ac3918e` | 26 | 176 |
| DEL-05-03 | `890aeab5d94fadaf99c031cde847b2e238dfbd12703eab58c0002ed2d012473b` | `db8d281b46acbb8aa0c529bbf07965a54bcee424ae7c0ec217560eafddba8765` | `49e84c94398c21386d009f20826c36a3aec2fe1dd7d375622d24443eb40a18a1` | 28 | 234 |
| DEL-05-04 | `60c8eddc479b0661ddc68c32b2fe4902e9ea1b60fede40d0788ff353f2d41492` | `d844393abd5bdd7b509f0839671339cbe89e600c75db91111567efa4eeb288b7` | `eb505ab254e4e1ba827bcf0c0fc104858cab3404dde122021af3bc8e9e4ec40c` | 32 | 269 |
| DEL-05-05 | `fa73cf8d1001cd4392dcecb2759e1f4e411db31554f0a2c346615b44d3359faf` | `3b0003c3fc44f4334d64a766b2afc4f6baf3d594a6fde9196009ff843d4c0c65` | `c0409e920ac5b9c4ba03fdb726d1556c52b5f52d2b48077c74ae00c2f7bf89df` | 28 | 322 |

Two conversions, finalizations/reports, production-bound maps/parity reports,
checklists, and renders per member are byte-identical. Seven negative probes
per member fail closed. Live nine-file bindings remain exact and Piping diff
is empty. Current Scope-of-Work/runtime tests pass 21/21.

The retained failed attempt is safe and mechanical: a reusable harness
asserted the literal branch name `main` despite exact accepted HEAD and
`origin/main` bindings in the isolated checkout. The second attempt removed
only the branch-name assertion and preserved the exact commit gates. No tool,
semantic, authority, source, candidate, lifecycle, or acceptance defect was
repaired or waived.

Blockers, waivers, unknowns, semantic expansions, contamination, project
writes, and required author reruns: none. This acceptance releases only the
fresh evidence-only verifier and does not accept or integrate project truth.
