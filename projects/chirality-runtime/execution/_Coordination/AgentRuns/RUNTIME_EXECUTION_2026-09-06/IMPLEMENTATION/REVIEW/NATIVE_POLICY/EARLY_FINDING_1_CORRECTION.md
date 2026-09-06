# Correction — exact App Server executable argv

Early finding 1 was incorrect and is withdrawn. I inferred ordinary Codex CLI behavior without verifying the exact accepted executable identity. The accepted supply is the dedicated `app-server` executable, not a multi-command Codex CLI. `SUPPLY_PROBE/interactive.py:4–7` pins SHA256 b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2 and invokes that binary directly followed by `-c` overrides under the experimental sandbox wrapper. Therefore the native launch's direct binary invocation was not defective for the missing subcommand I alleged. Adding `app-server` was an incorrect recommendation and must be removed for this exact pin.

Original finding and source hashes remain preserved as historical review evidence. Manager reports the wrong subcommand likely caused an initial discovery startup failure; that causal attribution requires the actual discovery record, not this reviewer's inference. No failed discovery is reclassified. This error demonstrates why exact local executable/schema evidence must precede generic CLI assumptions.

OpenAI GPT-6; exact serving ID unavailable; role instruction-asserted, not mechanically enforced. No code change or vendor execution in this correction.
