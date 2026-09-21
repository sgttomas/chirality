Rule adopted mid-pass (RUN_BASIS Addendum 6, CONVENTIONS §2.4): the legacy-versus-live subject test for R4-Q1 applies to your forward pass if you have not yet sealed it.

If you have NOT yet sealed your ledger (sealing = validator PASS and the SHA-256 recorded as final), apply the four points below to every row before sealing. If you HAD already sealed it before reading this message, do not edit it; say so in your return and keep going. Either way, state in your pass-1 return whether this notice arrived before or after you sealed.

Legacy-versus-live subject test (R4-Q1), verbatim from CONVENTIONS §2.4:

1. **Decide the subject from the claim text, not from where the code lives.** The subject is
   *product behaviour* if the claim names the App, the system, the user, a session, a turn or
   an agent run; states an observable outcome (something allowed, blocked, recorded, shown or
   sent); or states a guarantee or control (permission, path containment, hooks, redaction,
   approval), even when the text also names the component meant to provide it. The subject
   is *the module* only if the claim names a specific code unit (class, function, file, tool
   or API) and describes only that unit's own contract (inputs, outputs, structure), with no
   outcome the product can observe.
2. **If the text supports both readings, treat it as product behaviour** and judge it on the
   live path (§2.3).
3. **R4-Q1 is cited by evidence, not by opinion.** Cite `R4-Q1` in HumanDecisionNeeded on every
   row where the only code meeting the claim is tagged `REACH=LEGACY_ONLY`, whether the row is
   judged on the live path or at module level. Rows met by `LIVE` code, and rows with no code
   evidence, do not cite R4-Q1 for this reason.
4. **Record the other reading.** On a product-behaviour row met only by legacy code, add
   `ALSO_MODULE:<verdict>` to Notes, giving the verdict a module-level reading would have
   produced.

The rest of your brief is unchanged.
