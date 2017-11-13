import pandas as pd

from graphics.candlesticks.body import get_body
from graphics.candlesticks.body import get_upper_shadow, get_lower_shadow


def find_long_upper_shadows(df):
    """
    Candlestick pattern found in Shooting Star and Inverted Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: pandas dataframe containing only the lower small bodies
     candlesticks found in the incoming df
    """
    indexes = []
    bodies = []
    for i, r in df.iterrows():
        body, max_body, min_body = get_body(r)
        top_shadow = get_upper_shadow(r)
        bottom_shadow = get_lower_shadow(r)
        if top_shadow > body * 2 and body > bottom_shadow * 4:
            indexes.append(i)
            bodies.append(r)

    return pd.DataFrame(bodies, index=indexes,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def find_long_lower_shadows(df):
    """
    Candlestick pattern found in Hanging Man and Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: pandas dataframe containing only the upper big bodies candlesticks
     found in the incoming df
    """
    indexes = []
    bodies = []
    for i, r in df.iterrows():
        body, max_body, min_body = get_body(r)
        top_shadow = get_upper_shadow(r)
        bottom_shadow = get_lower_shadow(r)
        if bottom_shadow > body * 2 and body > top_shadow * 4:
            indexes.append(i)
            bodies.append(r)

    return pd.DataFrame(bodies, index=indexes,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def is_body_higher_than(r0, r1):
    """

    :param r0: first row to analyse
    :param r1: second row to analyse
    :return: true if min(r0.open, r0.close) > max(r1.open, r1.close)
    """
    body0, max_body0, min_body0 = get_body(r0)
    body1, max_body1, min_body1 = get_body(r1)
    return min_body0 > max_body1
