import React from 'react';
import { act, create, type ReactTestInstance, type ReactTestRenderer } from 'react-test-renderer';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

// Human-gated transitions in the Workbench and Pipeline forms (App SPEC §4.3):
// the ruling and amendment inputs, what is sent to the transition API and how
// its refusals are shown.

const state = vi.hoisted(() => ({
  currentState: 'CHECKING',
  searchParams: new URLSearchParams(),
  transition: vi.fn()
}));

vi.mock('next/navigation', () => ({
  useSearchParams: () => state.searchParams
}));

vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: '/repo/projects/chirality-app-dev' })
}));

vi.mock('../../components/workspace/deliverables-provider', () => ({
  useDeliverables: () => ({
    loading: false,
    error: null,
    scan: {
      projectRoot: '/repo/projects/chirality-app-dev',
      scannedAt: '2026-09-26T00:00:00.000Z',
      truncated: false,
      deliverables: [
        {
          id: 'DEL-07-04',
          name: 'Lifecycle',
          pkg: 'PKG-07',
          status: 'CHECKING',
          path: '/repo/execution/PKG-07/DEL-07-04',
          key: 'PKG-07::DEL-07-04'
        }
      ],
      knowledgeDecomposition: { enabled: false, markerFile: null },
      knowledgeTypes: []
    },
    refresh: () => {}
  })
}));

vi.mock('../../components/shell/document-view', () => ({
  DocumentView: () => null
}));

vi.mock('../../lib/workspace/deliverable-api', async (importOriginal) => {
  const actual = await importOriginal<typeof import('../../lib/workspace/deliverable-api')>();
  const deliverablePath = '/repo/execution/PKG-07/DEL-07-04';
  return {
    ...actual,
    fetchDeliverableStatus: vi.fn(async () => ({
      projectRoot: '/repo/projects/chirality-app-dev',
      deliverablePath,
      statusFilePath: `${deliverablePath}/_STATUS.md`,
      status: {
        title: 'Status: DEL-07-04 Lifecycle',
        currentState: state.currentState,
        lastUpdated: '2026-09-25',
        history: [],
        extraFields: []
      }
    })),
    fetchDeliverableDependencies: vi.fn(async () => ({
      projectRoot: '/repo/projects/chirality-app-dev',
      deliverablePath,
      dependenciesFilePath: `${deliverablePath}/Dependencies.csv`,
      registerPresent: true,
      secondarySummaryPresent: false,
      headers: [],
      rows: [],
      warnings: []
    })),
    transitionDeliverableStatus: state.transition
  };
});

import { WorkspaceApiClientError } from '../../lib/workspace/deliverable-api';
import { PipelineSurface } from '../../components/pipeline/pipeline-surface';
import { WorkbenchSurface } from '../../components/workbench/workbench-surface';

const RULING = 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md';

let tree: ReactTestRenderer | undefined;

beforeEach(() => {
  state.currentState = 'CHECKING';
  state.searchParams = new URLSearchParams();
  state.transition.mockReset();
  vi.stubGlobal(
    'fetch',
    vi.fn(async () => ({
      ok: true,
      json: async () => ({
        deliverables: [{ id: 'DEL-07-04', label: 'Lifecycle', path: '/repo/execution/PKG-07/DEL-07-04' }],
        knowledgeTypes: [],
        hasKnowledgeDecomposition: false,
        truncated: false,
        scannedAt: '2026-09-26T00:00:00.000Z'
      })
    }))
  );
});

afterEach(() => {
  if (tree) {
    act(() => tree!.unmount());
  }
  tree = undefined;
  vi.unstubAllGlobals();
});

const text = (node: ReactTestInstance | string): string =>
  typeof node === 'string' ? node : node.children.map(text).join('');

async function flush(): Promise<void> {
  for (let index = 0; index < 6; index += 1) {
    await act(async () => {
      await Promise.resolve();
    });
  }
}

async function mount(element: React.ReactElement): Promise<ReactTestInstance> {
  await act(async () => {
    tree = create(element);
  });
  await flush();
  return tree!.root;
}

function transitionForm(root: ReactTestInstance): ReactTestInstance {
  // The Pipeline scaffold form shares the class; pick the lifecycle form.
  const forms = root
    .findAllByProps({ className: 'pipeline-transition-form' })
    .filter(
      (form) =>
        form.type === 'form' &&
        form.findAllByType('h4').some((heading) => text(heading) === 'Lifecycle Transition')
    );
  expect(forms).toHaveLength(1);
  return forms[0];
}

function targetSelect(form: ReactTestInstance): ReactTestInstance {
  return form.findAllByType('select')[0];
}

function approvalInput(form: ReactTestInstance): ReactTestInstance {
  return form
    .findAllByType('input')
    .find((input) => input.props.type !== 'date' && !input.props.name)!;
}

function submitButton(form: ReactTestInstance): ReactTestInstance {
  return form.findByProps({ type: 'submit' });
}

async function change(input: ReactTestInstance, value: string): Promise<void> {
  await act(async () => {
    input.props.onChange({ target: { value } });
  });
}

async function submit(form: ReactTestInstance): Promise<void> {
  await act(async () => {
    form.props.onSubmit({ preventDefault: vi.fn() });
  });
  await flush();
}

const SURFACES: Array<[string, () => React.ReactElement, () => void]> = [
  ['Workbench', () => <WorkbenchSurface />, () => {}],
  [
    'Pipeline',
    () => <PipelineSurface />,
    () => {
      state.searchParams = new URLSearchParams({ category: 'TASK', scopeKey: 'PKG-07::DEL-07-04' });
    }
  ]
];

describe.each(SURFACES)('%s lifecycle transition gates', (_name, element, prepare) => {
  beforeEach(() => {
    prepare();
  });

  it('offers the human-ruled reversal from CHECKING and requires its ruling before submitting', async () => {
    const root = await mount(element());
    const form = transitionForm(root);
    const options = targetSelect(form).findAllByType('option').map((option) => text(option));
    expect(options).toEqual(['ISSUED', 'IN_PROGRESS (ruled reversal)']);

    await change(targetSelect(form), 'IN_PROGRESS');
    expect(form.findByProps({ name: 'ruling' }).props.required).toBe(true);
    expect(form.findAllByProps({ name: 'amendment' })).toHaveLength(0);
    expect(text(form)).toContain('Ruling record (required)');
    expect(text(form)).toContain('The actor is asserted by the caller');
    expect(text(form)).toContain('tools/scaffolding/write_status.sh');

    await change(approvalInput(form), 'abc1234');
    expect(submitButton(form).props.disabled).toBe(true);
    await change(form.findByProps({ name: 'ruling' }), `  ${RULING}  `);
    expect(submitButton(form).props.disabled).toBe(false);

    state.transition.mockResolvedValueOnce(await pendingSnapshot('IN_PROGRESS'));
    await submit(form);
    expect(state.transition).toHaveBeenCalledExactlyOnceWith(
      expect.objectContaining({
        targetState: 'IN_PROGRESS',
        actor: 'HUMAN',
        approvalSha: 'abc1234',
        ruling: RULING,
        amendment: undefined
      })
    );
  });

  it('sends an optional ruling on the forward gate into ISSUED', async () => {
    const root = await mount(element());
    const form = transitionForm(root);
    expect(targetSelect(form).props.value).toBe('ISSUED');
    expect(form.findByProps({ name: 'ruling' }).props.required).toBe(false);
    expect(text(form)).toContain('Ruling record (optional)');

    await change(approvalInput(form), 'abc1234');
    expect(submitButton(form).props.disabled).toBe(false);
    await change(form.findByProps({ name: 'ruling' }), RULING);
    state.transition.mockResolvedValueOnce(await pendingSnapshot('ISSUED'));
    await submit(form);
    expect(state.transition).toHaveBeenCalledExactlyOnceWith(
      expect.objectContaining({ targetState: 'ISSUED', actor: 'HUMAN', ruling: RULING, amendment: undefined })
    );
  });

  it('reopens ISSUED only with an amendment and shows the checker refusal code', async () => {
    state.currentState = 'ISSUED';
    const root = await mount(element());
    const form = transitionForm(root);
    expect(targetSelect(form).findAllByType('option').map((option) => text(option))).toEqual([
      'IN_PROGRESS (amendment reopening)'
    ]);
    expect(form.findAllByProps({ name: 'ruling' })).toHaveLength(0);
    expect(form.findByProps({ name: 'amendment' }).props.required).toBe(true);
    expect(text(form)).toContain('ACCEPTED amendment whose action register names this deliverable');

    await change(approvalInput(form), 'abc1234');
    expect(submitButton(form).props.disabled).toBe(true);
    await change(form.findByProps({ name: 'amendment' }), 'SCA-001');
    expect(submitButton(form).props.disabled).toBe(false);

    state.transition.mockRejectedValueOnce(
      new WorkspaceApiClientError(400, 'AMENDMENT_NOT_ADMITTED', 'REGISTER_SCHEMA: stray whitespace in ScopeChanging', {
        refusalCode: 'REGISTER_SCHEMA'
      })
    );
    await submit(form);
    expect(state.transition).toHaveBeenCalledExactlyOnceWith(
      expect.objectContaining({
        targetState: 'IN_PROGRESS',
        actor: 'HUMAN',
        approvalSha: 'abc1234',
        amendment: 'SCA-001',
        ruling: undefined
      })
    );
    const alert = transitionForm(tree!.root).findByProps({ role: 'alert' });
    expect(text(alert)).toBe(
      'AMENDMENT_NOT_ADMITTED (checker code REGISTER_SCHEMA): stray whitespace in ScopeChanging. ' +
        'The amendment record check refused the reopening. _STATUS.md was not changed.'
    );
  });

  it('shows the history refusal as an alert', async () => {
    const root = await mount(element());
    const form = transitionForm(root);
    await change(targetSelect(form), 'IN_PROGRESS');
    await change(approvalInput(form), 'abc1234');
    await change(form.findByProps({ name: 'ruling' }), RULING);
    state.transition.mockRejectedValueOnce(
      new WorkspaceApiClientError(
        400,
        'HISTORY_NOT_PRESERVED',
        'The transition would drop the recorded reopening under SCA-001 from _STATUS.md',
        { amendmentId: 'SCA-001' }
      )
    );
    await submit(form);
    expect(text(transitionForm(tree!.root).findByProps({ role: 'alert' }))).toContain(
      'HISTORY_NOT_PRESERVED: The transition would drop the recorded reopening under SCA-001'
    );
  });
});

async function pendingSnapshot(currentState: string) {
  return {
    projectRoot: '/repo/projects/chirality-app-dev',
    deliverablePath: '/repo/execution/PKG-07/DEL-07-04',
    statusFilePath: '/repo/execution/PKG-07/DEL-07-04/_STATUS.md',
    status: {
      title: 'Status: DEL-07-04 Lifecycle',
      currentState,
      lastUpdated: '2026-09-26',
      history: [],
      extraFields: []
    },
    transition: { from: 'CHECKING', to: currentState, actor: 'HUMAN' }
  };
}
