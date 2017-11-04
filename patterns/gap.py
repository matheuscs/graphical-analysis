
def find_gaps(df):
    """

    :param df: pandas.DataFrame
    :return: indexes of the days after the gap
    """
    gaps = []
    last_index = None
    last_row = None
    for i, r in df.iterrows():
        if last_index is None:
            last_index = i
            last_row = r
            continue
        if r['Low'] > last_row['High'] or r['High'] < last_row['Low']:
            gaps.append([{last_index: last_row}, {i: r}])
        last_index = i
        last_row = r

    return gaps
