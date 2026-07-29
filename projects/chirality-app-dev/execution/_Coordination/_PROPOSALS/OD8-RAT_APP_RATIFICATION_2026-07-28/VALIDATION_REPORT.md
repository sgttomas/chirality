# D-APP-82 Validation Report

Date: 2026-07-28

Basis: `85ea0628fa4e57dd6aae53b06139b2b8734a9612`

Stage: `prepared`

Verdict: `PASS`

## Evidence identity of the four ratified acts

Every record and closeout below was hashed at the basis and matches the
identity already recorded inside the corresponding effective-state closeout or
register row. No value in this package is a new claim about those acts.

| Decision | Record SHA-256 | Closeout SHA-256 | RecordCommit | EffectiveCommit |
|---|---|---|---|---|
| D-APP-78 | `47e97b8f2baf5901972852ca03f5c586ee3842ea882e0a00a725c92de9f41fdd` | `2121ceca7f74af2b7db8a1af138d13fa95d181da92964ed47df8397174fdcb0e` | `63777c0f447536c6a0aecbe8c545339edf8973fb` | `23b3b07d1122ae065affe69346c53bac78289a2e` |
| D-APP-79 | `23d1fdf8b3aa9c1e28ee876adece5443a8a4a182c54201285c5f1cfa871316d2` | `e25fa5aac5b6a74ee9f3e281162a9af0069c7b07affdf9d4569e54a789e57045` | `c19fa656a434e4cf38bffeafe0ec15a3274d7262` | `deb01644e324af2b39cff7b52abae43784cd071b` |
| D-APP-80 | `26f381bcb3548961670e9ee1ceb9e9f1ee4babf05632a6e195d20758f57614a6` | `2834005d9e2d9334265da54c2a2081522cc1c74afb756ce7d96a604ad063e924` | `0410a15df4c8be0e8a768fbca6080a8f7b637c10` | `b0b673dc3d65a4cfff9a045fda6c1fefa060645c` |
| D-APP-81 | `6c373bf5d0ed67e1d4a7044ed88bd3163fc90941bc3f3fae41fbacb34e1d1294` | `f767fcaab9ffbf264caa9d69ae7204881fc423d78f9c60750698fe88795030d5` | `a149fb8d6a6e58a9b66510f9d1a06674c6b565e9` | `826351b810758d5143a9114ce5d6b78d0990d13e` |

The D-APP-78, D-APP-79, and D-APP-80 record SHA-256 values reproduce the
values asserted in their own effective-state closeouts, and the D-APP-81 value
reproduces the one asserted in the D-APP-81 closeout.

## Accepted candidate identities of the ratified acts

| Decision | Accepted artifact | SHA-256 | Reproduced |
|---|---|---|---|
| D-APP-78 | `OD6-G2-T1_TERMINAL_APP_BASIS_2026-07-28/TERMINAL_BASIS_MANIFEST.json` | `8c66030719cab9ca268e3c16ad6fa298d6bfab9153e6a492abf6c3632fcfd8ef` | PASS |
| D-APP-79 | none — no immutable pre-decision candidate exists | — | DISCLOSED DEFECT |
| D-APP-80 | `OD6-G4_APP_CONTRACT_CONCORDANCE_2026-07-28/LIVE_SURFACE_MANIFEST.csv` | `6507828512e247f4cd96c1b2ae84cf72c7b1c1973bd2b69dfb21ef32206c7218` | PASS |
| D-APP-81 | `OD6-G5_APP_HOLD_RELEASE_2026-07-28/LIVE_SURFACE_MANIFEST.csv` | `5d0dacdf790d63bb44a579382b56acd776547cbf46cac401adce9e585b92613d` | PASS |

## Preparation checks

| Check | Result |
|---|---|
| Four decisions enumerated, one section each | PASS — 4/4 |
| Each decision independently declinable | PASS — one fence per decision |
| Owner-return fences present and unique | PASS — 5/5 (4 ruling + 1 D-APP-78 token) |
| No ruled record modified | PASS — no existing record is in the write set |
| Register append only, one new row | PASS — 6 columns, State `AWAITING_RULING` |
| Ratified-act SHA-256 identities reproduce | PASS — 8/8 records and closeouts |
| Accepted-candidate manifests reproduce | PASS — 3/3 (D-APP-79 has none by defect) |
| Post-release live hold register state | PASS — header-only, SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f` |
| Next App loop receipt number | PASS — last is `Receipt-101`, draft is `Receipt-102` |
| Receipt draft contract shape | PASS — 4 required records, allowed fields only, 8 top-level records, 2,098 bytes excluding the heading |
| App loop receipt validator on the untouched ledger | PASS — `VALID` |
| `validate_od8_rat.py --stage prepared` | PASS — verdict `PASS`, zero violations |

## Disclosed defects carried into the ratification record

1. **D-APP-78 selection token never returned.** The record conditions its own
   authority on a verbatim owner return that no App artifact records, and
   `Receipt-96` labels the transcription `CHAT_TRANSCRIPTION — EVIDENCE, NOT
   RULING`. D-APP-82 presents the exact token for return now, dated 2026-07-28
   as the new act, never backdated.
2. **D-APP-79 has no immutable pre-decision candidate.** Its register Packet
   column reads "— (recommendation and owner direction transcribed in the
   ruling)", unlike D-APP-75, D-APP-77, D-APP-80, and D-APP-81. The posture is
   ratified against the exact record and closeout SHA-256 values instead.
3. **Blanket authorization for all four acts.** Each was authorized solely by
   the single 2026-07-28 blanket owner direction, quoted verbatim inside the
   ratified records themselves and cited here by reference only.
4. **Author equals merger, zero reviews.** Each landing pull request (#393,
   #394, #397, #401) was merged by its own author with no recorded GitHub
   review. K-MERGE-1 evidence status for those pull requests is recorded in
   the merge-approval matrix package landing at
   `execution/_Evaluation/MERGE_APPROVAL_MATRIX_2026-07-28_85EA0628/`, cited
   content-addressed by manifest SHA-256
   `53844bfdcedaf5bae4396241375deba5dd35cc5b6d483342efac4a28268fccc1`.

None of these defects is cured by this package. They are disclosed so that the
owner's fresh per-decision judgment is informed rather than implied.

## Completion checks (not yet run)

`validate_od8_rat.py` with the default `--stage completed` must exit `0` after
the owner session and the completion tranche. It then requires zero remaining
placeholder fences, a D-APP-82 register row that has left `AWAITING_RULING`,
and every manifest postimage — the ruling record included — reproducing
byte-for-byte.

## Evidence identities of this package

- `CANDIDATE.md`:
  `119005ed743d8de70de10de29fe9767e103901eb2e3995ab0c6275b115cd8a78`
- `LIVE_SURFACE_MANIFEST.csv`: recorded in `ARTIFACT_HASHES.sha256`
- `RECEIPT_DRAFT.md`:
  `b2629b4a030c79a28abf553f337318fdb9ee887c2e2e809adccdf7a188128e3d`
- `validate_od8_rat.py`:
  `98d03a3939965520aff6bc099d1e95203e4a994681bbb9da75950b7c6df17c36`

The package hash list is generated last, after all package prose is stable,
and covers every package file except itself.
