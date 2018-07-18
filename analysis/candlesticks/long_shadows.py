from modules.candlesticks import candlestick_positioning
from modules.candlesticks import find_long_lower_shadows
from modules.candlesticks import find_long_upper_shadows


def _get_significance(df, index):
    previous_row = df.ix[index-1]
    current_row = df.ix[index]
    if index + 1 == len(df):
        next_row = None
    else:
        next_row = df.ix[index+1]

    significance = 0
    pos = candlestick_positioning(previous_row, current_row)
    significance += pos
    pos = candlestick_positioning(current_row, next_row)
    significance -= pos
    return significance


def analyse_long_shadows(stocks_data, min_significance=3):
    for stock_symbol, df in stocks_data.items():
        hammers = []
        hanging_men = []
        for index, df_index in find_long_lower_shadows(df):
            significance = _get_significance(df, index)
            if -significance > min_significance:
                hammers.append((df_index, -significance))
            if significance > min_significance:
                hanging_men.append((df_index, significance))

        inverted_hammers = []
        shooting_stars = []
        for index, df_index in find_long_upper_shadows(df):
            significance = _get_significance(df, index)
            if -significance > min_significance:
                inverted_hammers.append((df_index, -significance))
            if significance > min_significance:
                shooting_stars.append((df_index, significance))

        if len(hammers) > min_significance:
            print('\n--- HAMMERS ---')
            print(stock_symbol)
            [print('Date: {}, Significance: {}'.format(h[0], h[1])) for h in hammers]

        if len(hanging_men) > 0:
            print('\n--- HANGING MEN ---')
            print(stock_symbol)
            [print('Date: {}, Significance: {}'.format(h[0], h[1])) for h in hanging_men]

        if len(inverted_hammers) > 0:
            print('\n--- INVERTED HAMMERS ---')
            print(stock_symbol)
            [print('Date: {}, Significance: {}'.format(h[0], h[1])) for h in inverted_hammers]

        if len(shooting_stars) > 0:
            print('\n--- SHOOTING STARS ---')
            print(stock_symbol)
            [print('Date: {}, Significance: {}'.format(h[0], h[1])) for h in shooting_stars]

