# 1. Imports
import pandas as pd
import streamlit as st
import plotly.express as px
from data_processing import process_data

st.set_page_config(page_title='Cities', page_icon='🏙️', layout='wide')

df1 = process_data('dataset/zomato.csv')

def top_cidades(countries, top_n):
    grouped_df = (
        df1[df1['country'].isin(countries)]
        .groupby(['country', 'city'])['restaurant_id']
        .nunique()
        .reset_index(name='Quantidade')
        .sort_values(
            ['Quantidade', 'city'],
            ascending=[False, True]
        )
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x='city',
        y='Quantidade',
        text='Quantidade',
        color='country',
        title=f'Top {top_n} Cidades com Mais Restaurantes',
        labels={
            'city': 'Cidade',
            'Quantidade': 'Quantidade de Restaurantes',
            'country': 'País'
        }
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    return fig

# função avaliações 
def media_avaliacoes(countries, top_n, avaliacao):
    if avaliacao == 'alta':
        condicao = df1['aggregate_rating'] >= 4
        descricao = 'Nota Maior ou Igual a 4'
    else:
        condicao = df1['aggregate_rating'] <= 2.5
        descricao = 'Nota Menor ou Igual a 2.5'

    group_df = df1[
        df1['country'].isin(countries) & condicao
    ]

    grouped_df = (
        group_df
        .groupby(['country', 'city'])['restaurant_id']
        .nunique()
        .reset_index(name='Quantidade')
        .sort_values(
            ['Quantidade', 'city'],
            ascending=[False, True]
        )
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x='city',
        y='Quantidade',
        text='Quantidade',
        color='country',
        title=f'Top {top_n} Cidades com Restaurantes com {descricao}',
        labels={
            'city': 'Cidade',
            'Quantidade': 'Quantidade de Restaurantes',
            'country': 'País'
        }
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    return fig
    
# função Tipos de culinarias 
def tipos_culinarios(countries, top_n):
    grouped_df = (
        df1[df1['country'].isin(countries)]
        .groupby(['country', 'city'])['cuisines']
        .nunique()
        .reset_index(name='quantidade_culinarias')
        .sort_values(
            ['quantidade_culinarias', 'city'],
            ascending=[False, True]
        )
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x='city',
        y='quantidade_culinarias',
        text='quantidade_culinarias',
        color='country',
        title=f'Top {top_n} Cidades com Mais Tipos de Culinárias Distintas',
        labels={
            'city': 'Cidade',
            'quantidade_culinarias': 'Quantidade de Tipos de Culinária',
            'country': 'País'
        }
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    return fig

# filtro lateral 
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('---')

countries = st.sidebar.multiselect(
    'Escolha os Países que Deseja visualizar',
     df1.loc[:, 'country'].unique().tolist(),
     default = ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar","Singapure","South Africa",
 "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America",]
)

st.sidebar.markdown('---')


top_n = st.sidebar.slider(
    'Selecione a quantidade de cidades que deseja visualizar',
    1, 20, 10
)


# Layout
st.title('🏙️ Visão Cidades')

if countries:

    # Gráfico: cidades com mais restaurantes
    fig = top_cidades(countries, top_n)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    # Restaurantes com avaliações altas
    with col1:
        fig = media_avaliacoes(countries, top_n, 'alta')
        st.plotly_chart(fig, use_container_width=True)

    # Restaurantes com avaliações baixas
    with col2:
        fig = media_avaliacoes(countries, top_n, 'baixa')
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico: variedade de culinárias
    fig = tipos_culinarios(countries, top_n)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning('Selecione pelo menos um país para visualizar os gráficos.')