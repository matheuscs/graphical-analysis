from graphics.patterns.candlesticks import candlestick_positioning, \
    candlestick_body_diff
from graphics.patterns.candlesticks import is_candlestick_positive


def analyse_threes(stocks_data):

    for stock_symbol, df in stocks_data.items():
        morning_stars = []
        for i in range(2, len(df)):
            current_row = df.ix[i]
            previous_row = df.ix[i - 1]
            preprevious_row = df.ix[i - 2]
            diff_pos1 = candlestick_positioning(previous_row, current_row)
            diff_pos2 = candlestick_positioning(preprevious_row, current_row)
            diff_pos3 = candlestick_positioning(preprevious_row, previous_row)
            diff_val1 = candlestick_body_diff(previous_row, current_row)
            diff_val2 = candlestick_body_diff(previous_row, preprevious_row)
            if is_candlestick_positive(current_row) and \
                    not is_candlestick_positive(preprevious_row) and \
                    diff_pos1 >= 2 and diff_pos2 == -2 and diff_pos3 <= -3 and \
                    diff_val1 > 2 and diff_val2 > 4:
                morning_stars.append((df.index[i], diff_pos1-diff_pos3))

        if len(morning_stars) > 0:
            print('\n--- MORNING STARS ---')
            print(stock_symbol)
            [print('Date: {}, Significance: {}'.format(m[0], m[1])) for m in morning_stars]

