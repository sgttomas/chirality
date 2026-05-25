# Guidance: EPC / Controls Discipline Production Package

## Purpose

This document guides preparation and review of the controls discipline production package for `PKG-010 - Controls system design and integration`. The package exists to carry the non-vendor controls production basis for WBS 03 while preserving source limits identified in Gate 7.

## Principles

- Treat Gate 7 registers as the accepted decomposition truth for package identity, deliverable identity, interface membership, artifact expectations, and objective association.
- Treat the DBM SEC-13 controls basis as the accessible controls source slice for BPCS, RIO, control network, package controls, and safety-device wiring content.
- Keep unsupported detailed discipline outputs as `TBD`; Gate 7 explicitly records that detailed non-vendor package deliverable requirements are source-limited and remain open.
- Do not convert package-interface facts into a new package or deliverable. Gate 7 disposition keeps controls power-panel questions as interface facts/artifacts under the package datasheet.

## Considerations

The BPCS/RIO and network basis is specific enough to establish production-package requirements, but not complete enough to finish detailed design. Final controller sizing, data maps, alarm priorities, permissives, trip interfaces, IDMZ policies, firewall rules, VLAN segmentation, IP addressing, cause-and-effect actions, and reset responsibilities remain detailed-design/client/vendor coordination items.

Instrumentation and safety-device wiring should be coordinated with RIO layout, fire and gas detection, ESD placement, electrical area classification, building HVAC/ventilation, and package controls. The DBM basis supports nearest-practical RIO wiring for BPCS-associated process and safety devices, but final device lists and I/O assignments are not present in the accepted source slice.

Instrument air is a cross-facility interface supplied from 04-25. The controls package should include monitoring/alarm/trip interface treatment for the 03-25 instrument-air interface, but should not add local 03-25 instrument-air compressor controls.

## Trade-offs

| Topic | Trade-off / source-limited treatment |
|---|---|
| Control architecture specificity | The DBM names ControlLogix, Flex5000, PRP, PCN, I/O Network, IDMZ, and enterprise interfaces. It leaves final topology, sizing, policies, and addressing to detailed design. |
| Package integration | Standalone Unit Control Systems reduce direct BPCS control scope but require disciplined data maps, alarm priorities, permissives, trip interfaces, and vendor integration records. |
| Interface scope | PKG-010 has broad process, utility, electrical, communications, HVAC, and safety interfaces. The production package should preserve these interfaces while avoiding invented tagged equipment or unverified panel boundaries. |
| Closure record | Keeping unresolved discipline requirements as `TBD` slows completion but prevents unsupported requirements from being promoted into authoritative package content. |

## Examples

| Example topic | Acceptable treatment |
|---|---|
| Modbus package interface | State that Modbus is used for monitoring/data collection only, not process control, and require final package data maps to be resolved during vendor integration. |
| Safety detector wiring | State that BPCS-associated ESD, fire, LEL, H2S, and other process safety items are wired to nearest practical RIO panels, then leave final device and I/O lists as TBD. |
| Instrument air | State that 03-25 monitors the 04-25-supplied instrument-air interface and does not add local instrument-air compressor controls. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-010-04-001 | The responsible party is not assigned beyond "TBD; EPC Integrator or discipline subcontractor as assigned." | DELIVERABLE_REGISTER.csv, DEL-010-04 | _CONTEXT.md, Identity | Datasheet Identification; Specification Scope; Procedure Prerequisites | Keep responsibility as TBD until assignment is accepted. | TBD |
| HRR-010-04-002 | Detailed discipline deliverable register and final discipline production requirements are not available in the current source set. | ARTIFACT_REGISTER.csv, DEL-010-04 source-limited requirements closure record | DELIVERABLE_REGISTER.csv notes for DEL-010-04 | All four documents | Keep detailed register and unsupported requirements as TBD; require Gate 5/source-document disposition. | TBD |
| HRR-010-04-003 | Controls power-panel interfaces are noted for confirmation, but Gate 6 disposition keeps them under package datasheet artifacts rather than separate packages/deliverables. | INTERFACE_REGISTER.csv, PKG-010 notes | ARTIFACT_REGISTER.csv interface fact rows for PKG-010 | Specification Scope; Datasheet Construction | Follow Gate 6 disposition; do not create separate package/deliverable without human-approved decomposition change. | TBD |
