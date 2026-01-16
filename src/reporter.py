from __future__ import annotations

from pathlib import Path
import json
import pandas as pd

from .validator import ValidationResult


def build_summary(df: pd.DataFrame, validation: ValidationResult) -> dict:
    total_rows = int(len(df))
    total_columns = int(len(df.columns))
    missing_values_total = int(df.isna().sum().sum())

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing_values_total": missing_values_total,
        "duplicate_rows": validation.duplicate_row_count,
        "missing_by_required_column": validation.missing_by_column,
        "validation_passed": validation.is_valid,
        "validation_errors": validation.errors,
    }


def save_report(
    report: dict,
    output_dir: str = "outputs",
    filename: str = "report.json",
) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / filename
    file_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    return file_path
