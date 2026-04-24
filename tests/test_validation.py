import json

from open_ep_framework.audit import stable_hash
from open_ep_framework.cli import run_example
from open_ep_framework.validation import validate_json_file


def test_synthetic_runtime_input_validates():
    assert validate_json_file("examples/synthetic_run.json", "schemas/synthetic_run.schema.json")


def test_audit_hash_is_deterministic():
    obj_a = {"b": 2, "a": 1}
    obj_b = {"a": 1, "b": 2}
    assert stable_hash(obj_a) == stable_hash(obj_b)


def test_cli_runtime_outputs_required_fields():
    outputs = run_example("examples/synthetic_run.json")
    required = {
        "ftp_rate",
        "expected_loss",
        "planning_recovery",
        "market_implied_recovery",
        "recovery_wedge",
        "capital_charge",
        "break_even_rate",
        "economic_profit_at_break_even",
    }
    assert required.issubset(outputs.keys())
    assert abs(outputs["economic_profit_at_break_even"]) < 1e-3
