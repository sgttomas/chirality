import { mkdir, mkdtemp, realpath, rm, symlink, utimes, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { observeSignedAppFiles, revalidateObservedSignedAppFiles } from "../packages/daemon/src/host-account-release.js";

const cleanups: Array<() => Promise<void>> = [];
afterEach(async () => { while (cleanups.length) await cleanups.pop()!(); });

/** An Electron-style bundle: the framework binary is reached through two symlinks (`Current` and the leaf). */
async function bundle() {
  const root = await realpath(await mkdtemp(join(tmpdir(), "signed-app-")));
  cleanups.push(() => rm(root, { recursive: true, force: true }));
  const appRoot = join(root, "Chirality.app"), contents = join(appRoot, "Contents");
  const frameworkDir = join(contents, "Frameworks", "Electron Framework.framework");
  await mkdir(join(frameworkDir, "Versions", "A"), { recursive: true });
  await mkdir(join(contents, "MacOS"), { recursive: true }); await mkdir(join(contents, "Resources"), { recursive: true });
  await writeFile(join(frameworkDir, "Versions", "A", "Electron Framework"), "framework");
  await symlink("A", join(frameworkDir, "Versions", "Current"));
  await symlink("Versions/Current/Electron Framework", join(frameworkDir, "Electron Framework"));
  await writeFile(join(contents, "MacOS", "Chirality"), "executable"); await writeFile(join(contents, "Info.plist"), "plist"); await writeFile(join(contents, "Resources", "app.asar"), "asar");
  const paths = [join(contents, "MacOS", "Chirality"), join(frameworkDir, "Electron Framework"), join(contents, "Info.plist"), join(contents, "Resources", "app.asar")];
  return { root, appRoot, frameworkDir, paths };
}

describe("signed-app file observation", () => {
  it("follows the Electron framework symlinks to the regular file inside the bundle and revalidates by identity", async () => {
    const b = await bundle();
    const observed = await observeSignedAppFiles(b.appRoot, b.paths);
    expect(observed.map(file => file.path)).toEqual(b.paths);
    expect(observed[1]!.resolvedPath).toBe(join(b.frameworkDir, "Versions", "A", "Electron Framework"));
    await expect(revalidateObservedSignedAppFiles(observed, "TRIAL_SEAL_SUBJECT_CHANGED")).resolves.toBeUndefined();
  });
  it("rejects a re-pointed symlink and a rewritten target", async () => {
    const b = await bundle();
    const observed = await observeSignedAppFiles(b.appRoot, b.paths);
    await writeFile(join(b.frameworkDir, "Versions", "A", "Electron Framework"), "framework!");
    await expect(revalidateObservedSignedAppFiles(observed, "TRIAL_SEAL_SUBJECT_CHANGED")).rejects.toMatchObject({ details: { reason: "TRIAL_SEAL_SUBJECT_CHANGED" } });
    const again = await observeSignedAppFiles(b.appRoot, b.paths);
    await mkdir(join(b.frameworkDir, "Versions", "B")); await writeFile(join(b.frameworkDir, "Versions", "B", "Electron Framework"), "framework");
    await rm(join(b.frameworkDir, "Versions", "Current")); await symlink("B", join(b.frameworkDir, "Versions", "Current"));
    await expect(revalidateObservedSignedAppFiles(again, "TRIAL_SEAL_SUBJECT_CHANGED")).rejects.toMatchObject({ details: { reason: "TRIAL_SEAL_SUBJECT_CHANGED" } });
  });
  it("refuses a file that resolves outside the bundle or is missing", async () => {
    const b = await bundle();
    const outside = join(b.root, "outside"); await writeFile(outside, "x");
    await rm(join(b.frameworkDir, "Electron Framework")); await symlink(outside, join(b.frameworkDir, "Electron Framework"));
    await expect(observeSignedAppFiles(b.appRoot, b.paths)).rejects.toMatchObject({ details: { reason: "PACKAGED_APP_PATH_INVALID" } });
    await expect(observeSignedAppFiles(b.appRoot, [join(b.appRoot, "Contents", "missing")])).rejects.toMatchObject({ details: { reason: "PACKAGED_APP_PATH_INVALID" } });
  });
});
