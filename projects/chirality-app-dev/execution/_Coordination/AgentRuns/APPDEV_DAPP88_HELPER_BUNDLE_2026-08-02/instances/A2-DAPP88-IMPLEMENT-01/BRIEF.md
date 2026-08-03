# Sealed brief — A2-DAPP88-IMPLEMENT-01

- Parent: `WI-PKG09-DAPP88-B`
- Role: `TASK`
- TaskSkill: `software-bounded-implementation`
- Scope: App-owned Electron packaging/runtime-control surfaces, DEL-09-04 run evidence, and this run root.
- Objective: implement and prove D-APP-88 Option B without Root runtime semantic changes.
- Acceptance: distinct helper identifier/UI posture; LaunchAgent and CLI routing; one daemon/store continuity; relocatable package; stable helper/GUI coexistence; preserved graceful and SIGKILL recovery; full cleanup.
- Stop: any Root runtime change, live owner-keychain prompt, release/signing/distribution effect, or unresolved preservation regression.
