# Stage-1 Candidate Schema Freeze

Verdict: `FROZEN_FOR_MEASUREMENT`
Basis: `main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`
Schema marker: `chirality-deliverable-sow/v1`

Both calibration returns pass without a schema/content conflict or requested
change. The frozen implementation is therefore the unmodified candidate at
the basis above. This freeze is a Stage-1 measurement control, not ratification
or an amendment to TYPES/SPEC canon.

| Frozen surface | SHA-256 |
|---|---|
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `637d45769192c55ca270280c9a67d22b71afe7a1c165535cb663ce8fcaec70dc` |
| `tools/scope_of_work/id_catalog.json` | `7a1f8a1251147f7134c50058d633bb242979d2955285ce4a146cc886220be757` |
| `tools/scope_of_work/common.py` | `70f0e41360ed70dc6d4ddf89aff094eb9f230bcc7958c8cf26e6c5095ea84bef` |
| `convert_four_documents_to_scope_of_work.py` | `73bdd11f8799c9506c08ff4f937f5b07a46177b0a1e8438b7d7084e8df439997` |
| `validate_scope_of_work.py` | `6f894cd623fdda62fe851eb14df5b0f58f9212caf110f5388cc69403d6ae3106` |
| `map_scope_of_work_claims.py` | `59f539cbf70c8428998d2a6f285c7ea30846da9163e0e0b691dcd13797b9b25f` |
| `report_scope_of_work_parity.py` | `7d666619ba0ae908bedc734edeaf052f6096719db06bd58dfd25bf744f6f1bb9` |
| `render_scope_of_work.py` | `cb96ff118ae567540827b1563e66c0b4b2092aa47d4d4adbaf3da6a181e2056e` |

Calibration commits: App Dev `9f219099e...`; Piping `64aceb781...`.
The Piping runtime-capacity fallback is a separately recorded substrate result
and does not alter this freeze.
