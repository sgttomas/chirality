# Published CAEPIPE benchmark agreement

<!-- policy-text -->
This folder is the one public place for benchmark agreement between SWBPIPE and CAEPIPE
(`docs/IP_AND_DATA_BOUNDARY.md` §6.2; DEL-17-05 `Design/caepipe-correlation-pilot.md` §8.1). A report here
may state agreement and differences on the benchmark set's non-code mechanical outputs, the tolerances and
decision rules applied, the model and case counts, and the CAEPIPE version. It never states CAEPIPE's defects,
crashes, trial limits, evaluation stamp or performance, and carries no screenshots, survey notes or
user-interface critique. CAEPIPE's output files and the result values parsed from them stay private.

Nothing is published here before the owner rules the external-oracle tolerance class. `publication.json`
carries that gate: `tolerance_class_ruled` stays `false` until the ruling, and setting it `true` records the
ruling's date (`ruled_on`) and the repository path of the text that records it (`recorded_in`).

Agreement on the benchmark set is not acceptance, validation of a user's design, code compliance or
compatibility, and it issues or releases nothing. Reliance on SWBPIPE's results stays with the user;
acceptance, issuance and release remain the owner's acts.
<!-- /policy-text -->
