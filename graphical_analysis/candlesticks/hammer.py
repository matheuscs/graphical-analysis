from graphics.patterns.candlesticks import find_long_lower_shadows
from graphics.patterns.candlesticks import candlestick_positioning


def analyse_hammers(stocks_data):
    """
    Hammer definition:
        - Long lower shadow
        - Downward movement

    Higher significance factors:
        - Upward trend
        - Over a support area
        - Higher volume than previous candlestick

    Next candlestick:
        - Positive
        - Opening higher than hammers body

    Conclusion:
        - Reversal of movement
        - Buy signal
    """

    for stock_symbol, df in stocks_data.items():
        hammers = []
        hammers_indexes = find_long_lower_shadows(df)
        for index, df_index in hammers_indexes:
            previous_row = df.ix[index-1]
            current_row = df.ix[index]
            if index + 1 == len(df):
                next_row = None
            else:
                next_row = df.ix[index+1]

            significance = 0
            pos = candlestick_positioning(previous_row, current_row)
            significance -= pos
            pos = candlestick_positioning(current_row, next_row)
            significance += pos

            if significance >= 0:
                hammers.append((df_index, significance))

        print('\n--- HAMMER ---')
        print(stock_symbol)
        [print('Date: {}, Significance: {}'.format(h[0], h[1])) for h in hammers]
