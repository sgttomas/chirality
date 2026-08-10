# D-APP-94 Option C manager validation

Status: `PASS_STATIC_PRE_FREEZE`

- owner capture: two complete LF-terminated stdout objects, each 54 bytes and
  SHA-256 `99563436b11d637838e83d3750afbe806eeab9c8c29dc7d860704e2f1da43953`;
  two `0\n` status objects, each SHA-256
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`;
- restoration: exact one-element search list and default literal
  `/Users/ryan/Library/Keychains/login.keychain-db`; driver revalidates both
  responses and filesystem existence before mutation and re-compares both after
  restoration;
- driver syntax: `/bin/zsh -n` PASS;
- driver fail-closed handling: explicit failures and idempotent
  EXIT/INT/TERM/HUP trap restore while mutated/not-restored, record the retained
  fixed root, and perform no failure deletion;
- Electron archive: exists at 122090802 bytes, SHA-256
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`;
- Electron executable member: exact archive path, 33968 bytes, SHA-256
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`;
- probe source: activation policy prohibited, no BrowserWindow, one public
  constant, no ciphertext/key/item/environment/memory output;
- empty password: public zero-length mechanics only; disposable safeStorage key
  classified as generated cryptographic probe state, not owner/provider
  credential;
- owner keychain exposure: path/default/search-list only; no item enumeration,
  unlock, password, deletion, or probe use;
- output: every returned raw primary, including SHA-output primaries, receives
  an adjacent whole-file SHA sidecar;
- successful deletion: only after exact restoration proof and then-produced
  evidence copy/hash; failure retains exact root/keychain/evidence;
- scope: no Chirality product/source/binary, package, trace, C1114/C1117,
  C196/C197, debugger, network, GUI window, reliance, Git, Task Management, or
  foreign-loop operation.

Only static parsing, hashing, archive-member listing/stream hashing, and
filesystem existence classification were performed during preparation. No
future packet operation executed.
