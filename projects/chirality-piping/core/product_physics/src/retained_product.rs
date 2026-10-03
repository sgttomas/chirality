//! Private same-run diagnostic adapter. Public entrypoints never construct it.
#![allow(dead_code)]
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api as k;

#[derive(Debug)]
pub(super) enum MaterialSelector {
    Point(String),
    Temperature(u64),
}
#[derive(Debug)]
pub(super) struct MaterialSelection {
    pub case: String,
    pub material: String,
    pub material_ordinal: usize,
    pub selected: k::ProductMaterial,
    pub alpha: Option<f64>,
    pub selector: MaterialSelector,
    pub point_ids: (String, Option<String>),
    pub source_alpha: [Option<f64>; 2],
}
#[derive(Debug)]
pub(super) struct BasisRecord {
    pub case: String,
    pub selector: MaterialSelector,
    pub text: String,
}
#[derive(Debug)]
pub(super) struct TermIdentity {
    pub original: usize,
    pub occurrence: usize,
    pub canonical: usize,
    pub id: String,
    pub dof: usize,
    pub bits: u64,
}
#[derive(Debug)]
pub(super) struct MemberIdentity {
    pub model: usize,
    pub built: usize,
    pub id: String,
    pub material: usize,
    pub nodes: [usize; 2],
}
#[derive(Debug)]
pub(super) struct SpringIdentity {
    pub boundary: usize,
    pub support: usize,
    pub dof: usize,
    pub bits: u64,
}
#[derive(Debug)]
pub(super) struct ObservationValue {
    pub value_bits: u64,
    pub basis: String,
}
#[derive(Debug)]
pub(super) struct SolverObservations {
    pub case: String,
    pub mode: PreviewSolverMode,
    pub mode_row: ObservationValue,
    /// Independent producing-prefix fact, never inferred from the owned snapshot.
    pub parity_produced: bool,
    pub parity: Option<ObservationValue>,
}
#[derive(Debug)]
pub(super) enum CaptureError {
    Association(String),
    CountRange(&'static str),
    Storage(&'static str),
    Accounting(AdapterFault),
    Source(k::SourceError),
    Origin(k::OriginError),
    NativeUnavailable,
}
#[derive(Default)]
pub(super) struct ProductCapture {
    pub adapter: AdapterWork,
    pub invocation_calls: usize,
    pub invocation_mode: Option<PreviewSolverMode>,
    pub observation_calls: usize,
    pub observations: Option<SolverObservations>,
    /// Successfully allocated case/mode-basis/parity-basis capacities, even on later failure.
    pub observation_capacity_bytes: [usize; 3],
    #[cfg(test)]
    pub observation_storage_failure: Option<usize>,
    pub normalized_calls: usize,
    pub case_calls: usize,
    pub final_calls: usize,
    pub request_materials: bool,
    pub nodes: Vec<(String, [f64; 3])>,
    pub materials: Vec<(String, f64, f64)>,
    pub selections: Vec<MaterialSelection>,
    pub basis_record: Option<BasisRecord>,
    pub basis_record_calls: usize,
    /// Set from the actual source case, independently of successful text capture.
    pub basis_expected: bool,
    pub members: Vec<MemberIdentity>,
    pub terms: Vec<TermIdentity>,
    pub supports: Vec<(String, usize)>,
    pub spring_map: Vec<SpringIdentity>,
    pub support_fixed: Vec<[bool; 6]>,
    /// Actual capacity bytes: built-used, spring-used, rigid-owned, spring-map,
    /// source springs, group child lists (sum), fixed-component maps.
    pub support_capacity_bytes: [usize; 7],
    pub facts: Vec<k::ProductMemberFacts>,
    pub source: Option<k::PrimitiveSource>,
    pub case_id: String,
    pub error: Option<CaptureError>,
    pub verdicts: Vec<k::ProductRowVerdict>,
    pub numeric_failure: Option<k::ProductFailure>,
    pub numeric_pass: bool,
    pub observable_error: Option<CaptureError>,
    pub native: Option<(k::RecordedInvocation, k::RecordedCase)>,
    pub operational: Vec<OperationalSpent>,
    pub g5a_work: ScalarWork,
    pub g5a_error: Option<G5aFailure>,
    pub summary_coverage: Vec<k::ProductSummaryCoverage>,
    pub source_correction_calls: Option<k::WorkTotal>,
    pub work: String,
    pub capacities: Vec<(&'static str, usize)>,
}
impl ProductCapture {
    pub(super) fn invocation(
        &mut self,
        capture: Option<&source_receipt::CapturedInvocation>,
        mode: PreviewSolverMode,
    ) {
        if self.error.is_some() { return; }
        let Some(calls) = self.invocation_calls.checked_add(1) else { self.fail_count("invocation calls"); return; };
        self.invocation_calls = calls;
        if calls != 1 { self.fail("duplicate invocation capture"); return; }
        if capture.is_none_or(|c| c.mode() != mode) {
            self.fail("missing/mismatched actual invocation capture");
            return;
        }
        if !self.adapter.enter(AdapterEvent::MapWrite, 1) { self.fail("invocation accounting"); return; }
        self.invocation_mode = Some(mode);
    }
    fn fail(&mut self, s: impl Into<String>) {
        if self.error.is_none() {
            self.error = Some(
                self.adapter
                    .fault
                    .get()
                    .map(CaptureError::Accounting)
                    .unwrap_or_else(|| CaptureError::Association(s.into())),
            );
        }
    }
    fn fail_count(&mut self, s: &'static str) {
        if self.error.is_none() {
            self.error = Some(CaptureError::CountRange(s));
        }
    }
    pub fn normalized(
        &mut self,
        model: &PreviewModel,
        materials: &[MaterialInput],
        request_materials: bool,
    ) {
        self.normalized_calls = self.normalized_calls.checked_add(1).expect("bounded calls");
        if self.normalized_calls != 1 {
            self.fail("capture reused across invocations");
            return;
        }
        if u32::try_from(model.nodes.len()).is_err()
            || model.nodes.len().checked_mul(6).is_none()
            || u32::try_from(model.pipe_segments.len())
                .ok()
                .and_then(|m| m.checked_mul(3))
                .is_none()
            || u32::try_from(model.supports.len()).is_err()
        {
            self.fail_count("source count range");
            return;
        }
        if !self.adapter.enter(AdapterEvent::LibraryBoundary, 1) {
            self.fail("normalization capture accounting");
            return;
        }
        self.request_materials = request_materials;
        if pressure_runtime::is_exact(model)
            || case_state::is_load_state(model)
            || !model.combinations.is_empty()
            || !model.components.is_empty()
        {
            self.fail("outside private ordinary no-component/no-combination scope");
            return;
        }
        for (i, n) in model.nodes.iter().enumerate() {
            if model.nodes[..i]
                .iter()
                .any(|a| self.adapter.same(&a.id, &n.id))
            {
                self.fail("ambiguous node id");
                return;
            }
        }
        for (i, m) in materials.iter().enumerate() {
            if materials[..i]
                .iter()
                .any(|a| self.adapter.same(&a.id, &m.id))
            {
                self.fail("ambiguous material id");
                return;
            }
        }
        for (i, m) in model.pipe_segments.iter().enumerate() {
            if model.pipe_segments[..i]
                .iter()
                .any(|a| self.adapter.same(&a.id, &m.id))
            {
                self.fail("ambiguous member id");
                return;
            }
        }
        for (i, m) in model.supports.iter().enumerate() {
            if model.supports[..i]
                .iter()
                .any(|a| self.adapter.same(&a.id, &m.id))
            {
                self.fail("ambiguous support id");
                return;
            }
        }
        let captured = (|| -> Result<(), CaptureError> {
            self.nodes = self.adapter.reserve(model.nodes.len())?;
            for n in &model.nodes {
                if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                    || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
                {
                    return Err(CaptureError::Accounting(self.adapter.fault.get().unwrap()));
                }
                let id = self.adapter.copy(&n.id)?;
                if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                    return Err(CaptureError::Accounting(self.adapter.fault.get().unwrap()));
                }
                self.nodes
                    .push((id, [n.position.x, n.position.y, n.position.z]));
            }
            self.materials = self.adapter.reserve(materials.len())?;
            for m in materials {
                if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                    || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
                {
                    return Err(CaptureError::Accounting(self.adapter.fault.get().unwrap()));
                }
                let record = (
                    self.adapter.copy(&m.id)?,
                    m.elastic_modulus.value,
                    m.shear_modulus.as_ref().map_or(f64::NAN, |g| g.value),
                );
                if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                    return Err(CaptureError::Accounting(self.adapter.fault.get().unwrap()));
                }
                self.materials.push(record);
            }
            Ok(())
        })();
        if let Err(e) = captured {
            self.error = Some(e);
        }
    }
    pub fn selection(
        &mut self,
        case: &PreviewLoadCase,
        materials: &[MaterialInput],
        material: &MaterialInput,
        ordinals: Option<(usize, Option<usize>)>,
        e: f64,
        g: f64,
        alpha: Option<f64>,
    ) {
        if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
            || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
        {
            self.fail("selection accounting");
            return;
        }
        let Some(material_ordinal) = materials.iter().position(|m| std::ptr::eq(m, material))
        else {
            self.fail("material pointer");
            return;
        };
        let selected = match ordinals {
            Some((i, None)) => k::ProductMaterial::Point { ordinal: i, e, g },
            Some((lo, Some(hi))) => {
                let a = &material.temperature_points[lo];
                let b = &material.temperature_points[hi];
                k::ProductMaterial::Interpolated {
                    lower: lo,
                    upper: hi,
                    t_lo: a.temperature.as_ref().unwrap().value,
                    t: case.modulus_basis_temperature.as_ref().unwrap().value,
                    t_hi: b.temperature.as_ref().unwrap().value,
                    e_lo: a.elastic_modulus.as_ref().unwrap().value,
                    e_hi: b.elastic_modulus.as_ref().unwrap().value,
                    g_lo: a.shear_modulus.as_ref().unwrap().value,
                    g_hi: b.shear_modulus.as_ref().unwrap().value,
                    e_hat: e,
                    g_hat: g,
                }
            }
            None => {
                self.fail("missing selected point provenance");
                return;
            }
        };
        let provenance = (|| -> Result<_, CaptureError> {
            let (lo, hi) =
                ordinals.ok_or_else(|| CaptureError::Association("selected ordinals".into()))?;
            let point_ids = (
                self.adapter.copy(&material.temperature_points[lo].id)?,
                hi.map(|i| self.adapter.copy(&material.temperature_points[i].id))
                    .transpose()?,
            );
            let selector = match &load_case_selector(case) {
                Some(SelectorRef::Point(id)) => MaterialSelector::Point(self.adapter.copy(id)?),
                Some(SelectorRef::Temperature(bits)) => MaterialSelector::Temperature(*bits),
                None => return Err(CaptureError::Association("selected selector".into())),
            };
            let alpha_at = |i: usize| {
                material.temperature_points[i]
                    .thermal_expansion_coefficient
                    .as_ref()
                    .map(|a| a.value)
            };
            Ok((selector, point_ids, [alpha_at(lo), hi.and_then(alpha_at)]))
        })();
        let (selector, point_ids, source_alpha) = match provenance {
            Ok(v) => v,
            Err(e) => {
                self.error = Some(e);
                return;
            }
        };
        if let Err(e) = self.adapter.push_room(&mut self.selections) {
            self.error = Some(e);
            return;
        }
        if !self.adapter.enter(AdapterEvent::MapWrite, 1)
            || !self.adapter.enter(AdapterEvent::LibraryBoundary, 2)
        {
            self.fail("selection accounting");
            return;
        }
        // // Existing String clone boundaries; their implementation cost is unqualified.
        self.selections.push(MaterialSelection {
            case: case.id.clone(),
            material: material.id.clone(),
            material_ordinal,
            selected,
            alpha,
            selector,
            point_ids,
            source_alpha,
        });
    }
    /// Observe only the actual successful aggregate resolver return, before case_source.
    /// This owned text is a presence-record warrant, never a numerical source law.
    pub fn successful_basis_record(&mut self, case: &PreviewLoadCase, text: &str) {
        if self.error.is_some() {
            return;
        }
        let result = (|| -> Result<BasisRecord, CaptureError> {
            self.adapter.enter(AdapterEvent::SourceVisit, 1);
            self.adapter.enter(AdapterEvent::ValidationEntry, 1);
            self.adapter.require()?;
            let calls = self
                .basis_record_calls
                .checked_add(1)
                .ok_or(CaptureError::CountRange("basis record calls"))?;
            self.adapter.enter(AdapterEvent::MapWrite, 1);
            self.adapter.require()?;
            self.basis_record_calls = calls;
            if calls != 1 || self.basis_record.is_some() {
                return Err("duplicate successful basis record".into());
            }
            self.validate_selected_case(case)?;
            let selector = match load_case_selector(case) {
                Some(SelectorRef::Point(id)) => MaterialSelector::Point(self.adapter.copy(id)?),
                Some(SelectorRef::Temperature(bits)) => MaterialSelector::Temperature(bits),
                None => return Err("unexpected base basis record".into()),
            };
            Ok(BasisRecord {
                case: self.adapter.copy(&case.id)?,
                selector,
                text: self.adapter.copy(text)?,
            })
        })();
        match result {
            Ok(record) => {
                if self.adapter.enter(AdapterEvent::MapWrite, 1) {
                    self.basis_record = Some(record);
                } else {
                    self.fail("basis record write accounting");
                }
            }
            Err(e) => self.error = Some(e),
        }
    }
    fn selector_matches(
        &self,
        selected: &MaterialSelector,
        case: &PreviewLoadCase,
    ) -> Result<bool, CaptureError> {
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.require()?;
        let matches = match (selected, load_case_selector(case)) {
            (MaterialSelector::Point(a), Some(SelectorRef::Point(b))) => self.adapter.same(a, b),
            (MaterialSelector::Temperature(a), Some(SelectorRef::Temperature(b))) => *a == b,
            _ => false,
        };
        self.adapter.require()?;
        Ok(matches)
    }
    fn validate_selected_case(&self, case: &PreviewLoadCase) -> Result<(), CaptureError> {
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.require()?;
        if load_case_selector(case).is_none() || self.selections.is_empty() {
            return Err("missing selected basis source".into());
        }
        for selection in &self.selections {
            self.adapter.enter(AdapterEvent::SourceVisit, 1);
            self.adapter.require()?;
            let same_case = self.adapter.same(&selection.case, &case.id);
            self.adapter.require()?;
            if !same_case || !self.selector_matches(&selection.selector, case)? {
                return Err("basis record source case/selector".into());
            }
        }
        Ok(())
    }
    fn basis_source_case(&mut self, case: &PreviewLoadCase) -> Result<(), CaptureError> {
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.enter(AdapterEvent::MapWrite, 1);
        self.adapter.require()?;
        self.basis_expected = load_case_selector(case).is_some();
        match (self.basis_expected, &self.basis_record) {
            (false, None) if self.basis_record_calls == 0 => Ok(()),
            (true, Some(record)) if self.basis_record_calls == 1 => {
                self.validate_selected_case(case)?;
                let same_case = self.adapter.same(&record.case, &case.id);
                self.adapter.require()?;
                if !same_case || !self.selector_matches(&record.selector, case)? {
                    return Err("basis record producing case/selector".into());
                }
                Ok(())
            }
            _ => Err("basis record source presence".into()),
        }
    }
    fn validate_modulus_record(&self, row: &ResultItem) -> Result<(), CaptureError> {
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.require()?;
        let record = self
            .basis_record
            .as_ref()
            .ok_or("missing successful basis record")?;
        let metadata = row.metadata.as_ref().ok_or("modulus record metadata")?;
        let basis = row.basis_ref.as_ref().ok_or("modulus record case basis")?;
        if !self.basis_expected
            || self.basis_record_calls != 1
            || row.value.to_bits() != 1.0f64.to_bits()
            || !row.source_result_refs.is_empty()
        {
            return Err("modulus record value/presence/references".into());
        }
        self.adapter.enter(AdapterEvent::LibraryBoundary, 1); // Existing fixed-id formatting; internals unqualified.
        self.adapter.require()?;
        let id = format!("result:modulus-basis:{}", stable_suffix(&self.case_id));
        let matches = self.adapter.same(&record.case, &self.case_id)
            && self.adapter.same(&row.kind, "modulus_basis_record")
            && self.adapter.same(&row.id, &id)
            && self.adapter.same(&row.unit, "record")
            && self.adapter.same(&row.entity_ref, &self.case_id)
            && self.adapter.same(&basis.ref_type, "load_case")
            && self.adapter.same(&basis.ref_id, &self.case_id)
            && self.adapter.same(&metadata.component, "material_modulus_basis")
            && self.adapter.same(&metadata.coordinate_system, "not_applicable")
            && self.adapter.same(&metadata.location, &self.case_id)
            && self.adapter.same(&metadata.sign_convention, "presence record; value 1.0 means the load case solved with the recorded user-entered property basis")
            && self.adapter.same(&metadata.basis, &record.text);
        self.adapter.require()?;
        if !matches {
            return Err("modulus record association".into());
        }
        Ok(())
    }
    fn observation_copy(&mut self, text: &str, slot: usize) -> Result<String, CaptureError> {
        std::alloc::Layout::array::<u8>(text.len())
            .map_err(|_| CaptureError::CountRange("observation layout"))?;
        let n =
            u64::try_from(text.len()).map_err(|_| CaptureError::CountRange("observation bytes"))?;
        self.capture_entry(AdapterEvent::AllocationRequest)?;
        self.adapter.enter(AdapterEvent::RequestedCopyBytes, n);
        self.adapter.require()?;
        self.capture_entry(AdapterEvent::MapWrite)?;
        self.capture_entry(AdapterEvent::LibraryBoundary)?;
        let mut value = String::new();
        #[cfg(test)]
        if self.observation_storage_failure == Some(slot) {
            return Err(CaptureError::Storage(
                "observation text (injected allocator refusal)",
            ));
        }
        value
            .try_reserve_exact(text.len())
            .map_err(|_| CaptureError::Storage("observation text"))?;
        self.observation_capacity_bytes[slot] = value.capacity();
        let bytes = u64::try_from(value.capacity())
            .map_err(|_| CaptureError::CountRange("observation capacity"))?;
        self.adapter.enter(AdapterEvent::RustCapacityBytes, bytes);
        self.adapter.require()?;
        self.capture_entry(AdapterEvent::LibraryBoundary)?;
        value.push_str(text);
        Ok(value)
    }
    fn observation_fields(
        &self,
        row: &ResultItem,
        case: &str,
        mode: PreviewSolverMode,
        parity: bool,
        final_row: bool,
        captured: Option<&ObservationValue>,
    ) -> Result<(), CaptureError> {
        self.capture_entry(AdapterEvent::ValidationEntry)?;
        let m = row.metadata.as_ref().ok_or("observation metadata")?;
        let (id, kind, unit, entity, component, location, sign) = if parity {
            ("result:sparse-live:dense-parity-relative-delta", "sparse_live_path_dense_parity_relative_delta",
             "unitless", "solver:sparse_direct", "sparse_live_path", "load_case",
             "unitless max absolute dense-sparse solution delta divided by max dense solution magnitude; no release threshold asserted")
        } else {
            ("result:solver-mode:linear-solve-basis", "linear_solver_mode_basis", "mode_code",
             "solver:linear_static_preview", "linear_solver_mode", case,
             "mode_code 1=sparse_interactive, 2=dense_scrutiny, 3=dense_fallback_after_sparse_failure")
        };
        let fixed = self.adapter.same(&row.id, id)
            && self.adapter.same(&row.kind, kind)
            && self.adapter.same(&row.unit, unit)
            && self.adapter.same(&row.entity_ref, entity)
            && self.adapter.same(&m.component, component)
            && self.adapter.same(&m.coordinate_system, "reduced_system")
            && self.adapter.same(&m.location, location);
        self.adapter.require()?;
        if !fixed || !row.source_result_refs.is_empty() {
            return Err("observation fixed fields".into());
        }
        let sign_matches = self.adapter.same(&m.sign_convention, sign);
        self.adapter.require()?;
        if !sign_matches {
            return Err(if parity {
                "observation parity sign"
            } else {
                "ordinary sparse mode sign"
            }
            .into());
        }
        if final_row {
            let basis = row.basis_ref.as_ref().ok_or("observation final basis")?;
            let same = self.adapter.same(&basis.ref_type, "load_case")
                && self.adapter.same(&basis.ref_id, case);
            self.adapter.require()?;
            if !same {
                return Err("observation final case".into());
            }
        } else if row.basis_ref.is_some() {
            return Err("observation producer basis".into());
        }
        if parity {
            if mode != PreviewSolverMode::DenseScrutiny || !row.value.is_finite() || row.value < 0.0
            {
                return Err("observation parity mode/value".into());
            }
        } else {
            let expected = match mode {
                PreviewSolverMode::SparseInteractive => 1.0f64,
                PreviewSolverMode::DenseScrutiny => 2.0f64,
            };
            if row.value.to_bits() != expected.to_bits() {
                return Err("observation mode value/fallback".into());
            }
        }
        if let Some(captured) = captured {
            let same = self.adapter.same(&m.basis, &captured.basis);
            self.adapter.require()?;
            if !same || row.value.to_bits() != captured.value_bits {
                return Err("observation captured value/text".into());
            }
        }
        Ok(())
    }
    pub(super) fn solver_observations(
        &mut self,
        case: &PreviewLoadCase,
        mode: PreviewSolverMode,
        produced_rows: &[ResultItem],
    ) {
        if self.error.is_some() {
            return;
        }
        if let Some(fault) = self.adapter.fault.get() {
            self.error = Some(CaptureError::Accounting(fault));
            return;
        }
        let result = (|| -> Result<(), CaptureError> {
            let calls = self
                .observation_calls
                .checked_add(1)
                .ok_or(CaptureError::CountRange("observation calls"))?;
            self.capture_entry(AdapterEvent::MapWrite)?;
            self.observation_calls = calls;
            self.capture_entry(AdapterEvent::ValidationEntry)?;
            if calls != 1 || self.observations.is_some() {
                return Err("duplicate observation completion".into());
            }
            let same_case = self.adapter.same(&case.id, &self.case_id);
            self.adapter.require()?;
            if self.invocation_calls != 1
                || self.invocation_mode != Some(mode)
                || self.case_calls != 1
                || !same_case
            {
                return Err("observation invocation/case/mode".into());
            }
            let mut mode_row = None;
            let mut parity_row = None;
            for row in produced_rows {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                let is_mode = self.adapter.same(&row.kind, "linear_solver_mode_basis");
                let is_parity = self
                    .adapter
                    .same(&row.kind, "sparse_live_path_dense_parity_relative_delta");
                self.adapter.require()?;
                if is_mode {
                    if mode_row.is_some() {
                        return Err("duplicate produced mode".into());
                    }
                    self.capture_entry(AdapterEvent::MapWrite)?;
                    mode_row = Some(row);
                }
                if is_parity {
                    if parity_row.is_some() {
                        return Err("duplicate produced parity".into());
                    }
                    self.capture_entry(AdapterEvent::MapWrite)?;
                    parity_row = Some(row);
                }
            }
            let mode_row = mode_row.ok_or("missing produced mode")?;
            self.observation_fields(mode_row, &case.id, mode, false, false, None)?;
            if let Some(row) = parity_row {
                self.observation_fields(row, &case.id, mode, true, false, None)?;
            }
            let parity_produced = parity_row.is_some();
            let captured_case = self.observation_copy(&case.id, 0)?;
            let captured_mode = ObservationValue {
                value_bits: mode_row.value.to_bits(),
                basis: self.observation_copy(&mode_row.metadata.as_ref().unwrap().basis, 1)?,
            };
            let parity = match parity_row {
                Some(row) => Some(ObservationValue {
                    value_bits: row.value.to_bits(),
                    basis: self.observation_copy(&row.metadata.as_ref().unwrap().basis, 2)?,
                }),
                None => None,
            };
            self.capture_entry(AdapterEvent::MapWrite)?;
            self.observations = Some(SolverObservations {
                case: captured_case,
                mode,
                mode_row: captured_mode,
                parity_produced,
                parity,
            });
            Ok(())
        })();
        if let Err(error) = result {
            self.error = Some(error);
        }
    }
    pub(super) fn bind_observations(
        &self,
        envelope: &MechanicsEnvelope,
    ) -> Result<(), CaptureError> {
        self.adapter.require()?;
        if self.error.is_some() {
            return Err("prior observation capture refusal".into());
        }
        self.capture_entry(AdapterEvent::ValidationEntry)?;
        let captured = self
            .observations
            .as_ref()
            .ok_or("missing observation completion")?;
        let same = self.adapter.same(&captured.case, &self.case_id);
        self.adapter.require()?;
        if self.invocation_calls != 1
            || self.case_calls != 1
            || self.observation_calls != 1
            || self.invocation_mode != Some(captured.mode)
            || !same
            || captured.parity_produced != captured.parity.is_some()
        {
            return Err("observation completion/presence custody".into());
        }
        let mut mode_count = 0usize;
        let mut parity_count = 0usize;
        for row in &envelope.results {
            self.capture_entry(AdapterEvent::RowVisit)?;
            let is_mode = self.adapter.same(&row.kind, "linear_solver_mode_basis");
            let is_parity = self
                .adapter
                .same(&row.kind, "sparse_live_path_dense_parity_relative_delta");
            self.adapter.require()?;
            if is_mode {
                mode_count = mode_count
                    .checked_add(1)
                    .ok_or(CaptureError::CountRange("final modes"))?;
                self.observation_fields(
                    row,
                    &captured.case,
                    captured.mode,
                    false,
                    true,
                    Some(&captured.mode_row),
                )?;
            }
            if is_parity {
                parity_count = parity_count
                    .checked_add(1)
                    .ok_or(CaptureError::CountRange("final parity"))?;
                let snapshot = captured.parity.as_ref().ok_or("unexpected final parity")?;
                self.observation_fields(
                    row,
                    &captured.case,
                    captured.mode,
                    true,
                    true,
                    Some(snapshot),
                )?;
            }
        }
        if mode_count != 1 || parity_count != usize::from(captured.parity_produced) {
            return Err("observation final presence".into());
        }
        Ok(())
    }
    fn capture_entry(&self, event: AdapterEvent) -> Result<(), CaptureError> {
        self.adapter.enter(event, 1);
        self.adapter.require()
    }
    pub(super) fn support_reserve<T>(
        &mut self,
        n: usize,
        slot: usize,
    ) -> Result<Vec<T>, CaptureError> {
        std::alloc::Layout::array::<T>(n)
            .map_err(|_| CaptureError::CountRange("support layout"))?;
        self.capture_entry(AdapterEvent::AllocationRequest)?;
        self.capture_entry(AdapterEvent::MapWrite)?; // capacity record entry before allocation
        let mut v = Vec::new();
        self.capture_entry(AdapterEvent::LibraryBoundary)?;
        v.try_reserve_exact(n)
            .map_err(|_| CaptureError::Storage("support vector"))?;
        let bytes = v
            .capacity()
            .checked_mul(std::mem::size_of::<T>())
            .ok_or(CaptureError::CountRange("support capacity bytes"))?;
        self.support_capacity_bytes[slot] = self.support_capacity_bytes[slot]
            .checked_add(bytes)
            .ok_or(CaptureError::CountRange("support capacity total"))?;
        let bytes = u64::try_from(bytes)
            .map_err(|_| CaptureError::CountRange("support capacity conversion"))?;
        self.adapter.enter(AdapterEvent::RustCapacityBytes, bytes);
        self.adapter.require()?;
        Ok(v)
    }
    pub(super) fn capture_supports(
        &mut self,
        model: &PreviewModel,
        built: &BuiltModel,
        restrained: &[usize],
        springs: &[SpringEntry],
        parts: &mut k::SourceParts,
    ) -> Result<(), CaptureError> {
        self.adapter.require()?;
        let n = model
            .nodes
            .len()
            .checked_mul(6)
            .ok_or(CaptureError::CountRange("support dofs"))?;
        for count in [
            springs.len(),
            model.supports.len(),
            built.supports.len(),
            restrained.len(),
        ] {
            self.capture_entry(AdapterEvent::ValidationEntry)?;
            u32::try_from(count).map_err(|_| CaptureError::CountRange("support count"))?;
        }
        model
            .supports
            .len()
            .checked_mul(6)
            .ok_or(CaptureError::CountRange("support slots"))?;
        let q = model
            .nodes
            .len()
            .checked_mul(7)
            .and_then(|v| {
                model
                    .pipe_segments
                    .len()
                    .checked_mul(30)
                    .and_then(|m| v.checked_add(m))
            })
            .and_then(|v| v.checked_add(springs.len()))
            .and_then(|v| v.checked_add(restrained.len()))
            .and_then(|v| {
                model
                    .supports
                    .len()
                    .checked_mul(2)
                    .and_then(|g| v.checked_add(g))
            })
            .ok_or(CaptureError::CountRange("support layout quantities"))?;
        u32::try_from(q).map_err(|_| CaptureError::CountRange("support layout quantities"))?;
        let mut built_used = self.support_reserve(built.supports.len(), 0)?;
        built_used.resize(built.supports.len(), false);
        let mut spring_used = self.support_reserve(springs.len(), 1)?;
        spring_used.resize(springs.len(), false);
        let mut rigid_owned = self.support_reserve(n, 2)?;
        rigid_owned.resize(n, false);
        self.spring_map = self.support_reserve(springs.len(), 3)?;
        parts.springs = self.support_reserve(springs.len(), 4)?;
        self.support_fixed = self.support_reserve(model.supports.len(), 6)?;
        for (i, authored) in model.supports.iter().enumerate() {
            self.capture_entry(AdapterEvent::SourceVisit)?;
            let mut node = None;
            for (j, p) in model.nodes.iter().enumerate() {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                let equal = self.adapter.same(&p.id, &authored.node);
                self.adapter.require()?;
                if equal {
                    node = Some(j);
                    break;
                }
            }
            let node = node.ok_or("support node")?;
            let mut matched = None;
            for (j, b) in built.supports.iter().enumerate() {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                let equal = self.adapter.same(&b.support_id, &authored.id);
                self.adapter.require()?;
                if equal {
                    if matched.is_some() || built_used[j] {
                        return Err("duplicate built support".into());
                    }
                    matched = Some(j);
                }
            }
            let bi = matched.ok_or("missing built support")?;
            let b = &built.supports[bi];
            self.capture_entry(AdapterEvent::ValidationEntry)?;
            if b.node_index != node || b.imposed_displacement.is_some() {
                return Err("support build node/motion".into());
            }
            let is_spring = authored.family.as_deref() == Some("spring");
            let family = match authored.family.as_deref() {
                Some("spring") => SupportFamily::Spring,
                Some("anchor") => SupportFamily::Anchor,
                Some("guide") => SupportFamily::Guide,
                Some("line_stop") => SupportFamily::LineStop,
                Some("vertical_support") => SupportFamily::VerticalSupport,
                None if authored.restraints.len() == 6 => SupportFamily::Anchor,
                None => SupportFamily::Guide,
                _ => return Err("unsupported support family".into()),
            };
            if b.family != family || b.restrained_dofs.len() != authored.restraints.len() {
                return Err("support build family/axes".into());
            }
            let mut fixed = [false; 6];
            for (a, d) in authored.restraints.iter().zip(&b.restrained_dofs) {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                self.capture_entry(AdapterEvent::LibraryBoundary)?;
                if parse_dof(a).map_err(CaptureError::from)? != *d {
                    return Err("support axis".into());
                }
                if !is_spring {
                    let axis = dof_index(*d);
                    let global = node
                        .checked_mul(6)
                        .and_then(|v| v.checked_add(axis))
                        .ok_or(CaptureError::CountRange("support global dof"))?;
                    if fixed[axis] || rigid_owned[global] {
                        return Err("ambiguous rigid ownership".into());
                    }
                    let mut hits = 0;
                    for &g in restrained {
                        self.capture_entry(AdapterEvent::SourceVisit)?;
                        self.capture_entry(AdapterEvent::ValidationEntry)?;
                        if g == global {
                            hits += 1;
                        }
                    }
                    if hits != 1 {
                        return Err("rigid boundary identity".into());
                    }
                    self.capture_entry(AdapterEvent::MapWrite)?;
                    fixed[axis] = true;
                    rigid_owned[global] = true;
                }
            }
            let mut children = self.support_reserve(usize::from(is_spring), 5)?;
            let mut found_spring = false;
            for (j, spring) in springs.iter().enumerate() {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                let equal = self.adapter.same(&spring.support_id, &authored.id);
                self.adapter.require()?;
                if !equal {
                    continue;
                }
                self.capture_entry(AdapterEvent::ValidationEntry)?;
                if !is_spring || found_spring || spring_used[j] {
                    return Err("duplicate/extra support spring".into());
                }
                let input = authored
                    .stiffness
                    .as_ref()
                    .ok_or("authored spring stiffness")?;
                let stiffness = b.stiffness.as_ref().ok_or("built spring stiffness")?;
                self.capture_entry(AdapterEvent::LibraryBoundary)?;
                let dof = parse_dof(&input.dof).map_err(CaptureError::from)?;
                let dimension = if dof.is_translational() {
                    QuantityDimension::TranslationalStiffness
                } else {
                    QuantityDimension::RotationalStiffness
                };
                if b.restrained_dofs.as_slice() != [dof]
                    || spring.node_dof.node_index != node
                    || spring.node_dof.dof != dof
                    || stiffness.dimension != dimension
                    || spring.stiffness.dimension != dimension
                    || !input.value.value.is_finite()
                    || input.value.value.to_bits() != stiffness.value.to_bits()
                    || input.value.value.to_bits() != spring.stiffness.value.to_bits()
                {
                    return Err("spring source identity".into());
                }
                let global = spring.node_dof.global_index();
                self.capture_entry(AdapterEvent::MapWrite)?;
                spring_used[j] = true;
                found_spring = true;
                self.capture_entry(AdapterEvent::MapWrite)?;
                children.push(j as u32);
                self.capture_entry(AdapterEvent::MapWrite)?;
                parts.springs.push(k::Spring {
                    id: j as u32,
                    dof: k::Dof::from_global(global),
                    stiffness: spring.stiffness.value,
                });
                self.capture_entry(AdapterEvent::MapWrite)?;
                self.spring_map.push(SpringIdentity {
                    boundary: j,
                    support: i,
                    dof: global,
                    bits: spring.stiffness.value.to_bits(),
                });
            }
            if is_spring != found_spring || (!is_spring && b.stiffness.is_some()) {
                return Err("missing/foreign support stiffness".into());
            }
            let id = self.adapter.copy(&authored.id)?;
            self.capture_entry(AdapterEvent::MapWrite)?;
            built_used[bi] = true;
            self.capture_entry(AdapterEvent::MapWrite)?;
            self.supports.push((id, node));
            self.capture_entry(AdapterEvent::MapWrite)?;
            self.support_fixed.push(fixed);
            self.capture_entry(AdapterEvent::MapWrite)?;
            parts.supports.push(k::SupportGroup {
                id: i as u32,
                node: node as u32,
                restrained: fixed,
                springs: children,
                directional_springs: Vec::new(),
            });
        }
        for used in built_used.into_iter().chain(spring_used) {
            self.capture_entry(AdapterEvent::ValidationEntry)?;
            if !used {
                return Err("unconsumed built/boundary support".into());
            }
        }
        for &g in restrained {
            self.capture_entry(AdapterEvent::SourceVisit)?;
            if !rigid_owned.get(g).copied().unwrap_or(false) {
                return Err("unowned rigid boundary".into());
            }
        }
        Ok(())
    }
    fn check_support_source(&self, source: &k::PrimitiveSource) -> Result<(), CaptureError> {
        self.check_support_maps(source.supports(), source.springs(), true)
    }
    pub(super) fn check_support_maps(
        &self,
        groups: &[k::SupportGroup],
        springs: &[k::Spring],
        canonical: bool,
    ) -> Result<(), CaptureError> {
        self.adapter.require()?;
        if groups.len() != self.supports.len()
            || springs.len() != self.spring_map.len()
            || self.support_fixed.len() != self.supports.len()
        {
            return Err("canonical support counts".into());
        }
        for (i, group) in groups.iter().enumerate() {
            self.capture_entry(AdapterEvent::SourceVisit)?;
            if group.id != i as u32
                || group.node as usize != self.supports[i].1
                || group.restrained != self.support_fixed[i]
                || !group.directional_springs.is_empty()
            {
                return Err("canonical support identity".into());
            }
            let mut count = 0;
            for map in &self.spring_map {
                self.capture_entry(AdapterEvent::SourceVisit)?;
                if map.support != i {
                    continue;
                }
                count += 1;
                if group.springs.as_slice() != [map.boundary as u32] {
                    return Err("canonical support membership".into());
                }
                let mut found = None;
                for (index, spring) in springs.iter().enumerate() {
                    self.capture_entry(AdapterEvent::SourceVisit)?;
                    self.capture_entry(AdapterEvent::ValidationEntry)?;
                    if spring.id != map.boundary as u32 {
                        continue;
                    }
                    if found.is_some() || (canonical && index != map.boundary) {
                        return Err("canonical spring occurrence".into());
                    }
                    found = Some(spring);
                }
                let spring = found.ok_or("canonical spring")?;
                if spring.dof.global() != map.dof || spring.stiffness.to_bits() != map.bits {
                    return Err("canonical spring identity".into());
                }
            }
            if count != group.springs.len() {
                return Err("canonical support coverage".into());
            }
        }
        Ok(())
    }
    pub fn case_source(
        &mut self,
        model: &PreviewModel,
        built: &BuiltModel,
        materials: &[MaterialInput],
        case: &PreviewLoadCase,
        restrained: &[usize],
        springs: &[SpringEntry],
        application: &LoadApplication,
        thermal: &[ThermalElementLoad],
        pressure: &[PressureThrustLoad],
    ) {
        self.case_calls = self.case_calls.checked_add(1).expect("bounded cases");
        if self.error.is_some() {
            return;
        }
        if self.case_calls != 1 || model.load_cases.len() != 1 {
            self.fail("private witness has exactly one actual case");
            return;
        }
        if let Err(e) = self.basis_source_case(case) {
            self.error = Some(e);
            return;
        }
        if !built.nonlinear_supports.is_empty()
            || !built.user_stiffness_elements.is_empty()
            || !built.curved_bend_elements.is_empty()
            || !thermal.is_empty()
            || !pressure.is_empty()
            || !application.element_uniform_loads.is_empty()
            || !application.imposed_displacements.is_empty()
            || case.equivalent_static.is_some()
            || case
                .pressure_regions
                .as_ref()
                .is_some_and(|v| !v.is_empty())
            || model.supports.iter().any(|s| s.hanger.is_some())
        {
            self.fail("unsupported producer present");
            return;
        }
        if !self.adapter.enter(AdapterEvent::LibraryBoundary, 1) {
            self.fail("case capture accounting");
            return;
        }
        let mut parts = k::SourceParts::default();
        let allocated = (|| -> Result<(), CaptureError> {
            self.case_id = self.adapter.copy(&case.id)?;
            parts.nodes = self.adapter.reserve(built.nodes.len())?;
            parts.members = self.adapter.reserve(model.pipe_segments.len())?;
            parts.stations = self.adapter.reserve(
                model
                    .pipe_segments
                    .len()
                    .checked_mul(3)
                    .ok_or(CaptureError::CountRange("stations"))?,
            )?;
            parts.constraints = self.adapter.reserve(restrained.len())?;
            parts.supports = self.adapter.reserve(model.supports.len())?;
            parts.loads = self.adapter.reserve(application.nodal_loads.len())?;
            self.facts = self.adapter.reserve(model.pipe_segments.len())?;
            self.members = self.adapter.reserve(model.pipe_segments.len())?;
            self.operational = self.adapter.reserve(model.pipe_segments.len())?;
            self.supports = self.adapter.reserve(model.supports.len())?;
            self.terms = self.adapter.reserve(application.nodal_loads.len())?;
            Ok(())
        })();
        if let Err(e) = allocated {
            self.error = Some(e);
            return;
        }
        for n in &built.nodes {
            if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                || !self.adapter.enter(AdapterEvent::MapWrite, 1)
            {
                self.fail("built-node accounting");
                return;
            }
            parts.nodes.push(n.coordinates);
        }
        if parts.nodes.len() != self.nodes.len()
            || parts
                .nodes
                .iter()
                .zip(&self.nodes)
                .any(|(a, b)| a.map(f64::to_bits) != b.1.map(f64::to_bits))
        {
            self.fail("normalized node/built identity");
            return;
        }
        for (i, pipe) in model.pipe_segments.iter().enumerate() {
            if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
            {
                self.fail("member accounting");
                return;
            }
            let Some(bi) = built
                .pipes
                .iter()
                .position(|p| self.adapter.same(&p.element_id, &pipe.id))
            else {
                self.fail("missing built member");
                return;
            };
            let b = &built.pipes[bi];
            let Some(section) = built.sections.get(&pipe.id) else {
                self.fail("missing section");
                return;
            };
            let Some(mi) = self
                .materials
                .iter()
                .position(|m| self.adapter.same(&m.0, &pipe.material))
            else {
                self.fail("normalized material");
                return;
            };
            let Some(m) = materials
                .iter()
                .find(|m| self.adapter.same(&m.id, &pipe.material))
            else {
                self.fail("resolved material");
                return;
            };
            let id = match u32::try_from(i) {
                Ok(i) => i,
                Err(_) => {
                    self.fail_count("member count range");
                    return;
                }
            };
            let material =
                if case.modulus_basis_ref.is_none() && case.modulus_basis_temperature.is_none() {
                    k::ProductMaterial::Base {
                        e: self.materials[mi].1,
                        g: self.materials[mi].2,
                    }
                } else {
                    let Some(s) = self.selections.iter().find(|s| {
                        self.adapter.same(&s.case, &case.id)
                            && self.adapter.same(&s.material, &pipe.material)
                    }) else {
                        self.fail("selection missing");
                        return;
                    };
                    s.selected
                };
            if m.elastic_modulus.value.to_bits() != b.section.elastic_modulus.to_bits()
                || m.shear_modulus.as_ref().unwrap().value.to_bits()
                    != b.section.shear_modulus.to_bits()
                || section.area.to_bits() != b.section.area.to_bits()
                || section.torsion_constant.to_bits() != b.section.torsion_constant.to_bits()
            {
                self.fail("resolved/built K mismatch");
                return;
            }
            let (Ok(ni), Ok(nj)) = (u32::try_from(b.node_i.index), u32::try_from(b.node_j.index))
            else {
                self.fail_count("node count range");
                return;
            };
            if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                self.fail("map-write accounting");
                return;
            }
            parts.members.push(k::StraightMember {
                id,
                node_i: ni,
                node_j: nj,
                elastic_modulus: b.section.elastic_modulus,
                shear_modulus: b.section.shear_modulus,
                area: b.section.area,
                second_moment_y: b.section.second_moment_y,
                second_moment_z: b.section.second_moment_z,
                torsion_constant: b.section.torsion_constant,
                y_reference: b.y_reference,
            });
            if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                self.fail("map-write accounting");
                return;
            }
            self.operational.push(evaluate_operational(
                [b.node_i.coordinates, b.node_j.coordinates],
                [
                    b.section.elastic_modulus,
                    b.section.shear_modulus,
                    b.section.area,
                    b.section.torsion_constant,
                ],
            ));
            if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                self.fail("map-write accounting");
                return;
            }
            self.facts.push(k::ProductMemberFacts {
                member: id,
                diameter: pipe.section.outside_diameter.value,
                effective_wall: section.wall_thickness,
                material,
                area: section.area,
                second_moment: section.second_moment,
                torsion_constant: section.torsion_constant,
                section_modulus: section.section_modulus,
                radius: section.torsion_radius,
            });
            self.adapter.enter(AdapterEvent::LibraryBoundary, 1);
            if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                self.fail("map-write accounting");
                return;
            }
            self.members.push(MemberIdentity {
                model: i,
                built: bi,
                id: pipe.id.clone(),
                material: mi,
                nodes: [b.node_i.index, b.node_j.index],
            });
            for (j, fraction) in [0.25, 0.5, 0.75].into_iter().enumerate() {
                let Some(station) = id.checked_mul(3).and_then(|v| v.checked_add(j as u32)) else {
                    self.fail_count("station count");
                    return;
                };
                if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                    || !self.adapter.enter(AdapterEvent::MapWrite, 1)
                {
                    self.fail("station-write accounting");
                    return;
                }
                parts.stations.push(k::Station {
                    id: station,
                    member: id,
                    fraction,
                });
            }
        }
        if built.pipes.len() != self.members.len() {
            self.fail("extra built member");
            return;
        }
        for &g in restrained {
            if !self.adapter.enter(AdapterEvent::SourceVisit, 1) {
                self.fail("constraint accounting");
                return;
            }
            if g >= parts.nodes.len() * 6 {
                self.fail("constraint index");
                return;
            }
            if !self.adapter.enter(AdapterEvent::MapWrite, 1) {
                self.fail("constraint-write accounting");
                return;
            }
            parts.constraints.push(k::Constraint {
                dof: k::Dof::from_global(g),
                value: 0.0,
            });
        }
        if let Err(e) = self.capture_supports(model, built, restrained, springs, &mut parts) {
            self.error = Some(e);
            return;
        }
        if let Err(e) = self.check_support_maps(&parts.supports, &parts.springs, false) {
            self.error = Some(e);
            return;
        }
        let mut used = match self.adapter.reserve(case.primitive_loads.len()) {
            Ok(v) => v,
            Err(e) => {
                self.error = Some(e);
                return;
            }
        };
        used.resize(case.primitive_loads.len(), false);
        for (occurrence, l) in application.nodal_loads.iter().enumerate() {
            if !self.adapter.enter(AdapterEvent::SourceVisit, 1)
                || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
            {
                self.fail("term accounting");
                return;
            }
            let candidate=case.primitive_loads.iter().enumerate().position(|(i,p)| !used[i]&&self.adapter.same(&p.id,&l.load_id)
                && p.magnitude.value.to_bits()==l.value.to_bits()
                && matches!(&p.target,LoadTargetInput::Node{node} if node==&model.nodes[l.node_index].id)
                && parse_direction(&p.direction).is_ok_and(|d|d.dof_index()==l.global_dof%6));
            let Some(original) = candidate else {
                self.fail("individual load occurrence not authored");
                return;
            };
            if !self.adapter.enter(AdapterEvent::LibraryBoundary, 2)
                || !self.adapter.enter(AdapterEvent::MapWrite, 3)
            {
                self.fail("term-write accounting");
                return;
            }
            used[original] = true;
            self.terms.push(TermIdentity {
                original,
                occurrence,
                canonical: usize::MAX,
                id: l.load_id.clone(),
                dof: l.global_dof,
                bits: l.value.to_bits(),
            });
            parts.loads.push(k::NodalLoad {
                dof: k::Dof::from_global(l.global_dof),
                value: l.value,
                source_id: l.load_id.clone(),
            });
        }
        if used.iter().any(|u| !*u) {
            self.fail("unconsumed authored primitive");
            return;
        }
        if !self.adapter.enter(AdapterEvent::LibraryBoundary, 1)
            || self.adapter.fault.get().is_some()
        {
            self.fail("source construction accounting");
            return;
        }
        match k::PrimitiveSource::new(parts) {
            Ok(source) => {
                // Reconcile each canonical load occurrence to the producing record, not a rounded net.
                let mut used = match self.adapter.reserve(self.terms.len()) {
                    Ok(v) => v,
                    Err(e) => {
                        self.error = Some(e);
                        return;
                    }
                };
                used.resize(self.terms.len(), false);
                for (canonical, l) in source.loads().iter().enumerate() {
                    if !self.adapter.enter(AdapterEvent::SourceVisit, 1) {
                        self.fail("canonical accounting");
                        return;
                    }
                    let Some(i) = self.terms.iter().enumerate().position(|(i, t)| {
                        !used[i]
                            && self.adapter.same(&t.id, &l.source_id)
                            && t.dof == l.dof.global()
                            && t.bits == l.value.to_bits()
                    }) else {
                        self.fail("canonical term map");
                        return;
                    };
                    if !self.adapter.enter(AdapterEvent::MapWrite, 2) {
                        self.fail("canonical-write accounting");
                        return;
                    }
                    used[i] = true;
                    self.terms[i].canonical = canonical;
                }
                if let Err(e) = self.check_support_source(&source) {
                    self.error = Some(e);
                    return;
                }
                self.source = Some(source);
            }
            Err(e) => self.error = Some(CaptureError::Source(e)),
        }
        self.capacities = vec![
            ("nodes", self.nodes.capacity()),
            ("materials", self.materials.capacity()),
            ("selections", self.selections.capacity()),
            ("members", self.members.capacity()),
            ("terms", self.terms.capacity()),
            ("facts", self.facts.capacity()),
            ("supports", self.supports.capacity()),
            ("spring_map", self.spring_map.capacity()),
            ("support_fixed", self.support_fixed.capacity()),
        ];
    }
    pub fn finish(&mut self, envelope: &MechanicsEnvelope) {
        self.final_calls = self
            .final_calls
            .checked_add(1)
            .expect("bounded final hooks");
        if self.error.is_some() {
            return;
        }
        if self.adapter.fault.get().is_some() {
            self.fail("adapter accounting");
            return;
        }
        if self.final_calls != 1 {
            self.fail("final hook repeated");
            return;
        }
        if envelope.producer.semantic_contract_id != preview_physics::ID
            || envelope.source_block_recovery.is_some()
            || envelope.status.mechanics != "MECHANICS_SOLVED"
        {
            self.fail("not final ordinary preview");
            return;
        }
        let Some(source) = self.source.as_ref() else {
            self.fail("missing actual source");
            return;
        };
        let cap = match k::OriginCapacity::for_calls(&[1], &[]) {
            Ok(v) => v,
            Err(e) => {
                self.error = Some(CaptureError::Origin(e));
                return;
            }
        };
        let mut invocation = match k::RecordedInvocation::new(60_000_000_000, cap) {
            Ok(v) => v,
            Err(e) => {
                self.error = Some(CaptureError::Origin(e));
                return;
            }
        };
        self.adapter.enter(AdapterEvent::LibraryBoundary, 1);
        let mut cases = match invocation.solve_cases(
            std::slice::from_ref(source),
            k::CaseLimit::new(20_000_000_000),
        ) {
            Ok(v) => v,
            Err(e) => {
                self.error = Some(CaptureError::Origin(e));
                return;
            }
        };
        let case = cases.remove(0);
        let k::ExecutionOutcome::Selected(owner) = &case.outcome else {
            self.error = Some(CaptureError::NativeUnavailable);
            self.native = Some((invocation, case));
            return;
        };
        match self.bind_rows(envelope, owner) {
            Ok(rows) => {
                let spent = invocation.certify_product_case(case.run, owner, &self.facts, &rows);
                self.numeric_pass = spent.passed();
                self.verdicts = spent.verdicts().to_vec();
                self.summary_coverage = spent.summary_coverage().to_vec();
                self.source_correction_calls = spent.source_correction_calls();
                self.numeric_failure = spent.failure().cloned();
                self.work = format!(
                    "{:?}; native={:?}",
                    spent.work_summary(),
                    spent.native_work()
                );
                self.observable_error = self.observables(envelope).err();
                self.g5a_error = self.g5a(owner, &rows).err();
            }
            Err(e) => {
                self.error = Some(
                    self.adapter
                        .fault
                        .get()
                        .map(CaptureError::Accounting)
                        .unwrap_or(e),
                );
            }
        }
        self.native = Some((invocation, case));
    }
    pub(super) fn bind_rows<'a>(
        &self,
        e: &'a MechanicsEnvelope,
        owner: &k::RetainedSolve,
    ) -> Result<Vec<k::ProductFinalRow<'a>>, CaptureError> {
        self.adapter.require()?;
        if self.error.is_some() {
            return Err("prior capture refusal".into());
        }
        self.bind_observations(e)?;
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.require()?;
        if self.basis_expected != self.basis_record.is_some()
            || self.basis_record_calls != usize::from(self.basis_expected)
        {
            return Err("basis record capture presence".into());
        }
        let mut modulus_basis = false;
        let mut out = self.adapter.reserve(e.results.len())?;
        for r in &e.results {
            if !self.adapter.enter(AdapterEvent::RowVisit, 1)
                || !self.adapter.enter(AdapterEvent::ValidationEntry, 1)
            {
                self.adapter.require()?;
            }
            let basis = r.basis_ref.as_ref().ok_or("final basis")?;
            let same_case =
                basis.ref_type == "load_case" && self.adapter.same(&basis.ref_id, &self.case_id);
            self.adapter.require()?;
            if !same_case {
                return Err("case binding".into());
            }
            let node = self
                .nodes
                .iter()
                .position(|n| self.adapter.same(&n.0, &r.entity_ref));
            let member = self
                .members
                .iter()
                .position(|m| self.adapter.same(&m.id, &r.entity_ref));
            let support = self
                .supports
                .iter()
                .position(|s| self.adapter.same(&s.0, &r.entity_ref));
            self.adapter.require()?;
            let loc = r.metadata.as_ref().map(|m| m.location.as_str());
            let (recipe, body, unit) = if r.kind == "linear_solver_mode_basis" {
                if r.unit != "mode_code" {
                    return Err("mode unit".into());
                }
                (k::ProductRecipe::NonQuantity, 0, k::ProductUnit::Record)
            } else if r.kind == "sparse_live_path_dense_parity_relative_delta" {
                (k::ProductRecipe::DenseParityObservation, 0, k::ProductUnit::Record)
            } else if r.kind == "modulus_basis_record" {
                if modulus_basis || !self.basis_expected {
                    return Err("modulus record coverage".into());
                }
                self.validate_modulus_record(r)?;
                modulus_basis = true;
                (
                    k::ProductRecipe::ModulusBasisRecord,
                    0,
                    k::ProductUnit::Record,
                )
            } else if r.kind == "displacement_magnitude" {
                let n = node.ok_or("node")?;
                if r.unit != "mm" {
                    return Err("magnitude unit".into());
                }
                (
                    k::ProductRecipe::Native(k::QuantityId::DisplacementMagnitude(n as u32)),
                    owner.source().body_of_node(n as u32),
                    k::ProductUnit::Millimetre,
                )
            } else if let Some(c) = [
                "global_nodal_displacement_x",
                "global_nodal_displacement_y",
                "global_nodal_displacement_z",
                "global_nodal_rotation_x",
                "global_nodal_rotation_y",
                "global_nodal_rotation_z",
            ]
            .iter()
            .position(|s| *s == r.kind)
            {
                let n = node.ok_or("node")?;
                let unit = if c < 3 {
                    k::ProductUnit::Millimetre
                } else {
                    k::ProductUnit::Radian
                };
                if r.unit != if c < 3 { "mm" } else { "rad" } {
                    return Err("node unit".into());
                }
                (
                    k::ProductRecipe::Native(k::QuantityId::Displacement(k::Dof {
                        node: n as u32,
                        component: k::Component::ALL[c],
                    })),
                    owner.source().body_of_node(n as u32),
                    unit,
                )
            } else if r.kind.starts_with("support_reaction_") {
                let s = support.ok_or("support")?;
                let m = r.metadata.as_ref().ok_or("support metadata")?;
                let (recipe, unit) = if r.kind == "support_reaction_force_magnitude_v2" {
                    (k::ProductRecipe::Native(k::QuantityId::SupportForceMagnitude(s as u32)), k::ProductUnit::Newton)
                } else if r.kind == "support_reaction_moment_magnitude_v2" {
                    (k::ProductRecipe::Native(k::QuantityId::SupportMomentMagnitude(s as u32)), k::ProductUnit::NewtonMetre)
                } else if r.kind == "support_reaction_component_v2" {
                    let c = ["Fx", "Fy", "Fz", "Mx", "My", "Mz"].iter()
                        .position(|v| *v == m.component).ok_or("support component")?;
                    (k::ProductRecipe::SupportComponent { support: s as u32, component: k::Component::ALL[c] },
                        if c < 3 { k::ProductUnit::Newton } else { k::ProductUnit::NewtonMetre })
                } else { return Err("unsupported support row".into()); };
                if r.unit
                    != if unit == k::ProductUnit::Newton {
                        "N"
                    } else {
                        "N*m"
                    }
                {
                    return Err("support unit".into());
                }
                (
                    recipe,
                    owner.source().body_of_node(self.supports[s].1 as u32),
                    unit,
                )
            } else {
                let m = member.ok_or("row member")?;
                let id = self.members[m].model as u32;
                let body = owner.source().body_of_node(self.members[m].nodes[0] as u32);
                if r.kind == "pipe_elastic_normal_stress_maximum_v2" {
                    if r.unit != "Pa" {
                        return Err("maximum unit".into());
                    }
                    (
                        k::ProductRecipe::CircularMaximum { member: id },
                        body,
                        k::ProductUnit::Pascal,
                    )
                } else {
                    let site = match loc {
                        Some("end_i") => k::ProductSite::End(k::End::I),
                        Some("end_j") => k::ProductSite::End(k::End::J),
                        Some("quarter_1") => k::ProductSite::Station(id * 3),
                        Some("midspan") => k::ProductSite::Station(id * 3 + 1),
                        Some("quarter_3") => k::ProductSite::Station(id * 3 + 2),
                        _ => return Err("row site".into()),
                    };
                    if let Some(c) = [
                        "element_local_axial_force",
                        "element_local_shear_force_y",
                        "element_local_shear_force_z",
                        "element_local_torsional_moment",
                        "element_local_bending_moment_y",
                        "element_local_bending_moment_z",
                    ]
                    .iter()
                    .position(|s| *s == r.kind)
                    {
                        let q = match site {
                            k::ProductSite::End(end) => k::QuantityId::EndAction {
                                member: id,
                                end,
                                component: k::Component::ALL[c],
                            },
                            k::ProductSite::Station(station) => k::QuantityId::StationAction {
                                station,
                                component: k::Component::ALL[c],
                            },
                        };
                        if r.unit != if c < 3 { "N" } else { "N*m" } {
                            return Err("action unit".into());
                        }
                        (
                            k::ProductRecipe::Native(q),
                            body,
                            if c < 3 {
                                k::ProductUnit::Newton
                            } else {
                                k::ProductUnit::NewtonMetre
                            },
                        )
                    } else {
                        let stress = match r.kind.as_str() {
                            "element_local_axial_normal_stress" => k::ProductStress::Axial,
                            "element_local_bending_normal_stress_y" => k::ProductStress::BendingY,
                            "element_local_bending_normal_stress_z" => k::ProductStress::BendingZ,
                            "element_local_torsional_shear_stress" => k::ProductStress::Torsion,
                            _ => {
                                return Err(CaptureError::Association(format!(
                                    "uncovered actual row {}",
                                    r.kind
                                )))
                            }
                        };
                        if r.unit != "MPa" {
                            return Err("stress unit".into());
                        }
                        (
                            k::ProductRecipe::Stress {
                                member: id,
                                site,
                                stress,
                            },
                            body,
                            k::ProductUnit::Megapascal,
                        )
                    }
                }
            };
            if recipe != k::ProductRecipe::ModulusBasisRecord {
                validate_final_metadata(r, recipe, &self.case_id, &self.adapter)?;
            }
            self.adapter.enter(AdapterEvent::MapWrite, 1);
            self.adapter.require()?;
            out.push(k::ProductFinalRow {
                id: &r.id,
                case_id: &basis.ref_id,
                value: &r.value,
                unit,
                body,
                recipe,
            });
        }
        self.adapter.require()?;
        if modulus_basis != self.basis_expected {
            return Err("missing final modulus record".into());
        }
        Ok(out)
    }
    pub(super) fn observables(&self, e: &MechanicsEnvelope) -> Result<(), CaptureError> {
        self.adapter.require()?;
        self.adapter.enter(AdapterEvent::LibraryBoundary, 1); // Closed evidence inspection; serde/number internals remain unqualified.
        let evidence = e.contract_evidence.as_ref().ok_or("preview evidence")?;
        // Existing preview-physics reader's closed namespace; this private scope has no combinations.
        self.adapter.closed_keys(
            evidence,
            &["preview_cases", "combination_gates"],
            "evidence shape",
        )?;
        self.adapter.enter(AdapterEvent::ValidationEntry, 1);
        self.adapter.require()?;
        let gates = evidence["combination_gates"]
            .as_array()
            .ok_or("combination gates")?;
        if !gates.is_empty() {
            return Err("excluded combination gates".into());
        }
        let cases = evidence["preview_cases"]
            .as_array()
            .ok_or("preview cases")?;
        if cases.len() != 1 {
            return Err("evidence case".into());
        }
        let c = &cases[0];
        self.adapter.closed_keys(
            c,
            &[
                "load_case_id",
                "pipe_stress_extrema",
                "stress_maximum_coverage",
                "support_attribution",
                "intensified_measures",
            ],
            "case shape",
        )?;
        let case_id = c["load_case_id"].as_str().ok_or("evidence case")?;
        let case_matches = self.adapter.same(case_id, &self.case_id);
        self.adapter.require()?;
        if !case_matches {
            return Err("evidence case".into());
        }
        self.adapter.closed_keys(
            &c["stress_maximum_coverage"],
            &[
                "complete",
                "unavailable_pipe_ids",
                "outside_domain_pipe_ids",
            ],
            "stress coverage shape",
        )?;
        self.adapter.closed_keys(
            &c["support_attribution"],
            &["attributed_support_ids", "withheld"],
            "support attribution shape",
        )?;
        if c["stress_maximum_coverage"]["complete"] != true
            || c["stress_maximum_coverage"]["unavailable_pipe_ids"]
                .as_array()
                .is_none_or(|v| !v.is_empty())
            || c["stress_maximum_coverage"]["outside_domain_pipe_ids"]
                .as_array()
                .is_none_or(|v| !v.is_empty())
            || c["intensified_measures"]
                .as_array()
                .is_none_or(|v| !v.is_empty())
        {
            return Err("maximum/SIF coverage".into());
        }
        let attributed = c["support_attribution"]["attributed_support_ids"]
            .as_array()
            .ok_or("support attribution")?;
        if attributed.len() != self.supports.len()
            || c["support_attribution"]["withheld"]
                .as_array()
                .is_none_or(|v| !v.is_empty())
        {
            return Err("support attribution coverage".into());
        }
        for (id, _) in &self.supports {
            if attributed
                .iter()
                .filter(|v| v.as_str() == Some(id.as_str()))
                .count()
                != 1
            {
                return Err("support attribution identity".into());
            }
        }
        let extrema = c["pipe_stress_extrema"].as_array().ok_or("extrema")?;
        if extrema.len() != self.members.len() {
            return Err("extrema coverage".into());
        }
        for (index, x) in extrema.iter().enumerate() {
            self.adapter.enter(AdapterEvent::RowVisit, 1);
            self.adapter.enter(AdapterEvent::ValidationEntry, 1);
            self.adapter.require()?;
            const KEYS: [&str; 13] = [
                "pipe_id",
                "result_id",
                "station_fraction",
                "span_index",
                "local_fraction",
                "value_lower_pa",
                "value_upper_pa",
                "global_upper_bound_pa",
                "certified_gap_pa",
                "subdivisions",
                "approximation",
                "coefficient_basis",
                "enclosure_scope",
            ];
            let object = x.as_object().ok_or("extrema object")?;
            if object.len() != KEYS.len() || object.keys().any(|k| !KEYS.contains(&k.as_str())) {
                return Err("extrema shape".into());
            }
            for key in ["station_fraction", "local_fraction"] {
                let n = x[key].as_f64().ok_or("extrema fraction")?;
                if !n.is_finite() || !(0.0..=1.0).contains(&n) {
                    return Err("extrema fraction".into());
                }
            }
            for (key, max) in [("span_index", f64::MAX), ("subdivisions", 131072.0)] {
                let n = x[key].as_f64().ok_or("extrema integer")?;
                if !n.is_finite() || n < 0.0 || n > max || n.fract() != 0.0 {
                    return Err("extrema integer".into());
                }
            }
            for key in [
                "value_lower_pa",
                "value_upper_pa",
                "global_upper_bound_pa",
                "certified_gap_pa",
            ] {
                if !x[key].as_f64().is_some_and(f64::is_finite) {
                    return Err("extrema finite".into());
                }
            }
            if x["approximation"]!="piecewise_quadratic_straight_section_statics"||x["coefficient_basis"]!="j_side_section_equilibrium_binary64"
                ||x["enclosure_scope"]!="supplied_binary64_polynomial_coefficients; solution and coefficient formation error are separate" {return Err("extrema scope".into());}
            if extrema[..index]
                .iter()
                .any(|a| a["pipe_id"] == x["pipe_id"] || a["result_id"] == x["result_id"])
            {
                return Err("extrema duplicate".into());
            }
            let id = x["result_id"].as_str().ok_or("maximum ref")?;
            let row = e.results.iter().find(|r| r.id == id).ok_or("maximum row")?;
            let lo = x["value_lower_pa"].as_f64().ok_or("lower")?;
            let hi = x["value_upper_pa"].as_f64().ok_or("upper")?;
            if !(lo >= 0.0
                && lo <= row.value
                && row.value <= hi
                && row.value == lo + 0.5 * (hi - lo))
            {
                return Err("maximum midpoint".into());
            }
            if x["pipe_id"] != row.entity_ref || row.kind != "pipe_elastic_normal_stress_maximum_v2"
            {
                return Err("maximum binding".into());
            }
        }
        for (id, _) in &self.supports {
            self.adapter.enter(AdapterEvent::RowVisit, 1);
            self.adapter.require()?;
            let rows: Vec<_> = e
                .results
                .iter()
                .filter(|r| &r.entity_ref == id && r.kind == "support_reaction_component_v2")
                .collect();
            if rows.len() != 6 {
                return Err("support coverage".into());
            }
            for (components, kind) in [
                (["Fx", "Fy", "Fz"], "support_reaction_force_magnitude_v2"),
                (["Mx", "My", "Mz"], "support_reaction_moment_magnitude_v2"),
            ] {
                let mut v = [0.0; 3];
                for (i, c) in components.into_iter().enumerate() {
                    let matches: Vec<_> = rows
                        .iter()
                        .filter(|r| r.metadata.as_ref().is_some_and(|m| m.component == c))
                        .collect();
                    if matches.len() != 1 {
                        return Err("support component identity".into());
                    }
                    v[i] = matches[0].value;
                }
                let matches: Vec<_> = e
                    .results
                    .iter()
                    .filter(|r| &r.entity_ref == id && r.kind == kind)
                    .collect();
                if matches.len() != 1 {
                    return Err("support magnitude identity".into());
                }
                let y = matches[0].value;
                if (y - v[0].hypot(v[1]).hypot(v[2])).abs()
                    > 64.0 * f64::EPSILON * y.abs().max(f64::MIN_POSITIVE)
                {
                    return Err("support guard".into());
                }
            }
        }
        for (headline, kind) in [
            (&e.summary.max_displacement, "displacement_magnitude"),
            (
                &e.summary.max_open_formula_stress,
                "pipe_elastic_normal_stress_maximum_v2",
            ),
        ] {
            let h = headline.as_ref().ok_or("headline")?;
            let best = e
                .results
                .iter()
                .filter(|r| r.kind == kind)
                .max_by(|a, b| {
                    a.value
                        .total_cmp(&b.value)
                        .then_with(|| b.entity_ref.cmp(&a.entity_ref))
                })
                .ok_or("headline candidate")?;
            if h.result_ref != best.id
                || h.value.to_bits() != best.value.to_bits()
                || h.unit != best.unit
                || h.location_ref != best.entity_ref
            {
                return Err("headline alias".into());
            }
        }
        Ok(())
    }
}

fn validate_final_metadata(
    row: &ResultItem,
    recipe: k::ProductRecipe,
    case: &str,
    work: &AdapterWork,
) -> Result<(), CaptureError> {
    work.require()?;
    work.enter(AdapterEvent::LibraryBoundary, 1); // Fixed expected-text construction, with formatting/allocator internals unqualified.

    if !row.source_result_refs.is_empty() {
        return Err("unexpected final source references".into());
    }
    let suffix = stable_suffix(&row.entity_ref);
    let m = row.metadata.as_ref();
    let meta = |component: &str,
                coordinate: &str,
                location: &str,
                basis: &str,
                sign: &str|
     -> Result<(), CaptureError> {
        let m = m.ok_or("missing final metadata")?;
        if !work.same(&m.component, component)
            || !work.same(&m.coordinate_system, coordinate)
            || !work.same(&m.location, location)
            || !work.same(&m.basis, basis)
            || !work.same(&m.sign_convention, sign)
        {
            work.require()?;
            return Err(CaptureError::Association(format!(
                "final metadata mismatch: {}",
                row.id
            )));
        }
        Ok(())
    };
    let expected = match recipe {
        k::ProductRecipe::NonQuantity => {
            let m = m.ok_or("mode metadata")?;
            if row.kind != "linear_solver_mode_basis"
                || row.entity_ref != "solver:linear_static_preview"
                || m.component != "linear_solver_mode"
                || m.coordinate_system != "reduced_system"
                || m.location != case
                || !(row.value == 1.0 || row.value == 2.0)
            {
                return Err("ordinary mode record".into());
            }
            work.enter(AdapterEvent::ValidationEntry, 1);
            work.require()?;
            let sign_matches = work.same(
                &m.sign_convention,
                "mode_code 1=sparse_interactive, 2=dense_scrutiny, 3=dense_fallback_after_sparse_failure",
            );
            work.require()?;
            if !sign_matches {
                return Err("ordinary sparse mode sign".into());
            }
            "result:solver-mode:linear-solve-basis".to_string()
        }
        k::ProductRecipe::DenseParityObservation => {
            let m=m.ok_or("parity metadata")?;
            meta("sparse_live_path","reduced_system","load_case",&m.basis,
                "unitless max absolute dense-sparse solution delta divided by max dense solution magnitude; no release threshold asserted")?;
            "result:sparse-live:dense-parity-relative-delta".to_string()
        }
        k::ProductRecipe::Native(k::QuantityId::DisplacementMagnitude(_)) => {
            if m.is_some() {
                return Err("magnitude metadata".into());
            }
            format!("result:disp:{suffix}")
        }
        k::ProductRecipe::Native(k::QuantityId::Displacement(d)) => {
            let i = d.component.index();
            let axis = ["X", "Y", "Z"][i % 3];
            let component = [
                "nodal_displacement_x",
                "nodal_displacement_y",
                "nodal_displacement_z",
                "nodal_rotation_x",
                "nodal_rotation_y",
                "nodal_rotation_z",
            ][i];
            let sign = if i < 3 {
                format!("positive value follows the global cartesian {axis} axis displacement of the node")
            } else {
                format!("positive value follows the right-hand-rule rotation about the global cartesian {axis} axis")
            };
            meta(
                component,
                "global",
                "node",
                "solved_from_global_linear_system",
                &sign,
            )?;
            format!(
                "result:disp:{suffix}:{}",
                ["ux", "uy", "uz", "rx", "ry", "rz"][i]
            )
        }
        k::ProductRecipe::Native(k::QuantityId::EndAction { end, component, .. }) => {
            let i = component.index();
            let loc = if end == k::End::I { "end_i" } else { "end_j" };
            let sign = if end == k::End::I {
                "positive value follows the element-local DOF at the i-end force vector"
            } else {
                "positive value follows the element-local DOF at the j-end force vector"
            };
            meta(
                [
                    "axial_force",
                    "shear_force_y",
                    "shear_force_z",
                    "torsional_moment",
                    "bending_moment_y",
                    "bending_moment_z",
                ][i],
                "element_local",
                loc,
                SECTION_RESULTANT_BASIS,
                sign,
            )?;
            format!(
                "result:{}:{suffix}:{}{}",
                if i < 3 { "force" } else { "moment" },
                [
                    "axial",
                    "shear-y",
                    "shear-z",
                    "torsion",
                    "bending-y",
                    "bending-z"
                ][i],
                if end == k::End::J { ":end-j" } else { "" }
            )
        }
        k::ProductRecipe::Native(k::QuantityId::StationAction { component, .. }) => {
            let i = component.index();
            let loc = m.ok_or("station metadata")?.location.as_str();
            meta(["axial_force","shear_force_y","shear_force_z","torsional_moment","bending_moment_y","bending_moment_z"][i],
                "element_local",loc,SECTION_RESULTANT_BASIS,"positive value follows the j-side section action in the element-local frame (x toward end j); section equilibrium from stiffness-recovered end actions with consistent distributed-load fixed-end correction")?;
            format!(
                "result:{}:{suffix}:{}:{}",
                if i < 3 { "force" } else { "moment" },
                station_id_location(loc),
                [
                    "axial",
                    "shear-y",
                    "shear-z",
                    "torsion",
                    "bending-y",
                    "bending-z"
                ][i]
            )
        }
        k::ProductRecipe::SupportComponent { .. } | k::ProductRecipe::Native(
            k::QuantityId::SupportForceMagnitude(_)
            | k::QuantityId::SupportMomentMagnitude(_),
        ) => {
            let component = match recipe {
                k::ProductRecipe::SupportComponent { component, .. } => {
                    ["Fx", "Fy", "Fz", "Mx", "My", "Mz"][component.index()]
                }
                k::ProductRecipe::Native(k::QuantityId::SupportForceMagnitude(_)) => {
                    "force_magnitude"
                }
                k::ProductRecipe::Native(k::QuantityId::SupportMomentMagnitude(_)) => {
                    "moment_magnitude"
                }
                _ => unreachable!("the enclosing arm admits only these support recipes"),
            };
            meta(component,"global","node","recovered_from_assembled_support_law",
                "support-on-pipe; positive global force and right-hand couple about attached node; force and moment norms remain separate")?;
            format!(
                "result:support-action:{}:{}:{}:{}:{}",
                case.len(),
                case,
                row.entity_ref.len(),
                row.entity_ref,
                component
            )
        }
        k::ProductRecipe::Stress { site, stress, .. } => {
            let (component, tail) = match stress {
                k::ProductStress::Axial => ("axial_normal_stress", "axial-normal"),
                k::ProductStress::BendingY => ("bending_normal_stress_y", "bending-normal-y"),
                k::ProductStress::BendingZ => ("bending_normal_stress_z", "bending-normal-z"),
                k::ProductStress::Torsion => ("torsional_shear_stress", "torsional-shear"),
            };
            let loc = m.ok_or("stress metadata")?.location.as_str();
            let (idloc, basis, sign) = if matches!(site, k::ProductSite::End(_)) {
                (
                    endpoint_id_location(loc),
                    SECTION_RESULTANT_BASIS,
                    STRAIGHT_ENDPOINT_SECTION_SIGN_CONVENTION.to_string(),
                )
            } else {
                let prefix=match stress {
                    k::ProductStress::Axial=>"positive normal stress follows the section-equilibrium element-local axial resultant at this station",
                    k::ProductStress::BendingY=>"positive bending normal stress follows the section-equilibrium element-local y bending resultant at this station",
                    k::ProductStress::BendingZ=>"positive bending normal stress follows the section-equilibrium element-local z bending resultant at this station",
                    k::ProductStress::Torsion=>"positive torsional shear stress follows the section-equilibrium element-local torsional resultant at this station",
                };
                (station_id_location(loc),"recovered_from_open_mechanics_stress_components",format!("{prefix}; j-side section action in the element-local frame (x toward end j); section equilibrium from stiffness-recovered end actions with consistent distributed-load fixed-end correction"))
            };
            meta(component, "element_local", loc, basis, &sign)?;
            format!("result:stress:{suffix}:{idloc}:{tail}")
        }
        k::ProductRecipe::CircularMaximum { .. } => {
            meta("maximum_absolute_normal_stress","pipe_section","governing_station","recovered_from_open_mechanics_stress_components",
                "nonnegative circumferential maximum |Nw/As|+hypot(My,Mz)/Z; bounded over all straight statics intervals; torsional shear remains separate; no code stress or equivalent stress claim")?;
            format!(
                "result:elastic-maximum:{}:{}:{}:{}",
                case.len(),
                case,
                row.entity_ref.len(),
                row.entity_ref
            )
        }
        _ => return Err("unsupported metadata recipe".into()),
    };
    work.require()?;
    if !work.same(&row.id, &expected) {
        work.require()?;
        return Err(CaptureError::Association(format!(
            "final id association: {}",
            row.id
        )));
    }
    Ok(())
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum ScalarOperation {
    Add,
    Sub,
    Mul,
    Div,
    Sqrt,
}
#[derive(Debug, Clone, PartialEq)]
pub(super) enum OperationalError {
    MissingOrForeign,
    Input,
    Degenerate,
    NonFinite {
        operation: ScalarOperation,
        entered: u64,
    },
    CoefficientRange {
        coefficient: &'static str,
        operation: ScalarOperation,
    },
    Accounting,
}
#[derive(Debug, Default)]
pub(super) struct ScalarWork {
    pub entered: u64,
    pub checks: u64,
    pub lost: bool,
}
impl ScalarWork {
    fn check(&mut self) -> Result<(), OperationalError> {
        if self.lost {
            return Err(OperationalError::Accounting);
        }
        match self.checks.checked_add(1) {
            Some(n) => self.checks = n,
            None => {
                self.lost = true;
                return Err(OperationalError::Accounting);
            }
        }
        if self.lost {
            Err(OperationalError::Accounting)
        } else {
            Ok(())
        }
    }
    pub(super) fn op(
        &mut self,
        kind: ScalarOperation,
        a: f64,
        b: f64,
    ) -> Result<f64, OperationalError> {
        self.operation(kind, a, b, None)
    }
    fn operation(
        &mut self,
        kind: ScalarOperation,
        a: f64,
        b: f64,
        normal: Option<&'static str>,
    ) -> Result<f64, OperationalError> {
        if self.lost {
            return Err(OperationalError::Accounting);
        }
        let Some(n) = self.entered.checked_add(1) else {
            self.lost = true;
            return Err(OperationalError::Accounting);
        };
        self.entered = n;
        let value = match kind {
            ScalarOperation::Add => a + b,
            ScalarOperation::Sub => a - b,
            ScalarOperation::Mul => a * b,
            ScalarOperation::Div => a / b,
            ScalarOperation::Sqrt => a.sqrt(),
        };
        // Numeric result is formed before collection. Collection loss cannot erase it.
        let numeric = if let Some(coefficient) = normal {
            if !value.is_normal() {
                Err(OperationalError::CoefficientRange {
                    coefficient,
                    operation: kind,
                })
            } else {
                Ok(value)
            }
        } else if !value.is_finite() {
            Err(OperationalError::NonFinite {
                operation: kind,
                entered: n,
            })
        } else {
            Ok(value)
        };
        let collected = self.check().and_then(|()| {
            if normal.is_some() {
                self.check()
            } else {
                Ok(())
            }
        });
        match numeric {
            Err(e) => Err(e),
            Ok(v) => collected.map(|()| v),
        }
    }
    fn norm(&mut self, d: [f64; 3]) -> Result<f64, OperationalError> {
        let x = self.op(ScalarOperation::Mul, d[0], d[0])?;
        let y = self.op(ScalarOperation::Mul, d[1], d[1])?;
        let xy = self.op(ScalarOperation::Add, x, y)?;
        let z = self.op(ScalarOperation::Mul, d[2], d[2])?;
        let xyz = self.op(ScalarOperation::Add, xy, z)?;
        self.op(ScalarOperation::Sqrt, xyz, 0.0)
    }
    pub(super) fn coefficient(
        &mut self,
        a: f64,
        b: f64,
        l: f64,
        name: &'static str,
    ) -> Result<f64, OperationalError> {
        let p = self.operation(ScalarOperation::Mul, a, b, Some(name))?;
        self.operation(ScalarOperation::Div, p, l, Some(name))
    }
}
#[derive(Debug, Clone, Copy)]
pub(super) struct OperationalOperands {
    pub length: f64,
    pub axial: f64,
    pub torsion: f64,
    pub normalization_check: [f64; 3],
}
#[derive(Debug)]
pub(super) struct OperationalSpent {
    pub inputs: [u64; 10],
    pub result: Result<OperationalOperands, OperationalError>,
    pub work: ScalarWork,
}
/// Newly evaluated operational expressions, never historical formation capture.
pub(super) fn evaluate_operational(nodes: [[f64; 3]; 2], properties: [f64; 4]) -> OperationalSpent {
    let [e, g, a, j] = properties;
    let input = [
        nodes[0][0],
        nodes[0][1],
        nodes[0][2],
        nodes[1][0],
        nodes[1][1],
        nodes[1][2],
        e,
        g,
        a,
        j,
    ];
    let mut work = ScalarWork::default();
    let result = (|| {
        for (i, &v) in input.iter().enumerate() {
            work.check()?;
            if !v.is_finite() || (i >= 6 && v <= 0.0) {
                return Err(OperationalError::Input);
            }
        }
        let mut d = [0.0; 3];
        for i in 0..3 {
            d[i] = work.op(ScalarOperation::Sub, nodes[1][i], nodes[0][i])?;
        }
        let magnitude = work.norm(d)?;
        work.check()?;
        if magnitude <= 1.0e-12 {
            return Err(OperationalError::Degenerate);
        }
        let inverse = work.op(ScalarOperation::Div, 1.0, magnitude)?;
        let mut normalization_check = [0.0; 3];
        for i in 0..3 {
            normalization_check[i] = work.op(ScalarOperation::Mul, d[i], inverse)?;
        }
        let length = work.norm(d)?;
        work.check()?;
        if length <= 0.0 {
            return Err(OperationalError::Input);
        }
        let axial = work.coefficient(e, a, length, "EA/L")?;
        let torsion = work.coefficient(g, j, length, "GJ/L")?;
        Ok(OperationalOperands {
            length,
            axial,
            torsion,
            normalization_check,
        })
    })();
    OperationalSpent {
        inputs: input.map(f64::to_bits),
        result,
        work,
    }
}
#[derive(Debug, Clone, PartialEq)]
pub(super) enum G5aFailure {
    Accounting(AdapterFault),
    Shape(&'static str),
    Summary(&'static str),
    Zero {
        row: usize,
    },
    Sanity {
        body: u32,
        kind: usize,
    },
    Lower {
        member: u32,
        kind: usize,
    },
    Operational {
        member: usize,
        cause: OperationalError,
    },
    Arithmetic(OperationalError),
}
impl From<OperationalError> for G5aFailure {
    fn from(e: OperationalError) -> Self {
        Self::Arithmetic(e)
    }
}
impl ProductCapture {
    pub(super) fn full_case_passed(&self) -> bool {
        self.error.is_none()
            && self.adapter.fault.get().is_none()
            && self.final_calls == 1
            && self.numeric_pass
            && self.observable_error.is_none()
            && self.g5a_error.is_none()
            && !self.g5a_work.lost
            && self
                .operational
                .iter()
                .all(|o| !o.work.lost && o.result.is_ok())
    }
    pub(super) fn g5a(
        &mut self,
        owner: &k::RetainedSolve,
        rows: &[k::ProductFinalRow<'_>],
    ) -> Result<(), G5aFailure> {
        if let Some(fault) = self.adapter.fault.get() { return Err(G5aFailure::Accounting(fault)); }
        let source = owner.source();
        let evidence = owner.evidence();
        let nb = source.body_count() as usize;
        let nonnegative = |v: f64| v.is_finite() && v >= 0.0 && (v != 0.0 || v.to_bits() == 0);
        if self.verdicts.len() != rows.len() || self.operational.len() != self.facts.len() {
            return Err(G5aFailure::Shape("final/operational rows"));
        }
        validate_summary_shape(evidence, &self.summary_coverage, nb)?;
        // B presence/data ownership is also checked by the same producing SourceBridgeView.
        for b in 0..nb {
            let rs: Vec<_> = evidence
                .resolution_scale
                .iter()
                .filter(|v| v.0 == b as u32)
                .collect();
            if rs.len() != 1 {
                return Err(G5aFailure::Shape("resolution coverage"));
            }
            let resolution = [f64::from_bits(rs[0].1), f64::from_bits(rs[0].2)];
            if resolution.iter().any(|v| !nonnegative(*v)) {
                return Err(G5aFailure::Summary("resolution"));
            }
            let mut scales = [0.0f64; 4];
            let mut bounds: Option<([f64; 3], [f64; 3])> = None;
            for (i, node) in source.nodes().iter().enumerate() {
                if source.body_of_node(i as u32) != b as u32 {
                    continue;
                }
                let (mut lo, mut hi) = bounds.unwrap_or((*node, *node));
                for j in 0..3 {
                    lo[j] = lo[j].min(node[j]);
                    hi[j] = hi[j].max(node[j]);
                }
                bounds = Some((lo, hi));
            }
            let (lo, hi) = bounds.ok_or(G5aFailure::Shape("body nodes"))?;
            let mut delta = [0.0; 3];
            for j in 0..3 {
                delta[j] = self.g5a_work.op(ScalarOperation::Sub, hi[j], lo[j])?;
            }
            let extent = self.g5a_work.norm(delta)?;
            for (i, row) in rows.iter().enumerate() {
                if row.body != b as u32 {
                    continue;
                }
                let classified = match row.recipe {
                    k::ProductRecipe::Native(id) => {
                        let meta = owner.publish().rows.iter().find(|r| r.id == id)
                            .ok_or(G5aFailure::Shape("native row"))?;
                        let kind = match meta.kind { k::Kind::Translation => 0, k::Kind::Rotation => 1,
                            k::Kind::Force => 2, k::Kind::Moment => 3 };
                        Some((kind, meta.class == k::RowClass::InputDerived))
                    }
                    k::ProductRecipe::SupportComponent { support, component } => {
                        let mut group = None;
                        for g in source.supports() {
                            if !self.adapter.enter(AdapterEvent::RowVisit, 1)
                                || !self.adapter.enter(AdapterEvent::ValidationEntry, 1) {
                                return Err(G5aFailure::Accounting(self.adapter.fault.get().unwrap()));
                            }
                            if g.id == support { group = Some(g); break; }
                        }
                        let group = group.ok_or(G5aFailure::Shape("support group"))?;
                        if source.body_of_node(group.node) != row.body {
                            return Err(G5aFailure::Shape("support body"));
                        }
                        Some((if component.index() < 3 { 2 } else { 3 }, false))
                    }
                    _ => None,
                };
                if let Some((kind, input)) = classified {
                    let n = f64::from_bits(self.verdicts[i].normalized_bits);
                    if kind >= 2 && resolution[kind - 2] == 0.0 && n.to_bits() != 0 {
                        return Err(G5aFailure::Zero { row: i });
                    }
                    if !input { scales[kind] = scales[kind].max(n.abs()); }
                }
            }
            if extent != 0.0 {
                let [tr, ro, fo, mo] = scales;
                scales = [
                    tr.max(self.g5a_work.op(ScalarOperation::Mul, extent, ro)?),
                    ro.max(self.g5a_work.op(ScalarOperation::Div, tr, extent)?),
                    fo.max(self.g5a_work.op(ScalarOperation::Div, mo, extent)?),
                    mo.max(self.g5a_work.op(ScalarOperation::Mul, extent, fo)?),
                ];
            }
            let hats = if extent == 0.0 {
                resolution
            } else {
                [
                    resolution[0].max(self.g5a_work.op(
                        ScalarOperation::Div,
                        resolution[1],
                        extent,
                    )?),
                    resolution[1].max(self.g5a_work.op(
                        ScalarOperation::Mul,
                        extent,
                        resolution[0],
                    )?),
                ]
            };
            let mut upper = [0.0; 2];
            for j in 0..2 {
                upper[j] = self.g5a_work.op(
                    ScalarOperation::Mul,
                    hats[j],
                    f64::from_bits(0x3ff0000000001000),
                )?;
                if upper[j] < scales[j + 2] {
                    return Err(G5aFailure::Sanity {
                        body: b as u32,
                        kind: j,
                    });
                }
            }
            for (mi, m) in source.members().iter().enumerate() {
                if source.body_of_node(m.node_i) != b as u32 {
                    continue;
                }
                let op = &self.operational[mi];
                let [a, c] = [
                    source.nodes()[m.node_i as usize],
                    source.nodes()[m.node_j as usize],
                ];
                let inputs = [
                    a[0],
                    a[1],
                    a[2],
                    c[0],
                    c[1],
                    c[2],
                    m.elastic_modulus,
                    m.shear_modulus,
                    m.area,
                    m.torsion_constant,
                ]
                .map(f64::to_bits);
                if op.inputs != inputs {
                    return Err(G5aFailure::Operational {
                        member: mi,
                        cause: OperationalError::MissingOrForeign,
                    });
                }
                if op.work.lost {
                    return Err(G5aFailure::Operational {
                        member: mi,
                        cause: OperationalError::Accounting,
                    });
                }
                let values = op
                    .result
                    .as_ref()
                    .map_err(|cause| G5aFailure::Operational {
                        member: mi,
                        cause: cause.clone(),
                    })?;
                let mut endpoint_norms = [[0.0; 2]; 2];
                for (end, node) in [m.node_i, m.node_j].into_iter().enumerate() {
                    for kind in 0..2 {
                        let mut x = [0.0; 3];
                        for (j, v) in x.iter_mut().enumerate() {
                            let id = k::QuantityId::Displacement(k::Dof {
                                node,
                                component: k::Component::ALL[kind * 3 + j],
                            });
                            let matches: Vec<_> = rows
                                .iter()
                                .enumerate()
                                .filter(|(_, r)| r.recipe == k::ProductRecipe::Native(id))
                                .collect();
                            if matches.len() != 1 {
                                return Err(G5aFailure::Shape(
                                    "all nodal components including input-derived",
                                ));
                            }
                            *v = f64::from_bits(self.verdicts[matches[0].0].normalized_bits).abs();
                        }
                        let xy = self.g5a_work.op(ScalarOperation::Add, x[0], x[1])?;
                        let n = self.g5a_work.op(ScalarOperation::Add, xy, x[2])?;
                        endpoint_norms[end][kind] = n;
                    }
                }
                let norm = [
                    self.g5a_work.op(
                        ScalarOperation::Add,
                        endpoint_norms[0][0],
                        endpoint_norms[1][0],
                    )?,
                    self.g5a_work.op(
                        ScalarOperation::Add,
                        endpoint_norms[0][1],
                        endpoint_norms[1][1],
                    )?,
                ];
                for kind in 0..2 {
                    let threshold = self.g5a_work.op(
                        ScalarOperation::Mul,
                        f64::from_bits((1023u64 - 59) << 52),
                        scales[kind],
                    )?;
                    let lower = if norm[kind] <= threshold {
                        0.0
                    } else {
                        let margin = self.g5a_work.op(
                            ScalarOperation::Mul,
                            f64::from_bits((1023u64 - 60) << 52),
                            scales[kind],
                        )?;
                        let net = self.g5a_work.op(ScalarOperation::Sub, norm[kind], margin)?;
                        self.g5a_work.op(
                            ScalarOperation::Mul,
                            if kind == 0 {
                                values.axial
                            } else {
                                values.torsion
                            },
                            net,
                        )?
                    };
                    if upper[kind] < lower {
                        return Err(G5aFailure::Lower { member: m.id, kind });
                    }
                }
            }
        }
        Ok(())
    }
}

pub(super) fn validate_summary_shape(
    e: &k::RetainedEvidence,
    coverage: &[k::ProductSummaryCoverage],
    bodies: usize,
) -> Result<(), G5aFailure> {
    let nonnegative = |v: f64| v.is_finite() && v >= 0.0 && (v != 0.0 || v.to_bits() == 0);
    if coverage.len() != bodies || e.resolution_scale.len() != bodies || e.theta.len() != bodies {
        return Err(G5aFailure::Shape("body summaries"));
    }
    for (i, c) in coverage.iter().enumerate() {
        if c.body as usize != i {
            return Err(G5aFailure::Shape("coverage owner"));
        }
    }
    for (entries, bound, label) in [
        (&e.stop_rule, f64::from_bits((1023u64 - 64) << 52), "stop"),
        (&e.verification_estimate, 0.25, "estimate"),
        (&e.verification_charge, 1.0, "charge"),
    ] {
        for &(b, kind, value) in entries {
            if b as usize >= bodies
                || (!matches!(kind, k::Kind::Force | k::Kind::Moment) && label != "stop")
            {
                return Err(G5aFailure::Shape(label));
            }
            if !nonnegative(value) || value > bound {
                return Err(G5aFailure::Summary(label));
            }
        }
        for c in coverage {
            for (i, kind) in [
                k::Kind::Translation,
                k::Kind::Rotation,
                k::Kind::Force,
                k::Kind::Moment,
            ]
            .into_iter()
            .enumerate()
            {
                let wanted = if label == "stop" {
                    c.stop[i]
                } else if i < 2 {
                    false
                } else if label == "estimate" {
                    c.estimate[i - 2]
                } else {
                    c.charge[i - 2]
                };
                if entries
                    .iter()
                    .filter(|v| v.0 == c.body && v.1 == kind)
                    .count()
                    != usize::from(wanted)
                {
                    return Err(G5aFailure::Shape(label));
                }
            }
        }
    }
    for c in coverage {
        let theta: Vec<_> = e.theta.iter().filter(|v| v.0 == c.body).collect();
        let resolution: Vec<_> = e
            .resolution_scale
            .iter()
            .filter(|v| v.0 == c.body)
            .collect();
        if theta.len() != 1 || resolution.len() != 1 {
            return Err(G5aFailure::Shape("theta/resolution"));
        }
        if !nonnegative(theta[0].1) || theta[0].1 > 0.5 {
            return Err(G5aFailure::Summary("theta"));
        }
        let bounds: Vec<_> = e.certified_bound.iter().filter(|v| v.0 == c.body).collect();
        if bounds.len() != usize::from(c.has_data) {
            return Err(G5aFailure::Shape("B data coverage"));
        }
        for b in bounds {
            let value = f64::from_bits(b.1);
            if !value.is_finite() || value <= 0.0 {
                return Err(G5aFailure::Summary("B"));
            }
        }
    }
    if e.certified_bound.iter().any(|v| v.0 as usize >= bodies) {
        return Err(G5aFailure::Shape("B body"));
    }
    Ok(())
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum AdapterEvent {
    SourceVisit = 0,
    RowVisit = 1,
    MapWrite = 2,
    ValidationEntry = 3,
    IdentityByteRead = 4,
    KeyProbe = 5,
    AllocationRequest = 6,
    LibraryBoundary = 7,
    RequestedCopyBytes = 8,
    RustCapacityBytes = 9,
}
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(super) enum AdapterFault {
    Overflow(AdapterEvent),
}
#[derive(Debug, Default)]
pub(super) struct AdapterWork {
    pub counts: std::cell::Cell<[u64; 10]>,
    pub fault: std::cell::Cell<Option<AdapterFault>>,
}
impl AdapterWork {
    /// Closed borrowed key decoder. Charge each entered group, key visit and actual comparison.
    fn closed_keys(
        &self,
        value: &serde_json::Value,
        expected: &[&str],
        reason: &'static str,
    ) -> Result<(), CaptureError> {
        self.enter(AdapterEvent::ValidationEntry, 1);
        self.enter(AdapterEvent::LibraryBoundary, 1);
        self.require()?;
        let object = value.as_object().ok_or(reason)?;
        if object.len() != expected.len() {
            return Err(reason.into());
        }
        for key in object.keys() {
            self.enter(AdapterEvent::RowVisit, 1);
            self.require()?;
            let mut matched = false;
            for allowed in expected {
                let equal = self.same(key, allowed);
                self.require()?;
                if equal {
                    matched = true;
                    break;
                }
            }
            if !matched {
                return Err(reason.into());
            }
        }
        Ok(())
    }
    fn enter(&self, event: AdapterEvent, amount: u64) -> bool {
        if self.fault.get().is_some() {
            return false;
        }
        let mut counts = self.counts.get();
        let Some(value) = counts[event as usize].checked_add(amount) else {
            self.fault.set(Some(AdapterFault::Overflow(event)));
            return false;
        };
        counts[event as usize] = value;
        self.counts.set(counts);
        true
    }
    fn require(&self) -> Result<(), CaptureError> {
        self.fault
            .get()
            .map_or(Ok(()), |f| Err(CaptureError::Accounting(f)))
    }
    /// Actual explicit comparison reads, stopping at the first mismatch.
    pub(super) fn same(&self, a: &str, b: &str) -> bool {
        if !self.enter(AdapterEvent::KeyProbe, 1) || !self.enter(AdapterEvent::ValidationEntry, 1) {
            return false;
        }
        if a.len() != b.len() {
            return false;
        }
        for i in 0..a.len() {
            if !self.enter(AdapterEvent::IdentityByteRead, 2) {
                return false;
            }
            if a.as_bytes()[i] != b.as_bytes()[i] {
                return false;
            }
        }
        true
    }
    pub(super) fn reserve<T>(&self, n: usize) -> Result<Vec<T>, CaptureError> {
        let layout = std::alloc::Layout::array::<T>(n)
            .map_err(|_| CaptureError::CountRange("adapter layout"))?;
        let _requested_layout = layout;
        if !self.enter(AdapterEvent::AllocationRequest, 1) {
            return Err(CaptureError::Accounting(self.fault.get().unwrap()));
        }
        let mut out = Vec::new();
        out.try_reserve_exact(n)
            .map_err(|_| CaptureError::Storage("adapter vector"))?;
        let bytes = out
            .capacity()
            .checked_mul(std::mem::size_of::<T>())
            .ok_or(CaptureError::CountRange("adapter capacity bytes"))?;
        let size = u64::try_from(bytes)
            .map_err(|_| CaptureError::CountRange("adapter capacity conversion"))?;
        if !self.enter(AdapterEvent::RustCapacityBytes, size) {
            return Err(CaptureError::Accounting(self.fault.get().unwrap()));
        }
        Ok(out)
    }
    fn copy(&self, s: &str) -> Result<String, CaptureError> {
        let n = u64::try_from(s.len()).map_err(|_| CaptureError::CountRange("identity bytes"))?;
        if !self.enter(AdapterEvent::AllocationRequest, 1)
            || !self.enter(AdapterEvent::RequestedCopyBytes, n)
        {
            return Err(CaptureError::Accounting(self.fault.get().unwrap()));
        }
        let mut out = String::new();
        out.try_reserve_exact(s.len())
            .map_err(|_| CaptureError::Storage("identity copy"))?;
        out.push_str(s);
        if !self.enter(AdapterEvent::RustCapacityBytes, out.capacity() as u64) {
            return Err(CaptureError::Accounting(self.fault.get().unwrap()));
        }
        Ok(out)
    }
    fn push_room<T>(&self, v: &mut Vec<T>) -> Result<(), CaptureError> {
        if v.len() == v.capacity() {
            if !self.enter(AdapterEvent::AllocationRequest, 1) {
                return Err(CaptureError::Accounting(self.fault.get().unwrap()));
            }
            v.try_reserve_exact(1)
                .map_err(|_| CaptureError::Storage("adapter growth"))?;
            let bytes = v
                .capacity()
                .checked_mul(std::mem::size_of::<T>())
                .ok_or(CaptureError::CountRange("adapter growth bytes"))?;
            if !self.enter(AdapterEvent::RustCapacityBytes, bytes as u64) {
                return Err(CaptureError::Accounting(self.fault.get().unwrap()));
            }
        }
        Ok(())
    }
}

impl From<&str> for CaptureError {
    fn from(s: &str) -> Self {
        Self::Association(s.to_string())
    }
}
impl From<String> for CaptureError {
    fn from(s: String) -> Self {
        Self::Association(s)
    }
}
impl std::fmt::Display for CaptureError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Association(s) => f.write_str(s),
            _ => write!(f, "{self:?}"),
        }
    }
}

enum SelectorRef<'a> {
    Point(&'a str),
    Temperature(u64),
}
fn load_case_selector(case: &PreviewLoadCase) -> Option<SelectorRef<'_>> {
    if let Some(id) = case.modulus_basis_ref.as_deref() {
        Some(SelectorRef::Point(id))
    } else {
        case.modulus_basis_temperature
            .as_ref()
            .map(|t| SelectorRef::Temperature(t.value.to_bits()))
    }
}
