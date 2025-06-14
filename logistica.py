import pandas as pd
import streamlit as st
import plotly.express as px

#lista de categoria

#contruir selectbox(categoria)

#lista de tipos de veiculos

#construir a slect box (tipoveiculos)

#Filtrar os meus dadaos(Filtrado

#calcular metricas

#exibir as metricas

#agrupar os dados

#exibir grafico de barras

#exibir a tabela filtrado

st.set_page_config(page_title="Análise de Produtos")

st.subheader("Análise de Produtos")

df = pd.read_excel("base_logistica_completa.xlsx")

st.dataframe(df)

categoria = df["Categoria"].unique().tolist()
categoria.append('Todos')

veiculo = df["Veiculo"].unique().tolist()
veiculo.append("Todos")

categoria_select = st.selectbox("Selecione a Categoria: ", categoria, placeholder="Categoria")

veiculos = st.selectbox("Selecione o tipo de veículo: ", veiculo, placeholder="Veículos")

filtrado = df[((df["Categoria"]== categoria_select) | (categoria_select == 'Todos')) & (df["Veiculo"]== veiculos) | (veiculos == 'Todos')]

total_entregas = filtrado["Produto"].count()

soma_fretes = filtrado["Valor_Frete"].sum()

colte, colsf = st.columns(2)

colte.metric("Total de Entregas: ", int(total_entregas))

colsf.metric("Soma dos Frentes: ", int(soma_fretes))

quantidade_entrega_estado = filtrado.groupby("Estado_Entrega")["Data_Entrega"].count().reset_index()

st.bar_chart(data=quantidade_entrega_estado,x="Estado_Entrega",y="Data_Entrega")

st.dataframe(quantidade_entrega_estado)
