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


# Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 31 a 37
df_filtered = df.iloc[30:37, 4:7]

# Renomeia as colunas para facilitar o uso
df_filtered.columns = ['AÇÃO', 'Orcamento_Inicial', 'Orcamento_Atualizado']

# Função para limpar e converter colunas de moeda
def clean_currency(column):
    return (column.astype(str)
            .str.replace('R$', '', regex=False)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
            .str.strip()
            .astype(float))

# Aplica a limpeza às colunas de orçamento
df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
df_filtered['Orcamento_Inicial'] = clean_currency(df_filtered['Orcamento_Inicial'])

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


df_filtered = df.copy()

df_filtered.columns = ['Ação', 'SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado']

def clean_currency(column):
    return (column.astype(str)
            .str.replace('R$', '', regex=False)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
            .str.strip()
            .astype(float))

df_filtered['SUM de Orçamento Atualizado'] = clean_currency(df_filtered['SUM de Orçamento Atualizado'])
df_filtered['SUM de Orçamento Realizado'] = clean_currency(df_filtered['SUM de Orçamento Realizado'])

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
