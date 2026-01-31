import csv

employees = open('employee_data.csv', 'r')

csv_file = csv.reader(employees, delimiter=',')
next(csv_file)  # Skip header row

for row in csv_file:
    salary = float(row[3])
    bonus = float(row[7])
    total_pay = salary + (salary * bonus)
    bonus_percentage = bonus * 100

    print ('Employee ID:', row[0])
    print ('Name:', row[1])
    print ('Age:', row[2])
    print (f'Salary: ${float(row[3]):,.2f}')
    print ('Hours Worked:', row[4])
    print ('Productivity:', row[5])
    print ('Team:', row[6])
    print (f'Bonus Rate: {bonus_percentage}%')
    print (f'Total Pay: ${total_pay:,.2f}')
    print ()
    input('Please press enter to continue to the next employee...')