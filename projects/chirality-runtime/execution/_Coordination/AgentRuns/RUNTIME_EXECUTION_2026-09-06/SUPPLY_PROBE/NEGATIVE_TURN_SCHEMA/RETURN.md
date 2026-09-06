# Negative turn request shape diagnostic

Parent explicitly authorized this additional bounded negative probe. OpenAI GPT-6 ephemeral Agent 2; exact serving ID unavailable, role instruction-asserted and not mechanically enforced. No delegation.

Same original accepted 0.149.0 payload, hard-deny sandbox, disposable HOME with no credentials. A fresh UUID was generated locally and never returned by thread/start. No thread creation request was sent in this process. The only requests after initialization were one turn/start against that nonexistent ID with input [{type:"text",text:"Offline nonexistent-thread request shape probe."}].

Exact response: code -32600, `thread not found: b7397d51-2bce-4783-b91a-53bc23dca6ad`. This establishes that this minimal text request parsed and reached thread lookup. No retry was necessary. No successful turn result or turn/item notification was observed; no hosted model execution, login, approval exercise or external connection occurred. No real thread turn was requested.

This is NOT proof of successful turn execution, output-event schema, approval request/response schema, complete serde schema or authenticated behavior. Those gaps remain. The payload SHA-256 after execution remains b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2. Aggregate diagnostic artifact teardown remains pending parent handshake completion.
