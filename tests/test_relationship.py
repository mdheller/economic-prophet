from open_ep_framework.relationship import RelationshipEffects, relationship_required_rate


def test_relationship_required_rate_not_blind_sum():
    transactions = [
        {
            "balance": 6_000_000,
            "break_even_rate": 0.041,
            "capital": 390_000,
            "expected_loss": 36_000,
            "utilization": 0.82,
            "collateral_set_id": "collateral-a",
        },
        {
            "balance": 3_000_000,
            "break_even_rate": 0.047,
            "capital": 240_000,
            "expected_loss": 22_000,
            "utilization": 0.41,
            "collateral_set_id": "collateral-a",
        },
        {
            "balance": 1_000_000,
            "break_even_rate": 0.018,
            "capital": 40_000,
            "expected_loss": 2_500,
            "utilization": 0.25,
            "collateral_set_id": "",
        },
    ]
    effects = RelationshipEffects(
        capital_diversification_factor=0.18,
        collateral_overlap_factor=0.35,
        utilization_interaction_bps=22.0,
        franchise_credit_bps=18.0,
        capital_hurdle_rate=0.12,
    )
    result = relationship_required_rate(transactions, effects)

    assert result["total_balance"] == 10_000_000
    assert result["weighted_instrument_break_even_rate"] > 0
    assert result["capital_diversification_credit"] > 0
    assert result["collateral_overlap_charge"] > 0
    assert result["relationship_required_rate"] != result["weighted_instrument_break_even_rate"]
    assert 0 < result["relationship_required_rate"] < 0.10
