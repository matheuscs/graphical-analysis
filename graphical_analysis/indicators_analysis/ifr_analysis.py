import matplotlib.pyplot as plt


from graphical_analysis.indicators.ifr import find_ifr


def analyse_ifr(stocks_data):
    labels, ifr = find_ifr(stocks_data)
    # print(stocks_data)
    plt.plot(ifr)
    # plt.xlabel(labels)
    plt.show()
