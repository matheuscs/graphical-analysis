import matplotlib.pyplot as plt

from graphics.indicators.rsi import find_rsi


def analyse_rsi(stocks_data):
    """
    Layer of abstraction tha eventually will analyse a rsi

    :param stocks_data: {stock: stock DataFrame}
    """
    result = {}
    for k, df in stocks_data.items():
        result[k] = find_rsi(df)
    print(result['BBAS3'])


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
