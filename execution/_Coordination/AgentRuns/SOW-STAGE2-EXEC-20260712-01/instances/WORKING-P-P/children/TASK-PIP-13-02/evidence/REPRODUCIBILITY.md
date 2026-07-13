# Execution-Substrate Reproducibility

Verdict: `PASS`.

- Legacy validation: valid `LEGACY_FOUR_DOC`, zero issues.
- Target validation: valid `SOW_V1`, zero issues.
- Claim maps 1/2 are byte-identical: SHA-256 `42e3e073b73fb8d273ffe0ecc9e4326353112ad91bad645b241d42663c3f1845`.
- Parity JSON 1/2 is byte-identical: SHA-256 `58e76ae4c409283de5e3d398c8fc7c3fb6f0446891f731f167fe31ee0bae2`; Markdown 1/2 is byte-identical: `14d3ddaa7358701c1dcca5db068aa101782a76ebbd58906f76252275269d3142`.
- REVIEW checklist 1/2 is byte-identical: SHA-256 `a7df476e54587d971d28922e827914c36c4f231edb25faedacc570c611fcc0fe`.
- HTML render 1/2 is byte-identical: SHA-256 `dfac3cc0091de56ff194d2ac8afde72fcc0a93260c8750ebd521ffe274d3c796`. Neither file contains a script tag, active `src`/`href` resource, iframe, import, or external resource reference.
- All registered tools completed successfully. The converter was not invoked.
