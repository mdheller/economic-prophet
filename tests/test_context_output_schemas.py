from open_ep_framework.cli import run_instrument_context, run_relationship_context
from open_ep_framework.validation import validate_instance
import json
from pathlib import Path


class InstrumentArgs:
    example = "examples/synthetic_run.json"
    graph = "examples/object_graph.json"
    object_id = "instrument-loan-001"
    account = "examples/account.json"
    instrument = "examples/instrument.json"
    event = "examples/transaction_event.json"
    collateral = "examples/collateral_set.json"
    funding = "examples/funding_source.json"
    hedge = "examples/hedge_set.json"


def _schema(path):
    return json.loads(Path(path).read_text())


def test_instrument_context_output_schema():
    output = run_instrument_context(InstrumentArgs())
    assert validate_instance(output, _schema("schemas/instrument_context_output.schema.json"))


def test_relationship_context_output_schema():
    output = run_relationship_context(
        "examples/synthetic_relationship_runtime.json",
        "examples/object_graph.json",
        "rel-synthetic-001",
    )
    assert validate_instance(output, _schema("schemas/relationship_context_output.schema.json"))
