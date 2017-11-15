from graphics.patterns.bodies import does_body_engulf
from helpers.dataframe import previous_row


def analyse_bullish_engulfing(stocks_data):
    """
    Bullish Engulfing definition:
        - 2 candles, first is negative, second is positive
        - second engulfs the first body, not necessarily the shadows

    Higher significance factors:
        - Size matters, bigger the second is to the first better it is
        - Number matters, bigger the previous candles engulfed better it is
        - Higher volume than previous candlestick
        - Upward movement
        - Over a support area

    Conclusion:
        - Reversal of movement
        - Buy signal
    """

    result = {}
    for k, df in stocks_data.items():
        for i, r in df.iterrows():
            print(df)
            # r0 = previous_row(df, i)
            # r1 = df.ix[i]
            # if does_body_engulf(r0, r1):
            #     pass

    # print('--- BULLISH ENGULFING ---')
    # print(result)

