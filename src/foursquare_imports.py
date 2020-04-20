# Imports
import pandas as pd
from pandas import json_normalize
import requests
import json
import os
from dotenv import load_dotenv
from foursquare_queries import foursquare2jdf, column2Geo, df2geo

# Categories for venues
categories={
    "Café": "4bf58dd8d48988d16d941735",
    "CoffeShop": "4bf58dd8d48988d1e0931735",
    "NigthLife": "4d4b7105d754a06376d81259",
    "Vegan": "4bf58dd8d48988d1d3941735",
    "BasketballStadium": "4bf58dd8d48988d18b941735",
    "Airport": "4bf58dd8d48988d1ed931735",
    "Highschool": "4bf58dd8d48988d13d941735",
    "Elem_school": "4f4533804b9074f6e4fb0105",
    "Mid_school": "4f4533814b9074f6e4fb0106",
    "Preschool": "52e81612bcbc57f1066b7a45"}

#####################################################
#               QUERIES TO MONGO DB                 #
#####################################################

# Starbucks
categoria = categories["CoffeShop"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
# Filter before insert into database
datas = datas[datas.name.eq("Starbucks")]
df2geo(datas, '../output/starbucks.json')

#Nightlife
categoria = categories["NightLife"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/nightlife.json')

# Vegan restaurants
categoria = categories["Vegan"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/vegan.json')

# Elementary School
categoria = categories["Elem_school"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/elem_school.json')

# Middleschool
categoria = categories["Mid_school"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/midschool.json')

# Preschool
categoria = categories["Preschool"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/preschool.json')

# Highschool
categoria = categories["Highschool"]
radio = 5000
latlon = '37.7955307,-122.4005983'
datas = foursquare2jdf(categoria, radio, latlon)
df2geo(datas, '../output/highschool.json')