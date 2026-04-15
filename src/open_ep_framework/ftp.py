from .domain import FTPStack

def ftp_rate(stack: FTPStack) -> float:
    return (
        stack.matched_maturity_base
        + stack.tenor_premium
        + stack.liquidity_premium
        + stack.optionality_charge
        + stack.contingent_draw_charge
        + stack.stress_surcharge
        - stack.stable_funding_credit
    )
