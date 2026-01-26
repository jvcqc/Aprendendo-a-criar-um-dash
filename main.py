import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Possibilidades de Gráficos.csv')

col1, col2 = st.colunns(2)

with col1: 
    # Seleciona as três primeiras colunas (índices 0, 1 e 2)
    df_filtered = df.iloc[:, :3]
    
    # Renomeia as colunas para facilitar o uso, já que os nomes se repetem
    df_filtered.columns = ['ANO', 'Orcamento_Atualizado', 'Orcamento_Realizado']
    
    # Converte a coluna 'ANO' para numérico, transformando erros em NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    
    # Remove linhas onde a coluna 'ANO' é NaN (linhas vazias ou não numéricas)
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    df_filtered['Orcamento_Atualizado'] = clean_currency(df_filtered['Orcamento_Atualizado'])
    df_filtered['Orcamento_Realizado'] = clean_currency(df_filtered['Orcamento_Realizado'])
    
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig1 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Pessoal e Encargos Sociais',
    barmode = 'group', text_auto=True)
    fig1.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    # Seleciona as colunas G, H e I (índices 6, 7 e 8)
    df_filtered = df.iloc[:7, 6:9]
    
    # Renomeia as colunas para facilitar o uso
    df_filtered.columns = ['ANO', 'Orcamento_Atualizado', 'Orcamento_Realizado']
    
    # Converte a coluna 'ANO' para numérico, transformando erros em NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    
    # Remove linhas onde a coluna 'ANO' é NaN (linhas vazias ou não numéricas)
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
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
    df_filtered['Orcamento_Realizado'] = clean_currency(df_filtered['Orcamento_Realizado'])
    
    # Converte a coluna 'ANO' para inteiro
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    df_filtered.head()
    
    fig2 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Corrente',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
    fig2.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig2, use_container_width=True)
