from open_ep_framework.heller_mesh import run_heller_mesh
from open_ep_framework.validation import validate_json_file


def test_heller_mesh_measurement_fixture_validates():
    assert validate_json_file(
        "examples/heller_mesh_measurement.json",
        "schemas/heller_mesh_measurement.schema.json",
    )


def test_heller_mesh_summary_metrics_are_deterministic():
    output = run_heller_mesh("examples/heller_mesh_measurement.json")
    summary = output["summary"]

    assert summary["run_id"] == "heller-mesh-synthetic-001"
    assert summary["scenario"] == "packaging-education-release"
    assert summary["sphere_count"] == 5
    assert summary["known_canonical_sphere_count"] == 5
    assert summary["unknown_spheres"] == []
    assert summary["edge_count"] == 2
    assert summary["triparty_face_count"] == 1
    assert summary["total_credit_exposure"] == 1.5
    assert summary["total_required_collateral"] == 0.32
    assert abs(summary["computed_reserve_adequacy"] - 38.75) < 1e-9
    assert abs(summary["computed_credit_utilization"] - 0.09375) < 1e-9
    assert abs(summary["computed_gross_to_net_compression"] - 0.8) < 1e-9
    assert abs(summary["computed_reserve_adequacy"] - summary["reported_reserve_adequacy"]) < 1e-9
    assert abs(summary["computed_credit_utilization"] - summary["reported_credit_utilization"]) < 1e-9
    assert abs(summary["computed_gross_to_net_compression"] - summary["reported_gross_to_net_compression"]) < 1e-9
