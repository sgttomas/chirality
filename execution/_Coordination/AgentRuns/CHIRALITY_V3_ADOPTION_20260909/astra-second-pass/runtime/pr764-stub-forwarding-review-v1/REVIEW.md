# Stub argument forwarding — PASS

Independent TASK reviewer `/root/astra_runtime_second_pass`, gpt-6-astra/high. No actionable findings in the complete one-file diff against `cf15e194a35539f4dcc099f2878b2e470f4d8203`.

`startRuntimeTurn` now forwards the original `contentBlocks` and `turnId` as arguments four and five, matching the existing Legacy adapter calling convention. The two new optional parameters preserve three-argument callers. They remain unused by the deterministic simulation; stream output, permission markers, context-required rejection, and real provider paths are unchanged.

The existing `routes.test.ts` attachment assertion at line 1027 is byte-identical to the base. It observes argument four and validates both attachment warnings and usable content; forwarding restores the actual seam without weakening that assertion. Forwarding the turn ID does not claim new stub lifecycle attribution.

Exact base/current/diff and unchanged-test hashes are in `SUBJECT.json`. Static review PASS; manager owns the ongoing full App tests/typecheck and final CI confirmation. No reviewer test/provider/native run or source edit.
