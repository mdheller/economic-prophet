from open_ep_framework.cli import run_object_context
from open_ep_framework.product_objects import (
    build_instrument_context,
    load_account,
    load_collateral_set,
    load_funding_source,
    load_hedge_set,
    load_instrument,
    load_transaction_event,
)


class Args:
    graph = "examples/object_graph.json"
    object_id = "instrument-loan-001"
    account = "examples/account.json"
    instrument = "examples/instrument.json"
    event = "examples/transaction_event.json"
    collateral = "examples/collateral_set.json"
    funding = "examples/funding_source.json"
    hedge = "examples/hedge_set.json"


def test_product_object_loaders():
    account = load_account("examples/account.json")
    instrument = load_instrument("examples/instrument.json")
    event = load_transaction_event("examples/transaction_event.json")
    collateral = load_collateral_set("examples/collateral_set.json")
    funding = load_funding_source("examples/funding_source.json")
    hedge = load_hedge_set("examples/hedge_set.json")

    assert account.account_id == "account-credit-001"
    assert instrument.instrument_id == "loan-001"
    assert event.event_id == "event-draw-001"
    assert collateral.collateral_set_id == "collateral-a"
    assert funding.funding_source_id == "ftp-usd-commercial-base"
    assert hedge.hedge_set_id == "hedge-set-ir-001"


def test_build_instrument_context_join():
    context = build_instrument_context(
        graph_path="examples/object_graph.json",
        graph_object_id="instrument-loan-001",
        account_path="examples/account.json",
        instrument_path="examples/instrument.json",
        transaction_event_path="examples/transaction_event.json",
        collateral_path="examples/collateral_set.json",
        funding_path="examples/funding_source.json",
        hedge_path="examples/hedge_set.json",
    )

    assert context["lineage"]["object_id"] == "instrument-loan-001"
    assert context["account"]["account_id"] == "account-credit-001"
    assert context["instrument"]["instrument_id"] == "loan-001"
    assert context["transaction_event"]["event_id"] == "event-draw-001"
    assert context["collateral_set"]["collateral_set_id"] == "collateral-a"
    assert context["funding_source"]["funding_source_id"] == "ftp-usd-commercial-base"
    assert context["hedge_set"]["hedge_set_id"] == "hedge-set-ir-001"


def test_object_context_cli_mode():
    context = run_object_context(Args())
    assert context["lineage"]["object_id"] == "instrument-loan-001"
    assert context["transaction_event"]["event_id"] == "event-draw-001"
