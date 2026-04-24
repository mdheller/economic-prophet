from open_ep_framework.breakeven import economic_profit_for_rate, solve_break_even_rate
from open_ep_framework.domain import CapitalStack, ExpectedLossInputs, FTPStack, PricingContext, RecoverySurfaceInputs


def test_break_even_solver_returns_zero_ep_rate():
    context = PricingContext(
        balance=10_000_000,
        fee_income=12_500,
        expense=18_000,
        tax_rate=0.24,
        funding_credits=0.0,
        horizon_years=1.0,
    )
    ftp_stack = FTPStack(280, 35, 22, 18, 12, 20, 10, 5)
    expected_loss = ExpectedLossInputs(pd=0.012, lgd=0.45, ead=10_000_000)
    recovery = RecoverySurfaceInputs(0.7, 0.6, 0.8, "base", "normal", 540, 0.4)
    capital = CapitalStack(650_000, 420_000, 90_000, 80_000, 60_000)

    rate = solve_break_even_rate(context, ftp_stack, expected_loss, capital, recovery, 0.12)
    ep = economic_profit_for_rate(rate, context, ftp_stack, expected_loss, capital, recovery, 0.12)

    assert 0.0 <= rate <= 0.50
    assert abs(ep) < 1e-3
