# Amendment 05 — owner-authorized record-only EOF repair

- Date: `2026-08-23`.
- Authority: exact owner approval in `CHAT_TRANSCRIPTION.md`.
- Write set: only the terminal byte of these three prior-validator files: `instances/A2-PKG09-R20-PHASEB-VALIDATE-02/ACTIVATION.md`, `RETURN.md`, and `VALIDATION.md`.
- Preimages: `3c50905cd730925da6ccf9374b8880a09c48b893b2ac2effb5795f2789ec2cb2`, `9620af4620e4cbaae32ce22e06b2cc214b81149fc67542a2d340278ce322caaf`, and `ef06190377bbba777089b70635575ff3e67642fadbf62eb40f3b161d6cd76440`; each ends in exact bytes `0a0a`.
- Exact repair: remove only the final `0a` from each file, leaving one final newline. Record byte counts and pre→post SHA-256; substantive content must compare byte-for-byte after appending one LF to each postimage.
- Preserve unchanged: historical executor `RETURN.md` 16,439 bytes / `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`; raw pack log 15,852 bytes / `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`; all other accepted raw evidence; R20/status/TM semantic hashes.
- After repair, run only gates still unreached at VALIDATE-03 and then a genuinely fresh overall review. No prior/one-shot command rerun.
- Any failed gate stops. No stage, commit, fetch, push, PR, merge, Receipt 191, proof, operator/private evidence, network, signing, distribution, deployment, or release action is authorized here.
