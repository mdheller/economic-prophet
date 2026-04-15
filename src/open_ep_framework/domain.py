from dataclasses import dataclass

@dataclass
class FTPStack:
    matched_maturity_base: float
    tenor_premium: float
    liquidity_premium: float
    optionality_charge: float
    contingent_draw_charge: float
    stress_surcharge: float
    stable_funding_credit: float = 0.0

@dataclass
class ExpectedLossInputs:
    pd: float
    lgd: float
    ead: float

@dataclass
class RecoverySurfaceInputs:
    seniority: float
    collateral_quality: float
    jurisdiction_score: float
    macro_regime: str = "base"
    liquidity_regime: str = "normal"
    workout_horizon_days: int = 365

@dataclass
class CapitalStack:
    credit: float
    market: float
    operational: float
    business: float
    other: float = 0.0

@dataclass
class PricingContext:
    balance: float
    fee_income: float
    expense: float
    tax_rate: float
    funding_credits: float
    hurdle_rate: float
