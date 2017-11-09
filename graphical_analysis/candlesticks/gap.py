from graphics.patterns.gaps import find_gaps


def analyse_gap(stocks_data):
    """

    :param stocks_data: {stock: stock DataFrame}
    :return: TBD - result of the analysis
    """
    result = {}
    for k, df in stocks_data.items():
        result[k] = find_gaps(df)

    for stock_symbol, df in result.items():
        print('-------------------------')
        print(stock_symbol)
        highs1 = df.iloc[0::2]['High']
        lows1 = df.iloc[0::2]['Low']
        highs2 = df.iloc[1::2]['High']
        lows2 = df.iloc[1::2]['Low']
        for i in range(len(highs1)):
            print('-------------------------')
            gap_value = 0
            if lows2[i] > highs1[i]:
                gap_value = lows2[i] - highs1[i]
            elif highs2[i] < lows1[i]:
                gap_value = highs2[i] - lows1[i]
            print(gap_value)

    return result
