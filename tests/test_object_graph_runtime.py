from open_ep_framework.object_graph import ObjectGraph


def test_object_graph_runtime_smoke():
    records = [
        {"object_id": "root", "object_type": "legal_entity", "as_of": "2026-04-24", "source_system": "test", "cadence": "close"},
        {"object_id": "child", "parent_id": "root", "object_type": "instrument", "as_of": "2026-04-24", "source_system": "test", "cadence": "daily"}
    ]
    graph = ObjectGraph.from_dicts(records)
    data = graph.lineage("child")
    assert data["object_id"] == "child"
    assert data["parent_chain"] == ["root"]
