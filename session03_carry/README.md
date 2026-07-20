# Session 03 — Carry in Commodities
## Risk Transfer, Hedging Pressure & the Carry Trade

> *"Natural gas investors paid a 9.7% annual 'carry tax' over 16 years. Oil investors paid 6.5%. Gold investors paid nothing. The difference is entirely in storage economics and hedging pressure."*

---

### Learning Objectives

1. Define carry in the commodity context: the return earned from holding a futures position assuming spot doesn't move
2. Understand Keynes' Theory of Normal Backwardation and Cootner's hedging pressure model
3. Measure carry across a diversified commodity universe using ETF pairs
4. Build and backtest carry long/short strategies

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. What Is Carry?** | Formal definition and intuition |
| **2. Theory of Normal Backwardation** | Keynes (1930): producers pay a risk premium to hedge |
| **3. Hedging Pressure Framework** | Cootner: net hedger position → carry signal |
| **4. ETF Pair Methodology** | Using USO/USL, UNG/UNL, DBC/GSG as carry proxies |
| **5. 16-Year Carry Analysis** | Cross-commodity carry measurement with real data |
| **6. Predictive Power** | R² of carry signal at 1-month, 3-month, 1-year horizons |
| **7. Carry Long/Short Backtest** | Strategy construction and performance attribution |
| **8. Regime Analysis** | When does carry work? When does it fail? |
| **9. Cross-Commodity Correlation** | Carry diversification across sectors |
| **10. Summary & Carry + Momentum Preview** | Setup for Session 4 |

---

### Core Carry Metrics

| Asset | Avg Annual Carry | Regime |
|-------|-----------------|--------|
| Natural Gas (UNG/UNL) | −9.7% | Deep contango |
| Crude Oil (USO/USL) | −6.5% | Contango |
| Broad Cmdty (DBC/GSG) | −1.8% | Mild contango |
| Gold (GLD/IAU) | 0.0% | Flat / no carry |

**Carry predictive power (R² at horizon):**
- 1 month: ~0.8%
- 3 months: ~3.1%
- 1 year: **8.1%**

---

### Theoretical Framework

**Carry (annualized):**
```
Carry = −ln(F₂/F₁) × (252/ΔT)
```

**Keynes' Risk Premium:**
Producers are natural short hedgers → futures prices below expected spot → speculators earn a premium for providing insurance.

**Cootner's Hedging Pressure:**
```
Expected Return ∝ Net Hedger Short Position
```

---

### Strategy: Carry Long/Short

```python
# Signal: go long high-carry (backwardated) commodities,
#         short low-carry (contangoed) commodities

carry_signal = -(F2 - F1) / F1  # annualized
position = np.sign(carry_signal) * vol_target / realized_vol
```

**Results vs benchmarks:**
- Carry L/S outperformed equal-weight in all tested periods
- Sharpe improvement: ~0.25 over equal-weight long-only

---

### Data Sources

- `USO` / `USL` — WTI crude (front-month vs 12-month roll)
- `UNG` / `UNL` — Natural gas ETF pair
- `DBC` / `GSG` — Broad commodity index pair
- `GLD` / `IAU` — Gold pair (near-zero carry baseline)
- CFTC Disaggregated COT Reports (optional extension)

---

### Discussion Questions

1. Why does natural gas have higher negative carry than oil despite both being energy commodities?
2. If carry predictive power improves dramatically at 1-year vs 1-month horizons, what does that imply about short-term market efficiency?
3. What market conditions would cause carry strategies to fail catastrophically?
4. How would you combine carry and momentum signals for a more robust strategy? (Preview of Session 4)

---

*← [Session 02: Term Structure](../session02_term_structure/) | [Session 04: Trend Following →](../session04_trend_following/)*
