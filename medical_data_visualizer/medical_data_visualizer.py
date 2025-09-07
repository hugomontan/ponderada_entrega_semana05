#Ponderada Hugo Montan T15, entrega semana 05, primeira aplicação de entrega "Medical_data_visualizer"


# Importando todas as bibliotecas necessárias para a aplicação
import pandas as pd  # Para manipulação e análise de dados
import seaborn as sns  # Para criação de gráficos estatísticos
import matplotlib.pyplot as plt  # Para criação de gráficos e visualizações
import numpy as np  # Para operações matemáticas e arrays

# Importando os dados do arquivo CSV disponibilizado pela ponderada contendo os dados médicos
df = pd.read_csv('medical_examination.csv')

# Adição da coluna 'overweight' (sobrepeso) aos dados (instrução dada pela ponderada)
# Para determinar se uma pessoa está acima do peso, primeiro calculamos o IMC (Índice de Massa Corporal) (IMC = peso (kg) / altura (m)²)
# Se o valor for > 25, a pessoa está acima do peso, usamos valor 0 para dentro do peso saudável e valor 1 para acima do peso
# A altura está em cm, então dividimos por 100 para converter para metros
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalização dos dados para que 0 sempre represente "bom" e 1 sempre represente "ruim", para colesterol e glicose: se o valor for 1 (normal), definimos como 0 (bom)
# Se o valor for maior que 1 (acima do normal), definimos como 1 (ruim)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Função para criar o Gráfico Categórico (Categorical Plot)
def draw_cat_plot():
    """
    Gráfico categórico mostrando as contagens de resultados bons e ruins
    para as variáveis: colesterol, glicose, fumo, álcool, atividade física e sobrepeso
    separados por pacientes com e sem doença cardiovascular (cardio=1 e cardio=0), demonstrando os efeitos seccionados das variáveis
    """
    
    # Criação de um DataFrame para o gráfico categórico usando pd.melt
    # pd.melt transforma o DataFrame de formato largo para formato longo
    # Um dataframe longo é um formato onde cada linha representa uma observação e cada coluna representa uma variável, pd.melt "desempilha" o dataframe, o "derretendo"
    # id_vars=['cardio'] mantém a coluna cardio como identificador
    # value_vars especifica as colunas que serão transformadas em variáveis
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    
    # Agrupa os dados por cardio, variable e value e conta quantas vezes cada combinação aparece.
    # Em seguida, ele transforma essa contagem em uma nova coluna chamada total.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Criação do gráfico categórico usando seaborn
    # sns.catplot() cria um gráfico de barras mostrando as contagens de valores das características categóricas
    # data=df_cat: dados a serem plotados
    # x='variable': variáveis no eixo x (cholesterol, gluc, etc.)
    # y='total': contagens no eixo y
    # hue='value': diferenciação por cor baseada no valor (0 ou 1)
    # col='cardio': cria painéis separados para cardio=0 e cardio=1
    # kind='bar': tipo de gráfico (barras)
    # .fig: acessa a figura matplotlib subjacente
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig
    
    # Retorna a figura para ser salva ou exibida
    return fig

# Função para criar o Mapa de Calor (Heat Map)
def draw_heat_map():
    """
    Cria um mapa de calor mostrando a matriz de correlação entre as variáveis médicas
    Os dados são limpos removendo valores incorretos ou extremos antes da análise
    """
    
    # Limpeza dos dados na variável df_heat filtrando segmentos de pacientes que representam dados incorretos, conforme intrução listada no freecodecamp
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Pressão diastólica deve ser menor ou igual à sistólica
        (df['height'] >= df['height'].quantile(0.025)) &  # Altura deve ser maior que o percentil 2.5 (remove valores muito baixos)
        (df['height'] <= df['height'].quantile(0.975)) &  # Altura deve ser menor que o percentil 97.5 (remove valores muito altos)
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Peso deve ser maior que o percentil 2.5 (remove valores muito baixos)
        (df['weight'] <= df['weight'].quantile(0.975))    # Peso deve ser menor que o percentil 97.5 (remove valores muito altos)
    ]
    
    # Cálculo da matriz de correlação e armazenamento na variável corr
    # A correlação mede a relação linear entre duas variáveis (valores entre -1 e 1)
    # Valores próximos de 1 indicam correlação positiva forte
    # Valores próximos de -1 indicam correlação negativa forte
    # Valores próximos de 0 indicam pouca ou nenhuma correlação
    corr = df_heat.corr()
    
    # Geração de uma máscara para o triângulo superior e armazenamento na variável mask
    # np.triu() cria uma matriz triangular superior (valores True acima da diagonal principal)
    # np.ones_like() cria uma matriz de uns com a mesma forma da matriz de correlação
    # dtype=bool converte para tipo booleano
    # Isso é usado para mascarar (ocultar) a parte superior do mapa de calor, evitando duplicação
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Configuração da figura matplotlib
    # figsize=(12, 9) define o tamanho da figura em polegadas (largura x altura)
    fig, ax = plt.subplots(figsize=(12, 9))


    # EXECUÇÃO DO HEATMAP
    # sns.heatmap() plota a matriz de correlação como um mapa de calor
    # corr: matriz de correlação a ser plotada
    # annot=True: mostra os valores de correlação em cada célula
    # fmt=.1F formata os números com 1 casa decimal
    # square=True: faz as células quadradas
    # center=0: centraliza a escala de cores em 0
    # cbar_kws reduz o tamanho da barra de cores pela metade
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, center=0, cbar_kws={'shrink': 0.5})
    
    # Salvamento da figura como arquivo PNG
    # Esta linha salva o mapa de calor como 'heatmap.png' no diretório atual
    fig.savefig('heatmap.png')
    
    # Retorna a figura 
    return fig
