# N3 deterministic validation record

- Accepted basis: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`.
- Frozen `origin/main`: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`.
- Report SHA-256:
  `61640f586ea50854fc01eb3e83ef7cb58c4de27e0453a01b38efb80698cc3869`.
- Whitespace-repair lineage: preimage
  `d0992ab1d9110a94c9b6c6f4c7c38ade971fbd215a2076743c24860c2104cab8`
  to postimage
  `61640f586ea50854fc01eb3e83ef7cb58c4de27e0453a01b38efb80698cc3869`;
  exactly two trailing ASCII spaces removed from each of 31 direct citation
  headings (62 bytes total), with reconstructed preimage hash exact.
- Citation verification: `PASS`. Manager verification compared 31 directly
  hash-bound citation ranges byte-for-byte with `git show origin/main:<path>`
  and recomputed every adjacent complete-blob SHA-256. Fresh REVIEW-03
  independently verified all 37 citation occurrences, including the six final
  plan-row citations using the report's explicit shared plan blob binding.
- Fresh review sequence: REVIEW-01 `BLOCK` on one calibrated prose finding;
  the report was repaired inside the fixed content target; independent
  REVIEW-02 `PASS`, zero actionable findings; closeout whitespace repair;
  REVIEW-03 `PASS`, zero actionable findings.
- REVIEW-01 SHA-256:
  `4aeb974539c3f5ecf360d83c50cf8d26f23be2864a03d89483158b3b802c2518`.
- REVIEW-02 SHA-256:
  `479b30edbd8b1304d7aa31d80579e71a5de4b41d8691fbe572cde66703958aa0`.
- REVIEW-03 SHA-256:
  `311db7ca3efdfa2507a14eb42710910d30b46ed6db2dd7ba88b53e1f1b21933c`.
- Candidate whitespace over the N3 content/control targets: `PASS`.
- `git diff --check` over the N3 content/control targets: `PASS`.
- Frontend diff from basis: empty.
- Frontend tree at closeout:
  `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`, equal to basis and frozen
  `origin/main`.
- Git index mutation by N3: none.
- Network use: none.
- Out-of-scope subject write: none.
