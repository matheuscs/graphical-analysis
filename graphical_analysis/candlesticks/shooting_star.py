from graphics.patterns.bodies import find_long_upper_shadows
from graphics.patterns.bodies import is_body_higher_than_or_equal_to
from helpers.dataframe import previous_row, next_row


def analyse_shooting_stars(stocks_data):
    """
    Shooting star definition:
        - Long upper shadow
        - Upward movement

    Higher significance factors:
        - Downward trend
        - Under a resistance area
        - Higher volume than previous candlestick

    Next candlestick:
        - Negativa
        - Opening lower than shooting star body

    Conclusion:
        - Reversal of movement
        - Sell signal
    """

    result = {}
    for k, df in stocks_data.items():
        df_hm = find_long_upper_shadows(df)
        for i, r in df_hm.iterrows():
            r0 = previous_row(df, i)
            r1 = df.ix[i]
            r2 = next_row(df, i)
            # upward movement and next cs lower
            if is_body_higher_than_or_equal_to(r1, r0) and \
                    is_body_higher_than_or_equal_to(r1, r2):
                result[k] = i

    print('--- SHOOTING STAR ---')
    print(result)

