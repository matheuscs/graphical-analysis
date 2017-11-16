from graphics.patterns.candlesticks import candlestick_positioning, \
    candlestick_diff_value


def analyse_gaps(stocks_data):
    gaps = []
    for stock_symbol, df in stocks_data.items():
        previous_row = df.ix[0]
        for index in range(1, len(df)):
            current_row = df.ix[index]
            if abs(candlestick_positioning(previous_row, current_row)) == 5:
                diff = candlestick_diff_value(previous_row, current_row)
                gaps.append((df.index[index], diff))
            previous_row = current_row

        print('\n---GAP---')
        print(stock_symbol)
        [print('Date: {}, Difference: {:.2f}'.format(g[0], g[1])) for g in gaps]
