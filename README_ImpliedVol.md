## 📈 Implied Volatility Estimation (Brent Method)

This module extends the vanilla option pricer by computing the **implied volatility** from observed market option prices using a numerical root-finding approach.

## 🎯 Objective

Given:
- Spot price \( S_0 \)
- Strike \( K \)
- Time to maturity \( T \)
- Risk-free rate \( r \)
- Dividend yield \( q \)
- Market option price \( P^{mkt} \)

The goal is to compute the volatility \( \sigma \) such that:

\[
BSM(\sigma) = P^{mkt}
\]

This is achieved by solving:

\[
f(\sigma) = BSM(\sigma) - P^{mkt} = 0
\]

---

## ⚙️ Numerical Method

| Method | Description | Why Used |
|--------|-------------|-----------|
| **Brent’s Method (scipy.optimize.brentq)** | Hybrid root-finding algorithm combining bisection, secant, and inverse quadratic interpolation. | Robust and guaranteed convergence if bracketed |
| **Newton-Raphson (optional extension)** | Iterative method using Vega (first derivative). | Fast convergence but may diverge |

The implementation uses:

```python
brentq(error_function, 1e-6, 5.0)
```

Where:
- Lower bound ≈ 0%
- Upper bound = 500%
- Root is guaranteed if \( f(a)f(b) < 0 \)

---

## 🔎 Workflow

1. Retrieve spot price via `yfinance`
2. Select option expiry and compute \( T \) (ACT/365)
3. Retrieve bid/ask and compute market mid price
4. Define pricing error function:
   \[
   f(\sigma) = BSM(\sigma) - P^{mkt}
   \]
5. Apply Brent solver
6. Return implied volatility

---

## 📊 Practical Considerations

- Uses **calendar days (365)** for maturity conversion.
- Mid price is preferred:  
  \[
  P^{mkt} = \frac{bid + ask}{2}
  \]
- Falls back to `lastPrice` if bid/ask unavailable.
- Bracket range is wide enough to capture most equity options.

---

## 🚀 Future Improvements

- [ ] Automatic risk-free curve integration by maturity
- [ ] Market-implied dividend yield extraction
- [ ] Surface construction (strike–maturity grid)
- [ ] Volatility interpolation for non-listed strikes
- [ ] Smile / skew visualization
- [ ] Vega-based Newton fallback implementation

---

## 🧠 Financial Interpretation

Implied volatility represents the market’s expectation of future uncertainty embedded in option prices.

It is not a forecast but the volatility that reconciles theoretical price with observed market price.
