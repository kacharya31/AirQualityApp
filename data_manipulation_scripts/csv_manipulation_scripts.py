import csv

input_file = 'population.csv'  # replace with your input file name
output_file = 'populationd.csv'  # replace with your desired output file name

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        # Remove 4th and 5th columns (index 3 and 4)
        del row[4]  # Deleting 5th column
        del row[3]  # Deleting 4th column
        writer.writerow(row)

# import csv

# input_file = 'pm2.5.csv'  # Replace with your input file name
# output_file = 'pm2.51.csv'  # Replace with your desired output file name

# with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # Optional: If your CSV file has a header and you want to keep it
#     headers = next(reader)
#     headers.insert(0, 'Index')  # Add 'Index' to the header
#     writer.writerow(headers)

#     for index, row in enumerate(reader, start=1):  # Start indexing from 1 (or 0 if you prefer)
#         row.insert(0, index)  # Add index at the beginning of each row
#         writer.writerow(row)
