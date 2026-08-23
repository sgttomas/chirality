# Pre-full-suite semantic freeze

- Exact frontend tree: `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- R20/status/TM deterministic binary-diff concatenation: 27,465 bytes, SHA-256 `c4781102cff88dd7ca9216cda604400c70bf895ec9a451b0d86825831d34fc25`.
- R20 SHA-256: `f21831c0ac7e5827dcaf610049dad8e0af2e64b476ae4126ae827380ae922161`.
- `_STATUS.md` SHA-256: `d7e3846cfdc105d06145751f2355cef7fb0447c855fd0086f79d1d1bf34862e4`.
- TM candidate SHA-256: `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.

## Frozen source/test/package SHA-256

```text
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  scripts/verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  scripts/pack-electron-with-supply.mjs
f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306  scripts/run-packaged-launchagent-login-proof.mjs
6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18  src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531  fixture
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  electron/runtime-host.ts
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  runtime-host socket-path test
79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874  packaged main executable
0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989  packaged runtime CLI
```

No source/test/package change is authorized between the ordinary-sandbox diagnostic and the sole local-socket cure.
