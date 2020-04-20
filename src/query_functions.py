import pandas as pd 
import pymongo
# Connect with the database
from pymongo import MongoClient
client = MongoClient("mongodb://localhost/datamad0320")
db = client.get_database()
###########################################################
#         FUNCTIONS FOR PYMONGO SPATIAL QUERIES           #
###########################################################

# Function to count the number of the Point of Interest within a maximum distance
def contadorPOIs(coords, radio, coleccion):
    query = {'object': {'$near': {'$geometry': {'type': 'Point',
    'coordinates': coords},
    '$maxDistance': radio}}}
    #Result         
    n_POIs=list((db[coleccion].find((query), {"object.coordinates"})))
    return len(n_POIs)

# Function to show the Point of Interest within a maximum distance
def mostradorPOIs(coords, radio, coleccion):
    query = {'object': {'$near': {'$geometry': {'type': 'Point',
    'coordinates': coords},
    '$maxDistance': radio}}}
    #Result         
    n_POIs=list((db[coleccion].find((query), {"object.coordinates"})))
    return n_POIs