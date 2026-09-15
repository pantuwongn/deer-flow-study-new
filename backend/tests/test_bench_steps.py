"""Tests for deerflow.bench.steps."""

from datetime import date

from deerflow.bench.steps import parse_boundary


def test_parse_boundary_returns_date_object() -> None:
    result = parse_boundary("2026-04-27")
    assert result == date(2026, 4, 27)
    assert isinstance(result, date)
