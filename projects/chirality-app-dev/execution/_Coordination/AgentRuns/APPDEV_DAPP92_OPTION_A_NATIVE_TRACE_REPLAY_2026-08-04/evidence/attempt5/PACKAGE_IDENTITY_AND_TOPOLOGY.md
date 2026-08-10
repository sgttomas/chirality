# Attempt 5 package identity and topology

Status: `CAPTURED BEFORE MANDATORY CLEANUP`

## C179 package hashes

| Package path | SHA-256 |
|---|---|
| `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service` | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar` | `85eac95d186524180975ae99eefab0a0db8f5818913e3a063fbb90e6531ed16c` |
| `dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist` | `5306990501a6e68611a0f0c4967ec4a60f03fc36180b46b01be9846934e9df2d` |
| `dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality` | `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874` |
| `dist/mac-arm64/Chirality.app/Contents/Resources/app.asar` | `e5efe64bb821be178e13ff40793203aabe2e04da2fdb8bb88fe1f6b236116a33` |

## C180 helper public plist output

The public identity/posture fields were:

```text
CFBundleDisplayName = Chirality Runtime Service
CFBundleExecutable = Chirality Runtime Service
CFBundleIdentifier = com.chirality.app.runtime-helper
CFBundleName = Chirality Runtime Service
CFBundleShortVersionString = 2.0.0
CFBundleVersion = 2.0.0
LSMinimumSystemVersion = 15.0.0
LSUIElement = true
NSHighResolutionCapable = true
NSPrincipalClass = AtomApplication
```

`ElectronAsarIntegrity[Resources/app.asar]` used SHA256 hash
`255e95a8e5763754331cedc79168bd049fb1f96f17cb5ce6ddf821d8193cf9bd`.
The default-app asar hash was
`553d6dd413d71a62ae1e67b1db59bd83fadf16ae529f015415dce85787ea437b`.

## C181 GUI public plist output

The public identity/posture fields were:

```text
CFBundleDisplayName = Chirality
CFBundleExecutable = Chirality
CFBundleIdentifier = com.chirality.app
CFBundleName = Chirality
CFBundleShortVersionString = 2.0.0
CFBundleVersion = 2.0.0
LSMinimumSystemVersion = 15.0.0
NSHighResolutionCapable = true
NSPrincipalClass = AtomApplication
```

`ElectronAsarIntegrity[Resources/app.asar]` used SHA256 hash
`3ad9ba702460b0ff847ba59953532dccd5d01bff83a6868d9c2db2a8ecd4ad91`.
The default-app asar hash was
`553d6dd413d71a62ae1e67b1db59bd83fadf16ae529f015415dce85787ea437b`.

## C182-C183 helper symlink topology

| Relative symlink path under helper app | Target |
|---|---|
| `Contents/Frameworks/Electron Framework.framework/Electron Framework` | `Versions/Current/Electron Framework` |
| `Contents/Frameworks/Electron Framework.framework/Resources` | `Versions/Current/Resources` |
| `Contents/Frameworks/Electron Framework.framework/Versions/Current` | `A` |
| `Contents/Frameworks/Electron Framework.framework/Libraries` | `Versions/Current/Libraries` |
| `Contents/Frameworks/Electron Framework.framework/Helpers` | `Versions/Current/Helpers` |
| `Contents/Frameworks/ReactiveObjC.framework/Resources` | `Versions/Current/Resources` |
| `Contents/Frameworks/ReactiveObjC.framework/ReactiveObjC` | `Versions/Current/ReactiveObjC` |
| `Contents/Frameworks/ReactiveObjC.framework/Versions/Current` | `A` |
| `Contents/Frameworks/Squirrel.framework/Resources` | `Versions/Current/Resources` |
| `Contents/Frameworks/Squirrel.framework/Versions/Current` | `A` |
| `Contents/Frameworks/Squirrel.framework/Squirrel` | `Versions/Current/Squirrel` |
| `Contents/Frameworks/Mantle.framework/Mantle` | `Versions/Current/Mantle` |
| `Contents/Frameworks/Mantle.framework/Resources` | `Versions/Current/Resources` |
| `Contents/Frameworks/Mantle.framework/Versions/Current` | `A` |

All 14 targets are relative. No absolute symlink target was observed.

## C184 standalone/embedded comparison

Exact command exit: `0`.

No file-difference line was emitted. The only diagnostics were the documented
`Directory loop detected` messages on corresponding standalone and embedded
framework paths for Electron Framework `Helpers`, `Libraries`, `Resources`,
and `Current`, plus Mantle, ReactiveObjC, and Squirrel `Resources`/`Current`.
The comparison therefore supports byte-equivalent standalone and embedded
helper trees within the command's documented loop-diagnostic semantics.
