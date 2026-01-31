import csv

infile = 'customers.csv'
outfile = 'customer_country.csv'

total_customer = 0

with open(infile, 'r') as csv_in, open(outfile, 'w', newline='') as csv_out:
    csv_reader = csv.reader(csv_in)
    csv_writer = csv.writer(csv_out)

    # Write header to the output file
    csv_writer.writerow(['Full Name', 'Country'])

    next(csv_reader)  # Skip header row

    for row in csv_reader:
        full_name = row[1] + ' ' + row[2]
        country = row[4]
        csv_writer.writerow([full_name, country])
        total_customer += 1

print(f'Total number customers: {total_customer}')