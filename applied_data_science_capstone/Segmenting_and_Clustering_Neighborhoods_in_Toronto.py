# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ### Import packages

import pandas as pd
import requests
from bs4 import BeautifulSoup
import locator as loc
import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim

# ### Load data

url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(url, 'lxml')

# ### Quick view and examination

print(soup.prettify()[:1000])

wikitable = soup.find('table')

wikitable.find_all('th')

for i in wikitable.find_all('th'):
    print(i.text.strip())

# ## Part 1

# ### Created columns and data

columns = [i.text.strip() for i in wikitable.find_all('th')]

data = [[j.text.strip() for j in i.find_all('td')] for i in wikitable.find_all("tr")[1:]]

trtdata = pd.DataFrame(data, columns = columns)

trtdata['Neighborhood'] = trtdata.Neighborhood.apply(lambda x: x.replace(' /',','))

trtdata.columns = ['PostalCode','Borough', 'Neighborhood']

trtdata.head()

# ### Step 1 Remove 'Not Assigned'

trtdata1 = trtdata.loc[trtdata.Borough != 'Not assigned'].reset_index(drop=True)

# ### Step 2 Fill Neighborhood with Borough

trtdata1.loc[trtdata1.Neighborhood == 'Not assigned', 'Neighborhood'] = trtdata['Borough']

trtdata1.head()

# ### Step 3 Merge neighborhood

trtdata2 = trtdata1.groupby(['PostalCode', 'Borough']).agg(', '.join).reset_index()

trtdata2.shape

# ## Part 2

# ### Adding Latitude and Longitude

trtdata3 = loc.locator(trtdata2, 'PostalCode', 'ca')

trtdata3 = trtdata3.dropna()

trtdata3.head()

# ## Part 3

# ### Visualization in Map

# +
# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[trtdata3.lat.mean(), trtdata3.lng.mean()], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(trtdata3['lat'], trtdata3['lng'], trtdata3['Borough'], trtdata3['Neighborhood']):
    labeltext = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(labeltext, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto
# -

trt = trtdata3[trtdata3.Borough.str.contains('Toronto')].reset_index(drop=True)

trt.head()

# +
address = 'Toronto'

geolocator = Nominatim(user_agent="ca_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))

# +
# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, labeltext in zip(trt['lat'], trt['lng'], trt['Neighborhood']):
    label = folium.Popup(labeltext, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=10,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto

# +
# add markers to map
for row in trt.itertuples():
    map_toronto.add_child(folium.Marker(location=[row.lat,row.lng],
           popup=row.Neighborhood))

map_toronto

# +
# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

mc = MarkerCluster()

# add markers to map
for row in trt.itertuples():
    mc.add_child(folium.Marker(location=[row.lat,row.lng],
           popup=row.Neighborhood))

    
map_toronto.add_child(mc)
map_toronto
