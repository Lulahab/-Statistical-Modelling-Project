import requests
import pandas as pd

##Fetch all networks from the CityBikes API
base_url = "https://api.citybik.es/v2/networks"

response = requests.get(base_url)

##Check if the request is successful
if response.status_code == 200:
    networks_data = response.json()
else:
    print("Error: Unable to fetch networks")
    exit()

####Find the network for Salvador
networks = networks_data['networks']

##Filter networks for the city of Salvador
salvador_network = None
for network in networks:
    if network['location']['city'].lower() == 'salvador':
        salvador_network = network
        break

if not salvador_network:
    print("No network found for Salvador")
    exit()

Display the selected network
print(f"Network found: {salvador_network['name']}")
print(f"GBFS URL: {salvador_network.get('gbfs_href', 'N/A')}\n")

Fetch bike station data for the Salvador network
salvador_network_url = f"https://api.citybik.es{salvador_network['href']}"

response_stations = requests.get(salvador_network_url)

if response_stations.status_code == 200:
    salvador_stations_data = response_stations.json()
else:
    print("Error: Unable to fetch station data")
    exit()
Parse station data and create a DataFrame
salvador_stations = salvador_stations_data['network']['stations']

Extract relevant data into a list
station_info = []
for station in salvador_stations:
    station_info.append({
        'Station Name': station.get('name', 'N/A'),
        'Latitude': station.get('latitude', None),
        'Longitude': station.get('longitude', None),
        'Free Bikes': station.get('free_bikes', 0),
        'Empty Slots': station.get('empty_slots', 0)
    })

Convert the list to a Pandas DataFrame
salvador_station = pd.DataFrame(station_info)

Display the DataFrame
print("Bike Stations DataFrame:")
print(salvador_station)