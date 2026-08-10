# D-APP-93 R4.4 simplification authority adoption

Parent: `HELP_HUMAN`

Manager: `WORKING_ITEMS`

Status: `ADOPTED — SOLE INTEGRATION OWNER ACTIVE`

Accepted predecessor basis:

- Receipt 138;
- R4.3 freeze SHA-256
  `7f4a9858f8ba2947ce1db522f82669678369b0a4ac3f09a20a5c66bc7747ddf1`;
- sealed verifier brief SHA-256
  `de76cb3615e067a31f71cf5914c5d052869d51abf7eb11b9e02b06901ace866f`;
- accepted verifier `BLOCK_PACKET_REPAIR_REQUIRED` return SHA-256
  `a4c09714934163edd6181e5b932a20593bad1a98dab8ff8219fe5902b0a1e386`;
- R4 validation / manager return / handoff SHA-256 identities
  `cbde53e4242c79778b8566ea10d6c043f5cbfbf8b70d429b9bbfd7d1e1039779`,
  `ed56476fd48ab736be6b307d9804328d09b66000d53be6831b726ece5999f94f`,
  and `9aab0c44a102949988b97fb057784a17a875046ef36404fef83fb3bbe51b8f3c`.

## Verbatim latest owner token relayed by HELP_HUMAN

> OWNER AUTHORITY RESUMES D-APP-93. Adopt verbatim the latest user token as a new versioned authority record. Act as sole WORKING_ITEMS integration owner for R4.4 simplification. Exact scope:
> 1. Replace C1154-C1156 and EVERY in-runbook parsing/manifest/range/hash-crosscheck/terminal-verdict operation with plain enumerated raw-byte capture, whole-file `/usr/bin/shasum -a 256`, and `/bin/cp -p` to exact returned destinations. Future runbook command bytes for these evidence steps may contain NO awk/sed/grep/jq/python/node/perl field extraction, loops, functions, case/if/for/while, command substitution, pipelines for derived parsing, or conditional logic. Do not create/assume helper scripts.
> 2. Move all manifest derivation, range indexing, completeness checking, exit-code enforcement (including exact command_exit=0 and tee_exit=0 if tee remains, crosschecked to PASS dispositions), and terminal verdict to the later loop-side INGESTION/VALIDATION contract over returned immutable raw bytes. The packet/runbook produces raw bytes/hashes only and makes no PASS verdict.
> 3. Re-author EVERY failure route over the reduced command set with satisfiable prerequisites, explicitly covering pre-C1070, partial C1070, incomplete baseline, post-first-write/pre-C196, post-C196, returned-path occupied, prohibited content, copy/hash failure, cleanup/rollback failure. Eliminate step-5 and universal pre-C1070 contradictions.
> 4. Preserve C196/C197 exact bytes/status and ordinary C1145→C1144→C1130 order. Preserve unaffected prepared bytes exactly. Update only owner-listed affected ledger/runbook/evidence/ingestion/range/token/index/freeze/crossrefs/control records. No product/runtime/etc/Git/Task Management/foreign-loop action.
> 5. Start with durable authority adoption + work-graph amendment. You may use a read-only EVALUATION manager only if essential, but no Agent2 verifier before stable freeze. Produce exact command inventory, exhaustive branch/precondition + required-raw-byte producer/return matrix, mechanical checks, and immutable successor freeze. Report hashes to HELP_HUMAN BEFORE verifier dispatch. Do not dispatch verifier until I explicitly accept the freeze.

## Adopted boundary

No execution authority is inferred. This adoption authorizes only the bounded
R4.4 prepared/control-byte repair and static validation named above. It does
not authorize packet execution, product/runtime work, a verifier before freeze
acceptance, or any other effect.
