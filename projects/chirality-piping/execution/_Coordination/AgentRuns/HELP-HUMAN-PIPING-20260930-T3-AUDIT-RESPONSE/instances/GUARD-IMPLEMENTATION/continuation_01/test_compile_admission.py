"""Pure fake-file argv regressions for GR-01/02; no native operations."""
from contextlib import ExitStack
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from harness import HERE, FORBIDDEN, blocked, original, original_guard, v2 as guard

CASES = json.loads((HERE / 'regression_inputs.json').read_text())['cases']
BINARY = b'fake rustup proxy bytes'


def make_job(argv):
    return {
        'job_id': 'pure-v2-schema', 'run_id': guard.RUN_ID,
        'candidate_sha': 'a' * 40, 'kind': 'compile',
        'containment': 'inherited-group', 'cwd': '/fake/workspace',
        'command': argv,
        'env': {'RUSTUP_TOOLCHAIN': '1.97.1', 'RUSTUP_AUTO_INSTALL': '0',
                'CARGO_INCREMENTAL': '0', 'CARGO_BUILD_JOBS': '1', 'RUST_TEST_THREADS': '1'},
        'input_hashes': {'/fake/cargo': guard.hashlib.sha256(BINARY).hexdigest(),
                        '/fake/rustc': guard.hashlib.sha256(BINARY).hexdigest()},
        'limits': {'cap_bytes': 128 * guard.MIB, 'allowance_bytes': 64 * guard.MIB,
                   'disk_write_budget_bytes': 64 * guard.MIB,
                   'disk_reserve_bytes': guard.GIB, 'max_seconds': 8},
    }


def attempt(job, module=guard):
    raw = json.dumps(job).encode()
    def fake_open(path, mode):
        assert mode == 'rb'
        values = {'/fake/job.json': raw, '/fake/cargo': BINARY, '/fake/rustc': BINARY}
        return io.BytesIO(values[str(path)])
    with ExitStack() as fence:
        for target in FORBIDDEN:
            fence.enter_context(patch(target, side_effect=blocked))
        fence.enter_context(patch.object(Path, 'is_dir', return_value=True))
        fence.enter_context(patch('builtins.open', side_effect=fake_open))
        try:
            actual, _ = module.read_job(Path('/fake/job.json'))
            assert actual == job
            return {'accepted': True}
        except module.Refusal as exc:
            return {'accepted': False, 'reason': str(exc)}


class PreservedValidation(original.PureCase):
    def test_original_review_witness_reproduces_on_preserved_v1(self):
        for case in CASES[:4]:
            with self.subTest(case=case['name']):
                self.assertTrue(attempt(make_job(case['argv']), original_guard)['accepted'])

    def test_environment_contract_still_required(self):
        for key in make_job(CASES[0]['argv'])['env']:
            job = make_job(CASES[0]['argv'])
            job['env'][key] = 'incompatible'
            with self.subTest(key=key):
                self.assertEqual(attempt(job), {'accepted': False, 'reason': 'compile-environment-not-pinned-and-serial'})

    def test_executable_content_pin_still_required(self):
        job = make_job(CASES[0]['argv'])
        job['input_hashes']['/fake/cargo'] = '0' * 64
        self.assertEqual(attempt(job), {'accepted': False, 'reason': 'input-hash-mismatch'})
        job = make_job(CASES[0]['argv'])
        del job['input_hashes']['/fake/cargo']
        self.assertEqual(attempt(job), {'accepted': False, 'reason': 'executable-hash-required'})


class CommandCases(original.PureCase):
    pass


def test_for(case):
    def test(self):
        actual = attempt(make_job(case['argv']))
        self.assertEqual(actual['accepted'], case['expected_accept'],
                         json.dumps({'case': case, 'actual': actual}))
    return test


for index, case in enumerate(CASES):
    # Numeric names avoid punctuation from selector values in test identifiers.
    test = test_for(case)
    test.__doc__ = case['name']
    setattr(CommandCases, 'test_case_%02d' % index, test)


if __name__ == '__main__':
    unittest.main(verbosity=2)
