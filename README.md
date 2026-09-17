# Synthetic-Volatility-Surface-Project

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
