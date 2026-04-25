import argparse
import json
from pathlib import Path

from .audit import write_audit_pack
from .breakeven import economic_profit_for_rate, solve_break_even_rate
from .capital import capital_charge
from .domain import CapitalStack, ExpectedLossInputs, FTPStack, PricingContext, RecoverySurfaceInputs
from .expected_loss import expected_loss_amount
from .ftp import ftp_rate
from .object_graph import ObjectGraph, lineage_aware_output
from .recovery import market_implied_recovery, planning_recovery, recovery_wedge
from .relationship import RelationshipEffects, relationship_required_rate
from .validation import validate_json_file


def load_context(path: str):
    data = json.loads(Path(path).read_text())
    ftp_stack = FTPStack(**data["ftp_stack"])
    el = ExpectedLossInputs(**data["expected_loss"])
    recovery = RecoverySurfaceInputs(**data["recovery_surface"])
    capital = CapitalStack(**data["capital_stack"])
    context = PricingContext(
        balance=data["balance"],
        fee_income=data.get("fee_income", 0.0),
        expense=data.get("expense", 0.0),
        tax_rate=data.get("tax_rate", 0.0),
        funding_credits=data.get("funding_credits", 0.0),
        horizon_years=float(data.get("horizon_years", 1.0)),
    )
    return data, context, ftp_stack, el, recovery, capital


def run_example(path: str) -> dict:
    validate_json_file(path, "schemas/synthetic_run.schema.json")
    data, context, ftp_stack, el, recovery, capital = load_context(path)
    hurdle_rate = float(data.get("hurdle_rate", 0.12))
    break_even_rate = solve_break_even_rate(context, ftp_stack, el, capital, recovery, hurdle_rate)
    ep_at_break_even = economic_profit_for_rate(break_even_rate, context, ftp_stack, el, capital, recovery, hurdle_rate)

    return {
        "ftp_rate": ftp_rate(ftp_stack),
        "expected_loss": expected_loss_amount(el),
        "planning_recovery": planning_recovery(recovery),
        "market_implied_recovery": market_implied_recovery(recovery),
        "recovery_wedge": recovery_wedge(recovery),
        "capital_charge": capital_charge(capital, hurdle_rate),
        "break_even_rate": break_even_rate,
        "economic_profit_at_break_even": ep_at_break_even,
    }


def _relationship_items_to_transactions(items: list[dict]) -> list[dict]:
    return [
        {
            "transaction_id": item["id"],
            "balance": item["balance"],
            "break_even_rate": item["rate"],
            "capital": item["capital"],
            "expected_loss": item["loss"],
            "utilization": item["util"],
            "collateral_set_id": item["collateral"],
        }
        for item in items
    ]


def run_relationship(path: str) -> dict:
    validate_json_file(path, "schemas/relationship.schema.json")
    data = json.loads(Path(path).read_text())
    effects = RelationshipEffects(**data["effects"])
    txs = _relationship_items_to_transactions(data["items"])
    outputs = relationship_required_rate(txs, effects)
    outputs["relationship_id"] = data["relationship_id"]
    return outputs


def run_object_graph(path: str, object_id: str) -> dict:
    records = json.loads(Path(path).read_text())
    graph = ObjectGraph.from_dicts(records)
    return lineage_aware_output(object_id, graph, {"economic_profit": 0.0})


def main():
    p = argparse.ArgumentParser(prog="oepf")
    p.add_argument("--mode", choices=["instrument", "relationship", "object-graph"], default="instrument")
    p.add_argument("--example", default="examples/synthetic_run.json")
    p.add_argument("--audit", default="audit.json")
    p.add_argument("--object-id", default="instrument-loan-001")
    args = p.parse_args()

    if args.mode == "relationship":
        outputs = run_relationship(args.example)
    elif args.mode == "object-graph":
        outputs = run_object_graph(args.example, args.object_id)
    else:
        outputs = run_example(args.example)

    inputs = json.loads(Path(args.example).read_text())
    run_id = inputs.get("run_id") if isinstance(inputs, dict) else None
    run_id = run_id or (inputs.get("relationship_id") if isinstance(inputs, dict) else None) or args.object_id
    scenario = inputs.get("scenario", "base") if isinstance(inputs, dict) else "base"
    write_audit_pack(args.audit, run_id, scenario, "0.1.0", {"input": inputs}, outputs)
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
