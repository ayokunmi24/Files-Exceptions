import csv

infile = 'sales.csv'
outfile = 'salesreportFINAL.csv'


with open(infile, 'r') as csv_in, open(outfile, 'w', newline='') as csv_out:
    csv_reader = csv.reader(csv_in)
    csv_writer = csv.writer(csv_out)

    next(csv_reader)  # Skip header row
    csv_writer.writerow(['CustomerID', 'Total'])

    for row in csv_reader:
        customer_id = row[0]
        subtotal = float(row[3])
        tax = float(row[4])
        freight = float(row[5])
        total = subtotal + tax + freight
        
        csv_writer.writerow([customer_id, f"{total:.2f}"])
    