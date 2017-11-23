from stocks.my import read_stocks_data, update_db_from_request

if __name__ == '__main__':
    update_db_from_request('1w')
    read_stocks_data()
