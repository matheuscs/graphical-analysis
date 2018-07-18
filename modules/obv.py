
def find_obv(df):
    closes = df['Close'].values.tolist()
    volumes = df['Volume'].values.tolist()
    last_close = closes[0]
    obv = [0]
    cont = 0
    for c in closes:
        if c > last_close:
            obv.append(obv[-1] + volumes[cont])
        else:
            obv.append(obv[-1] - volumes[cont])
        last_close = c
        cont += 1
    return obv
