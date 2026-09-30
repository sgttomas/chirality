# Build-packet postcheck provenance

The parent packet includes the raw files already present in the job controller
folder when ROOT exported it. `controller-POSTCHECK.raw.json` is explicitly the
TASK’s **pre-retry permission-timeout** postcheck: no process had started at
that time. It is preserved historical evidence, not a check of ROOT’s later
successful build. The one-shot controller does not itself write a postcheck.

After the successful build, ROOT independently rehashed all 47 job-spec inputs
before producing `RESULT.json`; its `inputs_reverified_after` field records
that check, with the executable/lock/fingerprint results alongside it. The
exact loop and result are retained in the host-tool transcript. This new
`CURRENT_PRESERVATION_CHECK.json` supplies another explicit per-file witness
after the partial B runs, with its own timestamp. All 47 hashes still match.
It is not relabelled as the earlier observation. No compiler/model was rerun;
no parent raw output, result, seal or source byte was changed.
