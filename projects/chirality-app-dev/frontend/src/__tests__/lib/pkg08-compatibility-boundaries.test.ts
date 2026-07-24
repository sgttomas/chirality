import { describe, expect, it } from 'vitest';
import {
  MATRIX_ROWS,
  matrixCellLaunchKind
} from '../../lib/portal/agent-matrix-cells';
import { mergeMatrixTargetIntoCurrentUrl } from '../../lib/portal/agent-matrix-launch';
import { resolvePersona } from '../../lib/shell/persona-resolution';
import {
  PIPELINE_CATEGORY_ORDER,
  validatePipelineDispatchIntent
} from '../../lib/pipeline/pipeline-dispatch-contract';

describe('PKG-08 compatibility and authority boundaries', () => {
  it('preserves the governed ORCHESTRATE compatibility alias', () => {
    expect(resolvePersona('ORCHESTRATE')).toBe('PROJECT_SETUP');
  });

  it('keeps exact OPERATIVE matrix intent aligned with the Pipeline taxonomy', () => {
    const operative = MATRIX_ROWS.find((row) => row.rowLabel === 'OPERATIVE');
    expect(operative?.cells.map((cell) => cell.label)).toEqual([
      'DECOMP*',
      'PREP*',
      'TASK*',
      'AUDIT*'
    ]);
    expect(
      operative?.cells.map((cell) => {
        expect(matrixCellLaunchKind(cell)).toBe('route');
        return new URL(cell.target, 'http://chirality.local').searchParams.get('category');
      })
    ).toEqual(PIPELINE_CATEGORY_ORDER);
  });

  it('round-trips unknown query parameters through the existing matrix compatibility helper', () => {
    expect(
      mergeMatrixTargetIntoCurrentUrl(
        '/pipeline?category=AUDIT',
        '/',
        new URLSearchParams(
          'agent=WORKING_ITEMS&row=NORMATIVE&column=JUDGING&future=keep&category=TASK&scopeKey=old'
        )
      )
    ).toBe('/?agent=WORKING_ITEMS&row=NORMATIVE&column=JUDGING&future=keep&category=AUDIT');
  });

  it('does not turn Pipeline presentation state into delegation authority', () => {
    const result = validatePipelineDispatchIntent(
      {
        category: 'AUDIT',
        option: 'AGENTS'
      },
      {
        knowledgeDecompositionEnabled: false,
        deliverableKeys: [],
        knowledgeTypes: []
      }
    );

    expect(result.valid).toBe(true);
    if (result.valid) {
      expect(result.intent.executionAuthorized).toBe(false);
      expect('delegate_agent' in result.intent).toBe(false);
      expect('approvalRef' in result.intent).toBe(false);
      expect('writeTargets' in result.intent).toBe(false);
    }
  });
});
