import unittest
from unittest.mock import patch
from src.analysis.company_analysis import distribution_by_cnt_ads, distribution_by_date_founded
import pandas as pd

class TestCompanyAnalysis(unittest.TestCase):

    @patch('sqlite3.connect')
    @patch('pandas.read_sql_query')
    @patch('matplotlib.pyplot.show')
    def test_distribution_by_cnt_ads(self, mock_show, mock_read_sql_query, mock_connect):
        mock_read_sql_query.return_value = pd.DataFrame({
            'name': ['Company1', 'Company2'],
            'cnt_job_ads': [10, 20]
        })

        distribution_by_cnt_ads()

        mock_connect.assert_called_once()
        mock_read_sql_query.assert_called_once()
        mock_show.assert_called_once()

    @patch('sqlite3.connect')
    @patch('pandas.read_sql_query')
    @patch('matplotlib.pyplot.show')
    def test_distribution_by_date_founded(self, mock_show, mock_read_sql_query, mock_connect):
        mock_read_sql_query.return_value = pd.DataFrame({
            'name': ['Company1', 'Company2'],
            'year_founded': [2000, 2010]
        })

        distribution_by_date_founded()

        mock_connect.assert_called_once()
        mock_read_sql_query.assert_called_once()
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
