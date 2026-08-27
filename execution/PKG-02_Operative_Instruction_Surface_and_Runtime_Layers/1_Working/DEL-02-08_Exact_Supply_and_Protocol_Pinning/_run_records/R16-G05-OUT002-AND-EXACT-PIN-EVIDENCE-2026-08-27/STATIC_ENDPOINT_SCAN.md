# Exact-Pin Static Endpoint Scan

- **Payload:** App Server 0.149.0 arm64 at SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`
- **Method:** `/usr/bin/strings -a`, URL-like token extraction, bytewise sort
- **Disposable complete scan:** 180 rows, SHA-256
  `9955c5cc39b0b64921f344b340e0af19dc4378023b91ab8307419c77a252a55f`
- **Epistemic class:** `STATIC_STRING_OBSERVATION_NOT_ENDPOINT_ENUMERATION`

Relevant exact strings include:

- `https://auth.openai.com`
- `https://auth.openai.com/api/accounts`
- `https://auth.openai.com/oauth/token`
- `https://auth.openai.com/oauth/revoke`
- `https://api.openai.com/auth`
- `https://api.openai.com/profile`
- `https://api.openai.com/v1`
- `https://chatgpt.com/oauth/codex/`
- `https://chatgpt.com/backend-api`
- `https://chatgpt.com/backend-api/`
- `https://chatgpt.com/backend-api/codex`
- `https://chatgpt.com/codex/settings/usage`

The same payload also contains staging, legacy, example, documentation,
telemetry, plugin, and dynamically formatted URL strings. Static presence
does not prove that a destination is used by an account, model, or turn
operation; adjacent concatenated strings do not prove path boundaries; and
the scan cannot prove that runtime URL construction is exhausted. Therefore
none of the strings above is promoted to an exact account/model/turn policy
row. They are preserved solely as evidence that a static attempt was made.
