# 1. Imports
import streamlit as st
import folium
from streamlit_folium import st_folium
from data_processing import process_data


st.set_page_config(
    page_icon="📊",
    page_title="Main_Page",
    layout="wide"
)


# 2. Processamento dos dados
df1 = process_data('dataset/zomato.csv')


st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown("""---""")


countries = st.sidebar.multiselect(
    'Escolha os Países que Deseja visualizar',
     df1.loc[:, 'country'].unique().tolist(),
     default = ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar","Singapure","South Africa",
 "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America",]
)

st.sidebar.markdown("""---""")


st.sidebar.markdown("### 📂 Dados Tratados")

st.sidebar.download_button(
    label="📥 Download",
    data=df1.to_csv(index=False, sep=";").encode("utf-8"),
    file_name="dados_processados.csv",
    mime="text/csv",
)

# Filtrar os restaurantes pelos países selecionados
df_filtrado = df1[df1['country'].isin(countries)]



st.markdown('# Fome Zero!')  
st.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito') 

with st.container():  
      st.markdown('### Temos as seguintes marcas dentro da nossa plataforma')
      col1, col2, col3, col4, col5 = st.columns(5)

with col1:
        restaurantes_unicos = df_filtrado['restaurant_name'].nunique()
        col1.metric('Restaurantes Unicos', restaurantes_unicos)

with col2:
        paises_unicos = df_filtrado['country'].nunique()
        col2.metric('Países Unicos', paises_unicos)

with col3:
     cidades_unicas = df_filtrado['city'].nunique()
     col3.metric('Cidades Unicas', cidades_unicas)

with col4:
       avaliações = df_filtrado['votes'].sum()
       col4.metric('Avaliações feitas na plataforma', f'{avaliações:,.0f}'.replace(',', '.'))

with col5:
       culinaria = df_filtrado['cuisines'].nunique()
       col5.metric('Tipos de colunarias oferecidos', culinaria)


    
                    
st.subheader('Localização dos Restaurantes')

from folium.plugins import FastMarkerCluster

df_mapa = df_filtrado[
    ['latitude', 'longitude', 'restaurant_name']
].copy()

df_mapa = df_mapa.dropna(
    subset=['latitude', 'longitude']
)

df_mapa = df_mapa[
    df_mapa['latitude'].between(-90, 90) &
    df_mapa['longitude'].between(-180, 180)
]

mapa = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles='OpenStreetMap'
)

dados_mapa = df_mapa[
    ['latitude', 'longitude', 'restaurant_name']
].values.tolist()

FastMarkerCluster(
    data=dados_mapa,
    callback="""
    function (row) {
        var marker = L.marker(new L.LatLng(row[0], row[1]));
        marker.bindTooltip(row[2]);
        return marker;
    }
    """
).add_to(mapa)


st_folium(
    mapa,
    width=900,
    height=500,
    returned_objects=[]
)


