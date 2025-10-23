## 🧮 Vanilla Option Pricer in Python

This project implements multiple pricing models for **European vanilla options** in Python.  
It compares **predicted vs actual price changes** and calculates the main **Greeks** (Δ, Γ, Θ, ρ, Vega) to assess model precision and realism.

## ⚙️ Repository Structure

📁 option-pricer-python/
┣ 📓 Vanilla_Option_Pricer.ipynb ← Core model explanations and examples
┣ 📓 Optimized_Pricer.ipynb ← Calibrated model with error analysis
┣ 📄 Vanilla_Option_Pricer.py ← Clean Python version (executable)
┗ 📄 README.md ← This documentation

## 🎯 Objectives

This project demonstrates:
- Application of **theoretical finance models** in code  
- Use of **Greeks** to evaluate model robustness  
- Quantitative **error analysis and calibration**  
- Reproducible workflows for **option pricing and hedging**

## 📊 Models

| Model | Description | Key Features |
|--------|--------------|---------------|
| **Black–Scholes–Merton (BSM)** | Analytical model assuming log-normal distribution of returns. | Closed-form pricing and Greeks computation |
| **Binomial Tree** | Discrete-time approximation of underlying price evolution. | Step-by-step convergence toward BSM price |
| **Monte Carlo Simulation** | Randomized sampling of terminal prices using GBM. | Convergence check and performance test |
| **Greeks-Based Calibration** | Model refinement comparing predicted vs realized changes. | Estimation of model accuracy (mean and max error) |

## ✅ Current Work (Completed)

- **Black–Scholes–Merton (BSM) model:**  
  Computes theoretical prices for European calls and puts using analytical formulas.
- **Greeks computation:**  
  Calculates sensitivities (Δ, Γ, Θ, ρ, Vega) to assess price responsiveness.
- **Price variation prediction:**  
  Uses Greeks to estimate small price changes and compares them to simulated results.
- **Error analysis:**  
  Measures **average** and **maximum percentage error** between predicted and actual price variations.

## 🚧 Upcoming Improvements (In Progress)

- [ ] Add **Implied Volatility estimation** using Newton-Raphson  
- [ ] Implement **American option pricing** (Cox–Ross–Rubinstein model)  
- [ ] Introduce **stochastic volatility models** (Heston framework)  
- [ ] Build a **Streamlit app** for interactive option visualization  
- [ ] Integrate **real market data** (e.g., Yahoo Finance API) for validation  

## 🧰 Technologies

- **Python 3.12**
- Libraries: NumPy, SciPy, Pandas, Matplotlib
- Environment: Jupyter Notebook / VS Code

## 📬 Author

**Thomas Bures**  
MSc Financial Engineering & Quantitative Finance  
🔗 [LinkedIn](https://www.linkedin.com/in/thomas-bures-07437b253/)  
🔗 [GitHub](https://github.com/ThomasBuresQuant)

> “In quantitative finance, every model is wrong — the key is knowing how wrong.”
