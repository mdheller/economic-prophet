from open_ep_framework.validation import validate_json_file


def test_account_schema_validates():
    assert validate_json_file("examples/account.json", "schemas/account.schema.json")


def test_instrument_schema_validates():
    assert validate_json_file("examples/instrument.json", "schemas/instrument.schema.json")


def test_transaction_event_schema_validates():
    assert validate_json_file("examples/transaction_event.json", "schemas/transaction_event.schema.json")


def test_collateral_set_schema_validates():
    assert validate_json_file("examples/collateral_set.json", "schemas/collateral_set.schema.json")


def test_funding_source_schema_validates():
    assert validate_json_file("examples/funding_source.json", "schemas/funding_source.schema.json")


def test_hedge_set_schema_validates():
    assert validate_json_file("examples/hedge_set.json", "schemas/hedge_set.schema.json")
