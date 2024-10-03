# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os
import base64
import logging
from utils.salvar_dados import salvar_dataframe
from processing.similaridade_semantica import calcular_similaridade_semantica
from processing.similaridade_lexical import calcular_similaridade_ngramas, calcular_similaridade_word2vec
from processing.similaridade_fonologica import calcular_similaridade_fonologica
from analysis.correlacoes_pearson import calcular_correlacao_pearson
from analysis.regressao_linear import regressao_linear
from analysis.regressao_multipla import regressao_multipla
from analysis.anova import analise_anova
from statistics.testes_hipotese import testes_hipotese
from visualizations.pca import aplicar_pca, grafico_pca
from visualizations.clustering import analise_clustering, visualizar_clusters
from visualizations.dendrograma import grafico_dendrograma
from visualizations.heatmaps import grafico_interativo_plotly
from math.q_exponencial import ajuste_q_exponencial

# Definir o caminho do ícone e da capa
icon_path = "logo.png"
capa_path = 'capa.png'

# Configuração da página com Streamlit
if os.path.exists(icon_path):
    st.set_page_config(page_title="Geomaker +IA", page_icon=icon_path, layout="wide")
else:
    st.set_page_config(page_title="Geomaker +IA", layout="wide")

# Exibição da imagem principal
if os.path.exists(capa_path):
    st.image(capa_path, caption='Laboratório de Educação e Inteligência Artificial - Geomaker', use_column_width='always')
else:
    st.warning("Imagem 'capa.png' não encontrada.")

# Menu lateral
if os.path.exists(icon_path):
    st.sidebar.image(icon_path, width=200)
else:
    st.sidebar.text("Imagem do logotipo não encontrada.")
st.sidebar.title("Geomaker +IA")

# Função principal para rodar a aplicação
def main():
    st.title('Análises Avançadas de Similaridade Linguística')

    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Tabela Completa do Dataset")
        st.dataframe(df)

        # Extração de frases por idioma
        sentences_dzubukua = df[df['Idioma'] == 'Dzubukuá']['Texto Original'].tolist()
        sentences_arcaico = df[df['Idioma'] == 'Português Arcaico']['Texto Original'].tolist()
        sentences_moderno = df['Tradução para o Português Moderno'].tolist()

        # Similaridades
        st.info("Calculando similaridades...")
        similarity_arcaico_dzubukua_sem, similarity_moderno_dzubukua_sem, similarity_arcaico_moderno_sem = calcular_similaridade_semantica(sentences_dzubukua, sentences_arcaico, sentences_moderno)
        similarity_arcaico_dzubukua_ng, similarity_moderno_dzubukua_ng, similarity_arcaico_moderno_ng = calcular_similaridade_ngramas(sentences_dzubukua, sentences_arcaico, sentences_moderno)
        similarity_arcaico_dzubukua_phon, similarity_moderno_dzubukua_phon, similarity_arcaico_moderno_phon = calcular_similaridade_fonologica(sentences_dzubukua, sentences_arcaico, sentences_moderno)

        # Criar DataFrame
        similarity_df = pd.DataFrame({
            'Dzubukuá - Arcaico (Semântica)': similarity_arcaico_dzubukua_sem,
            'Dzubukuá - Moderno (Semântica)': similarity_moderno_dzubukua_sem,
            'Dzubukuá - Arcaico (N-gramas)': similarity_arcaico_dzubukua_ng,
            'Dzubukuá - Moderno (N-gramas)': similarity_moderno_dzubukua_ng,
            'Dzubukuá - Arcaico (Fonológica)': similarity_arcaico_dzubukua_phon,
            'Dzubukuá - Moderno (Fonológica)': similarity_moderno_dzubukua_phon
        })

        st.subheader("Similaridades Calculadas")
        st.dataframe(similarity_df)

        # Gráficos e análises
        st.subheader("Mapa de Correlação entre Similaridades")
        grafico_interativo_plotly(similarity_df)

        st.subheader("Análise de Regressão Linear")
        model, y_pred = regressao_linear(similarity_df)
        st.write(model.summary())

        st.subheader("Ajuste Q-Exponencial")
        a, b, q = ajuste_q_exponencial(similarity_df['Dzubukuá - Moderno (Semântica)'])
        st.write(f"a: {a}, b: {b}, q: {q}")

        # Salvar os resultados
        if st.checkbox("Baixar Resultados"):
            salvar_dataframe(similarity_df)

if __name__ == '__main__':
    main()
