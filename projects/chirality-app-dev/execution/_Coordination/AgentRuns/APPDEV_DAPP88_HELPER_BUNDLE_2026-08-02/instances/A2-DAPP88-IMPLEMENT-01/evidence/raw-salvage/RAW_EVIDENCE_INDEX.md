# Raw evidence index — D-APP-88 helper investigation

This index binds the sanitized evidence salvaged before deletion of the exact
temporary drill trees. The keyword scan for `token`, `authorization`,
`api key`, `secret`, `password`, and `bearer` returned no matches before these
files were retained. No owner credential or token bytes are present here.

## Package structure evidence

These files came from the last diagnostic package, whose `app.asar` included
the temporary SIGUSR2 diagnostic. They support only the recorded plist,
Mach-O, and relative-symlink structure claims; they are **not** an exact frozen
copy of the source-aligned candidate package.

| File | SHA-256 |
| --- | --- |
| `PACKAGED_HASHES.txt` | `69578f43b8b57e84feb4ea2720b0ab309a0222ef3eb2ce3d4fe4485eb09c5093` |
| `PLIST_EXTRACTS.txt` | `84fbc1499ef120f504cd487f9a1bff25c15f0b1d48c0a6b4cf85c5321bf08920` |
| `RELATIVE_SYMLINK_CENSUS.txt` | `1049cdf45db6749dabcf29e71dffaef45e9a74bd098baa76a04c90a27e24185f` |
| `plists/gui.Info.plist` | `01de8962983e0a3a39443a1fe88fc9b8c739159a0896729bf1e80c393456b4dc` |
| `plists/helper.Info.plist` | `2f2d3fa66703adb20c0413be1fe3ddaa27a32d165472c0998f60692849fc2144` |
| `plists/child.Info.plist` | `afab4cfbe34103fe7aa498019dbe100af8d626dabbda138edc99bbd12811783d` |

## Runtime logs

| File | SHA-256 |
| --- | --- |
| `logs/childicu-desktop-daemon.log` | `61b18bc66298ac726400c81ac195234f31acf77e78a40361eaf0e711fab47145` |
| `logs/childres-desktop-daemon.log` | `be8dbb2c502621753b81982934a575f393e5f0f52454717a2386a830089ab32a` |
| `logs/final-desktop-daemon.log` | `e9f016c6c12be37494c1ebd93716d44caa43b266a9fb0c718d754c6c69b94a70` |
| `logs/flags-desktop-daemon.log` | `fd6b054fa3bfcf647d13df5790024eb69a96b4adc2908ef08face4f06c2c6760` |
| `logs/frameworkid-desktop-daemon.log` | `eb1a6785c46236e0cd0cf013bf81072390f03e75a45a6abc8922f249908aa8ed` |
| `logs/gui-control-desktop-daemon.log` | `97ee67b1fc56fdbed1a4da792f9823f4d327a331040cdeac9c406d71dc52bb3e` |
| `logs/gui-control.stdout.log` | `7ddd44d7a391c65e01e5d87321e0ad9312db19ac8d503f99b5e017fa99004adc` |
| `logs/helper-escalated-desktop-daemon.log` | `7019b1d90d13de85dee0a45aec461a4d349d6593b1d754d4193013bce056c093` |
| `logs/helper-escalated.stderr.log` | `857c54be3bcfbfcfea4f7e1db0b4534df32e9989b3f100b42151c4b25202784c` |
| `logs/helper-escalated.stdout.log` | `74e41dd0b05dbd63ad231438f413ac8b1fb7da45f6cf294ae40544bd5b686461` |
| `logs/helper-loginitem.stderr.log` | `e75fefee561af17840030f17b3f83c6106ead59b8a6cf5835efad82f16a5690d` |
| `logs/helper-valid.stderr.log` | `de4f379a10b6430b0bc1498106a34f0d97a7ff1de1cb24f595a9780b0989a9b4` |
| `logs/trace-desktop-daemon.log` | `a726180ea236cf5e86446c1a9f8854d7e6260e87edc395c077b3517795521e26` |

## Transcript recovery boundary

`RECOVERED_TRANSCRIPT_EXCERPTS.md`
(`d0a954f1a3e6d928314c9ab22dd035138a9101172a1f8f80445a1e40618f03aa`)
contains sanitized excerpts copied from retained terminal tool outputs. The
later final-run raw terminal streams were not independently retained before
their temporary trees were removed, so this file supports only the bounded
observations it quotes: socket-ready state, CLI/owner PID agreement, concurrent
GUI/owner PID observations, clean fresh shutdown, failed post-GUI shutdown,
SIGUSR2 suppression, and SIGKILL recovery. It does not recreate missing raw
transcripts or establish durations beyond the quoted observations.
