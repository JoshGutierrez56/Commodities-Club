# Session 06 — Building an Institutional Commodity Allocation
## Capstone: Core-Satellite Framework & Multi-Factor Portfolio Construction

> *"Institutional commodity allocation is not about picking the best commodity. It is about combining carry, momentum, and macro signals in a risk-budgeted framework that survives every regime."*

---

### Learning Objectives

1. Synthesize all five prior sessions into a unified, institutional-grade allocation framework
2. Implement a core-satellite structure: passive diversification + active factor tilts
3. Integrate carry, momentum, and inflation signals into a composite score
4. Apply risk budgeting, volatility targeting, and tracking error constraints
5. Evaluate performance via walk-forward backtesting (2005–2024)

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. Framework Overview** | Core-satellite structure and investment objectives |
| **2. Signal Integration** | Combining carry (S3), momentum (S4), and inflation beta (S5) |
| **3. Universe Construction** | 15-20 commodity ETFs across energy, metals, agriculture |
| **4. Factor Scoring** | Z-score normalization and composite signal formation |
| **5. Core Allocation** | Passive index replication with risk-parity weighting |
| **6. Satellite Allocation** | Active long/short overlay using composite signals |
| **7. Risk Budgeting** | Volatility targeting, TEV constraints, sector limits |
| **8. Portfolio Optimization** | CVXPY-based mean-variance with factor constraints |
| **9. Walk-Forward Backtest** | 2005–2024 out-of-sample performance (expanding window) |
| **10. Regime Analysis** | Performance across inflation, deflation, crisis regimes |
| **11. Attribution** | Factor-level and sector-level PnL decomposition |
| **12. Final Dashboard** | Full performance tearsheet |

---

### Core-Satellite Framework

```
Total Portfolio
├── Core (60–70% of risk budget)
│   ├── Passive broad commodity index (DBC/GSG)
│   ├── Risk-parity weighted across sectors
│   └── Rebalanced quarterly
│
└── Satellite (30–40% of risk budget)
    ├── Carry L/S overlay (Session 3)
    ├── TSMOM overlay (Session 4)
    ├── Inflation tilt (Session 5)
    └── Combined via composite Z-score
```

---

### Composite Signal Construction

```python
# Individual signals (Z-scored cross-sectionally)
z_carry     = zscore(carry_signal)        # Session 3
z_momentum  = zscore(momentum_12_1)       # Session 4
z_inflation = zscore(inflation_beta_roll) # Session 5

# Composite (equal-weight by default, can optimize weights)
composite = (w1 * z_carry + w2 * z_momentum + w3 * z_inflation)

# Position construction
position_i = composite_i * (target_vol / realized_vol_i)
```

---

### Risk Budget Architecture

| Allocation | Risk Budget | Expected Sharpe |
|------------|------------|-----------------|
| Core (passive) | 60% | ~0.3–0.4 |
| Carry Satellite | 15% | ~0.5–0.7 |
| Momentum Satellite | 15% | ~0.7–1.0 |
| Inflation Tilt | 10% | ~0.4–0.6 |
| **Composite Portfolio** | **100%** | **~0.8–1.1** |

---

### Optimization Problem

```
Minimize:  w' Σ w  (portfolio variance)

Subject to:
  Σ wᵢ = 1                           (full investment)
  |wᵢ| ≤ 0.15                        (position limits)
  σ_portfolio ≤ target_vol            (vol constraint)
  |factor_exposure| ≤ factor_limit    (factor limits)
  sector_weight ≤ 0.40               (sector concentration)
  TE vs benchmark ≤ 0.08             (tracking error)
```

---

### Walk-Forward Backtest Results (2005–2024)

| Metric | Composite | Passive Benchmark |
|--------|-----------|------------------|
| Ann. Return | ~10–13% | ~3–5% |
| Ann. Volatility | 10% (targeted) | ~18% |
| Sharpe Ratio | ~0.85–1.1 | ~0.2–0.3 |
| Max Drawdown | ~−20% | ~−55% |
| Calmar Ratio | ~0.5–0.65 | ~0.05–0.10 |
| Information Ratio | ~0.6–0.8 | — |

*Results are illustrative; actual performance depends on execution assumptions.*

---

### Academic Grounding

| Citation | Relevance |
|----------|-----------|
| Grinold & Kahn (1999) — *Active Portfolio Management* | IC, IR, Fundamental Law |
| Black & Litterman (1992) | Bayesian signal integration |
| Brinson, Hood & Beebower (1986) | Attribution framework |
| Gorton & Rouwenhorst (2006) | Commodity factor premia |
| Moskowitz, Ooi & Pedersen (2012) | TSMOM in institutional context |

---

### Data Sources

- `USO`, `USL`, `UNG`, `UNL`, `DBC`, `GSG`, `GLD`, `SLV`, `DBA`, `PDBC` — Commodity universe
- `SPY`, `TLT`, `TIP` — Cross-asset context
- `CPIAUCSL`, `T10YIE` (FRED) — Macro overlay
- `^IRX` — Collateral rate

---

### Discussion Questions

1. Why is the core-satellite structure preferred over a pure active approach for institutional allocators?
2. You have carry, momentum, and inflation signals. One is consistently outperforming. Should you increase its weight? What are the risks?
3. How would you adjust this framework if your mandate required you to stay net-long at all times?
4. A sovereign wealth fund wants 8% vol target with max 15% drawdown. How do you modify the risk budget?
5. What do you think is the most important risk not captured in this model?

---

### Series Synthesis

This capstone completes the full analytical arc of the seminar series:

| Session | What We Built | What It Contributes Here |
|---------|--------------|--------------------------|
| S1 | Return decomposition | Explains *why* commodity returns behave as they do |
| S2 | Term structure analysis | Regime identification for signal conditioning |
| S3 | Carry signal | First active factor — satellite layer |
| S4 | Momentum signal | Second active factor — crisis alpha |
| S5 | Inflation hedge | Third factor — macro overlay |
| **S6** | **Integration** | **Full institutional framework** |

---

*← [Session 05: Inflation Hedging](../session05_inflation_hedging/) | [Back to Series Overview →](../README.md)*
