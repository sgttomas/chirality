# Approval test lifetime repair

Parent PR737 Linux CI release: tests/delegated-runtime.test.ts only plus evidence. OpenAI GPT-6 specialist, exact serving ID unavailable; Agent2 instruction-asserted, not mechanically enforced. No product/authority/Git/account/provider changes.

Live source fixture slow worker exits after 900ms, maxRunMs2000. Approval test polls for registration then performs durable/API assertions that may exceed remaining lifetime on CI. Replace only this test's worker with an explicit host-controlled release-file handshake. Actual ProcessSupervisor/private RPC/public daemon remain. Bounded worker watchdog remains; test releases only after approval assertions then awaits successful terminal and stale-binding rejection. Failure interrupts exact turn and joins, falling back to owned supervisor close if admission is already lost. Preserve production live checks and all existing assertions. Capture CI failure evidence and run focused controlled socket/process checks.
