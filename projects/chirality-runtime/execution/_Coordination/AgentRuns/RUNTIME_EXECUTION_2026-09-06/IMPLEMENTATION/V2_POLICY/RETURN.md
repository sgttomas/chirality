# Return

PASS: 24 tests; contracts/core TypeScript build passes. Four owned source/test outputs are pinned in OUTPUTS.json.

HarnessEventV2 is a discriminated payload union with strict envelope/payload validator, session/model/message/approval lifecycle shapes, and exactly four turn terminals. Projector explicitly handles supported runtime-owned types, strips extra provider fields, and returns content-free quarantine reasons for unsupported/invalid events. Existing v1 remains unchanged. turn.cancelled additive projector input is explicit because old RuntimeEvent union lacks it.

Role evidence offers all five roles independently of model and native descent. Policy digest binds role, instruction-asserted labels, tools and declared containment settings; actual model/provider/adapter remains separate. Digest proves neither containment nor non-delegation. Parent integrates actual current settings and routes; these unit tests do not prove live provider operation or approval delivery.
