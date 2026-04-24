from open_ep_framework.domain import FTPStack, ExpectedLossInputs, RecoverySurfaceInputs, CapitalStack
from open_ep_framework.ftp import ftp_rate
from open_ep_framework.expected_loss import expected_loss_amount
from open_ep_framework.recovery import planning_recovery, market_implied_recovery, recovery_wedge
from open_ep_framework.capital import capital_charge


def test_reference_engine_smoke():
    ftp = FTPStack(280, 35, 22, 18, 12, 20, 10, 5)
    assert round(ftp_rate(ftp), 4) == 0.0372

    el = ExpectedLossInputs(pd=0.012, lgd=0.45, ead=10_000_000)
    assert expected_loss_amount(el) == 54_000

    recovery = RecoverySurfaceInputs(
        seniority=0.7,
        collateral_quality=0.6,
        jurisdiction_score=0.8,
        macro_regime="base",
        liquidity_regime="normal",
        workout_horizon_days=540,
        market_state_price=0.4,
    )
    assert 0 <= planning_recovery(recovery) <= 0.95
    assert 0 <= market_implied_recovery(recovery) <= 0.95
    assert recovery_wedge(recovery) <= 0

    capital = CapitalStack(total=650_000, credit=420_000, market=90_000, operational=80_000, business=60_000)
    assert capital_charge(capital, 0.12) == 78_000
