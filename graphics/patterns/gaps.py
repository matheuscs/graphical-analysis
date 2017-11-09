import pandas as pd


def find_gaps(df):
    """

    :param df: pandas.DataFrame
    :return: indexes of the days after the gap
    """
    gaps_indexes = []
    gaps = []
    last_index = None
    last_row = None
    for i, r in df.iterrows():
        if last_index is None:
            last_index = i
            last_row = r
            continue
        if r['Low'] > last_row['High'] or r['High'] < last_row['Low']:
            gaps_indexes.append(last_index)
            gaps_indexes.append(i)
            gaps.append(last_row)
            gaps.append(r)
        last_index = i
        last_row = r

    return pd.DataFrame(gaps, index=gaps_indexes,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])
