"""T4-RV4: re-run T4-I8's own scripts and compare their outputs byte for byte.

Usage: python -I reproduce_i8.py <T4-I8 dir> <SOURCE_ODWALL_EXPECTATIONS.json> <empty scratch dir>
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
    i8, fixture, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    print("fixture sha256", sha(fixture))
    # SHA256SUMS of the frozen set
    lines = (i8 / "SHA256SUMS").read_text().splitlines()
    ok = True
    for line in lines:
        digest, name = line.split(None, 1)
        good = sha(i8 / name) == digest
        ok &= good
        print("SHA256SUMS", name, "OK" if good else "MISMATCH")
    print("SHA256SUMS file digest", sha(i8 / "SHA256SUMS"))
    for script in ("derive_rebuilt_references.py", "check_reference_json.py"):
        shutil.copy(i8 / "_run_records" / script, out / script)
    derive = subprocess.run([sys.executable, "-I", "derive_rebuilt_references.py", str(fixture.resolve()), "rebuilt_reference_cases.json"],
                            cwd=out, capture_output=True)
    (out / "derive.stdout.txt").write_bytes(derive.stdout)
    check = subprocess.run([sys.executable, "-I", "check_reference_json.py", "rebuilt_reference_cases.json"], cwd=out, capture_output=True)
    (out / "check.stdout.txt").write_bytes(check.stdout)
    pairs = [("rebuilt_reference_cases.json", i8 / "rebuilt_reference_cases.json"),
             ("derive.stdout.txt", i8 / "_run_records" / "derive_rebuilt_references.stdout.txt"),
             ("check.stdout.txt", i8 / "_run_records" / "check_reference_json.stdout.txt")]
    print("derive exit", derive.returncode, "check exit", check.returncode)
    for mine, theirs in pairs:
        same = (out / mine).read_bytes() == Path(theirs).read_bytes()
        ok &= same
        print("byte-equal" if same else "DIFFERS", mine, sha(out / mine))
    print("python", sys.version.split()[0])
    print("RESULT:", "PASS" if ok and derive.returncode == 0 and check.returncode == 0 else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
