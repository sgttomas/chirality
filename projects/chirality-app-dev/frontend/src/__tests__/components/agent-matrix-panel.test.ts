import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it } from 'vitest';
import { AgentMatrixPanel } from '../../components/portal/agent-matrix';

const baseProps = {
  loading: false,
  error: null,
  scan: null,
  streaming: false,
  launchNotice: null,
  onFocusLoop: () => {},
  onCellLaunch: () => {},
  onDeliverableLaunch: () => {}
};

function disabledAttributeCount(html: string): number {
  return (html.match(/disabled=""/g) ?? []).length;
}

describe('AgentMatrixPanel rendering', () => {
  it('describes loop-first launch behavior for matrix cells', () => {
    const html = renderToStaticMarkup(createElement(AgentMatrixPanel, baseProps));
    expect(html).toContain('Type-0/Type-1 cells focus the mounted live loop');
    expect(html).toContain('governed Pipeline form in the sidebar');
    expect(html).toContain('Focus live loop');
    expect(html).toContain('>Loop<');
    expect(html).toContain('>Pipeline<');
    expect(disabledAttributeCount(html)).toBe(0);
  });

  it('disables launches while the mounted loop is streaming', () => {
    const html = renderToStaticMarkup(
      createElement(AgentMatrixPanel, { ...baseProps, streaming: true })
    );
    expect(html).toContain('Matrix launches are paused');
    expect(disabledAttributeCount(html)).toBeGreaterThan(0);
  });

  it('renders deliverable launch rows with stable pkg::deliverable keys', () => {
    const html = renderToStaticMarkup(
      createElement(AgentMatrixPanel, {
        ...baseProps,
        scan: {
          projectRoot: '/repo/projects/chirality-app-dev',
          scannedAt: '2026-06-21T00:00:00.000Z',
          truncated: false,
          deliverables: [
            {
              id: 'DEL-02-01',
              name: 'Desktop Shell and Matrix Navigation',
              pkg: 'PKG-02',
              status: 'CHECKING',
              path: '/repo/execution/PKG-02/DEL-02-01',
              key: 'PKG-02::DEL-02-01'
            }
          ],
          knowledgeDecomposition: { enabled: false, markerFile: null },
          knowledgeTypes: []
        }
      })
    );

    expect(html).toContain('OPERATIVE Deliverable Rows');
    expect(html).toContain('PKG-02::DEL-02-01');
    expect(html).toContain('Desktop Shell and Matrix Navigation');
    expect(disabledAttributeCount(html)).toBe(0);
  });
});
