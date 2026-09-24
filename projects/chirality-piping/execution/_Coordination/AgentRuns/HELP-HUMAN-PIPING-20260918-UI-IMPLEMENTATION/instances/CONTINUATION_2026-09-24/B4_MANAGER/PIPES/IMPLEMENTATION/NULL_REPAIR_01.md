# Null optional quantity repair

Independent review identified that `null` mill tolerance is accepted as absence by the owned backend but was marked malformed by the Pipe table. The repair excludes raw null from the optional malformed flag. The value remains TBD and the unit remains empty, so both direct and review authoring require explicit value/unit entry. Non-null malformed quantities and numeric quantities without units retain their existing admission checks. Material/Section editing still requires existing finite quantities and actual units.

The UI and operation-adapter regressions now each run for omitted and null slots, asserting explicit-unit requirements, zero authoring, before TBD, direct/review payload or resulting-model equality, and unchanged input state. Source and test identities are preserved in [_run_records/null-repair-01/repair.json](_run_records/null-repair-01/repair.json). Earlier candidate freezes and results are unchanged.

The implementation TASK ran no tests, builds or browser/native operations for this repair. The manager owns affected tests, TypeScript, updated candidate freeze and independent reviewer backcheck.
