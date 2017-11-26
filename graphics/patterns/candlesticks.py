
def _get_body_size(row):
    if is_candlestick_positive(row):
        return row['Close'] - row['Open']
    else:
        return row['Open'] - row['Close']


def _get_upper_shadow_size(row):
    if is_candlestick_positive(row):
        return row['High'] - row['Close']
    else:
        return row['High'] - row['Open']


def _get_lower_shadow_size(row):
    if is_candlestick_positive(row):
        return row['Open'] - row['Low']
    else:
        return row['Close'] - row['Low']


def _get_candlestick_values(row):
    if is_candlestick_positive(row):
        max_body = row['Close']
        min_body = row['Open']
    else:
        max_body = row['Open']
        min_body = row['Close']
    return max_body, min_body, row['High'], row['Low']


def is_candlestick_positive(row):
    return row['Close'] > row['Open']


def find_long_upper_shadows(df):
    """
    Candlestick pattern found in Shooting Star and Inverted Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: indexes of the long upper shadows candlesticks found in the df
    """
    indexes = []
    index = 0
    for dfi, row in df.iterrows():
        body = _get_body_size(row)
        top_shadow = _get_upper_shadow_size(row)
        bottom_shadow = _get_lower_shadow_size(row)
        if top_shadow > body * 2 and body > bottom_shadow:
            indexes.append((index, dfi))

    return indexes


def find_long_lower_shadows(df):
    """
    Candlestick pattern found in Hanging Man and Hammer

    :param df: pandas dataframe with a long period to be analysed
    :return: indexes of the long lower shadows candlesticks found in the df
    """
    indexes = []
    index = 0
    for dfi, row in df.iterrows():
        body = _get_body_size(row)
        top_shadow = _get_upper_shadow_size(row)
        bottom_shadow = _get_lower_shadow_size(row)
        if bottom_shadow > body * 2 and body > top_shadow:
            indexes.append((index, dfi))
        index += 1

    return indexes


def candlestick_positioning(row0, row1):
    """

    :param row0:
    :param row1:
    :return:
    0: if can't be determined
    1: body 0 engulfs body 1
    2: body 0 invades body 1
    3: body 0 invades shadow 1 or shadow 0 invades body 1
    4: shadow 0 invades shadow 1
    5: gap
    negative values if negative movement
    """
    if row0 is None or row1 is None:
        return 0

    max_body0, min_body0, max_shadow0, min_shadow0 = _get_candlestick_values(row0)
    max_body1, min_body1, max_shadow1, min_shadow1 = _get_candlestick_values(row1)

    # engulfs
    if max_body0 <= max_body1 and min_body0 >= min_body1:
        return 1
    elif max_body0 >= max_body1 and min_body0 <= min_body1:
        return -1

    # body invasion
    elif min_body0 < min_body1 < max_body0 < max_body1:
        return 2
    elif max_body0 > max_body1 > min_body0 > min_body1:
        return -2

    # body-shadow invasion
    elif max_shadow0 >= min_body1 >= max_body0 or min_body1 >= max_body0 >= min_shadow1:
        return 3
    elif min_shadow0 <= max_body1 <= min_body0 or max_body1 <= min_body0 <= max_shadow1:
        return -3

    # shadow invasion
    elif max_body0 <= min_shadow1 <= max_shadow0:
        return 4
    elif max_body1 <= min_shadow0 <= max_shadow1:
        return -4

    # gap
    elif min_shadow0 < min_shadow1 > max_shadow0:
        return 5
    elif min_shadow1 < min_shadow0 > max_shadow1:
        return -5

    return 0  # should never ever occur


def candlestick_gap_value(row0, row1):
    if row0 is None or row1 is None:
        return 0

    max_body0, min_body0, max_shadow0, min_shadow0 = _get_candlestick_values(row0)
    max_body1, min_body1, max_shadow1, min_shadow1 = _get_candlestick_values(row1)

    if min_shadow0 > max_shadow1:
        return min_shadow0 - max_shadow1
    elif min_shadow1 > max_shadow0:
        return min_shadow1 - max_shadow0

    return 0
