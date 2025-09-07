#Ponderada Hugo Montan T15, entrega semana 05, primeira aplicação de entrega "Medical_data_visualizer"

# Importação das funções de visualização do módulo principal
from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Teste das funções de visualização
# Criação e salvamento do gráfico categórico
cat_fig = draw_cat_plot()  # Chama a função que cria o gráfico categórico
cat_fig.savefig('catplot.png')  # Salva o gráfico como arquivo PNG

# Criação e salvamento do mapa de calor
heat_fig = draw_heat_map()  # Chama a função que cria o mapa de calor (já salva automaticamente)
