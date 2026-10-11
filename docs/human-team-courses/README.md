# Project Practice for Human Teams

This series teaches project management and project engineering for human teams. It contains twelve courses, from individual practice to complex project leadership.

Use the courses to prepare, perform, examine, and coordinate professional work. Develop the technical knowledge of your discipline alongside this series.

## Start the series

Read the courses in the order below. Each course contains lessons, a worked example, practice, a knowledge check, and an assessed assignment.

Use the [Northbank case](case-study.html) for the exercises. Use the [glossary](glossary.html) for shared terms. Instructors use the [teaching guide](instructor-guide.html).

| No | Course | Learning result |
| --- | --- | --- |
| 01 | [Professional Practice and Responsibility](courses/01-professional-practice.html) | Explain responsibilities, competence limits, and decision rights. |
| 02 | [Document and Configuration Control](courses/02-document-control.html) | Establish a controlled basis and trace a change. |
| 03 | [Information Research and Evidence](courses/03-information-evidence.html) | Prepare information that another person can find and examine. |
| 04 | [Interpreting Requirements and Obligations](courses/04-requirements-interpretation.html) | Establish applicability and explain an interpretation. |
| 05 | [Reasoning, Uncertainty, and Professional Judgment](courses/05-reasoning-judgment.html) | Defend a recommendation and state its limits. |
| 06 | [Communication and Working Relationships](courses/06-working-relationships.html) | Establish understanding, decisions, and workable responsibilities. |
| 07 | [Defining an Engineering Project](courses/07-project-definition.html) | Prepare a coherent basis and division of work. |
| 08 | [Planning and Managing Project Execution](courses/08-project-execution.html) | Maintain a credible plan, cost forecast, and response to change. |
| 09 | [Project Engineering and Technical Integration](courses/09-technical-integration.html) | Coordinate disciplines and assess interface changes. |
| 10 | [Assurance, Delivery, and Handover](courses/10-assurance-handover.html) | Establish grounds for use and transfer continuing responsibilities. |
| 11 | [Leading Complex Projects](courses/11-complex-projects.html) | Diagnose a troubled project and defend its next direction. |
| 12 | [Integrated Project Practicum](courses/12-project-practicum.html) | Deliver and defend a combined team result. |

Courses 01 to 04 establish professional and information foundations. Courses 05 to 07 connect reasoning, relationships, and project definition. Courses 08 to 10 address execution, technical integration, and delivery. Courses 11 and 12 address complexity and integrated practice.

The learning order does not prescribe a fixed project sequence. Real projects develop their basis, plans, design, and assurance together.

## Study with a team

1. Read the lesson before the session.
2. Discuss the worked example.
3. Complete the practice without the instructor answers.
4. Prepare the assessed assignment.
5. Ask another participant to challenge its basis and conclusions.
6. Repair the assignment where the challenge identifies a defect.
7. Explain the repair and its effects on connected work.

Keep your course outputs in one learning portfolio. Identify each output and its revision. Link to supporting evidence instead of copying it repeatedly.

Use a mentor for individual study. The mentor can challenge the evidence, interpretation, and proposed reliance. Course 12 requires a team or a facilitated role exercise.

## Assessment

Each course states observable criteria for its assignment. The instructor uses three ratings: meets the criterion, needs repair, or has insufficient evidence.

Meet each criterion before closing the assignment. A strong presentation does not compensate for an unsupported conclusion. Correct errors, then show the affected work again.

Different solutions can satisfy a criterion. Explain the source basis, authority, reasoning, uncertainty, and consequences of your solution.

The series provides training materials. It does not grant professional authority or establish competence for every technical assignment. Use the actual jurisdiction, appointment, and professional requirements for real work.

## Source and reading editions

The Markdown files are the maintained course source. Each HTML file renders its matching source. Open `index.html` to read the series offline. Follow external references when a network connection is available.

The source files are in `courses/`, `instructors/`, and this directory. Instructor guides include answer guidance. Keep them separate from a learner assessment when necessary.

Read [References](references.html) for source roles and further reading. The existing Chirality manuals retain their edition identities. This series adapts their project principles for human teams. It does not change their text or repository instructions.

## Render the reading editions

The renderer uses the dependencies in `../alignment-manual/requirements.txt`. Run these commands from the repository root:

```sh
python3 -m venv /tmp/chirality-course-renderer
/tmp/chirality-course-renderer/bin/python -m pip install -r docs/alignment-manual/requirements.txt
```

Render all Markdown files with the explicit edition basis below:

```sh
/tmp/chirality-course-renderer/bin/python - <<'PY'
from pathlib import Path
import subprocess
root = Path('docs/human-team-courses')
for source in sorted(root.rglob('*.md')):
    output = source.with_name('index.html') if source.name == 'README.md' else source.with_suffix('.html')
    subprocess.run([
        '/tmp/chirality-course-renderer/bin/python',
        'docs/alignment-manual/render_manual.py',
        '--source', str(source), '--output', str(output),
        '--basis-date', '2026-10-11',
        '--basis-revision', '26d04270617c405fc3ca131d2ea6c86120ecc5ed',
        '--edition-label', 'Human team courses', '--metadata-at-end',
    ], check=True)
PY
```

The basis revision identifies the repository used to prepare this edition. Each source fingerprint identifies the actual rendered Markdown bytes. Add `--check` to the renderer arguments to check currency without writing.

After a source change, regenerate the affected HTML. Check navigation and content at desktop and narrow widths. Check print layout before distributing a printed copy.
