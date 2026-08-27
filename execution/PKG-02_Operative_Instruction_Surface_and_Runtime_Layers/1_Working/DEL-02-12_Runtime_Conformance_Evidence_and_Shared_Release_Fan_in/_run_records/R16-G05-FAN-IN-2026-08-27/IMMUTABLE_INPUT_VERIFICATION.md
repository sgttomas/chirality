# R16 immutable-input verification at fan-in

Recomputation after N1–N3 commit
`661174b8834eb795cd368e06dec891caa9b021dc` reproduced every R16 pin.
The complete path/value list remains in the immutable N0 basis record
`execution/_Coordination/AgentRuns/ROOT_V3_R16_G05_SPIKES_2026-08-27/BASIS_AND_INPUT_PINS.md`
at SHA-256
`6e0ad1bafee457053d679c3525b047f18e5ade89b263922b111d50c19a2e648e`.

## Critical identities reverified from current bytes

| Input | SHA-256 |
|---|---|
| R16 ruling | `f1baab4a42874635fef39b8e7f69666d72c588e59056f55a10f2d4aceb9535ef` |
| R16 companion steer | `aa598aea6a125d2e76e3c894e56c784fbddcd51da0484f33bfb42132f2a937ba` |
| release execution plan | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |
| R12 ruling / supply steer / resume steer | `2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd` / `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391` / `248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701` |
| R13 ruling / resume2 steer | `0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960` / `38b76ca27defd39507f6d9cfe9501d392b1e9ade7c5f107cd67cb4ce420ef164` |
| R14 ruling | `2633637bd68c7f4cb54457a3547b2bcab8933f19e021abf558b1ef2463d1b5e9` |
| R15 ruling / G2 steer | `a8463a7f0392978325e8d25558332e72868271e9c4d99ac26c7425bb3a448301` / `a0d14e05b7749c06605bdfce5d978058b4bea999569f94d0a918a5f2bad6eb76` |
| accepted compatibility snapshot | `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4` |
| accepted compatibility JSON | `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c` |
| accepted semantic candidate V2 | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` |
| DEL-02-07 through DEL-02-12 Scopes of Work | `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5`; `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430`; `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176`; `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29`; `abd5dcef7a835bafac3e1dd29d7f7b6771ad0aeb60e4af9c25734bfa2534ab02`; `62bcfbdd6a20b647f15594fdd35b312d62942f85cf96aedb4aae5db12ea04663` |
| workplan pointer / idle workplan | `efaea5b88a58e9fe408efffde3ac92ae3c4ec55fdde43b6c61f8add7d3913776` / `f75497926a2ba74ae9038b4e09a06eb951bb8b86d41d6672894c79e6b9f3318d` |
| Task Management register | `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` |
| accepted config readback / plugin suppression / denied egress / OUT-002 predecessor | `3eea0e0f075a8cbd0f143f5a0bc6b441ddb9691aca4c9a7d1d6d921d42581a93`; `c3024e555589995acc685d2feb15d1ca38db2d4e9fa2855eb1a3f7d4e025928c`; `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513`; `fd6bd4e4dd7c2a0dc477e567becd5d2d092514db36dfedaf2fa2a529798d9f47` |

`origin/main` still equals
`b0d975a9139eddebf5c1e728cf724b55c8a97cad`, with tree
`6a3b804539b6c260abaf2fa62660576deff97250` and ordered parents
`b9960755bb7cbeed02e69591a2fcd51eaf2caf60`,
`f291bfe4600c1f2cbf36ab103a3f78106ff620ce` at the last remote fetch.

The complete branch diff is confined to Receipt 131, the new DEL-02-06 R16
successor packet, new R16 evidence packets in DEL-02-07/08/09/10/12, and the
single Root run directory. No accepted snapshot, compatibility JSON, G2
packet, Scope of Work, workplan, pin, register, runtime, tool, App, Piping,
Tier-0, agent-instruction, or prior immutable record path appears as a
modification.

`TM-ROOT-106` and `TM-ROOT-122` still parse as `OPEN` with no disposition or
closure act. The workplan remains idle.
