# Synthetic Volatility Surfaces

Generative models for SPX implied volatility surface modeling. Builds four architectures (VAE, WGAN-GP, normalizing flow, conditional diffusion) to generate synthetic vol surfaces, extract latent features, and benchmark against SVI-parameterized baselines.

## What this does

1. Ingests raw SPX/SPXW options data (127 trading days, H2 2022)
2. Computes implied volatility via Black-76 inversion with Brent's method
3. Constructs forward prices from put-call parity
4. Fits Gatheral SVI parameterization per expiration slice
5. Trains four generative models on the fitted surfaces
6. Extracts latent volatility features and benchmarks pricing improvement

## Data

EOD options data from [HistoricalData.net](https://historicaldata.net) (free sample). 34 columns per row including bid/ask quotes, precomputed IV/Greeks (used for validation only), and risk-free rate curves in the manifest.

**Data is not included in this repo.** Download the free sample from HistoricalData.net and place the `day_by_date/` folder in `data/`.

## Project structure

```
Synthetic-Volatility-Surface-Project/
├── src/                        # Importable Python modules
│   ├── data/
│   │   └── loader.py           # Data loading, filtering, cleaning
│   ├── pricing/
│   │   └── black76.py          # Black-76 pricing and IV solver
│   ├── surface/
│   │   └── svi.py              # SVI parameterization and fitting
│   └── utils/
│       └── rates.py            # Treasury rate interpolation
├── notebooks/                  # Exploration and visualization
│   └── 01_data_exploration.ipynb
├── tests/                      # Unit tests
├── data/                       # Local data (not committed)
│   └── day_by_date/            # Daily option CSVs
├── configs/                    # Pipeline parameters
└── requirements.txt
```

## Setup

1. Clone the repo:

```bash
git clone https://github.com/jpzam1106/Synthetic-Volatility-Surface-Project.git
cd Synthetic-Volatility-Surface-Project
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Add data:

Download the free options sample from [HistoricalData.net](https://historicaldata.net/samples.html). Extract the ZIP and copy `day_by_date/` into `data/`.

4. Verify setup:

```bash
python -c "import pandas; print('ready')"
```

## Requirements

- Python 3.12
- numpy, scipy, pandas, matplotlib, plotly
- PyTorch (Modules 1-3)
- Streamlit (Module 4)

See `requirements.txt` for full list.

## Pipeline

**Module 0: Data pipeline and SVI baseline**
- Load and filter SPX/SPXW European-style contracts
- Compute mid prices, time to expiry, risk-free rates from manifest curve
- Forward prices via put-call parity
- Black-76 IV extraction via Brent's method, validated against provider IV
- Gatheral SVI fit per (date, expiration) slice

**Module 1: VAE and Conditional VAE**
- Variational autoencoder on discretized vol surfaces
- Conditional variant conditioned on macro regime features

**Module 2: WGAN-GP, normalizing flow, diffusion**
- WGAN-GP with gradient penalty
- RealNVP normalizing flow
- Conditional DDPM
- Unified comparison: fidelity, arbitrage-free rate, sampling speed

**Module 3: Latent features for pricing**
- Extract latent representations from each model
- Ablation study on pricing RMSE improvement over SVI baseline
- Out-of-sample stress testing

**Module 4: Dashboard and documentation**
- Streamlit app for interactive surface exploration
- Research note summarizing results

## Current status

Module 0 in progress.

## License

MIT
