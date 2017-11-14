from graphics.patterns.bodies import find_long_lower_shadows
from graphics.patterns.bodies import is_body_higher_than
from helpers.dataframe import previous_row, next_row


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

    result = {}
    for k, df in stocks_data.items():
        df_hm = find_long_lower_shadows(df)
        for i, r in df_hm.iterrows():
            r0 = previous_row(df, i)
            r1 = df.ix[i]
            r2 = next_row(df, i)
            # dowward movement and next cs higher
            if is_body_higher_than(r0, r1) and is_body_higher_than(r2, r1):
                result[k] = i

    print('--- HAMMER ---')
    print(result)
