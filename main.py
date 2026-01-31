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
       
   df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Tabela dinâmica 2.csv')
    
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
   
   st.plotly_chart(fig7, use_container_width=True)
    
with row4_col2:
    df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Gráficos gerados pela IA.csv')

    # Create a copy to work with, avoiding modifying the original df
    df_temp = df.copy()
    
    # Set the second row (index 1) as the header
    new_columns = df_temp.iloc[1].tolist()
    df_filtered = df_temp[2:].copy() # Select data from row 2 onwards
    df_filtered.columns = new_columns # Assign the extracted header as new column names
    
    # Rename the columns to be consistent and easier to work with
    df_filtered = df_filtered.rename(columns={
        'Orçamento Atualizado(R$)': 'Orçamento Atualizado',
        'Orçamento Realizado (R$)': 'Orçamento Realizado'
    })
    
    # Reset index after dropping rows
    df_filtered = df_filtered.reset_index(drop=True)
    
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    df_filtered['Orçamento Atualizado'] = clean_currency(df_filtered['Orçamento Atualizado'])
    df_filtered['Orçamento Realizado'] = clean_currency(df_filtered['Orçamento Realizado'])
    
    
    fig8 = px.histogram(df_filtered, x='Função', y=['Orçamento Atualizado', 'Orçamento Realizado'],
    title='Execução orçamentária por FUNÇÃO',
    barmode = 'group', text_auto=True,
    color_discrete_map={'Orçamento Atualizado': 'blue', 'Orçamento Realizado': 'red'})
    fig8.update_layout(yaxis_title = 'Valor em R$')

    st.plotly_chart(fig8, use_container_width=True)

row5_col1, row5_col2 = st.columns(2)

with row5_col1:

    df = pd.read_csv('despesaOrcamentaria 2022x2023x2024 - Tabela dinâmica 2.csv')
    
    # Create a copy to work with, avoiding modifying the original df
    df_temp = df.copy()
    
    # Filter for rows where Unnamed: 0 is a year (2022, 2023, 2024)
    # And Unnamed: 1 and Unnamed: 2 (budget data) are not NaN
    # Assuming these budget columns are always together with the year
    df_filtered_raw = df_temp[
        (pd.to_numeric(df_temp['Unnamed: 0'], errors='coerce').isin([2022, 2023, 2024])) &
        (df_temp['Unnamed: 1'].notna()) &
        (df_temp['Unnamed: 2'].notna())
    ].copy()
    
    # Select only the relevant columns
    df_filtered = df_filtered_raw[['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2']].copy()
    
    # Explicitly assign the correct column names
    df_filtered.columns = ['ANO', 'DESPESA CORRENTE (R$)', 'DESPESA DE CAPITAL (R$)']
    
    # Convert 'ANO' to numeric, coercing errors to NaN
    df_filtered['ANO'] = pd.to_numeric(df_filtered['ANO'], errors='coerce')
    # At this point, all ANO should be valid years, but keep dropna as a safeguard if other data sneaks in
    df_filtered = df_filtered.dropna(subset=['ANO'])
    
    def clean_currency(column):
        return (column.astype(str)
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.strip()
                .astype(float))
    
    # Apply cleaning to relevant columns
    df_filtered['DESPESA CORRENTE (R$)'] = clean_currency(df_filtered['DESPESA CORRENTE (R$)'])
    df_filtered['DESPESA DE CAPITAL (R$)'] = clean_currency(df_filtered['DESPESA DE CAPITAL (R$)'])
    
    # Convert 'ANO' to integer after cleaning
    df_filtered['ANO'] = df_filtered['ANO'].astype(int)
    
    fig9 = px.histogram(df_filtered, x='ANO', y=['DESPESA CORRENTE (R$)', 'DESPESA DE CAPITAL (R$)'],
    title='Distribuição do Orçamento Realizado por Categoria Econômica (2022-2024)',
    barmode = 'group', text_auto=True,
    color_discrete_map={'DESPESA CORRENTE (R$)': 'blue', 'DESPESA DE CAPITAL (R$)': 'red'})
    fig9.update_layout(yaxis_title = 'Valor em R$')

st.plotly_chart(fig9, use_container_width=True)
    
