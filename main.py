import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Possibilidades de Gráficos.csv')

fig1 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
title='Grupo de Natureza de Despesa Pessoal e Encargos Sociais',
barmode = 'group', text_auto=True)
fig1.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')

fig2 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
title='Grupo de Natureza de Despesa Corrente',
barmode = 'group', text_auto=True,
color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
fig2.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')

fig3 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
title='Grupo de Natureza de Despesa Investimento',
barmode = 'group', text_auto=True,
color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
fig3.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')

fig4 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2022',
barmode = 'group', text_auto=True,
color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
fig4.update_layout(yaxis_title = 'Valor em R$')

fig5 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2023',
barmode = 'group', text_auto=True,
color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
fig5.update_layout(yaxis_title = 'Valor em R$')

fig6 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2024',
barmode = 'group', text_auto=True,
color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
fig6.update_layout(yaxis_title = 'Valor em R$')

fig7 = px.histogram(df_filtered, x='Ação', y=['SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado'],
title='Comparativo de Despesa Corrente',
barmode = 'group', text_auto=True,
color_discrete_map={'SUM de Orçamento Atualizado': 'blue', 'SUM de Orçamento Realizado': 'red'})
fig7.update_layout(yaxis_title = 'Valor em R$')


st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)
st.plotly_chart(fig6, use_container_width=True) 
st.plotly_chart(fig7, use_container_width=True)
