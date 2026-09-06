# Integration v2 review gate

Frozen input: integration-01/SOURCE_MANIFEST_v2.json, SHA256 e0db67285c8ee327ba981069f49e33986a687d9efb14c6a086c75f54ef9de8e1, all 24 source/test members from base e00238621db7a00b036245962c21e3fc6ed75452. Independent source review and browser execution each verified unchanged hashes and stayed in their evidence scope.

Source review terminated BLOCK with one actionable finding: persona change released a completed conversation's folder lock. See source-review-03/RETURN.md, SHA256 558b0126de201fbda67ee3d548a5ce31e259f2177eb53e44a78db243d13aca41. No other actionable source finding was reported after full-diff inspection.

Browser checkpoint independently found expanded Settings intercepting its own toggle. The earlier container-width assertion was an evaluator mistake, preserved separately; corrected message reading width is 620px and strip height is 32px. Development tools were hidden through their own session preference, without product changes. Remaining matrix stopped on the real interaction defect. Browser and owned server cleanup and port refusal were verified before source release.

Manager disposition: reject v2 implementation acceptance and return exactly these two defects to the sole author under integration-01/REMEDIATION_v3_BRIEF.md. No source, lifecycle, dependency or publication acceptance follows from this gate. A complete revised freeze, fresh independent full-diff review, browser/native evidence and final checks remain required. Native preparation is only preparation, with no execution claim.

The user's visual direction confirmation remains the composition baseline. The repair must not introduce unrelated restyling, persist session authority, disable intended persona selection after a turn, or change the no-folder restriction. Per-historical-chat Reveal remains separate from current-root Reveal.
