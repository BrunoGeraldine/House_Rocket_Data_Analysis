# Handling .Json file whit Multi_thread process
import time

from geopy.geocoders import Nominatim

geolocator = Nominatim( user_agent='geopyExercises')


def get_data( x ):
    index, row = x
    time.sleep( 1 )
    
    # call the api
    response = geolocator.reverse( row['query'] )
    address = response.raw['address']
    
    place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA'
    osm_type = response.raw['osm_type'] if 'osm_type' in response.raw else 'NA'
    country = address['country'] if 'contry' in address else 'NA'# this informar are in other subpack
    country_code = address['country_code'] if 'contry_code' in address else 'NA'# necessary declare the subfolder
    
    return place_id, osm_type, country, country_code



