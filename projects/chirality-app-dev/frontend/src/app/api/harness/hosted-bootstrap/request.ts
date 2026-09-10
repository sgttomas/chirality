import { HarnessError } from '@chirality/runtime-contracts/errors';
import { readJsonBody, requireNonEmptyString } from '../../../../lib/harness/http';

type HostedBootstrapRequest = {
  projectRoot?: unknown;
  consent?: unknown;
};

export async function readHostedBootstrapProjectRoot(
  request: Request,
  requireConsent = false
): Promise<string> {
  const body = await readJsonBody<HostedBootstrapRequest>(request);
  if (requireConsent && body.consent !== true) {
    throw new HarnessError(
      'INVALID_REQUEST',
      400,
      "Field 'consent' must be true"
    );
  }
  return requireNonEmptyString(body.projectRoot, 'projectRoot');
}
