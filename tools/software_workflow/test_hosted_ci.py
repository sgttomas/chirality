"""Real-diff routing and aggregate failures for hosted App/PEC coverage."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import sys
import unittest
from unittest.mock import patch

from hosted_ci import (aggregate, desktop_plan, desktop_rust_plan, make_plan, select_paths, validate_plan, numerical_plan,
                       ROOT as SOURCE_ROOT, SUITES, WASM_ENGINE_CRATES)

PROFILE = json.loads((Path(__file__).resolve().parents[1] / "hosted-ci-routing.json").read_text())


def modes(**overrides):
    return {**dict.fromkeys(SUITES, "not-applicable"), **overrides}


class HostedCITests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "ci-test@example.invalid")
        self.git("config", "user.name", "CI routing fixture")
        self.write("README.md")
        self.base = self.commit()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.PIPE).decode().strip()

    def write(self, path, content="fixture"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def plan(self, base=None, event="pull_request"):
        return make_plan(self.root, PROFILE, event, base or self.base, "HEAD")

    def test_evergreen_instruction_pr_uses_only_bundle_and_governance(self):
        paths = ["AGENTS.md", "docs/SPEC.md", "projects/chirality-app-dev/AGENTS.md",
                 "projects/chirality-app-dev/loop/LOOP_INIT.md", "projects/chirality-piping/AGENTS.md",
                 "projects/chirality-piping/loop/LOOP_INIT.md",
                 "workflows/construct-local-work-graph/WORKFLOW.md",
                 "workflows/construct-local-work-graph/resources/work-graph-template.md"]
        paths += [f"projects/{p}/execution/_Coordination/NOTICE.md" for p in
                  ["chirality-app-dev", "chirality-piping", "chirality-runtime", "pec"]]
        for path in paths:
            self.write(path)
        self.commit()
        # This temporary Git fixture models a diff, not a product checkout.
        # Supply the actual repository source graph for its records-only paths.
        with patch('hosted_ci.numerical_plan', side_effect=lambda root, paths, profile: numerical_plan(SOURCE_ROOT, paths, profile)), \
             patch('hosted_ci.desktop_plan', side_effect=lambda root, *args: desktop_plan(SOURCE_ROOT, *args)), \
             patch('hosted_ci.desktop_rust_plan', side_effect=lambda root, *args: desktop_rust_plan(SOURCE_ROOT, *args)):
            self.assertEqual(self.plan()["modes"], modes(**{"app-v4": "full"}))

    def test_project_records_including_json_do_not_run_product_suites(self):
        paths = [f"projects/{project}/{folder}/{filename}" for project in
                 ["chirality-app-dev", "chirality-runtime", "pec"] for folder in
                 ["docs", "execution", "loop", "plans"] for filename in ["note.md", "state.json"]]
        self.assertEqual(select_paths(paths, PROFILE)["modes"], modes())

    def test_app_v4_records_and_prose_do_not_run_product_suites(self):
        paths = [f"projects/chirality-app-v4/{folder}/{filename}" for folder in
                 ["execution/_Coordination/AgentRuns/RUN", "docs", "conceptual", "foundation", "reference", "loop", "init"]
                 for filename in ["note.md", "state.json"]]
        paths += ["projects/chirality-app-v4/AGENTS.md", "projects/chirality-app-v4/README.md"]
        self.assertEqual(select_paths(paths, PROFILE)["modes"], modes())
        # Its application source selects App v4, not unrelated legacy products.
        self.assertEqual(select_paths(["projects/chirality-app-v4/app/src/main.rs"], PROFILE)["modes"],
                         modes(**{"app-v4": "full"}))

    def test_hash_bound_scope_selects_app_v4(self):
        self.assertEqual(select_paths([
            "projects/chirality-app-v4/execution/PKG-02/DEL-02-04/ScopeOfWork.md"
        ], PROFILE)["modes"], modes(**{"app-v4": "full"}))

    def test_retired_products_do_not_select_product_checks(self):
        for path, expected_modes in [
            ("projects/chirality-app-dev/frontend/src/a.tsx", modes()),
            ("projects/pec/server/src/a.ts", modes()),
            ("projects/chirality-runtime/packages/client/src/a.ts", modes()),
            ("projects/chirality-runtime/package-lock.json", modes()),
            ("projects/chirality-app-dev/instructions/AGENTS.md", modes()),
        ]:
            with self.subTest(path=path):
                self.assertEqual(select_paths([path], PROFILE)["modes"], expected_modes)

    def test_earlier_source_commit_is_not_hidden_by_later_docs(self):
        self.write("projects/chirality-app-v4/app/src/a.tsx")
        self.commit()
        self.write("docs/notes.md")
        self.commit()
        plan = self.plan()
        self.assertEqual(plan["modes"]["app-v4"], "full")
        self.assertEqual(len(plan["paths"]), 2)

    def test_consumed_doc_deletion_keeps_its_executable_app_checks(self):
        path = "projects/chirality-app-v4/execution/PKG-02/DEL-02-04/ScopeOfWork.md"
        self.write(path)
        base = self.commit()
        (self.root / path).unlink()
        self.commit()
        self.assertEqual(self.plan(base)["modes"]["app-v4"], "full")

    def test_move_from_product_to_records_still_checks_removed_product(self):
        original = "projects/chirality-app-v4/app/src/a.ts"
        self.write(original)
        base = self.commit()
        self.write("projects/chirality-app-v4/docs/a.ts")
        (self.root / original).unlink()
        self.commit()
        plan = self.plan(base)
        self.assertIn(original, plan["paths"])
        self.assertEqual(plan["modes"]["app-v4"], "full")

    def test_newline_in_filename_cannot_hide_product_path(self):
        path = "projects/chirality-app-v4/app/src/odd\nname.ts"
        self.write(path)
        self.commit()
        self.assertIn(path, self.plan()["paths"])
        self.assertEqual(self.plan()["modes"]["app-v4"], "full")

    def test_unknown_inputs_fall_back_to_owner_or_both_products(self):
        for path, expected in [
            ("projects/chirality-app-dev/new-input.bin", modes()),
            ("projects/chirality-app-dev/new-runtime/docs/input.json", modes()),
            ("projects/pec/new-input.bin", modes()),
            ("unknown-root-input.bin", dict.fromkeys(SUITES, "full")),
            ("projects/chirality-app-v4/unmapped/new-code.bin", modes(**{"app-v4": "full"})),
            # An unmatched project input also selects the full desktop suite and the desktop Rust tests.
            ("projects/chirality-piping/new-code.bin", modes(piping="full", **{"piping-desktop": "full", "piping-desktop-rust": "full", "piping-numerical": "full", "piping-python": "full"})),
        ]:
            selection = select_paths([path], PROFILE)
            self.assertEqual(selection["unmatched_paths"], [] if path.startswith(("projects/chirality-app-dev/", "projects/pec/")) else [path])
            self.assertEqual(selection["modes"], expected)

    def test_policy_changes_require_full_consumer_checks(self):
        selection = select_paths(["tools/hosted-ci-routing.json"], PROFILE)
        self.assertEqual(selection["modes"], dict.fromkeys(SUITES, "full"))

    def test_missing_base_and_manual_dispatch_request_full_coverage(self):
        for plan in [self.plan(base="missing-ref"), self.plan(event="workflow_dispatch")]:
            self.assertEqual(plan["modes"], dict.fromkeys(SUITES, "full"))

    def test_product_paths_and_consumed_design_select_without_deliverable_mappings(self):
        for path in ('projects/chirality-app-v4/app/src-tauri/src/workflow_catalog.rs',
                     'projects/chirality-app-v4/execution/PKG-04/DEL-04-03/Design/RS_RECORD.schema.json'):
            self.assertEqual(select_paths([path], PROFILE)['modes'], modes(**{'app-v4':'full'}))
        selection = select_paths(['projects/chirality-piping/core/solver/src/lib.rs'], PROFILE)
        self.assertEqual(selection['modes'], modes(piping='full', **{'piping-numerical':'full','piping-python':'full'}))
        self.assertEqual(select_paths(['projects/chirality-piping/docs/note.md'], PROFILE)['modes'], modes())

    def test_piping_python_implementation_and_tests_select_python_lane(self):
        for path in ('projects/chirality-piping/tools/product_preview/validate.py',
                     'projects/chirality-piping/tests/product_preview/test_contract.py',
                     'projects/chirality-piping/tests/security/test_permissions.py'):
            selection = select_paths([path], PROFILE)
            self.assertEqual(selection['modes']['piping-python'], 'full')
            self.assertEqual(selection['modes']['piping-numerical'], 'full' if '/tools/' in path else 'not-applicable')
            self.assertEqual(selection['modes']['piping'], 'full')

    def test_new_required_results_never_launder_missing_failed_or_cancelled_checks(self):
        for suite in SUITES:
            for state in ('failure','cancelled','skipped',''):
                self.assertFalse(aggregate(suite,'full','success',state))
            self.assertFalse(aggregate(suite,'not-applicable','failure','skipped'))
            self.assertTrue(aggregate(suite,'not-applicable','success','skipped'))
            self.assertTrue(aggregate(suite,'full','success','success'))

    def test_unselected_desktop_suite_requires_its_own_job_skipped(self):
        # The desktop suite runs in its own sharded job, skipped when unselected.
        self.assertTrue(aggregate('piping-desktop', 'not-applicable', 'success', 'skipped'))
        for state in ('success', 'failure', 'cancelled'):
            self.assertFalse(aggregate('piping-desktop', 'not-applicable', 'success', state))

    def test_aggregate_cli_failure_returns_failure_without_traceback(self):
        completed = subprocess.run([sys.executable, str(Path(__file__).with_name('hosted_ci.py')),
            'aggregate', '--suite', 'app-v4', '--mode', 'full', '--selection', 'success',
            '--product', 'skipped'], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 1)
        self.assertIn('did not complete', completed.stdout)
        self.assertNotIn('Traceback', completed.stderr)

    def test_merge_base_excludes_changes_unique_to_advanced_base(self):
        self.git('checkout', '-qb', 'candidate')
        self.write('projects/chirality-app-v4/app/src/candidate.ts')
        head = self.commit()
        self.git('checkout', '-qb', 'advanced-base', self.base)
        self.write('unknown-root-input.bin')
        advanced = self.commit()
        self.git('checkout', 'candidate')
        plan = make_plan(self.root, PROFILE, 'pull_request', advanced, head)
        self.assertEqual(plan['base'], self.base)
        self.assertEqual(plan['paths'], ['projects/chirality-app-v4/app/src/candidate.ts'])
        self.assertEqual(plan['modes'], modes(**{'app-v4': 'full'}))

    def test_renamed_fixture_keeps_old_and_new_paths(self):
        original = 'projects/chirality-piping/fixtures/old.json'
        self.write(original)
        base = self.commit()
        self.write('projects/chirality-piping/fixtures/new.json')
        (self.root / original).unlink()
        self.commit()
        plan = self.plan(base)
        self.assertEqual(plan['paths'], ['projects/chirality-piping/fixtures/new.json', original])
        self.assertEqual(plan['modes']['piping-numerical'], 'full')
        self.assertEqual(plan['piping_numerical_selection']['classification'], 'full-fallback')

    def test_execution_recomputes_exact_selection_identity(self):
        self.write('projects/chirality-app-v4/app/src/candidate.ts')
        self.commit()
        target = self.root / 'tools/hosted-ci-routing.json'
        target.parent.mkdir()
        target.write_text(json.dumps(PROFILE))
        plan = self.plan()
        validate_plan(self.root, plan)
        for key, value in [('classification', 'reachability'), ('manifests', ['core/unregistered/Cargo.toml']),
                           ('reasons', [{'kind': 'forged'}])]:
            modified = json.loads(json.dumps(plan))
            modified['piping_numerical_selection'][key] = value
            with self.assertRaisesRegex(ValueError, 'Selection differs'):
                validate_plan(self.root, modified)
        changed = dict(plan, paths=['projects/chirality-app-v4/docs/candidate.ts'])
        with self.assertRaisesRegex(ValueError, 'Selection differs'):
            validate_plan(self.root, changed)

    def test_piping_cache_control_does_not_expand_unrelated_app_coverage(self):
        # The browser result it keys now covers the desktop suite too; as a
        # shared Piping control it also selects the desktop Rust tests.
        self.assertEqual(select_paths(['tools/software_workflow/result_cache.py'], PROFILE)['modes'],
                         modes(piping='full', **{'piping-desktop': 'full', 'piping-desktop-rust': 'full', 'piping-numerical': 'full', 'piping-python': 'full'}))

    def test_desktop_suite_follows_the_inputs_it_reads_or_compiles(self):
        project = 'projects/chirality-piping/'
        for path, kind in [
            ('apps/desktop/src/App.tsx', 'desktop-source-reference'),
            ('apps/desktop/package.json', 'desktop-source-reference'),
            ('package-lock.json', 'desktop-input'),
            ('fixtures/results/new.json', 'desktop-source-reference'),
            ('validation/references/t3_r1/new.json', 'desktop-input'),
            # Docs that desktop tests read are selected although docs select no product job.
            ('docs/BUILD_AND_RELEASE.md', 'desktop-source-reference'),
            # Python a desktop test reads as text.
            ('core/analysis_runs/compatibility.py', 'desktop-source-reference'),
            # Rust compiled into the wasm engines, and a file one of them includes.
            ('core/loads/primitive_loads/src/lib.rs', 'wasm-engine-source'),
            ('core/loads/self_weight_wasm/tests/fixtures/applied_self_weight_v1.json', 'desktop-input'),
            ('validation/benchmarks/numerical_robustness/src/exact.rs', 'wasm-engine-compile-read'),
        ]:
            with self.subTest(path=path):
                selection = select_paths([project + path], PROFILE)
                self.assertEqual(selection['modes']['piping-desktop'], 'full')
                self.assertEqual(selection['modes']['piping'], 'full')
                self.assertEqual(selection['piping_desktop_selection']['reasons'], [{'path': project + path, 'kind': kind}])
        for paths in [
            # Python-only: tests and tools the desktop suite neither names nor runs.
            ['tests/test_export_public_openpipestress.py', 'tools/release/run_evidence_sweep.py'],
            # Rust-only: crates outside the wasm engines' normal/build dependencies.
            ['core/solver/performance_harness/src/lib.rs', 'core/reporting/report_package/src/lib.rs'],
            ['docs/note.md'],
        ]:
            with self.subTest(paths=paths):
                selection = select_paths([project + path for path in paths], PROFILE)
                self.assertEqual(selection['modes']['piping-desktop'], 'not-applicable')
                self.assertEqual(selection['piping_desktop_selection']['classification'], 'not-applicable')

    def test_desktop_selection_fails_toward_the_full_suite(self):
        selection = select_paths(['projects/chirality-piping/tests/test_export_public_openpipestress.py'], PROFILE, self.root)
        self.assertEqual(selection['modes']['piping-desktop'], 'full')
        self.assertEqual(selection['piping_desktop_selection']['classification'], 'full-fallback')

    def test_wasm_engine_crates_are_the_ones_the_desktop_build_compiles(self):
        script = (SOURCE_ROOT / 'projects/chirality-piping/apps/desktop/scripts/build-wasm-engine.mjs').read_text()
        for manifest in WASM_ENGINE_CRATES:
            segments = Path(manifest).parent.parts
            self.assertIn(', '.join(f'"{part}"' for part in segments), script)

    def test_desktop_resource_table_cannot_hide_new_unknown_fixture(self):
        profile = json.loads(json.dumps(PROFILE))
        profile['piping_desktop_resources']['files'].append('fixtures/new-unreviewed.json')
        selection = select_paths(['projects/chirality-piping/fixtures/new-unreviewed.json'], profile)
        numerical = selection['piping_numerical_selection']
        self.assertEqual(numerical['classification'], 'full-fallback')
        # 41 discovered crates since the pressure-source join added core/numerics/correct_norm.
        self.assertEqual(len(numerical['manifests']), 41)
        self.assertIn('Stale desktop resource declaration', numerical['fallback_reasons'][0])


    def test_desktop_rust_tests_follow_the_crate_its_path_dependencies_and_their_reads(self):
        project = 'projects/chirality-piping/'
        for path, kind in [
            # The desktop shell crate itself: Rust, manifest, lock, build script and Tauri config.
            ('apps/desktop/src-tauri/src/solve_jobs.rs', 'desktop-rust-source'),
            ('apps/desktop/src-tauri/Cargo.lock', 'desktop-rust-source'),
            ('apps/desktop/src-tauri/build.rs', 'desktop-rust-source'),
            ('apps/desktop/src-tauri/tauri.conf.json', 'desktop-rust-source'),
            # Direct and transitive Cargo path dependencies.
            ('core/units/src/lib.rs', 'path-dependency-source'),
            ('core/model_operations/operation_applier/Cargo.toml', 'path-dependency-source'),
            ('core/solver/frame_kernel/src/lib.rs', 'path-dependency-source'),
            # A fixture the crate compiles in, and fixtures its tests read by a literal or a format template.
            ('fixtures/model_document/invented_every_slot_model.json', 'desktop-rust-compile-read'),
            ('fixtures/product_preview/r2_from_blank_rehearsal.json', 'desktop-rust-source-reference'),
            ('fixtures/results/new_exact_source.json', 'desktop-rust-source-reference'),
            # Files a path dependency's compiled source or build script reads (declared): the
            # product_physics build script reads its own sources.
            ('fixtures/rule_expressions/checksum_binding/payload_grammar_v1_0_0.json', 'path-dependency-runtime-read'),
            ('core/product_physics/src/bend_pressure.rs', 'path-dependency-runtime-read'),
        ]:
            with self.subTest(path=path):
                selection = select_paths([project + path], PROFILE)
                self.assertEqual(selection['modes']['piping-desktop-rust'], 'full')
                self.assertIn('piping-desktop-rust', selection['checks'])
                self.assertEqual(selection['piping_desktop_rust_selection']['reasons'], [{'path': project + path, 'kind': kind}])
        for paths in [
            # Desktop TypeScript, a crate outside the path dependencies, Python, docs and another product.
            [project + 'apps/desktop/src/App.tsx', project + 'apps/desktop/package.json'],
            [project + 'core/runner/headless/src/lib.rs', project + 'core/solver/performance_harness/src/lib.rs'],
            [project + 'tests/test_export_public_openpipestress.py', project + 'tools/release/run_evidence_sweep.py'],
            [project + 'docs/note.md'],
            ['projects/chirality-app-v4/app/src-tauri/src/workflow_catalog.rs'],
        ]:
            with self.subTest(paths=paths):
                selection = select_paths(paths, PROFILE)
                self.assertEqual(selection['modes']['piping-desktop-rust'], 'not-applicable')
                self.assertNotIn('piping-desktop-rust', selection['checks'])
                self.assertEqual(selection['piping_desktop_rust_selection']['classification'], 'not-applicable')

    def test_desktop_rust_tests_run_for_shared_controls_unmatched_inputs_and_full_coverage(self):
        for path, kind in [('tools/hosted-ci-routing.json', 'shared-input'),
                           ('.github/workflows/piping-desktop-e2e.yml', 'shared-input'),
                           # Its dependency cache is keyed and trimmed here.
                           ('tools/software_workflow/build_cache.py', 'shared-input'),
                           ('.github/workflows/shared-build-cache.yml', 'shared-input'),
                           ('projects/chirality-piping/new-code.bin', 'unmatched-input'),
                           ('unknown-root-input.bin', 'shared-input')]:
            with self.subTest(path=path):
                selection = select_paths([path], PROFILE)
                self.assertEqual(selection['modes']['piping-desktop-rust'], 'full')
                self.assertEqual(selection['piping_desktop_rust_selection']['reasons'], [{'path': path, 'kind': kind}])
        for plan in [self.plan(base='missing-ref'), self.plan(event='workflow_dispatch')]:
            self.assertEqual(plan['modes']['piping-desktop-rust'], 'full')
            self.assertEqual(plan['piping_desktop_rust_selection']['classification'], 'full-fallback')

    def test_desktop_rust_selection_fails_toward_running_the_tests(self):
        # No readable crate in this fixture checkout.
        selection = select_paths(['projects/chirality-piping/tests/test_export_public_openpipestress.py'], PROFILE, self.root)
        self.assertEqual(selection['modes']['piping-desktop-rust'], 'full')
        self.assertEqual(selection['piping_desktop_rust_selection']['classification'], 'full-fallback')
        # A stale runtime-read declaration in a path dependency also fails toward the tests.
        profile = json.loads(json.dumps(PROFILE))
        profile['piping_runtime_reads']['reads']['core/rules/rule_pack_lifecycle/src/lib.rs']['sha256'] = '0' * 64
        selection = select_paths(['projects/chirality-piping/tests/test_export_public_openpipestress.py'], profile)
        self.assertEqual(selection['piping_desktop_rust_selection']['classification'], 'full-fallback')
        self.assertIn('stale runtime read declaration', selection['piping_desktop_rust_selection']['fallback_reasons'][0])

    def test_desktop_rust_closure_is_every_path_dependency_the_crate_compiles(self):
        import tomllib
        from hosted_ci import DESKTOP_RUST_CRATE, compiled_crate_inputs
        project = SOURCE_ROOT / 'projects/chirality-piping'
        manifest = tomllib.loads((project / DESKTOP_RUST_CRATE / 'Cargo.toml').read_text())
        direct = {Path(os.path.normpath(Path(DESKTOP_RUST_CRATE) / spec['path'])).as_posix()
                  for key in ('dependencies', 'dev-dependencies', 'build-dependencies')
                  for spec in manifest.get(key, {}).values() if isinstance(spec, dict) and 'path' in spec}
        crates, _ = compiled_crate_inputs(SOURCE_ROOT, (DESKTOP_RUST_CRATE + '/Cargo.toml',), True, 'desktop Rust')
        self.assertTrue(direct)
        self.assertLessEqual(direct | {DESKTOP_RUST_CRATE}, crates)
        # Transitive: the applier's solver dependencies are compiled in too.
        self.assertIn('core/solver/frame_kernel', crates)


if __name__ == "__main__":
    unittest.main()
