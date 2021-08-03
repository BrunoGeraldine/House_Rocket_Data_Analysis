# Handling .Json file whit Multi_thread process
import time

from geopy.geocoders import Nominatim

geolocator = Nominatim( user_agent='geopyExercises')


def get_data( x ):
    index, row = x
    time.sleep( 1 )
    
    # call the api
    response = geolocator.reverse( row['query'] )
    
    place_id = response.raw['place_id']
    osm_type = response.raw['osm_type']
    country = response.raw['address']['country'] # this informar are in other subpack
    country_code = response.raw['address']['country_code'] # necessary declare the subfolder
    
    return place_id, osm_type, country, country_code



