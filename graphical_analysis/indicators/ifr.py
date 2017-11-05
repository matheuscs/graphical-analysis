
def find_ifr(stocks_data, period=14):
    labels = []
    ifr = []
    for k, df in stocks_data.items():
        labels = [str(x)[:10] for x in df.index.values]
        closes = df['Close'].values.tolist()
        last_close = closes[0]
        total_gain = 0
        total_loss = 0
        for c in closes[1:period+1]:
            var = c - last_close
            last_close = c
            if var > 0:
                total_gain += var
            elif var < 0:
                total_loss -= var
        average_gain = total_gain/period
        average_loss = total_loss/period
        if average_loss == 0:
            average_loss = 0.000000000001
        fr = average_gain/average_loss
        ifr.append(100-(100/(1+fr)))

        for i in range(period+1, len(closes)):
            c = closes[i]
            var = c - last_close
            last_close = c
            gain = 0
            loss = 0
            if var > 0:
                gain = var
            elif var < 0:
                loss = var
            average_gain = (average_gain * 13 + gain)/14
            average_loss = (average_loss * 13 - loss)/14
            if average_loss == 0:
                average_loss = 0.000000000001
            fr = average_gain/average_loss
            ifr.append(100-(100/(1+fr)))
    return labels[period:], ifr
