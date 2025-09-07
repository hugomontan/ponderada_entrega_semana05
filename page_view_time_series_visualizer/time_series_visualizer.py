#Ponderada Hugo Montan T15, entrega semana 05, aplicação "Page View Time Series Visualizer"

# Importando todas as bibliotecas necessárias para a aplicação
import matplotlib.pyplot as plt  # Para criação de gráficos e visualizações
import pandas as pd  # Para manipulação e análise de dados
import seaborn as sns  # Para criação de gráficos estatísticos
from pandas.plotting import register_matplotlib_converters  # Para compatibilidade com matplotlib

# Registra conversores para matplotlib trabalhar com dados pandas
register_matplotlib_converters()

# Importando os dados do arquivo CSV disponibilizado pela ponderada contendo os dados de visualizações de página
# Definindo a coluna 'date' como índice do DataFrame
df = pd.read_csv('fcc_forum_pageviews.csv', index_col='date', parse_dates=True)

# Limpeza dos dados filtrando os dias quando as visualizações de página estavam no top 2.5% ou bottom 2.5% do dataset
# Isso remove outliers extremos que podem distorcer a visualização
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &  # Remove valores abaixo do percentil 2.5
    (df['value'] <= df['value'].quantile(0.975))    # Remove valores acima do percentil 97.5
]

# Função para criar o Gráfico de Linha (Line Plot)
def draw_line_plot():
    """
    Cria um gráfico de linha mostrando as visualizações diárias de página do fórum freeCodeCamp
    Demaio de 2016 a dezembro de 2019
    """
    
    # Criação de uma cópia dos dados para evitar modificações no DataFrame original
    df_line = df.copy()
    
    # Configuração da figura matplotlib
    fig, ax = plt.subplots(figsize=(15, 6))
    
    # Criação do gráfico de linha
    # df_line.index contém as datas (eixo x)
    # df_line['value'] contém os valores de visualizações (eixo y)
    # color='red' define a cor da linha como vermelha
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    
    # Configuração do título do gráfico
    ax.set_title('Visualizações diárias no FreeCodeCamp 05/2016-12/2019', fontsize=14)
    
    # Configuração dos rótulos dos eixos
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Page Views', fontsize=12)
    
    # Salvamento da figura como arquivo PNG
    fig.savefig('line_plot.png')
    
    # Retorna a figura
    return fig

# Função para criar o Gráfico de Barras (Bar Plot)
def draw_bar_plot():
    """
    Cria um gráfico de barras mostrando a média diária de visualizações de página para cada mês agrupado por ano, demonstrando sazonalidade e padrões
    """
    
    # Criação de uma cópia dos dados para evitar modificações no DataFrame original
    df_bar = df.copy()
    
    # Criação de colunas para ano e mês a partir do índice de data
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Agrupamento dos dados por ano e mês, calculando a média das visualizações
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Configuração da figura matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Criação do gráfico de barras, df_bar.plot() cria um gráfico de barras com barras agrupadas por mês
    # kind='bar' especifica o tipo de gráfico
    # ax=ax define o eixo onde o gráfico será plotado
    df_bar.plot(kind='bar', ax=ax)
    
    # Configuração do título do gráfico
    ax.set_title('Média diária de visualizações em página para cada mês (agrupado em ano)', fontsize=14)
    
    # Configuração dos rótulos dos eixos (refino visual dos eixos)
    ax.set_xlabel('Anos', fontsize=12)
    ax.set_ylabel('Média de visualizações em página', fontsize=12)
    
    # Configuração da legenda
    # Lista dos nomes dos meses para a legenda
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(title='Meses', labels=month_labels)
    
    # Rotação dos rótulos do eixo x para melhor legibilidade
    ax.tick_params(axis='x', rotation=45)
    
    # Salvamento da figura como arquivo PNG
    fig.savefig('bar_plot.png')
    
    # Retorna a figura
    return fig

# Função para criar os Gráficos de Caixa (Box Plots)
def draw_box_plot():
    """
    Cria dois gráficos de caixa adjacentes mostrando como os valores são distribuídos, dentro de um determinado ano ou mês e como isso se compara ao longo do tempo
    """
    
    # Criação de uma cópia dos dados para evitar modificações no DataFrame original
    df_box = df.copy()
    
    # Criação de colunas para ano e mês a partir do índice de data
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    
    # Criação de uma coluna com nomes dos meses abreviados
    # map() aplica a função lambda a cada valor da coluna 'month'
    # A função lambda converte números de mês (1-12) em nomes abreviados
    df_box['month_name'] = df_box['month'].map({
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    })
    
    # Configuração da figura matplotlib com dois subplots lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    # Primeiro box plot: Tendência anual (Year-wise Box Plot)
    # sns.boxplot() cria um gráfico de caixa usando seaborn
    # ax=ax1: especifica o primeiro subplot
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    
    # Configuração do primeiro gráfico
    ax1.set_title('Box Plot por Ano , fontsize=14')
    ax1.set_xlabel('Anos', fontsize=12)
    ax1.set_ylabel('Visualizações por página', fontsize=12)
    
    # Segundo box plot: Sazonalidade mensal (Month-wise Box Plot)
    # Ordenação dos dados por mês para garantir ordem cronológica correta
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month_name'] = pd.Categorical(df_box['month_name'], categories=month_order, ordered=True)
    
    sns.boxplot(data=df_box, x='month_name', y='value', ax=ax2)
    
    # Configuração do segundo gráfico
    ax2.set_title('Gráfico de Box Plot por Mês (análise de sazonalidade))', fontsize=14)
    ax2.set_xlabel('Mês', fontsize=12)
    ax2.set_ylabel('Visualizações por página', fontsize=12)
    
    # Rotação dos rótulos do eixo x para melhor legibilidade
    ax2.tick_params(axis='x', rotation=45)
    
    # Ajuste do layout para evitar sobreposição
    plt.tight_layout()
    
    # Salvar figura como arquivo PNG
    fig.savefig('box_plot.png')
    
    # Retorna a figura
    return fig
