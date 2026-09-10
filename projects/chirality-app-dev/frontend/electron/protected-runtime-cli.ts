import {
  createDefaultCliDependencies,
  processCliIo,
  runCli,
  type CliDependencies,
  type CliIo
} from '@chirality/runtime-cli/dist/src/cli.js';

export type ProtectedRuntimeCliEntry = {
  createDependencies(): CliDependencies;
  io: CliIo;
  run: typeof runCli;
};

const productionEntry: ProtectedRuntimeCliEntry = Object.freeze({
  createDependencies: createDefaultCliDependencies,
  io: processCliIo,
  run: runCli
});

function isDaemonInstall(arguments_: readonly string[]): boolean {
  return arguments_[0] === 'daemon' && arguments_[1] === 'install';
}

function hasExecutableOverride(arguments_: readonly string[]): boolean {
  return arguments_.some(
    (argument) => argument === '--executable' || argument.startsWith('--executable=')
  );
}

/** Run Runtime's real CLI implementation from the protected app.asar closure. */
export async function runProtectedRuntimeCli(
  arguments_: readonly string[],
  desktopExecutable: string,
  packaged: boolean,
  entry: ProtectedRuntimeCliEntry = productionEntry
): Promise<number> {
  if (isDaemonInstall(arguments_)) {
    if (!packaged) {
      entry.io.stderr('daemon install requires a packaged Chirality application.\n');
      return 2;
    }
    if (hasExecutableOverride(arguments_)) {
      entry.io.stderr('daemon install does not accept an executable override.\n');
      return 2;
    }
  }
  const protectedArguments = isDaemonInstall(arguments_)
    ? [...arguments_, '--executable', desktopExecutable]
    : [...arguments_];
  return entry.run(protectedArguments, entry.io, entry.createDependencies());
}
