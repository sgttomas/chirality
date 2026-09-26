# Manager integration observations during source authoring

These are in-progress integration feedback, not independent review or executed findings. Writers remain responsible for final code and tests; closure requires candidate-bound verification after resource release.

- F observer initially checked token presence ahead of stale generation/revision. An old visible queue entry could therefore retain queued standing after model replacement. Requested stale expiration priority while preserving already observed commits and rejected states.
- F preview must validate response batch ID and initial hash against frozen input, plus absence of apply/acceptance, before issuing a usable preview reference.
- Native registration readiness may precede frontend invoke Promise resolution. F must buffer early requests/cancellation while registration is pending, then admit only the exact installed app/controller/registration. N keeps stable dispatch correlation. Failed partial listener setup must clean up; no fourth command is introduced.
- New submit must respect in-flight operation/project ownership. Historical same-key/status recovery must run before this new-work admission gate.
- Normalized Save adoption invokes commitModel and clears queue/history without necessarily advancing project generation. Pending invalidation cannot depend only on advanceProjectSession; observed committed ticket history survives those cell resets.

No source content was changed by manager in these writers' files. Feedback was sent through parent coordination to the owning TASKs.
