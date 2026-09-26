import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import {
  WorkbenchLifecycleTransitionForm,
  WorkbenchSurface
} from '../../components/workbench/workbench-surface';

const mockState = vi.hoisted(() => ({
  projectRoot: '/repo/projects/chirality-app-dev',
  searchParams: new URLSearchParams()
}));

vi.mock('next/navigation', () => ({
  useSearchParams: () => mockState.searchParams
}));

vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({ projectRoot: mockState.projectRoot })
}));

// `DocumentView` drags the react-markdown ESM graph plus `fetch` into this node
// environment; the Workbench Documents block only needs to prove the mount point.
vi.mock('../../components/shell/document-view', async () => {
  const { createElement: h } = await import('react');
  return {
    DocumentView: () => h('div', { 'data-document-view': 'mounted' }, 'Document view')
  };
});

function disabledAttributeCount(html: string): number {
  return (html.match(/disabled=""/g) ?? []).length;
}

describe('WorkbenchSurface rendering', () => {
  beforeEach(() => {
    mockState.projectRoot = '/repo/projects/chirality-app-dev';
    mockState.searchParams = new URLSearchParams();
  });

  it('renders unsupported agents as read-only while preserving matrix context', () => {
    mockState.searchParams = new URLSearchParams({
      agent: 'HELP_HUMAN',
      row: 'EVALUATIVE',
      column: 'JUDGING'
    });

    const html = renderToStaticMarkup(createElement(WorkbenchSurface));

    expect(html).toContain('Active Agent Context');
    expect(html).toContain('HELP_HUMAN');
    expect(html).toContain('EVALUATIVE');
    expect(html).toContain('JUDGING');
    expect(html).toContain('Deliverable Contracts (Read-Only)');
    expect(html).toContain('Transition writes are disabled for this agent.');
    expect(html).not.toContain('Apply Transition');
  });

  it('mounts the folded Documents block inside the Workbench surface', () => {
    const html = renderToStaticMarkup(createElement(WorkbenchSurface));

    expect(html).toContain('aria-label="Documents"');
    expect(html).toContain('<h3>Documents</h3>');
    expect(html).toContain('Deliverable documents, evidence, and contracts read from the Working Root.');
    expect(html).toContain('data-document-view="mounted"');
  });

  it('keeps the Documents block mounted for read-only agents', () => {
    mockState.searchParams = new URLSearchParams({ agent: 'HELP_HUMAN' });

    const html = renderToStaticMarkup(createElement(WorkbenchSurface));

    expect(html).toContain('Deliverable Contracts (Read-Only)');
    expect(html).toContain('data-document-view="mounted"');
    expect(html).not.toContain('Apply Transition');
  });
});

describe('WorkbenchLifecycleTransitionForm rendering', () => {
  const noop = () => {};

  it('requires approval SHA and locks actor choice to HUMAN for human-gated transitions', () => {
    const html = renderToStaticMarkup(
      createElement(WorkbenchLifecycleTransitionForm, {
        availableTransitionTargets: ['CHECKING'],
        canSubmitTransition: false,
        requiresApprovalSha: true,
        transitionActor: 'HUMAN',
        transitionApprovalSha: '',
        transitionDate: '2026-06-21',
        transitionError: null,
        transitionSubmitting: false,
        transitionTarget: 'CHECKING',
        onActorChange: noop,
        onApprovalShaChange: noop,
        onDateChange: noop,
        onSubmit: noop,
        onTargetChange: noop
      })
    );

    expect(html).toContain('Approval SHA (required)');
    expect(html).toContain('placeholder="e.g. abcd1234"');
    expect(html).toContain('<option value="HUMAN" selected="">HUMAN</option>');
    expect(html).toContain('<option value="WORKING_ITEMS" disabled="">WORKING_ITEMS</option>');
    expect(html).toContain('<button type="submit" disabled="">Apply Transition</button>');
    expect(disabledAttributeCount(html)).toBe(4);
  });

  it('keeps the approval SHA optional for non-human-gated transitions', () => {
    const html = renderToStaticMarkup(
      createElement(WorkbenchLifecycleTransitionForm, {
        availableTransitionTargets: ['IN_PROGRESS'],
        canSubmitTransition: true,
        requiresApprovalSha: false,
        transitionActor: 'WORKING_ITEMS',
        transitionApprovalSha: '',
        transitionDate: '2026-06-21',
        transitionError: null,
        transitionSubmitting: false,
        transitionTarget: 'IN_PROGRESS',
        onActorChange: noop,
        onApprovalShaChange: noop,
        onDateChange: noop,
        onSubmit: noop,
        onTargetChange: noop
      })
    );

    expect(html).toContain('Approval SHA (optional)');
    expect(html).toContain('Optional (required at CHECKING/ISSUED)');
    expect(html).toContain('<option value="WORKING_ITEMS" selected="">WORKING_ITEMS</option>');
    expect(html).not.toContain('value="WORKING_ITEMS" disabled');
    expect(html).not.toContain('<button type="submit" disabled="">');
  });
});

describe('WorkbenchLifecycleTransitionForm human-gate inputs (App SPEC §4.3)', () => {
  const noop = () => {};
  const render = (props: {
    currentState: string;
    targets: string[];
    target: string;
    ruling?: string;
    amendment?: string;
    error?: string | null;
    canSubmit?: boolean;
  }): string =>
    renderToStaticMarkup(
      createElement(WorkbenchLifecycleTransitionForm, {
        availableTransitionTargets: props.targets,
        canSubmitTransition: props.canSubmit ?? false,
        currentState: props.currentState,
        requiresApprovalSha: true,
        transitionActor: 'HUMAN',
        transitionAmendment: props.amendment ?? '',
        transitionApprovalSha: '',
        transitionDate: '2026-09-26',
        transitionError: props.error ?? null,
        transitionRuling: props.ruling ?? '',
        transitionSubmitting: false,
        transitionTarget: props.target,
        onActorChange: noop,
        onAmendmentChange: noop,
        onApprovalShaChange: noop,
        onDateChange: noop,
        onRulingChange: noop,
        onSubmit: noop,
        onTargetChange: noop
      })
    );

  function describedByNote(html: string, name: string): void {
    const inputId = new RegExp(`<input name="${name}"[^>]*aria-describedby="([^"]+)"`).exec(html)?.[1];
    expect(inputId).toBeTruthy();
    expect(html).toContain(`<p class="pipeline-note" id="${inputId}">`);
  }

  it('requires a ruling record for the reversal from CHECKING and explains what is checked', () => {
    const html = render({ currentState: 'CHECKING', targets: ['ISSUED', 'IN_PROGRESS'], target: 'IN_PROGRESS' });

    expect(html).toContain('<option value="ISSUED">ISSUED</option>');
    expect(html).toContain(
      '<option value="IN_PROGRESS" selected="">IN_PROGRESS (ruled reversal)</option>'
    );
    expect(html).toContain('Approval SHA (required)');
    expect(html).toContain('Ruling record (required)');
    expect(html).toMatch(/<input name="ruling"[^>]*required=""/);
    expect(html).not.toContain('name="amendment"');
    expect(html).toContain('Reversal from CHECKING needs the approval SHA and the ruling record');
    expect(html).toContain('The actor is asserted by the caller');
    expect(html).toContain('<code>tools/scaffolding/write_status.sh</code> is the anchored');
    expect(html).toContain('<option value="WORKING_ITEMS" disabled="">WORKING_ITEMS</option>');
    expect(html).toContain('<button type="submit" disabled="">Apply Transition</button>');
    describedByNote(html, 'ruling');
  });

  it('requires an accepted amendment for the reopening of ISSUED and takes no ruling', () => {
    const html = render({ currentState: 'ISSUED', targets: ['IN_PROGRESS'], target: 'IN_PROGRESS' });

    expect(html).toContain(
      '<option value="IN_PROGRESS" selected="">IN_PROGRESS (amendment reopening)</option>'
    );
    expect(html).toContain('Accepted amendment (required)');
    expect(html).toMatch(/<input name="amendment"[^>]*required=""/);
    expect(html).not.toContain('name="ruling"');
    expect(html).toContain('the App reads working-tree records only');
    describedByNote(html, 'amendment');
  });

  it('offers an optional ruling on the forward gates', () => {
    for (const [currentState, target] of [
      ['IN_PROGRESS', 'CHECKING'],
      ['CHECKING', 'ISSUED']
    ]) {
      const html = render({ currentState, targets: [target], target, ruling: 'records/ruling.md', canSubmit: true });
      expect(html).toContain('Ruling record (optional)');
      expect(html).toContain('value="records/ruling.md"');
      expect(html).not.toMatch(/<input name="ruling"[^>]*required=""/);
      expect(html).not.toContain('name="amendment"');
      expect(html).toContain('The actor is asserted by the caller');
      expect(html).toContain('<button type="submit">Apply Transition</button>');
    }
  });

  it('shows no gate inputs or note for an ordinary transition', () => {
    const html = renderToStaticMarkup(
      createElement(WorkbenchLifecycleTransitionForm, {
        availableTransitionTargets: ['IN_PROGRESS'],
        canSubmitTransition: true,
        currentState: 'INITIALIZED',
        requiresApprovalSha: false,
        transitionActor: 'WORKING_ITEMS',
        transitionApprovalSha: '',
        transitionDate: '2026-09-26',
        transitionError: null,
        transitionSubmitting: false,
        transitionTarget: 'IN_PROGRESS',
        onActorChange: noop,
        onApprovalShaChange: noop,
        onDateChange: noop,
        onSubmit: noop,
        onTargetChange: noop
      })
    );
    expect(html).toContain('<option value="IN_PROGRESS" selected="">IN_PROGRESS</option>');
    expect(html).not.toContain('name="ruling"');
    expect(html).not.toContain('name="amendment"');
    expect(html).not.toContain('asserted by the caller');
  });

  it('shows a refusal as an alert', () => {
    const html = render({
      currentState: 'ISSUED',
      targets: ['IN_PROGRESS'],
      target: 'IN_PROGRESS',
      error: 'AMENDMENT_NOT_ADMITTED (checker code DELIVERABLE_REMOVED): removed'
    });
    expect(html).toContain(
      '<p class="panel-error" role="alert">AMENDMENT_NOT_ADMITTED (checker code DELIVERABLE_REMOVED): removed</p>'
    );
  });
});
