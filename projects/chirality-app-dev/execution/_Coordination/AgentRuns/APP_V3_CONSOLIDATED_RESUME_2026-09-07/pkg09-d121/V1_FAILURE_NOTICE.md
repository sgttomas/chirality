# V1 preparation failure notice

Status: `FAILED_SUPERSEDED`; application remains prohibited from v1.

The first preparation packet incorrectly transcribed the accepted DEL-09-06 `_STATUS.md` postimage SHA-256 in `CARRIER_APPLICATION.md` and `PREFLIGHT_AND_IDENTITIES.json` as `0f4b65b53eef04a1108f1cfddc082a98be465e1655faf019c5a98643356f11f25`.

The correct digest, computed directly from retained `pdf-application/DEL09-06_STATUS_POSTIMAGE.txt`, is `0f4b65b53f0e05183fcd8a5f489bb2da8ccdb4ead6fab22944f89f8daf42e6ba`. It agrees with the authoritative preserved `PREPOST_IDENTITIES.json` and with the exact isolated patch result.

Cause: manual transcription introduced a visually similar but unrelated 64-character value instead of mechanically carrying the digest produced from the accepted bytes. The v1 manifest accurately hashes the v1 files but does not validate the truth of the identity written inside them. Therefore the v1 application and identity records are failed preparation evidence and must never be used to apply or validate carriers.

Claim correction: v1's carrier-readiness verdict is withdrawn. Only `CARRIER_APPLICATION_v2.md`, `PREFLIGHT_AND_IDENTITIES_v2.json`, `CHECKS_v2.md`, `MANAGER_RETURN_v2.md`, and `MANIFEST_v2.json` may support the prepared application. No carrier was applied before detection, so no live remediation or rollback is required.
