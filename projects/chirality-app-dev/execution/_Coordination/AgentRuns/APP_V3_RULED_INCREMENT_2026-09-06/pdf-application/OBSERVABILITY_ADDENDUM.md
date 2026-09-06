# Observability clarification — application-return Step 5

This addendum corrects the overly broad possible reading of APPLICATION_RETURN.md Step 5; the original return remains immutable. It adds no gate and changes no accepted design or patch.

LOOP_INIT.md Step 1 expressly states: “Owner acts, rulings, and routed Root notices are observable only on origin/main (after git fetch). A predecessor item is observable once its commit, checks, and run record are on the run’s branch (Step 4), so a chain of dependent items proceeds within one run without a merge between links.” Backticks omitted in quotation only.

The owner accepted the exact D121 design and exact three-surface amendment. Once that governing owner ruling is observable on freshly fetched origin/main, application of those already accepted bytes is an implementation/record predecessor, not a second owner act. The exact accepted patch requires the carrier amendments accepted and observable under the owner ruling; it does not explicitly require another carrier merge. The recorded owner mapping requires main observability, carrier application and an exact brief, without adding carrier-main wording. No consulted authoritative source requires separately merging the applied carrier bytes before the product brief.

Correct sequence: governing D121 owner ruling on freshly fetched main → parent releases exact carrier application → owning package managers apply exact patch, perform checks and write run records → those application commits/checks/run records become observable on the run branch → parent checks actual Depends/Dependencies/accepted closure and freezes/releases the bounded source brief. No merge between the carrier-application predecessor and source increment is required solely by D121. Any genuinely new owner choice still must follow its own main-observability gate.

Thus read Step 5’s “both carriers and governing ruling meet main-observability requirements” as: governing ruling meets the owner-act main gate; carrier application meets the run-branch predecessor evidence rule. It must not be used to invent an additional carrier merge. Current preparation remains complete; no carrier/source application is released or performed by this addendum.

Sources: projects/chirality-app-dev/loop/LOOP_INIT.md Step 1; exact accepted CANDIDATE.patch SHA e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32; new-run OWNER_RULING_v1.md mapping 6. Parent raised the ambiguity; SCOPE_CHANGE confirms the narrower controlling rule.
