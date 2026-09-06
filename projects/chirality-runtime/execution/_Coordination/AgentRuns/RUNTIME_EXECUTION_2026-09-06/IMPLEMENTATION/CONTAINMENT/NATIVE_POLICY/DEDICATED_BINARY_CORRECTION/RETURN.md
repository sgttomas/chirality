# Dedicated exact-binary invocation correction

Parent identified the prior reviewer assertion about a required app-server subcommand as incorrect. The accepted supply is a dedicated App Server executable. SUPPLY_PROBE/interactive.py invokes that executable directly with configuration flags; it is not the general Codex CLI.

launchArguments again returns [verifiedExecutablePath,...args] without a subcommand. Consumer notified. No vendor execution occurred here. Earlier extension statements asserting the subcommand was correct are retained as historical error, superseded by this correction.
