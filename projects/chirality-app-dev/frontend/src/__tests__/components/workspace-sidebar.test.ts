import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { WorkspaceSidebar } from '../../components/shell/workspace-sidebar';

describe('WorkspaceSidebar default tabs', () => {
  it('renders exactly the eight default tabs with the active tab selected and no Portal, Workbench or Pipeline tab', () => {
    const html = renderToStaticMarkup(
      createElement(WorkspaceSidebar, {
        activeTab: 'workflow',
        onTabChange: () => {}
      })
    );

    const tabs = [...html.matchAll(/<button[^>]*role="tab"[^>]*>([^<]*)<\/button>/g)].map((match) => ({
      label: match[1],
      selected: /aria-selected="true"/.test(match[0])
    }));

    expect(tabs.map((tab) => tab.label)).toEqual([
      'Files',
      'Sessions',
      'Transcript',
      'Tools',
      'Subagents',
      'Document',
      'Workflow',
      'Tool Kit'
    ]);
    expect(tabs.filter((tab) => tab.selected).map((tab) => tab.label)).toEqual(['Workflow']);
    expect(html.match(/role="tab"/g)).toHaveLength(8);
    for (const retired of ['Portal', 'Workbench', 'Pipeline']) {
      expect(tabs.some((tab) => tab.label === retired)).toBe(false);
    }
  });
});
