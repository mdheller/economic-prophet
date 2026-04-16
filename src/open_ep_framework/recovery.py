from .domain import RecoverySurfaceInputs

_MACRO = {"benign": 0.03, "base": 0.0, "stressed": -0.06, "crisis": -0.12}
_LIQ = {"normal": 0.0, "tight": -0.03, "frozen": -0.08}

def planning_recovery(surface: RecoverySurfaceInputs) -> float:
    base = 0.15 + 0.35 * surface.seniority + 0.25 * surface.collateral_quality + 0.15 * surface.jurisdiction_score
    base += _MACRO.get(surface.macro_regime, 0.0) + _LIQ.get(surface.liquidity_regime, 0.0)
    horizon_drag = min(surface.workout_horizon_days / 3650.0, 0.10)
    return max(0.05, min(0.95, base - horizon_drag))

def market_implied_recovery(surface: RecoverySurfaceInputs) -> float:
    pr = planning_recovery(surface)
    stress_penalty = 0.02 if surface.macro_regime in {"stressed", "crisis"} else 0.0
    liq_penalty = 0.02 if surface.liquidity_regime in {"tight", "frozen"} else 0.0
    return max(0.02, pr - stress_penalty - liq_penalty)

def recovery_wedge(surface: RecoverySurfaceInputs) -> float:
    return market_implied_recovery(surface) - planning_recovery(surface)
