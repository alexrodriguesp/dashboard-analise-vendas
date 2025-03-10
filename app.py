import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configurar a página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_excel("data/vendas.xlsx")

df = carregar_dados()

# Título
st.title("📊 Dashboard de Análise de Vendas")

# Exibir os primeiros dados
st.write("### 🔍 Dados das Vendas")
st.dataframe(df.head())

# Gráfico de Vendas por Categoria
st.write("### 📈 Vendas por Categoria")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="Categoria", y="Vendas", data=df, ax=ax)
st.pyplot(fig)

# Filtros interativos
categoria_selecionada = st.selectbox("Selecione uma categoria:", df["Categoria"].unique())
df_filtrado = df[df["Categoria"] == categoria_selecionada]

st.write("### 🛍️ Vendas da Categoria Selecionada")
st.dataframe(df_filtrado)
