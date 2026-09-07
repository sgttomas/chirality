# Test log original-byte reference resolution

TEST_LOG_ORIGINAL_BYTES.json preserves all original bytes of CI_FAILURE_REPAIR/AUTHOR/TEST_OUTPUT.log in base64. The raw log is excluded from this Git publication and remains unchanged locally. Its historical manifest reference resolves through this archive, not an assertion that the raw path exists in the published tree.

Decode the data field strictly, require 1068 bytes and SHA256 4fb1c597ebf131ea70446b39eee46ce4654fafdc332be8256d46b80fb8bd2b1c, and reconstruct originalPath only in owned scratch when validating the historical manifest. Do not overwrite newer repository state. The exact log's surplus terminal blank line is preserved; no normalization, attributes change, test change or authority substitution occurs. Structured command/result/validation receipts remain published directly. This is a derivative representation of the original evidence, not a replacement acceptance act.
