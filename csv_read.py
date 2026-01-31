import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers, delimiter=',')
next(csv_file)  # Skip header row

for row in csv_file:

    print ('First Name:', row[1])
    print ('Last Name:', row[2])
    print ('City:', row[3])
    print ('Country:', row[4])
    print ('Phone Number:', row[5])
    print ()
    input()





