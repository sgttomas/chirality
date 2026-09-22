# R4 QA — RUN_D128_CONCORDANCE_2026-09-21_1614Z

Built by `R4/_scripts/r4_qa.py` from `R3/CLUSTER_INDEX.csv`, the final R3 concordance, `R4/PACKET_INDEX.csv`, `R4/PACKET_SUBQUESTIONS.csv` and the packet files. C1–C4 are the checks the R4 brief requires; C5 is a form check.

| Check | Verdict | Detail |
|---|---|---|
| C1 every PRIMARY cluster row is PRIMARY in exactly one packet | PASS | 2401 PRIMARY rows; not exactly once 0 []; extra 0; packets in index 25, packet files 25, missing files [] |
| C2 packet counts reproduce from PACKET_INDEX.csv and the concordance | PASS | packets checked 25; count blocks not reproducing []; sub-question coverage problems [] |
| C3 every UNKNOWN, AUTHORITY_CONFLICT and HumanDecisionNeeded != NO row is in some packet | PASS | 990 rows ({'UNKNOWN': 23, 'HDN': 798, 'AUTHORITY_CONFLICT': 169}); missing 0 [] |
| C4 no packet presents CONTEXT as GOVERNING | PASS | CONTEXT source on a [GOVERNING]-tagged line or GOVERNING tier on the CONTEXT packet: 0 [] |
| C5 packet form (header, headings, evidence tags, no absolute paths) | PASS | problems 0: [] |

Input hashes (SHA-256):

- `R3/CLAIM_CONCORDANCE.csv` `a6f6cdda685173cac3aa8ab75d8dd823143feadbde2c44a755571337936dd852`
- `R3/EXTENSION_CONCORDANCE.csv` `eeaaf27fcba05f2b8a16c6429a95be220b071c2b8938c41a3d5ff959854dbb37`
- `R3/CLUSTER_INDEX.csv` `9efe82c66a7173af17ba14087d539544d13d24fee1563c3ab7506740c977c046`
- `R4/PACKET_INDEX.csv` `b17789eb6c6775a36c4ad986e0d423eff4b6218a6e1deea00cd8e696cd399457`
- `R4/PACKET_SUBQUESTIONS.csv` `122b627019a6e1d96708ba48de3ecd10d237dd3093e27305c2a18c716e5e979b`
