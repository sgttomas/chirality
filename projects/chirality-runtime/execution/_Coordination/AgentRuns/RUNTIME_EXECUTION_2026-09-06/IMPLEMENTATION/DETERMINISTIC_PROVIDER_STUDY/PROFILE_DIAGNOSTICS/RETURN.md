# Selected native profile diagnostic observer

Parent requested diagnosis of the exact second discovery's profile-readback mismatch. The driver now records the trusted expectedPermissions and selected profile ID, then attaches a read-only bounded stdout observer. For at most four config responses it records only result.config.permissions[selectedProfile], permission-table presence/counts, scalar allow_login_shell/approval_policy, boolean feature flags, and a count of remaining config fields. Unknown whole config values and prompts are not retained. Profile recursion/string/key counts are bounded and credential-shaped key values redacted. The actor independently retains exact equality and malformed-protocol rejection; diagnostics confer no authority and change no permission.

No vendor invocation performed by this author. Fixture-only check: 2 pass, 1 vendor skip. Parent owns fresh-directory discovery rerun. Final tiny count guard ensures the four-response bound even when responses share one transport chunk. Prior seals are unchanged.

Attribution: OpenAI GPT-6, exact model ID unavailable; ephemeral Agent 2, role not mechanically enforced.
