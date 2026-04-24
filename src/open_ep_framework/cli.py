import json
import argparse
from pathlib import Path

from .domain import FTPStack, ExpectedLossInputs, RecoverySurfaceInputs, CapitalStack, PricingContext
from .ftp import ftp_rate
from .expected_loss import expected_loss_amount
from .recovery import planning_recovery, market_implied_recovery, recovery_wedge
from .capital import capital_charge
from .audit import write_audit_pack


def run_example(path: str) -> dict:
    data = json.loads(Path(path).read_text())
    ftp_stack = FTPStack(**data["ftp_stack"])
    el = ExpectedLossInputs(**data["expected_loss"])
    recovery = RecoverySurfaceInputs(**data["recovery_surface"])
    capital = CapitalStack(**data["capital_stack"])
    ctx = PricingContext(
        balance=data["balance"],
        fee_income=data.get("fee_income", 0.0),
        expense=data.get("expense", 0.0),
        tax_rate=data.get("tax_rate", 0.0),
        funding_credits=data.get("funding_credits", 0.0),
        horizon_years=float(data.get("horizon_years", 1.0)),
    )

    ftp = ftp_rate(ftp_stack)
    el_amt = expected_loss_amount(el)
    rr_p = planning_recovery(recovery)
    rr_q = market_implied_recovery(recovery)
    wedge = recovery_wedge(recovery)
    cap = capital_charge(capital, float(data.get("hurdle_rate", 0.12)))

    # NOTE: The full zero-EP pricing solver is defined in docs/product_spec.md.
    # The reference implementation will land in a follow-up PR to keep the repo
    # aligned with platform policy and to ensure proper governance in code.
    outputs = {
        "ftp_rate": ftp,
        "expected_loss": el_amt,
        "planning_recovery": rr_p,
        "market_implied_recovery": rr_q,
        "recovery_wedge": wedge,
        "capital_charge": cap,
    }
    return outputs


def main():
    p = argparse.ArgumentParser(prog="oepf")
    p.add_argument("--example", default="examples/synthetic_run.json")
    p.add_argument("--audit", default="audit.json")
    args = p.parse_args()

    outputs = run_example(args.example)
    inputs = json.loads(Path(args.example).read_text())
    write_audit_pack(args.audit, inputs.get("run_id", "run"), inputs.get("scenario", "base"), "0.1.0", inputs, outputs)
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
