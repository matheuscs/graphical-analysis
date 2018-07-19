from unittest.mock import patch
from unittest import TestCase
import pandas as pd
import ast


class TestMock(TestCase):

    @patch('stocks.my_request.get_stock_data')
    def test_stock_data(self, mock_get_stock_data):
        with open(r'../data/mock_data_bbas3_1y.txt') as d:
            data = ast.literal_eval(d.read())
        with open(r'../data/mock_index_bbas3_1y.txt') as i:
            index = ast.literal_eval(i.read())
        with open(r'../data/mock_dataframe_bbas3_1y.txt') as df:
            dataframe = df.read()
        stock_data = pd.DataFrame(
            data,
            index=index,
            columns=['Open', 'High', 'Low', 'Close', 'Volume']
        )
        self.assertEqual(str(stock_data), dataframe)
        mock_get_stock_data.return_value = stock_data
        self.assertEqual(mock_get_stock_data('BBAS3', '1Y'), stock_data)
