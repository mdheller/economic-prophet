from open_ep_framework.cli import run_instrument_context


class Args:
    example = "examples/synthetic_run.json"
    graph = "examples/object_graph.json"
    object_id = "instrument-loan-001"
    account = "examples/account.json"
    instrument = "examples/instrument.json"
    event = "examples/transaction_event.json"
    collateral = "examples/collateral_set.json"
    funding = "examples/funding_source.json"
    hedge = "examples/hedge_set.json"


def test_instrument_context_output_contains_calculation_and_context():
    output = run_instrument_context(Args())

    assert "calculation" in output
    assert "object_context" in output
    assert output["calculation"]["break_even_rate"] > 0
    assert abs(output["calculation"]["economic_profit_at_break_even"]) < 1e-3
    assert output["object_context"]["lineage"]["object_id"] == "instrument-loan-001"
    assert output["object_context"]["account"]["account_id"] == "account-credit-001"
    assert output["object_context"]["instrument"]["instrument_id"] == "loan-001"
    assert output["object_context"]["transaction_event"]["event_id"] == "event-draw-001"
    assert output["object_context"]["collateral_set"]["collateral_set_id"] == "collateral-a"
    assert output["object_context"]["funding_source"]["funding_source_id"] == "ftp-usd-commercial-base"
    assert output["object_context"]["hedge_set"]["hedge_set_id"] == "hedge-set-ir-001"
