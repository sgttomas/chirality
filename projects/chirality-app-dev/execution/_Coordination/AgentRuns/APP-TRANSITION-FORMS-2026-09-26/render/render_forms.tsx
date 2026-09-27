// Static render of the Workbench and Pipeline lifecycle transition forms for the
// browser layout check recorded in ../RECEIPT.md. It renders each form state to
// markup with the App stylesheet inlined; it does not start the App.
//
// Bundle and run from projects/chirality-app-dev (see ../RECEIPT.md):
//   NODE_PATH=frontend/node_modules frontend/node_modules/.bin/esbuild \
//     <this file> --bundle --platform=node --format=cjs --jsx=automatic \
//     --log-level=warning --outfile=<tmp>/render_forms.cjs
//   node <tmp>/render_forms.cjs <out-dir>
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { PipelineLifecycleTransitionForm } from '../../../../../frontend/src/components/pipeline/pipeline-surface';
import { WorkbenchLifecycleTransitionForm } from '../../../../../frontend/src/components/workbench/workbench-surface';
import {
  lifecycleTransitionEvidence,
  lifecycleTransitionTargets
} from '../../../../../frontend/src/lib/workspace/deliverable-api';

const noop = (): void => {};

type Scenario = {
  name: string;
  form: 'workbench' | 'pipeline';
  currentState: 'CHECKING' | 'ISSUED' | 'IN_PROGRESS';
  target: string;
  approvalSha: string;
  ruling: string;
  amendment: string;
  error: string | null;
};

const SCENARIOS: Scenario[] = [
  {
    name: 'workbench-reversal-filled',
    form: 'workbench',
    currentState: 'CHECKING',
    target: 'IN_PROGRESS',
    approvalSha: 'abc1234',
    ruling: 'execution/_Coordination/_DECISIONS/D-001_check_withdrawn.md',
    amendment: '',
    error: null
  },
  {
    name: 'workbench-reopen-refused',
    form: 'workbench',
    currentState: 'ISSUED',
    target: 'IN_PROGRESS',
    approvalSha: 'abc1234',
    ruling: '',
    amendment: 'SCA-001',
    error:
      'AMENDMENT_NOT_ADMITTED (checker code REGISTER_SCHEMA): stray whitespace in ScopeChanging. ' +
      'The amendment record check refused the reopening. _STATUS.md was not changed.'
  },
  {
    name: 'pipeline-reversal-empty',
    form: 'pipeline',
    currentState: 'CHECKING',
    target: 'IN_PROGRESS',
    approvalSha: '',
    ruling: '',
    amendment: '',
    error: null
  },
  {
    name: 'pipeline-forward-issued-optional-ruling',
    form: 'pipeline',
    currentState: 'CHECKING',
    target: 'ISSUED',
    approvalSha: 'abc1234',
    ruling: '',
    amendment: '',
    error: null
  }
];

function render(scenario: Scenario): string {
  const evidence = lifecycleTransitionEvidence(scenario.currentState, scenario.target);
  const canSubmit =
    Boolean(scenario.approvalSha) &&
    (evidence.ruling !== 'required' || Boolean(scenario.ruling)) &&
    (evidence.amendment !== 'required' || Boolean(scenario.amendment));
  const props = {
    availableTransitionTargets: lifecycleTransitionTargets(scenario.currentState),
    canSubmitTransition: canSubmit,
    currentState: scenario.currentState,
    requiresApprovalSha: evidence.humanGate,
    transitionActor: 'HUMAN',
    transitionAmendment: scenario.amendment,
    transitionApprovalSha: scenario.approvalSha,
    transitionDate: '2026-09-26',
    transitionError: scenario.error,
    transitionRuling: scenario.ruling,
    transitionSubmitting: false,
    transitionTarget: scenario.target,
    onActorChange: noop,
    onAmendmentChange: noop,
    onApprovalShaChange: noop,
    onDateChange: noop,
    onRulingChange: noop,
    onSubmit: noop,
    onTargetChange: noop
  };
  return renderToStaticMarkup(
    scenario.form === 'workbench' ? (
      <WorkbenchLifecycleTransitionForm {...props} />
    ) : (
      <PipelineLifecycleTransitionForm {...props} />
    )
  );
}

const outDir = process.argv[2];
if (!outDir) {
  throw new Error('usage: node render_forms.cjs <out-dir>');
}
const css = readFileSync(path.join('frontend', 'src', 'app', 'globals.css'), 'utf8');
for (const scenario of SCENARIOS) {
  const html = `<!doctype html>
<html lang="en" data-theme="light"><head><meta charset="utf-8"><title>${scenario.name}</title>
<style>${css}</style>
<style>body { margin: 0; padding: 16px; background: var(--ground, #fff); } .frame { max-width: 760px; }</style>
</head><body><div class="frame"><article class="pipeline-contracts">${render(scenario)}</article></div></body></html>
`;
  writeFileSync(path.join(outDir, `${scenario.name}.html`), html);
}
console.log(SCENARIOS.map((scenario) => scenario.name).join('\n'));
