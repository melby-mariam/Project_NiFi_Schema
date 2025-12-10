from dataclasses import dataclass
from typing import List, Any
import pandas as pd
from .md_parser import SchemaField


@dataclass
class ValidationResult:
    record_number: int
    field_name: str
    schema_expected: str
    actual_value: Any
    status: str  # "PASS" or "FAIL"
    reason: str  # empty or explanation


def _build_schema_expected(field: SchemaField) -> str:
    """
    Create a human-readable description of what the schema expects for a field.
    """
    parts = []
    if field.data_type:
        parts.append(f"type={field.data_type}")
    if field.max_length is not None:
        parts.append(f"max_length={field.max_length}")
    if field.required is not None:
        parts.append("required" if field.required else "optional")
    if field.rules:
        parts.append(f"rules={field.rules}")
    return "; ".join(parts)


def validate_dataframe(df: pd.DataFrame, schema_fields: List[SchemaField]) -> List[ValidationResult]:
    """
    Validate the DataFrame against the schema fields.

    SKELETON:
    ---------
    For now:
      - Checks only if field exists in DataFrame.
      - Checks if required fields are non-empty.
    Later:
      - Add strict type, length, format, allowed values validations.
    """
    results: List[ValidationResult] = []
    total_records = len(df)

    for field in schema_fields:
        expected_desc = _build_schema_expected(field)
        col_name = field.name

        if col_name not in df.columns:
            # Field completely missing from file
            for i in range(total_records):
                results.append(
                    ValidationResult(
                        record_number=i + 1,
                        field_name=col_name,
                        schema_expected=expected_desc,
                        actual_value=None,
                        status="FAIL",
                        reason="Field missing in file",
                    )
                )
            continue

        # Validate row by row
        for idx, value in df[col_name].items():
            record_number = idx + 1
            value_str = None if pd.isna(value) else str(value)

            # Example basic required check
            if field.required and (value_str is None or value_str.strip() == ""):
                results.append(
                    ValidationResult(
                        record_number=record_number,
                        field_name=col_name,
                        schema_expected=expected_desc,
                        actual_value=value_str,
                        status="FAIL",
                        reason="Missing required field value",
                    )
                )
            else:
                # For now, assume pass if basic required check passes.
                results.append(
                    ValidationResult(
                        record_number=record_number,
                        field_name=col_name,
                        schema_expected=expected_desc,
                        actual_value=value_str,
                        status="PASS",
                        reason="",
                    )
                )

    return results
