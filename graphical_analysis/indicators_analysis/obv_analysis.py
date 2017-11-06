import matplotlib.pyplot as plt

from graphical_analysis.indicators.obv import find_obv


def analyse_obv(stocks_data):
    """

    :param stocks_data: dict; key: stock; value: stock DataFrame
    :return: TBD - result of the analysis
    """
    result = {}
    for k, df in stocks_data.items():
        result[k] = find_obv(df)

    # tbd


def plot_obv(stocks_data, stock):
    closes = stocks_data[stock][['Close']]
    plt.subplot(211)
    plt.plot(closes)

    obv = find_obv(stocks_data[stock])
    print(obv)
    plt.subplot(212)
    plt.plot(obv)
    # plt.xlabel(labels)

    plt.show()
