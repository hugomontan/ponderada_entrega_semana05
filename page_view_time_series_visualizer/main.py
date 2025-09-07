#Ponderada Hugo Montan T15, entrega semana 05, aplicação "Page View Time Series Visualizer"

# Importação das funções de visualização do módulo principal
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Teste das funções de visualização
#Criação e salvamento do gráfico de linha
line_fig = draw_line_plot()  # Chama a função que cria o gráfico de linha

# Criação e salvamento do gráfico de barras
bar_fig = draw_bar_plot()  # Chama a função que cria o gráfico de barras

# Criação e salvamento dos gráficos de caixa
box_fig = draw_box_plot()  # Chama a função que cria os gráficos de caixa
