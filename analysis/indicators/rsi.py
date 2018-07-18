import matplotlib.pyplot as plt

from graphics.indicators.rsi import find_rsi


def analyse_rsi(stocks_data, oversold=25, overbought=85):
    """
    Layer of abstraction tha eventually will analyse a rsi

    :param stocks_data: {stock: stock DataFrame}
    :param oversold:
    :param overbought:
    """
    print('\n--- RSI ANALYSIS ---')
    for stock_symbol, df in stocks_data.items():
        rsi = find_rsi(df)
        min_rsi = oversold
        max_rsi = overbought
        for i in range(len(rsi[1])):
            r = rsi[1][i]
            if r < min_rsi:
                min_rsi = r
            elif r > max_rsi:
                max_rsi = r

        mins = []
        maxs = []
        for i in range(len(rsi[1])):
            r = rsi[1][i]
            if r <= min_rsi * 1.2:
                mins.append((rsi[0][i], rsi[1][i]))
            elif r >= max_rsi * 0.95:
                maxs.append((rsi[0][i], rsi[1][i]))

        if mins:
            print(stock_symbol)
            [print(m[0], m[1]) for m in mins]
        if maxs:
            print(stock_symbol)
            [print(m[0], m[1]) for m in maxs]


def plot_rsi(stocks_data, stock):
    """
    A visual way to inspect the rsi analysis

    :param stock: a single stock symbol
    :param stocks_data: {stock: stock DataFrame}
    """
    stock = stocks_data[stock]
    closes = stock['Close'].values
    plt.subplot(211)
    plt.plot(closes)

    labels, ifr = find_rsi(stock)
    plt.subplot(212)
    plt.plot(ifr)
    # plt.xlabel(labels)

    plt.show()
