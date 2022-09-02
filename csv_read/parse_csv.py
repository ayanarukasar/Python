import csv

with open('csv_read/test.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        # print(row)
        print(row[1]) #it will print the index 1 value