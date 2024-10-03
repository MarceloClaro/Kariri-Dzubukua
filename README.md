# Kariri-Dzubukua

---

Este projeto realiza uma **análise linguística trilingue** entre **Dzubukuá**, **Português Arcaico**, e **Português Moderno**, utilizando técnicas avançadas de **Processamento de Linguagem Natural (PLN)**, **estatísticas descritivas e inferenciais**, e **visualização de dados**. A seguir, está uma descrição detalhada da estrutura do código e das funcionalidades implementadas.

---

## Estrutura Modular do Projeto

A organização modular permite uma fácil manutenção e extensão do código, com cada módulo responsável por uma parte específica da análise. Segue a estrutura do projeto:

```bash
projeto/
│
├── app.py  # Integração do código com Streamlit, a interface do usuário
├── data/
│   └── carrega_dados.py  # Funções relacionadas ao carregamento e tratamento dos dados
├── processing/
│   ├── similaridade_semantica.py  # Implementa Sentence-BERT e similaridade de cosseno
│   ├── similaridade_lexical.py    # Implementa Word2Vec, N-gramas e coeficiente de Sorensen-Dice
│   ├── similaridade_fonologica.py # Implementa Soundex e Distância de Levenshtein
├── analysis/
│   ├── correlacoes_pearson.py  # Cálculo de correlações de Pearson
│   ├── correlacoes_spearman.py # Cálculo de correlações de Spearman
│   ├── correlacoes_kendall.py  # Cálculo de correlações de Kendall
│   ├── regressao_linear.py     # Funções para regressão linear simples
│   ├── regressao_multipla.py   # Funções para regressão múltipla
│   ├── anova.py                # Funções para análise ANOVA
├── statistics/
│   ├── estatistica_descritiva.py  # Funções para média, mediana, variância, desvio padrão, etc.
│   ├── margens_erro.py           # Cálculo de margens de erro e intervalos de confiança
│   ├── testes_hipotese.py        # Testes de hipóteses estatísticas
├── math/
│   ├── funcoes_matematicas.py  # Funções matemáticas gerais
│   ├── ajustes_curvas.py       # Funções para ajustes de curvas
│   ├── q_exponencial.py        # Funções para ajuste q-exponencial
├── visualizations/
│   ├── pca.py          # Análise de Componentes Principais (PCA) e gráficos
│   ├── clustering.py   # Análise de agrupamentos (clusters) com K-Means e DBSCAN
│   ├── heatmaps.py     # Mapas de calor interativos
│   └── dendrograma.py  # Geração de dendrogramas para análise hierárquica
├── utils/
│   ├── salvar_dados.py  # Funções para salvar os resultados em CSV
│   ├── estatisticas_utils.py # Funções auxiliares para cálculos estatísticos
│   └── ajustes.py       # Funções adicionais de ajustes matemáticos
```

---

### Descrição Detalhada dos Módulos

#### `app.py`
Este arquivo é o ponto de entrada da aplicação **Streamlit**, que oferece uma interface interativa para o usuário. Ele permite o carregamento de dados, a execução das análises e a visualização dos resultados em tempo real.

#### `data/carrega_dados.py`
Contém funções para carregar, limpar e preparar os dados linguísticos. É responsável por garantir que as frases nas três línguas estejam devidamente organizadas para a análise.

#### `processing/`
Este diretório contém os módulos de processamento das diferentes formas de similaridade:

- **`similaridade_semantica.py`**: Utiliza **Sentence-BERT** para calcular a similaridade semântica entre as frases das três línguas, baseando-se no cálculo da **similaridade de cosseno**.
- **`similaridade_lexical.py`**: Implementa técnicas como **N-gramas**, **Word2Vec** e o **coeficiente de Sorensen-Dice** para medir a similaridade lexical.
- **`similaridade_fonologica.py`**: Utiliza algoritmos como **Soundex** e a **Distância de Levenshtein** para medir a similaridade fonológica entre palavras.

#### `analysis/`
Módulos responsáveis por cálculos estatísticos e análises avançadas:

- **`correlacoes_pearson.py`**, **`correlacoes_spearman.py`**, **`correlacoes_kendall.py`**: Cada módulo calcula correlações entre variáveis de interesse, utilizando diferentes métodos.
- **`regressao_linear.py`**: Aplica modelos de regressão linear simples entre variáveis de similaridade.
- **`regressao_multipla.py`**: Realiza regressão múltipla para entender como diferentes variáveis afetam a similaridade.
- **`anova.py`**: Aplica a **análise de variância (ANOVA)** para comparar as médias das similaridades entre os três idiomas.

#### `statistics/`
Responsável por cálculos estatísticos e análise de hipóteses:

- **`estatistica_descritiva.py`**: Realiza cálculos de média, mediana, variância, desvio padrão, etc.
- **`margens_erro.py`**: Calcula margens de erro e intervalos de confiança, úteis para entender a precisão das estimativas.
- **`testes_hipotese.py`**: Executa testes de hipóteses para verificar a significância estatística.

#### `math/`
Inclui funções matemáticas e de ajuste de curvas:

- **`funcoes_matematicas.py`**: Contém funções auxiliares para cálculos matemáticos.
- **`ajustes_curvas.py`**: Implementa métodos de ajuste de curvas para modelagem de dados.
- **`q_exponencial.py`**: Aplica o ajuste **q-exponencial**, relevante para sistemas complexos.

#### `visualizations/`
Este diretório contém funções para gerar visualizações:

- **`pca.py`**: Implementa a **Análise de Componentes Principais (PCA)** para visualização de dados em duas dimensões.
- **`clustering.py`**: Executa **K-Means** e **DBSCAN** para análise de agrupamentos.
- **`heatmaps.py`**: Gera mapas de calor interativos com base nas correlações entre variáveis.
- **`dendrograma.py`**: Gera dendrogramas para análise de agrupamentos hierárquicos.

#### `utils/`
Contém funções utilitárias:

- **`salvar_dados.py`**: Permite salvar os resultados das análises em arquivos **CSV**.
- **`estatisticas_utils.py`**: Funções auxiliares para cálculos estatísticos.
- **`ajustes.py`**: Contém funções adicionais para ajustes matemáticos.

---

### Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto.git
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo principal via **Streamlit**:
   ```bash
   streamlit run app.py
   ```

4. Carregue o arquivo **CSV** contendo as frases nas três línguas e veja as visualizações e análises sendo geradas em tempo real.

---

### Funcionalidades Principais

- **Análises Semânticas** com **Sentence-BERT** para medir similaridades de significado entre as frases.
- **Análises Lexicais** com **Word2Vec**, **N-gramas**, e o **coeficiente de Sorensen-Dice** para avaliar a estrutura das palavras.
- **Análises Fonológicas** usando **Soundex** e a **Distância de Levenshtein** para medir a similaridade sonora.
- **Modelos Estatísticos** como **Correlação de Pearson, Spearman e Kendall**, **Regressão Linear e Múltipla**.
- **Análise de Componentes Principais (PCA)** e **Agrupamentos (Clustering)** com visualizações interativas.

---

### Contribuições

Sinta-se à vontade para contribuir com o projeto enviando **pull requests** ou abrindo **issues** se encontrar problemas ou tiver sugestões de melhorias.

---

### Licença

Este projeto está licenciado sob a **MIT License**.
