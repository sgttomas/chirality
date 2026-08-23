# Exact one-byte EOF repair lineage

## Authority and boundary

- Authority: owner-approved record-only repair in `CHAT_TRANSCRIPTION.md` and `AMENDMENT_05_RECORD_ONLY_EOF_REPAIR.md`.
- Authorized shared write set: only `instances/A2-PKG09-R20-PHASEB-VALIDATE-02/{ACTIVATION.md,RETURN.md,VALIDATION.md}`.
- Transformation: remove exactly the final `0a` byte from each preimage; no content rewrite or normalization.
- Repair execution: one `apply_patch` operation removed the final empty line from all three files. No other path was targeted by the repair operation.

## Reversible byte lineage

| File | Pre bytes | Pre SHA-256 | Pre tail | Post bytes | Post SHA-256 | Post tail condition | Reversal proof |
|---|---:|---|---|---:|---|---|---|
| `ACTIVATION.md` | 1,668 | `3c50905cd730925da6ccf9374b8880a09c48b893b2ac2effb5795f2789ec2cb2` | `0a0a` | 1,667 | `0eee8bf6ceb539797c418fc55411c8fbda2f6ee1c981bb7950bdf14e4c59e9bb` | ends `0a`, not `0a0a` | `postimage + 0a` SHA = exact preimage SHA |
| `RETURN.md` | 5,937 | `9620af4620e4cbaae32ce22e06b2cc214b81149fc67542a2d340278ce322caaf` | `0a0a` | 5,936 | `6257fccadf4062d7549b512abea5eebb0abcc5a4edfb69ee9021ecee564c80d3` | ends `0a`, not `0a0a` | `postimage + 0a` SHA = exact preimage SHA |
| `VALIDATION.md` | 8,126 | `ef06190377bbba777089b70635575ff3e67642fadbf62eb40f3b161d6cd76440` | `0a0a` | 8,125 | `d1a4f7788ed1a4b5fd865be4abc992ff1625134b38ae73327ce75f5c52c04d34` | ends `0a`, not `0a0a` | `postimage + 0a` SHA = exact preimage SHA |

Before mutation, each prospective postimage (all bytes except the final byte) plus one LF compared byte-for-byte equal to the current preimage. After mutation, each postimage matched the prospectively frozen prefix hash, and appending one LF reproduced the exact preimage hash. Each byte count decreased by exactly one. The repair is therefore fully reversible by appending one final LF to each named postimage.

## Immutable preservation at repair boundary

- Historical executor `RETURN.md`: 16,439 bytes / `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399` before and after.
- Raw `desktop-pack.full.log`: 15,852 bytes / `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2` before and after.
- All 15 accepted raw-log path/byte/hash identities matched before repair.
- Shared R20/status/TM: `bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c` / `6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48` / `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8` before and after the repair.
