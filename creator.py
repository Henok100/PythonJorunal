import pandas as pd
from pyproj import Proj
import math
#from ex import biased_height

import numpy as np

def generate_height():
    # Define the desired range
    min_height = 25
    max_height = 70
    target_min = 30
    target_max = 60

    # Define the weights for each range
    weights = []
    for i in range(min_height, max_height + 1):
        if target_min <= i <= target_max:
            weights.append(3)  # Higher weight for the target range
        else:
            weights.append(1)  # Lower weight for other ranges

    # Normalize the weights to create a probability distribution
    weights = np.array(weights)
    probabilities = weights / np.sum(weights)

    # Generate a random height using the defined probability distribution
    height = np.random.choice(range(min_height, max_height + 1), p=probabilities)

    return height


def init_df():
    # Set the filename to the path of the shapefile or CSV file containing the obstacle data
    # You can either uncomment the getFileName() function call and implement it to dynamically retrieve the filename,
    # or manually specify the filename as a string
    filename = "Valencia1.csv"

    # Print a message to indicate that the shapefile is being read
    print("Reading shapeFile")

    # Use the pandas library to read the CSV file into a DataFrame object
    df = pd.read_csv(filename, delimiter=',')

    # Sort the DataFrame by the 'osm_id' column in ascending order
    df = df.sort_values(by=['osm_id'])

    # Return the sorted DataFrame
    return df

def print_header(f):
	f.write("<environment>\n")
	f.write("<material id=\"1\" resistivity=\"100\" relativePermittivity=\"4.5\" relativePermeability=\"1\" /> <!-- concrete-->\n")

def print_footer(f):
	f.write("\n</environment>")
	

def get_building(buildingId):
    # Retrieve the data for a specific building based on its ID
    # The buildingId parameter represents the ID of the building to retrieve
    # The function filters the dataframe to select rows where the 'osm_id' column matches the provided buildingId

    building = df.loc[df['osm_id'] == buildingId]

    # The resulting dataframe called 'building' contains the data for the specific building

    # Identify any duplicated rows based on the 'startX', 'startY', 'endX', and 'endY' columns
    duplicatedRows = building[building.duplicated(['startX','startY','endX','endY'])]

    # Remove the duplicated rows from the 'building' dataframe
    # The '~' operator negates the condition to keep only the non-duplicated rows
    # The .dropna() function removes any rows with missing values
    building = building[~building.isin(duplicatedRows)].dropna()

    # Reset the index of the 'building' dataframe to have a new index
    building = building.reset_index(drop=True)

    # The 'building' dataframe now contains the clean data for the specific building
    # This dataframe can be used for further processing or analysis

    return building

def make_wall(wall, height):
	# in omnet a wall is rotated in its center
	# so starting from the start and end point
	# we must calculate its length (widht always 1)
	# the angle of rotation
	# and the displacement (offset) due to the rotation to correct
    
    # Convert the start and end points of the wall from geographic coordinates to UTM coordinates
    start_UTMx, start_UTMy = converter(wall['startX'], wall['startY'])
    end_UTMx, end_UTMy = converter(wall['endX'], wall['endY'])

    # Calculate the displacement (offset) of the wall from the center of the area of interest
    x1 = start_UTMx - centerX
    y1 = start_UTMy - centerY
    x2 = end_UTMx - centerX
    y2 = end_UTMy - centerY

    # Calculate the change in x and y coordinates (dx, dy) between the start and end points
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the length of the wall using the Euclidean distance formula
    length = math.sqrt(dx ** 2 + dy ** 2)

    # Calculate the angle of rotation for the wall
    # The negative sign is used because in OMNeT++, rotation is clockwise (unlike the usual counter-clockwise)
    angle = -math.atan2(dy, dx)

    # Calculate the offset in x and y coordinates due to the rotation
    offsetX = -(1 - math.cos(angle)) * length / 2
    offsetY = -math.sin(angle) * length / 2

    # Calculate the final position of the wall by applying the offset to the start point
    posx = round((x1 + offsetX) * 100) / 100
    posy = round((y1 + offsetY) * 100) / 100

    # Round the angle and length values to two decimal places
    angle = -round(math.degrees(angle) * 100) / 100
    length = round(length * 100) / 100

    # Print or use the calculated values for further processing
    # print_wall(posx, posy, angle, length, 5, height)
    print_wall(posx,posy,angle,length,10,height)




def print_wall(posx, posy, angle, length, width, height):
    # Write the opening tag for the wall object in the XML file
    f.write("<object ")

    # Write the position attribute of the wall object, specifying its x, y, and z coordinates
    f.write("position=\"min " + str(-posx) + " " + str(-posy) + " 0\" ")

    # Write the orientation attribute of the wall object, specifying its rotation along the x, y, and z axes
    f.write("orientation=\"" + str(angle) + " 0 0\" ")
    # f.write("orientation=\"" + "0 0 0\" ")

    # Write the shape attribute of the wall object, specifying its dimensions as a cuboid
    f.write("shape=\"cuboid ")
    f.write(" " + str(-length) + " " + str(width) + " " + str(height))

    # Write the material attribute of the wall object
    f.write("\" material=\"1\" /> \n")




if __name__ == "__main__":
    # Initialize the dataframe by reading the CSV file and sorting it by 'osm_id'
    df = init_df()
    
    # Set up the coordinate converter using the UTM zone 30 and WGS84 ellipsoid
    converter = Proj(proj='utm', zone=30, ellps='WGS84', preserve_units=False)
    
    # Define the center coordinates of the area of interest

    #UPV
    centerX = 728094.82
    centerY = 4372199.89

	# # Madrid
    # centerX = 435684.80
    # centerY = 4471112.47

    # Open the XML file for writing
    f = open("Valencia1.xml", "w")
    
    # Write the XML file header
    print_header(f)
    
    # Get the unique building IDs from the dataframe
    buildingIds = df['osm_id'].drop_duplicates()
    
    # Iterate over each building ID
    for buildingId in buildingIds:
        # Retrieve the building data for the current building ID
        building = get_building(buildingId)
        
        # Iterate over each wall in the building
        height = generate_height()     #   For UPV
        for index, wall in building.iterrows():
            # Create the wall based on its start and end points
            make_wall(wall, height)
    
    # Write the XML file footer
    print_footer(f)
    
    # Close the XML file
    f.close()
    
    # Print a completion message
    print("done!\n")