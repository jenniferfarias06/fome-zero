# 1. Imports
import pandas as pd
import streamlit as st
import plotly.express as px
from data_processing import process_data

st.set_page_config(page_title='Cuisines', page_icon='🍽️', layout='wide')

# 2. Processamento dos dados
df1 = process_data('dataset/zomato.csv')

# 4. Função das métricas
def melhores_tipos_de_culinarias(cuisine):
    resultado = df1[df1['cuisines'] == cuisine].sort_values(
        by=['aggregate_rating', 'restaurant_id'],
        ascending=[False, True]
    ).head(1)

    return resultado 


# 5. Função dos melhores restaurantes
def top_restaurants(countries, cuisines, top_n):
    cols = [
        'restaurant_id',
        'restaurant_name',
        'country',
        'city',
        'cuisines',
        'average_cost_for_two',
        'aggregate_rating',
        'votes'
    ]

    lines = (
        df1['cuisines'].isin(cuisines) &
        df1['country'].isin(countries)
    )

    dataframe = df1.loc[lines, cols].sort_values(
        ['aggregate_rating', 'restaurant_id'],
        ascending=[False, True]
    )

    return dataframe.head(top_n)
    
    
# 6. Função do ranking de culinárias
def cuisines_ranking(countries, top_n, melhores=True):
    linhas = df1['country'].isin(countries)

    grouped_df = (
        df1.loc[linhas, ['aggregate_rating', 'cuisines']]
        .groupby('cuisines')
        .mean()
        .sort_values('aggregate_rating', ascending=not melhores)
        .reset_index()
        .head(top_n)
    )

    titulo = 'Melhores' if melhores else 'Piores'

    fig = px.bar(
        grouped_df,
        x='cuisines',
        y='aggregate_rating',
        text_auto='.2f',
        title=f'Top {top_n} {titulo} Tipos de Culinárias',
        labels={
            'cuisines': 'Tipo de culinária',
            'aggregate_rating': 'Nota média'
        },
        color_discrete_sequence=['#C0392B']
    )

    return fig


# 7. Filtros da barra lateral
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('---')

countries = st.sidebar.multiselect(
    'Escolha os Países que Deseja visualizar',
     df1.loc[:, 'country'].unique().tolist(),
     default = ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar","Singapure","South Africa",
 "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America",]
)

st.sidebar.markdown('---')


top_n = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar', 1, 20, 10)

st.sidebar.markdown('---')


cuisines = st.sidebar.multiselect(
    'Escolha os Tipos de culinarias que deseja visualizar',
     df1.loc[:, 'cuisines'].unique().tolist(),
     default =["Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",

              ])


# 8. Layout do dashboard

#    - Título e métricas
with st.container():
    st.title('🍽️ Visão Geral dos Restaurantes')
    st.subheader('Melhores Restaurantes dos Principais Tipos Culinários')

    col1, col2, col3, col4, col5 = st.columns(5)

    culinarias = [
        ("Italian", col1),
        ("American", col2),
        ("Arabian", col3),
        ("Japanese", col4),
        ("Brazilian", col5)
    ]

    for culinaria, coluna in culinarias:
        resultado = melhores_tipos_de_culinarias(culinaria)

        nome = resultado['restaurant_name'].iloc[0]
        nota = resultado['aggregate_rating'].iloc[0]

        coluna.metric(
            label=f"{culinaria}: {nome}",
            value=f"{nota}/5.0",
            help=f"""
            País: {resultado['country'].iloc[0]}
            Cidade: {resultado['city'].iloc[0]}
            Custo médio para dois: {resultado['average_cost_for_two'].iloc[0]}
            Moeda: {resultado['currency'].iloc[0]}
            """
        )

#    - Tabela de restaurantes
with st.container():
    st.subheader(f'Top {top_n} Restaurantes')
    top_10 = top_restaurants(countries, cuisines, top_n)
    st.dataframe(top_10, use_container_width=True)


#    - Gráficos
col1, col2 = st.columns(2)

with col1:
   fig = cuisines_ranking(countries, top_n)
   st.plotly_chart(fig, use_container_width=True)


with col2:
   fig = cuisines_ranking(countries, top_n, melhores = False )
   st.plotly_chart(fig, use_container_width=True)