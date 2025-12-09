# AI-Driven Trading Pattern Indicator

An educational, end-to-end machine learning pipeline for generating **synthetic stock market data**, engineering **technical indicator features**, and training an **ensemble model (XGBoost + SVM)** to classify trading signals as **Buy / Hold / Sell**.  
Outputs are exported to CSV for integration into **Power BI** dashboards.

> ⚠️ **Disclaimer**  
> This repository is for **educational and research purposes only**. It is **not** financial advice and must **not** be used directly for live trading or investment decisions.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Data & Features](#data--features)
- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Option 1 — Python Script](#option-1--python-script)
  - [Option 2 — Jupyter Notebook](#option-2--jupyter-notebook)
- [Power BI Integration](#power-bi-integration)
- [Repository Structure](#repository-structure)
- [Results & Evaluation](#results--evaluation)
- [Extending the Project](#extending-the-project)
- [Limitations](#limitations)
- [References](#references)
- [Contact](#contact)
- [License](#license)

---

## Overview

The **AI-Driven Trading Pattern Indicator** demonstrates how to:

1. Generate **synthetic historical price data** and technical indicators.
2. Build an **ensemble classifier** combining:
   - **XGBoost** (tree-based gradient boosting)
   - **Support Vector Machine (SVM)**  
3. Produce **trading signals** (`Buy`, `Hold`, `Sell`) that can be visualized in **Power BI** for monitoring signal quality, pattern distribution, and model behavior over time.

This project is ideal for:

- Data science learners exploring **financial time-series classification**.
- Developers who want a starting point for **trading signal research**.
- Analysts who want to build **Power BI dashboards** from ML outputs.

---

## Key Features

- 🧪 **Synthetic Market Data Generator**  
  - Creates artificial price/indicator datasets to experiment without using real market feeds.

- 🧮 **Feature Engineering & Preprocessing**  
  - Computes technical-indicator-style features (trend / momentum–like signals).  
  - Applies scaling and train/test splitting.

- 🤝 **Ensemble Model (XGBoost + SVM)**  
  - Combines strengths of gradient-boosted trees and margin-based classifiers via soft/hard voting.

- 📊 **Trading Signal Classification**  
  - Outputs class labels: `Buy`, `Hold`, `Sell` for each time step in the generated dataset.

- 📤 **Power BI-Ready Output**  
  - Saves predictions to `predictions_for_power_bi.csv` for downstream BI dashboards.

- 📓 **Code in Script + Notebook**  
  - Standalone Python script for batch runs.  
  - Jupyter Notebook for interactive experimentation.

---

## Project Architecture

At a high level, the pipeline consists of:

1. **Data Generation**
   - Synthetic time-series data mimicking stock-like behavior (e.g., price movement with noise).
   - Derived indicator-style features (e.g., rolling statistics, momentum-like features).

2. **Preprocessing**
   - Split into train/test sets.
   - Scaling / normalization of numeric features where required (especially for SVM).

3. **Modeling**
   - **XGBoost Classifier** for non-linear decision boundaries and interaction capture.
   - **SVM Classifier** to complement with margin-based decision surfaces.
   - Ensemble logic (e.g., majority or weighted voting) to obtain final class predictions.

4. **Export**
   - Predictions plus relevant metadata are written to `predictions_for_power_bi.csv`.

5. **Visualization (outside Python)**
   - Power BI imports the CSV and builds dashboards for:
     - Actual vs. predicted signals
     - Signal distribution
     - Model performance tracking over time

---

## Data & Features

> 💡 All data in this repository is **synthetic** and generated programmatically. It is **not** real market data.

Typical aspects of the synthetic dataset:

- **Inputs (features)**  
  While exact feature definitions are determined in the code, they conceptually include:
  - Price-like features (e.g., synthetic close price series).
  - Trend or momentum-style features (e.g., rolling means, differences, or ratio-style indicators).
  - Possibly volatility-style or smoothed statistics.

- **Target (label)**  
  - Multi-class label representing **trading action**:  
    - `1` → **Buy**  
    - `0` → **Hold**  
    - `-1` → **Sell**  
    (Exact encoding may vary slightly; check `trading_pattern_predictor.py` for implementation details.)

You can extend the generator to include **real technical indicators** such as Moving Average, RSI, or MACD if you wish to plug in real data sources later.

---

## Installation

### Prerequisites

- **Python** ≥ 3.8
- Recommended environment management:
  - [venv](https://docs.python.org/3/library/venv.html)
  - or [conda](https://docs.conda.io/en/latest/)

### Install Dependencies

From the root of the repository:

```bash
pip install pandas numpy scikit-learn xgboost
