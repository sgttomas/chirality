import { createHash } from 'node:crypto';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

/** One action-register row; missing columns are written empty. */
export type AmendmentActionRow = Partial<
  Record<'AmendmentID' | 'ActionSeq' | 'ActionType' | 'EntityType' | 'EntityID' | 'ScopeChanging', string>
>;

export interface AmendmentRecordsInput {
  /** The `_ScopeChange/` folder to write into. */
  scopeChangeRoot: string;
  /** Base the group-2 manifest's register path is written relative to. */
  manifestBase: string;
  amendmentId?: string;
  rows: readonly AmendmentActionRow[];
  /** Include the `ScopeChanging` column (false writes a legacy register). */
  scopeColumn?: boolean;
  /** Checkpoint groups with a decision snapshot; group 3 records acceptance. */
  groups?: readonly ('1' | '2' | '3')[];
}

export interface AmendmentRecords {
  registerPath: string;
  registerSha256: string;
  snapshotDir: string;
  group3Dir: string;
}

/**
 * Writes one amendment's scope-change records in the layout the amendment
 * check reads: a snapshot folder with `Amendment_Actions.csv`, and
 * `checkpoint_snapshots/<ID>_GROUP-<n>_2026-09-26/` decision folders whose
 * group-2 `ACCEPTED_MANIFEST.csv` binds the register by SHA-256.
 */
export async function writeAmendmentRecords(input: AmendmentRecordsInput): Promise<AmendmentRecords> {
  const amendmentId = input.amendmentId ?? 'SCA-001';
  const columns = ['AmendmentID', 'ActionSeq', 'ActionType', 'EntityType', 'EntityID'];
  if (input.scopeColumn !== false) {
    columns.push('ScopeChanging');
  }
  const lines = [columns.join(',')];
  for (const row of input.rows) {
    lines.push(columns.map((column) => row[column as keyof AmendmentActionRow] ?? '').join(','));
  }
  const register = `${lines.join('\n')}\n`;
  const registerSha256 = createHash('sha256').update(register).digest('hex');

  const snapshotDir = path.join(input.scopeChangeRoot, `${amendmentId}_2026-09-26_1200`);
  const registerPath = path.join(snapshotDir, 'Amendment_Actions.csv');
  await mkdir(snapshotDir, { recursive: true });
  await writeFile(registerPath, register, 'utf8');

  const manifestPath = path.relative(input.manifestBase, registerPath).split(path.sep).join('/');
  const snapshots = path.join(input.scopeChangeRoot, 'checkpoint_snapshots');
  for (const group of input.groups ?? ['1', '2', '3']) {
    const folder = path.join(snapshots, `${amendmentId}_GROUP-${group}_2026-09-26`);
    await mkdir(folder, { recursive: true });
    await writeFile(
      path.join(folder, 'DECISION.md'),
      `# ${amendmentId} checkpoint group ${group} — accepted fixture\n\nFixture decision.\n`,
      'utf8'
    );
    const manifestRows = ['Path,SHA256,Role,AcceptanceBoundary'];
    if (group === '2') {
      manifestRows.push(`${manifestPath},${registerSha256},exact final action register,Accepted`);
    }
    await writeFile(path.join(folder, 'ACCEPTED_MANIFEST.csv'), `${manifestRows.join('\n')}\n`, 'utf8');
  }
  return {
    registerPath,
    registerSha256,
    snapshotDir,
    group3Dir: path.join(snapshots, `${amendmentId}_GROUP-3_2026-09-26`)
  };
}
