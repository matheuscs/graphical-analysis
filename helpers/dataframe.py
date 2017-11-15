import pandas as pd
import math


def previous_row(df, idx):
    i = 1
    while math.isnan(df.ix[pd.DatetimeIndex([idx]) -
            pd.DateOffset(days=i)]['Open']):
        i += 1
        if i >= 7:
            return None
    return df.ix[idx - pd.DateOffset(days=i)]


def next_row(df, idx):
    i = 1
    while math.isnan(df.ix[pd.DatetimeIndex([idx]) +
            pd.DateOffset(days=i)]['Open']):
        i += 1
        if i >= 7:
            return None
    return df.ix[idx + pd.DateOffset(days=i)]
