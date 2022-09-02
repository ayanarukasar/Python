import csv

with open('csv_read/student.csv', 'r') as file:
    my_reader = csv.reader(file)
    for row in my_reader:
        print(row)