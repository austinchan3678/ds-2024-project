
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

import numpy as np
import pandas as pd

# Define my API Key, My Endpoint, and My Header
API_KEY = '1LmNDpXKm1aNSwK2HCThD4C5v_cQtVxpEio3smS4i5G4-hHbI1DQiFU6Ysa6_ymVvpKIkTCNCGHT1mHKDMGyLh1GHhWklAlFTGBtBx6tm8F8BlNow6F-Z9pEmMrOZXYx'

ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

def search(term, limit, offset, location, price):
    PARAMETERS = {'term': term,
                'limit': limit,
                'offset': offset,
                'radius': 16093, # 10 miles already set
                'location': location,
                'price': price
            }


    # Make a request to the Yelp API
    response = requests.get(url = ENDPOINT,
                            params = PARAMETERS,
                            headers = HEADERS)

    # Conver the JSON String
    business_data = response.json()

    for i in business_data['businesses']:
        print(i['name'])

print("What type of food or restaurant do you want? ")
userTerm = input()
print("How many restaurant suggestions would you like? ")
userLimit = int(input())
print("What location would you like? ")
userLocation = input()
print("How many price signs? 1, 2, 3, or 4? ")
userPrice = int(input())
userOffset = 0

search(userTerm, userLimit, userOffset, userLocation, userPrice)


print("Type 's' to see more or any other key to quit")
inputKey = input()

while (inputKey == 's'):
    # userLimit += 3
    userOffset += 3
    search(userTerm, userLimit, userOffset, userLocation, userPrice)
    print("Type 's' to see more or any other key to quit")
    inputKey = input()