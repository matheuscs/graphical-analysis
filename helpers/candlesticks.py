
def get_body(row):
    if row['Close'] > row['Open']:
        max_body = row['Close']
        min_body = row['Open']
        body = max_body - min_body
    else:
        max_body = row['Open']
        min_body = row['Close']
        body = min_body - max_body
    return body, max_body, min_body


def get_top_shadow(row):
    if row['Close'] > row['Open']:
        return row['High'] - row['Close']
    else:
        return row['High'] - row['Open']


def get_bottom_shadow(row):
    if row['Close'] < row['Open']:
        return row['Close'] - row['Low']
    else:
        return row['Open'] - row['Low']
