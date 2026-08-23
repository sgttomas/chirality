# Repair cycle 1 — terminal whitespace

- Manager disposition: remove exactly one surplus terminal LF from each of the four files named by the failed terminal candidate-whitespace gate; do not alter source, other evidence, or substantive validations.
- Repair: complete. Each named file decreased by exactly one byte. No content other than its surplus terminal LF changed.

| File | Pre bytes / SHA-256 | Post bytes / SHA-256 |
| --- | --- | --- |
| `ACTIVATION.md` | `880` / `63ad8fe7dc0608ca2463d15d63246c3d72d6540e0ec04c756390cc3e91b715f5` | `879` / `ab140cce1022fcfaf01ade300861b220de9657685fb6584f7812e469002af248` |
| `CHECKS_AND_LINEAGE.md` | `1,458` / `770c543aac62bd64e40218d99e4a9d1ce78bb2e906c6d5502d2a0244f0de47cf` | `1,457` / `ef6e9a82c4d7e5cee04567e3bd20a3530fcf13425a60d3a51562123f0be6332b` |
| `COMMAND_OUTPUTS.md` | `4,034` / `797e5b22dd2a2baa692d1044c7d043e5957cb4b3327c90e98b663eadb42e7762` | `4,033` / `0fbfe28975341254dd18d1bc7fa33a541252307b30e7a7c52cd01188e8375be2` |
| `IMPLEMENTATION_INVENTORY.md` | `4,017` / `e20655a842bc0afe066470ef413917fab66787f19dba5b288a92b42c86799178` | `4,016` / `f1065a97e6f8de66f2b36147631264e0cdec9a8eee24d7b2bbc92279326bdfce` |

The authorized repair touched only these four instance records. The new repair record is itself frozen before the single repair-cycle candidate-whitespace rerun.
