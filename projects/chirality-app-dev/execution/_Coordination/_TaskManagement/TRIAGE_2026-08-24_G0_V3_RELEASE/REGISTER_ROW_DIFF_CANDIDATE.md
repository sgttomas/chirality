# Unapplied register row-diff candidate

Status: `CANDIDATE ONLY — NOT APPLIED`

The live register remains SHA-256
`eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`,
29,035 bytes. `REGISTER_LAST_REVIEWED_CANDIDATE.csv` is a complete hypothetical
post-image, also 29,035 bytes, SHA-256
`00f7754c4effe1cbd240976023834b891161fc8781373a63a94ae6fecc2db016`.

The candidate changes exactly one field on each of the 12 reviewed non-closed
rows: `LastReviewed` from its existing value to `2026-08-24`. Header, row
order, all other fields, and closed TM-APP-044 are byte-identical. It does not
change `Status`, `Trigger`, `Priority`, `Disposition`, `Evidence*`, `Closed`,
`Notes`, or any notice/adoption field.

## Exact CSV row identities

Each identity hashes the complete newline-terminated CSV row.

| Row | Live `LastReviewed` | Candidate | Pre-image SHA-256 | Post-image SHA-256 |
| --- | --- | --- | --- | --- |
| TM-APP-025 | `2026-08-02` | `2026-08-24` | `326816615419aa76c61af973b739d509338b5f5372c7c9da7a2787ac6062fd57` | `1e8c2ea205a0f9ea9acaed22546dec291908621d95fbbb16b198b01376abf182` |
| TM-APP-027 | `2026-08-19` | `2026-08-24` | `5bc5966ea43648d02ed83c2858bf675d7c002a296e665a0f4041e38ef945e48a` | `e4b9128e6ffa97a8906499047b30c4de88d4f4eac1e18e89e6f7d2c9bd13c6c8` |
| TM-APP-028 | `2026-08-19` | `2026-08-24` | `bf292765033d18fed549b67a4b8b8588c6a029ac5f29bdf8caa8d037128909da` | `c563f187a0291f001d4b78e0188d9e3ff1668fb5b81571fa7cb07e1779bc8194` |
| TM-APP-029 | `2026-08-02` | `2026-08-24` | `b8644019cf7d129cc27ae9e7565f38a08aefb1072592ea0e717a2695821cd1ed` | `450810d75136b05e66c0ca2e7946e9e0d582ca50fbeae2daf4e7a36f691fd3f1` |
| TM-APP-030 | `2026-08-02` | `2026-08-24` | `7359b18b66a1a8974ced33c11c9a6aaf5ddd9a95efe71805f9692819ca88d1d5` | `6a1927ad326015132f5795d013b435912a806485eb7c897c7e47624a09fa2d6b` |
| TM-APP-032 | `2026-08-21` | `2026-08-24` | `3456bc79c6255d84036aa34e7a69cc27cbab73e235920edfcc76e9d9c3d6e696` | `8669b9ebe5bcf3448838279a3e6819bceadbfce755f4c4dc87400c68551a3251` |
| TM-APP-033 | `2026-08-02` | `2026-08-24` | `1cad4d43e7e93f4b255c542a95d102dd10476367bd6905b076d337aeb4d6b693` | `1d3d578888b6543c8f201240bc8da87753e7e681e3604c90f851337e39ef9f7b` |
| TM-APP-034 | `2026-08-02` | `2026-08-24` | `9d50b7a32b6e1b036ca2e1b59130a9f83f8ffa9c16a77b713ebc3e27aa81566c` | `e1c7311c3b9e90858cbd8f4b05c6f941b9a47bab9450d26d68c8a38598b674cf` |
| TM-APP-036 | `2026-08-21` | `2026-08-24` | `a9bd2a78c5770c6d04203d962c5c7df9d75b33c93c1fbebac9950ca369447ce8` | `3e36618ebf23f96eccb3413b262b695440ac5d87720caa3b761725f902fc8257` |
| TM-APP-038 | `2026-08-03` | `2026-08-24` | `3728e221c72b859d64effe9d84e89500b8e63d75873618007608c6e597952773` | `c11b8d5a3d8d79c1887aa9d37ccebd4825eb29f3a647ceb137eb72727d0c59df` |
| TM-APP-040 | `2026-08-03` | `2026-08-24` | `8049f1d2b00f655608258d555402256d028aff7424ac2204bdd459cb48a329f9` | `9a79c0fa5e9d9e23527777eca0fc67325e1e67f2288da90125f09ab8339940c0` |
| TM-APP-042 | `2026-08-09` | `2026-08-24` | `41577c4a95fef7a25c0de40d9bcc93f5b1c167eec41c40ac6714596e08a43e21` | `485ced8ae9e932c0e563d41405b59f2409627f76a0b8e7b9357b87199c500025` |

Unchanged control rows:

- Header row SHA-256 remains
  `8f44ca48f90fbf5dfae355b77917a1076ac0a263d3d9147f5fadd0bf5f4e4f1a`.
- TM-APP-044 SHA-256 remains
  `20facb6978ecef9f8fa5b4a9023d6535fa92cff6aedef825554c16f0043d42d7`.

## Mechanical proof

A field-aware CSV comparison must report exactly 12 cell changes, all in
column `LastReviewed`, and zero other differences. The candidate is provided
so a later owner ruling can name exact bytes. It is not a register mutation,
does not bind the owner to accept it, and must be regenerated if the live
register changes before any later application.
