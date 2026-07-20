# Session 04 — Trend Following & Crisis Convexity
## Time-Series Momentum in Commodity Futures

> *"Trend-following in commodities earned positive returns in every equity bear market exceeding 20% since 1990. It is not just an alpha strategy — it is crisis insurance."*

---

### Learning Objectives

1. Understand time-series momentum (TSMOM) and how it differs from cross-sectional momentum
2. Build momentum signals using multiple lookback windows
3. Backtest TSMOM strategies across a diversified commodity universe
4. Analyze the "crisis alpha" property and the convexity of trend-following returns
5. Combine carry and momentum signals for factor diversification

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. What Is Time-Series Momentum?** | Definition, intuition, and empirical evidence |
| **2. Why Momentum Works in Commodities** | Behavioral + structural explanations |
| **3. Signal Construction** | 1-month, 3-month, 6-month, 12-month lookbacks |
| **4. Volatility Targeting** | Position sizing via realized vol normalization |
| **5. Strategy Backtest** | Full TSMOM backtest 2006–2024 |
| **6. Crisis Alpha Analysis** | Performance during GFC, COVID, Ukraine |
| **7. Return Convexity** | Payoff profile vs equity market returns |
| **8. Carry + Momentum Combo** | Factor diversification: correlation ~0.15 |
| **9. Risk Attribution** | What drives strategy PnL? |
| **10. Summary & Robustness** | Lookback sensitivity, regime dependence |

---

### Core TSMOM Framework

**Signal (Moskowitz, Ooi & Pedersen 2012):**
```
TSMOM_signal(t) = sign(r_{t-1, t-12})
```

**Volatility-Scaled Position:**
```
w_i = (TSMOM_signal_i × target_vol) / σ_i
```
Where `σ_i` is the 21-day realized volatility of asset `i`.

**Key Insight — Convexity:**
```
E[TSMOM | equity down > 20%] >> E[TSMOM | normal]
```
Trend-following has a positive skew vs equity markets — it is effectively long volatility.

---

### Strategy Results Summary

| Metric | TSMOM | Buy-and-Hold |
|--------|-------|-------------|
| Ann. Return | ~8–12% | ~3–5% |
| Ann. Volatility | 10% (targeted) | ~18% |
| Sharpe Ratio | ~0.7–1.0 | ~0.2–0.3 |
| Max Drawdown | ~−18% | ~−60%+ |
| GFC (2008) Return | **Positive** | −45%+ |
| COVID (2020) | **Positive** | −35% |

---

### Crisis Alpha: Historical Performance

| Event | TSMOM | CRB Commodity Index |
|-------|-------|---------------------|
| GFC 2008 | +18–25% | −47% |
| 2011 (EM slowdown) | +5–10% | −13% |
| COVID 2020 | +12–20% | −24% |
| 2022 Inflation | +30–40% | +25% |

---

### Carry + Momentum Combination

```python
# Signal combination
combo_signal = 0.5 * carry_zscore + 0.5 * momentum_zscore

# Benefits:
# - Carry profits from static curve relationships
# - Momentum profits from directional price trends
# - Low correlation: ~0.15 (strong diversification)
```

---

### Data Sources

- `USO`, `UNG`, `DBC`, `GLD`, `DBA`, `SLV` — Commodity ETF universe
- `^GSPC` — S&P 500 (for crisis alpha analysis)
- `^IRX` — T-bill rate (collateral)

---

### Discussion Questions

1. Why do behavioral factors (herding, underreaction) support momentum in commodity markets?
2. When would you expect momentum to fail? Think about sudden reversals and choppy sideways markets.
3. Why does trend-following have positive convexity vs equity returns?
4. You have a carry signal and a momentum signal for 10 commodities. How do you combine them optimally?

---

*← [Session 03: Carry](../session03_carry/) | [Session 05: Inflation Hedging →](../session05_inflation_hedging/)*
