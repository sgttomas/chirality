import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { WorkspaceSidebar } from '../../components/shell/workspace-sidebar';

describe('WorkspaceSidebar tertiary tabs', () => {
  it('renders Portal, Workbench, and Pipeline as sidebar tabs when provided', () => {
    const html = renderToStaticMarkup(
      createElement(WorkspaceSidebar, {
        activeTab: 'workbench',
        onTabChange: () => {},
        pipelineTab: createElement('div', null, 'Pipeline tertiary form'),
        portalTab: createElement('div', null, 'Portal matrix'),
        workbenchTab: createElement('div', null, 'Workbench tertiary form')
      })
    );

    expect(html).toContain('role="tab"');
    expect(html).toContain('Portal');
    expect(html).toContain('Workbench');
    expect(html).toContain('Pipeline');
    expect(html).toContain('Workbench tertiary form');
    expect(html).not.toContain('Pipeline tertiary form');
  });
});
