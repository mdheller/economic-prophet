from open_ep_framework.cli import run_object_graph
from open_ep_framework.validation import validate_json_file


def test_lineage_ep_output_fixture_validates():
    assert validate_json_file("examples/lineage_ep_output.json", "schemas/lineage_ep_output.schema.json")


def test_object_graph_cli_output_validates(tmp_path):
    output = run_object_graph("examples/object_graph.json", "instrument-loan-001")
    assert output["lineage"]["object_id"] == "instrument-loan-001"
    assert output["components"]["economic_profit"] == 0.0
