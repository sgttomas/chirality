# Attempt 8 R6 proposal sources

Proposal-only static artifacts for command-register v1.21. These bytes carry
no execution authority and remain unhashed until independent manager freeze.

The directory contains exactly ten `.mjs` proposal scripts plus this README.
It repairs only the four findings in the immutable v1.20 verifier return:
immediate C847 target guard, error-versus-drained-close settlement, accepted
C1018/no-close fail-closed proof, and accepted-C1009-gated C1014 with trapped
stdin stream/callback errors. No proposed script was executed by the author.
