# Kariri-Dzubukua
Este estudo apresenta uma análise comparativa entre três idiomas: Dzubukuá (uma língua extinta), Português Arcaico e Português Moderno.

### Projeto de Análise Linguística Trilingue

Este repositório contém um projeto modular voltado para a análise de similaridades linguísticas entre o **Dzubukuá**, o **Português Arcaico** e o **Português Moderno**. Utilizamos técnicas avançadas de **Processamento de Linguagem Natural (PLN)**, estatística descritiva e inferencial, e métodos de visualização de dados para realizar análises semânticas, lexicais e fonológicas entre esses idiomas.

---

## Estrutura do Projeto

A organização modular do projeto permite a fácil integração, extensão e manutenção do código, com a divisão das responsabilidades entre os módulos de processamento, análise, estatística, e visualização. Abaixo está uma visão detalhada da estrutura e da função de cada módulo:

```bash
projeto/
│
├── app.py  # Arquivo principal que integra todos os módulos e a interface do Streamlit
├── data/
│   └── carrega_dados.py  # Funções para carregar e preparar os dados
├── processing/
│   ├── similaridade_semantica.py  # Funções para cálculos com Sentence-BERT e similaridade de cosseno
│   ├── similaridade_lexical.py    # Funções para cálculos com Word2Vec, N-gramas e coeficiente de Sorensen-Dice
│   ├── similaridade_fonologica.py # Funções para Soundex e Distância de Levenshtein
├── analysis/
│   ├── correlacoes_pearson.py  # Cálculo da correlação de Pearson
│   ├── correlacoes_spearman.py # Cálculo da correlação de Spearman
│   ├── correlacoes_kendall.py  # Cálculo da correlação de Kendall
│   ├── regressao_linear.py     # Funções para regressão linear simples
│   ├── regressao_multipla.py   # Funções para regressão múltipla
│   ├── anova.py                # Funções para análise de variância (ANOVA)
├── statistics/
│   ├── estatistica_descritiva.py  # Funções para média, mediana, moda, variância e desvio padrão
│   ├── margens_erro.py           # Cálculo de margens de erro e intervalos de confiança
│   ├── testes_hipotese.py        # Testes de hipóteses estatísticas
├── math/
│   ├── funcoes_matematicas.py  # Funções matemáticas gerais para o projeto
│   ├── ajustes_curvas.py       # Funções para ajustes de curvas
│   ├── q_exponencial.py        # Funções para ajustes e modelagem com q-exponencial
├── visualizations/
│   ├── pca.py          # Funções para visualização com análise de componentes principais (PCA)
│   ├── clustering.py   # Funções para análise de agrupamentos (clusters) com K-Means e DBSCAN
│   ├── heatmaps.py     # Funções para geração de mapas de calor interativos
│   └── dendrograma.py  # Funções para geração de dendrogramas de agrupamentos hierárquicos
├── utils/
│   ├── salvar_dados.py  # Funções para salvar os resultados como CSV
│   ├── estatisticas_utils.py  # Funções auxiliares para cálculos estatísticos
│   └── ajustes.py       # Funções para ajustes matemáticos e correções
```

---

### Descrição dos Módulos

#### `app.py`
Este é o arquivo principal que integra todos os módulos do projeto. Ele utiliza o **Streamlit** para criar uma interface de usuário simples e interativa, onde o usuário pode fazer upload de dados e visualizar os resultados das análises em tempo real.

#### `data/carrega_dados.py`
Contém as funções para carregar, limpar e preparar os dados utilizados nas análises. Esta etapa inclui a tokenização e normalização dos textos nas três línguas (Dzubukuá, Português Arcaico e Moderno).

#### `processing/`
Este diretório contém os módulos de processamento das diferentes formas de similaridade entre as línguas:

- `similaridade_semantica.py`: Implementa o cálculo da **similaridade semântica** usando o **Sentence-BERT** e a **similaridade de cosseno** para medir a proximidade entre frases nas três línguas.
- `similaridade_lexical.py`: Inclui funções para calcular a **similaridade lexical** usando **Word2Vec**, **N-gramas**, e o **coeficiente de Sorensen-Dice**.
- `similaridade_fonologica.py`: Contém funções que utilizam o **Soundex** e a **Distância de Levenshtein** para medir a similaridade fonológica entre as palavras.

#### `analysis/`
Este diretório é responsável pelas análises estatísticas:

- `correlacoes_pearson.py`: Calcula a correlação de Pearson entre variáveis.
- `correlacoes_spearman.py`: Calcula a correlação de Spearman, útil para dados não lineares.
- `correlacoes_kendall.py`: Calcula a correlação de Kendall para avaliar a concordância entre rankings.
- `regressao_linear.py`: Implementa a **regressão linear simples**, mostrando a relação entre duas variáveis.
- `regressao_multipla.py`: Contém funções para **regressão múltipla**, que modela a influência de várias variáveis independentes.
- `anova.py`: Realiza a **análise de variância (ANOVA)** para verificar diferenças significativas entre grupos.

#### `statistics/`
Módulo dedicado às estatísticas descritivas e inferenciais:

- `estatistica_descritiva.py`: Funções para calcular **média, mediana, variância, desvio padrão** e outras estatísticas descritivas.
- `margens_erro.py`: Calcula **margens de erro** e **intervalos de confiança**, importantes para avaliar a precisão das estimativas.
- `testes_hipotese.py`: Contém funções para realizar **testes de hipóteses estatísticas**, incluindo testes t e ANOVA.

#### `math/`
Inclui funções matemáticas gerais e específicas para ajustes:

- `funcoes_matematicas.py`: Funções matemáticas auxiliares, como soma, produto, etc.
- `ajustes_curvas.py`: Funções para ajuste de curvas com métodos de otimização.
- `q_exponencial.py`: Modelagem e ajuste de distribuições com o **q-exponencial**, útil para dados não-lineares complexos.

#### `visualizations/`
Este diretório contém funções para gerar diferentes tipos de visualizações gráficas:

- `pca.py`: Realiza a **análise de componentes principais (PCA)** e plota os resultados em gráficos 2D.
- `clustering.py`: Funções para agrupar dados usando **K-Means** e **DBSCAN**, gerando visualizações de agrupamentos.
- `heatmaps.py`: Gera **mapas de calor** interativos com base nas correlações entre variáveis.
- `dendrograma.py`: Gera **dendrogramas** para visualização de agrupamentos hierárquicos.

#### `utils/`
Ferramentas auxiliares para salvar dados e ajustes:

- `salvar_dados.py`: Funções para salvar os resultados das análises em arquivos **CSV**.
- `estatisticas_utils.py`: Funções auxiliares para cálculos estatísticos e validações.
- `ajustes.py`: Funções para ajustes matemáticos gerais e correções de dados.

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

- **Análises Semânticas** com **Sentence-BERT** para medir similaridades de significado.
- **Análises Lexicais** com **Word2Vec**, **N-gramas**, e o **coeficiente de Sorensen-Dice**.
- **Análises Fonológicas** usando **Soundex** e **Distância de Levenshtein**.
- **Regressão Linear e Múltipla**, **Correlação** (Pearson, Spearman, Kendall).
- **Estatísticas Descritivas** e **Inferenciais**, incluindo testes de hipótese e ANOVA.
- **Visualizações** como **PCA**, **Mapas de Calor**, **Clustering** e **Dendrogramas**.

---

### Contribuições

Sinta-se à vontade para enviar **pull requests** ou abrir **issues** se encontrar bugs ou tiver sugestões de melhorias. Este projeto é de código aberto e será melhorado com a ajuda da comunidade.

---

### Licença

Este projeto está licenciado sob a **MIT License**.
