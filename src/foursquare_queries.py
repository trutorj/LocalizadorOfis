##########################################################
#        SCRIPTS FOR DO FOURSQUARE SEARCHS               #
##########################################################
# Imports
import pandas as pd
from pandas import json_normalize
import requests
import json
import os
from dotenv import load_dotenv
#############################################################

# Function to make a query
def foursquare2jdf(categoria, radio, latlon):
    # Import token and check it
    load_dotenv()
    clientId = os.getenv("client_id")
    clientSecret = os.getenv("client_secret")
    print("Requested APIKEY found!") if clientId else print("UhUh, check your APIs")
    print("Requested APIKEY found!") if clientSecret else print("UhUh, check your APIs")

    # URL   
    url = 'https://api.foursquare.com/v2/venues/explore'
   
    # Query params
    params = dict(
              client_id=clientId,
              v='20180323',
              client_secret=clientSecret,
              ll=latlon,
              categoryId=categoria,
              limit=25
              )
    # Do the request
    resp = requests.get(url=url, params=params)
    # Parse to Json
    data = json.loads(resp.text)
    # Extract the results
    reasons = data['response']['groups'][0]['items']
    print(len(reasons) + "elements found!")
    # Results to pandas df
    df = json_normalize(reasons)
    # Extact the interest columns
    df_cleaned = df[["venue.name", "venue.location.lat", "venue.location.lng"]]
    # Rename them
    df_cleaned = df_cleaned.rename(columns = {"venue.name": "name", "venue.location.lat": "lat", "venue.location.lng": 'lon'})
    return df_cleaned

# Function to convert df to readable "geoJSON"
def row2Geo(row):
    return [({
        "name": row["name"],
        "type":"Point",
        "coordinates":[float(row["lon"]),float(row["lat"])]
        })]

# Apply to every row in the dataframe
def df2geo(df, ruta):
    geo_df = df.apply(row2Geo,axis=1,
                      result_type="expand")
    geo_df.columns= ["object"]
    # Save
    geo_df.to_json(ruta,orient="records")
    return geo_df

