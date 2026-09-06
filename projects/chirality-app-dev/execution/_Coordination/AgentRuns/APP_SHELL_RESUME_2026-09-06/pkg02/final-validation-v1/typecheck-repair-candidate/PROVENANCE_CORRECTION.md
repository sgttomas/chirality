# Candidate status correction

The removal-only config patch is unapplied. Current installed @chirality symlinks resolve to a preexisting temporary Runtime installation, not the freshly built sibling. CANDIDATE.json describes the intended accepted declaration boundary; it is not an observation that the current links satisfy it. The alignment proposal identifies each link and current sibling declaration hash.

Probe01 used the repository cwd for the compiler host and therefore reports an artificial missing node type. Probe02 corrects cwd to frontend: zero diagnostics, 46 external Runtime declaration inputs, but still the preexisting temporary installation. Neither probe substitutes for registered validation on correctly aligned local dependencies.

The actual registered Electron typecheck has 60 errors in seven current sibling Runtime source files because the tsconfig source aliases combine with Next’s required NODE_ENV ProcessEnv augmentation. Main frontend compiler alone passes. No config/source/types flags or Runtime files were changed.
