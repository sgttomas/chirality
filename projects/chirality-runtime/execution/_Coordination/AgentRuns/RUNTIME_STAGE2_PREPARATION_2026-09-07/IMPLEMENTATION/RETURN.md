# Stage2 candidate SOW refreeze — Agent2 return

Status: FROZEN_FOR_INDEPENDENT_REVIEW. Preparation only; neither live SOW was modified or accepted. Two complete postimages and CANDIDATE.patch bind exact live preimages through POSTIMAGE_INDEX.json.

Accepted upstream is the decomposition at actual commit `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, its `CUSTODY_DISPOSITION_D36.md` companion, and SCA-001 as accepted by `execution/_ScopeChange/ACCEPTANCE_SCA001_STAGE1_2026-09-06/OWNER_ACCEPTANCE.md`. Exact inputs are in INPUT_PINS.json. Historical candidate/pending language in the decomposition and earlier SCA records is preserved and interpreted with that later Stage1 acceptance. The prior CORRECTION_V2 step 5 supplies the refreeze sequence; prior DOWNSTREAM_SOW is derivative input, not acceptance authority. Both candidate decomposition_basis fields now resolve to the actual committed decomposition bytes, verified using read-only git show.

## Exact deltas and semantic review

- DEL-02-06: preserve the earlier REQ-041 custody supplement, replace only decomposition_basis and qualify its reciprocal references as `DEL-02-09/REQ-001` and `DEL-02-09/REQ-002`. The earlier space-separated references were ambiguous with DEL-02-06's own local requirements. No requirement is renumbered or reassigned.
- DEL-02-09: preserve the earlier REQ-001/002 supplements, replace only decomposition_basis, qualify `DEL-02-06/REQ-041`, and restore the accepted companion's exact one OpenAI sign-in target with independent folder consent and the caveat that documentation does not prove the actual multi-root experience. The prior `DEL-02-06 REQ-041` was deterministically an unresolved local REQ-041 under the SOW parser; qualification fixes that error without inventing a DEL-02-09 requirement.
- Authority for the cross-deliverable meanings is `CUSTODY_DISPOSITION_D36.md` under “Exact interpretation of inherited requirements”: DEL-02-06 REQ-041 and DEL-02-09 REQ-001/002. Authority for the added target/caveat is that section's second paragraph. This restores an omitted accepted target; it neither establishes readiness nor grants live sign-in. No broader policy or architecture is proposed.

## Validation and preservation

Both actual candidate directories passed `validate_scope_of_work.py --json` as SOW_V1 with no issues. The validator and common parser were read before execution; Python -B/PYTHONDONTWRITEBYTECODE suppressed out-of-scope bytecode writes. No interpreter dependency failure occurred in this child. Its checks cover schema, local IDs, required sections, and output/acceptance/method matrix references; they do not establish substantive acceptance.

CHECKS.json records all inherited local definitions (including OUT, REQ, AC and VER where present), unchanged 52+6 requirement definitions, unchanged objectives and all frontmatter except the basis, and byte-identical procedure and evaluation-matrix sections. Removing exactly the custody supplement ranges and restoring the old basis reconstructs each current live SOW byte-for-byte. Thus all unrelated content, lifecycle cautions, nine holds, REQ-027, root-runtime-1 epoch 1 and R16-B remain intact. Existing method/procedure sections remain valid as inherited production/evidence instructions; logout ordering is the separately supplemented product boundary, not an invented production authorization. No new procedure, criterion or residual is created.

The exact patch passed read-only `git apply --check`; read-only tracked diff remained empty. INPUT_PINS.json records 54 inputs including all seven statuses, contexts and dependency files. All seven statuses remain INITIALIZED; absence of Remaining sections is preserved. No product test, build, supplier, network, credential, protected-fixture, Git mutation or live/source operation was performed. Rehashing all input pins at freeze passed.

## Handoff state

This packet is a derivative candidate package, not replacement decomposition truth. Bounded preparation is complete, subject to fresh independent review. Stage2 application, final acceptance, owning SCA/derivative closure, any Root adoption, and publication remain ungranted. No lifecycle advancement, hold release or product completion is asserted. Supplier identity, exact keyring/isolation/UX qualification and human-assurance questions remain outside this work.

Next owner: WORKING_ITEMS validates this return and routes the exact frozen postimages for independent review and later owning application authority. Rerun/refreeze on any preimage or accepted-basis drift, review finding requiring edits, or changed propagation authority; do not amend this frozen packet. Earlier candidates remain immutable. Parent owns manager telemetry and fan-in. Actual executor: bounded ephemeral Agent2, nondelegating, instruction-asserted; OpenAI GPT-6 attribution, exact serving identifier and token/context measurements unavailable.
