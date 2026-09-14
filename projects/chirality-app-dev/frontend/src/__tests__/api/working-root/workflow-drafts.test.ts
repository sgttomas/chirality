import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { mkdtemp, mkdir, writeFile, readFile, rm, symlink, realpath, readdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { discoverMethodCatalog } from '@chirality/runtime-core';
import { listDrafts, readWorkflowDraft, registerDraft } from '../../../app/api/working-root/workflow-drafts/workflow-draft-store';

let root: string;
const content = '---\nname: sample\ndescription: A reviewed workflow\n---\n# Sample\nRead resources/guide.md.\n';
async function draft(name = 'sample', text = content) {
  const target = path.join(root, '.chirality/workflow-drafts', name);
  await mkdir(path.join(target, 'resources'), { recursive: true });
  await writeFile(path.join(target, 'WORKFLOW.md'), text);
  await writeFile(path.join(target, 'resources/guide.md'), 'Resource bytes\r\n');
  return target;
}
beforeEach(async () => { root = await realpath(await mkdtemp(path.join(tmpdir(), 'workflow-drafts-test-'))); });
afterEach(async () => { await rm(root, { recursive: true, force: true }); });
describe('workflow draft review and registration', () => {
  it('ignores ordinary folder housekeeping files when listing packages', async () => {
    await draft();
    await writeFile(path.join(root, '.chirality/workflow-drafts/.DS_Store'), 'Finder metadata');
    await writeFile(path.join(root, '.chirality/workflow-drafts/notes.txt'), 'Author notes');
    expect((await listDrafts(root, 'project')).map(item => item.name)).toEqual(['sample']);
  });
  it('keeps drafts out of the catalog, then registers the exact reviewed entrypoint and resources', async () => {
    await draft();
    const source = { sourceRootId: 'test-project', source: 'project' as const, rootPath: root, workflowDirectory: '.chirality/workflows' };
    expect((await discoverMethodCatalog([source])).entries).toHaveLength(0);
    const review = await readWorkflowDraft(root, 'sample', 'project');
    expect(review.content).toBe(content);
    expect(review.files.map(file => file.path)).toEqual(['resources/guide.md', 'WORKFLOW.md']);
    expect(review.destinationExists).toBe(false);
    expect(review.registered).toBe(false);
    expect(review.files.find(file => file.path === 'resources/guide.md')?.content).toBe('Resource bytes\r\n');
    await registerDraft(root, 'sample', 'project', review.reviewToken);
    expect(await readFile(path.join(root, '.chirality/workflows/sample/WORKFLOW.md'), 'utf8')).toBe(content);
    expect(await readFile(path.join(root, '.chirality/workflows/sample/resources/guide.md'), 'utf8')).toBe('Resource bytes\r\n');
    expect((await discoverMethodCatalog([source])).entries[0]?.descriptor.name).toBe('sample');
    expect((await readWorkflowDraft(root, 'sample', 'project')).destinationExists).toBe(true);
    expect((await readWorkflowDraft(root, 'sample', 'project')).registered).toBe(true);
    await writeFile(path.join(root, '.chirality/workflows/sample/resources/guide.md'), 'Different canonical resource');
    expect((await readWorkflowDraft(root, 'sample', 'project')).registered).toBe(false);
  });
  it('rejects stale review when any resource changes and preserves the draft', async () => {
    const target = await draft();
    const review = await readWorkflowDraft(root, 'sample', 'project');
    await writeFile(path.join(target, 'resources/guide.md'), 'Changed');
    await expect(registerDraft(root, 'sample', 'project', review.reviewToken)).rejects.toMatchObject({ code: 'DRAFT_CHANGED', status: 409 });
    expect(await readFile(path.join(target, 'WORKFLOW.md'), 'utf8')).toBe(content);
  });
  it('binds the review to its source and root', async () => {
    await draft();
    const review = await readWorkflowDraft(root, 'sample', 'project');
    await expect(registerDraft(root, 'sample', 'user', review.reviewToken)).rejects.toMatchObject({ code: 'DRAFT_CHANGED' });
  });
  it('never overwrites an existing empty destination or an accepted package', async () => {
    await draft();
    const review = await readWorkflowDraft(root, 'sample', 'project');
    const target = path.join(root, '.chirality/workflows/sample');
    await mkdir(target, { recursive: true });
    await expect(registerDraft(root, 'sample', 'project', review.reviewToken)).rejects.toMatchObject({ code: 'WORKFLOW_EXISTS' });
    expect(await readdir(target)).toEqual([]);
    await writeFile(path.join(target, 'WORKFLOW.md'), 'Existing');
    await expect(registerDraft(root, 'sample', 'project', review.reviewToken)).rejects.toMatchObject({ code: 'WORKFLOW_EXISTS' });
    expect(await readFile(path.join(target, 'WORKFLOW.md'), 'utf8')).toBe('Existing');
  });
  it('allows only one concurrent registration and rejects repeated clicks', async () => {
    await draft();
    const review = await readWorkflowDraft(root, 'sample', 'project');
    const results = await Promise.allSettled([1, 2].map(() => registerDraft(root, 'sample', 'project', review.reviewToken)));
    expect(results.filter(result => result.status === 'fulfilled')).toHaveLength(1);
    expect(results.filter(result => result.status === 'rejected')).toHaveLength(1);
    await expect(registerDraft(root, 'sample', 'project', review.reviewToken)).rejects.toMatchObject({ code: 'WORKFLOW_EXISTS' });
  });
  it.each(['../sample', '/sample', 'sample/other', 'Sample', 'sample\\other'])('rejects malicious or noncanonical name %s', async name => {
    await expect(readWorkflowDraft(root, name, 'project')).rejects.toMatchObject({ code: 'INVALID_REQUEST' });
  });
  it('surfaces malformed metadata rather than hiding a rejected draft', async () => {
    const target = await draft('sample', '# Missing frontmatter');
    await expect(listDrafts(root, 'project')).rejects.toMatchObject({ code: 'INVALID_DRAFT' });
    expect(await readFile(path.join(target, 'WORKFLOW.md'), 'utf8')).toBe('# Missing frontmatter');
  });
  it('rejects symlinked resources even when they remain inside the package', async () => {
    const target = await draft();
    await symlink(path.join(target, 'WORKFLOW.md'), path.join(target, 'resources/link.md'));
    await expect(readWorkflowDraft(root, 'sample', 'project')).rejects.toMatchObject({ code: 'DRAFT_UNSAFE_PATH' });
  });
  it('rejects a symlinked draft collection and destination collection', async () => {
    const target = path.join(root, 'elsewhere');
    await mkdir(target); await mkdir(path.join(root, '.chirality'));
    await symlink(target, path.join(root, '.chirality/workflow-drafts'));
    await expect(listDrafts(root, 'project')).rejects.toMatchObject({ code: 'DRAFT_UNSAFE_PATH' });
    await rm(path.join(root, '.chirality/workflow-drafts'));
    await draft();
    const review = await readWorkflowDraft(root, 'sample', 'project');
    await symlink(target, path.join(root, '.chirality/workflows'));
    await expect(registerDraft(root, 'sample', 'project', review.reviewToken)).rejects.toMatchObject({ code: 'DRAFT_UNSAFE_PATH' });
    expect(await readdir(target)).toEqual([]);
  });
  it('bounds all package files including resources outside the resources directory', async () => {
    const target = await draft();
    await writeFile(path.join(target, 'large.bin'), Buffer.alloc(8 * 1024 * 1024));
    await expect(readWorkflowDraft(root, 'sample', 'project')).rejects.toMatchObject({ code: 'DRAFT_TOO_LARGE' });
  });
  it('returns an empty list for an absent draft directory', async () => {
    expect(await listDrafts(root, 'user')).toEqual([]);
  });
});
