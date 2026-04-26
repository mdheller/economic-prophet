from open_ep_framework.cli import run_relationship_context


def test_relationship_context_output_contains_lineage_and_calculation():
    output = run_relationship_context(
        "examples/synthetic_relationship_runtime.json",
        "examples/object_graph.json",
        "rel-synthetic-001",
    )

    assert "calculation" in output
    assert "relationship_context" in output
    assert output["calculation"]["relationship_id"] == "rel-synthetic-001"
    assert output["relationship_context"]["lineage"]["object_id"] == "rel-synthetic-001"
    assert output["relationship_context"]["lineage"]["object_type"] == "relationship"
    assert output["calculation"]["relationship_required_rate"] > 0
