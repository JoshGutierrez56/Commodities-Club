# Commodity Futures Research Series

Six educational notebooks on futures return decomposition, term structure, carry, trend following, inflation hedging, and institutional allocation, plus a deterministic offline signal demo.

## Verified result

The repository now includes a reproducible carry/trend evidence bundle in [`results/`](results/README.md). On 238 months of deterministic synthetic data, after 10 bps one-way costs, the demo recorded:

- 4.68% annualized return
- 10.52% annualized volatility
- 0.445 zero-rate Sharpe
- -20.43% maximum drawdown

The equal-weight synthetic benchmark recorded a 3.06% annualized return and 0.350 Sharpe. These figures prove the code runs; they are not historical commodity performance or an alpha claim.

## Reproduce the offline signal demo

```bash
python -m pip install -r requirements.txt
python run_signal_demo.py --output-dir results --seed 42
python -m pytest -q
```

The demo uses only generated data, lags signals before applying returns, constrains gross exposure, and deducts turnover-based costs.

## Notebook series

1. [`Session01_Return_Decomposition.ipynb`](session01_return_decomposition/Session01_Return_Decomposition.ipynb)
2. [`Session02_Futures_Curve.ipynb`](session02_term_structure/Session02_Futures_Curve.ipynb)
3. [`Session03_Carry_in_Commodities.ipynb`](session03_carry/Session03_Carry_in_Commodities.ipynb)
4. [`Session04_Trend_Following.ipynb`](session04_trend_following/Session04_Trend_Following.ipynb)
5. [`Session05_Inflation_Surprise.ipynb`](session05_inflation_hedging/Session05_Inflation_Surprise.ipynb)
6. [`Session06_Institutional_Allocation.ipynb`](session06_institutional_allocation/Session06_Institutional_Allocation.ipynb)

The notebooks download public data through `yfinance` and, where applicable, FRED. Results can change with data revisions, ticker availability, and run date. The committed offline bundle is the canonical reproducibility check.

## Methodology covered

- Futures total return as spot, roll, and collateral components
- Cost-of-carry and curve-regime interpretation
- Cross-commodity carry signals
- Time-series momentum with volatility scaling
- Inflation-surprise sensitivity
- Core/satellite allocation and transaction-cost-aware signal combination

## Requirements

Python 3.10+ is recommended. An internet connection is needed only for the live-data notebook cells.

This repository is educational research, not investment advice.
