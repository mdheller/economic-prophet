import pytest

from open_ep_framework.object_graph import ObjectGraph, ObjectGraphError


def test_object_graph_runtime_smoke():
    records = [
        {"object_id": "root", "object_type": "legal_entity", "as_of": "2026-04-24", "source_system": "test", "cadence": "close"},
        {"object_id": "child", "parent_id": "root", "object_type": "instrument", "as_of": "2026-04-24", "source_system": "test", "cadence": "daily"}
    ]
    graph = ObjectGraph.from_dicts(records)
    data = graph.lineage("child")
    assert data["object_id"] == "child"
    assert data["parent_chain"] == ["root"]


def test_validated_object_graph_loader():
    graph = ObjectGraph.from_json_file("examples/object_graph.json", validate=True)
    data = graph.lineage("instrument-loan-001")
    assert data["relationship_id"] == "rel-synthetic-001"


def test_object_graph_loader_rejects_non_list(tmp_path):
    path = tmp_path / "bad_graph.json"
    path.write_text("{}")
    with pytest.raises(ObjectGraphError):
        ObjectGraph.from_json_file(str(path), validate=True)
