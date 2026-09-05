# Parent-authorized boundary clarification v1.3

D-APP-64 ordinary reconciliation, explicitly approved by HELP_HUMAN: target section12 says Remove nothing. Preserve existing opaque properties during seed-only compatibility patch, including a pre-existing activeChatRoot key; never read it into normalized state, infer a root from it, or introduce that key. Explicit normal writer must omit activeChatRoot. The contract concerns application semantic state; no claim that arbitrary pre-existing raw storage is scrubbed. This preserves non-destructive read migration and excludes active-root authority from convenience state.

Same two-file fence. Extend existing seed-only regression to include a pre-existing activeChatRoot value; assert raw preservation and normalized exclusion. Existing explicit-writer omission regression must remain. No product algorithm change expected unless these checks reveal a defect. Focused rerun and updated freeze required before fresh review; retain prior evidence.
