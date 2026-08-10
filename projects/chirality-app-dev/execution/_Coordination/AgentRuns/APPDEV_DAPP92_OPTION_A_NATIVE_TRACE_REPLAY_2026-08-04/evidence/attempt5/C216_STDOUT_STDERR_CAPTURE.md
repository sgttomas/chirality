# C216 stdout/stderr capture identity

Status: `COMPLETE TOOL CAPTURE — DURABLE RAW-BYTE FILE NOT AVAILABLE`

C216 was invoked exactly once by the governed execution tool. Its combined
stdout/stderr was returned in two terminal chunks:

- chunk `929110`: 6,324 tokens reported by the execution tool;
- chunk `dd5a16`: 303 tokens reported by the execution tool and terminal exit
  code `0`.

The executor inspected the complete returned bytes. Relevant verbatim lines
from the capture were:

```text
> chirality-frontend@2.0.0 desktop:pack
> npm run build && npm run build:runtime-helper && CSC_IDENTITY_AUTO_DISCOVERY=false electron-builder --mac --arm64 --dir --publish never && npm run desktop:verify-dependencies && npm run instruction-root:integrity
  • packaging       platform=darwin arch=arm64 electron=43.2.0 appOutDir=dist-runtime-helper/mac-arm64
  • using custom electronDist zip file  zipFile=/private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip
  • skipped macOS application code signing  reason=, see https://electron.build/code-signing CSC_IDENTITY_AUTO_DISCOVERY=false
  • packaging       platform=darwin arch=arm64 electron=43.2.0 appOutDir=dist/mac-arm64
  • using custom electronDist zip file  zipFile=/private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip
  • skipped macOS application code signing  reason=, see https://electron.build/code-signing CSC_IDENTITY_AUTO_DISCOVERY=false
> chirality-frontend@2.0.0 desktop:verify-dependencies
> node ./scripts/verify-packaged-dependency-boundary.mjs
  "status": "PASS",
  "localPackageEntries": 0,
  "forbiddenDevelopmentPackagesPresent": [],
  "failures": []
> chirality-frontend@2.0.0 instruction-root:integrity
> node ./scripts/verify-instruction-root-integrity.mjs
instruction-root integrity status: pass
checked files: 43
source completeness status: needs_remediation
git sha: 7aada3fbadf340a07ef828cc18b350c8c01b517d
```

No `download`, DNS, `ENOTFOUND`, remote URL fetch, or other network-attempt
indicator appeared in either captured chunk. Both electron-builder package
stages explicitly reported use of the approved local archive.

The execution tool's returned bytes were not redirected by the frozen C216
command and its completed session cannot be reopened. Consequently an exact
durable raw-byte file and SHA-256 cannot honestly be asserted after the fact.
This is an evidence-durability variance, not a runtime or cleanup failure. The
package hashes, public plist output, symlink topology, standalone/embedded
comparison, exit code, and exact cleanup proof are independently durable in
the sibling Attempt-5 evidence files.
