#Ponderada Hugo Montan T15, entrega semana 05, aplicação "Page View Time Series Visualizer"

import unittest  
import pandas as pd  
import numpy as np  
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv('fcc_forum_pageviews.csv', index_col='date', parse_dates=True)
    
    def test_data_loaded(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0)
    
    def test_data_cleaning(self):
        #Testa se os dados foram filtrados corretamente
        original_length = len(self.df)
        cleaned_df = self.df[
            (self.df['value'] >= self.df['value'].quantile(0.025)) &
            (self.df['value'] <= self.df['value'].quantile(0.975))
        ]
        #Verifica se alguns dados foram removidos (outliers)
        self.assertLess(len(cleaned_df), original_length)
    
    def test_line_plot_function(self):
        try:
            fig = draw_line_plot()
            self.assertIsNotNone(fig)
        except Exception as e:
            self.fail(f"draw_line_plot() raised {type(e).__name__} unexpectedly: {e}")
    
    def test_bar_plot_function(self):
        try:
            fig = draw_bar_plot()
            self.assertIsNotNone(fig)
        except Exception as e:
            self.fail(f"draw_bar_plot() raised {type(e).__name__} unexpectedly: {e}")
    
    def test_box_plot_function(self):
        try:
            fig = draw_box_plot()
            self.assertIsNotNone(fig)
        except Exception as e:
            self.fail(f"draw_box_plot() raised {type(e).__name__} unexpectedly: {e}")

# Execução dos testes quando o arquivo é executado diretamente
if __name__ == '__main__':
    unittest.main()
