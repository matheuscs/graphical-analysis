import pandas as pd

from helpers.candlesticks import get_body, get_top_shadow, get_bottom_shadow


def find_big_bottom_bodies(df):
    """
    Candlestick pattern found in Shooting Star and Inverted Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: pandas dataframe containing only the big bottom bodies candlesticks
     found in the incoming df
    """
    big_bottom_bodies_indexes = []
    big_bottom_bodies = []
    for i, r in df.iterrows():
        body, max_body, min_body = get_body(r)
        top_shadow = get_top_shadow(r)
        bottom_shadow = get_bottom_shadow(r)
        if top_shadow > body * 2 and body > bottom_shadow * 4:
            big_bottom_bodies_indexes.append(i)
            big_bottom_bodies.append(r)

    return pd.DataFrame(big_bottom_bodies, index=big_bottom_bodies_indexes,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def find_big_top_bodies(df):
    """
    Candlestick pattern found in Hanging Man and Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: pandas dataframe containing only the big top bodies candlesticks
     found in the incoming df
    """
    big_top_bodies_indexes = []
    big_top_bodies = []
    for i, r in df.iterrows():
        body, max_body, min_body = get_body(r)
        top_shadow = get_top_shadow(r)
        bottom_shadow = get_bottom_shadow(r)
        if bottom_shadow > body * 2 and body > top_shadow * 4:
            big_top_bodies_indexes.append(i)
            big_top_bodies.append(r)

    return pd.DataFrame(big_top_bodies, index=big_top_bodies_indexes,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])
