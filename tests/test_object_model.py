from open_ep_framework.audit import write_audit_pack
from open_ep_framework.validation import validate_json_file


def test_canonical_object_schema_validates():
    assert validate_json_file("examples/canonical_object.json", "schemas/canonical_object.schema.json")


def test_audit_record_schema_validates(tmp_path):
    audit_path = tmp_path / "audit.json"
    write_audit_pack(
        str(audit_path),
        run_id="schema-test",
        scenario="base",
        framework_version="0.1.0",
        inputs={"object_id": "instrument-loan-001"},
        outputs={"economic_profit": 0.0},
    )
    assert validate_json_file(str(audit_path), "schemas/audit_record.schema.json")
