# Exact final package manifest

Status: `STRUCTURAL PASS / D-APP-88 ACCEPTANCE BLOCKED`

## Identity and topology

- GUI bundle identifier: `com.chirality.app`.
- Helper bundle identifier: `com.chirality.app.runtime-helper`.
- Helper `LSUIElement`: `true`.
- Exactly one top-level `.app` exists in GUI `Contents/Library/LoginItems`.
- Four builder-generated child apps use `com.chirality.app.runtime-helper.helper`, `.helper.GPU`, `.helper.Plugin`, and `.helper.Renderer`.
- Standalone and embedded helper each contain 812 descendants: 446 regular files, 352 descendant directories, and 14 symbolic links.
- `diff -qr` returned exit 0. Its only diagnostics were expected macOS framework directory-loop notices caused by relative framework symlinks.
- All 14 symlinks are relative; zero absolute symlinks.

## Critical SHA-256 values

| Surface | SHA-256 |
|---|---|
| Standalone helper executable | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| Embedded helper executable | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| Standalone helper `app.asar` | `cc67632d39422e555c378328a4b8b7f51910b23a885f1181fafa9a8052362687` |
| Embedded helper `app.asar` | `cc67632d39422e555c378328a4b8b7f51910b23a885f1181fafa9a8052362687` |
| Standalone helper `Info.plist` | `7984df499ae7fd3f54c49072770cb3c6263148e7a760fb704c2ad88ea25b7f7d` |
| Embedded helper `Info.plist` | `7984df499ae7fd3f54c49072770cb3c6263148e7a760fb704c2ad88ea25b7f7d` |
| GUI executable | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| GUI `app.asar` | `f78a5e3c0cb749ddcc01ad266f275c85a96fa272d97ad1f3bd0ef5f5237159b8` |
| Packaged runtime CLI | `3adc8490634427b814cbebbf93563851f0794f59715b82d4b26415a5aa0cc9a4` |
| Packaged Claude platform executable | `2f8413ea1083f108587940496a17057751344109d261fb4239ab2d45b2285c99` |
| Packaged instruction-root `AGENTS.md` | `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb` |

The clean fully materialized validation projection produced no builder `cannot find path for dependency` messages. Packaged dependency boundary passed, and instruction-root integrity passed over 43 files with the independent `needs_remediation` source-completeness advisory retained.
