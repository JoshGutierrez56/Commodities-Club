import numpy as np

from run_signal_demo import (
    build_lagged_weights,
    generate_synthetic_panel,
    run_backtest,
)


def test_signal_demo_is_deterministic_and_uses_lagged_inputs():
    returns, carry = generate_synthetic_panel(periods=80, seed=7)
    again_returns, again_carry = generate_synthetic_panel(periods=80, seed=7)
    assert returns.equals(again_returns)
    assert carry.equals(again_carry)

    original = build_lagged_weights(returns, carry)
    changed = returns.copy()
    changed.iloc[40] += 5.0
    perturbed = build_lagged_weights(changed, carry)

    # A return shock at t cannot alter weights applied at t.
    assert np.allclose(original.iloc[40], perturbed.iloc[40])


def test_backtest_includes_costs_and_disclosed_claim_limit():
    returns, carry = generate_synthetic_panel(periods=80, seed=11)
    result, weights, summary = run_backtest(returns, carry, transaction_cost_bps=10)
    assert not result.empty
    assert (result["transaction_cost"] >= 0).all()
    assert np.allclose(weights.abs().sum(axis=1), 1.0)
    assert summary["data_mode"] == "synthetic"
    assert "no historical commodity alpha claim" in summary["claim_limit"]
