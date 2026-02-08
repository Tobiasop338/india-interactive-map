import matplotlib.pyplot as plt
import geopandas as gpd

# Load the geographical data of India
indian_states = gpd.read_file('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/india.geojson')

# Population data for each state (in millions)
population_data = {
    'Andhra Pradesh': 49.67,
    'Arunachal Pradesh': 1.43,
    'Assam': 31.21,
    'Bihar': 125.49,
    'Chhattisgarh': 29.11,
    'Goa': 1.58,
    'Gujarat': 60.43,
    'Haryana': 28.21,
    'Himachal Pradesh': 7.54,
    'Jharkhand': 38.99,
    'Karnataka': 61.95,
    'Kerala': 34.83,
    'Madhya Pradesh': 85.35,
    'Maharashtra': 122.15,
    'Manipur': 3.05,
    'Meghalaya': 3.21,
    'Mizoram': 1.09,
    'Nagaland': 2.20,
    'Odisha': 41.95,
    'Punjab': 27.74,
    'Rajasthan': 77.85,
    'Sikkim': 0.61,
    'Tamil Nadu': 72.14,
    'Telangana': 39.48,
    'Tripura': 4.17,
    'Uttar Pradesh': 199.81,
    'Uttarakhand': 10.11,
    'West Bengal': 91.28
}

# Merge population data into the geo-dataframe
indian_states['population'] = indian_states['st_nm'].map(population_data)

# Create a plot
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
indian_states.boundary.plot(ax=ax, color='black')
indian_states.plot(column='population', ax=ax, legend=True,
                   legend_kwds={'label': "Population by State (millions)",
                                  'orientation': "horizontal"})

# Set title and show the plot
ax.set_title('Interactive Map of India States with Populations')
plt.show()