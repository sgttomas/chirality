"""I110 round 3, G11: refuse a flexibility-consuming expansion joint that lacks a user stiffness value."""
import sys
p = sys.argv[1]
s = open(p).read()
anchor = '''        let lateral = component.modifiers.as_ref().and_then(|m| m.lateral_stiffness_user_value.as_ref()).map(|q| q.value);
        if !lateral.is_some_and(|k| k != 0.0) {
            continue;
        }
'''
fix = '''        // G11 (I111): the element builder needs all four user stiffness values and
        // skips a joint that lacks one, so the model would solve without the joint
        // while the joint's review rows say its stiffness was consumed. Refuse instead.
        let modifiers = component.modifiers.as_ref();
        let missing: Vec<&str> = [
            ("axial", modifiers.and_then(|m| m.axial_stiffness_user_value.as_ref())),
            ("lateral", modifiers.and_then(|m| m.lateral_stiffness_user_value.as_ref())),
            ("angular", modifiers.and_then(|m| m.angular_stiffness_user_value.as_ref())),
            ("torsional", modifiers.and_then(|m| m.torsional_stiffness_user_value.as_ref())),
        ]
        .into_iter()
        .filter_map(|(axis, value)| value.is_none().then_some(axis))
        .collect();
        if !missing.is_empty() {
            let mut refs = vec![component.id.clone()];
            refs.extend(
                component
                    .geometry
                    .as_ref()
                    .and_then(|g| g.expansion_joint_pipe_ref.as_deref())
                    .filter(|id| !id.trim().is_empty())
                    .map(str::to_string),
            );
            diagnostics.push(diag(
                &format!("diagnostic:preview-physics:joint-stiffness-incomplete:{}", identity(&[&component.id])),
                "JOINT_ELEMENT_STIFFNESS_INCOMPLETE",
                "blocking",
                format!("expansion joint {} declares mechanics_geometry_and_user_flexibility but has no user-entered {} stiffness, so its user-stiffness element cannot be assembled; the solve is refused rather than published without the joint (G11)", component.id, missing.join(", ")),
                refs,
            ));
            continue;
        }
'''
assert s.count(anchor) == 1
s = s.replace(anchor, fix + anchor)
doc_old = '''/// result of the model is suspect. Refuse the solve until T4 repairs it.
pub(crate) fn refuse_unqualified_joint_elements('''
doc_new = '''/// result of the model is suspect. Refuse the solve until T4 repairs it. A joint
/// that declares user flexibility without all four user stiffness values is
/// refused too (G11): the element builder would skip it silently.
pub(crate) fn refuse_unqualified_joint_elements('''
assert s.count(doc_old) == 1
s = s.replace(doc_old, doc_new)
open(p, 'w').write(s)
print("applied")
