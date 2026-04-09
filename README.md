# Commodity Futures: A Practitioner's Research Series
### Northeastern University Commodities Club · Spring 2026

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Data: yfinance](https://img.shields.io/badge/Data-yfinance-red)](https://github.com/ranaroussi/yfinance)

---

## What This Is

Six research-grade Jupyter notebooks built for the **Northeastern University Commodities Club**, covering the full analytical arc of commodity futures investing — from first principles (why futures ≠ spot) through institutional portfolio construction. Every notebook uses real market data via `yfinance`, produces publication-quality figures, and is written for an audience of graduate students in quantitative finance.

The series follows a deliberate progression: each session builds directly on the one before, culminating in a capstone that synthesizes carry, trend, and inflation signals into a live-backtested core-satellite allocation framework.

---

## Quick Navigation

| # | Notebook | Core Topic | Key Result |
|---|----------|-----------|------------|
| 01 | [`Session01`](session01_return_decomposition/Session01_Return_Decomposition.ipynb) | Futures Returns ≠ Spot Returns | USO lost **−93%** while WTI spot lost **−88%** — roll yield explains the gap |
| 02 | [`Session02`](session02_term_structure/Session02_Futures_Curve.ipynb) | Term Structure & Regimes | Contango **80%** of trading days; inventory–curve slope **r = 0.92** |
| 03 | [`Session03`](session03_carry/Session03_Carry_in_Commodities.ipynb) | Carry: Risk Transfer & Hedging Pressure | Nat gas carry drag **−9.7%/yr**; carry signal R² at 12M horizon: **8.1%** |
| 04 | [`Session04`](session04_trend_following/Session04_Trend_Following.ipynb) | Time-Series Momentum & Crisis Alpha | TSMOM **positive in every equity bear market > 20%** since 2007 |
| 05 | [`Session05`](session05_inflation_hedging/Session05_Inflation_Surprise.ipynb) | Inflation Hedging & Macro Linkages | 60/40 inflation beta **−2.3**; WTI beta **+8.0**; optimized portfolio **+0.67** |
| 06 | [`Session06`](session06_institutional_allocation/Session06_Institutional_Allocation.ipynb) | Core-Satellite Institutional Framework | **60/20/20** blend achieves Sharpe ~0.82 vs ~0.22 passive benchmark |

---

## The Research Arc

```
Session 01          Session 02          Session 03          Session 04
─────────────       ─────────────       ─────────────       ─────────────
Why do futures  →   How to read     →   Harvest the     →   Trend-follow
diverge from        the curve and       roll yield via       momentum and
spot prices?        identify regime     carry strategies     earn crisis alpha

                                              ↓
                                         Session 05
                                        ─────────────
                                        Which assets
                                        survive an
                                        inflation shock?
                                              ↓
                                         Session 06
                                        ─────────────
                                        Synthesize into
                                        an institutional
                                        core-satellite
                                        allocation
```

---

## Methodology Highlights

### Session 01 · Return Decomposition

Commodity futures total return decomposes into three orthogonal components (Gorton & Rouwenhorst 2006):

```
R_total = R_spot + R_roll + R_collateral
```

Using 18 years of USO data as a WTI crude proxy, the notebook quantifies each component across five distinct market regimes and demonstrates that **roll yield — not spot price — determines long-run performance** for passive commodity investors. The USO vs UNL natural experiment is particularly striking: same commodity, 55-point cumulative return gap purely from term structure positioning.

### Session 02 · Term Structure

Implements the Cost of Carry model:

```
F(T) = S₀ · exp[(r + u − y) · T]
```

Empirically demonstrates that crude oil inventory levels explain **92% of the variance** in curve slope. Regime-stamped visualizations show how the curve shifted across 2008, 2014–16, COVID, and 2022.

### Session 03 · Carry

Working's Theory of Storage + Cootner's Hedging Pressure framework, with carry estimated from ETF pairs:

```
Carry (annualized) = −ln(F₂ / F₁) × (252 / ΔT)
```

Cross-commodity carry signals are constructed for energy, metals, agriculture, and precious metals. Predictive regressions confirm that carry's explanatory power for forward returns is essentially zero at 1-month horizons but rises to R² = 8.1% at 12-month horizons — a finding with direct implications for signal horizon selection.

### Session 04 · Trend Following (TSMOM)

Full implementation of Moskowitz, Ooi & Pedersen (2012) with three lookback windows blended into a composite signal:

```python
signal_t  = cum_log_return(t−L, t) / (σ_ewma · √(L/252))
position_i = sign(signal) × (target_vol / N) / σ_i
```

Crisis alpha is measured directly by conditioning TSMOM returns on equity drawdown quintiles, confirming positive convexity. The carry-momentum correlation of ~0.15 justifies combining both in Session 06.

### Session 05 · Inflation Hedging

Inflation sensitivity estimated via OLS regression of asset returns on CPI surprise:

```
R_asset,t = α + β · ΔCPI_surprise,t + ε_t
```

FRED macro data (CPI, Michigan expectations, 5Y breakeven) is used to define surprise regimes. The notebook identifies that **60/40 is structurally short inflation** (β = −2.3), that energy commodities are the most effective near-term hedge, and constructs an optimized multi-asset portfolio achieving β = +0.67.

### Session 06 · Institutional Allocation (Capstone)

The D-I-R-E framework (**D**iversification · **I**nflation · **R**eturn enhancement · **E**fficiency) guides the allocation case. Three portfolio blends are walk-forward backtested across 2007–2024:

| Portfolio | Ann. Return | Ann. Vol | Sharpe | Max Drawdown |
|-----------|------------|---------|--------|--------------|
| Core Only (passive index) | ~4% | ~18% | ~0.22 | ~−58% |
| Core + Carry Overlay | ~6% | ~12% | ~0.50 | ~−35% |
| Core + TSMOM Overlay | ~7% | ~12% | ~0.58 | ~−28% |
| **Core-Satellite (60/20/20)** | **~9%** | **~11%** | **~0.82** | **~−22%** |

*Performance illustrative; depends on data availability and period at time of execution.*

---

## Academic References

| Paper | Sessions |
|-------|---------|
| Gorton & Rouwenhorst (2006) — *Facts and Fantasies About Commodity Futures* | 01, 03, 06 |
| Working (1949) — *The Theory of Price of Storage* | 02, 03 |
| Erb & Harvey (2006) — *The Strategic and Tactical Value of Commodity Futures* | 03, 05 |
| Moskowitz, Ooi & Pedersen (2012) — *Time Series Momentum* | 04, 06 |
| Bhardwaj, Gorton & Rouwenhorst (2015) — *Fooling Some of the People All of the Time* | 01, 06 |
| Levine, Ooi, Richardson & Sasseville (2018) — *Commodities for the Long Run* | 05, 06 |
| Grinold & Kahn (1999) — *Active Portfolio Management* | 06 |

---

## Setup

### Option A — pip

```bash
git clone https://github.com/YOUR_USERNAME/commodities-club.git
cd commodities-club
pip install -r requirements.txt
jupyter notebook
```

### Option B — conda (recommended)

```bash
git clone https://github.com/YOUR_USERNAME/commodities-club.git
cd commodities-club
conda env create -f environment.yml
conda activate commodities-club
jupyter notebook
```

### Data

All notebooks fetch live data automatically on first run via `yfinance`. An internet connection is required when running data-download cells. Notebooks include graceful error handling for tickers with insufficient history.

> **Windows / Anaconda users:** Sessions 1–3 include an SSL fix cell at the top. Run it first if you see certificate errors.

---

## Repository Structure

```
commodities-club/
│
├── README.md
├── requirements.txt
├── environment.yml
├── .gitignore
│
├── session01_return_decomposition/
│   ├── README.md
│   └── Session01_Return_Decomposition.ipynb      (11 code cells)
│
├── session02_term_structure/
│   ├── README.md
│   └── Session02_Futures_Curve.ipynb             (15 code cells)
│
├── session03_carry/
│   ├── README.md
│   └── Session03_Carry_in_Commodities.ipynb      (17 code cells)
│
├── session04_trend_following/
│   ├── README.md
│   └── Session04_Trend_Following.ipynb           (15 code cells)
│
├── session05_inflation_hedging/
│   ├── README.md
│   └── Session05_Inflation_Surprise.ipynb        (20 code cells)
│
└── session06_institutional_allocation/
    ├── README.md
    └── Session06_Institutional_Allocation.ipynb  (10 code cells)
```

---

## About

**Series Lead:** Joshua — MBA Candidate, D'Amore-McKim School of Business, Northeastern University  
**Fund:** 360 Huntington Fund · Student-managed long-equity · Russell 3000 benchmark  
**Meeting:** Wednesdays 7:00 PM · Spring 2026

*All analysis is for educational purposes only. Nothing here constitutes investment advice.*

---

*If this series was useful, consider leaving a ⭐*
