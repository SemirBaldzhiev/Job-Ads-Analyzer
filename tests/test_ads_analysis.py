import unittest
from unittest.mock import patch
from io import StringIO
from src.analysis.job_analysis import wordcloud_job_titles, distribution_by_date_posted
import pandas as pd

class TestJobAnalysis(unittest.TestCase):
    def setUp(self):
        # Set up any initial conditions or mock objects needed for tests
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_wordcloud_job_titles(self, mock_stdout):
        wordcloud_job_titles()

    @patch('sys.stdout', new_callable=StringIO)
    def test_distribution_by_date_posted(self, mock_stdout):
        distribution_by_date_posted()


if __name__ == '__main__':
    unittest.main()
