import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";

const electronDist =
  "/private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip";

const targets = [
  {
    path: "electron-builder.runtime-helper.json",
    before: "bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982",
    after: "1cb9e4c7325166f69139eeba3a0bdfcfa1d4f871e03acf4af1809aa88fa02a36",
    apply: (value) => {
      value.electronDist = electronDist;
    },
  },
  {
    path: "package.json",
    before: "7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15",
    after: "b53a867e8aa7d8874cf7ce2417691a05d449babaa9bf0b905c550deb13b3ac6d",
    apply: (value) => {
      value.build.electronDist = electronDist;
    },
  },
];

const digest = (bytes) => createHash("sha256").update(bytes).digest("hex");

for (const target of targets) {
  const beforeBytes = readFileSync(target.path);
  const before = digest(beforeBytes);
  if (before !== target.before) {
    throw new Error(`${target.path}: unexpected pre-overlay SHA-256 ${before}`);
  }

  const value = JSON.parse(beforeBytes.toString("utf8"));
  target.apply(value);
  const afterBytes = Buffer.from(`${JSON.stringify(value, null, 2)}\n`);
  const after = digest(afterBytes);
  if (after !== target.after) {
    throw new Error(`${target.path}: unexpected post-overlay SHA-256 ${after}`);
  }
  writeFileSync(target.path, afterBytes);
  process.stdout.write(`${after}  ${target.path}\n`);
}
