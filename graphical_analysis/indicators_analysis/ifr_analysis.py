import matplotlib.pyplot as plt


from graphical_analysis.indicators.ifr import find_ifr


def analyse_ifr(stocks_data):
    result = {}
    for k, df in stocks_data.items():
        result[k] = find_ifr(df)
    print(result['BBAS3'])


def plot_ifr(stocks_data, stock):
    stock = stocks_data[stock]
    closes = stock[['Close']]
    plt.subplot(211)
    plt.plot(closes)

    labels, ifr = find_ifr(stock)
    plt.subplot(212)
    plt.plot(ifr)
    # plt.xlabel(labels)

    plt.show()
