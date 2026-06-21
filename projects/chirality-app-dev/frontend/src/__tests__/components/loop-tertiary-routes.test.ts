import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';

vi.mock('../../components/shell/loop-tertiary-shell', async () => {
  const React = await import('react');
  return {
    LoopTertiaryShell: (props: {
      defaultSidebarTab: string;
      section: string;
      subtitle: string;
      title: string;
    }) =>
      React.createElement(
        'section',
        {
          'data-default-sidebar-tab': props.defaultSidebarTab,
          'data-section': props.section
        },
        React.createElement('h1', null, props.title),
        React.createElement('p', null, props.subtitle)
      )
  };
});

describe('LoopTertiaryShell route clients', () => {
  it('opens the Workbench deep link as a right-sidebar tertiary form', async () => {
    const { default: WorkbenchClient } = await import('../../app/workbench/workbench-client');
    const html = renderToStaticMarkup(createElement(WorkbenchClient));

    expect(html).toContain('data-default-sidebar-tab="workbench"');
    expect(html).toContain('data-section="WORKBENCH"');
    expect(html).toContain('Run the live loop while reviewing persona context');
  });

  it('opens the Pipeline deep link as a right-sidebar tertiary form', async () => {
    const { default: PipelineClient } = await import('../../app/pipeline/pipeline-client');
    const html = renderToStaticMarkup(createElement(PipelineClient));

    expect(html).toContain('data-default-sidebar-tab="pipeline"');
    expect(html).toContain('data-section="PIPELINE"');
    expect(html).toContain('Run the live loop while configuring operative');
  });
});
