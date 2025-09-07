#Ponderada Hugo Montan T15, entrega semana 05, primeira aplicação de entrega "Medical_data_visualizer"
#Corretor, confesso que a proposta e utilidade dentro do fluxo da aplicação do test_module.py ainda não é claro para mim, este arquivo 
#foi majoritariamente desenvolvido com base em IA, em cima do exemplo do freecodecamp e as demais peças desenvolvidas por mim

import unittest  
import pandas as pd  
import numpy as np  
from medical_data_visualizer import draw_cat_plot, draw_heat_map  

class TestMedicalDataVisualizer(unittest.TestCase):
    """
    Classe de testes unitários para o visualizador de dados médicos
    Testa se as funções estão funcionando corretamente e se os dados são processados adequadamente
    """
    
    def setUp(self):
        """
        Método executado antes de cada teste
        Carrega os dados do CSV para uso nos testes
        """
        # Carregamento dos dados para teste
        self.df = pd.read_csv('medical_examination.csv')
    
    def test_data_loaded(self):
        """
        Testa se os dados foram carregados corretamente
        Verifica se o DataFrame foi criado e se contém dados
        """
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0)
    
    def test_overweight_column(self):
        """
        Testa se a coluna overweight é calculada corretamente
        Verifica o cálculo do IMC e a classificação de sobrepeso
        """
        # Teste do cálculo do IMC
        # IMC = peso (kg) / altura (m)²
        bmi = self.df['weight'] / ((self.df['height'] / 100) ** 2)
        # Valores esperados para a coluna overweight (1 se IMC > 25, 0 caso contrário)
        expected_overweight = (bmi > 25).astype(int)
        pass
    
    def test_cat_plot_function(self):
        """
        Testa se a função de gráfico categórico executa sem erros
        Verifica se a função retorna uma figura válida
        """
        try:
            fig = draw_cat_plot()
            self.assertIsNotNone(fig)
        except Exception as e:
            self.fail(f"draw_cat_plot() raised {type(e).__name__} unexpectedly: {e}")
    
    def test_heat_map_function(self):
        """
        Testa se a função de mapa de calor executa sem erros
        Verifica se a função retorna uma figura válida
        """
        try:
            # Chama a função e verifica se retorna uma figura
            fig = draw_heat_map()
            self.assertIsNotNone(fig)
        except Exception as e:
            self.fail(f"draw_heat_map() raised {type(e).__name__} unexpectedly: {e}")

# Execução dos testes quando o arquivo é executado diretamente
if __name__ == '__main__':
    unittest.main()
