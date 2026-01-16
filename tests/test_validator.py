import pandas as pd
from src.validator import validate_dataframe


def test_missing_required_columns_fails():
    df = pd.DataFrame({"id": [1], "name": ["A"]})
    result = validate_dataframe(df, required_columns=["id", "name", "email"], allow_duplicates=True)
    assert result.is_valid is False
    assert any("Missing required columns" in e for e in result.errors)


def test_duplicates_fail_when_not_allowed():
    df = pd.DataFrame({"id": [1, 1], "name": ["A", "A"], "email": ["a@x.com", "a@x.com"]})
    result = validate_dataframe(df, required_columns=["id", "name", "email"], allow_duplicates=False)
    assert result.is_valid is False
    assert "Duplicate rows found" in " ".join(result.errors)


def test_missing_counts_present():
    df = pd.DataFrame({"id": [1, 2], "name": ["A", None], "email": ["a@x.com", None]})
    result = validate_dataframe(df, required_columns=["id", "name", "email"], allow_duplicates=True)
    assert result.missing_by_column["name"] == 1
    assert result.missing_by_column["email"] == 1
