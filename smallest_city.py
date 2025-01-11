import requests
import pandas as pd

# API endpoint for city bike data
url = "https://api.citybik.es/v2/networks"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract relevant information: city name and number of stations
city_data = [
    {
        "city": network["location"]["city"],
        "stations": len(network["stations"]) if "stations" in network else 0
    }
    for network in data["networks"] if "location" in network and network["location"]["city"]
]

# Create a DataFrame
bike_data = pd.DataFrame(city_data)

# Find the city with the smallest number of stations
smallest_city = bike_data.loc[bike_data['stations'].idxmin()]
print(f"The city with the smallest number of stations is {smallest_city['city']} with {smallest_city['stations']} stations.")



import requests## to get a city with over 20 stations
import pandas as pd

# API endpoint for city bike data
url = "https://api.citybik.es/v2/networks"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract relevant information: city name and number of stations
city_data = [
    {
        "city": network["location"]["city"],
        "stations": len(network["stations"]) if "stations" in network else 0
    }
    for network in data["networks"] if "location" in network and network["location"]["city"]
]

# Create a DataFrame
bike_data = pd.DataFrame(city_data)

# Filter cities with more than 20 stations
filtered_data = bike_data[bike_data['stations'] > 20]

# Find the city with the smallest number of stations
if not filtered_data.empty:
    smallest_city = filtered_data.loc[filtered_data['stations'].idxmin()]
    print(f"The city with the smallest number of stations (over 20) is {smallest_city['city']} with {smallest_city['stations']} stations.")
else:
    print("No cities found with more than 20 stations.")



city_data = []
for network in data["networks"]:
    if "location" in network and network["location"]["city"]:
        network_id = network["id"]
        network_response = requests.get(f"https://api.citybik.es/v2/networks/{network_id}")
        network_data = network_response.json()

        # Count stations if available
        station_count = len(network_data["network"]["stations"]) if "stations" in network_data["network"] else 0

        city_data.append({
            "city": network["location"]["city"],
            "stations": station_count
        })

# Create DataFrame
bike_data = pd.DataFrame(city_data)

# Filter cities with more than 20 stations
filtered_data = bike_data[bike_data['stations'] > 20]

# Find the city with the smallest number of stations
if not filtered_data.empty:
    smallest_city = filtered_data.loc[filtered_data['stations'].idxmin()]
    print(f"The city with the smallest number of stations (over 20) is {smallest_city['city']} with {smallest_city['stations']} stations.")
else:
    print("No cities found with more than 20 stations.")
