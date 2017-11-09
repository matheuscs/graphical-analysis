from graphics.patterns.bodies import find_long_upper_shadows


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
        result[k] = find_long_upper_shadows(df)

    # tbd
