"""T4-RV4 addendum 01: re-run T4-I8's round-01 scripts and compare their outputs byte for byte.

Usage: python -I reproduce_i8_r01.py <T4-I8 dir> <SOURCE_ODWALL_EXPECTATIONS.json> <frozen round-00 json>
                                     <T1 generate_reference_values.py> <empty scratch dir>
Prints only file names, digests and verdicts (no paths).
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    i8, fixture, frozen, t1gen, out = (Path(a) for a in sys.argv[1:6])
    out.mkdir(parents=True, exist_ok=True)
    print("fixture sha256", sha(fixture))
    print("frozen round-00 json sha256", sha(frozen))
    print("T1 generator sha256", sha(t1gen))
    ok = True
    for line in (i8 / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split(None, 1)
        good = sha(i8 / name) == digest
        ok &= good
        print("SHA256SUMS", name, "OK" if good else "MISMATCH")
    print("SHA256SUMS file digest", sha(i8 / "SHA256SUMS"))
    for script in ("derive_rebuilt_references.py", "check_reference_json.py", "t1_generator_probe.py"):
        shutil.copy(i8 / "_run_records" / script, out / script)
    runs = {
        "derive": [sys.executable, "-I", "derive_rebuilt_references.py", str(fixture.resolve()), "rebuilt_reference_cases.json"],
        "check": [sys.executable, "-I", "check_reference_json.py", "rebuilt_reference_cases.json", str(frozen.resolve())],
        "probe": [sys.executable, "-I", "t1_generator_probe.py", str(t1gen.resolve()), "rebuilt_reference_cases.json"],
    }
    codes = {}
    for name, cmd in runs.items():
        r = subprocess.run(cmd, cwd=out, capture_output=True)
        (out / f"{name}.stdout.txt").write_bytes(r.stdout)
        codes[name] = r.returncode
        print(name, "exit", r.returncode)
    pairs = [("rebuilt_reference_cases.json", i8 / "rebuilt_reference_cases.json"),
             ("derive.stdout.txt", i8 / "_run_records" / "derive_rebuilt_references.stdout.txt"),
             ("check.stdout.txt", i8 / "_run_records" / "check_reference_json.stdout.txt"),
             ("probe.stdout.txt", i8 / "_run_records" / "t1_generator_probe.stdout.txt")]
    for mine, theirs in pairs:
        same = (out / mine).read_bytes() == Path(theirs).read_bytes()
        ok &= same
        print("byte-equal" if same else "DIFFERS", mine, sha(out / mine))
    print("python", sys.version.split()[0])
    ok &= all(c == 0 for c in codes.values())
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
