
#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

# Import the modules
import requests
import json

import numpy as np
import pandas as pd

# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = '1LmNDpXKm1aNSwK2HCThD4C5v_cQtVxpEio3smS4i5G4-hHbI1DQiFU6Ysa6_ymVvpKIkTCNCGHT1mHKDMGyLh1GHhWklAlFTGBtBx6tm8F8BlNow6F-Z9pEmMrOZXYx'

ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
# PARAMETERS = {'term': 'food',
#              'limit': 50,
#              'offset': 50,
#              'radius': 10000,
#              'location': 'San Diego'}

# BUSINESS MATCH PARAMETERS - EXAMPLE
#PARAMETERS = {'name': 'Peets Coffee & Tea',
#              'address1': '7845 Highland Village Pl',
#              'city': 'San Diego',
#              'state': 'CA',
#              'country': 'US'}

# PARAMETERS = {'name': ''
#                 'term':'pizza',
#               'limit': 2,
#               'offset': 3,
#               'radius': 10000,
#               'location': 'San Diego'}

# offset should be random number ? 
PARAMETERS = {  'term': 'burrito',
                'limit': 3,
                'radius': 16093, # 10 miles
                'location': 'Goleta',
                'price': 1
            }



# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String
business_data = response.json()

# print the response
#print(json.dumps(business_data, indent = 3))
# print(business_data)



"""
import numpy as np
import pandas as pd
r_dtypes = {"stars": np.float16, 
            "useful": np.int32, 
            "funny": np.int32,
            "cool": np.int32,
           }

with open("/Users/yensydney/Desktop/DSProject/yelp_dataset/copyyelp_academic_dataset_tip.json", "r") as f:
    df = pd.read_json(f, orient="records", lines=True, dtype=r_dtypes)
    for i in df['text']:
        print(i)
"""

# r_dtypes = {"stars": np.float16, 
#             "useful": np.int32, 
#             "funny": np.int32,
#             "cool": np.int32,
#            }

#with open("/Users/yensydney/Desktop/DSProject/yelp_dataset/copyyelp_academic_dataset_tip.json", "r") as f:
#    df = pd.read_json(f, orient="records", lines=True, dtype=r_dtypes)



for i in business_data['businesses']:
    print(i['name'])