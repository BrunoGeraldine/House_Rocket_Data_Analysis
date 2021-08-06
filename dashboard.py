#VIASUALIZAÇÃO DE DADOS AULA 2

import geopandas
import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import plotly.express as px

# Configurando a aparência do Gráfico default
st.set_page_config(page_title='House Rocket Insights',
                   page_icon= '🧊',
                   layout= 'wide')

# Supress Scientific Notation
np.set_printoptions(suppress=True)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Garantir que o formato date seja um datetime
# data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
#st.write(data.dtypes)

#Load data function
@st.cache( allow_output_mutation=True )
def get_data(path):
    data = pd.read_csv(path)
    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)
    return geofile

def set_feature( data ):
    # Add new features
    data['price_m2'] = data['price'] / data['sqft_lot']

    return data

def overview_data(data):
    pass
    f_attributes = st.sidebar.multiselect('Enter Columns', data.columns)
    f_zipcode = st.sidebar.multiselect('Enter Zipcode', data['zipcode'].unique())

    st.title('Data Overview')

    # attributes+zipcode= selecionar colunas e linhas
    # attributes= selecionar colunas
    # zipcode= selecionar linhas
    # 0+0= Retorno o dataset original
    if (f_zipcode != []) & (f_attributes != []):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), :]
    elif (f_zipcode == []) & (f_attributes != []):
        data = data.loc[:, f_attributes]
    else:
        data = data.copy()
    st.dataframe(data)

    # Configurando a aparência das tabelas
    c1, c2 = st.beta_columns((1, 1))

    # Average metrics
    df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # Merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    # Renomeando as colunas
    df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQFT LIVING', 'PRICE/M²']

    # Plotando as tabelas de médias
    c1.header('Average Values')  # Nomeando a tabela
    c1.dataframe(df, height=150)

    # Statistic Descriptive
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))
    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    df1 = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()
    df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

    c2.header('Descriptive Analysis')
    c2.dataframe(df1, height=150)
    return None

def portfolio_density(data, geofile):
    pass
    st.title('Region Overview')
    b1, b2 = st.beta_columns((1, 1))
    b1.header('Portfolio Density')

    df = data.sample(20)

    # Base Map - Folium
    density_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=15)
    marker_cluster = MarkerCluster().add_to(density_map)

    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold R${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}'.format(
                          row['price'],
                          row['date'],
                          row['sqft_living'],
                          row['bedrooms'],
                          row['bathrooms'],
                          row['yr_built'])).add_to(marker_cluster)
    with b1:
        folium_static(density_map)

    # Region Price Map
    b2.header('Price Density')
    df = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    # df = df.sample(10)
    geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]

    region_price_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=15)
    region_price_map.choropleth(data=df,
                                geo_data=geofile,
                                columns=['ZIP', 'PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlOrRd',
                                fill_opacity=0.7,
                                line_opacity=0.2,
                                legend_name='AVG PRICE')
    with b2:
        folium_static(region_price_map)

    return None

def commercial_destribution(data):
    st.sidebar.title('Commercial Options')
    st.title('Commercial Attributes')

    # Criando filtros
    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())
    st.sidebar.subheader('Select Max Year built')
    f_year_built = st.sidebar.slider('Year Built', min_year_built,
                                     max_year_built,
                                     min_year_built)
    st.header('Average Price per Year Built')

    # Data selection
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()
    # Plot
    fig = px.line(df, x='yr_built', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # --- Average Price per Day
    #st.header('Average Price per Day')
    #st.sidebar.subheader('Select Max Date')

    # Filters
    # espaço para o codigo com problema

    # Continuação do código

    # ------ Histograma
    st.header('Price Distribuition')
    st.sidebar.subheader('Select Max Price')
    # obs.: Usar o comando st.subheader() coloca o filtro na area de plotagem do streamlit e não na lateral

    # Filter
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    # Data filtering
    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)
    df = data.loc[data['price'] < f_price]

    # Data plot
    fig = px.histogram(df, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

    return None

def attributes_destribution(data):
    st.sidebar.title('Attributes Options')
    st.title('House Attributes')

    # filters
    f_bedroom = st.sidebar.selectbox('Max number of Bedrooms',
                                     sorted(set(data['bedrooms'].unique())))

    f_bathroom = st.sidebar.selectbox('Max number of Bathrooms',
                                      sorted(set(data['bathrooms'].unique())))

    c1, c2 = st.beta_columns(2)

    # House por bedrooms
    c1.header('Houses per bedrooms')
    df = data[data['bedrooms'] < f_bedroom]
    fig = px.histogram(data, x='bedrooms', nbins=19)
    c1.plotly_chart(fig, use_container_width=True)

    # House por bathrooms
    c2.header('Houses per bathrooms')
    df = data[data['bathrooms'] < f_bedroom]
    fig = px.histogram(data, x='bathrooms', nbins=19)
    c2.plotly_chart(fig, use_container_width=True)

    # Filters
    f_floor = st.sidebar.selectbox('Max number of floors',
                                   sorted(set(data['floors'].unique())))

    f_water = st.sidebar.checkbox('Only Houses with Water View',
                                  sorted(set(data['waterfront'].unique())))

    c1, c2 = st.beta_columns(2)

    # House por floors
    c1.header('Houses per floor')
    df = data[data['floors'] < f_floor]
    # plot
    fig = px.histogram(data, x='floors', nbins=19)
    c1.plotly_chart(fig, use_container_width=True)

    # House per water View
    c2.header('Houses Waterfront View')
    if f_water:
        df = data[data['waterfront'] == 1]
    else:
        df = data.copy()

    fig = px.histogram(data, x='waterfront', nbins=10)
    c2.plotly_chart(fig, use_container_width=True)

    return None





if __name__ == '__main__':
    #ETL
    # Data Extration
    path = ('kc_house_data.csv') #extraction DataFrame
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

    data = get_data(path) #load dataframe
    geofile = get_geofile(url)


    # Data Transformation
    data = set_feature(data)

    overview_data(data)

    portfolio_density(data, geofile)

    commercial_destribution(data)

    attributes_destribution(data)

    # Loading