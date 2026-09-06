# Immutable native-policy fixture platform calibration

The three drift fixtures operate on the real root-owned macOS SSL file and macOS native-policy compiler. They now run only on darwin. Their mocked opened-fd owner/mode and pathname-replacement checks remain unchanged. Other platforms explicitly assert native policy rejection before macOS filesystem access. No production platform guard was changed or bypassed.

Local macOS result:3 PASS,1 unsupported-platform case intentionally skipped. Actual Linux execution of that case remains the parent CI job's responsibility; no Linux pass is claimed here. CI previously failed because the correct unsupported-platform error arrived before the macOS-only assertions.

Source frozen; parent aggregate/CI and whitespace presentation packaging remain pending. OpenAI GPT-6 WORKING_ITEMS; exact serving ID unavailable; role not mechanically enforced.
