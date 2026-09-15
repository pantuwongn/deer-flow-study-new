"""Tests for ``deerflow.bench.steps``."""

from __future__ import annotations

from datetime import date

from deerflow.bench.steps import apply_boundary


def test_apply_boundary_handles_undated_orders() -> None:
    orders = [
        {"id": "A-1001", "placed": "2026-08-02", "total": 240},
        {"id": "A-1002", "placed": "2026-08-15", "total": 90},
        {"id": "A-1009", "placed": None, "total": 0},
        {"id": "A-1010", "total": 10},
    ]
    result = apply_boundary(orders, date(2026, 8, 10))
    assert [o["id"] for o in result] == ["A-1001"]

    result_none = apply_boundary(orders, None)
    assert [o["id"] for o in result_none] == ["A-1001", "A-1002"]
