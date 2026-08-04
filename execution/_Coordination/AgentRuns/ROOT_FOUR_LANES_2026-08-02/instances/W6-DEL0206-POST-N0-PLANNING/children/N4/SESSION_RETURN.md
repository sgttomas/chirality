# W6 manager receipt — N4

- Runtime child: `/root/w1_del0206/n4_w6`
- Runtime parent: `/root/w1_del0206`
- Launch brief SHA-256: `afa7d439917382fa0ff5aca3fefd06fd542d9f5bf2a5d4de4e475d01da78de7b`
- Governing brief SHA-256: `d8e47eda5594692379d408fd8a7713383589dd38a23f511c3fba37d04392db22`
- Verdict: `ADMIT_FOR_N5`; new findings: none.
- Recovery specification: `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`.
- Compatibility disposition: `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`.
- Degraded-mode delta: `cfec76035e3a527e561922308a67134f879cfd9b58122c7687593945ea88c593`.
- Open-item map: `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`.
- Implementation plan: `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`.
- Self-check: `924ae2ebc528925818513bcdaaa34132c664e2f2f64ebf4a61653ab254e9462a`.
- Child return: `a8a34949160fec63bf6dd6c33a373cd0dfd1609df0c3bd268e69a8555f2dab72`.
- Manager validation: all seven hashes reproduce; exact seven regular non-symlink files; 11/11 source coverage; no undeclared reads; D1-D9, all TBD/OD6 items, PEC `UNRESOLVED`, accepted findings, and REQ-027/035/052 remain explicit; candidate/fact and no-effect boundaries are intact; text hygiene and `git diff --check` pass.
- Disposition: accepted for fresh read-only N5 refutation only; no semantic package or implementation is accepted.
- Forbidden effects: none.

## Attempt 2 — N5-F01 disposition

- Brief amendment SHA-256: `49eb4a79bb1e5e52a47b245fbbe30b205603dc619da0c0ff584dac14d42982aa`.
- Accepted N5 finding capture SHA-256: `30c1178643ad4aa5405e2109df2ca461dc074b7c3e79e7a777228e1f812d169f`.
- Verdict: `ADMIT_FOR_FRESH_N5_RECHECK`.
- Changed only:
  - degraded-mode delta `cfec76035e3a527e561922308a67134f879cfd9b58122c7687593945ea88c593` → `ac7a3e50406ca7a46ca5a8b91af145f1c5ff95028fe7a9d8ff23d7ed5847a1cd`;
  - self-check `924ae2ebc528925818513bcdaaa34132c664e2f2f64ebf4a61653ab254e9462a` → `3587c2f2e5ff9579ae8c3ae42469d68df3c61041d388db721c0d9146c4bd0cf6`;
  - N4 return `a8a34949160fec63bf6dd6c33a373cd0dfd1609df0c3bd268e69a8555f2dab72` → `d16e409b41577113d38f4bcae630618730fcd1cbfbef5cec800dc3b6d031892b`.
- Preserved byte-identically: recovery specification `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`; compatibility disposition `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`; open-item map `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`; implementation plan `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`.
- Manager validation: the revised matrix has exactly ten independent condition rows and nine columns; every row has all nine cells and explicit unresolved fields; the accepted base SHA-256 is bound; positive and negative/adversarial verification duties are present; evidence remains globally `DESIGNED_NOT_EXECUTED`; exact seven-file membership, text hygiene, and `git diff --check` pass.
- Disposition: attempt 2 accepted only for fresh N5-R2 read-only recheck.

## Attempt 3 — N5-R2-F01 disposition

- Brief amendment SHA-256: `3f58f9d7c741a3ba4abf08e7822963acbc8c17d35af5b8150c7979c6bac4587e`.
- Accepted N5-R2 finding capture SHA-256: `33f9e22cb25bf9a44a83f11a90deac84bab93b98c3b1ca336432d42c20e73de1`.
- Verdict: `ADMIT_FOR_FRESH_N5_R3_RECHECK`.
- Changed only:
  - degraded-mode delta `ac7a3e50406ca7a46ca5a8b91af145f1c5ff95028fe7a9d8ff23d7ed5847a1cd` → `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b`;
  - self-check `3587c2f2e5ff9579ae8c3ae42469d68df3c61041d388db721c0d9146c4bd0cf6` → `92cfd5b00f463056cfa05df614df55ec31ea4395a849c005656753498ace3179`;
  - N4 return `d16e409b41577113d38f4bcae630618730fcd1cbfbef5cec800dc3b6d031892b` → `8c8722ace32e1dae6b3ed3c54ab975ad6056f407a94cdf4cfc167dcb6619636a`.
- Preserved byte-identically: recovery specification `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7`; compatibility disposition `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`; open-item map `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`; implementation plan `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9`.
- Manager validation: the exact invalid literal `D1/D6/D16` is absent and the corrected literal `D1/D6/TBD-016` is present; the degraded-mode matrix remains exactly ten condition rows by nine columns; exhaustive decision-ID review across all seven outputs finds no identifier above D9; exact seven-file membership, text hygiene, and `git diff --check` pass.
- Disposition: attempt 3 accepted only for fresh N5-R3 read-only recheck; N6 remains held.
