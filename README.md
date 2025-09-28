# Predicting Market Regimes for the S&P 500

A research project exploring machine learning methods to **predict market regimes** using a combination of:

- **Macroeconomic indicators from FRED.gov**

- **Foreign Currencies data from Yahoo Finance (yfinance)**

- **Historical data for the S&P 500 from Polygon.io**

---

## Overview

This repository contains research code for downloading data, cleaning data, feature engineering and feature reduction along with mahcine learning experiments aimed at forecasting **future market regimes** defined by combinations of return distributions and volatility measures.

Key goals:
- Predict the **S&P 500 regime t+3 days ahead**.
- Compare and ensemble multiple models (K-Nearest Neighbors, Support Vector Machine, Random Forrest, etc.).
- Analyze confidence and performance overall and across different regime types.

---

## Methodology

1. **Data Collection**
   - Economic data (e.g. Fed, macro series, etc.)
   - S&P 500 market data from Polygon.io
   - Foreign currency data from Yahoo Finance (yfinance) 

2. **Feature Engineering**
   - Rolling windows and lagged features
   - Regime labeling 
   - Normalization / Stationarity conversion
   - Feature reduction techniques

3. **Modeling Approach**
   - Baseline models: XGBoost, Random Forest, Extra Trees, MLP, Logistic Regression, Support Vector Classifier, Linear Discriminate Analysis, K-Nearest Neighbors
   - Ensemble: Soft voting + weight optimization

4. **Evaluation**
   - Accuracy, AUC
   - Confusion matrix for regime class accuracy
   - Confidence decile analysis

---

## Project Structure

project/
├── data/ # datasets & data processing 
├── models/ # baseline models and ensemble model
├── utils/ # Stationarity test function
├── results/ # evaluation outputs, confusion matrices
└── README.md

---

## Process for running the code:

**Handle requirements:** "pip install requirements.txt"

**Run files in the following order:**

**note:** Must have a polygon account to download SPY tcker data (data is included in repo so no need to redownload). 

### Data Processing

1. /data/data_processing/***download_data.ipynb***
2. /data/data_processing/***merge_data.ipynb***
3. /data/data_processing/***clean_data.ipynb***
4. /data/data_processing/***eda_&_fe.ipynb***

### Modeling

5. /models/***extra_tree.ipynb***
6. /models/***knn.ipynb***
7. /models/***knn.ipynb***
8. /models/***lda.ipynb***
9. /models/***mlp.ipynb***
10. /models/***random_forrest.ipynb***
11. /models/***svc.ipynb***
12. /models/***xgb.ipynb***
13. /models/***ensemble.ipynb***

**Results saved in results directory**


TO DO: 

## Sources

(Add sources here)

## License

(Add license details here)

## Citation

(Add citation details here)