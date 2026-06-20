'use client';

import { LoopTertiaryShell } from '../../components/shell/loop-tertiary-shell';

export default function WorkbenchClient(): JSX.Element {
  return (
    <LoopTertiaryShell
      defaultSidebarTab="workbench"
      section="WORKBENCH"
      title="Workbench"
      subtitle="Run the live loop while reviewing persona context and deliverable contracts in the sidebar."
    />
  );
}
