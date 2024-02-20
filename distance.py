import csv
import math

def calculate_distance(uav1_coords, uav2_coords):
    x1, y1 = uav1_coords
    x2, y2 = uav2_coords
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        coordinates = [(float(row[0]), float(row[1])) for row in reader]
    return coordinates

# Specify the file paths for the two CSV files
file1 = 'City_Profiles/Valencia/20_m/20_m_0_path_test.csv'
file2 = 'City_Profiles/Valencia/20_m/20_m_3_path_test.csv'

# Read the coordinates from the CSV files
uav1_coordinates = read_csv_file(file1)
uav2_coordinates = read_csv_file(file2)

# Calculate the distances between the UAVs
distances = []
for i in range(min(len(uav1_coordinates), len(uav2_coordinates))):
    distance = calculate_distance(uav1_coordinates[i], uav2_coordinates[i])
    distances.append(distance)

# Print the distances
for i, distance in enumerate(distances):
    print(f"Distance between UAV {i+1}: {distance}")