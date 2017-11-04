from patterns.gap import find_gaps


def analyse(stocks_data):
    """

    :param stocks_data: dict; key: stock; value: stock DataFrame
    :return: TBD - result of the analysis
    """
    result = {}
    for k, df in stocks_data.items():
        result[k] = find_gaps(df)

    for stock_symbol, gaps in result.items():
        print('-------------------------')
        print(stock_symbol)
        for gap in gaps:
            print('-------------------------')
            k1 = list(gap[0].keys())[0]
            v1 = list(gap[0].values())[0]
            k2 = list(gap[1].keys())[0]
            v2 = list(gap[1].values())[0]
            gap_value = 0
            if v2['Low'] > v1['High']:
                gap_value = v2['Low'] - v1['High']
            elif v2['High'] < v1['Low']:
                gap_value = v2['High'] - v1['Low']
            print(k1, v1, k2, v2, gap_value)

    return result
