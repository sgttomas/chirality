# Handoff — waiting for D-APP-94 Option C owner input capture

State: `WAITING_FOR_OWNER_RETURN`

Accepted authorization:
`INPUT_CAPTURE_AUTHORITY_ADOPTION_V1.md`.

The owner personally runs exactly these two commands, separately and in the
intended security session:

1. `/usr/bin/security default-keychain -d user`
2. `/usr/bin/security list-keychains -d user`

Required return fields for each command:

| Field | Required value |
|---|---|
| command | exact literal command above |
| stdout | complete, unedited stdout bytes |
| exit_status | observed integer exit status |

Do not enumerate keychain items and do not provide a password, credential,
environment dump, process output, or other data. If either command does not
complete, return the command, all stdout actually produced, and its observed
exit status; do not retry or substitute another command.

The existing preparation blocker remains active. No probe packet, freeze,
verifier, or execution token is authorized before this owner return is
validated.
