# Import necessary libraries
import requests # For making API requests
import pandas as pd  # For handling data and creating a DataFrame

# Step 1: Explore the API structure by querying the base endpoint
# Define the base URL for the CityBikes API
base_url = "https://api.citybik.es/v2/networks"

# Fetch data from the API
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved data from the API!")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Parse the response JSON into a Python dictionary
data = response.json()

# Inspect the structure of the data
print("\nKeys in the JSON response:")
print(data.keys())  # Top-level keys (e.g., 'networks')

# Extract the list of bike-sharing networks
networks = data['networks']

# Convert the networks list into a Pandas DataFrame for easier exploration
networks_df = pd.DataFrame(networks)

# Display the first few rows of the DataFrame
print("\nAvailable networks:")
print(networks_df[['id', 'name', 'location']].head())

# Step 2: Select Luxembourg's network
# Locate the network ID for Luxembourg City (e.g., 'luxembourg')
# After checking, the network ID for Luxembourg is 'veloh'. You may need to adjust this based on the available networks.
chosen_network_id = "veloh"
print(f"\nSelected network ID: {chosen_network_id}")

# Step 3: Query details about the selected network (Luxembourg City)
# Construct the URL for the specific network
network_url = f"https://api.citybik.es/v2/networks/{chosen_network_id}"


# Fetch data for Luxembourg's network
response = requests.get(network_url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved Luxembourg's network data!")
else:
    print(f"Failed to retrieve Luxembourg's network data. Status code: {response.status_code}")
    exit()

# Parse the response JSON
network_data = response.json()

# Inspect the keys in the network data
print("\nKeys in Luxembourg's network data:")
print(network_data['network'].keys())

# Step 4: Extract bike station details
# The stations are stored under the 'stations' key
stations = network_data['network']['stations']

# Display the first few stations to understand their structure
print("\nSample station data:")
print(stations[:3]) # Display first 3 stations for inspection

# Step 5: Convert station data into a Pandas DataFrame
# Create a DataFrame from the stations data
stations_df = pd.DataFrame(stations)

# Select relevant columns: 'name', 'latitude', 'longitude', 'free_bikes'
stations_df = stations_df[['name', 'latitude', 'longitude', 'free_bikes']]

# Rename columns for better readability
stations_df.rename(columns={
    'name': 'station_name',
    'free_bikes': 'available_bikes'
}, inplace=True)

# Display the final DataFrame
print("\nLuxembourg Bike Stations DataFrame:")
print(stations_df.head())

# Step 6: Save the DataFrame to a CSV file (optional)
stations_df.to_csv("luxembourg_bike_stations.csv", index=False)
print("\nData saved to 'luxembourg_bike_stations.csv'.")

# Final Output
print("\nScript completed successfully!")
