# R16 N0 ancestry and immutability proof

| Field | Exact value |
|---|---|
| R16 merge parent of N0 | `b0d975a9139eddebf5c1e728cf724b55c8a97cad` |
| immutable N0 transcription commit | `9164d95456bd67576a1b1164fd08e52516edb368` |
| immutable N0 tree | `3184f5f899422458e39e435409b724a8cb1c94ef` |
| N0 proof commit | `0246e92b4bfede52c226d58122e8ac4bb980e666` |
| N1–N3 evidence commit | `661174b8834eb795cd368e06dec891caa9b021dc` |
| N1–N3 evidence tree | `192e75f75cbd177a0c0a8c9b73bceaddc193929b` |

`git merge-base --is-ancestor 9164d95456bd67576a1b1164fd08e52516edb368
661174b8834eb795cd368e06dec891caa9b021dc` exited `0`. The N0 commit's
tree still resolves to `3184f5f899422458e39e435409b724a8cb1c94ef`; therefore its
delta and bytes are unchanged. The branch was never amended, squashed,
rebased, reset, force-pushed, abandoned, or rewritten.

The N0 commit and proof commit were pushed before N1 download and before any
spike binary executed. The later evidence commit was pushed ordinarily and
descends from both. Final closeout repeats the ancestor check against the
final PR head.
