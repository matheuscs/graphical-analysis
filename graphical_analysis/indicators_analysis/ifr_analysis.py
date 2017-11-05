import matplotlib.pyplot as plt


from graphical_analysis.indicators.ifr import find_ifr


def analyse_ifr(stocks_data):
    # tbd
    return find_ifr(stocks_data)


def plot_ifr(stocks_data, stock):
    closes = stocks_data[stock][['Close']]
    plt.subplot(211)
    plt.plot(closes)

    labels, ifr = find_ifr(stocks_data)
    plt.subplot(212)
    plt.plot(ifr)
    # plt.xlabel(labels)

    plt.show()
