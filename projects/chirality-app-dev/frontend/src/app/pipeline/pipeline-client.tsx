'use client';

import { LoopTertiaryShell } from '../../components/shell/loop-tertiary-shell';

export default function PipelineClient(): JSX.Element {
  return (
    <LoopTertiaryShell
      defaultSidebarTab="pipeline"
      section="PIPELINE"
      title="Pipeline"
      subtitle="Run the live loop while configuring operative DECOMP, PREP, TASK, and AUDIT forms in the sidebar."
    />
  );
}
