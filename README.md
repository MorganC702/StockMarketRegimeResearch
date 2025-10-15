# Predicting Market Regimes for the S&P 500

A research project exploring machine learning methods to **predict market regimes** using a combination of:

- **Macroeconomic indicators from FRED.gov.**

- **Foreign Currencies data from Yahoo Finance (yfinance)/**

- **Historical data for the S&P 500 from Polygon.io.**

---

## Overview

This repository contains research code for downloading data, cleaning data, feature engineering and feature reduction, along with machine learning experiments aimed at forecasting **future market regimes** defined by combinations of return distributions and volatility measures.


Key goals:
- Predict the **S&P 500 regime t+3 days ahead**.
- Compare and ensemble multiple models (K-Nearest Neighbors, Support Vector Machine, Random Forrest, etc.).
- Analyze confidence and performances across models.

---

## Methodology

1. **Data Collection**
   - Economic data (e.g. Fed, macro series, etc.)
   - S&P 500 market data from Polygon.io
   - Foreign currency data from Yahoo Finance (yfinance) 

2. **Feature Engineering**
   - Rolling windows and lagged features
   - Regime labeling 
   - Normalization & Stationarity conversion
   - Feature reduction techniques

3. **Modeling Approach**
   - Baseline models: XGBoost, Random Forest, Extra Trees, Multi-Layer-Perceptron, Logistic Regression, Support Vector Classifier, Linear Discriminate Analysis, K-Nearest Neighbors
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

**Handle requirements:** "pip install -r requirement.txt"

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
7. /models/***lda.ipynb*** 
8. /models/***log_reg.ipynb***
9. /models/***mlp.ipynb***
10. /models/***random_forrest.ipynb***
11. /models/***svc.ipynb***
12. /models/***xgb.ipynb***
13. /models/***ensemble.ipynb***


**Intermediat results saved in results directory**

1. /Results/

## Key Ensemble Results
- Ensemble model achieved **AUC ≈ 0.6863** on test data.
- Confidence decile analysis shows strong calibration in top 25% predictions.
- Ensemble model achieved **Accuracy ≈ 0.3158** on test data.
--- 

### Recommended Citation: 
Cooper, Morgan (2025). Market Regime Prediction using Ensemble Learning and Macroeconomic Signals. GitHub repository.
https://github.com/MorganC702/MarketRegimeResearch

---

## License
This project is released under the MIT License. See LICENSE file for details.
 
---

## Resources

U.S. Energy Information Administration, Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma [DCOILWTICO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DCOILWTICO, October 13, 2025.

U.S. Energy Information Administration, Crude Oil Prices: Brent - Europe [DCOILBRENTEU], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DCOILBRENTEU, October 13, 2025.

U.S. Energy Information Administration, Henry Hub Natural Gas Spot Price [DHHNGSP], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DHHNGSP, October 13, 2025.

University of Michigan, University of Michigan: Consumer Sentiment [UMCSENT], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/UMCSENT, October 13, 2025.

U.S. Census Bureau and U.S. Bureau of Economic Analysis, Trade Balance: Goods and Services, Balance of Payments Basis [BOPGSTB], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/BOPGSTB, October 13, 2025.

U.S. Bureau of Economic Analysis, Balance on current account [IEABC], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/IEABC, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Nominal Broad U.S. Dollar Index [DTWEXBGS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DTWEXBGS, October 13, 2025.

U.S. Bureau of Economic Analysis, Imports of Goods and Services [IMPGS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/IMPGS, October 13, 2025.

U.S. Bureau of Economic Analysis, Net Exports of Goods and Services [NETEXP], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/NETEXP, October 13, 2025.

Federal Reserve Bank of Atlanta, GDPNow Project [GDPNOW], retrieved from Atlanta Fed, https://www.atlantafed.org/cqer/research/gdpnow, October 13, 2025.

U.S. Bureau of Economic Analysis, Real Gross Domestic Product [GDPC1], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/GDPC1, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Industrial Production: Total Index [INDPRO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/INDPRO, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Industrial Production: Total Index [INDPRO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/INDPRO, October 13, 2025.

U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S. City Average [CPIAUCSL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CPIAUCSL, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Capacity Utilization: Total Index [TCU], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/TCU, October 13, 2025.

U.S. Census Bureau, Advance Retail Sales: Retail Trade [RSXFS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/RSXFS, October 13, 2025.

Federal Reserve Bank of Chicago, Chicago Fed National Activity Index [CFNAI], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CFNAI, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Federal Funds Effective Rate [DFF], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DFF, October 13, 2025.

U.S. Census Bureau and U.S. Department of Housing and Urban Development, New Privately-Owned Housing Units Started: Total Units [HOUST], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/HOUST, October 13, 2025.

National Association of Realtors, Existing Home Sales [EXHOSLUSM495S], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/EXHOSLUSM495S, October 13, 2025.

U.S. Census Bureau and U.S. Department of Housing and Urban Development, New One Family Houses Sold: United States [HSN1F], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/HSN1F, October 13, 2025.

S&P Dow Jones Indices LLC, S&P CoreLogic Case-Shiller 20-City Composite Home Price Index [SPCS20RSA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/SPCS20RSA, October 13, 2025.

U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S. City Average [CPIAUCSL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CPIAUCSL, October 13, 2025.

Federal Reserve Bank of Atlanta, Sticky Price Consumer Price Index less Food and Energy [CORESTICKM159SFRBATL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CORESTICKM159SFRBATL, October 13, 2025.

U.S. Bureau of Labor Statistics, Producer Price Index by Commodity: All Commodities [PPIACO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PPIACO, October 13, 2025.

U.S. Bureau of Economic Analysis, Personal Consumption Expenditures: Chain-type Price Index [PCEPI], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PCEPI, October 13, 2025.

U.S. Bureau of Labor Statistics, Import Price Index (End Use): All Commodities [IR], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/IR, October 13, 2025.

Federal Reserve Bank of New York, Effective Federal Funds Rate [EFFR], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/EFFR, October 13, 2025.

Federal Reserve Bank of New York, Overnight Bank Funding Rate [OBFR], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/OBFR, October 13, 2025.

Board of Governors of the Federal Reserve System (US), 3-Month Treasury Bill Secondary Market Rate, Discount Basis [DTB3], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DTB3, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at 1-Year Constant Maturity, Quoted on an Investment Basis [DGS1], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS1, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity, Quoted on an Investment Basis [DGS2], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS2, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at 5-Year Constant Maturity, Quoted on an Investment Basis [DGS5], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS5, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis [DGS10], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS10, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at 30-Year Constant Maturity, Quoted on an Investment Basis [DGS30], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DGS30, October 13, 2025.

Federal Reserve Bank of St. Louis, 10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity [T10Y2Y], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/T10Y2Y, October 13, 2025.

Federal Reserve Bank of St. Louis, 10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity [T10Y3M], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/T10Y3M, October 13, 2025.

Moody’s, Moody's Seasoned Baa Corporate Bond Yield [DBAA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DBAA, October 13, 2025.

Moody’s, Moody's Seasoned Aaa Corporate Bond Yield [DAAA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DAAA, October 13, 2025.

Ice Data Indices, LLC, ICE BofA US High Yield Index Option-Adjusted Spread [BAMLH0A0HYM2], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/BAMLH0A0HYM2, October 13, 2025.

U.S. Bureau of Labor Statistics, Unemployment Rate [UNRATE], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/UNRATE, October 13, 2025.

U.S. Bureau of Labor Statistics, Labor Force Participation Rate [CIVPART], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CIVPART, October 13, 2025.

U.S. Bureau of Labor Statistics, All Employees, Total Nonfarm [PAYEMS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PAYEMS, October 13, 2025.

U.S. Bureau of Labor Statistics, Average Weekly Hours of All Employees, Total Private [AWHAETP], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/AWHAETP, October 13, 2025.

U.S. Bureau of Labor Statistics, Average Hourly Earnings of All Employees, Total Private [CES0500000003], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CES0500000003, October 13, 2025.

U.S. Employment and Training Administration, Initial Claims [ICSA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/ICSA, October 13, 2025.

U.S. Employment and Training Administration, Continued Claims (Insured Unemployment) [CCSA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CCSA, October 13, 2025.

U.S. Bureau of Labor Statistics, Job Openings: Total Nonfarm [JTSJOL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/JTSJOL, October 13, 2025.

Chicago Board Options Exchange, CBOE Volatility Index: VIX [VIXCLS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/VIXCLS, October 13, 2025.

Federal Reserve Bank of St. Louis, TED Spread (DISCONTINUED) [TEDRATE], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/TEDRATE, October 13, 2025.

Federal Reserve Bank of St. Louis, St. Louis Fed Financial Stress Index [STLFSI4], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/STLFSI4, October 13, 2025.

Board of Governors of the Federal Reserve System (US), M1 [M1SL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/M1SL, October 13, 2025.

Board of Governors of the Federal Reserve System (US), M2 [M2SL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/M2SL, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Monetary Base: Total [BOGMBASE], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/BOGMBASE, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Assets: Total Assets: Total Assets (Less Eliminations from Consolidation): Wednesday Level [WALCL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/WALCL, October 13, 2025.

Board of Governors of the Federal Reserve System (US), Commercial and Industrial Loans, All Commercial Banks [TOTCI], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/TOTCI, October 13, 2025.

Federal Reserve Bank of Philadelphia, Large Bank Consumer Credit Card Balances: Total Balances [RCCCBBALTOT], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/RCCCBBALTOT, October 13, 2025.

Polygon.io, S&P 500 ETF (SPY) Historical Market Data [SPY], retrieved via Polygon.io API; https://polygon.io, October 13, 2025.

Yahoo Finance, Foreign Exchange Historical Data (AUD/USD, EUR/USD, GBP/USD, NZD/USD, USD/CAD, USD/CHF, USD/JPY, USD/SEK), retrieved via Yahoo Finance API; https://finance.yahoo.com, October 13, 2025.

OpenAI, ChatGPT (GPT-5). Used for generating, refining, and documenting Python code throughout the project; retrieved from https://chat.openai.com, October 13, 2025.
