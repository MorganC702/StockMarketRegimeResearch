# """
# File:         stationarity_tests.py
# Description:  
# Author:       Morgan Cooper
# Created:      2025-09-04
# Updated:      2025-09-04
# Usage:        N/A  

# Notes:
# Stationarity means that the statistical properties of a time series i.e. mean, variance 
# and covariance do not change over time. Many statistical models require the series to be 
# stationary to make effective and precise predictions.

# Two statistical tests would be used to check the stationarity of a time series:

# 1) Augmented Dickey Fuller (“ADF”) test 
# 2) Kwiatkowski-Phillips-Schmidt-Shin (“KPSS”) test.

# Partial code aquired from:
# https://www.statsmodels.org/stable/examples/notebooks/generated/stationarity_detrending_adf_kpss.html
# """

import warnings
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

def adf_test(timeseries, verbose: bool = False):
    s = pd.Series(timeseries).astype(float)
    s = s.replace([np.inf, -np.inf], np.nan).dropna()
    # constant series => ADF will return nan; treat as stationary for ADF side
    if s.nunique() < 2 or s.std(ddof=0) == 0:
        return pd.Series(
            {"Test Statistic": 0.0, "p-value": 1.0, "#Lags Used": 0.0, "Number of Observations Used": float(len(s))}
        )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        dftest = adfuller(s, autolag="AIC")
    return pd.Series(
        dftest[0:4],
        index=["Test Statistic", "p-value", "#Lags Used", "Number of Observations Used"],
    )

def kpss_test(timeseries, verbose: bool = False):
    s = pd.Series(timeseries).astype(float)
    s = s.replace([np.inf, -np.inf], np.nan).dropna()
    # constant / nearly constant => treat as stationary for KPSS side
    if s.nunique() < 2 or s.std(ddof=0) == 0:
        return pd.Series({"Test Statistic": 0.0, "p-value": 1.0, "Lags Used": 0})

    n = len(s)
    # safe fixed nlags instead of 'auto' to avoid overflow in autolag
    nlags = min(int(np.sqrt(n)), n - 1)

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            stat, pval, lags, crit = kpss(s, regression="c", nlags=nlags)
    except Exception:
        # last-resort fallback
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            stat, pval, lags, crit = kpss(s, regression="c", nlags="legacy")

    out = pd.Series({"Test Statistic": stat, "p-value": pval, "Lags Used": lags})
    return out

def test_stationarity(series: pd.Series, name: str, alpha: float = 0.05) -> dict:
    s = pd.Series(series).astype(float)
    if s.isna().any():
        raise ValueError("Input series contains NaNs")
    s = s.replace([np.inf, -np.inf], np.nan).dropna()

    adf_res = adf_test(s)
    kpss_res = kpss_test(s)

    adf_stationary = (adf_res["p-value"] < alpha) if not np.isnan(adf_res["p-value"]) else False
    kpss_stationary = (kpss_res["p-value"] > alpha) if not np.isnan(kpss_res["p-value"]) else False

    return {name: {"stationary": bool(adf_stationary and kpss_stationary)}}
    