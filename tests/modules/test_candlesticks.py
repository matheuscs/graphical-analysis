from unittest import TestCase
import pandas as pd
import ast

import modules.candlesticks as cs


class TestCandlesticks(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Preparing stock data with a valid mocked dataframe.
        """
        with open(r'tests/data/mock_data_bbas3_30d.txt') as d:
            data_30d = ast.literal_eval(d.read())
        with open(r'tests/data/mock_index_bbas3_30d.txt') as i:
            index_30d = ast.literal_eval(i.read())
        with open(r'tests/data/mock_dataframe_bbas3_30d.txt') as df:
            dataframe_30d = df.read()
        cls.stock_data_30d = pd.DataFrame(
            data_30d,
            index=index_30d,
            columns=['Open', 'High', 'Low', 'Close', 'Volume']
        )
        assert str(cls.stock_data_30d) == dataframe_30d

    def test_long_upper_shadows(self):
        self.assertListEqual(cs.find_long_upper_shadows(self.stock_data_30d),
                             [(0, '2018-06-18')])

    def test_long_lower_shadows(self):
        self.assertListEqual(cs.find_long_lower_shadows(self.stock_data_30d),
                             [(1, '2018-06-07'), (7, '2018-06-15')])

    def test_candlestick_positioning(self):
        row0 = self.stock_data_30d.iloc[1]
        row1 = self.stock_data_30d.iloc[2]
        self.assertEqual(cs.candlestick_positioning(row0, row1), -1)
        row0 = self.stock_data_30d.iloc[2]
        row1 = self.stock_data_30d.iloc[3]
        self.assertEqual(cs.candlestick_positioning(row0, row1), 1)
        row0 = self.stock_data_30d.iloc[3]
        row1 = self.stock_data_30d.iloc[4]
        self.assertEqual(cs.candlestick_positioning(row0, row1), -1)
        row0 = self.stock_data_30d.iloc[4]
        row1 = self.stock_data_30d.iloc[5]
        self.assertEqual(cs.candlestick_positioning(row0, row1), 2)


