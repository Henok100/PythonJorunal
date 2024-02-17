import csv

for i in range(6):
    # Define the input and output file paths
    input_file = 'City_Profiles/Valencia/20_m/20_m_{0}_path_test.csv'.format(i)
    output_file = 'City_Profiles/Valencia/60_m/60_m_{0}_path_test.csv'.format(i)

    # Read the input CSV file
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Change each row of the 3rd column (except the header) to 100
    for row in data[1:]:
        row[2] = '60'

    # Write the modified data to the output CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)  