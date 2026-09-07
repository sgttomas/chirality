# D121 carrier application — DEL-09-06

Status: `APPLIED_REVIEWED_PENDING_CHANGE_COMMIT`

Authority: D-APP-121 owner selection A-design and A-proof; ruling file SHA-256 `fa410ae195c74fab2ad3de7cb5d64e244a327905ea3d1f76849f6b51fb74caeb`. The ruling is observable on main, now `e8cdc460cffccfe9e58ab4e5b9bbc05350c09327`. HELP_HUMAN explicitly released the exact carrier application; no repeat vote occurred.

Accepted patch: `execution/_Coordination/AgentRuns/APP_V3_RULED_INCREMENT_2026-09-06/pdf-application/ACCEPTED.patch`, SHA-256 `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32`.

## Applied union

| Carrier | Owner | Preimage SHA-256 | Applied postimage SHA-256 |
|---|---|---|---|
| `PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI/_STATUS.md` | PKG02 | `da18f6ef905840270718f88947fcbfdd13d26609f1c9a06522f1463385999ecd` | `af33c2623097cdffb3eedb58819a0bfbdf8c5dcb987b4f13befbeed6b72b1960` |
| `PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md` | PKG09 | `d8152c669ca3e57768004e184ec75ac9aaccaba5791d96589547e017545c1fe0` | `0f4b65b53f0e05183fcd8a5f489bb2da8ccdb4ead6fab22944f89f8daf42e6ba` |
| `PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/ScopeOfWork.md` | PKG09 | `1fed47a10b3f480a545947e6cf1d60ef7e150f166caceb4a26c0267f92dde652` | `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0` |

PKG02 evidence: `execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg02-cross-root/d121-carrier/APPLICATION.json`, SHA-256 `be4919c7314750711f65cf400a9457b30a840ece9b0e92c88ebf99506a0700a9`.

PKG09 application evidence: `execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg09-d121/application-v2/APPLICATION.json`, SHA-256 `48b189fddd6b7d250409852793baf228d40a88beb273b592ac6677e5d2755203`.

All three live files byte-compare equal to the retained accepted postimages. Complete-patch reverse check passes and the exact union is `+12/-3`. `git diff --check` passes.

## Independent review and validation

Fresh separate reviewer `/root/app_pkg09/d121_carrier_review`, model `gpt-5.6-sol`, reasoning `medium`, returned PASS with no findings. Role and Agent 2 nondelegation are instruction-asserted. Review return SHA-256 `4bad420a228ba05df58e9ba9a7498b011b1a9572062e7ecb595e645dfb6d2505`; checks `a312494a9d4476391a45c6eddf7cc1f893390455dc90c931becd01aea767520f`; manifest `0470c90bf1317d972c80d3179d6075db7f33c82cfb1d31286769e0f3f8740e42`.

Configured Python `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python` validation:

- live SOW: `SOW_V1`, valid, no issues;
- generated review checklist: one `DEL-09-06-AC-001` item with `DEL-09-06-VER-001`, snapshot SHA-256 `2cd5fc07681b3c4535ecad5bcf58e7b9343ff58e3311187d7ecd4762797c24e4`;
- APP-HOLD dispatch/reliance: `ALLOW`; post-sync closeout scan `d27f77a49487b75c51d2ba7a3929587bcc8231651a67ed73a05a02b2a838478b`, register `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc`;
- authority corpus v20: MATCH, no drift;
- receipt validator: PASS before append;
- practitioner harness status: PASS; self-check exits 0 with the pre-existing baseline findings retained; practitioner-harness pytest: 379 passed.

Frontend source/build/native checks were skipped because this application changes carrier and evidence records only. No frontend source or process was changed.

## Applicability and closure

The accepted D121 scope is now seated in DEL-02-03 and DEL-09-06. The generated checklist is a current derivative snapshot of the amended SOW; its D121 criterion remains open. The applied carrier bytes, checks and this run record make the predecessor observable on the run branch; D121 does not require a separate carrier merge before the dependent source increment.

Source work remains held pending the safe synchronized basis, exact twelve-locus freeze, accepted PKG02 loci 1–10 return, and explicit HELP_HUMAN source/process release. PKG09 may later write only loci 11–12. Actual unsigned packaged readable multi-page PDF and page navigation under the restrictive policy is mandatory. `inlinePdfPreview` remains `false`; browser load or HTTP 200 is insufficient. Failure keeps published capability false, and success qualifies only unchanged exact candidate bytes.

Lifecycle stays `IN_PROGRESS`; Checking Approval SHA remains `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`. No dependency closure, supplier acceptance, signing, publication, distribution, release readiness or official release is asserted.

## Failed preparation retained

V1 manually transcribed the wrong DEL-09-06 status postimage hash into two evidence files. No carrier had been applied at detection. `pkg09-d121/V1_FAILURE_NOTICE.md` records the cause and withdraws v1. Only v2 identity/application records are valid. A later coordination message also misstated the DEL-02-03 hash; CHANGE stopped before mutation, checked the live bytes, and received the corrected full hash. Machine records and direct-byte verification govern over chat abbreviations.
