"""Deterministic offline carry/trend signal demo for the Commodities Club.

This is execution evidence for the signal pipeline, not a historical market
backtest. The synthetic data and fixed seed are disclosed in every artifact.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


COMMODITIES = ["WTI", "NATGAS", "GOLD", "SILVER", "CORN", "WHEAT", "COPPER", "COFFEE"]


def generate_synthetic_panel(
    start: str = "2005-01-31",
    periods: int = 240,
    seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return monthly synthetic commodity returns and observable carry scores."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start, periods=periods, freq="ME")
    n_assets = len(COMMODITIES)
    carry = np.zeros((periods, n_assets))
    returns = np.zeros((periods, n_assets))

    for t in range(1, periods):
        carry[t] = 0.88 * carry[t - 1] + rng.normal(0, 0.45, n_assets)
        returns[t] = (
            0.12 * returns[t - 1]
            + 0.004 * carry[t - 1]
            + rng.normal(0.003, 0.07, n_assets)
        )

    return (
        pd.DataFrame(returns, index=dates, columns=COMMODITIES),
        pd.DataFrame(carry, index=dates, columns=COMMODITIES),
    )


def _cross_sectional_zscore(frame: pd.DataFrame) -> pd.DataFrame:
    centered = frame.sub(frame.mean(axis=1), axis=0)
    scale = frame.std(axis=1, ddof=0).replace(0, np.nan)
    return centered.div(scale, axis=0).fillna(0.0)


def build_lagged_weights(
    returns: pd.DataFrame,
    carry: pd.DataFrame,
    momentum_months: int = 12,
) -> pd.DataFrame:
    """Build unit-gross carry/trend weights using only information through t-1."""
    momentum = (1.0 + returns).rolling(momentum_months).apply(np.prod, raw=True) - 1.0
    momentum_signal = _cross_sectional_zscore(momentum.shift(1))
    carry_signal = _cross_sectional_zscore(carry.shift(1))
    combined = 0.5 * momentum_signal + 0.5 * carry_signal
    gross = combined.abs().sum(axis=1).replace(0, np.nan)
    return combined.div(gross, axis=0).fillna(0.0)


def run_backtest(
    returns: pd.DataFrame,
    carry: pd.DataFrame,
    transaction_cost_bps: float = 10.0,
) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Backtest lagged weights against an equal-weight commodity benchmark."""
    weights = build_lagged_weights(returns, carry)
    turnover = weights.diff().abs().sum(axis=1).fillna(0.0)
    costs = turnover * transaction_cost_bps / 10_000.0
    strategy = (weights * returns).sum(axis=1) - costs
    benchmark = returns.mean(axis=1)
    result = pd.DataFrame({
        "strategy_return": strategy,
        "benchmark_return": benchmark,
        "turnover": turnover,
        "transaction_cost": costs,
    })
    result = result.loc[weights.abs().sum(axis=1) > 0].copy()

    def metrics(series: pd.Series) -> dict:
        ann_return = float((1.0 + series).prod() ** (12.0 / len(series)) - 1.0)
        ann_vol = float(series.std(ddof=1) * np.sqrt(12.0))
        nav = (1.0 + series).cumprod()
        max_drawdown = float((nav / nav.cummax() - 1.0).min())
        return {
            "annualized_return": ann_return,
            "annualized_volatility": ann_vol,
            "sharpe_zero_rf": ann_return / ann_vol if ann_vol else None,
            "max_drawdown": max_drawdown,
            "positive_month_rate": float((series > 0).mean()),
            "total_return": float(nav.iloc[-1] - 1.0),
        }

    summary = {
        "data_mode": "synthetic",
        "seed": 42,
        "months": int(len(result)),
        "transaction_cost_bps_one_way": float(transaction_cost_bps),
        "average_monthly_turnover": float(result["turnover"].mean()),
        "strategy": metrics(result["strategy_return"]),
        "equal_weight_benchmark": metrics(result["benchmark_return"]),
        "claim_limit": "Synthetic execution evidence only; no historical commodity alpha claim.",
    }
    return result, weights.reindex(result.index), summary


def save_results(output_dir: str = "results", seed: int = 42) -> dict:
    returns, carry = generate_synthetic_panel(seed=seed)
    result, weights, summary = run_backtest(returns, carry)
    summary["seed"] = seed
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    result.to_csv(out / "synthetic_carry_trend_returns.csv")
    weights.to_csv(out / "synthetic_carry_trend_weights.csv")
    (out / "synthetic_carry_trend_metrics.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    nav = (1.0 + result[["strategy_return", "benchmark_return"]]).cumprod()
    fig, axes = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
    axes[0].plot(nav.index, nav["strategy_return"], label="Carry + trend", linewidth=2)
    axes[0].plot(nav.index, nav["benchmark_return"], label="Equal-weight", linestyle="--")
    axes[0].set_ylabel("Growth of $1")
    axes[0].set_title("Synthetic Commodity Signal Demo")
    axes[0].legend()
    axes[0].grid(alpha=0.25)
    drawdown = nav.div(nav.cummax()).sub(1.0)
    axes[1].plot(drawdown.index, drawdown["strategy_return"] * 100, color="#b22222")
    axes[1].fill_between(
        drawdown.index, drawdown["strategy_return"] * 100, 0, color="#b22222", alpha=0.2
    )
    axes[1].set_ylabel("Drawdown (%)")
    axes[1].grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "synthetic_carry_trend_backtest.png", dpi=150)
    plt.close(fig)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Offline commodity carry/trend signal demo")
    parser.add_argument("--output-dir", default="results")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(save_results(args.output_dir, args.seed), indent=2))
