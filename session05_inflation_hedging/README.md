# Session 05 — Inflation Surprise & Commodity Hedging
## Macro Linkages & Building an Inflation-Resilient Portfolio

> *"A traditional 60/40 portfolio has an inflation beta of −2.3. Every unexpected 1% CPI surprise costs you 2.3% in real purchasing power. Commodities are one of the few assets that reverse this."*

---

### Learning Objectives

1. Quantify inflation sensitivity (inflation beta) across asset classes using regression analysis
2. Identify which commodities are the most effective inflation hedges and why
3. Analyze performance across defined inflation regimes (deflation, normal, surprise)
4. Construct a portfolio optimized for inflation protection without sacrificing growth exposure

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. Inflation Mechanics** | CPI dynamics, actual vs expected, surprise distribution |
| **2. Regime Definition** | Deflation / Normal / Mild Inflation / Surprise Inflation |
| **3. Asset Inflation Betas** | OLS regression: which assets hedge and which hurt? |
| **4. Commodity Sector Analysis** | Gold, oil, agriculture, metals, nat gas — ranked |
| **5. Historical Episodes** | 2008 GFC, 2011 QE2, 2021–22 Surge (case studies) |
| **6. Rolling Beta Analysis** | How inflation sensitivity changes over time |
| **7. Portfolio Construction** | Modifying 60/40 for inflation protection |
| **8. Real Returns** | Purchasing power preservation over 20 years |
| **9. Summary Dashboard** | Executive scorecard with academic citations |

---

### Inflation Beta Rankings

| Asset | Inflation Beta | Inflation Regime Return |
|-------|---------------|------------------------|
| **USO (Oil)** | **+8.0** | **+69.9%** |
| **UNG (Nat Gas)** | **+5.4** | **+82.2%** |
| **DBC (Broad Cmdty)** | **+5.0** | **+51.3%** |
| GLD (Gold) | +2.2 | +30.5% |
| TIP (TIPS) | +0.8 | +10.3% |
| SPY (Equities) | −1.3 | +2.7% |
| TLT (Long Bonds) | **−3.9** | **−25.5%** |

---

### Portfolio Comparison

| Portfolio | Inflation Beta | Ann. Return | Volatility |
|-----------|---------------|------------|------------|
| 60/40 Traditional | −2.3 | ~7.5% | ~10% |
| All Commodity | +5.1 | ~3.5% | ~18% |
| **Inflation Hedge** | **+0.67** | **~6.8%** | **~11%** |

**Inflation Hedge Allocation:**
```
40% SPY (U.S. equity growth)
20% TIPS (inflation-linked bonds)
15% DBC (broad commodity)
15% GLD (gold — store of value)
10% VNQ (REITs — real asset income)
```

---

### The Inflation Surprise Problem

Traditional finance theory says equities are a long-run inflation hedge (Fisher effect). In practice:
- **Short-run**: Inflation surprises compress P/E multiples → equities fall
- **Long-run**: Earnings eventually catch up → equities recover
- **Implication**: For tactical allocation around inflation surprises, equities fail — commodities are the better near-term hedge

---

### Academic Grounding

| Citation | Relevance |
|----------|-----------|
| Gorton & Rouwenhorst (2006) | Commodity returns and inflation correlation |
| Erb & Harvey (2006) | Cross-commodity inflation sensitivity |
| Levine et al. (2018) — *Commodities for the Long Run* | Long-horizon inflation hedging analysis |
| Campbell & Shiller (1996) | Equity and inflation: short vs long run |

---

### Data Sources

- `USO`, `UNG`, `DBC`, `GLD`, `DBA`, `SLV` — Commodity universe
- `SPY`, `TLT`, `TIP`, `VNQ` — Multi-asset comparison
- `CPIAUCSL` (FRED) — CPI All Urban Consumers
- `T10YIE` (FRED) — 10-year breakeven inflation (expectations)

---

### Discussion Questions

1. Why does the Fisher effect (equities hedge inflation) break down in the short run?
2. Gold has a much lower inflation beta than oil. When would you prefer gold as an inflation hedge?
3. If you manage a pension fund with mostly bond liabilities, how does the inflation hedge portfolio change?
4. What would cause commodity inflation betas to decline over the next decade?

---

*← [Session 04: Trend Following](../session04_trend_following/) | [Session 06: Institutional Allocation →](../session06_institutional_allocation/)*
