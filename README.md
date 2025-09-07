# 📊 Entrega Ponderada Semana 5 - Visualização de Dados

**Aluno:** Hugo Montan - T15  
**Disciplina:** Análise de Dados com Python  
**Período:** Semana 5  

## 📋 Projetos Incluídos

Este repositório contém dois projetos de visualização de dados desenvolvidos para a entrega ponderada da semana 5:

### 1. 🏥 Medical Data Visualizer
- **Arquivo principal:** `medical_data_visualizer/medical_data_visualizer.py`
- **Descrição:** Visualização e análise de dados de exames médicos
- **Funcionalidades:**
  - Cálculo de IMC e classificação de sobrepeso
  - Normalização de dados (colesterol e glicose)
  - Gráfico categórico (catplot) mostrando distribuição por doença cardiovascular
  - Mapa de calor (heatmap) com matriz de correlação
- **Gráficos gerados:**
  - `catplot.png` - Gráfico categórico
  - `heatmap.png` - Mapa de calor

### 2. 📈 Page View Time Series Visualizer
- **Arquivo principal:** `page_view_time_series_visualizer/time_series_visualizer.py`
- **Descrição:** Visualização de séries temporais de visualizações de página do fórum freeCodeCamp
- **Funcionalidades:**
  - Limpeza de dados (remoção de outliers)
  - Gráfico de linha temporal
  - Gráfico de barras por mês/ano
  - Box plots para análise de tendência e sazonalidade
- **Gráficos gerados:**
  - `line_plot.png` - Gráfico de linha temporal
  - `bar_plot.png` - Gráfico de barras
  - `box_plot.png` - Box plots

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação e análise de dados
- **Matplotlib** - Criação de gráficos
- **Seaborn** - Visualizações estatísticas avançadas
- **NumPy** - Operações matemáticas

## 📁 Estrutura do Projeto

```
entrega_ponderada_semana5/
├── medical_data_visualizer/
│   ├── medical_data_visualizer.py
│   ├── main.py
│   ├── test_module.py
│   ├── requirements.txt
│   ├── medical_examination.csv
│   ├── catplot.png
│   └── heatmap.png
├── page_view_time_series_visualizer/
│   ├── time_series_visualizer.py
│   ├── main.py
│   ├── test_module.py
│   ├── requirements.txt
│   ├── fcc_forum_pageviews.csv
│   ├── line_plot.png
│   ├── bar_plot.png
│   └── box_plot.png
├── .gitignore
└── README.md
```

## 🚀 Como Executar

### Para o Medical Data Visualizer:
```bash
cd medical_data_visualizer
pip install -r requirements.txt
python main.py
```

### Para o Page View Time Series Visualizer:
```bash
cd page_view_time_series_visualizer
pip install -r requirements.txt
python main.py
```

## 📊 Resultados

Ambos os projetos geram visualizações que demonstram:
- **Análise exploratória de dados**
- **Identificação de padrões e tendências**
- **Correlações entre variáveis**
- **Distribuições estatísticas**
- **Sazonalidade e tendências temporais**

## 🎯 Objetivos Alcançados

✅ Implementação completa dos requisitos do freeCodeCamp  
✅ Código bem documentado em português  
✅ Visualizações funcionais e informativas  
✅ Estrutura de projeto organizada  
✅ Testes unitários implementados  

## 📝 Observações

- Todos os códigos possuem comentários detalhados em português
- Os gráficos são salvos automaticamente como arquivos PNG
- Os dados são limpos e processados conforme especificações
- As visualizações seguem as melhores práticas de design

---

**Desenvolvido com ❤️ por Hugo Montan - T15**
