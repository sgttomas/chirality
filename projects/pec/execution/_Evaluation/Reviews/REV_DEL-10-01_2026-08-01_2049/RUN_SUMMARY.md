# Run summary — DEL-10-01 SELF_CHECK

The valid `SOW_V1` contract compiled to eight exact `AC-*` criteria. All eight
were populated in order. Exact telemetry arithmetic reproduces input
`5,691,203`, cached-input subset `5,440,768`, output `22,436`, logical total
`5,713,639`, and uncached input `250,435`. The five-run latency arithmetic
reproduces median `2.78 s`, range `2.64..3.34 s`, and mean `2.854 s`. Strict
decomposition-register validation passes with 64 registers, 254 rows, and zero
findings.

Seven criteria are mechanically addressed. AC-008 is `PARTIAL` pending the
owner's fitness and pre-P1 confirmation. SELF_CHECK recorded one MAJOR
`AGENT_CHECK` finding, RF-001: present-tense candidate/pending-acceptance prose
must be normalized before accepting exact artifact hashes, or the accepted
bytes would immediately contain false status claims. Proposed disposition is
`REVISE`; human disposition remains `TBD`. Recommendation: `RECOMMEND_HOLD`.
