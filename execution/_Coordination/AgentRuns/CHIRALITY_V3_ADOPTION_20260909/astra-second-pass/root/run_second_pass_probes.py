"""Independent behavioral probes; outputs only below this review directory."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[5]
sys.path[:0] = [str(ROOT/'tools/validation'), str(ROOT/'tools/workflow_runtime')]
from build_workflow_index import CENTRAL, _frontmatter, validate_and_build
from resolve_workflow import resolve
from validate_workflow_metadata import validate_workflow_dir
from validate_skill_metadata import validate_skill_dir


def fixture(base):
    workflows = base/'workflows'
    workflows.mkdir(parents=True)
    (workflows/'catalog.yaml').write_text(json.dumps({'schema':'chirality-workflow-catalog/v1','library':{'source':'bundled','sourceRootId':'fixture-bundle'},'centralWorkflowNames':list(CENTRAL)}))
    (workflows/'legacy-agents.json').write_text(json.dumps({'schema_version':1,'aliases':{}}))
    (workflows/'legacy-methods.json').write_text(json.dumps({'schema':'chirality-legacy-methods/v1','convertedWorkflowAliases':{},'historicalOnly':[],'unknownLegacyBehavior':'error'}))
    for name in CENTRAL:
        folder=workflows/name; folder.mkdir()
        (folder/'WORKFLOW.md').write_text(f'---\nname: {name}\ndescription: Fixture\n---\n')
        (folder/'execution.json').write_text(json.dumps({'schema_version':1,'compatible_roles':['WORKING_ITEMS']}))
    return base


def expect_rejection(fn):
    try:
        fn()
    except (ValueError, OSError) as exc:
        return {'pass':True,'rejection':str(exc)}
    return {'pass':False,'error':'Unexpected acceptance'}


results=[]
with tempfile.TemporaryDirectory(dir=OUT) as temporary:
    temp=Path(temporary)
    base=fixture(temp/'root')
    lib=base/'.agents/skills'; lib.mkdir(parents=True)
    outside=temp/'external'; outside.mkdir()
    (outside/'SKILL.md').write_text('---\nname: outside\ndescription: External bytes\n---\n')
    link=lib/'outside';link.symlink_to(outside)
    results.append({'case':'skill-package-escape',**expect_rejection(lambda:validate_and_build(base))})
    link.unlink()
    lib.rmdir(); lib.symlink_to(temp/'external-library');(temp/'external-library').mkdir()
    package=temp/'external-library'/'outside';package.mkdir();(package/'SKILL.md').write_text('---\nname: outside\ndescription: Outside library\n---\n')
    results.append({'case':'skill-library-escape',**expect_rejection(lambda:validate_and_build(base))})
    lib.unlink();lib.mkdir()
    for name in ['a--b','ends-', 'a'*65]:
        package=lib/name;package.mkdir();(package/'SKILL.md').write_text(f'---\nname: {name}\ndescription: Invalid name\n---\n')
        results.append({'case':'invalid-name-'+name,**expect_rejection(lambda:validate_and_build(base))})
        standalone=validate_skill_dir(package,base)
        results.append({'case':'standalone-skill-invalid-name-'+name,'pass':not standalone['valid'],'issues':standalone['issues']})
        (package/'SKILL.md').unlink();package.rmdir()
    for description in ['before---after', '"quoted --- text"', '>\n  folded --- words\n  continue']:
        p=temp/'SKILL.md';p.write_text(f'---\nname: example\ndescription: {description}\n---\nBody\n')
        expected={'before---after':'before---after','"quoted --- text"':'quoted --- text','>\n  folded --- words\n  continue':'folded --- words continue'}[description]
        value=_frontmatter(p)['description']
        results.append({'case':'frontmatter-'+description,'pass':value==expected,'actual':value,'expected':expected})
    (base/'workflows'/CENTRAL[0]/'execution.json').unlink()
    try:
        catalog=validate_and_build(base)
        item=next(x for x in catalog['methods'] if x['name']==CENTRAL[0])
        results.append({'case':'optional-workflow-execution','pass':set(item['executionRoleIds'])=={'HELP_HUMAN','HELPS_HUMANS','WORKING_ITEMS','TASK'} and 'execution' not in item})
    except Exception as exc:
        results.append({'case':'optional-workflow-execution','pass':False,'error':str(exc)})
    policy=base/'workflows'/CENTRAL[0]/'execution.json'
    policy.write_text(json.dumps({'schema_version':1,'compatible_roles':[]}))
    try:
        item=next(x for x in validate_and_build(base)['methods'] if x['name']==CENTRAL[0])
        results.append({'case':'empty-role-list-denies','pass':item['executionRoleIds']==[] and item['execution']['compatibleRoles']==[]})
        standalone=validate_workflow_dir(base/'workflows'/CENTRAL[0],base)
        results.append({'case':'standalone-workflow-empty-role-list','pass':standalone['valid'],'issues':standalone['issues']})
    except Exception as exc:
        results.append({'case':'empty-role-list-denies','pass':False,'error':str(exc)})
    for roles in ['TASK',['UNKNOWN']]:
        policy.write_text(json.dumps({'schema_version':1,'compatible_roles':roles}))
        results.append({'case':'malformed-roles-'+str(roles),**expect_rejection(lambda:validate_and_build(base))})
results.append({'case':'unregistered-qualified-source',**expect_rejection(lambda:resolve(ROOT,'TASK',methods=[{'kind':'skill','name':'researcher','source':'user','sourceRootId':'unregistered-user'}]))})
source_paths=['tools/validation/build_workflow_index.py','tools/validation/validate_skill_metadata.py','tools/workflow_runtime/resolve_workflow.py']
report={'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths},'results':results,'pass':all(x['pass'] for x in results)}
print(json.dumps(report,indent=2))
raise SystemExit(0 if report['pass'] else 1)
