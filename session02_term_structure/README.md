# Session 02 — Reading the Futures Curve
## Term Structure Analysis & Market Regime Identification

> *"The shape of the futures curve is the market's collective forecast. An investor who can read it has an edge; one who ignores it is flying blind."*

---

### Learning Objectives

1. Interpret futures curves — plot price against delivery date and diagnose market regime
2. Connect curve shape to underlying supply/demand fundamentals and inventory levels
3. Identify contango vs backwardation regimes and understand their return implications
4. Recognize regime transitions and how to position around them

---

### Notebook Highlights

| Section | Description |
|---------|-------------|
| **1. What Is the Futures Curve?** | Term structure as a market snapshot |
| **2. Contango vs Backwardation** | Side-by-side curve visualizations with real data |
| **3. Historical Term Structure Evolution** | How the oil curve shifted across 2007–2024 |
| **4. Curve Snapshots Across Crises** | COVID crash, Ukraine invasion, 2014 glut |
| **5. Fundamental Drivers** | Inventory correlation (r = 0.92), storage costs, convenience yield |
| **6. Regime Statistics** | Frequency, duration, and roll-yield consequences by regime |
| **7. Convergence** | Why all futures must converge to spot at expiration |
| **8. USO vs USL Analysis** | Real-world proof: same commodity, 55-point return gap |
| **9. Summary Dashboard** | Key takeaways + preview of Session 3 (Carry) |

---

### Key Results

| Metric | Value |
|--------|-------|
| % of days in contango (2006–2024) | ~80.1% |
| Average curve slope | +4.36% |
| Avg roll yield — contango regime | −6.8%/yr |
| Avg roll yield — backwardation regime | +5.3%/yr |
| Inventory-curve correlation | 0.92 |
| USO vs USL cumulative gap | 55 percentage points |

---

### Theoretical Framework

**Cost of Carry Model:**
```
F(T) = S₀ × e^{(r + u - y) × T}
```
Where:
- `S₀` = spot price
- `r` = risk-free rate
- `u` = storage cost (% of spot)
- `y` = convenience yield

**Convenience Yield:**
```
y = r + u - ln(F/S)/T
```

High inventory → low convenience yield → contango
Low inventory → high convenience yield → backwardation

---

### Data Sources

- `CL=F` — WTI Crude Oil front-month futures
- `USO`, `USL`, `BNO` — Crude oil ETFs (term structure proxies)
- `UNG`, `UNL` — Natural gas ETFs
- `EIA` — U.S. crude oil inventory data

---

### Discussion Questions

1. You observe a steep contango in natural gas. What does this tell you about current supply/demand conditions?
2. How does the theory of storage (Working 1949) explain the relationship between inventory and curve shape?
3. When might you prefer USL over USO as your oil exposure vehicle?
4. What market event would most quickly flip oil from contango into backwardation?

---

*← [Session 01: Return Decomposition](../session01_return_decomposition/) | [Session 03: Carry →](../session03_carry/)*
