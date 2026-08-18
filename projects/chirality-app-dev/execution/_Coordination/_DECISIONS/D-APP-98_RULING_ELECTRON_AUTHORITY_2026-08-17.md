# D-APP-98 — Electron authority disposition

Status: `RULED — C2`

DecisionID: `D-APP-98`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**C2 — Electron authority disposition, TM-APP-041.**

Electron `43.2.0`, as pinned in `frontend/package.json` on `main`, is the App's recorded Electron authority and the D-APP-72 successor for that single fact. D-APP-72's `43.1.1` reference is historical. Future Electron changes are made by amending the pin and recording a successor disposition in the same tranche; no separate packet is required for patch/minor upgrades that pass the registered checks and the packaged-artifact proofs of the release-preparation phase. TM-APP-041 is resolved by this ruling. No dependency, product, or lock-file byte changes in the recording tranche.
```

## Effect

`TM-APP-041` is resolved by this ruling and awaits the next TASK_MANAGEMENT
maintenance pass. This tranche changes no dependency, product, package, or
lock-file byte.
