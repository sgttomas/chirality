# Actual B1 routing outcome

This is derivative evidence transcribed from parent HELP_HUMAN's actual tool-event report; it is not a Root ruling or a copied private message payload. Destination task: `dev - runtime`, ID `01a07343-cc53-70e1-80a6-b108c8f9a750`.

The initial detailed send_message_to_thread attempt was rejected by automatic approval review because destination trust was uncertain and the content included nonpublic project details. That attempted message was not sent. The parent then verified the already public D120 ruling using unauthenticated curl against raw GitHub at commit c34bca30c57ef0f36de25d8065b8c1944431d48c. Its SHA-256 matched 35587f5b9a018a7e263518f13c164ce0300518b4f4009b1a0c6725d215801ebc.

The safer retry sent only public PR735/ruling links and the B1 contract-design request to the same task. The tool returned that thread ID, establishing successful delivery. No private content was sent. Delivery requests a design under the runtime owner's own authority; it does not accept a no-folder design, alter runtime/session/project identity, change filesystem permissions, or complete App no-folder behavior.

Public context: https://github.com/sgttomas/chirality/pull/735 and the D120 ruling under projects/chirality-app-dev/execution/_Coordination/_DECISIONS/ at public source commit c34bca30c57ef0f36de25d8065b8c1944431d48c. Exact user publication and CI-green merge authorization is preserved in PR/merge body per parent report. This record does not enlarge that authorization to later local commit e00238621db7a00b036245962c21e3fc6ed75452 or source/evidence payloads.
