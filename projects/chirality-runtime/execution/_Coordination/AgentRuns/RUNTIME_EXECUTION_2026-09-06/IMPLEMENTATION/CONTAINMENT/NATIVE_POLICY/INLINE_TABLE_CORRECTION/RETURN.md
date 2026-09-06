# Exact CLI parser correction

Parent discovery3 found the dedicated App Server's -c parser splits dotted CLI keys without honoring quoted filesystem path segments. The previous dotted permissions/project overrides therefore did not define the intended keys, including root/.codex. This is an observed parser incompatibility, not a successful policy application.

Compiler now emits one permissions={profile={filesystem={path="deny",...},network={enabled=false}}} inline TOML value and one projects={path={trust_level="trusted"}} value. Path strings are quoted inside TOML values; no path is embedded in the CLI dotted key. Recursive serializer uses TOML equals, not JSON object colons. expectedPermissions and semantic digest remain unchanged; actual readback must still confirm decoded profile equivalence and reject extras or unsupported defaults. No authoritative loader-replacement guarantee is inferred from this implementation alone.

features.remote_plugin=false is now explicit, alongside plugins=false. Native compiler test verifies single whole-table overrides and absence of path-bearing dotted overrides; daemon TypeScript build passes. Parent notified ready before sealing for exact vendor rerun. No vendor/account/network operation occurred here.
