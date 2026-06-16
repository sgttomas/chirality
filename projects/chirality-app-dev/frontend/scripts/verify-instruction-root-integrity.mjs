#!/usr/bin/env node

import { execSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync } from 'node:fs';
import { mkdir, readdir, readFile, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';

const REQUIRED_ROOT_FILES = [
  'AGENTS.md',
  'README.md',
  'PROFESSIONAL_ENGINEERING.md'
];

const REQUIRED_DOC_FILES = [
  'DIRECTIVE.md',
  'CONTRACT.md',
  'SPEC.md',
  'TYPES.md',
  'PLAN.md',
  'WHAT-IS-AN-AGENT.md'
];

const REQUIRED_UNPACKED_SDK_FILES = [
  'app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/package.json',
  'app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/sdk.mjs',
  'app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/manifest.json'
];

const SDK_PLATFORM_PACKAGE_BY_RUNTIME = new Map([
  ['darwin:arm64', '@anthropic-ai/claude-agent-sdk-darwin-arm64'],
  ['darwin:x64', '@anthropic-ai/claude-agent-sdk-darwin-x64'],
  ['linux:arm64', '@anthropic-ai/claude-agent-sdk-linux-arm64'],
  ['linux:x64', '@anthropic-ai/claude-agent-sdk-linux-x64'],
  ['win32:arm64', '@anthropic-ai/claude-agent-sdk-win32-arm64'],
  ['win32:x64', '@anthropic-ai/claude-agent-sdk-win32-x64']
]);

function toPosix(relativePath) {
  return relativePath.split(path.sep).join('/');
}

function nowIso() {
  return new Date().toISOString();
}

function printUsage() {
  console.log(`Usage: node ./scripts/verify-instruction-root-integrity.mjs [options]

Options:
  --source-root <path>   Monolithic source instruction-root root
  --root-files-root <path>
                         Source root for AGENTS.md, README.md, and PROFESSIONAL_ENGINEERING.md
                         (default: auto-detected monorepo root)
  --agents-root <path>   Source agents directory root (default: <root-files-root>/agents)
  --docs-root <path>     Source docs directory root (default: auto-detected app-dev docs)
  --bundle-root <path>   Packaged Resources root (default: dist/mac-arm64/Chirality.app/Contents/Resources)
  --output-root <path>   Output directory for manifest + summary (default: artifacts/harness/instruction-root-integrity/latest)
  --help                 Show this message
`);
}

function readArgValue(argv, index, flagName) {
  const value = argv[index];
  if (!value || value.startsWith('--')) {
    throw new Error(`Missing value for ${flagName}`);
  }
  return value;
}

function parseArgs(argv) {
  const options = {};

  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];

    if (token === '--help') {
      options.help = true;
      continue;
    }

    if (token === '--source-root') {
      options.sourceRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    if (token === '--root-files-root') {
      options.rootFilesRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    if (token === '--agents-root') {
      options.agentsRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    if (token === '--docs-root') {
      options.docsRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    if (token === '--bundle-root') {
      options.bundleRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    if (token === '--output-root') {
      options.outputRoot = readArgValue(argv, index + 1, token);
      index += 1;
      continue;
    }

    throw new Error(`Unknown argument: ${token}`);
  }

  return options;
}

async function sha256ForFile(absolutePath) {
  const fileBuffer = await readFile(absolutePath);
  const fileStat = await stat(absolutePath);
  if (!fileStat.isFile()) {
    throw new Error(`Expected a file but found non-file entry: ${absolutePath}`);
  }
  return {
    sha256: createHash('sha256').update(fileBuffer).digest('hex'),
    sizeBytes: fileStat.size
  };
}

function readGitSha(sourceRoot) {
  try {
    return execSync('git rev-parse HEAD', {
      cwd: sourceRoot,
      stdio: ['ignore', 'pipe', 'ignore']
    })
      .toString('utf8')
      .trim();
  } catch {
    return null;
  }
}

function hasMonolithicInstructionRootShape(candidateRoot) {
  return (
    existsSync(path.join(candidateRoot, 'agents')) &&
    existsSync(path.join(candidateRoot, 'AGENTS.md')) &&
    existsSync(path.join(candidateRoot, 'docs', 'DIRECTIVE.md'))
  );
}

function hasSplitInstructionRootShape({ rootFilesRoot, agentsRoot, docsRoot }) {
  return (
    REQUIRED_ROOT_FILES.every((fileName) => existsSync(path.join(rootFilesRoot, fileName))) &&
    existsSync(agentsRoot) &&
    REQUIRED_DOC_FILES.every((fileName) => existsSync(path.join(docsRoot, fileName)))
  );
}

function resolveDefaultSourceRoots() {
  const envRoot = process.env.CHIRALITY_INSTRUCTION_ROOT
    ? path.resolve(process.env.CHIRALITY_INSTRUCTION_ROOT)
    : undefined;

  if (envRoot && hasMonolithicInstructionRootShape(envRoot)) {
    return {
      rootFilesRoot: envRoot,
      agentsRoot: path.join(envRoot, 'agents'),
      docsRoot: path.join(envRoot, 'docs'),
      sourceLayout: 'monolithic',
      sourceRoot: envRoot
    };
  }

  const monorepoRoot = path.resolve(process.cwd(), '..', '..', '..');
  const appDevRoot = path.resolve(process.cwd(), '..');
  const splitCandidate = {
    rootFilesRoot: monorepoRoot,
    agentsRoot: path.join(monorepoRoot, 'agents'),
    docsRoot: path.join(appDevRoot, 'docs'),
    sourceLayout: 'split'
  };

  if (hasSplitInstructionRootShape(splitCandidate)) {
    return splitCandidate;
  }

  const candidates = [
    envRoot,
    path.resolve(process.cwd(), '..'),
    path.resolve(process.cwd(), '..', '..', '..')
  ].filter(Boolean);

  const sourceRoot = candidates.find(hasMonolithicInstructionRootShape) ?? candidates[0];
  return {
    rootFilesRoot: sourceRoot,
    agentsRoot: path.join(sourceRoot, 'agents'),
    docsRoot: path.join(sourceRoot, 'docs'),
    sourceLayout: 'monolithic',
    sourceRoot
  };
}

function resolveSourceRoots(args) {
  if (args.sourceRoot) {
    const sourceRoot = path.resolve(args.sourceRoot);
    return {
      rootFilesRoot: sourceRoot,
      agentsRoot: path.join(sourceRoot, 'agents'),
      docsRoot: path.join(sourceRoot, 'docs'),
      sourceLayout: 'monolithic',
      sourceRoot
    };
  }

  const defaults = resolveDefaultSourceRoots();
  const rootFilesRoot = path.resolve(args.rootFilesRoot ?? defaults.rootFilesRoot);
  const agentsRoot = path.resolve(args.agentsRoot ?? defaults.agentsRoot);
  const docsRoot = path.resolve(args.docsRoot ?? defaults.docsRoot);
  const sourceLayout =
    rootFilesRoot === docsRoot && agentsRoot === path.join(rootFilesRoot, 'agents')
      ? 'monolithic'
      : 'split';

  return {
    rootFilesRoot,
    agentsRoot,
    docsRoot,
    sourceLayout,
    sourceRoot: sourceLayout === 'monolithic' ? rootFilesRoot : undefined
  };
}

async function listSourceAgentFiles(agentsRoot) {
  const entries = await readdir(agentsRoot, { withFileTypes: true });

  const agentFiles = entries
    .filter((entry) => entry.isFile() && /^AGENT_.*\.md$/.test(entry.name))
    .map((entry) => entry.name)
    .sort();

  if (agentFiles.length === 0) {
    throw new Error(`No AGENT_*.md files were found in ${agentsRoot}`);
  }

  return agentFiles;
}

async function listBundleAgentFiles(bundleRoot) {
  const agentsDirectory = path.join(bundleRoot, 'agents');
  let entries = [];
  try {
    entries = await readdir(agentsDirectory, { withFileTypes: true });
  } catch {
    return [];
  }

  return entries
    .filter((entry) => entry.isFile() && /^AGENT_.*\.md$/.test(entry.name))
    .map((entry) => toPosix(path.join('agents', entry.name)))
    .sort();
}

async function buildSourceManifest({ rootFilesRoot, agentsRoot, docsRoot }) {
  const sourceAgentFiles = await listSourceAgentFiles(agentsRoot);
  const sourceEntries = [
    ...REQUIRED_ROOT_FILES.map((fileName) => ({
      bundlePath: fileName,
      sourcePath: path.join(rootFilesRoot, fileName)
    })),
    ...REQUIRED_DOC_FILES.map((fileName) => ({
      bundlePath: toPosix(path.join('docs', fileName)),
      sourcePath: path.join(docsRoot, fileName)
    })),
    ...sourceAgentFiles.map((fileName) => ({
      bundlePath: toPosix(path.join('agents', fileName)),
      sourcePath: path.join(agentsRoot, fileName)
    }))
  ];

  const entries = [];
  for (const entry of sourceEntries) {
    const digest = await sha256ForFile(entry.sourcePath);
    entries.push({
      path: entry.bundlePath,
      sourcePath: entry.sourcePath,
      sha256: digest.sha256,
      sizeBytes: digest.sizeBytes
    });
  }

  return entries;
}

async function verifyManifestAgainstBundle({ manifestEntries, bundleRoot }) {
  const missingInBundle = [];
  const mismatchedFiles = [];
  const comparisons = [];

  for (const entry of manifestEntries) {
    const bundleFilePath = path.join(bundleRoot, entry.path);
    try {
      const bundleDigest = await sha256ForFile(bundleFilePath);
      const hashesMatch = bundleDigest.sha256 === entry.sha256;

      comparisons.push({
        path: entry.path,
        sourceSha256: entry.sha256,
        bundleSha256: bundleDigest.sha256,
        sourceSizeBytes: entry.sizeBytes,
        bundleSizeBytes: bundleDigest.sizeBytes,
        match: hashesMatch
      });

      if (!hashesMatch) {
        mismatchedFiles.push({
          path: entry.path,
          sourceSha256: entry.sha256,
          bundleSha256: bundleDigest.sha256
        });
      }
    } catch {
      missingInBundle.push(entry.path);
    }
  }

  const sourceAgentSet = new Set(
    manifestEntries.filter((entry) => entry.path.startsWith('agents/')).map((entry) => entry.path)
  );
  const bundleAgentFiles = await listBundleAgentFiles(bundleRoot);
  const unexpectedBundleAgentFiles = bundleAgentFiles.filter((entry) => !sourceAgentSet.has(entry));

  return {
    missingInBundle,
    mismatchedFiles,
    unexpectedBundleAgentFiles,
    comparisons
  };
}

function resolveSdkPlatformPackageName() {
  return SDK_PLATFORM_PACKAGE_BY_RUNTIME.get(`${process.platform}:${process.arch}`) ?? null;
}

function buildRequiredUnpackedSdkFiles() {
  const platformPackageName = resolveSdkPlatformPackageName();
  const platformPackageCandidates = platformPackageName
    ? [
        `app.asar.unpacked/node_modules/${platformPackageName}`,
        `app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/${platformPackageName}`
      ]
    : [];

  return {
    platformPackageName,
    requiredFiles: [...REQUIRED_UNPACKED_SDK_FILES],
    platformPackageCandidates: platformPackageCandidates.map((root) => ({
      root,
      files: [`${root}/package.json`, `${root}/claude`]
    }))
  };
}

async function verifyUnpackedSdkBundle({ bundleRoot }) {
  const { platformPackageName, requiredFiles, platformPackageCandidates } =
    buildRequiredUnpackedSdkFiles();
  const missingFiles = [];
  const comparisons = [];

  for (const relativePath of requiredFiles) {
    const absolutePath = path.join(bundleRoot, relativePath);
    try {
      const fileStat = await stat(absolutePath);
      const isFile = fileStat.isFile();
      comparisons.push({
        path: relativePath,
        sizeBytes: isFile ? fileStat.size : null,
        present: isFile
      });
      if (!isFile) {
        missingFiles.push(relativePath);
      }
    } catch {
      comparisons.push({
        path: relativePath,
        sizeBytes: null,
        present: false
      });
      missingFiles.push(relativePath);
    }
  }

  const platformCandidateComparisons = [];
  let selectedPlatformPackageRoot = null;

  for (const candidate of platformPackageCandidates) {
    const candidateFiles = [];
    for (const relativePath of candidate.files) {
      const absolutePath = path.join(bundleRoot, relativePath);
      try {
        const fileStat = await stat(absolutePath);
        candidateFiles.push({
          path: relativePath,
          sizeBytes: fileStat.isFile() ? fileStat.size : null,
          present: fileStat.isFile()
        });
      } catch {
        candidateFiles.push({
          path: relativePath,
          sizeBytes: null,
          present: false
        });
      }
    }

    const found = candidateFiles.every((entry) => entry.present);
    platformCandidateComparisons.push({
      root: candidate.root,
      found,
      files: candidateFiles
    });

    if (found && !selectedPlatformPackageRoot) {
      selectedPlatformPackageRoot = candidate.root;
    }
  }

  if (platformPackageName && !selectedPlatformPackageRoot) {
    missingFiles.push(
      `one complete ${platformPackageName} unpacked package under ${platformPackageCandidates
        .map((candidate) => candidate.root)
        .join(' or ')}`
    );
  }

  return {
    platformPackageName,
    selectedPlatformPackageRoot,
    missingFiles,
    comparisons,
    platformPackageCandidates: platformCandidateComparisons
  };
}

async function writeJson(filePath, value) {
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    printUsage();
    return;
  }

  const sourceRoots = resolveSourceRoots(args);
  const bundleRoot = path.resolve(
    args.bundleRoot ?? path.join(process.cwd(), 'dist', 'mac-arm64', 'Chirality.app', 'Contents', 'Resources')
  );
  const outputRoot = path.resolve(
    args.outputRoot ??
      path.join(process.cwd(), 'artifacts', 'harness', 'instruction-root-integrity', 'latest')
  );

  await mkdir(outputRoot, { recursive: true });

  const manifestEntries = await buildSourceManifest(sourceRoots);
  const verification = await verifyManifestAgainstBundle({
    manifestEntries,
    bundleRoot
  });
  const sdkBundleVerification = await verifyUnpackedSdkBundle({ bundleRoot });

  const status =
    verification.missingInBundle.length === 0 &&
    verification.mismatchedFiles.length === 0 &&
    verification.unexpectedBundleAgentFiles.length === 0 &&
    sdkBundleVerification.missingFiles.length === 0
      ? 'pass'
      : 'fail';

  const gitSha = readGitSha(sourceRoots.rootFilesRoot);
  const manifest = {
    generatedAt: nowIso(),
    gitSha,
    sourceLayout: sourceRoots.sourceLayout,
    sourceRoot: sourceRoots.sourceRoot ?? null,
    sourceRoots: {
      rootFilesRoot: sourceRoots.rootFilesRoot,
      agentsRoot: sourceRoots.agentsRoot,
      docsRoot: sourceRoots.docsRoot
    },
    files: manifestEntries
  };

  const summary = {
    generatedAt: nowIso(),
    gitSha,
    sourceLayout: sourceRoots.sourceLayout,
    sourceRoot: sourceRoots.sourceRoot ?? null,
    sourceRoots: {
      rootFilesRoot: sourceRoots.rootFilesRoot,
      agentsRoot: sourceRoots.agentsRoot,
      docsRoot: sourceRoots.docsRoot
    },
    bundleRoot,
    checkedFileCount: manifestEntries.length,
    status,
    missingInBundle: verification.missingInBundle,
    mismatchedFiles: verification.mismatchedFiles,
    unexpectedBundleAgentFiles: verification.unexpectedBundleAgentFiles,
    comparisons: verification.comparisons,
    sdkBundle: {
      platformPackageName: sdkBundleVerification.platformPackageName,
      selectedPlatformPackageRoot: sdkBundleVerification.selectedPlatformPackageRoot,
      requiredFiles: sdkBundleVerification.comparisons,
      platformPackageCandidates: sdkBundleVerification.platformPackageCandidates,
      missingFiles: sdkBundleVerification.missingFiles
    }
  };

  await writeJson(path.join(outputRoot, 'manifest.json'), manifest);
  await writeJson(path.join(outputRoot, 'summary.json'), summary);

  console.log(`instruction-root integrity status: ${status}`);
  console.log(`checked files: ${manifestEntries.length}`);
  if (gitSha) {
    console.log(`git sha: ${gitSha}`);
  } else {
    console.log('git sha: unavailable');
  }
  console.log(`manifest: ${path.join(outputRoot, 'manifest.json')}`);
  console.log(`summary: ${path.join(outputRoot, 'summary.json')}`);

  if (status !== 'pass') {
    if (verification.missingInBundle.length > 0) {
      console.error(`Missing in bundle (${verification.missingInBundle.length}):`);
      for (const filePath of verification.missingInBundle) {
        console.error(`  - ${filePath}`);
      }
    }
    if (verification.mismatchedFiles.length > 0) {
      console.error(`Hash mismatches (${verification.mismatchedFiles.length}):`);
      for (const entry of verification.mismatchedFiles) {
        console.error(`  - ${entry.path}`);
      }
    }
    if (verification.unexpectedBundleAgentFiles.length > 0) {
      console.error(`Unexpected bundled agent files (${verification.unexpectedBundleAgentFiles.length}):`);
      for (const filePath of verification.unexpectedBundleAgentFiles) {
        console.error(`  - ${filePath}`);
      }
    }
    if (sdkBundleVerification.missingFiles.length > 0) {
      console.error(`Missing unpacked Claude Agent SDK files (${sdkBundleVerification.missingFiles.length}):`);
      for (const filePath of sdkBundleVerification.missingFiles) {
        console.error(`  - ${filePath}`);
      }
    }

    process.exitCode = 1;
  }
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`instruction-root integrity verification failed: ${message}`);
  process.exitCode = 1;
});
