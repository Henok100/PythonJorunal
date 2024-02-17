import overpy

# Initialize Overpass API
api = overpy.Overpass()

# Define the bounding box coordinates (example coordinates for Mong Kok, Hong Kong)
bbox = (22.3199, 114.1598, 22.3369, 114.1780)

# Build the Overpass QL query
query = f"""
way["building"]({bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]});
out;
"""

# Send the query to the Overpass API
result = api.query(query)

# Count the number of buildings
building_count = len(result.ways)

# Print the count of buildings
print(f"Number of buildings: {building_count}")