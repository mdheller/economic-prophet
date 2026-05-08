import json
from pathlib import Path

import pytest

from open_ep_framework.uvmc import (
    adjusted_hurdle_rate,
    discount_factors,
    knowledge_geometric,
    knowledge_strict,
    npv_from_ep,
    reconcile_ep_components,
    weighted_inner_product,
    weights_sum_to_one,
)


def test_uvmc_schema_files_are_parseable_json():
    schema_dir = Path(__file__).resolve().parents[1] / "schemas"
    for schema_name in [
        "uvmc_measurement_context.schema.json",
        "uvmc_knowledge_quality.schema.json",
        "uvmc_dimension.schema.json",
        "uvmc_tensor_mapping.schema.json",
        "uvmc_calculation_receipt.schema.json",
    ]:
        payload = json.loads((schema_dir / schema_name).read_text())
        assert payload["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert payload["type"] == "object"
        assert payload["required"]


def test_knowledge_scores_are_bounded_and_weighted():
    assert knowledge_strict(0.8, 0.9, 0.75, 0.5) == pytest.approx(0.27)
    components = {"coverage": 0.8, "quality": 0.9, "stability": 0.75, "provenance": 0.5}
    weights = {"coverage": 0.25, "quality": 0.25, "stability": 0.25, "provenance": 0.25}
    assert 0.0 <= knowledge_geometric(components, weights) <= 1.0
    with pytest.raises(ValueError):
        knowledge_strict(1.2, 0.9, 0.75, 0.5)


def test_adjusted_hurdle_rate_is_sign_safe():
    assert adjusted_hurdle_rate(0.08, 0.025, 0.015, 0.01, 0.005, 0.01) == pytest.approx(0.11)
    with pytest.raises(ValueError):
        adjusted_hurdle_rate(0.08, 0.025, 0.015, 0.03, 0.005, 0.01)


def test_period_safe_discount_factors_and_npv():
    rates = [0.10, 0.20, 0.05]
    factors = discount_factors(rates)
    assert factors == pytest.approx([1 / 1.10, 1 / (1.10 * 1.20), 1 / (1.10 * 1.20 * 1.05)])
    assert npv_from_ep([100.0, 100.0, 100.0], rates) == pytest.approx(sum(100.0 * f for f in factors))


def test_metric_and_reconciliation_invariants():
    assert weights_sum_to_one([0.5, 0.25, 0.25])
    assert weighted_inner_product([1, 0, 1], [1, 1, 0], [0.5, 0.25, 0.25]) == pytest.approx(0.5)
    components = {
        "revenue": 120.0,
        "expected_loss": 10.0,
        "expense": 15.0,
        "funding_costs": 12.0,
        "funding_credits": 3.0,
        "taxes": 8.0,
        "capital_charge": 20.0,
    }
    assert reconcile_ep_components(components) == pytest.approx(58.0)
