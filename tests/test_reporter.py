import pandas as pd
from src.reporter import build_summary
from src.validator import ValidationResult


def test_build_summary_structure():
    df = pd.DataFrame({
        "id": [1],
        "name": ["A"],
        "email": ["a@x.com"],
        "age": [21],
    })

    validation = ValidationResult(
        is_valid=True,
        errors=[],
        missing_by_column={"id": 0, "name": 0, "email": 0, "age": 0},
        duplicate_row_count=0,
    )

    report = build_summary(df, validation)

    assert report["rows"] == 1
    assert report["columns"] == 4
    assert report["validation_passed"] is True
    assert "missing_by_required_column" in report
