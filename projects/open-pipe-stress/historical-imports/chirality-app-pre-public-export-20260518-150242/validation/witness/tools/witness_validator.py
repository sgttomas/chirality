#!/usr/bin/env python3
"""Validate and render OpenPipeStress formal calculation witnesses.

This module is validation-local. It interprets a small OpenMath arithmetic
phrasebook and does not call production solver, section-property, or
stress-recovery implementation code.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, getcontext
from html import escape
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "validation" / "witness" / "schemas" / "openmath_calculation_witness.schema.json"
DEFAULT_WITNESS_PATH = (
    ROOT
    / "validation"
    / "witness"
    / "fixtures"
    / "tp_phys_015_section_property_stress_witness.json"
)

getcontext().prec = 50

ALLOWED_OPERATORS = {
    ("arith1", "plus"),
    ("arith1", "minus"),
    ("arith1", "times"),
    ("arith1", "divide"),
    ("arith1", "power"),
}
ALLOWED_CONSTANTS = {("nums1", "pi")}

DIMENSIONS = {
    "dimensionless": {},
    "length": {"length": 1},
    "area": {"length": 2},
    "section_modulus": {"length": 3},
    "second_moment_area": {"length": 4},
    "force": {"mass": 1, "length": 1, "time": -2},
    "moment": {"mass": 1, "length": 2, "time": -2},
    "stress": {"mass": 1, "length": -1, "time": -2},
}


class WitnessError(AssertionError):
    """Raised when a formal witness fails deterministic validation."""


@dataclass(frozen=True)
class Quantity:
    value: Decimal
    dimension: dict[str, int]
    dimension_id: str
    unit: str


@dataclass(frozen=True)
class Comparison:
    output_id: str
    formula_id: str
    result_id: str
    witness_value: Decimal
    result_value: Decimal
    delta: Decimal
    tolerance: Decimal
    unit: str
    dimension: str

    @property
    def passed(self) -> bool:
        return abs(self.delta) <= self.tolerance


@dataclass(frozen=True)
class WitnessEvaluation:
    witness_id: str
    witness_hash: str
    values: dict[str, Quantity]
    formula_order: list[str]
    comparisons: list[Comparison]


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def resolve_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def canonical_json(value: Any) -> str:
    """Return the project-local JCS-compatible canonical JSON form.

    Witness numeric values are decimal strings, so this avoids JSON float
    canonicalization ambiguity while preserving sorted-object determinism.
    """

    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def witness_hash(witness: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(witness).encode("utf-8")).hexdigest()


def validate_schema(witness: dict[str, Any]) -> None:
    try:
        from jsonschema import Draft202012Validator
    except ModuleNotFoundError as exc:
        raise WitnessError(
            "jsonschema>=4,<5 is required for formal witness schema validation"
        ) from exc

    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(witness), key=lambda error: list(error.path))
    if errors:
        formatted = "\n".join(_format_schema_error(error) for error in errors[:10])
        raise WitnessError(f"witness schema validation failed:\n{formatted}")


def _format_schema_error(error: Any) -> str:
    path = "$"
    for part in error.path:
        path += f"[{part}]" if isinstance(part, int) else f".{part}"
    return f"{path}: {error.message}"


def validate_required_provenance(witness: dict[str, Any]) -> None:
    _require_provenance(witness.get("provenance"), "witness.provenance")
    for collection_name in ("constants", "inputs", "formulas", "outputs"):
        for item in witness.get(collection_name, []):
            _require_provenance(
                item.get("provenance"),
                f"{collection_name}.{item.get('id', '<missing-id>')}.provenance",
            )


def _require_provenance(provenance: dict[str, Any] | None, subject: str) -> None:
    required = {
        "source_name",
        "source_location",
        "source_license",
        "contributor",
        "contributor_certification",
        "redistribution_status",
        "review_status",
    }
    if not isinstance(provenance, dict):
        raise WitnessError(f"missing provenance: {subject}")
    missing = sorted(name for name in required if not provenance.get(name))
    if missing:
        raise WitnessError(f"missing provenance fields at {subject}: {', '.join(missing)}")


def evaluate_witness(witness: dict[str, Any]) -> WitnessEvaluation:
    validate_schema(witness)
    validate_required_provenance(witness)
    _validate_professional_boundary(witness)
    _validate_content_dictionary_paths(witness)
    _validate_openmath_symbols(witness)

    values: dict[str, Quantity] = {}
    display: dict[str, str] = {}
    for binding in witness["constants"] + witness["inputs"]:
        quantity = _quantity_from_binding(binding)
        values[binding["id"]] = quantity
        display[binding["id"]] = binding["display"]
        openmath = binding["openmath"]
        if openmath["om_type"] == "OMS":
            values[_symbol_key(openmath)] = quantity

    formulas = {formula["id"]: formula for formula in witness["formulas"]}
    for formula in witness["formulas"]:
        display[formula["id"]] = formula["display"]

    formula_order: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def eval_variable(name: str) -> Quantity:
        if name in values:
            return values[name]
        if name not in formulas:
            raise WitnessError(f"unknown OpenMath variable reference: {name}")
        if name in visiting:
            raise WitnessError(f"formula graph cycle detected at {name}")
        if name not in visited:
            visiting.add(name)
            formula = formulas[name]
            raw = _eval_openmath(formula["openmath"], eval_variable, values)
            expected_dimension = formula["expected_dimension"]
            expected_vector = _dimension_vector(expected_dimension)
            if raw.dimension != expected_vector:
                raise WitnessError(
                    f"dimension mismatch for {name}: "
                    f"got {_dimension_name(raw.dimension)}, expected {expected_dimension}"
                )
            values[name] = Quantity(
                value=raw.value,
                dimension=expected_vector,
                dimension_id=expected_dimension,
                unit=formula["expected_unit"],
            )
            visited.add(name)
            visiting.remove(name)
            formula_order.append(name)
        return values[name]

    for formula in witness["formulas"]:
        eval_variable(formula["id"])

    comparisons = _compare_outputs(witness, values)
    return WitnessEvaluation(
        witness_id=witness["witness_id"],
        witness_hash=witness_hash(witness),
        values=values,
        formula_order=formula_order,
        comparisons=comparisons,
    )


def _validate_professional_boundary(witness: dict[str, Any]) -> None:
    boundary = witness["professional_boundary"]
    forbidden_true = [
        "software_makes_compliance_claim",
        "software_makes_certification_claim",
        "software_makes_sealing_claim",
        "software_makes_approval_claim",
        "software_makes_authentication_claim",
    ]
    if boundary.get("human_review_required") is not True:
        raise WitnessError("professional boundary must require human review")
    for key in forbidden_true:
        if boundary.get(key) is not False:
            raise WitnessError(f"professional boundary overclaim: {key}")


def _validate_content_dictionary_paths(witness: dict[str, Any]) -> None:
    for cd in witness["content_dictionaries"]:
        path = resolve_repo_path(cd["path"])
        if not path.exists():
            raise WitnessError(f"content dictionary path does not exist: {cd['path']}")


def _validate_openmath_symbols(witness: dict[str, Any]) -> None:
    for formula in witness["formulas"]:
        _walk_openmath_symbols(formula["openmath"])
    for binding in witness["constants"]:
        openmath = binding["openmath"]
        if openmath["om_type"] != "OMS" or (openmath["cd"], openmath["name"]) not in ALLOWED_CONSTANTS:
            raise WitnessError(f"unsupported OpenMath constant binding for {binding['id']}")


def _walk_openmath_symbols(node: dict[str, Any]) -> None:
    om_type = node["om_type"]
    if om_type == "OMS":
        symbol = (node["cd"], node["name"])
        if symbol not in ALLOWED_OPERATORS and symbol not in ALLOWED_CONSTANTS:
            raise WitnessError(f"unsupported OpenMath symbol: {symbol[0]}.{symbol[1]}")
    elif om_type == "OMA":
        _walk_openmath_symbols(node["operator"])
        for argument in node["arguments"]:
            _walk_openmath_symbols(argument)
    elif om_type in {"OMV", "OMI", "OMF"}:
        return
    else:
        raise WitnessError(f"unsupported OpenMath node type: {om_type}")


def _quantity_from_binding(binding: dict[str, Any]) -> Quantity:
    quantity = binding["quantity"]
    return Quantity(
        value=_decimal(quantity["decimal"], binding["id"]),
        dimension=_dimension_vector(quantity["dimension"]),
        dimension_id=quantity["dimension"],
        unit=quantity["unit"],
    )


def _decimal(value: str, subject: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise WitnessError(f"invalid decimal for {subject}: {value}") from exc


def _eval_openmath(
    node: dict[str, Any],
    eval_variable: Any,
    values: dict[str, Quantity],
) -> Quantity:
    om_type = node["om_type"]
    if om_type == "OMV":
        return eval_variable(node["name"])
    if om_type in {"OMI", "OMF"}:
        return Quantity(
            value=_decimal(node["decimal"], "literal"),
            dimension={},
            dimension_id="dimensionless",
            unit="1",
        )
    if om_type == "OMS":
        key = _symbol_key(node)
        if key not in values:
            raise WitnessError(f"unbound OpenMath symbol: {key}")
        return values[key]
    if om_type != "OMA":
        raise WitnessError(f"unsupported OpenMath node type: {om_type}")

    operator = node["operator"]
    if operator["om_type"] != "OMS":
        raise WitnessError("OpenMath application operator must be an OMS symbol")
    symbol = (operator["cd"], operator["name"])
    if symbol not in ALLOWED_OPERATORS:
        raise WitnessError(f"unsupported OpenMath operator: {symbol[0]}.{symbol[1]}")

    args = [_eval_openmath(argument, eval_variable, values) for argument in node["arguments"]]
    if symbol == ("arith1", "plus"):
        return _add_or_subtract(args, Decimal(1), "plus")
    if symbol == ("arith1", "minus"):
        if len(args) == 1:
            return Quantity(-args[0].value, args[0].dimension, args[0].dimension_id, args[0].unit)
        return _add_or_subtract([args[0], *args[1:]], Decimal(-1), "minus")
    if symbol == ("arith1", "times"):
        return _multiply(args)
    if symbol == ("arith1", "divide"):
        if len(args) != 2:
            raise WitnessError("arith1.divide requires exactly two arguments")
        return _divide(args[0], args[1])
    if symbol == ("arith1", "power"):
        if len(args) != 2:
            raise WitnessError("arith1.power requires exactly two arguments")
        return _power(args[0], args[1])
    raise WitnessError(f"unsupported OpenMath operator: {symbol[0]}.{symbol[1]}")


def _add_or_subtract(args: list[Quantity], sign: Decimal, operator: str) -> Quantity:
    if len(args) < 2:
        raise WitnessError(f"arith1.{operator} requires at least two arguments")
    first = args[0]
    value = first.value
    for arg in args[1:]:
        if arg.dimension != first.dimension:
            raise WitnessError(f"dimension mismatch in arith1.{operator}")
        if arg.unit != first.unit:
            raise WitnessError(f"unit mismatch in arith1.{operator}: {first.unit} vs {arg.unit}")
        value += sign * arg.value
    return Quantity(value, first.dimension, first.dimension_id, first.unit)


def _multiply(args: list[Quantity]) -> Quantity:
    value = Decimal(1)
    dimension: dict[str, int] = {}
    dimensional_units = [arg.unit for arg in args if arg.dimension]
    for arg in args:
        value *= arg.value
        dimension = _combine_dimensions(dimension, arg.dimension, 1)
    unit = dimensional_units[0] if len(dimensional_units) == 1 else "derived"
    return Quantity(value, dimension, _dimension_name(dimension), unit)


def _divide(left: Quantity, right: Quantity) -> Quantity:
    if right.value == 0:
        raise WitnessError("division by zero in OpenMath witness")
    unit = left.unit if not right.dimension else "derived"
    return Quantity(
        left.value / right.value,
        _combine_dimensions(left.dimension, right.dimension, -1),
        _dimension_name(_combine_dimensions(left.dimension, right.dimension, -1)),
        unit,
    )


def _power(base: Quantity, exponent: Quantity) -> Quantity:
    if exponent.dimension:
        raise WitnessError("arith1.power exponent must be dimensionless")
    if exponent.value != exponent.value.to_integral_value():
        raise WitnessError("arith1.power exponent must be an integer for dimension checking")
    power = int(exponent.value)
    dimension = {name: exp * power for name, exp in base.dimension.items() if exp * power != 0}
    return Quantity(base.value**power, dimension, _dimension_name(dimension), "derived")


def _combine_dimensions(
    left: dict[str, int],
    right: dict[str, int],
    right_sign: int,
) -> dict[str, int]:
    combined = dict(left)
    for name, exponent in right.items():
        combined[name] = combined.get(name, 0) + right_sign * exponent
        if combined[name] == 0:
            del combined[name]
    return combined


def _dimension_vector(dimension_id: str) -> dict[str, int]:
    if dimension_id not in DIMENSIONS:
        raise WitnessError(f"unsupported canonical dimension: {dimension_id}")
    return dict(DIMENSIONS[dimension_id])


def _dimension_name(vector: dict[str, int]) -> str:
    for name, candidate in DIMENSIONS.items():
        if vector == candidate:
            return name
    rendered = ",".join(f"{key}^{value}" for key, value in sorted(vector.items()))
    return f"derived({rendered})"


def _symbol_key(openmath: dict[str, Any]) -> str:
    return f"{openmath['cd']}.{openmath['name']}"


def _compare_outputs(
    witness: dict[str, Any],
    values: dict[str, Quantity],
) -> list[Comparison]:
    result_path = resolve_repo_path(witness["result_export"]["path"])
    result_export = load_json(result_path)
    exported_values = _flatten_result_values(result_export)
    comparisons: list[Comparison] = []
    for output in witness["outputs"]:
        formula_id = output["formula_id"]
        if formula_id not in values:
            raise WitnessError(f"output formula not evaluated: {formula_id}")
        result_id = output["result_id"]
        if result_id not in exported_values:
            raise WitnessError(f"result export does not contain result_id {result_id}")
        witness_quantity = values[formula_id]
        result_value = exported_values[result_id]
        result_decimal = Decimal(str(result_value["magnitude"]))
        if result_value["unit"] != witness_quantity.unit:
            raise WitnessError(
                f"unit mismatch for {result_id}: "
                f"witness={witness_quantity.unit}, result={result_value['unit']}"
            )
        if result_value["dimension"] != witness_quantity.dimension_id:
            raise WitnessError(
                f"dimension mismatch for {result_id}: "
                f"witness={witness_quantity.dimension_id}, result={result_value['dimension']}"
            )
        tolerance = _decimal(output["abs_tolerance_decimal"], output["id"])
        comparison = Comparison(
            output_id=output["id"],
            formula_id=formula_id,
            result_id=result_id,
            witness_value=witness_quantity.value,
            result_value=result_decimal,
            delta=witness_quantity.value - result_decimal,
            tolerance=tolerance,
            unit=witness_quantity.unit,
            dimension=witness_quantity.dimension_id,
        )
        if not comparison.passed:
            raise WitnessError(
                f"OPS result mismatch for {result_id}: "
                f"witness={_format_decimal(comparison.witness_value)}, "
                f"result={_format_decimal(comparison.result_value)}, "
                f"abs_delta={_format_decimal(abs(comparison.delta))}, "
                f"tolerance={_format_decimal(comparison.tolerance)}"
            )
        comparisons.append(comparison)
    return comparisons


def _flatten_result_values(result_export: dict[str, Any]) -> dict[str, dict[str, Any]]:
    flattened: dict[str, dict[str, Any]] = {}
    for result_set in result_export["result_envelope"]["result_sets"]:
        for value in result_set["values"]:
            flattened[value["result_id"]] = value
    return flattened


def render_markdown(witness: dict[str, Any]) -> str:
    evaluation = evaluate_witness(witness)
    display = _display_map(witness)
    lines = [
        f"# Generated Hand-Calc Witness: {witness['witness_id']}",
        "",
        "This Markdown is generated from the machine-readable witness artifact.",
        "Do not edit this file as the authoritative calculation source.",
        "",
        f"- Witness title: {witness['title']}",
        f"- Witness SHA-256 over canonical JSON: `sha256:{evaluation.witness_hash}`",
        f"- Semantic source: {witness['openmath_binding']['semantic_source']}",
        f"- JSON binding: `{witness['openmath_binding']['json_binding']}`",
        f"- MathML rendering: `{witness['openmath_binding']['mathml_rendering']}`",
        "",
        "## Provenance",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    for key, value in witness["provenance"].items():
        lines.append(f"| `{key}` | {value} |")

    lines.extend(
        [
            "",
            "## Inputs",
            "",
            "| ID | Symbol | Value | Unit | Dimension |",
            "|---|---|---:|---|---|",
        ]
    )
    for binding in witness["constants"] + witness["inputs"]:
        quantity = binding["quantity"]
        lines.append(
            f"| `{binding['id']}` | `{binding['display']}` | "
            f"{quantity['decimal']} | `{quantity['unit']}` | `{quantity['dimension']}` |"
        )

    lines.extend(
        [
            "",
            "## Formula Evaluation",
            "",
            "| Formula | OpenMath-derived expression | Evaluated value | Unit | Dimension |",
            "|---|---|---:|---|---|",
        ]
    )
    for formula_id in evaluation.formula_order:
        formula = _formula_by_id(witness, formula_id)
        quantity = evaluation.values[formula_id]
        expression = _render_infix(formula["openmath"], display)
        lines.append(
            f"| `{formula['display']}` | `{formula['display']} = {expression}` | "
            f"{_format_decimal(quantity.value)} | `{quantity.unit}` | `{quantity.dimension_id}` |"
        )

    lines.extend(
        [
            "",
            "## Result Export Comparison",
            "",
            "| Output | OPS result ID | Witness value | OPS value | Abs delta | Tolerance |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for comparison in evaluation.comparisons:
        lines.append(
            f"| `{comparison.output_id}` | `{comparison.result_id}` | "
            f"{_format_decimal(comparison.witness_value)} | "
            f"{_format_decimal(comparison.result_value)} | "
            f"{_format_decimal(abs(comparison.delta))} | "
            f"{_format_decimal(comparison.tolerance)} |"
        )

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This witness is mechanics-only software verification evidence. It does not compare to allowables, classify code stress categories, apply fatigue rules, use SIF/flexibility factors, certify, seal, authenticate, approve, or declare code compliance.",
            "",
        ]
    )
    return "\n".join(lines)


def render_mathml(witness: dict[str, Any]) -> str:
    evaluation = evaluate_witness(witness)
    formulas = {formula["id"]: formula for formula in witness["formulas"]}
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<ops-witness-mathml witness-id="{escape(witness["witness_id"])}" witness-sha256="{evaluation.witness_hash}">',
    ]
    for formula_id in evaluation.formula_order:
        formula = formulas[formula_id]
        lines.extend(
            [
                f'  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block" id="{escape(formula_id)}">',
                "    <semantics>",
                "      <apply>",
                "        <eq/>",
                f"        <ci>{escape(formula['display'])}</ci>",
                _render_mathml_node(formula["openmath"], indent="        "),
                "      </apply>",
                f'      <annotation encoding="application/x-openmath-json">{escape(formula_id)}</annotation>',
                "    </semantics>",
                "  </math>",
            ]
        )
    lines.append("</ops-witness-mathml>")
    lines.append("")
    return "\n".join(lines)


def assert_generated_artifacts_current(witness: dict[str, Any]) -> None:
    markdown_path = resolve_repo_path(witness["generated_artifacts"]["markdown_path"])
    mathml_path = resolve_repo_path(witness["generated_artifacts"]["mathml_path"])
    expected_markdown = render_markdown(witness)
    expected_mathml = render_mathml(witness)
    _assert_file_text(markdown_path, expected_markdown, "generated Markdown")
    _assert_file_text(mathml_path, expected_mathml, "generated MathML")


def _assert_file_text(path: Path, expected: str, label: str) -> None:
    if not path.exists():
        raise WitnessError(f"{label} missing: {path}")
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise WitnessError(f"{label} is stale: {path}")


def write_generated_artifacts(witness: dict[str, Any]) -> None:
    artifacts = {
        resolve_repo_path(witness["generated_artifacts"]["markdown_path"]): render_markdown(witness),
        resolve_repo_path(witness["generated_artifacts"]["mathml_path"]): render_mathml(witness),
    }
    for path, rendered in artifacts.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")


def _display_map(witness: dict[str, Any]) -> dict[str, str]:
    display: dict[str, str] = {"nums1.pi": "pi"}
    for item in witness["constants"] + witness["inputs"] + witness["formulas"]:
        display[item["id"]] = item["display"]
    return display


def _formula_by_id(witness: dict[str, Any], formula_id: str) -> dict[str, Any]:
    for formula in witness["formulas"]:
        if formula["id"] == formula_id:
            return formula
    raise WitnessError(f"unknown formula id: {formula_id}")


def _render_infix(node: dict[str, Any], display: dict[str, str]) -> str:
    om_type = node["om_type"]
    if om_type == "OMV":
        return display.get(node["name"], node["name"])
    if om_type in {"OMI", "OMF"}:
        return node["decimal"]
    if om_type == "OMS":
        return display.get(_symbol_key(node), node["name"])
    if om_type != "OMA":
        raise WitnessError(f"unsupported OpenMath node type for rendering: {om_type}")
    operator = node["operator"]
    symbol = (operator["cd"], operator["name"])
    args = [_render_infix(argument, display) for argument in node["arguments"]]
    if symbol == ("arith1", "plus"):
        return "(" + " + ".join(args) + ")"
    if symbol == ("arith1", "minus"):
        return f"(-{args[0]})" if len(args) == 1 else "(" + " - ".join(args) + ")"
    if symbol == ("arith1", "times"):
        return "(" + " * ".join(args) + ")"
    if symbol == ("arith1", "divide"):
        return f"({args[0]} / {args[1]})"
    if symbol == ("arith1", "power"):
        return f"({args[0]}^{args[1]})"
    raise WitnessError(f"unsupported OpenMath operator for rendering: {symbol}")


def _render_mathml_node(node: dict[str, Any], indent: str) -> str:
    om_type = node["om_type"]
    if om_type == "OMV":
        return f"{indent}<ci>{escape(node['name'])}</ci>"
    if om_type in {"OMI", "OMF"}:
        return f"{indent}<cn>{escape(node['decimal'])}</cn>"
    if om_type == "OMS":
        if (node["cd"], node["name"]) == ("nums1", "pi"):
            return f"{indent}<pi/>"
        return f'{indent}<csymbol cd="{escape(node["cd"])}">{escape(node["name"])}</csymbol>'
    if om_type != "OMA":
        raise WitnessError(f"unsupported OpenMath node type for MathML: {om_type}")
    operator = node["operator"]
    symbol = (operator["cd"], operator["name"])
    operator_tag = {
        ("arith1", "plus"): "plus",
        ("arith1", "minus"): "minus",
        ("arith1", "times"): "times",
        ("arith1", "divide"): "divide",
        ("arith1", "power"): "power",
    }.get(symbol)
    if operator_tag is None:
        raise WitnessError(f"unsupported OpenMath operator for MathML: {symbol}")
    child_indent = indent + "  "
    rendered = [f"{indent}<apply>", f"{child_indent}<{operator_tag}/>"]
    rendered.extend(_render_mathml_node(argument, child_indent) for argument in node["arguments"])
    rendered.append(f"{indent}</apply>")
    return "\n".join(rendered)


def _format_decimal(value: Decimal) -> str:
    if value.is_zero():
        return "0"
    normalized = value.normalize()
    text = format(normalized, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def validated_copy(witness: dict[str, Any]) -> dict[str, Any]:
    return deepcopy(witness)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness", type=Path, default=DEFAULT_WITNESS_PATH)
    parser.add_argument("--write-generated", action="store_true")
    parser.add_argument("--check-generated", action="store_true")
    args = parser.parse_args()

    witness = load_json(args.witness)
    evaluation = evaluate_witness(witness)
    if args.write_generated:
        write_generated_artifacts(witness)
    if args.check_generated:
        assert_generated_artifacts_current(witness)
    print(f"{evaluation.witness_id} sha256:{evaluation.witness_hash}")
    print(f"comparisons passed: {len(evaluation.comparisons)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
