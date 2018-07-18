
def get_total_stock_volume(df, period=20):
    volumes = df['Volume'].values.tolist()
    total_volume = 0
    for volume in volumes[1:period+1]:
        total_volume += volume
    return total_volume


def get_total_money_volume(df, period=20):
    volumes = df['Volume'].values.tolist()
    closes = df['Close'].values.tolist()
    total_money_volume = 0
    i = 0
    for volume in volumes[1:period+1]:
        total_money_volume += volume * closes[i]
        i += 1
    return total_money_volume
