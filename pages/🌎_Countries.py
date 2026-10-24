import streamlit as st
import plotly.express as px
from data_processing import process_data

st.set_page_config(
    page_icon="🌍",
    page_title="Countries",
    layout="wide"
)

df1 = process_data('dataset/zomato.csv')


def restaurant_cidade(countries):
    restaurantes = (
        df1[df1['country'].isin(countries)]
        .groupby('country')['restaurant_id']
        .nunique()
        .reset_index(name='quantidade')
        .sort_values('quantidade', ascending=False)
    )

    fig = px.bar(
        restaurantes,
        x='country',
        y='quantidade',
        text='quantidade',
        title='Quantidade de Restaurantes por País',
        color_discrete_sequence=['#C0392B']
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    return fig


def cidades_pais(countries):
    cidades = (
        df1[df1['country'].isin(countries)]
        .groupby('country')['city']
        .nunique()
        .reset_index(name='quantidade')
        .sort_values('quantidade', ascending=False)
    )

    fig = px.bar(
        cidades,
        x='country',
        y='quantidade',
        text='quantidade',
        title='Quantidade de Cidades Registradas por País',
        color_discrete_sequence=['#C0392B']
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)

    return fig


def media_avaliacao(countries):
    media_avaliacao = (
        df1[df1['country'].isin(countries)]
        .groupby('country')['votes']
        .mean()
        .reset_index(name='quantidade')
        .sort_values('quantidade', ascending=False)
    )

    fig = px.bar(
        media_avaliacao.head(6),
        x='country',
        y='quantidade',
        text='quantidade',
        text_auto='.2f',
        title='Média de Avaliações por País',
        color_discrete_sequence=['#C0392B']
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return fig


def media_prato_p_2(countries):
    media_prato = (
        df1[df1['country'].isin(countries)]
        .groupby('country')['average_cost_for_two']
        .mean()
        .reset_index(name='quantidade')
        .sort_values('quantidade', ascending=False)
    )

    fig = px.bar(
        media_prato.head(6),
        x='country',
        y='quantidade',
        text='quantidade',
        text_auto='.2f',
        title='Média de Preço de um Prato para Duas Pessoas',
        color_discrete_sequence=['#C0392B']
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

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


# Layout 
st.header('  🌍 Visão Países ')


with st.container():  
    fig = restaurant_cidade(countries)
    st.plotly_chart(fig, use_container_width=True)


with st.container(): 
      fig = cidades_pais(countries)
      st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

with col1:
      fig = media_avaliacao(countries)

      st.plotly_chart(fig, use_container_width=True)


with col2:
      fig =  media_prato_p_2(countries)

      st.plotly_chart(fig, use_container_width=True)