import requests
import json
import pandas as pd

# Add the URL we want to make the request to
url = 'https://exemplurl.json'

# Set query parameters for pagination and field selection
limit = 100000  # Number of records per page. Adjust the limit as needed
offset = 0
data = []

while True:    
    params = {
        '$limit': limit,
        '$offset': offset,
        '$select': 'tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,payment_type,total_amount',  #optional, adjust as needed
        '$where': 'total_amount >= 50'  #optional, adjust as needed
    }    
   
    response = requests.get(url, params=params)    
    
    if response.status_code == 200:
        
        # Load the data as a JSON object
        batch_data = response.json()

        # If batch_data is empty, break the loop
        if not batch_data:
            print('All data retrieved')
            break

        # Extend the data list with the batch_data
        data.extend(batch_data)

        # Update the offset for the next batch
        offset += limit

    else:
        print(f"Request failed with status code {response.status_code}")
        break

# Create a pandas DataFrame from the JSON data
df = pd.DataFrame(data)
print('All data retrieved')
df
