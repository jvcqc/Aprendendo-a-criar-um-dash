import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Possibilidades de Gráficos.csv')

fig1 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
title='Grupo de Natureza de Despesa Pessoal e Encargos Sociais',
barmode = 'group', text_auto=True)
fig1.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')

st.plotly_chart(fig1, use_container_width=True)

