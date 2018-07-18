from graphics.indicators.volume import get_total_money_volume


def analyse_volume(stocks_data, period=20):
    volumes = {}
    for stock_symbol, df in stocks_data.items():
        volumes[stock_symbol] = get_total_money_volume(df) / period

    sorted_volumes = [(k, volumes[k]) for k in sorted(
        volumes, key=volumes.get, reverse=True)]

    print(f'\n--- VOLUME AVAREGES FOR {period} DAYS---')
    [print('{},\tVolume: {:,}'.format(s, v)) for s, v in sorted_volumes]

