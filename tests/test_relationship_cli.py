from open_ep_framework.cli import run_relationship
from open_ep_framework.validation import validate_json_file


def test_relationship_runtime_input_validates():
    assert validate_json_file("examples/synthetic_relationship_runtime.json", "schemas/relationship.schema.json")


def test_relationship_cli_output_contract():
    outputs = run_relationship("examples/synthetic_relationship_runtime.json")
    required = {
        "relationship_id",
        "total_balance",
        "weighted_instrument_break_even_rate",
        "weighted_utilization",
        "gross_capital",
        "capital_diversification_credit",
        "collateral_overlap_share",
        "collateral_overlap_charge",
        "utilization_interaction_charge",
        "franchise_credit",
        "relationship_required_rate",
    }
    assert required.issubset(outputs.keys())
    assert outputs["relationship_id"] == "rel-synthetic-001"
    assert outputs["total_balance"] == 10_000_000
    assert outputs["relationship_required_rate"] != outputs["weighted_instrument_break_even_rate"]
    assert 0 < outputs["relationship_required_rate"] < 0.10
