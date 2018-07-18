from modules.candlesticks import candlestick_positioning
from modules.candlesticks import is_candlestick_positive


def analyse_engulfs(stocks_data):

    for stock_symbol, df in stocks_data.items():
        bullishs_engulf = []
        for i in range(1, len(df)):
            engulfeds = 0
            current_row = df.ix[i]
            for j in range(1, i):
                previous_row = df.ix[i - j]
                if is_candlestick_positive(previous_row) or \
                        not is_candlestick_positive(current_row) or \
                        candlestick_positioning(previous_row, current_row) != 1:
                    break
                engulfeds += 1
            if engulfeds > 0:
                bullishs_engulf.append((df.index[i], engulfeds))

        bearishs_engulf = []
        for i in range(1, len(df)):
            engulfeds = 0
            current_row = df.ix[i]
            for j in range(1, i):
                previous_row = df.ix[i - j]
                if not is_candlestick_positive(previous_row) or \
                        is_candlestick_positive(current_row) or \
                        candlestick_positioning(previous_row, current_row) != 1:
                    break
                engulfeds += 1
            if engulfeds > 0:
                bearishs_engulf.append((df.index[i], engulfeds))

        if len(bullishs_engulf) > 0:
            print('\n--- BULLISH ENGULFS ---')
            print(stock_symbol)
            [print('Date: {}, Engulfeds: {}'.format(e[0], e[1])) for e in bullishs_engulf]

        if len(bearishs_engulf) > 0:
            print('\n--- BEARISH ENGULFS ---')
            print(stock_symbol)
            [print('Date: {}, Engulfeds: {}'.format(e[0], e[1])) for e in bearishs_engulf]

