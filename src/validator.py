from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import pandas as pd


@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    errors: List[str]
    missing_by_column: Dict[str, int]
    duplicate_row_count: int


def validate_dataframe(
    df: pd.DataFrame,
    required_columns: List[str],
    allow_duplicates: bool = False,
) -> ValidationResult:
    errors: List[str] = []

    # 1) Required columns check
    missing_required = [c for c in required_columns if c not in df.columns]
    if missing_required:
        errors.append(f"Missing required columns: {', '.join(missing_required)}")

    # 2) Missing values per required column (only for columns that exist)
    existing_cols = [c for c in required_columns if c in df.columns]
    missing_by_column = {c: int(df[c].isna().sum()) for c in existing_cols}

    # 3) Duplicate rows
    duplicate_row_count = int(df.duplicated().sum())
    if duplicate_row_count > 0 and not allow_duplicates:
        errors.append(f"Duplicate rows found: {duplicate_row_count}")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        missing_by_column=missing_by_column,
        duplicate_row_count=duplicate_row_count,
    )
