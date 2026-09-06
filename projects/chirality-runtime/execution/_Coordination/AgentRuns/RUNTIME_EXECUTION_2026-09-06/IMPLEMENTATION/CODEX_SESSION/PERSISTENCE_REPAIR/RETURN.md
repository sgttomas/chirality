# Durable thread persistence repair

Fresh review found ephemeral:true incompatible with supervisor retirement after every turn and successor thread/resume. startThread now explicitly sends ephemeral:false. No other production actor behavior changed.

Validation: workspace typecheck PASS;12 session tests PASS (680ms). New regression launches first actual controlled child, creates durable thread/store, runs and terminalizes its first turn, kills/reaps that process, starts a distinct child/actor, resumes from the same private persisted file, and completes durable-turn-2. The fixture rejects ephemeral:true, so the pre-repair actor fails this test. Both children are reaped and isolated fixture store removed. No real vendor account/network or observed0.149 successful-turn claim.

Previous actor/test bytes are losslessly retained as PRE_PERSISTENCE.gz; older LOGIN and diagnostic seals remain historical. Current exact source hashes are in this directory's OUTPUTS.sha256. OpenAI GPT-6 bounded Agent2, exact serving model ID unavailable; role instruction-asserted/not mechanically enforced, no delegation.
