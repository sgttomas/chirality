import { mkdtemp, mkdir, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { scanDeliverableDocumentKitContract } from '../../lib/workspace/filesystem';

let tmpRoot = '';
let deliverablePath = '';

function statusDocument(state = 'IN_PROGRESS'): string {
  return `# Status: DEL-07-03 Deliverable Contract Scanner

**Current State:** ${state}
**Last Updated:** 2026-06-21

## History
- 2026-06-21 - State set to ${state} (WORKING_ITEMS)
`;
}

async function writeDeliverableFiles(files: Record<string, string>): Promise<void> {
  for (const [fileName, content] of Object.entries(files)) {
    await writeFile(path.join(deliverablePath, fileName), content, 'utf8');
  }
}

beforeEach(async () => {
  tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-deliverable-contract-scanner-'));
  deliverablePath = path.join(
    tmpRoot,
    'PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies',
    '1_Working',
    'DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts'
  );
  await mkdir(deliverablePath, { recursive: true });
});

afterEach(async () => {
  await rm(tmpRoot, { recursive: true, force: true });
  tmpRoot = '';
  deliverablePath = '';
});

describe('scanDeliverableDocumentKitContract', () => {
  it('accepts complete metadata, document-kit, and canonical-memory files', async () => {
    await writeDeliverableFiles({
      '_STATUS.md': statusDocument('IN_PROGRESS'),
      '_CONTEXT.md': '# Context\n',
      '_DEPENDENCIES.md': '# Dependencies\n',
      '_REFERENCES.md': '# References\n\n| RefID | Status |\n|---|---|\n| REF-001 | MATCH |\n',
      '_SEMANTIC.md': '# Semantic\n',
      'Datasheet.md': '# Datasheet\n',
      'Specification.md': '# Specification\n',
      'Guidance.md': '# Guidance\n',
      'Procedure.md': '# Procedure\n',
      'MEMORY.md': '# Memory\n'
    });

    const result = await scanDeliverableDocumentKitContract({
      deliverableId: 'DEL-07-03',
      deliverablePath
    });

    expect(result.valid).toBe(true);
    expect(result.lifecycleState).toBe('IN_PROGRESS');
    expect(result.errorCount).toBe(0);
    expect(result.warningCount).toBe(0);
    expect(result.requiredMetadata.every((file) => file.present)).toBe(true);
    expect(result.preparationBaseline.every((file) => file.present)).toBe(true);
    expect(result.documentKit.every((file) => file.present)).toBe(true);
    expect(result.canonicalMemory.present).toBe(true);
    expect(result.optionalFiles.every((file) => !file.present)).toBe(true);
    expect(result.findings).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          category: 'canonical_memory',
          condition: 'canonical_memory_present',
          severity: 'info'
        })
      ])
    );
  });

  it('reports missing metadata, missing kit files, prohibited memory, and source-state warnings', async () => {
    await writeDeliverableFiles({
      '_STATUS.md': statusDocument('INITIALIZED'),
      '_DEPENDENCIES.md': '# Dependencies\n',
      '_REFERENCES.md': [
        '# References',
        '',
        '| RefID | Path | ExpectedSHA256 | ActualSHA256 | Status |',
        '|---|---|---|---|---|',
        '| REF-006 | `docs/PRD.md` | `expected` | `actual` | HASH_MISMATCH |',
        '| REF-099 | `docs/UNKNOWN.md` | `expected` | `actual` | UNKNOWN |'
      ].join('\n'),
      'Datasheet.md': '# Datasheet\n',
      'Specification.md': '# Specification\n',
      'MEMORY.md': '# Memory\n',
      '_MEMORY.md': '# Disabled memory\n',
      'HASH_VERIFICATION_BYPASS.jsonl': '{"ref":"REF-006"}\n'
    });

    const result = await scanDeliverableDocumentKitContract({
      deliverableId: 'DEL-07-03',
      deliverablePath
    });
    const conditions = result.findings.map((finding) => finding.condition);

    expect(result.valid).toBe(false);
    expect(result.errorCount).toBe(2);
    expect(conditions).toEqual(
      expect.arrayContaining([
        'missing_required_metadata',
        'missing_preparation_baseline',
        'missing_document_kit_file',
        'prohibited_memory_file',
        'reference_hash_warning',
        'reference_unknown_condition',
        'hash_verification_bypass_present',
        'canonical_memory_present'
      ])
    );
    expect(result.findings).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          path: path.join(deliverablePath, '_CONTEXT.md'),
          category: 'required_metadata',
          severity: 'error'
        }),
        expect.objectContaining({
          path: path.join(deliverablePath, '_MEMORY.md'),
          category: 'prohibited_file',
          severity: 'error'
        }),
        expect.objectContaining({
          path: path.join(deliverablePath, '_REFERENCES.md'),
          category: 'source_hash_warning',
          severity: 'warning'
        }),
        expect.objectContaining({
          path: path.join(deliverablePath, '_REFERENCES.md'),
          category: 'unknown_unsupported_condition',
          severity: 'warning'
        })
      ])
    );
  });
});
