import folium
import geopandas
import pandas as pd
import streamlit as st
from datetime import datetime
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout='wide')
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# functions
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile

def intro(data):
    st.header('Original Dataset')
    st.dataframe(data, height=500)

    st.sidebar.title('Real Estate Project')
    st.sidebar.subheader('https://github.com/jaohenritm')

def treatment_data(data):
    # removing repeated ids and keeping the last one
    data = data.drop_duplicates(subset = ['id'], keep = 'last')
    
    # excluding the row with 33 bedrooms
    data = data.drop(index=15870)

    return data

def transformation_data(data):
    # converting sqft to m2
    data['m2_living'] = data['sqft_living'] * 0.092903
    data['m2_lot'] = data['sqft_lot'] * 0.092903
    data['m2_above'] = data['sqft_above'] * 0.092903
    data['m2_basement'] = data['sqft_basement'] * 0.092903
    
    # removing columns with sqft
    data = data.drop(['sqft_living','sqft_lot','sqft_above','sqft_basement','sqft_living15','sqft_lot15'], axis=1)
    
    # new features
    data['old'] = data['yr_built'].apply(lambda x: 'yes' if x <= 1955 else 'no')

    data['renovated'] = data['yr_renovated'].apply(lambda x: 'yes' if x > 2009 else 'no')
    
    # convert bathroom to int
    data = data.astype({'bathrooms':'int'})

    return data

def recommended_properties(data):
    data = data.loc[((data['bathrooms'] == 2) | (data['bathrooms'] == 3)) &
                        (data['floors'] == 1) &
                        (data['condition'] == 2)]
                       
    price_sell = data['price'] * 1.30

    data.insert(loc=5, column='Estimated Sell Price', value=price_sell)

    data = data.rename(columns={'id':'ID','date':'Date','price':'Price','bedrooms':'Bedrooms',
                         'bathrooms':'Bathrooms', 'floors':'Floors', 'condition':'Condition'})

    return data

def map(data, geofile):
    df = data
    st.title('Spreadsheet with the recommend properties to Buy')

    st.dataframe(data[['ID', 'Price', 'Estimated Sell Price', 'Bathrooms', 'Floors',
                       'Condition']], height=510)

    st.subheader('Statistic description of the recommended Properties')
    st.dataframe(data.describe())

    c1, c2 = st.columns((1, 1))

    c1.header('Map with the Properties')
      # base map - Folium
    map = folium.Map(location=[data['lat'].mean(),
                               data['long'].mean()],
                               default_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(map)
    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']],
                       popup='Price to Buy: ${0}, Estimated Sell Price ${1}'.format(
                       row['Price'],
                       row['Estimated Sell Price'])).add_to(marker_cluster)

    with c1:
         folium_static(map)

    c2.header('Price Density')

    df = data[['Price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]

    region_price_map = folium.Map(location=[data['lat'].mean(),
                                            data['long'].mean()],
                                  default_zoom_start=15)

    region_price_map.choropleth(data=df,
                                geo_data=geofile,
                                columns=['ZIP', 'PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlOrRd',
                                fill_opacity=0.7,
                                line_opacity=0.2,
                                legend_name='Average Price')

    with c2:
        folium_static(region_price_map)

    return None

# loading data
path = 'kc_house_data.csv'
url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

data = get_data(path)
geofile = get_geofile(url)

# intro
intro(data)

# transformation of the data
data = transformation_data(data)

# cleaning the data
data = treatment_data(data)

# recommending properties
data = recommended_properties(data)

# maps
map(data, geofile)