import os

# Specify the directory where the CSV files are located
directory = 'City_Profiles/Valencia/20_m'

# Loop through the files in the directory
for filename in os.listdir(directory):
    if filename.startswith('20_m_') and filename.endswith('_path_test.csv'):
        # Extract the number from the filename
        number = int(filename.split('_')[2])
        
        # Rename the file
        new_filename = f"20_m_{number+1}_path_test.csv"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))