# Session 01 — Futures Returns ≠ Spot Returns
## Return Decomposition: Spot, Roll Yield & Collateral Yield

> *"An investor in crude oil futures over 2006–2024 would have lost 93% of their investment — while the spot price of oil was only down 88%. The gap is entirely explained by roll yield."*

---

### Learning Objectives

1. Understand why futures returns systematically diverge from spot price returns
2. Decompose total futures return into its three components: spot, roll yield, and collateral
3. Quantify the impact of contango drag using real ETF data (USO as the futures vehicle)
4. Identify historical regimes where roll yield helped or hurt investors

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. Return Decomposition Framework** | Mathematical derivation of the three-component model |
| **2. USO Deep Dive** | 18-year analysis using real WTI crude data |
| **3. Spot vs Futures: Cumulative Chart** | The key chart — why they diverge |
| **4. Roll Yield Attribution** | Regime-by-regime breakdown (2007 bull, oil glut, COVID) |
| **5. Contango vs Backwardation** | How curve shape determines roll return |
| **6. Cross-Commodity Comparison** | Oil vs natural gas vs gold vs broad index |
| **7. Collateral Yield** | Why the T-bill component matters more than you think |
| **8. Key Takeaways & Discussion** | Five investor insights + discussion questions |

---

### Core Equations

**Total Futures Return:**
```
R_total = R_spot + R_roll + R_collateral
```

**Roll Yield (annualized from term structure):**
```
RY = ln(F₁ / F₂) × (252 / ΔT)
```

**Collateral Return (fully collateralized):**
```
R_collateral ≈ r_f  (risk-free rate)
```

---

### Key Results

| Component | Cumulative (2006–2024) |
|-----------|----------------------|
| Spot Return | −88% |
| Roll Yield | −80% |
| Collateral Yield | +27% |
| **Total (USO)** | **−93%** |

- **59% of trading days** in contango (negative roll environment)
- Backwardation regime: avg roll yield **+47%/yr**
- Contango regime: avg roll yield **−41%/yr**

---

### Data Sources

- `USO` — United States Oil Fund (WTI crude futures proxy)
- `USL` — United States 12-Month Oil Fund (longer-dated proxy)
- `BNO` — United States Brent Oil Fund
- `^IRX` — 13-week T-bill rate (collateral proxy)

---

### Discussion Questions

1. Why does a futures investor earn a different return than someone who owns physical oil in a barrel?
2. How does contango and backwardation each affect a passive long futures strategy?
3. If you knew the futures curve would remain in steep contango for 2 years, how would you adjust your commodity exposure?
4. The collateral yield averaged ~2%/yr over this period. In a 5% rate environment, how does that change the calculus?

---

*← Back to [Series Overview](../README.md) | Session 02: Reading the Futures Curve →*
