import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="DashUF",
    layout="wide")

st.title("DASHUF: Um Dashboard sobre os Dados de Despesa da UFERSA - Anos 2022, 2023 e 2024")

df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Possibilidades de Gráficos.csv')

col1, col2 = st.columns(2)

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

st.divider()

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    # Seleciona as colunas L, M e N (índices 11, 12 e 13)
    df_filtered = df.iloc[:, 11:14]
    
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
    
    fig3 = px.histogram(df_filtered, x='ANO', y=['Orcamento_Atualizado', 'Orcamento_Realizado'],
    title='Grupo de Natureza de Despesa Investimento',
    barmode = 'group', text_auto=True,
                        
    color_discrete_map={'Orcamento_Atualizado': 'blue', 'Orcamento_Realizado': 'red'})
    fig3.update_layout(xaxis_title = 'Ano', yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig3, use_container_width=True)

with row2_col2:
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

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    
    # Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 57 a 63
    df_filtered = df.iloc[57:63, 4:7]
    
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
    
    fig5 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
    title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2023',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
    fig5.update_layout(yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig5, use_container_width=True)

with row3_col2:

    # Seleciona as colunas E, F e G (índices 4, 5 e 6) e as linhas 85 a 93
    df_filtered = df.iloc[87:93, 4:7]
    
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
    
    fig6 = px.histogram(df_filtered, x='AÇÃO', y=['Orcamento_Inicial', 'Orcamento_Atualizado'],
    title='Comparativo da Despesa de Pessoal e Encargos Sociais - 2024',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orcamento_Inicial': 'blue', 'Orcamento_Atualizado': 'red'})
    fig6.update_layout(yaxis_title = 'Valor em R$')
    
    st.plotly_chart(fig6, use_container_width=True)

st.divider()

row4_col1, row4_col2 = st.columns(2)

with row4_col1:
       
    # 2. Função de limpeza (a mesma que já usamos)
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # 3. Preparação dos dados
    # Vamos pegar as colunas relevantes. Supondo que 'Ação' seja a coluna 0 ou similar.
    # Ajuste o iloc abaixo para pegar: [Coluna Ação, Coluna Orc. Atualizado, Coluna Orc. Realizado]
    # Exemplo hipotético: df.iloc[:, [3, 7, 8]] -> Verifique no seu CSV qual o índice da coluna "Ação"
    # Vou assumir que você já sabe quais são e chamaremos de 'df_acao'
    # Para este exemplo, vou assumir que a coluna 'Ação' existe no seu df original.
    
    # Limpamos os valores monetários ANTES de agrupar
    col_orc_atualizado = df.columns[1] # Ajuste o índice conforme seu CSV
    col_orc_realizado = df.columns[2]  # Ajuste o índice conforme seu CSV
    
    df[col_orc_atualizado] = clean_currency(df[col_orc_atualizado])
    df[col_orc_realizado] = clean_currency(df[col_orc_realizado])
    
    # --- O PULO DO GATO (CORREÇÃO DO ERRO) ---
    
    # Agrupamos por Ação e Somamos
    # Substitua 'Ação' pelo nome exato da coluna no seu CSV se for diferente
    df_grouped = df.groupby('Ação')[[col_orc_atualizado, col_orc_realizado]].sum()
    
    # AQUI ESTÁ A CORREÇÃO: reset_index() traz a 'Ação' de volta como coluna
    df_grouped = df_grouped.reset_index()
    
    # Agora temos 3 colunas, então podemos dar 3 nomes
    df_grouped.columns = ['Ação', 'SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado']
    
    # 4. Criando o Gráfico (Barras Horizontais conforme sua imagem)
    fig = px.bar(df_grouped, 
                 y='Ação', # No eixo Y para ficar horizontal
                 x=['SUM de Orçamento Atualizado', 'SUM de Orçamento Realizado'],
                 title='Grupo de Despesas Correntes',
                 barmode='group',
                 orientation='h', # Define que é horizontal
                 text_auto=True) # Mostra os valores nas barras
    
    # Ajusta a altura para caber todos os nomes
    fig.update_layout(height=800, yaxis={'categoryorder':'total ascending'})
    
    st.plotly_chart(fig7, use_container_width=True)
